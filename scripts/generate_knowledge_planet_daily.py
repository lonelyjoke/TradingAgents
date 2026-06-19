"""Generate a local Knowledge Planet theme-trading daily report."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tradingagents.dataflows.config import set_config
from tradingagents.dataflows.knowledge_planet_research import (
    build_knowledge_planet_daily_report,
)


DEFAULT_OUTPUT_ROOT = REPO_ROOT / "reports" / "knowledge_planet_daily"


def default_report_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a Knowledge Planet theme-trading daily report."
    )
    parser.add_argument(
        "--date",
        default=default_report_date(),
        help="Report date in YYYY-MM-DD format. Defaults to today.",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=0,
        help="Number of prior calendar days to include. 0 means only --date.",
    )
    parser.add_argument(
        "--max-candidates",
        type=int,
        default=30,
        help="Maximum candidate rows to include in the ranking table.",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=None,
        help="Optional path to data/knowledge_planet/index.sqlite.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional markdown output path.",
    )
    args = parser.parse_args()

    if args.db:
        set_config({"knowledge_planet_db_path": str(args.db.resolve())})

    report = build_knowledge_planet_daily_report(
        args.date,
        look_back_days=args.lookback_days,
        max_candidates=args.max_candidates,
    )
    output = args.output
    if output is None:
        output = DEFAULT_OUTPUT_ROOT / args.date / "daily_report.md"
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("Knowledge Planet daily report generated")
    print(f"date: {args.date}")
    print(f"lookback days: {args.lookback_days}")
    print(f"output: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
