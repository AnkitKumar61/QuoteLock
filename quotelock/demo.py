"""One-command API replay of four synthetic personas; no external calls."""
import json,uuid
from pathlib import Path
from fastapi.testclient import TestClient
import quotelock.app as m
from quotelock.catalogue import read
ROOT=Path(__file__).resolve().parent.parent
def run(client,prefix='demo'):
 f=json.loads((ROOT/'evaluation/ocr_fields.json').read_text());out=[]
 def preview(name,seg,employees,sites,gst,intent,budget,bundle=None):
  sid=prefix+'-'+name
  r=client.post('/api/preview',json={'session':sid,'segment':seg,'tier':2,'employees':employees,'sites':sites,'gstin':gst,'intent':intent,'budget':budget,**({'bundle':bundle} if bundle else {})})
  assert r.status_code==200,r.text
  return sid,r.json()
 sid,q=preview('clinic','professional',5,1,f['K02']['gstin'],'internet backup email security clinic',5000)
 client.post('/api/consent',json={'session':sid,'consent':True});k=client.post('/api/kyc',json={'session':sid,'packet':'K02'}).json()
 a=client.post('/api/accept',json={'session':sid,'hash':q['hash'],'charges_known':True})
 locked=client.post('/api/lock',json={'session':sid,'serviceability':True,'payment_mandate':True,'charges_known':True}).json()
 out.append({'persona':'Professional clinic, GST','session':sid,'monthly':q['payload']['quote']['monthly'],'kyc':k['status'],'accept_http':a.status_code,'outcome':locked['status'],'all_services_mocked':True})
 sid,q=preview('kirana','micro',1,1,'','मुझे इंटरनेट मोबाइल दुकान चाहिए',2000)
 out.append({'persona':'Micro kirana, no GST','session':sid,'monthly':q['payload']['quote']['monthly'],'route':q['payload']['route'],'outcome':'preview, evidence pending','all_services_mocked':True})
 sid,q=preview('multisite','multisite',10,3,f['K02']['gstin'],'internet backup multisite',20000)
 out.append({'persona':'Multi-site assisted','session':sid,'monthly':q['payload']['quote']['monthly'],'route':q['payload']['route'],'outcome':'specialist hold','all_services_mocked':True})
 lead=next(x for x in read('smb_leads.csv') if x['udyam_number']==f['K06']['udyam'])
 sid,q=preview('k06','micro',1,1,lead['gstin'],'internet mobile shop',2000)
 client.post('/api/consent',json={'session':sid,'consent':True});k=client.post('/api/kyc',json={'session':sid,'packet':'K06'}).json()
 locked=client.post('/api/lock',json={'session':sid,'serviceability':True,'payment_mandate':True,'charges_known':True}).json()
 out.append({'persona':'K06 identifier failure','session':sid,'kyc':k['status'],'hold_codes':[x['code'] for x in k['holds']],'outcome':locked['status'],'all_services_mocked':True})
 return out
if __name__=='__main__':
 results=run(TestClient(m.app),'demo-'+uuid.uuid4().hex[:6]);print(json.dumps(results,indent=2,ensure_ascii=True))
