"""Reproduce measured synthetic evidence. No performance result is hard-coded."""
from pathlib import Path
import json,time,statistics,re,hashlib,datetime,sys
from fastapi.testclient import TestClient
import quotelock.app as appmod
from quotelock.quote import Store
from quotelock.privacy import Vault
from quotelock.kyc import validate_fields,norm
from quotelock.boundary import redact,IntentAdapter
from quotelock.tests.test_core import boundary_cases
from quotelock.demo import run
from quotelock.catalogue import read,evaluate
ROOT=Path(__file__).resolve().parent.parent;OUT=ROOT/'evaluation'
def main():
 appmod.store=Store();appmod.vault=Vault(appmod.store);appmod.EVIDENCE={}
 client=TestClient(appmod.app);fields=json.loads((OUT/'ocr_fields.json').read_text());gt=json.loads((ROOT/'quotelock/kyc/fixtures/ground_truth.json').read_text())['packets']
 per_field={k:{'correct':0,'n':0} for k in ['gstin','udyam','legal','address','bill_date','signatory','valid_till','udyam_date','activity']}
 kr=[];unsafe=fp=correct=0
 for p in gt:
  k=p['packet'];actual=validate_fields(fields[k]);human=validate_fields(p['fields']);expected=p['expected_status'];correct+=actual['status']==expected;unsafe+=actual['status']=='core_checks_clear' and expected=='hold';fp+=actual['status']=='hold' and expected=='core_checks_clear'
  kr.append({'packet':k,'expected_team_label':expected,'auto_status':actual['status'],'human_confirmed_core_status':human['status'],'holds':[x['code'] for x in actual['holds']],'advisories':actual['advisories']})
  for key in per_field:
   truth=p['fields'].get(key)
   if truth:
    per_field[key]['n']+=1;per_field[key]['correct']+=norm(fields[k].get(key))==norm(truth)
 for k in per_field:per_field[k]['accuracy_pct']=per_field[k]['correct']/per_field[k]['n']*100
 trials=[];adapter=IntentAdapter();blocked=leaks=0
 oracle=re.compile(r'\d|[₹$@]|UDYAM|GSTIN|\b(?:lakh|hazaar|thousand|inr|rs)\b',re.I)
 for i,text in enumerate(boundary_cases()):
  r=redact(text);blocked+=r['blocked']
  if not r['blocked']:
   adapter.extract(r['payload']);leaks+=bool(oracle.search(adapter.received[-1]))
  trials.append({'id':i,'input_sha256':hashlib.sha256(text.encode()).hexdigest(),'blocked':r['blocked'],'adapter_payload':r['payload']})
 scenarios=[('micro','en','internet mobile shop',1,1,'no_gst_starter'),('micro','hi','मुझे इंटरनेट मोबाइल दुकान चाहिए',1,1,'no_gst_starter'),('professional','en','internet backup email security clinic',5,1,'routine_gst'),('professional','hi','इंटरनेट बैकअप ईमेल क्लिनिक',5,1,'routine_gst'),('multisite','en','internet backup multisite',10,3,'specialist'),('multisite','hi','इंटरनेट बैकअप',10,3,'specialist'),('manufacturer','en','internet security factory',10,1,'specialist'),('manufacturer','hi','इंटरनेट सुरक्षा कारखाना',10,1,'specialist'),('micro','en','internet unknownperson',1,1,'clarify'),('micro','hi','इंटरनेट अज्ञात',1,1,'clarify'),('professional','en','internet',1,1,'routine_gst'),('micro','en','internet budget ₹1500',1,1,'no_gst_starter'),('micro','hi','मुझे इंटरनेट १५०० रुपये चाहिए',1,1,'no_gst_starter'),('multisite','en','internet',10,1,'specialist'),('manufacturer','en','internet',1,1,'specialist')]
 sr=[]
 for i,(seg,lang,intent,emp,sites,expected) in enumerate(scenarios):
  r=client.post('/api/preview',json={'session':'scenario-'+str(i),'segment':seg,'language':lang,'intent':intent,'employees':emp,'sites':sites,'budget':50000,'gstin':fields['K02']['gstin'] if seg!='micro' else ''}).json()
  observed='clarify' if r.get('status')=='clarify' else r['payload']['route'];sr.append({'id':i+1,'segment':seg,'language':lang,'expected':expected,'observed':observed,'pass':expected==observed})
 timings=[]
 for i in range(100):
  start=time.perf_counter_ns();r=client.post('/api/preview',json={'session':'timed-'+str(i),'segment':'professional' if i%2 else 'micro','employees':5 if i%2 else 1,'sites':1,'intent':'internet email' if i%2 else 'मुझे इंटरनेट चाहिए','language':'en' if i%2 else 'hi','budget':5000,'gstin':fields['K02']['gstin'] if i%2 else ''});end=time.perf_counter_ns()
  if r.status_code!=200 or 'payload' not in r.json():raise AssertionError(r.text)
  timings.append((end-start)/1e6)
 s='version-evidence';r=client.post('/api/preview',json={'session':s,'segment':'micro','employees':1,'sites':1,'intent':'internet shop','budget':2000,'bundle':{'P04':1}}).json();q2=client.post('/api/preview',json={'session':s,'segment':'micro','employees':1,'sites':1,'intent':'internet shop','budget':2000,'bundle':{'P04':1,'P07':1}}).json()
 personas=run(client,'evidence')
 for p in personas:
  exists=bool(appmod.store.db.execute('SELECT 1 FROM locks WHERE session=?',(p['session'],)).fetchone())
  p['durable_lock_recorded']=exists
  if p['outcome']=='order_locked':assert exists
 historical=read('smb_leads.csv');activated=[r for r in historical if r['outcome']=='Activated'];rule_conflicts=set();gst_failures=set()
 for row in activated:
  basket={part.split('x')[0]:int(part.split('x')[1]) for part in row['bundle_products'].split(';')}
  profile={'tier':int(row['city_tier']),'employees':int(row['employee_count']),'sites':int(row['num_sites']),'gstin':row['gstin']}
  holds=evaluate(basket,profile)['holds']
  if holds:rule_conflicts.add(row['lead_id'])
  if any(h['code']=='catalogue_gst' for h in holds):gst_failures.add(row['lead_id'])
 receipt={'scope':'V-proto: scripted synthetic API sessions, not user research, customer latency, field pilot or an LLM benchmark','generated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'T1_boundary':{'trials':len(trials),'model_slot_calls':len(adapter.received),'blocked':blocked,'blocked_pct':blocked/len(trials)*100,'leaks':leaks,'method':'Seed8621,420 generated English/Hindi/Hinglish utterances; independent regex leak oracle; deterministic stand-in adapter'},'T2_kyc':{'documents':len(list((ROOT/'YTL_TrackA_Udyam_Digital_Data/kyc_documents').glob('*.png'))),'packets':len(kr),'auto_clear':sum(x['auto_status']=='core_checks_clear' for x in kr),'auto_hold':sum(x['auto_status']=='hold' for x in kr),'team_confirmed_clear':sum(x['human_confirmed_core_status']=='core_checks_clear' for x in kr),'team_confirmed_hold':sum(x['human_confirmed_core_status']=='hold' for x in kr),'classification_agreement':correct,'false_passes':unsafe,'false_holds':fp,'per_field':per_field,'packets_table':kr,'core_policy':'CORE-v4; date/activity differences advisory by explicit policy; exact identifier mismatch remains blocking'},'T3_quote_time':{'n':len(timings),'median_ms':statistics.median(timings),'p90_ms':sorted(timings)[89],'min_ms':min(timings),'max_ms':max(timings),'scope':'TestClient HTTP request to priced, persisted quote; already completed structured facts; includes rules/boundary/DB; excludes typing, user reading, OCR, real LLM/network/install'},'T4_version':{'v1':r['version'],'v1_monthly':r['payload']['quote']['monthly'],'v2':q2['version'],'v2_monthly':q2['payload']['quote']['monthly'],'hash_changed':r['hash']!=q2['hash'],'fresh_acceptance':not q2['accepted']},'T5_advisor':{'scenarios':len(sr),'passed':sum(x['pass'] for x in sr),'rows':sr,'scope':'Team-written scenario set, not the hidden judges pack'},'T6_personas':personas,'T7_rules':{'historical_records':len(activated),'conflicts':len(rule_conflicts),'gst_failures':len(gst_failures),'source':'pytest historical replay through the prototype engine + analysis/numbers.json'}}
 (OUT/'prototype_evidence.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');(OUT/'boundary_trials.json').write_text(json.dumps(trials,indent=2),encoding='utf-8')
 lines=['# Measured prototype evidence','',receipt['scope'],'','Command: `$env:PYTHONPATH="quotelock/vendor"; python -m evaluation.measure`','', 'Tests command: `python -m pytest analysis/test_numbers.py quotelock/tests -q -p no:cacheprovider --junitxml=evaluation/pytest.xml`','']
 for k,v in receipt.items():
  if k.startswith('T'):lines+=['## '+k,'```json',json.dumps(v,indent=2),'```','']
 lines+=['## OCR reproduction','`python -m quotelock.kyc.prepare` then `python -m quotelock.kyc.ocr_tesseract`','Original images are unchanged. Tesseract5.5.3 English fast data; OpenCV deskew; whole-page label parser. Team visual fixtures are excluded from runtime extraction. No classifier result is corrected to match the supplied expectation.','', '## Limitations','No independent humans or real customers were tested. Zero leaks refers only to generated payload tests, not a universal privacy guarantee. Role filtering lacks production authentication; ephemeral-key encryption lacks production key management. Serviceability, payment mandate, DigiLocker and e-sign remain explicitly mocked.']
 (OUT/'prototype_evidence.md').write_text('\n'.join(lines),encoding='utf-8')
 print(json.dumps({k:v for k,v in receipt.items() if k in ['T1_boundary','T3_quote_time','T4_version','T5_advisor']},indent=2))
 print('KYC',receipt['T2_kyc']['auto_clear'],'clear /',receipt['T2_kyc']['auto_hold'],'hold; false holds',fp,'false passes',unsafe)
if __name__=='__main__':main()
