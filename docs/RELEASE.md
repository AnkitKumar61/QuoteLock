# Repository release notes

This repository is a source-only release copy of the QuoteLock synthetic evidence prototype. Original hackathon workspace files were left untouched.

Packaging changes:

- Excluded installed packages, virtual environments, downloaded binaries, live databases and the supplied PDF/PowerPoint template.
- Added a root quickstart, custom SVG banner, real screenshots, setup/contribution/privacy/attribution notes and a read-only-permission Python CI workflow.
- Replaced the workstation-specific Tesseract path with `TESSERACT_CMD` or PATH discovery. Missing fresh-OCR support returns a clear503; source-packet demos use disclosed recorded extraction receipts.
- Kept OCR derivative preparation separate from existing team-labelled ground truth; removed its dependency on private workspace audit scripts.
- Moved the retained business-model/pilot inputs to `analysis/baseline/`. Numeric recalculation no longer requires an external slide template.
- Preserved supplied CSV bytes through Git without line-ending normalization. Synthetic fixture attribution stays in its source README.

The historical evidence ledger retains its original measurements, date scope and limitations. It is not a fresh benchmark just because it is included in a new repository. No real customer/integration, live LLM, field conversion uplift, legal certification or production-readiness claim is added by this release.
