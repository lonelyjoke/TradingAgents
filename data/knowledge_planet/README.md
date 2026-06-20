# Knowledge Planet Local Research Inbox

Daily workflow:

1. Put downloaded research-report PDFs into:
   `data/knowledge_planet/reports/inbox/`
2. Put copied short posts, jokes, strategy notes, and industry snippets into one daily `.md` file under:
   `data/knowledge_planet/inbox/`
3. Run:
   `python scripts/import_knowledge_planet.py`

On Windows, the easiest command is:

`.\scripts\import_knowledge_planet.cmd`

This wrapper prefers the bundled Python runtime that includes PDF extraction dependencies. If you prefer PowerShell scripts and your execution policy allows them, `.\scripts\import_knowledge_planet.ps1` works too.

## Optional zsxq-cli Sync

If your Knowledge Planet account is logged in through `zsxq-cli`, supported
groups can be synced directly into the local stream inbox. The current primary
source is:

`.\scripts\sync_knowledge_planet_from_zsxq.cmd --date 2026-06-19 --group-id 28888112822211:前沿信息收录`

Then run the normal importer:

`.\scripts\import_knowledge_planet.cmd`

In normal TradingAgents usage this upstream step is now also guarded
automatically. Before single-stock Knowledge Planet context is read, and before
the standalone theme-trading daily report is generated, the system attempts:

`zsxq sync -> import_knowledge_planet`

The result is stamped under `data/knowledge_planet/.sync_state/`. By default a
second run within 30 minutes reuses the already-synced local index instead of
downloading the same images/PDFs again; after that interval the next project run
attempts a fresh upstream sync. Empty sync results are retried instead of being
treated as final, because older dates may require deeper pagination.

Optional environment overrides:

- `KNOWLEDGE_PLANET_AUTO_SYNC=0` disables automatic upstream sync.
- `KNOWLEDGE_PLANET_AUTO_SYNC_GROUP=28888112822211:前沿信息收录`
- `KNOWLEDGE_PLANET_AUTO_SYNC_MAX_PAGES=120`
- `KNOWLEDGE_PLANET_AUTO_SYNC_MAX_IMAGE_DOWNLOADS=100`
- `KNOWLEDGE_PLANET_AUTO_SYNC_MAX_FILE_DOWNLOADS=50`
- `KNOWLEDGE_PLANET_AUTO_SYNC_MIN_INTERVAL_MINUTES=30`
- `KNOWLEDGE_PLANET_AUTO_SYNC_CONTEXT_LOOKBACK_DAYS=30`

Not every joined group allows API access. If `zsxq-cli` reports a message such
as `该星球内容仅限成员在星球内查看，暂不支持通过 API 访问`, keep using the
manual inbox workflow for that group. The sync script writes only a daily
markdown stream under `data/knowledge_planet/inbox/`.

The sync script also attempts to enrich non-text material:

- topic images are downloaded to `data/knowledge_planet/attachments/images/YYYY-MM-DD/`;
- Windows OCR is run on downloaded images and the OCR text is embedded back into
  the daily markdown stream, so screenshot essays become searchable;
- file attachments are resolved through zsxq file download URLs;
- PDF attachments are downloaded to `data/knowledge_planet/reports/inbox/`, so
  the normal PDF importer can extract and index them.

Useful safety limits:

`.\scripts\sync_knowledge_planet_from_zsxq.cmd --date 2026-06-19 --group-id 28888112822211:前沿信息收录 --max-pages 120 --max-image-downloads 100 --max-file-downloads 50`

If you only want text sync:

`.\scripts\sync_knowledge_planet_from_zsxq.cmd --date 2026-06-19 --group-id 28888112822211:前沿信息收录 --no-download-images --no-download-files`

The importer will:

- split daily post streams into individual items;
- infer basic source type, credibility, tickers, industries, and themes;
- create or update `data/knowledge_planet/index.sqlite`;
- archive processed stream files by date;
- archive PDF reports by date;
- extract PDF text when `pypdf` is available;
- write PDF metadata into `data/knowledge_planet/reports/extracted/`.

## Daily Stream Format

Use the simplest possible format. You only need author, time, and raw content.

```markdown
# 2026-06-19 Knowledge Planet raw stream

---

纪要小能手
2026-06-19 10:33

Paste the full post here.

---

August
2026-06-19 10:20

Paste the next full post here.

---
```

Manual tagging is optional. If you want to add tags later, use the richer template in:

`data/knowledge_planet/inbox/post_template.md`

## PDF Reports

You do not need to create date folders manually. Put PDFs directly in:

`data/knowledge_planet/reports/inbox/`

The importer archives them under:

`data/knowledge_planet/reports/processed/YYYY/MM/DD/`

If you want the importer to rename PDFs with suggested normalized names, run:

`python scripts/import_knowledge_planet.py --reports --apply-suggested-pdf-names`

Otherwise it preserves original filenames and stores suggested names in metadata.

## First Validation

Before a real import, preview with:

`python scripts/import_knowledge_planet.py --dry-run`

After import, the SQLite database is:

`data/knowledge_planet/index.sqlite`

## Theme-Trading Daily Report

For the easiest interactive workflow, run the menu launcher:

`.\scripts\generate_knowledge_planet_daily_interactive.cmd`

Or double-click the repository-root launcher:

`KnowledgePlanetDaily.cmd`

The launcher lets you choose the report end date, look-back window, run mode,
LLM provider, model, Tushare scoring depth, and LLM candidate count. The default
mode is the full workflow: Knowledge Planet stream/PDFs, Tushare
fundamental/technical validation, and DeepSeek-style LLM thesis decomposition.

After the daily import finishes, generate the standalone Knowledge Planet
daily report with:

`.\scripts\generate_knowledge_planet_daily.cmd --date 2026-06-19`

The default output is:

`reports/knowledge_planet_daily/YYYY-MM-DD/daily_report.md`

Use `--lookback-days 0` for the exact day, or a larger value such as `3` when
you want a rolling window. The report ranks mentioned candidates by information
content, catalyst clues, and pump-risk signals. It is a theme-trading shortlist,
not a direct buy list.

For a rolling daily report, `--lookback-days` now syncs and imports every
calendar day in the window before the report is built. The command-line default
is `--lookback-days 6`, which means a seven-day window including the report
date. For example, `--date 2026-06-19 --lookback-days 2` covers 2026-06-17
through 2026-06-19.

The daily report applies a recency weighting to stream signals: report-date
items receive the highest weight, the prior two days receive a medium weight,
and days four through seven act as background continuity. The report also
prints a marginal-change table so you can see whether a theme is newly heating
up, continuing over several days, or fading.

By default the report also attempts an A-share trader-style validation for the
top ranked candidates. Fundamentals are used as cross-validation for the
narrative, not as a standalone additive score: strong fundamentals confirm and
amplify the theme, weak fundamentals cap or penalize the ranking, and missing
data prevents an A-bucket call. This validation looks at growth, profitability,
cash/leverage, valuation tolerance, and market-cap elasticity. The technical
score remains an independent timing/risk check covering trend, 5/20/60-day
momentum, turnover/volume confirmation, distance from recent highs, and overheat
risk. If Tushare or ticker resolution is unavailable, the candidate is marked as
unscored rather than filled with fake data. To skip this slower validation step,
run:

`.\scripts\generate_knowledge_planet_daily.cmd --date 2026-06-19 --no-market-scoring`

For the high-quality theme-trading version, add DeepSeek LLM analysis. This
uses deterministic scores only as inputs, then asks the model to decompose the
thesis path, company relevance, verification points, falsification points,
trading action, and pump risk:

`.\scripts\generate_knowledge_planet_daily.cmd --date 2026-06-19 --lookback-days 0 --llm-market-analysis --max-llm-candidates 8`

The LLM layer is explicit because it consumes API tokens. Mention count remains
only a recall signal; it should not be treated as the reason a candidate ranks
highly.

The daily report now follows a trading-desk chain:

- parse raw posts into event signals such as order/production, price hikes,
  inventory/supply-demand, customer validation, policy, overseas mapping, or
  sell-side promotion;
- rank theme mainlines and show a pre-market playbook before listing stocks;
- translate each candidate into expectation gap, company pass-through,
  fundamental validation, technical trading window, win-rate/payoff, entry plan,
  sizing, verification points, and falsification points.

Single-stock TradingAgents uses this knowledge base differently. It treats
Knowledge Planet as supplemental alternative intelligence: it can enrich
sell-side frameworks, channel clues, KPI questions, and expectation-gap
hypotheses, but official filings, announcements, financial statements, reputable
news, and price/volume evidence remain the objective anchor. If the private
stream conflicts with objective evidence, the objective evidence caps conviction.
The single-stock default remains a 30-day Knowledge Planet window.

## TradingAgents Integration

Single-stock A-share analysis now preloads local Knowledge Planet context when
`data/knowledge_planet/index.sqlite` exists. The agent receives:

- recent matched stream items from the configured look-back window;
- matched PDF research reports and extracted PDF text hits;
- source labels such as industry weekly data, channel check, research feedback,
  sell-side push, and rumor/sentiment;
- instructions to treat private/channel evidence as labeled clues and sell-side
  promotion as optimism-biased until validated.

Useful optional environment overrides:

- `KNOWLEDGE_PLANET_DB_PATH`
- `KNOWLEDGE_PLANET_LOOKBACK_DAYS`
- `KNOWLEDGE_PLANET_MAX_ITEMS`
- `KNOWLEDGE_PLANET_MAX_REPORTS`
