# T9 — quote/evidence identity binding

Synthetic adverse-case check; no external registry or real identity call. The complete packet is valid for its own source business, which does not establish that an identity-free quote belongs to it.

Command before repair:

```powershell
python -m pytest quotelock/tests/test_api.py::test_unbound_no_gst_preview_cannot_accept_another_business_packet -q -p no:cacheprovider
```

Observed:1 failed. Final acceptance returned HTTP200 where the new assertion required409. The regression was written before the guard, so it demonstrated a real defect.

Repair: `api/accept` refuses a quote without a bound business-identifier hash; `api/lock` independently treats that state as evidence pending, even for a legacy/manual accepted flag. Current evidence must still match a nonempty quote identity hash, and all existing catalogue/serviceability/payment/consent gates remain. No-GST preview is allowed; final verified acceptance needs a fresh bound quote or a future approved alternative-evidence path.

After repair:

```powershell
python -m pytest analysis/test_numbers.py quotelock/tests -q -p no:cacheprovider --junitxml=evaluation/pytest.xml
python -m quotelock.demo
```

Observed:448 passed,1 third-party anyio/Pytest deprecation warning. New regression checks both HTTP409 acceptance and an owned evidence hold on a legacy/manual acceptance bypass. Four-persona replay: Professional clinic→mock lock with HTTP200 acceptance; Micro no-GST→preview/evidence pending; multi-site→specialist hold; K06→checksum/registry/identity hold. No physical service completed.

This does not add production authentication, proof that a document was submitted by its lawful owner or a real no-GST evidence policy. These remain explicit limits. Priced-preview code was unchanged, so the frozen T3 timing receipt is retained rather than silently rebenchmarked. Existing screenshots use a quote-bound Professional clinic and remain valid for their displayed states.
