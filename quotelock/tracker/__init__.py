def tracker(quote,locked=False):
 return {'digital':'Order locked' if locked else 'Awaiting accepted current version / gates','physical':[{'name':x['name'],'typical_days':x['typical_days'],'status':'Awaiting provisioning-ready event','clock_starts':'product provisioning-ready; no guaranteed date'} for x in quote['lines']],'mocked':True}
