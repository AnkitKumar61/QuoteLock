# Contributing

Keep changes small and reviewable. Explain the owner-facing behavior and how you tested it in your pull request. Run `python -m pytest analysis/test_numbers.py quotelock/tests -q -p no:cacheprovider` before submitting.

## Invariants

- The adapter receives redacted non-commercial intent only. Budget bypasses it; no prices, catalogue rows, raw identifiers, contacts or write access.
- Deterministic rules own price, eligibility and terms. Unknown facts hold; human review cannot override a failed rule.
- Material quote changes create a new hash/version and require fresh acceptance.
- A clear packet is not enough: final acceptance and lock require the quote's bound business identity.
- Digital order lock and physical service activation remain different events.
- Do not substitute fixtures/registry values for unreadable OCR or tune outcomes to expected answers.

## Evidence and documentation

Use synthetic inputs only. Record the exact command, measurement scope and actual result. Keep assumptions/projections separate from observations. A benchmark rerun can change latency; do not silently reuse an old timing value as a fresh result. A new API edge case should include a meaningful regression test. Do not add tests that merely mirror trivial formatting.

Do not commit `.data`, databases, uploads, keys, tokens, virtual environments, downloaded binaries or external presentation templates. New fixture data must be explicitly synthetic and attributed. No open-source licence has yet been selected; contributions do not change third-party fixture rights.
