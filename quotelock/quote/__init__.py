import json,hashlib,sqlite3,time
from pathlib import Path
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False)
class Store:
 def __init__(self,path=':memory:'):
  self.db=sqlite3.connect(path,check_same_thread=False)
  self.db.executescript('''CREATE TABLE IF NOT EXISTS versions(session TEXT, v INTEGER, hash TEXT, payload TEXT, created REAL, PRIMARY KEY(session,v));
   CREATE TABLE IF NOT EXISTS sessions(id TEXT PRIMARY KEY, current INTEGER, accepted TEXT, consent INTEGER DEFAULT 0);
   CREATE TABLE IF NOT EXISTS locks(session TEXT PRIMARY KEY, hash TEXT, created REAL);
   CREATE TABLE IF NOT EXISTS holds(session TEXT, code TEXT, owner TEXT, action TEXT, created REAL, PRIMARY KEY(session,code));
   CREATE TABLE IF NOT EXISTS evidence(session TEXT, class TEXT, cipher BLOB, expires REAL);
   CREATE TRIGGER IF NOT EXISTS immutable_versions BEFORE UPDATE ON versions BEGIN SELECT RAISE(ABORT,'immutable quote'); END;
   CREATE TRIGGER IF NOT EXISTS no_delete_versions BEFORE DELETE ON versions BEGIN SELECT RAISE(ABORT,'immutable quote'); END;''')
  schema=self.db.execute("SELECT sql FROM sqlite_master WHERE name='locks'").fetchone()[0]
  if 'hash TEXT UNIQUE' in schema:
   # Migrate only this prototype's own database; preserve its old table/rows.
   self.db.executescript('ALTER TABLE locks RENAME TO locks_legacy_v1; CREATE TABLE locks(session TEXT PRIMARY KEY, hash TEXT, created REAL); INSERT INTO locks SELECT session,hash,created FROM locks_legacy_v1;')
 def version(self,session,payload):
  if self.db.execute('SELECT 1 FROM locks WHERE session=?',(session,)).fetchone():raise ValueError('Locked order cannot be edited')
  prior=self.current(session);body=canonical(payload);h=hashlib.sha256(body.encode()).hexdigest()
  if prior and prior['hash']==h:return prior
  v=1 if not prior else prior['version']+1
  with self.db:
   self.db.execute('INSERT INTO versions VALUES(?,?,?,?,?)',(session,v,h,body,time.time()))
   self.db.execute('INSERT INTO sessions(id,current) VALUES(?,?) ON CONFLICT(id) DO UPDATE SET current=excluded.current,accepted=NULL',(session,v))
  return self.current(session)
 def current(self,session):
  r=self.db.execute('SELECT v.v,v.hash,v.payload,s.accepted,s.consent FROM sessions s JOIN versions v ON s.id=v.session AND s.current=v.v WHERE s.id=?',(session,)).fetchone()
  return None if not r else {'session':session,'version':r[0],'hash':r[1],'payload':json.loads(r[2]),'accepted':r[3]==r[1],'consent':bool(r[4])}
 def consent(self,session,yes):
  with self.db:
   self.db.execute('UPDATE sessions SET consent=?,accepted=CASE WHEN ?=0 THEN NULL ELSE accepted END WHERE id=?',(int(yes),int(yes),session))
   if not yes:self.db.execute("DELETE FROM evidence WHERE session=? AND class='abandoned_upload'",(session,))
 def accept(self,session,h):
  c=self.current(session)
  if not c or h!=c['hash'] or not c['consent']:raise ValueError('Consent and current version required')
  with self.db:self.db.execute('UPDATE sessions SET accepted=? WHERE id=?',(h,session))
 def hold(self,session,code,owner,action):
  with self.db:self.db.execute('INSERT INTO holds VALUES(?,?,?,?,?) ON CONFLICT(session,code) DO UPDATE SET owner=excluded.owner,action=excluded.action',(session,code,owner,action,time.time()))
 def clear(self,session,code):
  with self.db:self.db.execute('DELETE FROM holds WHERE session=? AND code=?',(session,code))
 def queue(self,role='specialist'):
  allowed={'specialist':{'specialist','partner','operations'},'partner':{'partner'},'operations':{'operations'}}
  if role not in allowed:raise ValueError('Unknown demo role')
  return [{'session':s,'code':c,'owner':o,'next_action':a,'age_seconds':max(0,time.time()-t)} for s,c,o,a,t in self.db.execute('SELECT session,code,owner,action,created FROM holds') if o in allowed[role]]
