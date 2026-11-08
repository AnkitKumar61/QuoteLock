# Repository release notes

This repository is a source-only release copy of the QuoteLock synthetic evidence prototype. Original hackathon workspace files were left untouched.

Packaging changes:

- Excluded installed packages, virtual environments, downloaded binaries, live databases and the original case PDF/PowerPoint template.
- Added a root quickstart, custom SVG banner, real screenshots, setup/contribution/privacy/attribution notes and a read-only-permission Python CI workflow.
- Replaced the workstation-specific Tesseract path with `TESSERACT_CMD` or PATH discovery. Missing fresh-OCR support returns a clear503; source-packet demos use disclosed recorded extraction receipts.
- Kept OCR derivative preparation separate from existing team-labelled ground truth; removed its dependency on private workspace audit scripts.
- Moved the retained business-model/pilot inputs to `analysis/baseline/`. Numeric recalculation no longer requires an external slide template.
- Preserved supplied CSV bytes through Git without line-ending normalization. Synthetic fixture attribution stays in its source README.

The historical evidence ledger retains its original measurements, date scope and limitations. It is not a fresh benchmark just because it is included in a new repository. No real customer/integration, live LLM, field conversion uplift, legal certification or production-readiness claim is added by this release.

## Presentation and architecture update

The user-supplied final seven-slide PDF is attached unchanged under `docs/presentation/`. Its SHA-256 is checked by release hygiene. The README screenshot gallery is replaced with document links and a visible system diagram. The editable `.drawio` file and SVG were rendered locally with verified draw.io Desktop32.6.10; only local files were used for export. The diagram preserves the six modules/nine core authority paths and adds explicit single-process/storage context from code. The AI-generated concept cover was subsequently restored at the user's request, alongside the PDF and architecture, with its provenance retained.
