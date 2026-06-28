"""One-command rolling Knowledge Planet update for single-stock research.

This script syncs the recent Knowledge Planet window, imports stream/PDF files
into the local SQLite index, backfills missing PDF text, and rebuilds cached
research assets. Existing date sync stamps and content hashes prevent repeated
downloads/import overwrites unless --force is passed.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tradingagents.dataflows.config import set_config
from tradingagents.dataflows.knowledge_planet_research import (
    ensure_knowledge_planet_upstream_synced_for_window,
    preprocess_knowledge_planet_window,
)


def default_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync/import/preprocess the rolling 30-day Knowledge Planet window."
    )
    parser.add_argument("--date", default=default_date(), help="End date, YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--lookback-days", type=int, default=30, help="Rolling window size. Defaults to 30.")
    parser.add_argument("--group-id", default=None, help="Optional zsxq group id or id:name override.")
    parser.add_argument("--db", type=Path, default=None, help="Optional data/knowledge_planet/index.sqlite path.")
    parser.add_argument("--force", action="store_true", help="Ignore existing sync stamps and resync dates.")
    parser.add_argument("--max-pages", type=int, default=None, help="Override max zsxq pages per date.")
    parser.add_argument("--max-image-downloads", type=int, default=None, help="Override image download cap per date.")
    parser.add_argument("--max-file-downloads", type=int, default=None, help="Override file/PDF download cap per date.")
    parser.add_argument("--no-llm-report-analysis", action="store_true", help="Disable LLM enrichment for imported PDF reports.")
    parser.add_argument("--llm-provider", default=None, help="Optional LLM provider for PDF report enrichment.")
    parser.add_argument("--llm-model", default=None, help="Optional LLM model for PDF report enrichment.")
    parser.add_argument("--llm-base-url", default=None, help="Optional LLM base URL for PDF report enrichment.")
    parser.add_argument("--max-llm-reports", type=int, default=None, help="Maximum PDF reports to enrich with LLM.")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress logs from the sync/preprocess layer.")
    args = parser.parse_args()

    overrides: dict[str, object] = {
        "knowledge_planet_lookback_days": int(args.lookback_days),
    }
    if args.group_id:
        overrides["knowledge_planet_auto_sync_group"] = args.group_id
    if args.db:
        overrides["knowledge_planet_db_path"] = str(args.db.resolve())
    set_config(overrides)

    progress = None if args.quiet else print
    sync_status = ensure_knowledge_planet_upstream_synced_for_window(
        args.date,
        int(args.lookback_days),
        force=bool(args.force),
        progress=progress,
        max_pages=args.max_pages,
        max_image_downloads=args.max_image_downloads,
        max_file_downloads=args.max_file_downloads,
    )
    if not args.quiet:
        print(f"rolling sync: {sync_status}")

    stats = preprocess_knowledge_planet_window(
        args.date,
        int(args.lookback_days),
        progress=progress,
        include_llm_report_analysis=not bool(args.no_llm_report_analysis),
        llm_provider=args.llm_provider,
        llm_model=args.llm_model,
        llm_base_url=args.llm_base_url,
        max_llm_reports=args.max_llm_reports,
    )
    print("Knowledge Planet 30-day update complete")
    print(f"window: {stats.start_date} to {stats.end_date}")
    print(f"status: {stats.status}")
    print(f"items scanned: {stats.items_scanned}")
    print(f"reports scanned: {stats.reports_scanned}")
    print(f"events: {stats.events}")
    print(f"report assumptions: {stats.report_assumptions}")
    print(f"opportunities: {stats.opportunities}")
    sync_failed = "auto_sync_failed:" in sync_status or "local_import_failed:" in sync_status
    return 0 if stats.status in {"ok", "cached", "no_db"} and not sync_failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
