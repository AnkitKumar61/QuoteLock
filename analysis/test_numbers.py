import math
from analysis.numbers import compute
def test_expected_review_facts():
 d=compute();n=d['numbers'];get=lambda k:n[k]['value']
 expected={'baseline.cost':5539640,'baseline.mrr':4544990,'baseline.prequote_loss':1113,'baseline.postquote_loss':493,'pool.visit':827,'pool.quote':385,'pool.price':621,'rules.union':56,'rules.gst':21,'rules.tier':24,'rules.dependency':9,'rules.employees':8,'rules.mrr':768830,'model.Base.delta_mrr':292399.353928,'model.Base.starter_delta_mrr':162910.33,'model.Base.added_cost':436149.739537,'model.Base.program_break_even':841898.977734,'pilot.n.core.0.02':2644,'pilot.n.professional.0.02':4163,'baseline.within30':366,'language.non_english_pct':76.64}
 for k,v in expected.items():assert math.isclose(get(k),v,abs_tol=.01),(k,get(k),v)
def test_funnel():
 n=compute()['numbers']
 assert [n['funnel.'+s]['value'] for s in ['Lead','Contacted','Needs assessed','Quote accepted','KYC complete','Activated']]==[5000,3406,1974,861,588,368]
def test_traceability_and_no_model_regression():
 d=compute()
 assert len(d['discrepancies'])==1
 for k,r in d['numbers'].items():assert r['key']==k and r['source'] and r['formula'] and r['label'] in ['V','A','P','E','V-proto']
