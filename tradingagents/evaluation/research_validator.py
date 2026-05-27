"""Validate saved research reports against later real A-share returns.

This module evaluates the *published report view* rather than running a
strategy simulator. It is intentionally strict about real data: if Tushare
cannot provide prices, the report is marked unavailable instead of falling
back to synthetic data.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
import re
from typing import Iterable

import pandas as pd

from tradingagents.dataflows.tushare_client import (
    TushareClientError,
    get_tushare_pro_client,
)


RATING_MAP = {
    "buy": "Buy",
    "overweight": "Overweight",
    "hold": "Hold",
    "underweight": "Underweight",
    "sell": "Sell",
    "强烈买入": "Buy",
    "买入": "Buy",
    "高配": "Overweight",
    "超配": "Overweight",
    "增持": "Overweight",
    "持有": "Hold",
    "中性": "Hold",
    "低配": "Underweight",
    "减持": "Underweight",
    "卖出": "Sell",
    "回避": "Sell",
}

POSITIVE_RATINGS = {"Buy", "Overweight"}
NEGATIVE_RATINGS = {"Underweight", "Sell"}


@dataclass(frozen=True)
class ReportView:
    report_dir: Path
    ticker: str
    report_datetime: datetime
    rating: str
    core_bet: str = ""
    conviction: str = ""


@dataclass(frozen=True)
class DecisionDepthIssue:
    section: str
    severity: str
    issue: str


_SEGMENT_DEPTH_TERMS = (
    "revenue",
    "growth",
    "gross margin",
    "net margin",
    "profit",
    "cash",
    "valuation",
    "not disclosed",
    "收入",
    "增速",
    "增长",
    "毛利",
    "净利",
    "利润",
    "现金",
    "估值",
    "未披露",
)

_PEER_DEPTH_TERMS = (
    "rank",
    "peer",
    "comparable",
    "valuation",
    "ROE",
    "margin",
    "growth",
    "leverage",
    "allocation",
    "排名",
    "同行",
    "可比",
    "估值",
    "盈利",
    "毛利",
    "增长",
    "杠杆",
    "配置",
)

_VALUATION_DEPTH_TERMS = (
    "implied",
    "expectation",
    "EPS",
    "ROE",
    "cash flow",
    "multiple",
    "PE",
    "PB",
    "隐含",
    "预期",
    "每股收益",
    "现金流",
    "倍数",
    "估值",
)

_FALSIFICATION_DEPTH_TERMS = (
    "confirm",
    "weaken",
    "downgrade",
    "falsify",
    "margin",
    "orders",
    "cash",
    "确认",
    "削弱",
    "下调",
    "证伪",
    "毛利",
    "订单",
    "现金",
)


def _section_text(text: str, label: str) -> str:
    pattern = rf"\*\*{re.escape(label)}\*\*:\s*(.*?)(?:\n\n\*\*[^*\n]+\*\*:|\Z)"
    match = re.search(pattern, text, flags=re.S)
    return match.group(1).strip() if match else ""


def _term_hits(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def audit_decision_depth(decision_text: str) -> list[DecisionDepthIssue]:
    """Flag final-decision sections that look present but too shallow.

    This is a lightweight guardrail for saved reports. It intentionally avoids
    scoring investment correctness; it checks whether the public memo contains
    the minimum buy-side analytical loops that make a conclusion inspectable.
    """
    issues: list[DecisionDepthIssue] = []

    segment = _section_text(decision_text, "Investment Thesis")
    if "Business Segment Breakdown:" not in segment:
        issues.append(
            DecisionDepthIssue(
                "business_segment_breakdown",
                "warning",
                "missing explicit Business Segment Breakdown in the final thesis",
            )
        )
    elif _term_hits(segment, _SEGMENT_DEPTH_TERMS) < 5:
        issues.append(
            DecisionDepthIssue(
                "business_segment_breakdown",
                "warning",
                "segment discussion lacks revenue/growth/margin/profit/cash/valuation depth",
            )
        )

    if "Peer Comparison Summary:" not in segment:
        issues.append(
            DecisionDepthIssue(
                "peer_comparison_summary",
                "warning",
                "missing explicit Peer Comparison Summary in the final thesis",
            )
        )
    elif _term_hits(segment, _PEER_DEPTH_TERMS) < 5:
        issues.append(
            DecisionDepthIssue(
                "peer_comparison_summary",
                "warning",
                "peer discussion lacks rank/comparability/valuation/profitability/allocation depth",
            )
        )

    if _term_hits(decision_text, _VALUATION_DEPTH_TERMS) < 4:
        issues.append(
            DecisionDepthIssue(
                "valuation_expectation",
                "warning",
                "valuation discussion does not translate price into implied EPS/ROE/cash-flow/multiple assumptions",
            )
        )

    if _term_hits(decision_text, _FALSIFICATION_DEPTH_TERMS) < 4:
        issues.append(
            DecisionDepthIssue(
                "verification_and_falsification",
                "warning",
                "verification section lacks concrete confirm/weaken/downgrade conditions",
            )
        )

    return issues


def audit_report_depth(report_dir: str | Path) -> pd.DataFrame:
    """Audit the final portfolio decision for shallow buy-side sections."""
    decision_path = Path(report_dir) / "5_portfolio" / "decision.md"
    if not decision_path.exists():
        raise FileNotFoundError(f"Missing portfolio decision: {decision_path}")
    issues = audit_decision_depth(read_text_fallback(decision_path))
    return pd.DataFrame(
        [
            {
                "section": issue.section,
                "severity": issue.severity,
                "issue": issue.issue,
            }
            for issue in issues
        ]
    )


def read_text_fallback(path: Path) -> str:
    """Read markdown using common encodings without raising Unicode errors."""
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def _plain_markdown_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^#{1,6}\s*", "", line)
    line = re.sub(r"^[>\-\u2022]\s*", "", line)
    return line.replace("**", "").replace("__", "").strip()


def _next_nonempty_line(lines: list[str], start_index: int) -> str:
    for line in lines[start_index + 1 :]:
        plain = _plain_markdown_line(line)
        if plain:
            return plain
    return ""


def _extract_section(text: str, names: Iterable[str]) -> str:
    """Extract a one-line markdown field or the paragraph after a field header."""
    lines = text.splitlines()
    sorted_names = sorted(names, key=len, reverse=True)

    def _match_name_value(plain: str, name: str, *, anchored: bool) -> str | None:
        suffix = r"(?:[（(][^）)]*[）)])?"
        prefix = "^" if anchored else r"^.*?"
        match = re.match(
            rf"{prefix}{re.escape(name)}{suffix}\s*[:：是]\s*(.*)$",
            plain,
            flags=re.IGNORECASE,
        )
        if match:
            return match.group(1).strip()
        return None

    for index, line in enumerate(lines):
        plain = _plain_markdown_line(line)
        for name in sorted_names:
            value = _match_name_value(plain, name, anchored=True)
            if value is not None:
                return value if value else _next_nonempty_line(lines, index)

            header_match = re.match(
                rf"^{re.escape(name)}(?:[（(][^）)]*[）)])?$",
                plain,
                flags=re.IGNORECASE,
            )
            if header_match:
                return _next_nonempty_line(lines, index)

            if "核心" in name:
                value = _match_name_value(plain, name, anchored=False)
                if value is not None:
                    return value if value else _next_nonempty_line(lines, index)
    return ""


def _normalize_rating(raw: str) -> str:
    cleaned = _plain_markdown_line(raw).strip("：:")
    if not cleaned:
        return "Unknown"

    for token, normalized in RATING_MAP.items():
        if re.fullmatch(r"[a-z]+", token):
            pattern = rf"\b{re.escape(token)}\b"
            if re.search(pattern, cleaned, flags=re.IGNORECASE):
                return normalized
        elif token in cleaned:
            return normalized

    first_word = cleaned.split()[0].strip("：:")
    first_word = re.sub(r"[，,。.;；].*$", "", first_word)
    return RATING_MAP.get(first_word.lower(), RATING_MAP.get(first_word, "Unknown"))


def _extract_rating(text: str) -> str:
    raw_rating = _extract_section(
        text,
        [
            "Rating",
            "评级",
            "最终评级",
            "投资评级",
            "投资决策",
            "推荐",
            "Recommendation",
        ],
    )
    rating = _normalize_rating(raw_rating)
    if rating != "Unknown":
        return rating

    for token, normalized in RATING_MAP.items():
        if re.fullmatch(r"[a-z]+", token):
            pattern = rf"\b{re.escape(token)}\b"
            if re.search(pattern, text, flags=re.IGNORECASE):
                return normalized
        elif token in text:
            return normalized
    return "Unknown"


def parse_report_dir(report_dir: str | Path) -> ReportView:
    """Parse ticker, generated datetime, rating, and thesis snippets."""
    report_dir = Path(report_dir)
    ticker_match = re.match(r"([0-9]{6}\.(?:SZ|SH|BJ))_", report_dir.name, re.I)
    if not ticker_match:
        raise ValueError(f"Cannot parse ticker from report directory name: {report_dir}")
    ticker = ticker_match.group(1).upper()

    complete_path = report_dir / "complete_report.md"
    decision_path = report_dir / "5_portfolio" / "decision.md"
    if not complete_path.exists():
        raise FileNotFoundError(f"Missing complete report: {complete_path}")
    if not decision_path.exists():
        raise FileNotFoundError(f"Missing portfolio decision: {decision_path}")

    complete_text = read_text_fallback(complete_path)
    decision_text = read_text_fallback(decision_path)

    generated_match = re.search(r"Generated:\s*([0-9]{4}-[0-9]{2}-[0-9]{2}(?:\s+[0-9]{2}:[0-9]{2}:[0-9]{2})?)", complete_text)
    if generated_match:
        generated_text = generated_match.group(1)
        fmt = "%Y-%m-%d %H:%M:%S" if " " in generated_text else "%Y-%m-%d"
        report_datetime = datetime.strptime(generated_text, fmt)
    else:
        report_datetime = datetime.fromtimestamp(complete_path.stat().st_mtime)

    rating = _extract_rating(decision_text)
    core_bet = _extract_section(
        decision_text,
        [
            "Core Bet",
            "核心下注主线",
            "核心交易主线",
            "核心下注",
            "核心押注",
            "我们的核心押注",
            "核心赌注",
            "我们的核心赌注",
            "核心判断",
            "核心论点",
            "核心论题",
            "核心投资判断",
            "核心投资论点",
            "核心投资主线",
        ],
    )
    conviction = _extract_section(
        decision_text,
        [
            "Conviction And Position",
            "Conviction Level",
            "观点强度与仓位",
            "仓位与把握度",
            "仓位建议",
            "执行与仓位",
            "组合执行",
            "交易与仓位",
            "行动",
            "操作建议",
            "交易行动",
            "持仓建议",
        ],
    )

    return ReportView(
        report_dir=report_dir,
        ticker=ticker,
        report_datetime=report_datetime,
        rating=rating,
        core_bet=core_bet,
        conviction=conviction,
    )


def _to_tushare_date(dt: datetime) -> str:
    return dt.strftime("%Y%m%d")


def fetch_daily_prices(ts_code: str, start: datetime, end: datetime, *, index: bool = False) -> pd.DataFrame:
    """Fetch real daily close prices from Tushare."""
    try:
        pro = get_tushare_pro_client()
    except TushareClientError as exc:
        raise RuntimeError(str(exc)) from exc

    fields = "ts_code,trade_date,open,high,low,close,pre_close,pct_chg"
    if index:
        data = pro.index_daily(
            ts_code=ts_code,
            start_date=_to_tushare_date(start),
            end_date=_to_tushare_date(end),
            fields=fields,
        )
    else:
        data = pro.daily(
            ts_code=ts_code,
            start_date=_to_tushare_date(start),
            end_date=_to_tushare_date(end),
            fields=fields,
        )

    if data is None or data.empty:
        return pd.DataFrame()

    data = data.copy()
    data["trade_date"] = pd.to_datetime(data["trade_date"], format="%Y%m%d", errors="coerce")
    data = data.dropna(subset=["trade_date"]).sort_values("trade_date")
    for col in ("open", "high", "low", "close", "pre_close", "pct_chg"):
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
    return data.dropna(subset=["close"])


def _max_drawdown(close: pd.Series) -> float:
    if close.empty:
        return float("nan")
    drawdown = close / close.cummax() - 1.0
    return float(drawdown.min())


def _max_gain(close: pd.Series) -> float:
    if close.empty:
        return float("nan")
    return float(close.max() / close.iloc[0] - 1.0)


def _hit_result(rating: str, excess_return: float, hold_band: float) -> str:
    if pd.isna(excess_return):
        return "unavailable"
    if rating in POSITIVE_RATINGS:
        return "hit" if excess_return > 0 else "miss"
    if rating in NEGATIVE_RATINGS:
        return "hit" if excess_return < 0 else "miss"
    if rating == "Hold":
        return "hit" if abs(excess_return) <= hold_band else "miss"
    return "unrated"


def evaluate_report(
    report_dir: str | Path,
    horizons: Iterable[int] = (20, 60, 120),
    benchmark: str = "000300.SH",
    hold_band: float = 0.02,
) -> pd.DataFrame:
    """Evaluate one saved report across trading-day horizons.

    Entry policy is the next available trading day's close after the report date.
    This avoids using the same close that the report may already have seen.
    """
    view = parse_report_dir(report_dir)
    max_horizon = max(horizons)
    start = view.report_datetime + timedelta(days=1)
    end = view.report_datetime + timedelta(days=max_horizon * 3 + 30)

    stock = fetch_daily_prices(view.ticker, start, end, index=False)
    bench = fetch_daily_prices(benchmark, start, end, index=True)
    if stock.empty or bench.empty:
        return pd.DataFrame([
            {
                "report_dir": str(view.report_dir),
                "ticker": view.ticker,
                "report_date": view.report_datetime.date().isoformat(),
                "rating": view.rating,
                "horizon_days": None,
                "status": "price_unavailable",
            }
        ])

    rows = []
    entry_stock = stock.iloc[0]
    entry_bench = bench[bench["trade_date"] >= entry_stock["trade_date"]]
    if entry_bench.empty:
        entry_bench = bench
    entry_bench = entry_bench.iloc[0]

    for horizon in horizons:
        if len(stock) <= horizon or len(bench) <= horizon:
            rows.append(
                {
                    "report_dir": str(view.report_dir),
                    "ticker": view.ticker,
                    "report_date": view.report_datetime.date().isoformat(),
                    "rating": view.rating,
                    "core_bet": view.core_bet,
                    "conviction": view.conviction,
                    "horizon_days": horizon,
                    "status": "insufficient_future_data",
                    "available_stock_days": len(stock),
                    "available_benchmark_days": len(bench),
                }
            )
            continue

        end_stock = stock.iloc[horizon]
        end_bench_candidates = bench[bench["trade_date"] >= end_stock["trade_date"]]
        end_bench = end_bench_candidates.iloc[0] if not end_bench_candidates.empty else bench.iloc[horizon]

        stock_window = stock.iloc[: horizon + 1]["close"].reset_index(drop=True)
        stock_return = float(end_stock["close"] / entry_stock["close"] - 1.0)
        bench_return = float(end_bench["close"] / entry_bench["close"] - 1.0)
        excess_return = stock_return - bench_return

        rows.append(
            {
                "report_dir": str(view.report_dir),
                "ticker": view.ticker,
                "report_date": view.report_datetime.date().isoformat(),
                "rating": view.rating,
                "core_bet": view.core_bet,
                "conviction": view.conviction,
                "entry_date": entry_stock["trade_date"].date().isoformat(),
                "entry_close": round(float(entry_stock["close"]), 4),
                "horizon_days": horizon,
                "exit_date": end_stock["trade_date"].date().isoformat(),
                "exit_close": round(float(end_stock["close"]), 4),
                "stock_return": stock_return,
                "benchmark": benchmark,
                "benchmark_return": bench_return,
                "excess_return": excess_return,
                "max_drawdown": _max_drawdown(stock_window),
                "max_gain": _max_gain(stock_window),
                "hit_result": _hit_result(view.rating, excess_return, hold_band),
                "status": "ok",
            }
        )

    return pd.DataFrame(rows)


def evaluate_report_tree(
    reports_root: str | Path = "reports",
    horizons: Iterable[int] = (20, 60, 120),
    benchmark: str = "000300.SH",
    hold_band: float = 0.02,
) -> pd.DataFrame:
    """Evaluate every report directory under reports_root."""
    reports_root = Path(reports_root)
    frames = []
    for report_dir in sorted(reports_root.glob("*_*")):
        if not report_dir.is_dir():
            continue
        decision_path = report_dir / "5_portfolio" / "decision.md"
        complete_path = report_dir / "complete_report.md"
        if not decision_path.exists() or not complete_path.exists():
            continue
        try:
            frames.append(evaluate_report(report_dir, horizons, benchmark, hold_band))
        except Exception as exc:
            frames.append(
                pd.DataFrame([
                    {
                        "report_dir": str(report_dir),
                        "ticker": report_dir.name.split("_", 1)[0],
                        "rating": "Unknown",
                        "horizon_days": None,
                        "status": "error",
                        "error": str(exc),
                    }
                ])
            )

    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def summarize_validation(results: pd.DataFrame) -> pd.DataFrame:
    """Summarize hit rate and returns by rating and horizon."""
    ok = results[results.get("status").eq("ok")].copy() if "status" in results else pd.DataFrame()
    if ok.empty:
        return pd.DataFrame()

    summary = (
        ok.assign(hit=lambda df: df["hit_result"].eq("hit").astype(float))
        .groupby(["rating", "horizon_days"], dropna=False)
        .agg(
            count=("ticker", "count"),
            hit_rate=("hit", "mean"),
            avg_stock_return=("stock_return", "mean"),
            avg_benchmark_return=("benchmark_return", "mean"),
            avg_excess_return=("excess_return", "mean"),
            avg_max_drawdown=("max_drawdown", "mean"),
            avg_max_gain=("max_gain", "mean"),
        )
        .reset_index()
    )
    return summary
