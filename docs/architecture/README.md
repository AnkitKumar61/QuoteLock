# QuoteLock architecture

The README diagram is a logical module architecture for the implemented local prototype. It is not a cloud deployment diagram or a claim that the modules are separately deployed services.

- [Editable draw.io file](quotelock-system.drawio)
- [Rendered SVG](quotelock-system.svg)
- [Supplied presentation](../presentation/QuoteLock_Logging_Final_v2.pdf), pages5–6
- [Code authority contract](../../quotelock/architecture.json)

## Sources and mapping

| Reference | What the diagram preserves |
|---|---|
|PDF page5|Six modules A1–A6, all nine core paths, the A2-only boundary, deterministic price/rule authority, mocked integrations.|
|PDF page6|Owned holds, specialist-first resolution, revalidation, digital lock separate from physical readiness/activation.|
|`app.py`|The browser and partner views share one FastAPI application. Budget/facts follow the structured path; evidence goes to deterministic checks.|
|`quote/`, `privacy.py`|Shared SQLite stores versions/consent/holds/locks and encrypted evidence. Keys are ephemeral; transient fields remain in process memory.|
|`kyc/`, `orders/`, `tracker/`|Recorded source packets versus fresh OCR, mock lookups, identity binding, all required lock gates, readiness-based physical state.|

The SQLite access bus represents shared local storage used by trusted modules; it is not an event broker, network bus or additional service. The red boundary includes only A2. It must not grow to include prices, documents, raw identifiers, catalogue rows or order-write access.

The nine core connections are checked against `quotelock/architecture.json`. Supporting interface/storage lines add system context. The diagram is authored as native editable draw.io shapes and orthogonal connectors, not an AI-generated architecture image.

## Editing

Open `quotelock-system.drawio` in draw.io Desktop. Text, containers, database shape and connections remain editable. After a change, export SVG locally and replace `quotelock-system.svg`; check both the source contract and rendered labels before committing. Preserve the distinction between currently implemented modules and future/live integrations.

The reference PPTX was not available; the supplied PDF was exported from PowerPoint and contains the relevant architecture. The original case/template files were not changed or redistributed.
