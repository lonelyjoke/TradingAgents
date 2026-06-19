"""Interactive launcher for Knowledge Planet theme-trading daily reports."""

from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_SCRIPT = REPO_ROOT / "scripts" / "generate_knowledge_planet_daily.py"


def _ask(prompt: str, default: str) -> str:
    raw = input(f"{prompt} [{default}]: ").strip()
    return raw or default


def _ask_yes_no(prompt: str, default: bool) -> bool:
    default_text = "Y" if default else "N"
    raw = input(f"{prompt} [{default_text}]: ").strip().lower()
    if not raw:
        return default
    return raw in {"y", "yes", "1", "true", "是", "对"}


def main() -> int:
    print("Knowledge Planet theme-trading daily report")
    print("=" * 48)
    date = _ask("Report date YYYY-MM-DD", datetime.now().strftime("%Y-%m-%d"))
    lookback_days = _ask("Lookback days", "0")
    max_scored = _ask("Tushare scored candidates", "12")
    use_llm = _ask_yes_no("Enable DeepSeek LLM analysis", True)

    args = [
        sys.executable,
        str(REPORT_SCRIPT),
        "--date",
        date,
        "--lookback-days",
        lookback_days,
        "--max-scored-candidates",
        max_scored,
    ]

    if use_llm:
        max_llm = _ask("DeepSeek LLM candidates", "8")
        model = _ask("DeepSeek model", "deepseek-chat")
        args.extend(
            [
                "--llm-market-analysis",
                "--llm-provider",
                "deepseek",
                "--llm-model",
                model,
                "--max-llm-candidates",
                max_llm,
            ]
        )

    print()
    print("Running:")
    print(" ".join(args))
    print()
    return subprocess.call(args, cwd=REPO_ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
