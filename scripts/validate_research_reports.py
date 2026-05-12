"""Validate saved TradingAgents research reports with real Tushare prices."""

from __future__ import annotations

import argparse
from pathlib import Path

from tradingagents.evaluation.research_validator import (
    evaluate_report,
    evaluate_report_tree,
    summarize_validation,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reports",
        default="reports",
        help="Reports root directory or one report directory.",
    )
    parser.add_argument(
        "--horizons",
        nargs="+",
        type=int,
        default=[20, 60, 120],
        help="Trading-day horizons to evaluate.",
    )
    parser.add_argument(
        "--benchmark",
        default="000300.SH",
        help="Tushare index benchmark, default CSI 300.",
    )
    parser.add_argument(
        "--hold-band",
        type=float,
        default=0.02,
        help="Absolute excess-return band treated as correct for Hold.",
    )
    parser.add_argument(
        "--output",
        default="reports_validation.csv",
        help="CSV file for detailed validation rows.",
    )
    parser.add_argument(
        "--summary-output",
        default="reports_validation_summary.csv",
        help="CSV file for grouped summary rows.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target = Path(args.reports)

    if (target / "5_portfolio" / "decision.md").exists():
        results = evaluate_report(
            target,
            horizons=args.horizons,
            benchmark=args.benchmark,
            hold_band=args.hold_band,
        )
    else:
        results = evaluate_report_tree(
            target,
            horizons=args.horizons,
            benchmark=args.benchmark,
            hold_band=args.hold_band,
        )

    output_path = Path(args.output)
    results.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Wrote detailed validation rows: {output_path}")

    summary = summarize_validation(results)
    summary_output_path = Path(args.summary_output)
    summary.to_csv(summary_output_path, index=False, encoding="utf-8-sig")
    print(f"Wrote grouped summary rows: {summary_output_path}")

    if results.empty:
        print("No report rows found.")
    else:
        print(results[["ticker", "rating", "horizon_days", "status"]].to_string(index=False))


if __name__ == "__main__":
    main()

