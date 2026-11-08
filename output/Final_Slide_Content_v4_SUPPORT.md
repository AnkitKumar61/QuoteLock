REFERENCE ONLY — DO NOT BUILD AS SLIDES.

# QuoteLock v4 reference material

The only deck source is `Final_Slide_Content_v4.md`. This file is evidence and audit material, never slide8 or an appendix. The custom score is not Airtel’s official rubric. All supplied data are fictional Accel synthetic data.

## Per-slide number trace

Every displayed number is keyed below or belongs to a named T evidence receipt. Ranges/rounded displays inherit the same underlying key. Layout dimensions, source IDs, version labels and product-name bandwidths are metadata; product labels trace to the supplied catalogue, not invented tariffs.

| Slide | Canonical number keys / test receipt | Rounding and scope |
| --- | --- | --- |
|1|case date from README/case; all footer test counts T0/T1/T2/T3/T5/T6/T7|Date is case reference, not evaluation access date.|
|2|funnel.*;baseline.prequote_loss/postquote_loss;pool.*;reason.*;language.non_english_pct/language_pct.Hindi/Marathi;T5|Counts exact; language percentages1decimal.827 at Contacted,385/621 at Needs assessed,273 at Quote accepted,220 at KYC complete.|
|3|segment.{micro,professional,multisite,manufacturer}.{cac,payback,arpu};bundle.*;micro.ceiling.6/headroom;matched_micro.cac;typical_days.*|CAC rupee-rounded, payback2decimals. Midpoints retain.50. Quantity/profile choices A; ranges V, not final totals.|
|4|T3_quote_time;T4_version;case.quote_days_min/max;official V1 contact48h|Median/p90:2decimal milliseconds, scripted/prefilled only. Screenshot versions are real UI values. Vi48h is contact, not completed KYC.|
|5|T1_boundary;T2_kyc;T7_rules;retention.*|4/8 automatic classification;5/7 after team-confirmed transcription is a separate comparison, not OCR yield.0 false passes vs team labels, not a legal guarantee.|
|6|reason.Installation delayed beyond21 days;reason.Site not feasible for fibre;reason.First payment failed;baseline.calls_mean;typical_days.*;T6/T8|3.011 calls displayed3.0; screenshot age is live elapsed capture age, not promised handling time.|
|7|baseline.*,model.*,cost_build.*,run_rate.*,pilot.*,reason_crosscheck.*|Fractional projected activations439.761 rounded about440/+72; MRR range rounded1.63–2.92 lakh;4-cohort range6.52–11.70 lakh; no churn.|

### Exact per-slide canonical-key index

#### Slide 1

| Key | Value | Label | Formula / source |
| --- | --- | --- | --- |
| case.quote_days_min | 3 | V | case PDF p2; Airtel_SYNC_Case.pdf p2 |
#### Slide 2

| Key | Value | Label | Formula / source |
| --- | --- | --- | --- |
| funnel.Lead | 5000 | V | count stage_reached >= Lead; smb_leads.csv |
| funnel.Contacted | 3406 | V | count stage_reached >= Contacted; smb_leads.csv |
| funnel.Needs assessed | 1974 | V | count stage_reached >= Needs assessed; smb_leads.csv |
| funnel.Quote accepted | 861 | V | count stage_reached >= Quote accepted; smb_leads.csv |
| funnel.KYC complete | 588 | V | count stage_reached >= KYC complete; smb_leads.csv |
| funnel.Activated | 368 | V | count stage_reached >= Activated; smb_leads.csv |
| baseline.prequote_loss | 1113 | V | needs assessed - quote accepted; smb_leads.csv |
| baseline.postquote_loss | 493 | V | quote accepted - activated; smb_leads.csv |
| baseline.future_activations | 16 | V | count activated after case date; smb_leads.csv |
| reason.Quote took too long to arrive | 179 | V | count exact drop_reason; smb_leads.csv |
| reason.Locked in with current provider | 325 | V | count exact drop_reason; smb_leads.csv |
| reason.Visit not scheduled by sales | 296 | V | count exact drop_reason; smb_leads.csv |
| reason.Owner had no time for a visit | 531 | V | count exact drop_reason; smb_leads.csv |
| reason.Site not feasible for fibre | 41 | V | count exact drop_reason; smb_leads.csv |
| reason.Only wanted a mobile plan | 280 | V | count exact drop_reason; smb_leads.csv |
| reason.Authorised signatory not available | 53 | V | count exact drop_reason; smb_leads.csv |
| reason.Document details did not match | 47 | V | count exact drop_reason; smb_leads.csv |
| reason.Quote too complex to understand | 206 | V | count exact drop_reason; smb_leads.csv |
| reason.Not interested on first call | 470 | V | count exact drop_reason; smb_leads.csv |
| reason.Wrong or invalid number | 319 | V | count exact drop_reason; smb_leads.csv |
| reason.Installation delayed beyond 21 days | 98 | V | count exact drop_reason; smb_leads.csv |
| reason.Price too high | 414 | V | count exact drop_reason; smb_leads.csv |
| reason.First payment failed | 28 | V | count exact drop_reason; smb_leads.csv |
| reason.Decided to wait | 107 | V | count exact drop_reason; smb_leads.csv |
| reason.Competitor offered cheaper plan | 207 | V | count exact drop_reason; smb_leads.csv |
| reason.Missing GST or Udyam document | 94 | V | count exact drop_reason; smb_leads.csv |
| reason.Customer cancelled before install | 53 | V | count exact drop_reason; smb_leads.csv |
| reason.Found paperwork too long | 79 | V | count exact drop_reason; smb_leads.csv |
| reason.Unreachable after 3 attempts | 805 | V | count exact drop_reason; smb_leads.csv |
| pool.visit.micro | 484 | V | count exact stage-specific reason set ['Owner had no time for a visit', 'Visit not scheduled by sales']; smb_leads.csv |
| pool.quote.micro | 242 | V | count exact stage-specific reason set ['Quote too complex to understand', 'Quote took too long to arrive']; smb_leads.csv |
| pool.price.micro | 381 | V | count exact stage-specific reason set ['Price too high', 'Competitor offered cheaper plan']; smb_leads.csv |
| pool.visit.professional | 190 | V | count exact stage-specific reason set ['Owner had no time for a visit', 'Visit not scheduled by sales']; smb_leads.csv |
| pool.quote.professional | 82 | V | count exact stage-specific reason set ['Quote too complex to understand', 'Quote took too long to arrive']; smb_leads.csv |
| pool.price.professional | 145 | V | count exact stage-specific reason set ['Price too high', 'Competitor offered cheaper plan']; smb_leads.csv |
| pool.visit.multisite | 116 | V | count exact stage-specific reason set ['Owner had no time for a visit', 'Visit not scheduled by sales']; smb_leads.csv |
| pool.quote.multisite | 44 | V | count exact stage-specific reason set ['Quote too complex to understand', 'Quote took too long to arrive']; smb_leads.csv |
| pool.price.multisite | 74 | V | count exact stage-specific reason set ['Price too high', 'Competitor offered cheaper plan']; smb_leads.csv |
| pool.visit.manufacturer | 37 | V | count exact stage-specific reason set ['Owner had no time for a visit', 'Visit not scheduled by sales']; smb_leads.csv |
| pool.quote.manufacturer | 17 | V | count exact stage-specific reason set ['Quote too complex to understand', 'Quote took too long to arrive']; smb_leads.csv |
| pool.price.manufacturer | 21 | V | count exact stage-specific reason set ['Price too high', 'Competitor offered cheaper plan']; smb_leads.csv |
| pool.visit | 827 | V | sum exact disjoint reasons within stage; smb_leads.csv |
| pool.quote | 385 | V | sum exact disjoint reasons within stage; smb_leads.csv |
| pool.price | 621 | V | sum exact disjoint reasons within stage; smb_leads.csv |
| language.Malayalam | 83 | V | count preferred_language; smb_leads.csv |
| language_pct.Malayalam | 1.66 | V | preferred_language/5000*100; smb_leads.csv |
| language.Punjabi | 96 | V | count preferred_language; smb_leads.csv |
| language_pct.Punjabi | 1.92 | V | preferred_language/5000*100; smb_leads.csv |
| language.English | 1168 | V | count preferred_language; smb_leads.csv |
| language_pct.English | 23.36 | V | preferred_language/5000*100; smb_leads.csv |
| language.Hindi | 2137 | V | count preferred_language; smb_leads.csv |
| language_pct.Hindi | 42.74 | V | preferred_language/5000*100; smb_leads.csv |
| language.Telugu | 207 | V | count preferred_language; smb_leads.csv |
| language_pct.Telugu | 4.14 | V | preferred_language/5000*100; smb_leads.csv |
| language.Bengali | 111 | V | count preferred_language; smb_leads.csv |
| language_pct.Bengali | 2.22 | V | preferred_language/5000*100; smb_leads.csv |
| language.Kannada | 253 | V | count preferred_language; smb_leads.csv |
| language_pct.Kannada | 5.06 | V | preferred_language/5000*100; smb_leads.csv |
| language.Marathi | 505 | V | count preferred_language; smb_leads.csv |
| language_pct.Marathi | 10.100000000000001 | V | preferred_language/5000*100; smb_leads.csv |
| language.Gujarati | 233 | V | count preferred_language; smb_leads.csv |
| language_pct.Gujarati | 4.66 | V | preferred_language/5000*100; smb_leads.csv |
| language.Tamil | 207 | V | count preferred_language; smb_leads.csv |
| language_pct.Tamil | 4.14 | V | preferred_language/5000*100; smb_leads.csv |
| language.non_english_pct | 76.64 | V | non-English preference/5000*100; smb_leads.csv |
| pool.kyc_paperwork | 273 | V | quote accepted minus KYC complete; smb_leads.csv |
| pool.fulfilment_payment | 220 | V | KYC complete minus activated; smb_leads.csv |
#### Slide 3

| Key | Value | Label | Formula / source |
| --- | --- | --- | --- |
| segment.micro.leads | 2709 | V | same-segment raw rows: leads; smb_leads.csv |
| segment.micro.activations | 110 | V | same-segment raw rows: activations; smb_leads.csv |
| segment.micro.quotes | 325 | V | same-segment raw rows: quotes; smb_leads.csv |
| segment.micro.cac | 20007.090909090908 | V | same-segment raw rows: cac; smb_leads.csv |
| segment.micro.arpu | 2504.818181818182 | V | same-segment raw rows: arpu; smb_leads.csv |
| segment.micro.payback | 7.987442383769462 | V | same-segment raw rows: payback; smb_leads.csv |
| segment.micro.conversion | 4.060538944259875 | V | same-segment raw rows: conversion; smb_leads.csv |
| segment.micro.lead_share | 54.17999999999999 | V | same-segment raw rows: lead_share; smb_leads.csv |
| segment.micro.proxy | 2688.4545454545455 | V | same-segment raw rows: proxy; smb_leads.csv |
| segment.professional.leads | 1247 | V | same-segment raw rows: leads; smb_leads.csv |
| segment.professional.activations | 138 | V | same-segment raw rows: activations; smb_leads.csv |
| segment.professional.quotes | 285 | V | same-segment raw rows: quotes; smb_leads.csv |
| segment.professional.cac | 10694.710144927536 | V | same-segment raw rows: cac; smb_leads.csv |
| segment.professional.arpu | 6795.869565217391 | V | same-segment raw rows: arpu; smb_leads.csv |
| segment.professional.payback | 1.5737073883326402 | V | same-segment raw rows: payback; smb_leads.csv |
| segment.professional.conversion | 11.066559743384122 | V | same-segment raw rows: conversion; smb_leads.csv |
| segment.professional.lead_share | 24.94 | V | same-segment raw rows: lead_share; smb_leads.csv |
| segment.professional.proxy | 4169.347826086957 | V | same-segment raw rows: proxy; smb_leads.csv |
| segment.multisite.leads | 755 | V | same-segment raw rows: leads; smb_leads.csv |
| segment.multisite.activations | 83 | V | same-segment raw rows: activations; smb_leads.csv |
| segment.multisite.quotes | 168 | V | same-segment raw rows: quotes; smb_leads.csv |
| segment.multisite.cac | 15614.33734939759 | V | same-segment raw rows: cac; smb_leads.csv |
| segment.multisite.arpu | 31233.493975903613 | V | same-segment raw rows: arpu; smb_leads.csv |
| segment.multisite.payback | 0.49992285081662413 | V | same-segment raw rows: payback; smb_leads.csv |
| segment.multisite.conversion | 10.993377483443709 | V | same-segment raw rows: conversion; smb_leads.csv |
| segment.multisite.lead_share | 15.1 | V | same-segment raw rows: lead_share; smb_leads.csv |
| segment.multisite.proxy | 9099.036144578313 | V | same-segment raw rows: proxy; smb_leads.csv |
| segment.manufacturer.leads | 289 | V | same-segment raw rows: leads; smb_leads.csv |
| segment.manufacturer.activations | 37 | V | same-segment raw rows: activations; smb_leads.csv |
| segment.manufacturer.quotes | 83 | V | same-segment raw rows: quotes; smb_leads.csv |
| segment.manufacturer.cac | 15324.324324324325 | V | same-segment raw rows: cac; smb_leads.csv |
| segment.manufacturer.arpu | 19979.72972972973 | V | same-segment raw rows: arpu; smb_leads.csv |
| segment.manufacturer.payback | 0.7669935745688198 | V | same-segment raw rows: payback; smb_leads.csv |
| segment.manufacturer.conversion | 12.802768166089965 | V | same-segment raw rows: conversion; smb_leads.csv |
| segment.manufacturer.lead_share | 5.779999999999999 | V | same-segment raw rows: lead_share; smb_leads.csv |
| segment.manufacturer.proxy | 9606.216216216217 | V | same-segment raw rows: proxy; smb_leads.csv |
| matched_micro.leads | 1247 | V | four-channel Micro-only subset: leads; smb_leads.csv |
| matched_micro.activations | 53 | V | four-channel Micro-only subset: activations; smb_leads.csv |
| matched_micro.cac | 8068.301886792453 | V | four-channel Micro-only subset: cac; smb_leads.csv |
| matched_micro.conversion | 4.250200481154772 | V | four-channel Micro-only subset: conversion; smb_leads.csv |
| bundle.professional.min | 3118.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.professional.max | 3893.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.professional.mid | 3505.5 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.professional.setup | 1500.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.professional.term | 12 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| segment.professional.clean_arpu | 6268.482142857143 | V | mean monthly value, no detected supplied-rule conflict; smb_leads.csv |
| bundle.micro.min | 1198.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.max | 1498.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.mid | 1348.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.setup | 0.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.term | 6 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| segment.micro.clean_arpu | 2436.893203883495 | V | mean monthly value, no detected supplied-rule conflict; smb_leads.csv |
| bundle.multisite.min | 13494.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.multisite.max | 17694.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.multisite.mid | 15594.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.multisite.setup | 19500.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.multisite.term | 24 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| segment.multisite.clean_arpu | 31077.30769230769 | V | mean monthly value, no detected supplied-rule conflict; smb_leads.csv |
| bundle.manufacturer.min | 11489.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.manufacturer.max | 17489.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.manufacturer.mid | 14489.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.manufacturer.setup | 44000.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.manufacturer.term | 24 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| segment.manufacturer.clean_arpu | 21003.157894736843 | V | mean monthly value, no detected supplied-rule conflict; smb_leads.csv |
| typical_days.P01 | 5 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P02 | 5 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P03 | 7 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P04 | 2 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P05 | 21 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P06 | 30 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P07 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P08 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P09 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P10 | 14 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P11 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P12 | 5 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P13 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P14 | 4 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P15 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P16 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P17 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P18 | 2 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P19 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P20 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P21 | 10 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P22 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P23 | 4 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P24 | 10 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P25 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| micro.ceiling.6 | 8088 | P | 1348*6 constant months revenue; catalogue midpoint + policy |
| micro.ceiling.12 | 16176 | P | 1348*12 constant months revenue; catalogue midpoint + policy |
| micro.ceiling.24 | 32352 | P | 1348*24 constant months revenue; catalogue midpoint + policy |
| micro.headroom | 19.698113207547067 | P | 8088-matched Micro CAC; smb_leads.csv |
| assumption.bundle.professional.tier | 2 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.professional.employees | 5 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.professional.sites | 1 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.professional.quantity.P02 | 1 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.professional.quantity.P09 | 1 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.professional.quantity.P16 | 5 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.professional.quantity.P20 | 5 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.micro.tier | 2 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.micro.employees | 1 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.micro.sites | 1 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.micro.quantity.P04 | 1 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.micro.quantity.P07 | 1 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.multisite.tier | 2 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.multisite.employees | 10 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.multisite.sites | 3 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.multisite.quantity.P02 | 3 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.multisite.quantity.P09 | 3 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.multisite.quantity.P10 | 3 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.manufacturer.tier | 2 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.manufacturer.employees | 10 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.manufacturer.sites | 1 | A | illustrative eligible profile, checked against supplied catalogue; catalogue + explicit bundle choice |
| assumption.bundle.manufacturer.quantity.P05 | 1 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.manufacturer.quantity.P21 | 1 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
| assumption.bundle.manufacturer.quantity.P24 | 10 | A | chosen SKU quantity; price arithmetic uses this same quantity; catalogue + explicit bundle choice |
#### Slide 4

| Key | Value | Label | Formula / source |
| --- | --- | --- | --- |
| bundle.micro.min | 1198.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.max | 1498.0 | V | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.mid | 1348.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.setup | 0.0 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| bundle.micro.term | 6 | A | sum catalogue quantities; MIDPOINT-v1; setup/unit; term=max; product_catalogue.csv |
| typical_days.P04 | 2 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P07 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| case.quote_days_min | 3 | V | case PDF p2; Airtel_SYNC_Case.pdf p2 |
| case.quote_days_max | 5 | V | case PDF p2; Airtel_SYNC_Case.pdf p2 |
| quote.add_line_mid | 349.0 | A | P07 unit midpoint; no discount; product_catalogue.csv |
| quote.airfiber_mid | 999.0 | A | P04 unit midpoint; no discount; product_catalogue.csv |
| competitor.vi.contact_hours | 48 | E | public page: representative contacts within48hours, not completed KYC; https://www.myvi.in/business/enterprise-mobility/corporate-postpaid-plans ;access2026-11-08 |
#### Slide 5

| Key | Value | Label | Formula / source |
| --- | --- | --- | --- |
| rules.union | 56 | V | distinct activated lead IDs with >=1 supplied hard-rule conflict; product_catalogue.csv + mock_gstin_registry.csv + smb_leads.csv |
| rules.employees | 8 | V | distinct affected lead IDs; categories overlap; smb_leads.csv |
| rules.tier | 24 | V | distinct affected lead IDs; categories overlap; smb_leads.csv |
| rules.gst | 21 | V | distinct affected lead IDs; categories overlap; smb_leads.csv |
| rules.dependency | 9 | V | distinct affected lead IDs; categories overlap; smb_leads.csv |
| rules.mrr | 768830.0 | V | recorded MRR of rule-conflicting rows; smb_leads.csv |
| retention.raw_days | 365 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| retention.receipt_days | 365 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| retention.log_days | 365 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| retention.abandoned_days | 1 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
#### Slide 6

| Key | Value | Label | Formula / source |
| --- | --- | --- | --- |
| baseline.calls_mean | 3.010869565217391 | V | mean activated follow-up calls; window unspecified; smb_leads.csv |
| reason.Quote took too long to arrive | 179 | V | count exact drop_reason; smb_leads.csv |
| reason.Locked in with current provider | 325 | V | count exact drop_reason; smb_leads.csv |
| reason.Visit not scheduled by sales | 296 | V | count exact drop_reason; smb_leads.csv |
| reason.Owner had no time for a visit | 531 | V | count exact drop_reason; smb_leads.csv |
| reason.Site not feasible for fibre | 41 | V | count exact drop_reason; smb_leads.csv |
| reason.Only wanted a mobile plan | 280 | V | count exact drop_reason; smb_leads.csv |
| reason.Authorised signatory not available | 53 | V | count exact drop_reason; smb_leads.csv |
| reason.Document details did not match | 47 | V | count exact drop_reason; smb_leads.csv |
| reason.Quote too complex to understand | 206 | V | count exact drop_reason; smb_leads.csv |
| reason.Not interested on first call | 470 | V | count exact drop_reason; smb_leads.csv |
| reason.Wrong or invalid number | 319 | V | count exact drop_reason; smb_leads.csv |
| reason.Installation delayed beyond 21 days | 98 | V | count exact drop_reason; smb_leads.csv |
| reason.Price too high | 414 | V | count exact drop_reason; smb_leads.csv |
| reason.First payment failed | 28 | V | count exact drop_reason; smb_leads.csv |
| reason.Decided to wait | 107 | V | count exact drop_reason; smb_leads.csv |
| reason.Competitor offered cheaper plan | 207 | V | count exact drop_reason; smb_leads.csv |
| reason.Missing GST or Udyam document | 94 | V | count exact drop_reason; smb_leads.csv |
| reason.Customer cancelled before install | 53 | V | count exact drop_reason; smb_leads.csv |
| reason.Found paperwork too long | 79 | V | count exact drop_reason; smb_leads.csv |
| reason.Unreachable after 3 attempts | 805 | V | count exact drop_reason; smb_leads.csv |
| typical_days.P01 | 5 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P02 | 5 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P03 | 7 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P04 | 2 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P05 | 21 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P06 | 30 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P07 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P08 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P09 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P10 | 14 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P11 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P12 | 5 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P13 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P14 | 4 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P15 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P16 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P17 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P18 | 2 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P19 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P20 | 1 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P21 | 10 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P22 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P23 | 4 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P24 | 10 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
| typical_days.P25 | 3 | V | source typical_install_days, not a guarantee; product_catalogue.csv |
#### Slide 7

| Key | Value | Label | Formula / source |
| --- | --- | --- | --- |
| baseline.leads | 5000 | V | count all; smb_leads.csv |
| baseline.activations | 368 | V | count Activated; smb_leads.csv |
| baseline.cost | 5539640.0 | V | sum acquisition costs, all leads; smb_leads.csv |
| baseline.mrr | 4544990.0 | V | sum activated monthly value; smb_leads.csv |
| baseline.cac | 15053.369565217392 | V | cost/activations; smb_leads.csv |
| baseline.payback | 1.218845365996405 | V | cost/MRR; smb_leads.csv |
| baseline.conversion | 7.359999999999999 | V | activated/all leads*100; smb_leads.csv |
| baseline.quote_conversion | 42.74099883855981 | V | 368/861*100; smb_leads.csv |
| baseline.prequote_loss | 1113 | V | needs assessed - quote accepted; smb_leads.csv |
| baseline.needs_quote_conversion | 43.61702127659575 | V | 861/1974*100; smb_leads.csv |
| baseline.postquote_loss | 493 | V | quote accepted - activated; smb_leads.csv |
| baseline.days_mean | 17.616847826086957 | V | mean days_lead_to_activation; smb_leads.csv |
| baseline.calls_mean | 3.010869565217391 | V | mean activated follow-up calls; window unspecified; smb_leads.csv |
| baseline.churn_flags | 56 | V | count synthetic flag Y; smb_leads.csv |
| baseline.churn_pct | 15.217391304347828 | V | flags/activated*100, not matured; smb_leads.csv |
| baseline.future_activations | 16 | V | count activated after case date; smb_leads.csv |
| baseline.within30 | 366 | V | count lead-to-activation <=30 days; smb_leads.csv |
| baseline.days_max | 31.0 | V | max supplied lead-to-activation; smb_leads.csv |
| baseline.six_month_matured | 0 | V | earliest activation Apr13 +6 calendar months >Jul15; smb_leads.csv |
| model.Low.micro.delta_a | 19.731623076923114 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Low.professional.delta_a | 14.962205263157898 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Low.multisite.delta_a | 0.0 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Low.manufacturer.delta_a | 0.0 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Low.activations | 402.69382834008104 | P | unchanged Phase3 formulas; see model output definition activations; raw CSVs + scenario assumptions |
| model.Low.quotes | 900.5600000000001 | P | unchanged Phase3 formulas; see model output definition quotes; raw CSVs + scenario assumptions |
| model.Low.delta_a | 34.69382834008104 | P | unchanged Phase3 formulas; see model output definition delta_a; raw CSVs + scenario assumptions |
| model.Low.delta_mrr | 141874.17468761312 | P | unchanged Phase3 formulas; see model output definition delta_mrr; raw CSVs + scenario assumptions |
| model.Low.starter_delta_mrr | 79048.23845769238 | P | unchanged Phase3 formulas; see model output definition starter_delta_mrr; raw CSVs + scenario assumptions |
| model.Low.handling | 115430.20973776396 | P | unchanged Phase3 formulas; see model output definition handling; raw CSVs + scenario assumptions |
| model.Low.program | 197800 | P | unchanged Phase3 formulas; see model output definition program; raw CSVs + scenario assumptions |
| model.Low.added_cost | 313230.209737764 | P | unchanged Phase3 formulas; see model output definition added_cost; raw CSVs + scenario assumptions |
| model.Low.cost | 5852870.209737764 | P | unchanged Phase3 formulas; see model output definition cost; raw CSVs + scenario assumptions |
| model.Low.cac | 14534.293296382299 | P | unchanged Phase3 formulas; see model output definition cac; raw CSVs + scenario assumptions |
| model.Low.payback | 1.2487816995737597 | P | unchanged Phase3 formulas; see model output definition payback; raw CSVs + scenario assumptions |
| model.Low.conversion | 8.053876566801621 | P | unchanged Phase3 formulas; see model output definition conversion; raw CSVs + scenario assumptions |
| model.Low.quote_conversion | 44.71593545572544 | P | unchanged Phase3 formulas; see model output definition quote_conversion; raw CSVs + scenario assumptions |
| model.Low.churn | 15.531520265939111 | P | unchanged Phase3 formulas; see model output definition churn; raw CSVs + scenario assumptions |
| model.Low.calls | 3.0203743054076444 | P | unchanged Phase3 formulas; see model output definition calls; raw CSVs + scenario assumptions |
| model.Low.digital | 45 | P | unchanged Phase3 formulas; see model output definition digital; raw CSVs + scenario assumptions |
| model.Low.physical | 60 | P | unchanged Phase3 formulas; see model output definition physical; raw CSVs + scenario assumptions |
| model.Low.marginal | 9028.412969228184 | P | unchanged Phase3 formulas; see model output definition marginal; raw CSVs + scenario assumptions |
| model.Low.stress_a | 346.69382834008104 | P | unchanged Phase3 formulas; see model output definition stress_a; raw CSVs + scenario assumptions |
| model.Low.stress_cac | 16881.956733295323 | P | unchanged Phase3 formulas; see model output definition stress_cac; raw CSVs + scenario assumptions |
| model.Low.stress_payback | 1.4938282691738942 | P | unchanged Phase3 formulas; see model output definition stress_payback; raw CSVs + scenario assumptions |
| model.Low.program_break_even | 406828.8098976889 | P | unchanged Phase3 formulas; see model output definition program_break_even; raw CSVs + scenario assumptions |
| model.Base.micro.delta_a | 41.088646153846156 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Base.professional.delta_a | 30.672610526315793 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Base.multisite.delta_a | 0.0 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Base.manufacturer.delta_a | 0.0 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.Base.activations | 439.761256680162 | P | unchanged Phase3 formulas; see model output definition activations; raw CSVs + scenario assumptions |
| model.Base.quotes | 940.12 | P | unchanged Phase3 formulas; see model output definition quotes; raw CSVs + scenario assumptions |
| model.Base.delta_a | 71.76125668016198 | P | unchanged Phase3 formulas; see model output definition delta_a; raw CSVs + scenario assumptions |
| model.Base.delta_mrr | 292399.353928104 | P | unchanged Phase3 formulas; see model output definition delta_mrr; raw CSVs + scenario assumptions |
| model.Base.starter_delta_mrr | 162910.33121538465 | P | unchanged Phase3 formulas; see model output definition starter_delta_mrr; raw CSVs + scenario assumptions |
| model.Base.handling | 238349.7395371878 | P | unchanged Phase3 formulas; see model output definition handling; raw CSVs + scenario assumptions |
| model.Base.program | 197800 | P | unchanged Phase3 formulas; see model output definition program; raw CSVs + scenario assumptions |
| model.Base.added_cost | 436149.7395371878 | P | unchanged Phase3 formulas; see model output definition added_cost; raw CSVs + scenario assumptions |
| model.Base.cost | 5975789.739537188 | P | unchanged Phase3 formulas; see model output definition cost; raw CSVs + scenario assumptions |
| model.Base.cac | 13588.713532086742 | P | unchanged Phase3 formulas; see model output definition cac; raw CSVs + scenario assumptions |
| model.Base.payback | 1.23533362777273 | P | unchanged Phase3 formulas; see model output definition payback; raw CSVs + scenario assumptions |
| model.Base.conversion | 8.795225133603239 | P | unchanged Phase3 formulas; see model output definition conversion; raw CSVs + scenario assumptions |
| model.Base.quote_conversion | 46.777140862885794 | P | unchanged Phase3 formulas; see model output definition quote_conversion; raw CSVs + scenario assumptions |
| model.Base.churn | 14.363735585596679 | P | unchanged Phase3 formulas; see model output definition churn; raw CSVs + scenario assumptions |
| model.Base.calls | 2.665371512796247 | P | unchanged Phase3 formulas; see model output definition calls; raw CSVs + scenario assumptions |
| model.Base.digital | 70 | P | unchanged Phase3 formulas; see model output definition digital; raw CSVs + scenario assumptions |
| model.Base.physical | 75 | P | unchanged Phase3 formulas; see model output definition physical; raw CSVs + scenario assumptions |
| model.Base.marginal | 6077.788485242053 | P | unchanged Phase3 formulas; see model output definition marginal; raw CSVs + scenario assumptions |
| model.Base.stress_a | 383.761256680162 | P | unchanged Phase3 formulas; see model output definition stress_a; raw CSVs + scenario assumptions |
| model.Base.stress_cac | 15571.633758010097 | P | unchanged Phase3 formulas; see model output definition stress_cac; raw CSVs + scenario assumptions |
| model.Base.stress_payback | 1.4687729045338112 | P | unchanged Phase3 formulas; see model output definition stress_payback; raw CSVs + scenario assumptions |
| model.Base.program_break_even | 841898.9777337164 | P | unchanged Phase3 formulas; see model output definition program_break_even; raw CSVs + scenario assumptions |
| model.High.micro.delta_a | 64.07106923076924 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.High.professional.delta_a | 47.131215789473714 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.High.multisite.delta_a | 0.0 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.High.manufacturer.delta_a | 0.0 | P | n*(q/n+d1)*(a/q+d2)-a; uplift only core; smb_leads.csv |
| model.High.activations | 479.2022850202429 | P | unchanged Phase3 formulas; see model output definition activations; raw CSVs + scenario assumptions |
| model.High.quotes | 979.6800000000001 | P | unchanged Phase3 formulas; see model output definition quotes; raw CSVs + scenario assumptions |
| model.High.delta_a | 111.20228502024293 | P | unchanged Phase3 formulas; see model output definition delta_a; raw CSVs + scenario assumptions |
| model.High.delta_mrr | 451575.5377214731 | P | unchanged Phase3 formulas; see model output definition delta_mrr; raw CSVs + scenario assumptions |
| model.High.starter_delta_mrr | 251586.27827307704 | P | unchanged Phase3 formulas; see model output definition starter_delta_mrr; raw CSVs + scenario assumptions |
| model.High.handling | 368758.5893982719 | P | unchanged Phase3 formulas; see model output definition handling; raw CSVs + scenario assumptions |
| model.High.program | 197800 | P | unchanged Phase3 formulas; see model output definition program; raw CSVs + scenario assumptions |
| model.High.added_cost | 566558.5893982719 | P | unchanged Phase3 formulas; see model output definition added_cost; raw CSVs + scenario assumptions |
| model.High.cost | 6106198.589398272 | P | unchanged Phase3 formulas; see model output definition cost; raw CSVs + scenario assumptions |
| model.High.cac | 12742.423774419874 | P | unchanged Phase3 formulas; see model output definition cac; raw CSVs + scenario assumptions |
| model.High.payback | 1.222079154831383 | P | unchanged Phase3 formulas; see model output definition payback; raw CSVs + scenario assumptions |
| model.High.conversion | 9.58404570040486 | P | unchanged Phase3 formulas; see model output definition conversion; raw CSVs + scenario assumptions |
| model.High.quote_conversion | 48.91416432102757 | P | unchanged Phase3 formulas; see model output definition quote_conversion; raw CSVs + scenario assumptions |
| model.High.churn | 13.080612851143153 | P | unchanged Phase3 formulas; see model output definition churn; raw CSVs + scenario assumptions |
| model.High.calls | 2.2870565020786526 | P | unchanged Phase3 formulas; see model output definition calls; raw CSVs + scenario assumptions |
| model.High.digital | 85 | P | unchanged Phase3 formulas; see model output definition digital; raw CSVs + scenario assumptions |
| model.High.physical | 85 | P | unchanged Phase3 formulas; see model output definition physical; raw CSVs + scenario assumptions |
| model.High.marginal | 5094.84665081421 | P | unchanged Phase3 formulas; see model output definition marginal; raw CSVs + scenario assumptions |
| model.High.stress_a | 423.2022850202429 | P | unchanged Phase3 formulas; see model output definition stress_a; raw CSVs + scenario assumptions |
| model.High.stress_cac | 14428.557702863529 | P | unchanged Phase3 formulas; see model output definition stress_cac; raw CSVs + scenario assumptions |
| model.High.stress_payback | 1.4443189586757341 | P | unchanged Phase3 formulas; see model output definition stress_payback; raw CSVs + scenario assumptions |
| model.High.program_break_even | 1305210.503508083 | P | unchanged Phase3 formulas; see model output definition program_break_even; raw CSVs + scenario assumptions |
| sensitivity.cac.200000 | 13593.716246551876 | P | (C0+handling+program)/Base A; smb_leads.csv |
| sensitivity.payback.200000 | 1.235788418536722 | P | cost/(baseline MRR+clean ARPU delta); smb_leads.csv |
| sensitivity.cac.500000 | 14275.904582706713 | P | (C0+handling+program)/Base A; smb_leads.csv |
| sensitivity.payback.500000 | 1.2978053408992751 | P | cost/(baseline MRR+clean ARPU delta); smb_leads.csv |
| sensitivity.cac.841899 | 15053.369565217394 | P | (C0+handling+program)/Base A; smb_leads.csv |
| sensitivity.payback.841899 | 1.3684837487591024 | P | cost/(baseline MRR+clean ARPU delta); smb_leads.csv |
| sensitivity.cac.1000000 | 15412.885142964777 | P | (C0+handling+program)/Base A; smb_leads.csv |
| sensitivity.payback.1000000 | 1.401166878170197 | P | cost/(baseline MRR+clean ARPU delta); smb_leads.csv |
| sensitivity.cac.2000000 | 17686.8462634809 | P | (C0+handling+program)/Base A; smb_leads.csv |
| sensitivity.payback.2000000 | 1.6078899527120405 | P | cost/(baseline MRR+clean ARPU delta); smb_leads.csv |
| run_rate.history.1 | 292399.353928104 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| run_rate.starter.1 | 162910.33121538465 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| run_rate.history.2 | 584798.707856208 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| run_rate.starter.2 | 325820.6624307693 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| run_rate.history.3 | 877198.0617843119 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| run_rate.starter.3 | 488730.99364615395 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| run_rate.history.4 | 1169597.415712416 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| run_rate.starter.4 | 651641.3248615386 | P | cohorts*incremental MRR, no churn; not collected ARR; smb_leads.csv |
| reason_crosscheck.micro.base_added_a | 41.088646153846156 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.extra_accepted_quotes | 54.18 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.implied_quote_pool_recovery | 0.22388429752066116 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.implied_postquote_recovery | 0.10581767441860464 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.visit_pool | 484 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.quote_pool | 242 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.visit_downstream_activation | 0.05936319481921209 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.quote_downstream_activation | 0.10912698412698413 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.equal_pool_recovery_to_match_base | 0.7451625192917557 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.micro.alternative_added_a_at_20pct | 11.028103290245761 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.base_added_a | 30.672610526315793 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.extra_accepted_quotes | 24.94 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.implied_quote_pool_recovery | 0.3041463414634146 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.implied_postquote_recovery | 0.12650612244897957 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.visit_pool | 190 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.quote_pool | 82 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.visit_downstream_activation | 0.1597222222222222 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.quote_downstream_activation | 0.25650557620817843 | V | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.equal_pool_recovery_to_match_base | 0.5969677871514533 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| reason_crosscheck.professional.alternative_added_a_at_20pct | 10.276135894258571 | P | explicit disjoint stage pools * historical downstream conversion; assumptions not causal evidence; smb_leads.csv |
| pilot.p0_tier | 0.06268361833695038 | P | original four stratum quotas /1200; smb_leads.csv |
| pilot.p0_segment | 0.06267435495984013 | P | 822/1200*110/2709 +378/1200*138/1247; smb_leads.csv |
| pilot.mde_pp | 4.5123606091014965 | P | normal two-proportion alpha .05 n600/arm target .8; smb_leads.csv |
| pilot.base_lift_pp | 1.81458196509571 | P | Base core activation rate - weighted planning control; smb_leads.csv |
| pilot.base_power_pct | 22.959169016032916 | P | same approximate power at Base core effect; smb_leads.csv |
| pilot.n.core.0.01 | 9905 | P | smallest integer n/arm with normal approximate power>=.8; no clustering/attrition adjustment; smb_leads.csv |
| pilot.n.core.0.02 | 2644 | P | smallest integer n/arm with normal approximate power>=.8; no clustering/attrition adjustment; smb_leads.csv |
| pilot.n.professional.0.01 | 16056 | P | smallest integer n/arm with normal approximate power>=.8; no clustering/attrition adjustment; smb_leads.csv |
| pilot.n.professional.0.02 | 4163 | P | smallest integer n/arm with normal approximate power>=.8; no clustering/attrition adjustment; smb_leads.csv |
| pilot.n.core_segment.0.01 | 9904 | P | smallest integer n/arm with normal approximate power>=.8; no clustering/attrition adjustment; smb_leads.csv |
| pilot.n.core_segment.0.02 | 2644 | P | smallest integer n/arm with normal approximate power>=.8; no clustering/attrition adjustment; smb_leads.csv |
| pilot.n_total | 1200 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.n_arm | 600 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.micro | 822 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.professional | 378 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.days | 90 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.window | 30 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.digital_gate | 70 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.log_gate | 95 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| pilot.unsafe | 0 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| model.program_per_core_lead | 50 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| model.core_n | 3956 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| model.setup | 100000 | A | retained v2 planning design; work/03_pilot_design.json + v2 |
| assumption.model.Low.acceptance_uplift_pp | 1 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.Low.activation_uplift_pp | 3 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.Low.churn_cut_pp | 0 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.Low.call_cut | 0 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.Base.acceptance_uplift_pp | 2 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.Base.activation_uplift_pp | 6 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.Base.churn_cut_pp | 2 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.Base.call_cut | 0.5 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.High.acceptance_uplift_pp | 3 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.High.activation_uplift_pp | 9 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.High.churn_cut_pp | 4 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| assumption.model.High.call_cut | 1 | A | retained v2 scenario parameter, core segments only; work/03_business_model.json + v2 |
| pilot.setup_start | 1 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.setup_end | 14 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.intake_start | 15 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.intake_end | 59 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.followup_start | 60 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.followup_end | 90 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.min_tier | 1 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.max_tier | 2 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.lock_minutes | 10 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.mature_months | 6 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.process_true_pct | 75 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| pilot.process_bad_pct | 60 | A | explicit retained pilot calendar/gate or new process-planning alternative; v2 + evaluation/business_case_evidence.md |
| model.program_allowance | 197800 | A | retained INR50 per core lead *3956 core leads; v2 planning allowance |
| assumption.sensitivity.program.200000 | 200000 | A | scenario input for program-spend sensitivity, not observed cost; explicit sensitivity choice |
| assumption.sensitivity.program.500000 | 500000 | A | scenario input for program-spend sensitivity, not observed cost; explicit sensitivity choice |
| assumption.sensitivity.program.1000000 | 1000000 | A | scenario input for program-spend sensitivity, not observed cost; explicit sensitivity choice |
| assumption.sensitivity.program.2000000 | 2000000 | A | scenario input for program-spend sensitivity, not observed cost; explicit sensitivity choice |
| cost_build.hosting | 1890 | A | dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md; Render public pricing + A planning quantities/rates + T2 specimen hold share |
| cost_build.storage | 3000 | A | dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md; Render public pricing + A planning quantities/rates + T2 specimen hold share |
| cost_build.ocr_compute | 7912 | A | dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md; Render public pricing + A planning quantities/rates + T2 specimen hold share |
| cost_build.future_inference | 7912 | A | dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md; Render public pricing + A planning quantities/rates + T2 specimen hold share |
| cost_build.messaging | 3956 | A | dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md; Render public pricing + A planning quantities/rates + T2 specimen hold share |
| cost_build.review | 94943.99999999999 | A | dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md; Render public pricing + A planning quantities/rates + T2 specimen hold share |
| cost_build.security_ops | 20000 | A | dated public USD hosting reference or explicit planning allocation; see evaluation/business_case_evidence.md; Render public pricing + A planning quantities/rates + T2 specimen hold share |
| cost_build.subtotal | 139614.0 | A | sum planning components; smb_leads.csv |
| cost_build.total | 174517.5 | A | subtotal*1.25 contingency; smb_leads.csv |
| cost_build.hold_share | 0.6666666666666666 | V-proto | automatic held supplied packets/12; T2 measured synthetic packets |
| pilot.process_n | 323 | P | ceil(z.975^2*.7*.3/.05^2), about5pp95% precision; process planning |
| pilot.process_power_pct | 97.69301034776224 | P | P(Bin(n323,p.75)>=ceil(.7*n323)); hypothetical alternative; process planning |
| pilot.process_false_go_pct | 0.007905119350017477 | P | P(Bin(n323,p.60)>=ceil(.7*n323)); hypothetical unacceptable rate; process planning |
| pilot.process_power_at_target_pct | 48.38619938325373 | P | Probability of meeting70% point gate when true rate equals70%; not80%; process planning |
| cost_build.fx_inr_usd | 90 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| cost_build.host_usd_month | 7 | E | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| cost_build.months | 3 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| cost_build.storage_gb | 20 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| cost_build.storage_inr_gb_month | 50 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| cost_build.review_minutes | 6 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| cost_build.review_inr_minute | 6 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |
| cost_build.contingency_pct | 25 | A | Explicit planning policy or dated hosting reference; legal/operational review required; smb_leads.csv |

## Root cause → mechanism → test

| Stage / counted signal | Mechanism | What is and is not established |
| --- | --- | --- |
|Contacted:827 visit losses[V],Micro484/Professional190|Self-discovery with structured facts and Hindi/English templates; no initial salesperson visit prerequisite|T5 proves team scenarios/templates work; no observed visit-loss recovery.|
|Needs assessed:385 complexity/delay[V],Micro242/Professional82|Named, rules-priced bundle and toggleable add-on with immutable version|T3/T4/UI show mechanics. No row attributes loss to a changed accepted quote.|
|Needs assessed:621 price objections[V]|Separate value/affordability question; show starter alternatives and Micro CAC cap|No clarity-based recovery assumed.|
|Quote accepted:273 paperwork/KYC[V]:94 missing document,79 long paperwork,53 absent signatory,47 mismatch|Consent, OCR, exact mock lookup, checksum/date/name/authority checks, typed owned holds|T2 automatic4 clear/8 held; human-confirmed core5/7. OCR adds1 false hold, no unsafe passes vs team labels.|
|KYC complete:220[V]:98 install delay,53 cancelled,41 infeasible,28 first payment|Serviceability and mock first-payment mandate before lock, C-first survey continuation and per-product tracker|T6/T8 show controls/mocked digital lock, never completed real installation.|
|Activated:3.011 untimestamped status calls[V]|Owner-visible product tracker with readiness delay/open states|No actual reduction measured; future call reduction is assumed with a matched window.|

## Change register: v2 → v4

| Change | Why / red flag | Evidence and retained comparison |
| --- | --- | --- |
|Lead with before- and after-acceptance leaks|C1|Raw stage/reason recomputation. v2’s493 post-quote losses remain, but385 is placed before acceptance.|
|Replace0/12 hero with measured core result|C2|CORE-v4 treats date/activity discrepancies as advisory. Raw OCR4/8, human-confirmed5/7. v2 strict all-field0/12 remains historically true; not called OCR yield.|
|Value range and starter upside|H1|Base same+71.761 activations; INR162,910.33 starter value vs292,399.35 historical rule-screened ARPU. No business effect parameter replaced.|
|Planning cost build-up/CAC-parity ceiling|H2|INR174,517.50 planning stress vs retained v2 INR197,800 allowance +100,000 setup; all-in actual cost unknown.|
|Reason-pool cross-check|H3|Base implies22.4%/30.4% quote-process recovery; alternative visit+quote pool model needs74.5%/59.7% equal recovery. Delta model unchanged.|
|Hindi/English templates and conservative boundary|H4|15/15 team scenarios;420 generated boundary trials;30% calls blocked. Marathi next, not implemented.|
|Case-grounded continuity plus public comparison|H5|Working quote version/acceptance/order path; official product-scoped competitor sources. No absence/market-first/single-bill claim.|
|Assisted segment rationale|H6|Catalogue GST/dependency/profile predicates and typical14d SD-WAN /21–30d leased line; good historical payback does not remove feasibility work.|
|Product names rather than codes|H7|Owner labels come from catalogue; exact SKU mapping in footnote. Manufacturer is leased line +managed firewall +machine-monitoring IoT, not CCTV.|
|Mock mandate, DigiLocker and e-sign|H8|Gate tests and API replay. No real external call, funds or legal signature.|
|Cover-only legend, numeric suffixes,≤4 footnotes|H9|Exact main-file copy and text-advance budgets; no actual presentation render.|
|Replace implementation disclaimers with measured evidence|H10|Working prototype/T receipts, with one cover-scope footer. Necessary timing/KYC/model qualifiers remain visible.|
|Fix durable-lock persistence defect|Prototype verification|Global content-hash uniqueness could ignore a new inquiry’s insert. Scoped locks to inquiry, preserved old DB table, asserted persisted hash, added regression test. Screens/T6 rechecked.|
|Retention by document class|Medium/privacy|Draft365d submitted evidence/receipts/logs; abandoned unsubmitted1d. Official Rules2025 referenced; production applicability/keys/auth still need review.|

## Business-assumption preservation

No v2 uplift, activated-row cost proxy, clean-row ARPU basis, INR50/core lead allowance, INR100,000 setup, INR8,088 Micro expansion cap or1,200/600-arm pilot parameter was replaced. The cost build-up is a comparison, not a secretly cheaper model. The process precision requirement323 and its hypothetical75%/60% power calculation are added planning checks, not achieved results. Source and rationale also in `evaluation/CHANGELOG.md`.

## Prototype evidence ledger — current

### T0

Evidence: `evaluation/pytest.xml`

Command: `python -m pytest analysis/test_numbers.py quotelock/tests -q -p no:cacheprovider --junitxml=evaluation/pytest.xml`

V-proto: 448 passing tests; includes durable identical-content/different-inquiry regression.

### T1

Evidence: `evaluation/prototype_evidence.json#T1_boundary`

Command: `python -m evaluation.measure`

V-proto: 420 generated utterances,294 adapter calls,126 blocked,0 leaks. Stand-in adapter, not general LLM evaluation.

### T2

Evidence: `evaluation/prototype_evidence.json#T2_kyc`

Command: `python -m quotelock.kyc.prepare; python -m quotelock.kyc.ocr_tesseract; python -m evaluation.measure`

V-proto: 47 original scans,12 packets; automatic4 clear/8 held. Team-confirmed core5/7;1 false hold K08,0 unsafe passes vs independent team labels. Field accuracy table in JSON.

### T3

Evidence: `evaluation/prototype_evidence.json#T3_quote_time`

Command: `python -m evaluation.measure`

V-proto: 100 scripted, already-filled HTTP requests; current frozen median2.8428ms,p90 4.2628ms. No customer/user/LLM/OCR/network/install claim.

### T4

Evidence: `evaluation/prototype_evidence.json#T4_version + pytest.xml`

Command: `python -m evaluation.measure; pytest test_quote_version_hash_acceptance_and_immutability`

V-proto: Immutable hash999→1348, fresh current acceptance, stale hash rejected. No preview lock/price guarantee.

### T5

Evidence: `evaluation/prototype_evidence.json#T5_advisor`

Command: `python -m evaluation.measure`

V-proto: 15 team-written four-segment Hindi/English scenarios;15 pass. Not the hidden judges pack.

### T6

Evidence: `evaluation/prototype_evidence.json#T6_personas`

Command: `python -m quotelock.demo`

V-proto: Clinic mock lock, Micro no-GST preview/evidence pending, multi-site specialist hold, K06 failure. Durable row asserted.

### T7

Evidence: `evaluation/pytest.xml + numbers.json`

Command: `pytest test_historical_rule_audit_reproduces_56_and_21`

V-proto: 368 activated bundles replayed,56 rule conflicts,21 GST failures; categories overlap.

### T8

Evidence: `evaluation/asset_manifest.json`

Command: `python -m evaluation.capture; python -m evaluation.confirm_tracker_asset`

V-proto: Actual local UI panels/excerpts, enlarged accessibility scale. Code-derived architecture has exactly6 nodes/9 edges; captures contain no source IDs. Tracker rechecked against durable SQLite state.

### T9

Evidence: `evaluation/identity_binding_regression.md + pytest.xml`

Command: `pytest test_unbound_no_gst_preview_cannot_accept_another_business_packet`

V-proto: New regression failed before the fix; current448-pass suite checks acceptance409 and legacy/manual lock bypass held. No-GST alternative evidence remains pending, not exempt.

### Assets — verification

| File | Pixels | SHA-256 | Scope |
| --- | --- | --- | --- |
| s4_quote_card_v1_v2.png | [1328, 530] | 3907c1d95386be580f757e548a6006284057eedaff313b3c7460fd5a7d056a27 | Synthetic live quote versions, pre-tax midpoint; fresh-acceptance requirement captioned natively on slide |
| s5_kyc_k06_hold.png | [780, 738] | a7cdb82d8b93a6d4c396a820dc7ab88aeb634f7e896e1e2cbde73ba282e207ca | K06 fresh-OCR hold excerpt; no source identifier exposed |
| s5_architecture.png | [2000, 890] | c60b49eefb81bef42d7fcaa8ec7acf26ec008f4fdf18135d253803ad719ddd99 | Six implementation nodes; dashed boundary around A2 stand-in only; nine data paths |
| s6_backoffice_queue.png | [1700, 508] | 66f73d67fe5a0078bb404ee295d0895646847ceffefe6051062eff0047efe522 | Live queue excerpt: reason, owner, next action and age; role filter is demo-only |
| s6_tracker.png | [900, 520] | 9275b857170d2b47da892191776dd5f81e428c731706058860353976011518dc | Live first-product tracker excerpt: mocked order locked; physical provisioning still pending |

## KYC outcome table — automatic vs team-confirmed

| Packet | Automatic | Team-confirmed core | Automatic blocking reasons |
| --- | --- | --- | --- |
| K01 | hold | hold | gst_checksum, gst_registry_mismatch, udyam_missing_number, applicant_unknown |
| K02 | core_checks_clear | core_checks_clear |  |
| K03 | core_checks_clear | core_checks_clear |  |
| K04 | hold | hold | blur, gst_unreadable, ocr_uncertain_legal, ocr_uncertain_address |
| K05 | hold | hold | missing_udyam_certificate, udyam_missing_number |
| K06 | hold | hold | gst_checksum, gst_registry_mismatch |
| K07 | hold | hold | gst_checksum, gst_registry_mismatch, legal_mismatch |
| K08 | hold | core_checks_clear | gst_checksum, gst_registry_mismatch |
| K09 | core_checks_clear | core_checks_clear |  |
| K10 | hold | hold | gst_checksum, gst_registry_mismatch, authority_review |
| K11 | hold | hold | gst_checksum, gst_registry_mismatch, address_stale |
| K12 | core_checks_clear | core_checks_clear |  |

Per-field accuracy is computed from nonempty team-transcribed source fields, punctuation/spacing normalized for names/addresses; identifiers are exact. No registry value or expected answer is substituted for an unreadable OCR value. Runtime extraction cannot read the ground-truth fixture. K08’s extra identifier hold is disclosed, not tuned away. No judge answer key was accessed.

## Full source ledger — archived v2, intact

The following is the original v2 ledger, retained verbatim as historical provenance. Its proposed/strict-scope statements are not current implementation claims. Current changes, measurements and policies above supersede only the explicitly logged parts.



### T0 — template specification

VERIFIED: `work/00_env.md`, completed Phase 0 geometry. ASSUMPTION: Revised allocations and text sizes are written production instructions only; no rendering, image inspection or font-fit test occurred in v2.

### D1 — supplied funnel and economics

VERIFIED: `work/extracted/YTL_TrackA_Udyam_Digital_Data/smb_leads.csv`; Phase 1 `01_core_metrics.json`, `01_funnel.csv`, `01_segments_economics.csv`, `01_channel_groups_economics.csv`; matched subset in `02_challenge_evidence.json`. All are fictional Accel synthetic data. Lead source SHA-256 `b2521e8cedcf3b5775a087d40d07f548afbe3e7094a9fbad3a3908ffb01120ea`.

VERIFIED: Baseline cost INR5,539,640 /368 = CAC INR15,053.369565. Monthly recorded value INR4,544,990; gross revenue payback 1.218845 months. Micro cost INR2,200,780/110 = INR20,007.090909 CAC; observed monthly value INR275,530/110 = INR2,504.818182; payback 7.9874 months. Professional cost INR1,475,870/138 = INR10,694.710145; observed monthly value INR937,830/138 = INR6,795.869565. Historical ARPU mixes do not equal proposed starter prices.

VERIFIED: Matched Micro uses Website/WhatsApp/Inbound/Referral only: 1,247 leads, 53 activations, INR427,620 cost; CAC INR8,068.301887, conversion 4.250200%. Of 1,278 no-GST Micro leads, 771 also lack Udyam. ASSUMPTION: No-GST/N-only offers preserve identity/evidence requirements and assisted holds; optional exact mock one-ID prefill does not become compulsory registration.

### D2 — supplied catalogue and tariff assumptions

VERIFIED: `product_catalogue.csv`, source SHA-256 `5110529705bda36f668cfc92e7de943a4d3c6d5b7f78ae35c4d7b0484a136e0c`; `03_commercial_temporal.json` retains source CSV rows, SKU dependencies, quantities, profile eligibility and exact endpoint arithmetic for all four bundles. ASSUMPTION: Version MIDPOINT-v1 selects (min+max)/2 per purchased unit, setup/unit, common term=max and no discount. Tax/other-charge treatment is unknown. Unknown commercial authority or charges prevent a binding total. GSTIN=N means the product does not require GSTIN, not KYC exemption or serviceability approval.

VERIFIED catalogue facts / ASSUMPTION illustrative quote choice: P04 midpoint INR999, P07 INR349, combined INR1,348. Slide 4 v1 is P04×1 (range899–1099); v2 adds P07×1 (combined range1198–1498). Both setup0 and common minimum6mo under the stated profile/policy. The illustrative addition is INR349/month, not a provider-approved final payable price.

PROJECTION [R1]: Micro revenue ceiling at h months = 1,348×h: INR8,088 /16,176 /32,352 for 6/12/24 months. Historical Micro CAC /1,348 =14.842056 months; historical Professional CAC /3,505.50 =3.050837 months. These constant-revenue illustrations ignore service costs, margin, churn, discounting, tax and collection; they cannot establish contribution/profit break-even. Setup receipts are not counted as recurring value. The six-month ceiling is a chosen conservative expansion policy, not a supplied rule or validated affordable CAC.

PROJECTION [R1]: Matched Micro ceiling headroom =8,088−8,068.301887 =INR19.698113. At unchanged 53/1,247 conversion, an added INR50/lead alone costs INR1,176.415094 per activation. Thus the matched history does not establish the gate is attainable. The Phase 3 Base Micro blended CAC INR16,193.77 also fails the chosen gate. ASSUMPTION: Professional leads the bounded process exercise; Micro receives a limited, capped cost-discovery tranche. No Micro volume expansion until measured fully loaded acquisition CAC, including allocated setup, satisfies the ceiling. If it cannot, hold that expansion; do not silently change price or target.

### D3 — supplied registry and KYC audit

VERIFIED: `01_catalogue_registry.json`, `01_catalogue_bundle_violations.csv`, `01_kyc_audit.json`, `01_kyc_ocr.json`. Supplied-snapshot hard-rule conflict union56/368, active-GST failures21 within that union, categories overlap. Recorded monthly value of affected rows INR768,830. These current mock statuses do not prove historical legal eligibility or an actual future rejection rate.

VERIFIED: 47 original documents, 12 packets. Strict all-checked-field-clear0/12; limited-core exceptions/review7/12; numbered Udyam registry-date differences10/10, four also activity differences. K04 blur; K08 has no detected core name/address mismatch; K10 contact/signatory difference needs authorization review, not a fraud label. No source packet is called clean, altered or converted into an OCR-accuracy claim. ASSUMPTION: Preserve required holds and original images. Evidence sufficiency and adjudication policy need specialist approval.

### D4 — Phase 3 model, unchanged

VERIFIED model arithmetic / ASSUMPTION inputs / PROJECTION effects: `03_business_model.py/.json`, `03_business_case.md`, `03_validation.json`. Normalized 5,000-lead historical segment mix; only Micro/Professional receive hypothetical uplift. This is not the staged pilot forecast. Core lead→initial-interest increases1/2/3pp and initial-interest→activation3/6/9pp for Low/Base/High. Other segments remain flat. Model effects must be net of required gates/holds.

PROJECTION: Base activation439.761256680162, increment71.761256680162 = Micro41.088646153846 + Professional30.672610526316. Fractional counts are model expectations, not people observed. Base ΔMRR =41.088646153846×(251,000/103)+30.672610526316×(702,070/112) =INR292,399.353928/month. Value uses same-segment ARPU from rows with no detected supplied-hard-rule conflict: INR2,436.893204 and INR6,268.482143. It is a retained historical value-mix assumption, not statutory approval, validated future ARPU or the Slide 3 starter-price forecast. No collected ARR, profit or churn-derived saving is asserted.

ASSUMPTION: Incremental activation handling uses historical **activated-row** acquisition cost proxies, Micro INR2,688.454545 and Professional INR4,169.347826. These omit no baseline spend, but are unvalidated marginal-cost proxies, not measured tariffs or commission rates. Added recurring spend =41.088646153846×2,688.454545 +30.672610526316×4,169.347826 +50×3,956 =INR436,149.739537. Program allowance INR197,800 is included; INR100,000 setup is separate. Both allowances are planning choices, not supplier quotes or proven full implementation costs.

PROJECTION: Marginal acquisition cost per **added** activation =436,149.739537/71.761256680162 =INR6,077.788485. Base blended recurring CAC =(5,539,640+436,149.739537)/439.761256680162 =INR13,588.713532. Baseline blended CAC =5,539,640/368 =INR15,053.369565. Different denominators explain the different figures. With separate setup, marginal cost becomes INR7,471.298084 and blended CAC INR13,816.109644. Neither is a measured Micro CAC or proof of cash savings.

PROJECTION: Revenue payback =cohort acquisition spend /cohort monthly recurring value. Base5,975,789.739537 /(4,544,990+292,399.353928) =1.235334 months versus1.218845. Incremental monthly value/customer is INR4,074.613064 versus baseline INR12,350.516304. ASSUMPTION: Acquisition cost is booked upfront in this revenue-coverage convention; actual cash timing is not supplied. Lower added value mix explains why CAC can improve while payback rises. This is not margin/cash-flow payback.

PROJECTION: Enforcement stress retains full cost but withholds56 activations and INR768,830 monthly recorded value: Base383.761257 activations, CAC INR15,571.633758, payback1.468773 months. It is an evidence-anchored downside, not a forecast rejection rate. Retaining historical value in the main model does not make known conflicts valid.

ASSUMPTION: Initial interest freezes the first conditional proposal-interest timestamp before KYC; historical accepted quote precedes KYC and is not final verified acceptance. Lock is a separate durable event. Routine timing starts at first preview for preclassified fully verified routine inquiries, ends at durable lock, never resets on a version, and counts holds/failures/abandonment as missed under-ten-minute locks. Physical denominator is ready product lines with readiness delay shown separately; typical days are not guaranteed SLAs. Historical mean17.6168 lead-to-activation days is a different clock. Six-month targets require complete activation+six-calendar-month observation; calls require matched prospective windows. Low/Base/High core churn reductions0/2/4pp and call reductions0/.5/1 are assumed and not monetized.

### D5 — temporal integrity

VERIFIED: `01_secondary_signals.json` and `03_commercial_temporal.json`: full368 activations include16 after2026-07-15;352 are dated by then. No activated cohort has six months of observation at the reference date. Historical churn56/368 is a supplied synthetic flag, not a matured survival estimate; follow-up call windows are unspecified. Do not relabel this as real Airtel data or achieved pilot performance.

### D6 — proposed product and operating controls

ASSUMPTION: Approved concept `02_concept.md`, `03_business_case.md`, supplemented by this revision. Optional exact mock GSTIN/Udyam prefill; no-ID continuation; three normal discovery prompts followed by clarification/hold when required; C-first routing; deterministic commercial authority; reason-coded human ownership; separate digital and physical clocks. No universal zero typing, instant KYC, INR4,500 Micro target, automatic evidence pass, trained propensity, guaranteed install, discovery cash saving or live registry/e-sign entitlement is claimed.

ASSUMPTION: The memorable AI hook is a strict proposed data-flow policy. Money/budget fields bypass the model to structured deterministic inputs. Redaction must remove volunteered monetary text, prices and identifiers; uncertain redaction blocks the call. The model never receives catalogue rows, quote cards or order-write capability. Deterministic templates render/translate approved commercial outputs. No claim is made that a pretrained model lacks price knowledge or that these boundaries have been implemented/tested.

ASSUMPTION: Privacy line expands to purpose-specific multilingual consent, necessary-field collection, masked logs, restricted encrypted evidence/identifier storage, role-scoped partner handoff, accountable retention/deletion and withdrawal handling. Retention schedules, lawful evidence policy and provider access must be approved before real collection. These are design choices, not DPDP/telecom compliance certification. A2's named model is proposed, not an accuracy/latency/cost result.

### R1 — v2 arithmetic receipt

VERIFIED arithmetic under the above ASSUMPTION inputs: `work/revision_v2/calculations.json` records the exact Base reconciliation, Micro ceilings and sample-size calculations. Prior Phase 3 files are unchanged.

### R2 — replacement pilot decision protocol

ASSUMPTION: This revision supersedes the previous conversion-point/CI/CAC-ratio advancement gate **for this proposed pilot**. The 90-day exercise validates feasibility, safety, process and cost measurement. Conversion is directional, with arm counts and uncertainty, never a mandatory positive-lift gate or superiority proof. Any concerning harm signal still triggers investigation and containment; lack of significance is not evidence of no harm.

ASSUMPTION: Retain up to1,200 new core inquiries,600/arm, both city tiers; original quotas Micro822/Professional378, randomized within segment×tier. Run Professional readiness first, with a bounded Micro cost-discovery tranche, then progress only if staffed/safe. Both arms use the same mandatory evidence/consent/catalogue protections and contemporaneous tariff. If Micro expansion gate/capacity fails, do not replace Micro with Professional silently or claim the old mix/power; report recruitment shortfall, resize and freeze a revised protocol before new enrollment. Limited learning enrollment is not permission for economic expansion. Actual tranche size and approved spend cap must be set before recruitment because capacity/rates are not supplied.

ASSUMPTION: Days1–14 freeze/rehearse controls and funded queues; days15–59 intake; days60–90 follow-up/report. Every assigned inquiry remains in its original arm/denominator, including holds, no-ID cases, abandonment and later complexity; deduplicate before assignment. Observe all accepted-bundle products activated within30 days from assignment, last day59 entrant throughday89. Conversion readout is descriptive ITT with uncertainty and strata; prospective component-level endpoint differs from historical single Activated label. Continue physical/retention follow-up afterday90.

ASSUMPTION: Go **only to designing/funding a larger controlled test** requires all of: ≥70% of all preclassified routine preview starts reach durable lock within10 minutes; ≥95% required-event completeness; every hold reason-coded and assigned an owner; observed hold rate translated to queue workload within pre-agreed staffed capacity; zero unsafe locks and zero privacy incidents; reconciled full costs within a pre-approved cap. No trustworthy numeric “low hold rate” threshold can be derived from the supplied12 specimens, so none is invented. Hold/repair if time/logging/ownership/capacity or cost data fail; stop immediately for an unsafe lock, required-gate bypass, privacy incident or invented serviceability/activation state. Passing does not establish profit, production safety, causal lift or six-month retention.

PROJECTION sample planning: At the original quota-weighted historical core p0=.062683618337, n600/arm has approximate80%-power MDE+4.512361pp. Phase3 Base core expected lift is about+1.814pp, smaller than that MDE. For a **chosen +2pp** effect, the same two-sided independent two-proportion normal approximation, alpha.05 and80% power requires **2,644/arm,5,288 total**. A Professional-only population at historical138/1,247 requires **4,163/arm,8,326 total**. These are conditional planning counts, not a supplied recruitment forecast or exact power guarantee. Redetermine sample from actual eligible mix/control rate, clustering, missingness and operational changes before registration; no claim that the larger test fits90 days. A +1pp core effect would need9,905/arm under the same approximation.

ASSUMPTION formula: p1=p0+δ, pbar=(p0+p1)/2, cutoff=1.959964×sqrt(2×pbar×(1−pbar)/n), se=sqrt((p0(1−p0)+p1(1−p1))/n). Approximate power=1−Φ((cutoff−δ)/se)+Φ((−cutoff−δ)/se). Counts are the smallest integer n giving≥.80 with this method. It ignores clustering, attrition, multiplicity and potential stratification efficiency. Sample arithmetic does not validate historical p0 as the same30-day endpoint.

### External ledger — official public evidence only

EXTERNAL: All following public pages were read on **2026-11-08**. Sources are product-scoped, not exhaustive/provider-wide journey tests. No OTP, form, account, order or provider contact was submitted. PDF source text was read without rendering/exporting. No competitor is said to lack a capability. No price-equivalence, universal-online-KYC, first/only, speed, language-accuracy or performance-superiority claim follows.

| ID | Official source / URL | Documented claim and locator | Scope limit |
| --- | --- | --- | --- |
| EXTERNAL J1 | [JioBusiness Solution](https://www.jio.com/business/services/connectivity/jiobusiness-solution/) | Tariff section with quarterly/half-yearly/annual choices and promotional/installation/GST notes; self-care plan/bill/request description. | Public notes do not establish a customer-specific binding quote or all current plan prices. |
| EXTERNAL J2 | [JioBusiness FAQ](https://jep-asset.akamaized.net/enterprisestaticresources/prod/v01/en-pdf/JioBusiness_Solutions_FAQ.pdf) | §33 Business CAF following document verification, handed to installation engineer; §34 self-care order status. | Undated/legacy public FAQ retrieved today; not verified as current universal KYC or July archive. |
| EXTERNAL T1 | [TTBS SmartOffice](https://www.tatatelebusiness.com/data-services/smartoffice/) | Voice/data/storage/apps bundle; callback/mobile-OTP inquiry form. | Specific offering and inquiry route; no absence of online checkout inferred. |
| EXTERNAL T2 | [TTBS Smartflo rates](https://www.tatatelebusiness.com/features/smartflo-call-center-solutions/) | “A Plan for All Your Needs”: named monthly/per-license or concurrency rates and one-time charges; Lite tenure footnote. | Smartflo, not SmartOffice. Numeric tariffs are not used in Accel economics or an apples-to-apples price claim. |
| EXTERNAL T3 | [Smartflo Business Information](https://docs.smartflo.tatatelebusiness.com/docs/business-information) | Business Information documentation lists GST, PAN and KYC forms. | Documents portal fields, not automatic verification or an end-to-end KYC test. |
| EXTERNAL T4 | [Smartflo service requests](https://docs.smartflo.tatatelebusiness.com/docs/service-request-sr) | DBCH/self-care support procedure includes View Ticket, new ticket and generated ticket ID. | Post-activation support-ticket management, not proved order-activation tracking. |
| EXTERNAL V1 | [Vi corporate postpaid](https://www.myvi.in/business/enterprise-mobility/corporate-postpaid-plans) | Three purchase steps: plan/number choice, documents/assisted doorstep KYC and SIM delivery; corporate connection dashboard description. | Corporate mobility route. Exact price cards are dynamic in retrieved page text, so no numeric Vi tariff is asserted. |
| EXTERNAL V2 | [Vi Business Assist](https://www.myvi.in/business/blog/vi-business-assist-wins-silver-feather-award) | ViBA platform description: mobility/fixed-line account management, billing/payments; usage/bill functions described. | Provider blog, not transaction testing or measured QuoteLock comparison. |
| EXTERNAL V3 | [Vi public SIM status](https://www.myvi.in/new-connection/track-your-sim-online/) | Mobile-number/OTP status route; delivery, KYC, rejection/activation UI states in page text. | Public/consumer connection page. Static example states are not a real order; corporate applicability unverified. |
| EXTERNAL M1 | [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B) | Official model identity retained from Phase5 source check. | Identity only; no tested Indian-language, extraction, price-filtering or cost claim. |
| EXTERNAL P1 | [MeitY DPDP Act 2023](https://www.meity.gov.in/static/uploads/2024/02/Digital-Personal-Data-Protection-Act-2023-1.pdf) | Official Act text retained as legal-review reference. | No current applicability/commencement conclusion or compliance certification. |

EXTERNAL exclusion: TTBS `/kyc-forms/` is under Investor Updates/SEBI, so it was rejected as telecom-customer KYC evidence. Unofficial aggregators, UAT tariffs, consumer-to-enterprise transfer and untested quote-version behavior were also excluded. Pricing/onboarding/tracking dimensions with uneven scope are summarized rather than filled with repeated “Not assessed.”



## New official external references

| ID | Official page / access date | Supported scope |
| --- | --- | --- |
|E20|https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf ;2026-11-08|G.S.R.846(E),13Nov2025,Rule1: immediate rules1,2,17–21;Rule4 after1year;Rules3,5–16,22,23 after18months. Core period approximatelyMay2027. This is original Gazette text, not a legal applicability certification.|
|E21|https://render.com/pricing ;2026-11-08|Official public Starter USD7/month reference; dynamically rendered page/search extract, not an individualized hosting quote. FX/quantity/storage and staffing budgets are assumptions.|
|E22|https://tesseract-ocr.github.io/tessdoc/Installation.html ;2026-11-08|Official installation guidance. Windows5.5.3 package from https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.3 ;English data from https://github.com/tesseract-ocr/tessdata_fast .|
|E23|https://fastapi.tiangolo.com/tutorial/testing/ ;2026-11-08|Official TestClient testing approach. No software-version/performance claim inferred from docs.|

Public sources were inspected on actual evaluation date2026-11-08, not synthetic case date2026-07-15. No registry/DigiLocker/e-sign/payment credentials or real transactions were used. Jio callback, TTBS SmartOffice callback and Vi assisted KYC are documented routes, never provider-wide absence claims. Vi contacts within48h; completing KYC within48h is not established.

## Case coverage

| Requirement | Visible slides | Evidence |
| --- | --- | --- |
|Q1 segments/products/price/contract|3,7|Catalogue choices, observed economics, cap, ranges/setup/common term, assisted rationale.|
|Q2 needs/language|2,4,5|Three structured topics, Hindi/English templates, T5, fail-closed boundary; Marathi future.|
|Q3 near-instant KYC/privacy|5|Real OCR/deskew/core checks and conservative holds; mock lookups/DigiLocker/e-sign; consent/retention controls. No instant universal pass claim.|
|Q4 field/partners|6|C-first queue, owner/action/age, attributed closure credit, no assumed cash savings.|
|Q5 metrics/targets|7|Five groups with V/A/P/V-proto separation, powered process planning, conversion next study.|
|Advisor|4,5|Working rules-based slot stand-in, structured budget, deterministic bundle variants. Actual GenAI model integration not evaluated.|
|Quote/checkout|3,4,5|Owner product names, toggled add-on, hash/version/current acceptance, mandate/serviceability/charge gates.|
|Smart KYC|5|Upload, extraction/validation, consent, mock GSTIN/Udyam/DigiLocker, typed holds; actual OCR false hold disclosed.|
|Tracker|6,7|Digital lock and per-product readiness/durations separate; no invented activation feed.|
|Approach/competition/impact|3–6 /4 /7|One priced multi-product spine, official scoped comparison, conditional business model.|
|Case prototype/repo/privacy/architecture|4–6 and source files|Local prototype and tests, code-derived diagram, quotelock/PRIVACY.md. No3-minute video or PPT/PDF created; outside this request.|

## Headline-only sequence

1. QuoteLock
2. 1,113[V] leave before acceptance; 493[V] leave after
3. Professional first; Micro must earn its acquisition-cost ceiling
4. One bundle quote becomes the verified order record
5. Rules decide; uncertain evidence holds the order
6. Exceptions keep an owner; installation keeps its own clock
7. Base adds 72[P] activations; pilot tests safe, fast processing

## Current competitor scope — supersedes archived interpretations

| IDs | Verified documentation on2026-11-08 | Claim limit |
| --- | --- | --- |
|J1/J2|JioBusiness tariff/charge notes and callback; legacy FAQ§33 documents/CAF and engineer,§34 self-care order status|No verified Buy Plan transaction, provider-wide capability comparison or current universal KYC entitlement.|
|Tt1/Tt3/Tt4|SmartOffice bundled voice/data/apps and callback; Smartflo business-information KYC fields and service-request tickets|Smartflo is a different product scope; tickets do not establish an order tracker. No price-absence claim.|
|V1/V2|Vi corporate plan choice/order and assisted delivery KYC; representative contacts within48h. ViBA account/billing/usage self-service|48h is contact, not completed KYC. Do not use the archived consumer SIM tracker as corporate-order proof.|

URLs are in the archived ledger and main-file hyperlink table. These are public documents, not transaction tests, July2026 snapshots or evidence that a competitor lacks any feature.

## Additional model and denominator detail

Micro starter revenue ceilings at6/12/24months are INR8,088/16,176/32,352; keys micro.ceiling.6/.12/.24. They exclude margin, churn and cost of capital. Only the existing INR8,088 expansion gate is used. Base Micro CAC remains INR16,193.77 and fails it. Professional-first sequencing therefore does not make the unchanged whole-cohort model a pilot forecast.

Slide7 scorecard pairs follow row-label order; Low/Base/High are distinct scenarios, not confidence intervals. CAC=all acquisition spend/activations; revenue payback=spend/monthly value. Physical within-typical denominator is provisioning-ready product lines; report readiness delay separately. Routine-lock denominator includes every routine preview start, failures/holds included. Conversion uses30-day ITT over all randomized inquiries, complete bundle active; supplied historical Activated is a coarser label. Log completeness is required events present/all required events.

Need323 routine starts for approximate precision; hypothetical75% true vs60% bad yields97.693% advancement probability at the unchanged≥70% observed gate. At true70%, it is48.386%, not97.7%. This process planning is not field achievement or power to detect the expected conversion lift. MDE4.512pp at600/arm exceeds Base core1.815pp; approximate power23%. Next+2pp needs2644/arm at original mix,4163 if Professional-only; re-size before enrolling.

## Prototype and business limits

All measured performance is scripted synthetic behavior on this machine, with a rules-based intent stand-in. No owner research, field lift, real API entitlement, actual installation or legal certification. Business recovery rates, ARPU persistence, program allocations and reviewer time are hypotheses. Submitted synthetic evaluation fixtures remain developer-only plaintext files; the runtime upload vault is encrypted. Ephemeral keys and spoofable demo-role headers are not production authentication/key management. Raw originals are never modified. Retention/deletion scheduling, backups and immutable-quote archival remain production work; the expiry helper covers encrypted evidence rows.

The1,200/600-arm pilot keeps original822/378 segment quotas and four segment×tier strata. If staged Micro economics/capacity prevent quotas, report shortfall and resize before new enrollment; never silently substitute Professional leads. Go permits designing/funding a larger controlled test only. Six-month outcomes continue beyondDay90.
