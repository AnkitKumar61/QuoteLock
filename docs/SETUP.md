# Setup and reproduction

The root README is the shortest path to the local demo. Python3.11+ is supported by the CI matrix; the recorded workstation used3.13. Install `requirements-dev.txt` in a virtual environment. The runtime-only packages are in `requirements.txt`; `requirements-lock.txt` captures the complete tested release environment if exact transitive versions are needed.

## Two evidence paths

**Recorded source packets.** `evaluation/ocr_fields.json` contains the recorded Tesseract extraction for the supplied synthetic packets. Choosing a packet in the UI reruns deterministic validation over those fields; it does not pretend to rerun OCR. This keeps the base demo/test path independent of a system OCR installation. Team labels are separate under `quotelock/kyc/fixtures/` and never feed runtime extraction.

**Fresh upload or full OCR regeneration.** Install Tesseract with English data using its [official installation guidance](https://tesseract-ocr.github.io/tessdoc/Installation.html). `tesseract` on PATH is detected automatically. If needed, set an explicit executable:

```powershell
# Windows PowerShell; use your actual installation path
$env:TESSERACT_CMD = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

```bash
# macOS/Linux; use your actual installation path
export TESSERACT_CMD=/usr/bin/tesseract
```

Then:

```bash
python -m quotelock.kyc.prepare
python -m quotelock.kyc.ocr_tesseract
python -m evaluation.measure
```

`prepare` creates derivative scans and blur/deskew metadata only. It preserves the original PNGs and team labels. Different engines/trained data may produce different held/clear outcomes; publish the result observed, not the baseline expectation. No Tesseract executable is bundled.

## Useful commands

```bash
python -m pytest analysis/test_numbers.py quotelock/tests -q -p no:cacheprovider
python -m quotelock.demo
python analysis/numbers.py
python -m evaluation.business
python -m evaluation.measure
python scripts/check_repository.py
```

Re-running measurement updates scripted latency and synthetic evaluation receipts. It does not automatically update frozen pitch text. Original baseline measurements are dated2026-11-08; source date checks deliberately remain2026-07-15 as required by the fixture pack.

## State and limitations

SQLite state and encrypted uploads are written under ignored `quotelock/.data/`. No live database is committed. Quote records remain immutable, so start a new inquiry for a new attempt. The encryption key is generated in process memory: old vault blobs cannot be decrypted after restart. The current implementation lacks production user authentication, durable key management and a complete deletion/rights operation.

The no-GST route creates previews. Final acceptance requires bound identity; alternative no-GST final evidence is pending. Source packetK02 is deliberately used by the clinic walkthrough because it clears current core checks and matches the selected synthetic business. Do not use another business's packet as a shortcut.

Voice, Marathi, WhatsApp and an actual LLM are future work. No external registry, DigiLocker, payment, e-sign or serviceability credential is needed or used.

## Pitch files

`output/Final_Slide_Content_v4.md` is a seven-slide Markdown build source; its support file is reference only. The user-supplied final presentation is attached unchanged as `docs/presentation/QuoteLock_Logging_Final_v2.pdf`. The original case PDF and PowerPoint template remain excluded. Supply your authorised template separately if later building a presentation; no PPTX/PDF was authored or modified to attach this file.
