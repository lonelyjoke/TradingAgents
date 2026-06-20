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
        default=6,
        help="Number of prior calendar days to include. Defaults to 6, meaning a 7-day window including --date.",
    )
    parser.add_argument(
        "--max-candidates",
        type=int,
        default=30,
        help="Maximum candidate rows to include in the ranking table.",
    )
    parser.add_argument(
        "--max-scored-candidates",
        type=int,
        default=12,
        help="Maximum top candidates to enrich with real A-share fundamental/technical scores.",
    )
    parser.add_argument(
        "--no-market-scoring",
        action="store_true",
        help="Skip A-share fundamental/technical enrichment and only rank Knowledge Planet signals.",
    )
    parser.add_argument(
        "--llm-market-analysis",
        action="store_true",
        help="Use an LLM, default DeepSeek, to analyze candidate theme logic and trading action.",
    )
    parser.add_argument(
        "--max-llm-candidates",
        type=int,
        default=8,
        help="Maximum top candidates to send to the LLM market-analysis layer.",
    )
    parser.add_argument(
        "--llm-provider",
        default="deepseek",
        help="LLM provider for --llm-market-analysis.",
    )
    parser.add_argument(
        "--llm-model",
        default="deepseek-chat",
        help="LLM model for --llm-market-analysis.",
    )
    parser.add_argument(
        "--llm-base-url",
        default=None,
        help="Optional base URL override for the LLM provider.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress per-candidate market-scoring progress output.",
    )
    parser.add_argument(
        "--no-preprocess",
        action="store_true",
        help="Skip the cached Knowledge Planet preprocessing layer for a faster debug run.",
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
    if args.no_preprocess:
        set_config({"knowledge_planet_preprocess_enabled": False})

    include_market_scores = not args.no_market_scoring
    print(f"python: {sys.executable}")
    print(
        "market scoring: "
        + (
            f"enabled, max scored candidates={args.max_scored_candidates}"
            if include_market_scores
            else "disabled by --no-market-scoring"
        )
    )
    print(
        "llm market analysis: "
        + (
            f"enabled, provider={args.llm_provider}, model={args.llm_model}, max candidates={args.max_llm_candidates}"
            if args.llm_market_analysis
            else "disabled"
        )
    )
    print("preprocess: " + ("disabled by --no-preprocess" if args.no_preprocess else "enabled"))

    report = build_knowledge_planet_daily_report(
        args.date,
        look_back_days=args.lookback_days,
        max_candidates=args.max_candidates,
        include_market_scores=include_market_scores,
        max_scored_candidates=args.max_scored_candidates,
        include_llm_market_analysis=args.llm_market_analysis,
        max_llm_candidates=args.max_llm_candidates,
        llm_provider=args.llm_provider,
        llm_model=args.llm_model,
        llm_base_url=args.llm_base_url,
        progress=None if args.quiet else print,
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
