from quotelock.boundary import redact,IntentAdapter
from quotelock.catalogue import evaluate,BUNDLES,GST
ADAPTER=IntentAdapter()
def discover(text,profile,budget,language='en',bundle=None):
 if language not in ['en','hi']:raise ValueError('This prototype supports Hindi and English templates only')
 if not all(k in profile for k in ['tier','employees','sites','segment']):return {'status':'clarify','message':'Complete the required business facts / ज़रूरी जानकारी दें'}
 if budget is None or not isinstance(budget,(int,float)) or not 0<budget<=10000000:return {'status':'clarify','message':'Enter budget in its separate field / बजट अलग भरें'}
 r=redact(text)
 if r['blocked']:return {'status':'clarify','boundary':r,'message':'Use the structured fields; no model call / जानकारी फ़ॉर्म में दें'}
 slots=ADAPTER.extract(r['payload']);b=bundle or BUNDLES.get(profile['segment'])
 if not b:return {'status':'clarify','message':'Select business type'}
 quote=evaluate(b,profile)
 route='specialist' if quote['holds'] or profile['segment'] in ['multisite','manufacturer'] or profile['sites']>1 or (profile.get('gstin') and GST.get(profile['gstin'],{}).get('status')!='Active') else ('routine_gst' if profile.get('gstin') else 'no_gst_starter')
 explanation='आपकी जरूरतों के लिए यह पैकेज है। बदलाव पर नया कोट स्वीकार करें।' if language=='hi' else 'This bundle covers your stated needs. Accept a fresh quote after any change.'
 return {'status':'preview','route':route,'boundary':r,'slots':slots,'quote':quote,'budget_fit':quote['monthly']<=budget,'explanation':explanation,'language':language,'mocked':True}
