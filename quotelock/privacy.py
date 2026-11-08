"""Synthetic demo vault; ephemeral process key, never a saved credential."""
import time,json
from cryptography.fernet import Fernet
RETENTION={'raw_upload':365,'abandoned_upload':1,'field_receipt':365,'masked_log':365,'quote_hash':365}
class Vault:
 def __init__(self,store):self.store=store;self.cipher=Fernet(Fernet.generate_key())
 def put(self,session,kind,payload,consent):
  if not consent:raise ValueError('Consent required')
  if kind not in RETENTION:raise ValueError('Unknown document class')
  data=self.cipher.encrypt(payload)
  with self.store.db:self.store.db.execute('INSERT INTO evidence VALUES(?,?,?,?)',(session,kind,data,time.time()+RETENTION[kind]*86400))
  return {'stored':'encrypted','class':kind,'retention_days':RETENTION[kind],'mocked':True}
 def purge_expired(self,now=None):
  with self.store.db:self.store.db.execute('DELETE FROM evidence WHERE expires<=?',(now or time.time(),))
def breach_response():return {'action':'disable locking; restrict access; preserve masked incident record; accountable owner investigates and follows applicable notification duties','legal_status':'designed to support DPDP Act2023 / Rules2025 obligations; not certification'}
