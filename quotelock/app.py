from pathlib import Path
import json,base64,hashlib,uuid,io,tempfile,os
from fastapi import FastAPI,HTTPException,Header
from fastapi.responses import HTMLResponse,FileResponse
from pydantic import BaseModel,Field
from PIL import Image
from quotelock.advisor import discover
from quotelock.catalogue import BUNDLES,read,evaluate
from quotelock.quote import Store
from quotelock.kyc import validate_fields,mock_digilocker,mock_esign
from quotelock.kyc.ocr_tesseract import image_ocr,fields_from_documents
from quotelock.orders import lock
from quotelock.tracker import tracker
from quotelock.privacy import Vault,RETENTION,breach_response
ROOT=Path(__file__).resolve().parent.parent
APPDIR=ROOT/'quotelock';(APPDIR/'.data').mkdir(exist_ok=True)
app=FastAPI(title='QuoteLock synthetic evidence prototype')
store=Store(str(APPDIR/'.data/prototype.sqlite'));vault=Vault(store);EVIDENCE={};UPLOADS={}
def session(s):
 if not s or not s.replace('-','').isalnum() or len(s)>80:raise HTTPException(400,'Use an opaque session ID')
 return s
class Preview(BaseModel):
 session:str;segment:str='micro';tier:int=Field(2,ge=1,le=2);employees:int=Field(1,ge=1,le=10000);sites:int=Field(1,ge=1,le=100);language:str='en';intent:str='internet mobile shop';budget:float=Field(2000,gt=0);gstin:str='';bundle:dict[str,int]|None=None
class Consent(BaseModel):session:str;consent:bool
class Accept(BaseModel):session:str;hash:str;charges_known:bool=False
class KYC(BaseModel):session:str;packet:str
class Upload(BaseModel):session:str;kind:str;png_base64:str
class Gates(BaseModel):session:str;serviceability:bool=False;payment_mandate:bool=False;charges_known:bool=False
@app.get('/',response_class=HTMLResponse)
def home():return (APPDIR/'static/index.html').read_text(encoding='utf-8')
@app.get('/architecture-view',response_class=HTMLResponse)
def architecture_view():return (APPDIR/'static/architecture.html').read_text(encoding='utf-8')
@app.get('/api/catalogue')
def catalogue():return {'bundles':BUNDLES,'mocked':True}
@app.get('/api/demo-profile/{persona}')
def demo_profile(persona:str):
 from quotelock.catalogue import GST
 cache=ROOT/'evaluation/ocr_fields.json';candidate=json.loads(cache.read_text()).get('K02',{}).get('gstin') if cache.exists() else None
 return {'gstin':candidate if candidate in GST else next(k for k,v in GST.items() if v['status']=='Active'),'scope':'synthetic demo field; never sent to intent adapter'}
@app.post('/api/preview')
def preview(b:Preview):
 session(b.session)
 profile={'segment':b.segment,'tier':b.tier,'employees':b.employees,'sites':b.sites,'gstin':b.gstin}
 try:r=discover(b.intent,profile,b.budget,b.language,b.bundle)
 except ValueError as e:raise HTTPException(400,str(e))
 if r['status']!='preview':
  store.hold(b.session,'advisor_unclosed','partner','Clarify structured needs; boundary blocked model call');return r
 # Keep opaque business facts needed by the next deterministic recheck; no raw
 # registration identifier is written into the quote database.
 r['profile']={k:v for k,v in profile.items() if k!='gstin'}
 r['identity_hash']=hashlib.sha256(b.gstin.encode()).hexdigest() if b.gstin else None
 r['gst_active_snapshot']=bool(b.gstin and __import__('quotelock.catalogue',fromlist=['GST']).GST.get(b.gstin,{}).get('status')=='Active')
 try:q=store.version(b.session,r)
 except ValueError as e:raise HTTPException(409,str(e))
 store.clear(b.session,'advisor_unclosed')
 for h in r['quote']['holds']:store.hold(b.session,h['code'],h['owner'],h['next_action'])
 if r['route']=='specialist':store.hold(b.session,'specialist_route','specialist','Resolve survey / multi-site prerequisites; review cannot override rules')
 return q
@app.get('/api/session/{sid}')
def current(sid:str):
 c=store.current(session(sid))
 if not c:raise HTTPException(404,'No quote yet')
 return c
@app.post('/api/consent')
def consent(b:Consent):
 session(b.session);store.consent(b.session,b.consent)
 if not b.consent:EVIDENCE.pop(b.session,None)
 return {'consent':b.consent,'purpose':'evidence validation and order continuity','retention_days_by_class':RETENTION,'external_services':'mocked','withdrawal':'processing stopped; legal retention review needed before production'}
@app.post('/api/accept')
def accept(b:Accept):
 c=store.current(session(b.session));e=EVIDENCE.get(b.session,{}).get('result',{})
 if c and not c['payload'].get('identity_hash'):raise HTTPException(409,'Bind the business identity in a fresh quote before acceptance; no-GST alternative evidence remains pending')
 if not c or e.get('status')!='core_checks_clear' or c['payload']['quote']['holds'] or not b.charges_known:raise HTTPException(409,'Resolve evidence, catalogue and mock charge policy before final acceptance')
 try:store.accept(session(b.session),b.hash)
 except ValueError as e:raise HTTPException(409,str(e))
 return mock_esign(True,b.hash)
@app.post('/api/kyc')
def kyc(b:KYC):
 c=store.current(session(b.session))
 if not c or not c['consent']:raise HTTPException(409,'Purpose consent required before evidence')
 cache=ROOT/'evaluation/ocr_fields.json'
 if not cache.exists():raise HTTPException(503,'Run fresh OCR evidence command first')
 fields=json.loads(cache.read_text()).get(b.packet)
 if fields is None:raise HTTPException(404,'Unknown supplied packet')
 result=validate_fields(fields)
 if c['payload'].get('identity_hash') and c['payload']['identity_hash']!=hashlib.sha256(str(fields.get('gstin') or '').encode()).hexdigest():result['status']='hold';result['holds'].append({'code':'identity_binding','owner':'specialist','next_action':'Evidence must match the quoted business identifier'})
 EVIDENCE[b.session]={'result':result,'fields':fields}
 for h in result['holds']:store.hold(b.session,h['code'],h['owner'],h['next_action'])
 vault.put(b.session,'field_receipt',json.dumps(result).encode(),True)
 return {**result,'packet':b.packet,'ocr_source':'fresh Tesseract output; not human fixture','candidate_gstin_masked':('***********'+str(fields.get('gstin',''))[-4:]) if fields.get('gstin') else 'unreadable','digilocker':mock_digilocker(True,hashlib.sha256(json.dumps(result).encode()).hexdigest())}
@app.post('/api/kyc/upload')
def upload(b:Upload):
 c=store.current(session(b.session))
 if not c or not c['consent']:raise HTTPException(409,'Purpose consent required')
 if b.kind not in ['gst_certificate','udyam_certificate','signatory_id','address_proof']:raise HTTPException(400,'Unknown document class')
 try:
  data=base64.b64decode(b.png_base64,validate=True)
  if len(data)>12_000_000:raise ValueError('Image exceeds12MB')
  im=Image.open(io.BytesIO(data));im.verify()
 except Exception:raise HTTPException(400,'Upload a valid PNG/JPEG under12MB')
 vault.put(b.session,'raw_upload',data,True)
 tmp=APPDIR/'.data'/('upload-'+uuid.uuid4().hex+'.png')
 try:
  Image.open(io.BytesIO(data)).convert('RGB').save(tmp)
  try:ocr=image_ocr(tmp)
  except RuntimeError as exc:raise HTTPException(503,str(exc))
 finally:tmp.unlink(missing_ok=True)
 UPLOADS.setdefault(b.session,{})[b.kind]={**ocr,'full_text':ocr['text']}
 fields=fields_from_documents(UPLOADS[b.session]);result=validate_fields(fields)
 if c['payload'].get('identity_hash') and c['payload']['identity_hash']!=hashlib.sha256(str(fields.get('gstin') or '').encode()).hexdigest():result['status']='hold';result['holds'].append({'code':'identity_binding','owner':'specialist','next_action':'Confirm quoted business against uploaded evidence'})
 EVIDENCE[b.session]={'result':result,'fields':fields}
 for h in result['holds']:store.hold(b.session,h['code'],h['owner'],h['next_action'])
 return {'status':result['status'],'holds':result['holds'],'kind':b.kind,'character_count':len(ocr['text']),'mocked':True,'raw_text_exposed':False,'next_action':'Complete and resolve the packet before lock'}
@app.post('/api/lock')
def order_lock(b:Gates):
 session(b.session)
 evidence=EVIDENCE.get(b.session,{});result=evidence.get('result',{});c=store.current(b.session)
 if c and not c['payload'].get('identity_hash'):result={'status':'hold'}
 if c and result.get('status')=='core_checks_clear':
  p={**c['payload']['profile'],'gstin':evidence.get('fields',{}).get('gstin') or ''};bundle={x['product_id']:x['quantity'] for x in c['payload']['quote']['lines']}
  if evaluate(bundle,p)['holds']:result={'status':'hold'}
 try:return lock(store,b.session,result.get('status')=='core_checks_clear',b.serviceability,b.payment_mandate,b.charges_known,c.get('accepted',False))
 except (ValueError,AttributeError) as e:raise HTTPException(409,'No current quote / gate failure')
@app.get('/api/tracker/{sid}')
def track(sid:str):
 c=store.current(session(sid))
 if not c:raise HTTPException(404,'No quote')
 return tracker(c['payload']['quote'],bool(store.db.execute('SELECT 1 FROM locks WHERE session=?',(sid,)).fetchone()))
@app.get('/api/queue')
def queue(x_demo_role:str=Header('partner')):
 try:return {'role':x_demo_role,'items':store.queue(x_demo_role),'access':'demo role filter only; production authentication not implemented','mocked':True}
 except ValueError as e:raise HTTPException(403,str(e))
@app.get('/api/architecture')
def architecture():return json.loads((APPDIR/'architecture.json').read_text())
@app.get('/api/privacy')
def privacy():return {'retention':RETENTION,'incident':breach_response(),'storage':'Fernet authenticated encryption; ephemeral process key, production key management not implemented'}
