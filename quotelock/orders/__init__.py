import time
def lock(store,session,evidence,serviceability,payment,charges,signature):
 c=store.current(session)
 if not c:raise ValueError('No quote')
 prior=store.db.execute('SELECT hash FROM locks WHERE session=?',(session,)).fetchone()
 if prior:return {'status':'order_locked','hash':prior[0],'idempotent_replay':True,'mocked':True}
 specialist_pending=bool(store.db.execute("SELECT 1 FROM holds WHERE session=? AND code='specialist_route'",(session,)).fetchone())
 gates={'consent':c['consent'],'acceptance':c['accepted'],'evidence':evidence,'serviceability':serviceability,'payment_mandate':payment,'charges':charges,'esign_mock':signature,'catalogue':not c['payload']['quote']['holds'],'specialist_resolution':not specialist_pending}
 owners={'evidence':'specialist','catalogue':'specialist','serviceability':'operations','payment_mandate':'operations','charges':'specialist','acceptance':'partner','consent':'partner','esign_mock':'partner','specialist_resolution':'specialist'}
 failed=[]
 for k,passed in gates.items():
  if not passed:failed.append(k);store.hold(session,k,owners[k],'Resolve '+k+'; no override')
  else:store.clear(session,k)
 if failed:return {'status':'hold','failed':failed,'mocked':True}
 with store.db:store.db.execute('INSERT OR IGNORE INTO locks VALUES(?,?,?)',(session,c['hash'],time.time()))
 persisted=store.db.execute('SELECT hash FROM locks WHERE session=?',(session,)).fetchone()
 if not persisted or persisted[0]!=c['hash']:raise ValueError('Order lock was not durably recorded')
 return {'status':'order_locked','hash':c['hash'],'idempotent_replay':False,'mocked':True,'payment':'mock mandate only; no funds taken'}
