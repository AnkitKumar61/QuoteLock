"""Recompute QuoteLock's supplied-data facts and explicitly conditional projections."""
from pathlib import Path
import sys
# Avoid shadowing the standard-library numbers module when launched as a path.
if sys.path and Path(sys.path[0]).resolve()==Path(__file__).resolve().parent:sys.path.pop(0)
import csv,json,hashlib,math,statistics,zipfile,xml.etree.ElementTree as ET
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parent.parent
D=ROOT/'YTL_TrackA_Udyam_Digital_Data'
OUT=ROOT/'analysis'
def rows(n):
 with (D/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def power(p,d,n):
 q=p+d;b=(p+q)/2;c=1.95996398454*math.sqrt(2*b*(1-b)/n);se=math.sqrt((p*(1-p)+q*(1-q))/n)
 F=lambda x:(1+math.erf(x/math.sqrt(2)))/2
 return 1-F((c-d)/se)+F((-c-d)/se)
def sample(p,d):
 lo,hi=1,100000
 while lo<hi:
  m=(lo+hi)//2
  if power(p,d,m)>=.8:hi=m
  else:lo=m+1
 return lo
def compute():
 leads=rows('smb_leads.csv');cat={r['product_id']:r for r in rows('product_catalogue.csv')};gst={r['gstin']:r for r in rows('mock_gstin_registry.csv')}
 N={}
 def add(k,v,f,source='smb_leads.csv',label='V',basis=None):
  N[k]={'key':k,'value':v,'formula':f,'source':source,'label':label}
  if basis:N[k]['basis']=basis
 def cost(g):return sum(float(r['acquisition_cost_inr']) for r in g)
 def acts(g):return [r for r in g if r['outcome']=='Activated']
 def mrr(g):return sum(float(r['monthly_bundle_value_inr']) for r in acts(g))
 stages=['Lead','Contacted','Needs assessed','Quote accepted','KYC complete','Activated']
 for st in stages:add('funnel.'+st,sum(stages.index(r['stage_reached'])>=stages.index(st) for r in leads),'count stage_reached >= '+st)
 active=acts(leads);C0=cost(leads);M0=mrr(leads)
 for k,v,f in [('leads',len(leads),'count all'),('activations',len(active),'count Activated'),('cost',C0,'sum acquisition costs, all leads'),('mrr',M0,'sum activated monthly value'),('cac',C0/len(active),'cost/activations'),('payback',C0/M0,'cost/MRR'),('conversion',len(active)/len(leads)*100,'activated/all leads*100'),('quote_conversion',len(active)/861*100,'368/861*100'),('prequote_loss',1974-861,'needs assessed - quote accepted'),('needs_quote_conversion',861/1974*100,'861/1974*100'),('postquote_loss',861-368,'quote accepted - activated'),('days_mean',statistics.mean(float(r['days_lead_to_activation']) for r in active),'mean days_lead_to_activation'),('calls_mean',statistics.mean(float(r['customer_follow_up_calls']) for r in active),'mean activated follow-up calls; window unspecified'),('churn_flags',sum(r['churned_within_6_months']=='Y' for r in active),'count synthetic flag Y'),('churn_pct',sum(r['churned_within_6_months']=='Y' for r in active)/len(active)*100,'flags/activated*100, not matured'),('future_activations',sum(r['activated_date']>'2026-07-15' for r in active),'count activated after case date'),('within30',sum(float(r['days_lead_to_activation'])<=30 for r in active),'count lead-to-activation <=30 days'),('days_max',max(float(r['days_lead_to_activation']) for r in active),'max supplied lead-to-activation')]:add('baseline.'+k,v,f)
 add('baseline.six_month_matured',0,'earliest activation Apr13 +6 calendar months >Jul15')
 segs={'micro':'Micro retail & services','professional':'Professional offices','multisite':'Small multi-site businesses','manufacturer':'Small manufacturers'}
 reasons={r['drop_reason'] for r in leads if r['drop_reason']}
 for r in reasons:add('reason.'+r,sum(x['drop_reason']==r for x in leads),'count exact drop_reason')
 pools={'visit':['Owner had no time for a visit','Visit not scheduled by sales'],'quote':['Quote too complex to understand','Quote took too long to arrive'],'price':['Price too high','Competitor offered cheaper plan']}
 segment={}
 for key,name in segs.items():
  g=[r for r in leads if r['segment']==name];a=acts(g);q=sum(bool(r['quote_accepted_date']) for r in g)
  segment[key]={'n':len(g),'a':len(a),'q':q,'cost':cost(g),'mrr':mrr(g),'proxy':cost(a)/len(a),'churn':sum(r['churned_within_6_months']=='Y' for r in a)/len(a),'calls':statistics.mean(float(r['customer_follow_up_calls']) for r in a)}
  b=segment[key]
  for k,v in {'leads':len(g),'activations':len(a),'quotes':q,'cac':cost(g)/len(a),'arpu':mrr(g)/len(a),'payback':cost(g)/mrr(g),'conversion':len(a)/len(g)*100,'lead_share':len(g)/5000*100,'proxy':b['proxy']}.items():add(f'segment.{key}.{k}',v,'same-segment raw rows: '+k)
  for pk,rr in pools.items():add(f'pool.{pk}.{key}',sum(r['drop_reason'] in rr for r in g),'count exact stage-specific reason set '+str(rr))
 for pk,rr in pools.items():add('pool.'+pk,sum(r['drop_reason'] in rr for r in leads),'sum exact disjoint reasons within stage')
 for flag in ['Y','N']:
  g=[r for r in leads if r['has_gstin']==flag];add('gst.activation.'+flag,len(acts(g))/len(g)*100,'activations/has_gstin='+flag)
 micro=[r for r in leads if r['segment']==segs['micro']]
 for k,v in [('no_gst',sum(r['has_gstin']=='N' for r in micro)),('no_gst_no_udyam',sum(r['has_gstin']=='N' and r['has_udyam']=='N' for r in micro))]:add('micro.'+k,v,'count flags in Micro')
 cheap=[r for r in micro if r['lead_source'] in ['Website form','WhatsApp campaign','Inbound call','Referral']]
 for k,v in {'leads':len(cheap),'activations':len(acts(cheap)),'cac':cost(cheap)/len(acts(cheap)),'conversion':len(acts(cheap))/len(cheap)*100}.items():add('matched_micro.'+k,v,'four-channel Micro-only subset: '+k)
 add('channels.field_partner_spend_pct',cost([r for r in leads if r['lead_source'] in ['Field sales','Channel partner']])/C0*100,'field+partner acquisition cost/total; no activity attribution')
 for lang,n in Counter(r['preferred_language'] for r in leads).items():add('language.'+lang,n,'count preferred_language');add('language_pct.'+lang,n/5000*100,'preferred_language/5000*100')
 add('language.non_english_pct',sum(r['preferred_language']!='English' for r in leads)/5000*100,'non-English preference/5000*100')
 bad={};categories=defaultdict(set)
 for r in active:
  ids={x.split('x')[0] for x in r['bundle_products'].split(';')}
  for p in ids:
   c=cat[p];flags=[]
   if r['city_tier'] not in c['available_city_tiers'].split(';'):flags.append('tier')
   if int(r['employee_count'])<int(c['min_employees']):flags.append('employees')
   if int(r['num_sites'])<int(c['min_sites']):flags.append('sites')
   if c['requires_one_of'] and not ids&set(c['requires_one_of'].split('|')):flags.append('dependency')
   if c['requires_gstin']=='Y' and gst.get(r['gstin'],{}).get('status')!='Active':flags.append('gst')
   for f in flags:categories[f].add(r['lead_id'])
   if flags:bad.setdefault(r['lead_id'],[]).extend(flags)
 add('rules.union',len(bad),'distinct activated lead IDs with >=1 supplied hard-rule conflict','product_catalogue.csv + mock_gstin_registry.csv + smb_leads.csv')
 for k,ids in categories.items():add('rules.'+k,len(ids),'distinct affected lead IDs; categories overlap')
 bad_mrr=sum(float(r['monthly_bundle_value_inr']) for r in active if r['lead_id'] in bad);add('rules.mrr',bad_mrr,'recorded MRR of rule-conflicting rows')
 bundles={'professional':{'P02':1,'P09':1,'P16':5,'P20':5},'micro':{'P04':1,'P07':1},'multisite':{'P02':3,'P09':3,'P10':3},'manufacturer':{'P05':1,'P21':1,'P24':10}}
 for name,b in bundles.items():
  lo=sum(float(cat[p]['price_min_inr_per_month'])*q for p,q in b.items());hi=sum(float(cat[p]['price_max_inr_per_month'])*q for p,q in b.items());mid=(lo+hi)/2
  for k,v in {'min':lo,'max':hi,'mid':mid,'setup':sum(float(cat[p]['one_time_setup_inr'])*q for p,q in b.items()),'term':max(int(cat[p]['min_contract_months']) for p in b)}.items():add('bundle.'+name+'.'+k,v,'sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max','product_catalogue.csv','V' if k in ['min','max'] else 'A','Versioned illustrative pre-tax policy, no discounts; unknown taxes/charges block final lock')
  clean=[r for r in active if r['segment']==segs[name] and r['lead_id'] not in bad]
  segment[name]['clean_arpu']=sum(float(r['monthly_bundle_value_inr']) for r in clean)/len(clean)
  add('segment.'+name+'.clean_arpu',segment[name]['clean_arpu'],'mean monthly value, no detected supplied-rule conflict')
 for sku,c in cat.items():add('typical_days.'+sku,int(c['typical_install_days']),'source typical_install_days, not a guarantee','product_catalogue.csv')
 for h in [6,12,24]:add('micro.ceiling.'+str(h),1348*h,'1348*'+str(h)+' constant months revenue','catalogue midpoint + policy','P','Revenue coverage excludes service costs, margin, churn, collection')
 add('micro.starter_payback',segment['micro']['cost']/segment['micro']['a']/1348,'historical Micro CAC/1348',label='P')
 add('micro.headroom',8088-N['matched_micro.cac']['value'],'8088-matched Micro CAC',label='P')
 scenarios={};core_n=segment['micro']['n']+segment['professional']['n']
 for name,d1,d2,dc,df,dig,phy in [('Low',.01,.03,0,0,45,60),('Base',.02,.06,.02,.5,70,75),('High',.03,.09,.04,1,85,85)]:
  A=Q=delta_mrr=starter_mrr=handling=churn=calls=0;details={}
  for sk,b in segment.items():
   core=sk in ['micro','professional'];q=b['n']*(b['q']/b['n']+(d1 if core else 0));a=q*(b['a']/b['q']+(d2 if core else 0));da=a-b['a'];A+=a;Q+=q
   delta_mrr+=da*b['clean_arpu'];starter_mrr+=da*N['bundle.'+sk+'.mid']['value'];handling+=max(0,da)*b['proxy'];churn+=a*max(0,b['churn']-(dc if core else 0));calls+=a*max(0,b['calls']-(df if core else 0))
   details[sk]={'delta_a':da,'a':a}
   add(f'model.{name}.{sk}.delta_a',da,'n*(q/n+d1)*(a/q+d2)-a; uplift only core',label='P')
  program=50*core_n;C=C0+handling+program
  z={'activations':A,'quotes':Q,'delta_a':A-368,'delta_mrr':delta_mrr,'starter_delta_mrr':starter_mrr,'handling':handling,'program':program,'added_cost':handling+program,'cost':C,'cac':C/A,'payback':C/(M0+delta_mrr),'conversion':A/5000*100,'quote_conversion':A/Q*100,'churn':churn/A*100,'calls':calls/A,'digital':dig,'physical':phy,'marginal':(handling+program)/(A-368),'stress_a':A-56,'stress_cac':C/(A-56),'stress_payback':C/(M0+delta_mrr-bad_mrr),'program_break_even':A*(C0/368)-C0-handling}
  scenarios[name]=z
  for k,v in z.items():add(f'model.{name}.{k}',v,'unchanged Phase3 formulas; see model output definition '+k,'raw CSVs + scenario assumptions','P','Core d1/d2='+str((d1,d2))+'; same-segment clean ARPU, activated-row cost proxy; retained baseline value')
  if name=='Base':base_details=details
 b=scenarios['Base']
 for spend in [200000,500000,b['program_break_even'],1000000,2000000]:
  k=str(round(spend));c=C0+b['handling']+spend
  add('sensitivity.cac.'+k,c/b['activations'],'(C0+handling+program)/Base A',label='P');add('sensitivity.payback.'+k,c/(M0+b['delta_mrr']),'cost/(baseline MRR+clean ARPU delta)',label='P')
 for cohort in range(1,5):
  for basis,v in [('history',b['delta_mrr']),('starter',b['starter_delta_mrr'])]:add(f'run_rate.{basis}.{cohort}',cohort*v,'cohorts*incremental MRR, no churn; not collected ARR',label='P')
 cross={}
 for sk in ['micro','professional']:
  z=segment[sk];rq=N[f'pool.quote.{sk}']['value'];rv=N[f'pool.visit.{sk}']['value'];da=base_details[sk]['delta_a'];qa=z['a']/z['q'];nq=z['n']*.02;stage_extra=(z['q']+nq)*.06
  quote_share=nq/rq;postshare=stage_extra/((z['q']-z['a']))
  # Alternative attributable mechanism model: equal assumed recovery share across
  # disjoint visit and quote pools, at observed downstream activation probability.
  downstream_visit=z['a']/sum(r['segment']==segs[sk] and stages.index(r['stage_reached'])>=1 for r in leads)
  downstream_quote=z['a']/sum(r['segment']==segs[sk] and stages.index(r['stage_reached'])>=2 for r in leads)
  capacity=rv*downstream_visit+rq*downstream_quote;share=da/capacity
  cross[sk]={'base_added_a':da,'extra_accepted_quotes':nq,'implied_quote_pool_recovery':quote_share,'implied_postquote_recovery':postshare,'visit_pool':rv,'quote_pool':rq,'visit_downstream_activation':downstream_visit,'quote_downstream_activation':downstream_quote,'equal_pool_recovery_to_match_base':share,'alternative_added_a_at_20pct':.2*capacity}
  for k,v in cross[sk].items():add('reason_crosscheck.'+sk+'.'+k,v,'explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence',label='V' if k in ['visit_pool','quote_pool','visit_downstream_activation','quote_downstream_activation'] else 'P')
 p_tier=sum(quota/1200*len(acts([r for r in leads if r['segment']==segs[sk] and r['city_tier']==tier]))/len([r for r in leads if r['segment']==segs[sk] and r['city_tier']==tier]) for sk,tier,quota in [('micro','1',428),('micro','2',394),('professional','1',194),('professional','2',184)])
 p_segment=(822*(110/2709)+378*(138/1247))/1200
 add('pilot.p0_tier',p_tier,'original four stratum quotas /1200',label='P');add('pilot.p0_segment',p_segment,'822/1200*110/2709 +378/1200*138/1247',label='P')
 lo,hi=0.,.2
 for _ in range(80):
  m=(lo+hi)/2
  if power(p_tier,m,600)>=.8:hi=m
  else:lo=m
 add('pilot.mde_pp',hi*100,'normal two-proportion alpha .05 n600/arm target .8',label='P')
 lift=(b['activations']-120)/core_n-p_tier
 add('pilot.base_lift_pp',lift*100,'Base core activation rate - weighted planning control',label='P');add('pilot.base_power_pct',power(p_tier,lift,600)*100,'same approximate power at Base core effect',label='P')
 for name,p in [('core',p_tier),('professional',138/1247),('core_segment',p_segment)]:
  for delta in [.01,.02]:add(f'pilot.n.{name}.{delta}',sample(p,delta),'smallest integer n/arm with normal approximate power>=.8; no clustering/attrition adjustment',label='P')
 for k,v in {'pilot.n_total':1200,'pilot.n_arm':600,'pilot.micro':822,'pilot.professional':378,'pilot.days':90,'pilot.window':30,'pilot.digital_gate':70,'pilot.log_gate':95,'pilot.unsafe':0,'micro.cac_gate':8088,'model.program_per_core_lead':50,'model.core_n':core_n,'model.setup':100000}.items():add(k,v,'retained v2 planning design','analysis/baseline/03_pilot_design.json + v2','A','Proposed, not achieved')
 add('case.quote_days_min',3,'case PDF p2','Airtel_SYNC_Case.pdf p2','V');add('case.quote_days_max',5,'case PDF p2','Airtel_SYNC_Case.pdf p2','V')
 # Explicit visible planning quantities, kept separate from observed outcomes.
 add('pool.kyc_paperwork',N['funnel.Quote accepted']['value']-N['funnel.KYC complete']['value'],'quote accepted minus KYC complete')
 add('pool.fulfilment_payment',N['funnel.KYC complete']['value']-N['funnel.Activated']['value'],'KYC complete minus activated')
 for sk,employees,sites in [('professional',5,1),('micro',1,1),('multisite',10,3),('manufacturer',10,1)]:
  for k,v in [('tier',2),('employees',employees),('sites',sites)]:add(f'assumption.bundle.{sk}.{k}',v,'illustrative eligible profile, checked against supplied catalogue','catalogue + explicit bundle choice','A')
  for sku,quantity in bundles[sk].items():add(f'assumption.bundle.{sk}.quantity.{sku}',quantity,'chosen SKU quantity; price arithmetic uses this same quantity','catalogue + explicit bundle choice','A')
 for scenario,d1,d2,churn,calls in [('Low',1,3,0,0),('Base',2,6,2,.5),('High',3,9,4,1)]:
  for k,v in [('acceptance_uplift_pp',d1),('activation_uplift_pp',d2),('churn_cut_pp',churn),('call_cut',calls)]:add(f'assumption.model.{scenario}.{k}',v,'retained v2 scenario parameter, core segments only','analysis/baseline/03_business_model.json + v2','A')
 for k,v in {'setup_start':1,'setup_end':14,'intake_start':15,'intake_end':59,'followup_start':60,'followup_end':90,'min_tier':1,'max_tier':2,'lock_minutes':10,'mature_months':6,'process_true_pct':75,'process_bad_pct':60}.items():add('pilot.'+k,v,'explicit retained pilot calendar/gate or new process-planning alternative','v2 + evaluation/business_case_evidence.md','A')
 add('quote.add_line_mid', (float(cat['P07']['price_min_inr_per_month'])+float(cat['P07']['price_max_inr_per_month']))/2,'P07 unit midpoint; no discount','product_catalogue.csv','A')
 add('quote.airfiber_mid',(float(cat['P04']['price_min_inr_per_month'])+float(cat['P04']['price_max_inr_per_month']))/2,'P04 unit midpoint; no discount','product_catalogue.csv','A')
 add('competitor.vi.contact_hours',48,'public page: representative contacts within48hours, not completed KYC','https://www.myvi.in/business/enterprise-mobility/corporate-postpaid-plans ;access2026-11-08','E')
 add('model.program_allowance',50*core_n,'retained INR50 per core lead *3956 core leads','v2 planning allowance','A')
 for spend in [200000,500000,1000000,2000000]:add('assumption.sensitivity.program.'+str(spend),spend,'scenario input for program-spend sensitivity, not observed cost','explicit sensitivity choice','A')
 # Bounded planning build-up; does not replace the retained v2 allowance.
 evidence_path=ROOT/'evaluation/prototype_evidence.json'
 if evidence_path.exists():
  evidence=json.loads(evidence_path.read_text());h=evidence['T2_kyc']['auto_hold']/evidence['T2_kyc']['packets']
  components={'hosting':7*3*90,'storage':20*3*50,'ocr_compute':2*core_n,'future_inference':2*core_n,'messaging':core_n,'review':h*core_n*6*6,'security_ops':20000}
  subtotal=sum(components.values());total=subtotal*1.25
  for k,v in components.items():add('cost_build.'+k,v,'dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md','Render public pricing + A planning quantities/rates + T2 specimen hold share','A','Not a vendor quote or observed operating cost; specimen hold share used as stress, not population estimate')
  add('cost_build.subtotal',subtotal,'sum planning components',label='A');add('cost_build.total',total,'subtotal*1.25 contingency',label='A');add('cost_build.hold_share',h,'automatic held supplied packets/12','T2 measured synthetic packets','V-proto')
  for minutes in [3,6,12]:
   for share in [.25,.5,h,1.]:add(f'cost_stress.{minutes}.{share:.4f}',(subtotal-components['review']+share*core_n*minutes*6)*1.25,'substitute held fraction *minutes*INR6/min, plus other costs and25% reserve',label='P')
 def bintail(n,k,p):return sum(math.exp(math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1)+i*math.log(p)+(n-i)*math.log1p(-p)) for i in range(k,n+1))
 routine_n=math.ceil(1.95996398454**2*.7*.3/.05**2)
 cutoff=math.ceil(.7*routine_n)
 add('pilot.process_n',routine_n,'ceil(z.975^2*.7*.3/.05^2), about5pp95% precision','process planning','P')
 add('pilot.process_power_pct',bintail(routine_n,cutoff,.75)*100,'P(Bin(n323,p.75)>=ceil(.7*n323)); hypothetical alternative','process planning','P')
 add('pilot.process_false_go_pct',bintail(routine_n,cutoff,.60)*100,'P(Bin(n323,p.60)>=ceil(.7*n323)); hypothetical unacceptable rate','process planning','P')
 add('pilot.process_power_at_target_pct',bintail(routine_n,cutoff,.70)*100,'Probability of meeting70% point gate when true rate equals70%; not80%','process planning','P')
 for k,v in {'retention.raw_days':365,'retention.receipt_days':365,'retention.log_days':365,'retention.abandoned_days':1,'cost_build.fx_inr_usd':90,'cost_build.host_usd_month':7,'cost_build.months':3,'cost_build.storage_gb':20,'cost_build.storage_inr_gb_month':50,'cost_build.review_minutes':6,'cost_build.review_inr_minute':6,'cost_build.contingency_pct':25}.items():add(k,v,'Explicit planning policy or dated hosting reference; legal/operational review required',label='E' if k=='cost_build.host_usd_month' else 'A')
 discrepancies=[{'item':'pilot planning rate','review':.062674,'actual_tier_weighted':p_tier,'actual_segment_weighted':p_segment,'reason':'Review collapses city tiers; v2 used four fixed segment x tier quotas. Both +2pp calculations round to2644/arm; +1pp differs9905 vs9904. Retain tier-weighted v2 baseline.'}]
 old=json.loads((ROOT/'analysis/baseline/03_business_model.json').read_text())
 for z in old['scenarios']:
  for k,kk in [('activations','activations'),('cac','cac_inr'),('payback','gross_revenue_payback_months'),('delta_mrr','incremental_mrr_inr')]:
   if abs(scenarios[z['scenario']][k]-z[kk])>.01:discrepancies.append({'item':z['scenario']+k,'old':z[kk],'new':scenarios[z['scenario']][k]})
 return {'meta':{'case_date':'2026-07-15','all_data':'fictional Accel synthetic','source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in D.glob('*.csv')}},'numbers':N,'scenarios':scenarios,'segments':segment,'bundles':bundles,'rule_conflict_ids':bad,'reason_crosscheck':cross,'discrepancies':discrepancies}
if __name__=='__main__':
 d=compute();(OUT/'numbers.json').write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding='utf-8')
 print(json.dumps({'number_keys':len(d['numbers']),'Base':d['scenarios']['Base'],'reason_crosscheck':d['reason_crosscheck'],'discrepancies':d['discrepancies']},indent=2))
