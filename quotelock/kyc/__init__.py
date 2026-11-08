"""Core policy checks, conservative OCR extraction and explicitly mocked services."""
import re,datetime,json,hashlib,subprocess,tempfile,time
from pathlib import Path
from quotelock.catalogue import GST,UDYAM,read
TODAY=datetime.date(2026,7,15)
LEADS=read('smb_leads.csv')
def norm(s):return re.sub(r'[^a-z0-9]','',str(s or '').casefold())
def gst_check(s):
 if not s or len(s)!=15:return None
 chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';factor=2;total=0
 try:
  for ch in reversed(s[:14]):
   n=chars.index(ch)*factor;total+=n//36+n%36;factor=1 if factor==2 else 2
  return chars[(36-total%36)%36]
 except ValueError:return None
def parse_ocr(documents):
 """Never fill from registry/ground truth. Missing or uncertain fields stay null."""
 f={'present':list(documents),'blurred':False};alltext=' '.join(d.get('text','') for d in documents.values())
 def text(kind):return documents.get(kind,{}).get('text','')
 def match(pattern,t):
  m=re.search(pattern,t,re.I);return m.group(0).strip() if m else None
 f['gstin']=match(r'\b[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9][A-Z0-9]{2}\b',text('gst_certificate'))
 f['udyam']=match(r'UDYAM-[A-Z]{2}-[0-9]{2}-[0-9]{7}',text('udyam_certificate'))
 for key,kind in [('bill_date','address_proof'),('valid_till','signatory_id'),('udyam_date','udyam_certificate')]:f[key]=match(r'20[0-9]{2}-[01][0-9]-[0-3][0-9]',text(kind))
 for kind in documents:
  if documents[kind].get('blur_variance',1000)<20:f['blurred']=True
 lines=documents.get('gst_certificate',{}).get('lines',[])
 gi=next((i for i,x in enumerate(lines) if f['gstin'] and f['gstin'] in x),None)
 if gi is not None:
  tail=lines[gi+1:];ci=next((i for i,x in enumerate(tail) if x.strip() in ['Proprietorship','Limited Liability Partnership','Private Limited Company']),None)
  if ci is not None:
   before=tail[:ci];f['legal']=' '.join(before[:-1]) if len(before)>1 else (before[0] if before else None)
   dates=next((i for i,x in enumerate(tail[ci+1:]) if re.search(r'20\d{2}-\d{2}-\d{2}',x)),None)
   if dates is not None:f['address']=' '.join(tail[ci+1:ci+1+dates])
 sign=documents.get('signatory_id',{}).get('lines',[])
 # The specimen puts labels then values; anchor on a designation value.
 si=next((i for i,x in enumerate(sign) if x.strip()=='Name'),None)
 f['signatory']=sign[si+1] if si is not None and si+1<len(sign) else None
 f['activity']=match(r'\b(?:Manufacturing|Services|Trading)\b',text('udyam_certificate'))
 return f
def validate_fields(f,applicant=None):
 holds=[];advisories=[]
 def hold(code,action):holds.append({'code':code,'owner':'specialist','next_action':action})
 for k in ['gst_certificate','udyam_certificate','signatory_id','address_proof']:
  if k not in f.get('present',[]):hold('missing_'+k,'Upload the missing document')
 if f.get('blurred'):hold('blur','Re-upload a legible original; do not infer its fields')
 gid=f.get('gstin');uid=f.get('udyam');registry=GST.get(gid or '')
 if not gid:hold('gst_unreadable','Confirm GSTIN from a legible source')
 elif not re.fullmatch(r'\d{2}[A-Z]{5}\d{4}[A-Z]\d[A-Z0-9]{2}',gid) or gst_check(gid)!=gid[-1]:hold('gst_checksum','Re-upload and verify identifier; never substitute registry characters')
 if gid and not registry:hold('gst_registry_mismatch','Resolve exact identifier mismatch')
 if not uid:hold('udyam_missing_number','Supply the Udyam number/document or approved alternative evidence')
 u=UDYAM.get(uid or '')
 if uid and not u:hold('udyam_registry_mismatch','Resolve exact Udyam lookup')
 if applicant is None:
  applicant=next((r for r in LEADS if (uid and r['udyam_number']==uid) or (gid and r['gstin']==gid)),None)
 # An exact Udyam-linked applicant may provide comparison context, never a
 # replacement for the OCR GSTIN. Existing identifier holds remain blocking.
 if registry is None and applicant:registry=GST.get(applicant.get('gstin',''))
 if registry and registry['status']!='Active':hold('gst_not_active','Resolve non-active mock status; no override')
 if registry:
  for key,rkey in [('legal','legal_name'),('address','principal_place_of_business')]:
   if not f.get(key):hold('ocr_uncertain_'+key,'Human confirm '+key+' from original')
   elif norm(f[key])!=norm(registry[rkey]):hold(key+'_mismatch','Resolve '+key+' against exact mock evidence')
 if not f.get('signatory'):hold('ocr_uncertain_signatory','Human confirm signatory from original')
 elif not applicant:hold('applicant_unknown','Confirm applicant authority')
 elif norm(f['signatory'])!=norm(applicant['contact_name']):hold('authority_review','Confirm signatory authority, not a fraud finding')
 for key in ['bill_date','valid_till']:
  try:
   date=datetime.date.fromisoformat(f[key])
   if key=='bill_date' and not 0<=(TODAY-date).days<=90:hold('address_stale','Supply address proof within90 days of case date')
   if key=='valid_till' and date<TODAY:hold('id_expired','Upload valid signatory ID')
  except (KeyError,ValueError,TypeError):hold('ocr_uncertain_'+key,'Confirm '+key+' from original')
 if u:
  if f.get('udyam_date') and f['udyam_date']!=u['date_of_registration']:advisories.append('udyam_registration_date_difference')
  if f.get('activity') and f['activity']!=u['major_activity']:advisories.append('udyam_activity_difference')
 return {'status':'hold' if holds else 'core_checks_clear','holds':holds,'advisories':advisories,'policy':'CORE-v4: metadata differences advisory; not legal KYC certification','mocked':True}
def mock_digilocker(consent,document_hash):
 if not consent:raise ValueError('Consent required')
 return {'service':'DigiLocker','mocked':True,'document_hash':document_hash,'issuer_verification':'not performed'}
def mock_esign(consent,quote_hash):
 if not consent:raise ValueError('Consent required')
 return {'service':'e-sign','mocked':True,'signed_current_hash':quote_hash,'legal_signature':'not performed'}
