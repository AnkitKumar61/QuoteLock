# Business-case evidence

All data are fictional Accel synthetic. Labels: V supplied data, V-proto measured synthetic prototype, E public source, A planning assumption, P projection. No projected acquisition effect is validated by the prototype.

Command: `python analysis/numbers.py` then `python -m evaluation.business`

## Cost build-up and retained allowance

The v2 program allowance remains INR50×3,956=INR197,800 per5,000-lead cohort, plus INR100,000 setup. It is not replaced by the build-up below. All historical spend and the added activation-handling proxy INR238,349.74 remain counted. Do not add review costs twice when actual operations reveal overlap with the handling proxy.

| Item | Planning INR/cohort | Basis / label |
| --- | ---: | --- |
| hosting | 1,890.00 | E reference: Render Starter USD7/month, accessed2026-11-08, https://render.com/pricing . A:3 months ×INR90/USD, not a current exchange-rate claim or a complete deployment quote. |
| storage | 3,000.00 | A:20GB retained evidence/backups×3mo×INR50/GB-month, reserved allocation; no vendor rate asserted. |
| ocr_compute | 7,912.00 | A:INR2/core lead for self-hosted OCR compute/ops. Tesseract license has no per-document API bill; actual CPU/storage are not free. Fresh scan runtime recorded separately. |
| future_inference | 7,912.00 | A:INR2/core conversation reserve for a later model. Current rules stand-in makes no inference API call; future LLM pricing/quality unvalidated. |
| messaging | 3,956.00 | A:INR1/core lead, notification allocation. No WhatsApp/voice vendor quote. |
| review | 94,944.00 | A stress:8/12 V-proto held specimens×3,956 core leads×6min/hold×INR6/min. Specimens are adversarial, not a random population;6 minutes and labour rate are assumptions, not a timed human study. |
| security_ops | 20,000.00 | A:INR20,000/cohort QA, access/deletion checks and operating support reserve; no supplier quote. |
| Subtotal | 139,614.00 | A: sum |
| With25% reserve | 174,517.50 | A: not an observed cost |

P: CAC-parity program-spend ceiling = A_base×CAC_baseline−C0−incremental handling = INR841,898.98. It is NOT profit/cash break-even. Setup reduces that recurring headroom by INR100,000 if allocated to this cohort. The bottom-up stress allocation of INR174,517.50 is below the retained INR197,800 allowance, but much higher staffing, messaging or inference cost can erase headroom.

Partner principle (A): Preserve attributable credit for verified closure and physical completion. Price the rate and work explicitly before rollout; do not double count a new bonus on top of the historical activated-row handling proxy or claim existing partner work vanishes. No new commission rate is asserted.

## Program-spend sensitivity

| Program spend INR | Blended CAC INR | Revenue payback months |
| --- | ---: | ---: |
| 200,000.00 [P] | 13,593.72 [P] | 1.2358 [P] |
| 500,000.00 [P] | 14,275.90 [P] | 1.2978 [P] |
| 841,898.98 [P] | 15,053.37 [P] | 1.3685 [P] |
| 1,000,000.00 [P] | 15,412.89 [P] | 1.4012 [P] |
| 2,000,000.00 [P] | 17,686.85 [P] | 1.6079 [P] |

Revenue payback uses retained baseline MRR plus historical rule-screened incremental value; it is not margin/collection payback. Revenue at starter prices is lower.

## Value basis and run-rate

P: Base+71.761257 activations gives INR162,910.33/month at displayed starter prices versus INR292,399.35/month at same-segment rule-screened historical ARPU. This is a value-mix sensitivity range, not a confidence interval. A: Upsell only on confirmed needs: additional seats or eligible add-ons produce a new rules-priced version and fresh acceptance. No upsell rate is assumed.

| New quarterly cohorts | Starter-value added MRR | Historical-value added MRR |
| --- | ---: | ---: |
| 1 [A] | 162,910.33 [P] | 292,399.35 [P] |
| 2 [A] | 325,820.66 [P] | 584,798.71 [P] |
| 3 [A] | 488,730.99 [P] | 877,198.06 [P] |
| 4 [A] | 651,641.32 [P] | 1,169,597.42 [P] |

P: Each cohort repeats the unchanged5,000-lead mix and assumed effect. All prior added services retained, no churn, no additional capacity constraint. This is a monthly run-rate at that point, not collected ARR, profit or a recruitment forecast.

## Reason-pool cross-check

{
  "micro": {
    "base_added_a": 41.088646153846156,
    "extra_accepted_quotes": 54.18,
    "implied_quote_pool_recovery": 0.22388429752066116,
    "implied_postquote_recovery": 0.10581767441860464,
    "visit_pool": 484,
    "quote_pool": 242,
    "visit_downstream_activation": 0.05936319481921209,
    "quote_downstream_activation": 0.10912698412698413,
    "equal_pool_recovery_to_match_base": 0.7451625192917557,
    "alternative_added_a_at_20pct": 11.028103290245761
  },
  "professional": {
    "base_added_a": 30.672610526315793,
    "extra_accepted_quotes": 24.94,
    "implied_quote_pool_recovery": 0.3041463414634146,
    "implied_postquote_recovery": 0.12650612244897957,
    "visit_pool": 190,
    "quote_pool": 82,
    "visit_downstream_activation": 0.1597222222222222,
    "quote_downstream_activation": 0.25650557620817843,
    "equal_pool_recovery_to_match_base": 0.5969677871514533,
    "alternative_added_a_at_20pct": 10.276135894258571
  }
}

P: Base implies recovering22.39% of the Micro quote-process pool and30.41% of Professional to add conditional quote interest; its later conversion uplift is about10.58%/12.65% of each segment’s historical post-quote losses. An alternative model using equal recovery of the disjoint visit and quote pools, at observed stage-to-activation rates, needs74.52%/59.70% recovery to match Base. At an explicitly assumed20% recovery it adds only11.03+10.28≈21.30 activations. These are demanding assumptions, not causal evidence; price objections are not included. The v2 delta model remains primary as instructed, with this cross-check visible.

## Pilot process endpoint and conversion power

P: At least323 routine starts support approximately±5pp95% planning precision near70%. For the unchanged point gate≥70%, exact-binomial probability of going is97.69% if the hypothetical true rate is75%, and0.0079% if it is60%. At true70%, advancement probability is only48.4%. These75/60 planning alternatives are assumptions; they do not establish pilot performance.

A: If fewer323 routine starts occur among600 treatment inquiries, hold/revise/extend the controlled process study; do not exclude new holds or count only successful locks. All routine preview starts remain in the speed denominator; every assigned inquiry remains in30-day ITT conversion. Log completeness uses all required events in both arms. Zero safety incidents is a hard-stop tolerance, not proof that future risk is zero.

P: The original four-stratum core planning rate is0.062683618, different from the review’s collapsed-segment0.062674355. MDE4.512pp exceeds Base core lift1.815pp, approximate power23.0%. Next +2pp conversion test requires2,644/arm at the original mix or4,163/arm if Professional-only. Re-size before enrollment; no claim it fits90 days.

## Five KPI definitions

| KPI | Definition and limitation | Baseline / target |
| --- | --- | --- |
| Lead activation | all accepted products active within30d/assigned inquiries, ITT; historical file has a single Activated label | V7.36%; P8.05/8.80/9.58% full-mix model, not pilot forecast |
| Priced quote time | first request to persisted priced preview; report owner end-to-end separately | V case3–5days; V-proto scripted median/p90 in T3; A same-session owner target |
| CAC/revenue payback | all acquisition spend, converters and non-converters / activations; spend / monthly value | V15,053/1.219; P Low/Base/High in numbers.json; no profit or cash claim |
| Dual clock | routine first-preview→durable lock, all starts; product-ready→physical activation; report readiness delay | P digital45/70/85%,physical60/75/85% within source typical, never guaranteed |
| Retention/status calls | full6-calendar-month matured outcomes, timestamped status-chase calls over matched window | V15.22% immature flags,3.011 unspecified-window calls; P15.53/14.36/13.08% and3.020/2.665/2.287; not monetized |