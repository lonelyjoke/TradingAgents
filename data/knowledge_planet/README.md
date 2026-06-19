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

After the daily import finishes, generate the standalone Knowledge Planet
daily report with:

`.\scripts\generate_knowledge_planet_daily.cmd --date 2026-06-19`

The default output is:

`reports/knowledge_planet_daily/YYYY-MM-DD/daily_report.md`

Use `--lookback-days 0` for the exact day, or a larger value such as `3` when
you want a rolling window. The report ranks mentioned candidates by information
content, catalyst clues, and pump-risk signals. It is a theme-trading shortlist,
not a direct buy list.

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
