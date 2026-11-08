from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'YTL_TrackA_Udyam_Digital_Data'
def read(n):
 with (DATA/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
CAT={r['product_id']:r for r in read('product_catalogue.csv')}
GST={r['gstin']:r for r in read('mock_gstin_registry.csv')}
UDYAM={r['udyam_number']:r for r in read('mock_udyam_registry.csv')}
BUNDLES={'micro':{'P04':1,'P07':1},'professional':{'P02':1,'P09':1,'P16':5,'P20':5},'multisite':{'P02':3,'P09':3,'P10':3},'manufacturer':{'P05':1,'P21':1,'P24':10}}
def evaluate(bundle,profile):
 holds=[];lines=[];lo=hi=setup=0.;term=0
 for p,q in bundle.items():
  if p not in CAT or not isinstance(q,int) or isinstance(q,bool) or not 1<=q<=1000:raise ValueError('Invalid product or quantity')
  c=CAT[p]
  for code,okay in [('tier',str(profile['tier']) in c['available_city_tiers'].split(';')),('employees',profile['employees']>=int(c['min_employees'])),('sites',profile['sites']>=int(c['min_sites'])),('gst',c['requires_gstin']=='N' or GST.get(profile.get('gstin',''),{}).get('status')=='Active'),('dependency',not c['requires_one_of'] or bool(set(bundle)&set(c['requires_one_of'].split('|'))))]:
   if not okay:holds.append({'code':'catalogue_'+code,'owner':'specialist','next_action':'Resolve '+code+' before acceptance','product':p})
  low=float(c['price_min_inr_per_month'])*q;high=float(c['price_max_inr_per_month'])*q
  lo+=low;hi+=high;setup+=float(c['one_time_setup_inr'])*q;term=max(term,int(c['min_contract_months']))
  lines.append({'product_id':p,'name':c['product_name'],'quantity':q,'monthly':(low+high)/2,'typical_days':int(c['typical_install_days'])})
 return {'lines':lines,'monthly_min':lo,'monthly_max':hi,'monthly':(lo+hi)/2,'setup':setup,'term_months':term,'holds':holds,'tariff_policy':'MIDPOINT-v1','taxes':'unknown: illustrative pre-tax subtotal','charges_known':False}
