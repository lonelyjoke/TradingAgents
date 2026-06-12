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
    "\u5f3a\u70c8\u4e70\u5165": "Buy",
    "\u4e70\u5165": "Buy",
    "\u9ad8\u914d": "Overweight",
    "\u8d85\u914d": "Overweight",
    "\u589e\u6301": "Overweight",
    "\u6301\u6709": "Hold",
    "\u4e2d\u6027": "Hold",
    "\u4f4e\u914d": "Underweight",
    "\u51cf\u6301": "Underweight",
    "\u5356\u51fa": "Sell",
    "\u56de\u907f": "Sell",
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

_SAFETY_PRICE_TERMS = (
    "safety price",
    "defensive build anchor",
    "margin of safety",
    "slow accumulation",
    "normalized",
    "low-cycle",
    "fcf",
    "dividend yield",
    "book value",
    "pb",
    "roe",
    "cash conversion",
    "leverage",
    "payout",
    "valuation floor",
    "mean-revert",
    "invalidate",
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


_KEY_DATA_TERMS = (
    "key data check",
    "reconcile",
    "source-backed",
    "revenue",
    "net profit",
    "eps",
    "market cap",
    "operating cash flow",
    "capex",
    "contract liabilities",
    "orders",
    "backlog",
    "pe",
    "pb",
    "关键数据",
    "校验",
    "收入",
    "净利润",
    "每股收益",
    "市值",
    "经营现金流",
    "资本开支",
    "合同负债",
    "订单",
)

_EXPECTATION_GAP_EVIDENCE_TERMS = (
    "expectation-gap evidence",
    "market-implied",
    "valuation percentile",
    "price-eps",
    "multiple",
    "consensus",
    "sell-side",
    "holder",
    "technical",
    "investor interaction",
    "预期差",
    "市场隐含",
    "估值分位",
    "一致预期",
    "股东",
    "技术面",
    "投资者互动",
)

_UNDERWRITING_OPTIONALITY_TERMS = (
    "unit-economics bridge",
    "project ramp",
    "capacity bridge",
    "financing / listing scenario",
    "take rate",
    "breakeven",
    "occupancy",
    "utilization",
    "dilution",
    "use of proceeds",
    "单位经济",
    "费率",
    "盈亏平衡",
    "出租率",
    "利用率",
    "上市",
    "融资",
    "摊薄",
)

_FILING_INTERNAL_QUALITY_TERMS = (
    "filing internal quality",
    "accounting reconciliation",
    "segment economics",
    "footnote",
    "cash-flow quality",
    "cash flow quality",
    "capex",
    "cip",
    "md&a",
    "non-recurring",
    "balance-sheet forward",
    "shareholder-return",
    "disclosure quality",
)

_VERIFICATION_CALENDAR_TERMS = (
    "verification calendar",
    "next disclosure",
    "add",
    "hold",
    "trim",
    "downgrade",
    "exit",
    "半年度",
    "三季报",
    "年报",
    "加仓",
    "持有",
    "减仓",
    "下调",
    "退出",
    "验证日历",
)

_MEDICAL_DEVICE_TRIGGER_TERMS = (
    "medical device",
    "IVD",
    "in vitro diagnostic",
    "reagent",
    "analyzer",
    "医疗器械",
    "医疗设备",
    "体外诊断",
    "试剂",
    "耗材",
    "装机",
    "监护仪",
    "麻醉机",
    "超声",
    "医学影像",
)

_MEDICAL_DEVICE_DEPTH_TERMS = (
    "installed base",
    "replacement cycle",
    "tender",
    "procurement",
    "VBP",
    "registration",
    "FDA",
    "CE",
    "NMPA",
    "channel inventory",
    "distributor",
    "reagent pull-through",
    "service attach",
    "segment gross margin",
    "cash conversion",
    "receivables",
    "inventory",
    "contract liabilities",
    "SOTP",
    "装机",
    "替换周期",
    "招标",
    "中标",
    "采购",
    "集采",
    "带量采购",
    "注册证",
    "海外渠道",
    "渠道库存",
    "经销商",
    "试剂拉动",
    "试剂耗材",
    "服务收入",
    "分部毛利",
    "应收",
    "存货",
    "合同负债",
    "现金转化",
    "分部估值",
)

_MEDICAL_DEVICE_QUESTION_TERMS = (
    "evidence gate",
    "company-specific follow-up",
    "research gaps",
    "verification calendar",
    "conviction cap",
    "证据门禁",
    "公司专属",
    "研究缺口",
    "验证日历",
    "确信度",
    "仓位",
)

_BATTERY_MATERIAL_TRIGGER_TERMS = (
    "cathode",
    "precursor",
    "LFP",
    "lithium battery materials",
    "正极材料",
    "磷酸铁锂",
    "三元材料",
    "前驱体",
    "锂电材料",
    "电池材料",
)

_BATTERY_MATERIAL_DEPTH_TERMS = (
    "ASP",
    "lithium carbonate",
    "processing fee",
    "spread",
    "pass-through",
    "capacity utilization",
    "shipment",
    "customer mix",
    "CATL",
    "BYD",
    "contract liabilities",
    "receivables",
    "inventory",
    "OCF",
    "credit impairment",
    "capex",
    "碳酸锂",
    "售价",
    "价差",
    "加工费",
    "价格传导",
    "产能利用率",
    "出货",
    "销量",
    "客户结构",
    "宁德时代",
    "比亚迪",
    "合同负债",
    "应收",
    "票据",
    "存货",
    "经营现金流",
    "信用减值",
    "资本开支",
)

_BATTERY_MATERIAL_GATE_TERMS = (
    "KPI",
    "evidence gate",
    "driver bridge",
    "forecast",
    "verification calendar",
    "research gap",
    "证据门禁",
    "驱动桥",
    "预测",
    "验证日历",
    "研究缺口",
    "确信度",
    "仓位",
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

    if "Safety Price / Defensive Build Anchor" in decision_text and _term_hits(decision_text, _SAFETY_PRICE_TERMS) < 6:
        issues.append(
            DecisionDepthIssue(
                "value_stock_safety_price",
                "warning",
                "safety price is present but lacks enough financial-state support, margin-of-safety logic, or invalidation conditions",
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

    if _term_hits(decision_text, _KEY_DATA_TERMS) < 5:
        issues.append(
            DecisionDepthIssue(
                "key_data_check",
                "warning",
                "missing or shallow key data check for thesis-critical figures and unit/period conflicts",
            )
        )

    if _term_hits(decision_text, _EXPECTATION_GAP_EVIDENCE_TERMS) < 4:
        issues.append(
            DecisionDepthIssue(
                "expectation_gap_evidence",
                "warning",
                "expectation gap is asserted without enough market-implied or consensus/holder/technical evidence",
            )
        )

    if _term_hits(decision_text, _UNDERWRITING_OPTIONALITY_TERMS) < 3:
        issues.append(
            DecisionDepthIssue(
                "underwriting_modules",
                "warning",
                "missing unit-economics, project-ramp, or financing/listing scenario bridge where applicable",
            )
        )

    if _term_hits(decision_text, _FILING_INTERNAL_QUALITY_TERMS) < 5:
        issues.append(
            DecisionDepthIssue(
                "filing_internal_quality",
                "warning",
                "missing or shallow filing-internal quality review across accounting, footnotes, cash flow, capex, disclosure, or shareholder-return evidence",
            )
        )

    if _term_hits(decision_text, _VERIFICATION_CALENDAR_TERMS) < 4:
        issues.append(
            DecisionDepthIssue(
                "verification_calendar",
                "warning",
                "missing action-linked verification calendar for add/hold/trim/downgrade decisions",
            )
        )

    if _term_hits(decision_text, _MEDICAL_DEVICE_TRIGGER_TERMS) >= 2:
        if _term_hits(decision_text, _MEDICAL_DEVICE_DEPTH_TERMS) < 8:
            issues.append(
                DecisionDepthIssue(
                    "medical_device_evidence_gate",
                    "warning",
                    "medical-device report lacks installed-base/reagent/VBP/registration/channel/cash-conversion evidence-gate depth",
                )
            )
        if _term_hits(decision_text, _MEDICAL_DEVICE_QUESTION_TERMS) < 3:
            issues.append(
                DecisionDepthIssue(
                    "medical_device_follow_up_questions",
                    "warning",
                    "medical-device report does not carry unanswered company-specific questions into gaps, conviction, sizing, or verification calendar",
                )
            )

    if _term_hits(decision_text, _BATTERY_MATERIAL_TRIGGER_TERMS) >= 1:
        if _term_hits(decision_text, _BATTERY_MATERIAL_DEPTH_TERMS) < 9:
            issues.append(
                DecisionDepthIssue(
                    "battery_material_evidence_gate",
                    "warning",
                    "battery-material report lacks ASP/lithium-cost/spread/utilization/customer/cash-conversion evidence-gate depth",
                )
            )
        if _term_hits(decision_text, _BATTERY_MATERIAL_GATE_TERMS) < 3:
            issues.append(
                DecisionDepthIssue(
                    "battery_material_driver_bridge",
                    "warning",
                    "battery-material report does not turn industry KPIs into forecast drivers, conviction caps, sizing, and verification calendar",
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
