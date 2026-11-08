"""Fail-closed semantic allowlist. Never pass raw text or structured facts onward."""
import re,unicodedata
SAFE={'internet','backup','email','security','wireless','mobile','clinic','shop','factory','multisite'}
MAP={'इंटरनेट':'internet','नेट':'internet','बैकअप':'backup','ईमेल':'email','सुरक्षा':'security','मोबाइल':'mobile','क्लिनिक':'clinic','दुकान':'shop','किराना':'shop','फैक्ट्री':'factory','कारखाना':'factory','फाइबर':'internet','airfiber':'wireless','broadband':'internet','fibre':'internet','fiber':'internet','kirana':'shop','failover':'backup','reliable':'internet','uptime':'internet','wifi':'wireless','office':'email','कार्यालय':'email'}
STOP=set('i we me my our need want a an the and for with in please hai chahiye mujhe hame mera meri aur budget rupees rs inr cost price reliable connection to of on at is be चाहिए मुझे मेरा हमें और के की में एक का पर लिए है हैं चाहिये भरोसेमंद दुकान को चाहिए मैं हम'.split())
NUMBER_WORDS='zero one two three four five six seven eight nine ten twenty thirty hundred thousand lakh crore hazaar hajar thousand rupees रुपये रूपये हजार हज़ार लाख करोड़ शून्य दो तीन चार पांच पाँच छह सात आठ नौ दस सौ'.split()
PATTERNS=[r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',r'UDYAM[-\s]*[A-Z]{2}[-\s]*\d{2}[-\s]*\d{7}',r'\b\d{2}[A-Z]{5}\d{4}[A-Z]\d[A-Z0-9]{2}\b',r'\b[A-Z]{5}\d{4}[A-Z]\b',r'\bSYN[-\s]*ID[-\s]*\d+\b',r'[₹$€£]',r'\d+(?:[,.]\d+)*']
def redact(text):
 if not isinstance(text,str) or len(text)>2000:return {'blocked':True,'payload':None,'reason':'input_length_or_type'}
 t=unicodedata.normalize('NFKC',text)
 if any(unicodedata.category(c) in ['Cf','Cs'] for c in t):return {'blocked':True,'payload':None,'reason':'uncertain_unicode'}
 for p in PATTERNS:t=re.sub(p,' ',t,flags=re.I)
 for w in NUMBER_WORDS:t=re.sub(r'(?<!\w)'+re.escape(w)+r'(?!\w)',' ',t,flags=re.I)
 tokens=re.findall(r'[a-z]+|[\u0900-\u097F]+',t.lower());found=[];unknown=[]
 for token in tokens:
  if token in SAFE:found.append(token)
  elif token in MAP:found.append(MAP[token])
  elif token not in STOP:unknown.append(token)
 if unknown or not found:return {'blocked':True,'payload':None,'reason':'uncertain_redaction_or_missing_intent'}
 return {'blocked':False,'payload':' '.join(sorted(set(found))),'reason':None}
class IntentAdapter:
 """Deterministic test double for the model slot; no catalogue or DB capability."""
 def __init__(self):self.received=[]
 def extract(self,payload):
  if not payload or not set(payload.split())<=SAFE:raise ValueError('Unsafe adapter payload')
  self.received.append(payload)
  return {'needs':payload.split(),'implementation':'rules-based stand-in; no LLM inference'}
