"""One-command rolling Knowledge Planet update for single-stock research.

This script syncs the recent Knowledge Planet window, imports stream/PDF files
into the local SQLite index, backfills missing PDF text, and rebuilds cached
research assets. Existing date sync stamps and content hashes prevent repeated
downloads/import overwrites unless --force is passed.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tradingagents.dataflows.config import set_config
from tradingagents.dataflows.knowledge_planet_research import (
    ensure_knowledge_planet_upstream_synced_for_window,
    preprocess_knowledge_planet_window,
)


def default_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def run_import_backfill(db: Path | None) -> int:
    script = REPO_ROOT / "scripts" / "import_knowledge_planet.py"
    args = [sys.executable, str(script), "--backfill-report-text"]
    if db:
        args.extend(["--db", str(db.resolve())])
    completed = subprocess.run(args, cwd=str(REPO_ROOT), check=False)
    return int(completed.returncode)


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

    import_code = run_import_backfill(args.db)
    if import_code != 0:
        return import_code

    stats = preprocess_knowledge_planet_window(
        args.date,
        int(args.lookback_days),
        progress=progress,
    )
    print("Knowledge Planet 30-day update complete")
    print(f"window: {stats.start_date} to {stats.end_date}")
    print(f"status: {stats.status}")
    print(f"items scanned: {stats.items_scanned}")
    print(f"reports scanned: {stats.reports_scanned}")
    print(f"events: {stats.events}")
    print(f"report assumptions: {stats.report_assumptions}")
    print(f"opportunities: {stats.opportunities}")
    return 0 if stats.status in {"ok", "cached", "no_db"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
