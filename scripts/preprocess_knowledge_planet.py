"""Build cached Knowledge Planet research assets from the local SQLite index."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tradingagents.dataflows.config import set_config
from tradingagents.dataflows.knowledge_planet_research import (
    preprocess_knowledge_planet_window,
)


def default_report_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Preprocess local Knowledge Planet data into research-asset tables."
    )
    parser.add_argument(
        "--date",
        default=default_report_date(),
        help="End date in YYYY-MM-DD format. Defaults to today.",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=6,
        help="Number of prior calendar days to include. Defaults to 6.",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=None,
        help="Optional path to data/knowledge_planet/index.sqlite.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress output.",
    )
    args = parser.parse_args()

    if args.db:
        set_config({"knowledge_planet_db_path": str(args.db.resolve())})

    stats = preprocess_knowledge_planet_window(
        args.date,
        args.lookback_days,
        progress=None if args.quiet else print,
    )
    print("Knowledge Planet preprocessing complete")
    print(f"window: {stats.start_date} to {stats.end_date}")
    print(f"items scanned: {stats.items_scanned}")
    print(f"reports scanned: {stats.reports_scanned}")
    print(f"events: {stats.events}")
    print(f"clusters: {stats.clusters}")
    print(f"mappings: {stats.mappings}")
    print(f"report assumptions: {stats.report_assumptions}")
    print(f"opportunities: {stats.opportunities}")
    print(f"ocr low quality: {stats.ocr_low_quality}")
    print(f"pdf pending/limited: {stats.pdf_pending_or_limited}")
    print(f"status: {stats.status}")
    return 0 if stats.status in {"ok", "no_db"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
