# Measured prototype evidence

V-proto: scripted synthetic API sessions, not user research, customer latency, field pilot or an LLM benchmark

Command: `$env:PYTHONPATH="quotelock/vendor"; python -m evaluation.measure`

Tests command: `python -m pytest analysis/test_numbers.py quotelock/tests -q -p no:cacheprovider --junitxml=evaluation/pytest.xml`

## T1_boundary
```json
{
  "trials": 420,
  "model_slot_calls": 294,
  "blocked": 126,
  "blocked_pct": 30.0,
  "leaks": 0,
  "method": "Seed8621,420 generated English/Hindi/Hinglish utterances; independent regex leak oracle; deterministic stand-in adapter"
}
```

## T2_kyc
```json
{
  "documents": 47,
  "packets": 12,
  "auto_clear": 4,
  "auto_hold": 8,
  "team_confirmed_clear": 5,
  "team_confirmed_hold": 7,
  "classification_agreement": 11,
  "false_passes": 0,
  "false_holds": 1,
  "per_field": {
    "gstin": {
      "correct": 5,
      "n": 11,
      "accuracy_pct": 45.45454545454545
    },
    "udyam": {
      "correct": 10,
      "n": 10,
      "accuracy_pct": 100.0
    },
    "legal": {
      "correct": 11,
      "n": 11,
      "accuracy_pct": 100.0
    },
    "address": {
      "correct": 11,
      "n": 12,
      "accuracy_pct": 91.66666666666666
    },
    "bill_date": {
      "correct": 12,
      "n": 12,
      "accuracy_pct": 100.0
    },
    "signatory": {
      "correct": 12,
      "n": 12,
      "accuracy_pct": 100.0
    },
    "valid_till": {
      "correct": 12,
      "n": 12,
      "accuracy_pct": 100.0
    },
    "udyam_date": {
      "correct": 11,
      "n": 11,
      "accuracy_pct": 100.0
    },
    "activity": {
      "correct": 11,
      "n": 11,
      "accuracy_pct": 100.0
    }
  },
  "packets_table": [
    {
      "packet": "K01",
      "expected_team_label": "hold",
      "auto_status": "hold",
      "human_confirmed_core_status": "hold",
      "holds": [
        "gst_checksum",
        "gst_registry_mismatch",
        "udyam_missing_number",
        "applicant_unknown"
      ],
      "advisories": []
    },
    {
      "packet": "K02",
      "expected_team_label": "core_checks_clear",
      "auto_status": "core_checks_clear",
      "human_confirmed_core_status": "core_checks_clear",
      "holds": [],
      "advisories": [
        "udyam_registration_date_difference"
      ]
    },
    {
      "packet": "K03",
      "expected_team_label": "core_checks_clear",
      "auto_status": "core_checks_clear",
      "human_confirmed_core_status": "core_checks_clear",
      "holds": [],
      "advisories": [
        "udyam_registration_date_difference"
      ]
    },
    {
      "packet": "K04",
      "expected_team_label": "hold",
      "auto_status": "hold",
      "human_confirmed_core_status": "hold",
      "holds": [
        "blur",
        "gst_unreadable",
        "ocr_uncertain_legal",
        "ocr_uncertain_address"
      ],
      "advisories": [
        "udyam_registration_date_difference"
      ]
    },
    {
      "packet": "K05",
      "expected_team_label": "hold",
      "auto_status": "hold",
      "human_confirmed_core_status": "hold",
      "holds": [
        "missing_udyam_certificate",
        "udyam_missing_number"
      ],
      "advisories": []
    },
    {
      "packet": "K06",
      "expected_team_label": "hold",
      "auto_status": "hold",
      "human_confirmed_core_status": "hold",
      "holds": [
        "gst_checksum",
        "gst_registry_mismatch"
      ],
      "advisories": [
        "udyam_registration_date_difference",
        "udyam_activity_difference"
      ]
    },
    {
      "packet": "K07",
      "expected_team_label": "hold",
      "auto_status": "hold",
      "human_confirmed_core_status": "hold",
      "holds": [
        "gst_checksum",
        "gst_registry_mismatch",
        "legal_mismatch"
      ],
      "advisories": [
        "udyam_registration_date_difference"
      ]
    },
    {
      "packet": "K08",
      "expected_team_label": "core_checks_clear",
      "auto_status": "hold",
      "human_confirmed_core_status": "core_checks_clear",
      "holds": [
        "gst_checksum",
        "gst_registry_mismatch"
      ],
      "advisories": [
        "udyam_registration_date_difference"
      ]
    },
    {
      "packet": "K09",
      "expected_team_label": "core_checks_clear",
      "auto_status": "core_checks_clear",
      "human_confirmed_core_status": "core_checks_clear",
      "holds": [],
      "advisories": [
        "udyam_registration_date_difference"
      ]
    },
    {
      "packet": "K10",
      "expected_team_label": "hold",
      "auto_status": "hold",
      "human_confirmed_core_status": "hold",
      "holds": [
        "gst_checksum",
        "gst_registry_mismatch",
        "authority_review"
      ],
      "advisories": [
        "udyam_registration_date_difference",
        "udyam_activity_difference"
      ]
    },
    {
      "packet": "K11",
      "expected_team_label": "hold",
      "auto_status": "hold",
      "human_confirmed_core_status": "hold",
      "holds": [
        "gst_checksum",
        "gst_registry_mismatch",
        "address_stale"
      ],
      "advisories": [
        "udyam_registration_date_difference",
        "udyam_activity_difference"
      ]
    },
    {
      "packet": "K12",
      "expected_team_label": "core_checks_clear",
      "auto_status": "core_checks_clear",
      "human_confirmed_core_status": "core_checks_clear",
      "holds": [],
      "advisories": [
        "udyam_registration_date_difference",
        "udyam_activity_difference"
      ]
    }
  ],
  "core_policy": "CORE-v4; date/activity differences advisory by explicit policy; exact identifier mismatch remains blocking"
}
```

## T3_quote_time
```json
{
  "n": 100,
  "median_ms": 2.8428,
  "p90_ms": 4.2628,
  "min_ms": 2.2635,
  "max_ms": 4.8455,
  "scope": "TestClient HTTP request to priced, persisted quote; already completed structured facts; includes rules/boundary/DB; excludes typing, user reading, OCR, real LLM/network/install"
}
```

## T4_version
```json
{
  "v1": 1,
  "v1_monthly": 999.0,
  "v2": 2,
  "v2_monthly": 1348.0,
  "hash_changed": true,
  "fresh_acceptance": true
}
```

## T5_advisor
```json
{
  "scenarios": 15,
  "passed": 15,
  "rows": [
    {
      "id": 1,
      "segment": "micro",
      "language": "en",
      "expected": "no_gst_starter",
      "observed": "no_gst_starter",
      "pass": true
    },
    {
      "id": 2,
      "segment": "micro",
      "language": "hi",
      "expected": "no_gst_starter",
      "observed": "no_gst_starter",
      "pass": true
    },
    {
      "id": 3,
      "segment": "professional",
      "language": "en",
      "expected": "routine_gst",
      "observed": "routine_gst",
      "pass": true
    },
    {
      "id": 4,
      "segment": "professional",
      "language": "hi",
      "expected": "routine_gst",
      "observed": "routine_gst",
      "pass": true
    },
    {
      "id": 5,
      "segment": "multisite",
      "language": "en",
      "expected": "specialist",
      "observed": "specialist",
      "pass": true
    },
    {
      "id": 6,
      "segment": "multisite",
      "language": "hi",
      "expected": "specialist",
      "observed": "specialist",
      "pass": true
    },
    {
      "id": 7,
      "segment": "manufacturer",
      "language": "en",
      "expected": "specialist",
      "observed": "specialist",
      "pass": true
    },
    {
      "id": 8,
      "segment": "manufacturer",
      "language": "hi",
      "expected": "specialist",
      "observed": "specialist",
      "pass": true
    },
    {
      "id": 9,
      "segment": "micro",
      "language": "en",
      "expected": "clarify",
      "observed": "clarify",
      "pass": true
    },
    {
      "id": 10,
      "segment": "micro",
      "language": "hi",
      "expected": "clarify",
      "observed": "clarify",
      "pass": true
    },
    {
      "id": 11,
      "segment": "professional",
      "language": "en",
      "expected": "routine_gst",
      "observed": "routine_gst",
      "pass": true
    },
    {
      "id": 12,
      "segment": "micro",
      "language": "en",
      "expected": "no_gst_starter",
      "observed": "no_gst_starter",
      "pass": true
    },
    {
      "id": 13,
      "segment": "micro",
      "language": "hi",
      "expected": "no_gst_starter",
      "observed": "no_gst_starter",
      "pass": true
    },
    {
      "id": 14,
      "segment": "multisite",
      "language": "en",
      "expected": "specialist",
      "observed": "specialist",
      "pass": true
    },
    {
      "id": 15,
      "segment": "manufacturer",
      "language": "en",
      "expected": "specialist",
      "observed": "specialist",
      "pass": true
    }
  ],
  "scope": "Team-written scenario set, not the hidden judges pack"
}
```

## T6_personas
```json
[
  {
    "persona": "Professional clinic, GST",
    "session": "evidence-clinic",
    "monthly": 3505.5,
    "kyc": "core_checks_clear",
    "accept_http": 200,
    "outcome": "order_locked",
    "all_services_mocked": true,
    "durable_lock_recorded": true
  },
  {
    "persona": "Micro kirana, no GST",
    "session": "evidence-kirana",
    "monthly": 1348.0,
    "route": "no_gst_starter",
    "outcome": "preview, evidence pending",
    "all_services_mocked": true,
    "durable_lock_recorded": false
  },
  {
    "persona": "Multi-site assisted",
    "session": "evidence-multisite",
    "monthly": 15594.0,
    "route": "specialist",
    "outcome": "specialist hold",
    "all_services_mocked": true,
    "durable_lock_recorded": false
  },
  {
    "persona": "K06 identifier failure",
    "session": "evidence-k06",
    "kyc": "hold",
    "hold_codes": [
      "gst_checksum",
      "gst_registry_mismatch",
      "identity_binding"
    ],
    "outcome": "hold",
    "all_services_mocked": true,
    "durable_lock_recorded": false
  }
]
```

## T7_rules
```json
{
  "historical_records": 368,
  "conflicts": 56,
  "gst_failures": 21,
  "source": "pytest historical replay through the prototype engine + analysis/numbers.json"
}
```

## OCR reproduction
`python -m quotelock.kyc.prepare` then `python -m quotelock.kyc.ocr_tesseract`
Original images are unchanged. Tesseract5.5.3 English fast data; OpenCV deskew; whole-page label parser. Team visual fixtures are excluded from runtime extraction. No classifier result is corrected to match the supplied expectation.

## Limitations
No independent humans or real customers were tested. Zero leaks refers only to generated payload tests, not a universal privacy guarantee. Role filtering lacks production authentication; ephemeral-key encryption lacks production key management. Serviceability, payment mandate, DigiLocker and e-sign remain explicitly mocked.