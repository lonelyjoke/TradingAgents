# Knowledge Planet Research Reports

This folder stores downloaded sell-side and buy-side research report PDFs from Knowledge Planet.

Keep short posts and screenshots in:

`data/knowledge_planet/inbox/`

Keep PDF reports here:

`data/knowledge_planet/reports/inbox/`

## Folder Roles

- `inbox/`: newly downloaded PDF reports waiting for import.
- `extracted/`: generated text, metadata, and summaries derived from PDFs.
- `processed/`: original PDFs after successful import.
- `failed/`: PDFs that failed text extraction or metadata parsing.

## Filename Convention

Use stable, searchable names when possible:

`YYYYMMDD_broker_ticker_or_industry_short-title.pdf`

Examples:

- `20260618_GS_OKLO_fuel-supply-and-uranium-procurement.pdf`
- `20260618_GS_ACN_quarterly-results-guidance.pdf`
- `20260618_GS_lithium-carbonate-weekly-update.pdf`
- `20260618_GS_global-capital-flows-tic.pdf`
- `20260618_GS_US-auto-industrial-five-minute-market-points.pdf`

If the original filename is already descriptive, keep it. Do not spend time over-normalizing names manually; the importer can infer metadata later.

## Metadata Sidecar

For important reports, optionally create a `.yml` sidecar with the same base filename.

Example:

`20260618_GS_OKLO_fuel-supply-and-uranium-procurement.yml`

```yaml
source_platform: knowledge_planet
source_type: sell_side_report_pdf
broker: Goldman Sachs
broker_short: GS
published_at: 2026-06-18
imported_at:
language: zh-CN
tickers:
  - OKLO
company_names:
  - Oklo Inc.
industries:
  - nuclear
  - uranium
themes:
  - fuel supply
  - uranium procurement
  - project expansion
coverage_region: US
credibility: broker_research
source_url:
source_post_author: August
source_post_time: 2026-06-19 10:20
copyright_note: internal_research_only
investment_use:
  - Use as sell-side viewpoint and estimate input.
  - Cross-check key numbers against filings, company releases, market data, or primary sources before treating them as facts.
```

## Evidence Discipline

PDF reports can enrich the research system, but they should be treated as broker opinions and secondary evidence. The system should index extracted text and concise summaries for private research use, then cite metadata and small snippets rather than redistributing full report text.
