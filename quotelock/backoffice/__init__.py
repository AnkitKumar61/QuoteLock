def specialist_first(profile,holds):
 if holds or profile['sites']>1 or profile['segment'] in ['multisite','manufacturer']:return 'specialist'
 return 'routine_gst' if profile.get('gstin') else 'no_gst_starter'
