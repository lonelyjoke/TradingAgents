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
import json
import re
from typing import Any, Iterable, Mapping

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


# Deterministic contradictions and missing mandatory deep-research contracts
# block formal publication. Ordinary unavailable inputs remain neutral evidence:
# they can leave a cell missing and cap confidence, but cannot manufacture a
# bullish/bearish conclusion. The six universal company-depth sections are
# publication requirements because a memo without them is not a deep report.
PUBLICATION_BLOCKING_SECTIONS = frozenset(
    {
        "eps_profit_share_count_consistency",
        "pb_bvps_arithmetic",
        "safety_price_pb_bridge",
        "profit_pe_per_share_bridge",
        "q2_h1_period_semantics",
        "scenario_probability_math",
        "scenario_weighted_value_math",
        "scenario_contribution_math",
        "forecast_growth_arithmetic",
        "option_value_arithmetic",
        "scenario_weighted_range_math",
        "expected_return_range_math",
        "financial_calendar_period",
        "period_comparator_lineage",
        "upside_discount_math",
        "industry_playbook_alignment",
        "segment_growth_rank_consistency",
        "underwriting_readiness",
        "shared_model_change_audit",
        "pm_structured_generation",
        "research_manager_structured_generation",
        "share_count_source_conflict",
        "handoff_numeric_consistency",
    }
)


def _handoff_metric_key(period: Any, metric: Any) -> tuple[str, str]:
    normalized_period = re.sub(r"\s+", "", str(period or "")).lower()
    normalized_metric = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", str(metric or "")).lower()
    aliases = {
        "dilutedsharecount": "dilutedshares",
        "sharecount": "dilutedshares",
        "dilutedshares": "dilutedshares",
        "稀释股本": "dilutedshares",
        "总股本": "dilutedshares",
        "revenue": "revenue",
        "营业收入": "revenue",
        "营收": "revenue",
        "parentnetprofit": "parentnetprofit",
        "netprofitparent": "parentnetprofit",
        "归母净利润": "parentnetprofit",
        "dilutedeps": "eps",
        "eps": "eps",
        "每股收益": "eps",
        "稀释每股收益": "eps",
        "operatingcashflowocf": "ocf",
        "operatingcashflow": "ocf",
        "ocf": "ocf",
        "经营活动现金流净额": "ocf",
        "capitalexpenditurecapex": "capex",
        "capitalexpenditure": "capex",
        "capex": "capex",
        "资本开支": "capex",
        "freecashflowfcf": "fcf",
        "freecashflow": "fcf",
        "fcf": "fcf",
        "自由现金流": "fcf",
        "grossmargin": "grossmargin",
        "毛利率": "grossmargin",
        "operatingprofit": "operatingprofit",
        "营业利润": "operatingprofit",
    }
    canonical_metric = aliases.get(normalized_metric, normalized_metric)
    if canonical_metric == "dilutedshares":
        normalized_period = "current"
    return normalized_period, canonical_metric


def _numeric_line_map(payload: Mapping[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    result: dict[tuple[str, str], dict[str, Any]] = {}
    for row in payload.get("canonical_model_snapshot", []) or []:
        key = _handoff_metric_key(row.get("period"), row.get("metric"))
        if row.get("value") is not None:
            result[key] = dict(row)
    return result


def _underwriting_numeric_line_map(packet: Mapping[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    result: dict[tuple[str, str], dict[str, Any]] = {}
    company = dict(packet.get("company_model", {}))
    shares = company.get("diluted_share_count_mn")
    if shares is not None:
        result[_handoff_metric_key("current", "diluted shares")] = {
            "line_id": "shares",
            "period": company.get("share_count_period", "current"),
            "metric": "diluted shares",
            "value": shares,
            "unit": "mn shares",
        }
    years = list(packet.get("forecast_years", []))
    for row in packet.get("forecast_lines", []) or []:
        if str(row.get("segment", "")).lower() not in {
            "consolidated",
            "group",
            "合并",
            "公司整体",
        }:
            continue
        for index, value_key in enumerate(
            ("year_1_value", "year_2_value", "year_3_value")
        ):
            if index >= len(years) or row.get(value_key) is None:
                continue
            result[_handoff_metric_key(years[index], row.get("metric"))] = {
                "line_id": f"{years[index]}_{row.get('metric', '')}",
                "period": years[index],
                "metric": row.get("metric", ""),
                "value": row.get(value_key),
                "unit": row.get("unit", ""),
            }
    return result


def _change_ids(payload: Mapping[str, Any], field: str) -> set[str]:
    return {
        str(row.get("line_id", "")).strip().lower()
        for row in payload.get(field, []) or []
        if str(row.get("line_id", "")).strip()
        and str(row.get("disposition", "")).lower() == "accepted"
    }


def _line_changed(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    try:
        left_value = float(left.get("value"))
        right_value = float(right.get("value"))
    except (TypeError, ValueError):
        return left.get("value") != right.get("value")
    value_changed = abs(left_value - right_value) > max(
        abs(left_value) * 0.02,
        0.01,
    )
    left_unit = re.sub(r"\s+", "", str(left.get("unit", "")).lower())
    right_unit = re.sub(r"\s+", "", str(right.get("unit", "")).lower())
    return value_changed or (left_unit and right_unit and left_unit != right_unit)


def audit_handoff_numeric_consistency(report_dir: str | Path) -> list[DecisionDepthIssue]:
    """Compare underwriting -> Research Manager -> PM machine-readable values."""
    report_path = Path(report_dir)
    manager_path = report_path / "2_research" / "canonical_plan.json"
    pm_path = report_path / "5_portfolio" / "canonical_decision.json"
    if not manager_path.exists() and not pm_path.exists():
        return []
    issues: list[DecisionDepthIssue] = []
    underwriting_path = report_path / "0_context" / "company_underwriting.json"
    try:
        packet = json.loads(read_text_fallback(underwriting_path))
        manager = json.loads(read_text_fallback(manager_path))
        pm = json.loads(read_text_fallback(pm_path))
    except (OSError, TypeError, json.JSONDecodeError) as exc:
        return [
            DecisionDepthIssue(
                "handoff_numeric_consistency",
                "error",
                f"canonical handoff artifact is missing or unreadable: {exc}",
            )
        ]
    initial_map = _underwriting_numeric_line_map(packet)
    manager_map = _numeric_line_map(manager)
    pm_map = _numeric_line_map(pm)
    manager_change_ids = _change_ids(manager, "model_change_rows")
    pm_change_ids = _change_ids(pm, "handoff_change_rows")

    for key, initial in initial_map.items():
        accepted = manager_map.get(key)
        if accepted is None:
            issues.append(
                DecisionDepthIssue(
                    "handoff_numeric_consistency",
                    "error",
                    f"Research Manager canonical snapshot dropped {key[0]} {key[1]}",
                )
            )
            continue
        if _line_changed(initial, accepted) and str(
            accepted.get("line_id", "")
        ).lower() not in manager_change_ids:
            issues.append(
                DecisionDepthIssue(
                    "handoff_numeric_consistency",
                    "error",
                    f"Research Manager silently changed {key[0]} {key[1]} from "
                    f"{initial.get('value')} {initial.get('unit')} to "
                    f"{accepted.get('value')} {accepted.get('unit')}",
                )
            )
    for key, accepted in manager_map.items():
        final = pm_map.get(key)
        if final is None:
            issues.append(
                DecisionDepthIssue(
                    "handoff_numeric_consistency",
                    "error",
                    f"Portfolio Manager canonical snapshot dropped {key[0]} {key[1]}",
                )
            )
            continue
        if _line_changed(accepted, final) and str(final.get("line_id", "")).lower() not in pm_change_ids:
            issues.append(
                DecisionDepthIssue(
                    "handoff_numeric_consistency",
                    "error",
                    f"Portfolio Manager silently changed {key[0]} {key[1]} from "
                    f"{accepted.get('value')} {accepted.get('unit')} to "
                    f"{final.get('value')} {final.get('unit')}",
                )
            )
    return issues

PUBLICATION_BLOCKING_DEPTH_SECTIONS = frozenset()


def _is_publication_blocker(section: str, severity: str) -> bool:
    return (
        severity == "error" and section in PUBLICATION_BLOCKING_SECTIONS
    ) or (
        severity == "warning" and section in PUBLICATION_BLOCKING_DEPTH_SECTIONS
    )


def _normalized_mention(text: object) -> str:
    return re.sub(r"[\W_]+", "", str(text or "")).lower()


def _segment_is_mentioned(row: Mapping[str, Any], decision_text: str) -> bool:
    normalized_decision = _normalized_mention(decision_text)
    segment = str(row.get("segment", "")).strip()
    root = re.split(r"[（(]", segment, maxsplit=1)[0].strip()
    aliases = row.get("aliases") or []
    if isinstance(aliases, str):
        aliases = [aliases]
    candidates = [segment, root, *list(aliases)]
    normalized_candidates = {
        _normalized_mention(candidate)
        for candidate in candidates
        if len(_normalized_mention(candidate)) >= 2
    }
    return any(candidate in normalized_decision for candidate in normalized_candidates)


def _safe_float(value: object) -> float:
    try:
        return float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0


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

_SEGMENT_PROSPERITY_TERMS = (
    "segment prosperity",
    "prosperity level",
    "marginal direction",
    "demand",
    "supply",
    "capacity",
    "utilization",
    "asp",
    "margin",
    "working capital",
    "cash flow",
    "counterevidence",
    "confidence",
    "eps",
    "fcf",
    "分部景气",
    "景气水平",
    "边际方向",
    "需求",
    "供给",
    "产能",
    "利用率",
    "价格",
    "毛利",
    "现金流",
    "反证",
    "置信度",
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

_WIND_EQUIPMENT_TERMS = (
    "wind power",
    "offshore wind",
    "monopile",
    "jacket foundation",
    "风电",
    "海上风电",
    "海风",
    "塔筒",
    "管桩",
    "导管架",
    "海工",
    "风电装备",
)

_LITHIUM_BATTERY_ROUTE_TERMS = (
    "Lithium battery chain",
    "battery / energy-storage chain",
    "Cathode / material revenue",
    "lithium carbonate",
    "Downstream cells",
    "Power battery revenue",
    "锂电",
    "动力电池",
    "储能电池",
    "碳酸锂",
    "正极材料",
    "电芯",
)

_TELECOM_OPERATOR_TERMS = (
    "telecom operator",
    "telecommunication",
    "mobile subscribers",
    "mobile ARPU",
    "broadband",
    "cloud/AI",
    "中国电信",
    "中国移动",
    "中国联通",
    "电信运营",
    "移动用户",
    "宽带",
    "ARPU",
    "天翼云",
    "分红",
)

_PROJECT_ORDER_TRIGGER_TERMS = (
    "order",
    "backlog",
    "contract liabilities",
    "project",
    "订单",
    "在手订单",
    "新签",
    "合同负债",
    "项目",
    "交付",
)

_ORDER_BRIDGE_TERMS = (
    "opening backlog",
    "new orders",
    "delivered",
    "ending backlog",
    "receivables",
    "inventory",
    "cash collection",
    "期初",
    "新签",
    "交付",
    "期末",
    "应收",
    "存货",
    "发出商品",
    "回款",
)

_TRUE_PEER_TERMS = (
    "true operating peer",
    "business-comparable",
    "broad industry",
    "substitute",
    "alternative",
    "relative allocation",
    "真实可比",
    "业务可比",
    "宽行业",
    "替代表达",
    "相对配置",
)

_SCENARIO_SENSITIVITY_TERMS = (
    "bull",
    "base",
    "bear",
    "sensitivity",
    "scenario",
    "assumption",
    "2026E",
    "2027E",
    "2028E",
    "牛",
    "中",
    "熊",
    "敏感性",
    "情景",
    "假设",
)

_SECOND_CURVE_TRIGGER_TERMS = (
    "second curve",
    "new business",
    "optionality",
    "ship",
    "capacity",
    "project ramp",
    "第二曲线",
    "新业务",
    "期权",
    "船舶",
    "产能",
    "放量",
)

_SECOND_CURVE_DEPTH_TERMS = (
    "scenario value",
    "core value",
    "unit economics",
    "utilization",
    "capex",
    "cash conversion",
    "control rights",
    "customer",
    "场景价值",
    "核心估值",
    "单位经济",
    "利用率",
    "资本开支",
    "现金转化",
    "控制权",
    "客户",
)

_EVIDENCE_GRADE_TERMS = (
    "reported",
    "calculated",
    "estimated",
    "proxy",
    "stale",
    "missing",
    "unverified",
    "source period",
    "已披露",
    "计算",
    "估算",
    "代理",
    "滞后",
    "缺失",
    "未验证",
    "来源期间",
)


def _section_text(text: str, label: str) -> str:
    pattern = rf"\*\*{re.escape(label)}\*\*:\s*(.*?)(?:\n\n\*\*[^*\n]+\*\*:|\Z)"
    match = re.search(pattern, text, flags=re.S)
    return match.group(1).strip() if match else ""


def _heading_text(text: str, heading: str) -> str:
    """Return a Markdown heading body without depending on report language."""
    aliases = {
        "Company Disaggregation": ("Company Disaggregation", "二、公司业务与利润池拆解"),
        "Autonomous Three-Year Forecast Model": (
            "Autonomous Three-Year Forecast Model",
            "四、三年盈利及现金流预测",
        ),
        "Thesis-to-Financial Bridge": (
            "Thesis-to-Financial Bridge",
            "五、核心论点、护城河与财务传导",
        ),
        "Moat Evidence Scorecard": (
            "Moat Evidence Scorecard",
            "五、核心论点、护城河与财务传导",
        ),
        "Valuation Closure": ("Valuation Closure", "七、估值、情景与预期收益"),
        "Handoff Integrity Audit": (
            "Handoff Integrity Audit",
            "附录A：模型变更与交接审计",
        ),
    }
    heading_pattern = "(?:" + "|".join(
        re.escape(value) for value in aliases.get(heading, (heading,))
    ) + ")"
    pattern = (
        rf"^##\s+{heading_pattern}\s*$\n(.*?)"
        rf"(?=^##\s+|\Z)"
    )
    match = re.search(pattern, text, flags=re.M | re.S | re.I)
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

    company_map = _heading_text(decision_text, "Company Disaggregation")
    if len(company_map) < 300 or not any(
        token in company_map.lower()
        for token in ("reported", "analytical", "missing", "disclosed", "披露", "缺失", "分析口径")
    ):
        issues.append(
            DecisionDepthIssue(
                "company_disaggregation",
                "warning",
                "company map does not separate reported segments from economic product/channel/geography/customer/project units with disclosure limits",
            )
        )

    autonomous_model = _heading_text(
        decision_text, "Autonomous Three-Year Forecast Model"
    )
    model_years = sorted(set(re.findall(r"20\d{2}E", autonomous_model, re.I)))
    if len(autonomous_model) < 450 or len(model_years) < 3:
        issues.append(
            DecisionDepthIssue(
                "autonomous_forecast_model",
                "warning",
                "independent operating-driver model does not preserve three explicit forward years",
            )
        )

    thesis_bridge = _heading_text(decision_text, "Thesis-to-Financial Bridge")
    bridge_hits = _term_hits(
        thesis_bridge,
        (
            "formula",
            "assumption",
            "bull",
            "base",
            "bear",
            "revenue",
            "profit",
            "EPS",
            "FCF",
            "capital",
            "fair value",
            "公允价值",
            "财务传导",
            "公式",
            "假设",
            "收入",
            "利润",
            "资本",
            "估值",
            "公式",
            "假设",
            "收入",
            "利润",
            "资本",
            "估值",
        ),
    )
    if len(thesis_bridge) < 220 or bridge_hits < 5:
        issues.append(
            DecisionDepthIssue(
                "thesis_financial_bridge",
                "warning",
                "decisive claims are not translated through assumptions and formulas into earnings/cash-or-capital/fair-value effects",
            )
        )

    moat_scorecard = _heading_text(decision_text, "Moat Evidence Scorecard")
    moat_hits = _term_hits(
        moat_scorecard,
        (
            "proven",
            "partial",
            "unproven",
            "rejected",
            "peer",
            "history",
            "counterevidence",
            "margin",
            "cash",
            "ROIC",
            "已验证",
            "部分验证",
            "未证实",
            "反证",
            "同行",
            "财务传导",
            "已证实",
            "部分",
            "未证实",
            "反证",
            "同业",
        ),
    )
    if len(moat_scorecard) < 240 or moat_hits < 4:
        issues.append(
            DecisionDepthIssue(
                "moat_evidence_scorecard",
                "warning",
                "moat claims lack observable history/true-peer tests, counterevidence and financial transmission",
            )
        )
    unsupported_verified_moats = [
        line.strip()
        for line in moat_scorecard.splitlines()
        if re.search(r"(?:已验证|(?<!un)\bproven\b)", line, re.I)
        and not re.search(r"\b(?:EV|KPE|KF)\d+\b", line, re.I)
    ]
    if unsupported_verified_moats:
        issues.append(
            DecisionDepthIssue(
                "moat_evidence_lineage",
                "error",
                "moat is labelled proven without an EV/KPE/KF evidence id: "
                + unsupported_verified_moats[0][:180],
            )
        )

    valuation_closure = _heading_text(decision_text, "Valuation Closure")
    valuation_hits = _term_hits(
        valuation_closure,
        (
            "core",
            "scenario",
            "optionality",
            "excluded",
            "share count",
            "per share",
            "probability",
            "double count",
            "current price",
            "expected return",
            "概率加权",
            "公允价值",
            "当前股价",
            "预期收益",
            "重复计算",
            "核心",
            "情景",
            "期权",
            "股本",
            "每股",
            "核心",
            "情景",
            "期权",
            "股本",
            "每股",
            "概率",
            "重复计价",
            "现价",
            "预期收益",
        ),
    )
    if len(valuation_closure) < 350 or valuation_hits < 6:
        issues.append(
            DecisionDepthIssue(
                "valuation_closure",
                "warning",
                "valuation does not close mutually exclusive buckets to probability-weighted per-share value, expected return and double-counting control",
            )
        )

    handoff_audit = _heading_text(decision_text, "Handoff Integrity Audit")
    if len(handoff_audit) < 220 or _term_hits(
        handoff_audit,
        (
            "version",
            "preserved",
            "revised",
            "unresolved",
            "evidence",
            "old",
            "new",
            "版本",
            "保留",
            "修改",
            "未解决",
            "证据",
            "原值",
            "新值",
        ),
    ) < 3:
        issues.append(
            DecisionDepthIssue(
                "handoff_integrity_audit",
                "warning",
                "final memo does not prove that business units, all forecast years, thesis bridges and valuation buckets survived the agent handoff",
            )
        )

    segment = _section_text(decision_text, "Investment Thesis")
    has_segment_section = bool(company_map) or "Business Segment Breakdown:" in segment or any(
        marker in decision_text
        for marker in ("## 业务分部", "## 业务板块", "### 业务分部", "业务分部与估值")
    )
    segment_scope = company_map or (
        segment if "Business Segment Breakdown:" in segment else decision_text
    )
    if not has_segment_section:
        issues.append(
            DecisionDepthIssue(
                "business_segment_breakdown",
                "warning",
                "missing explicit Business Segment Breakdown in the final thesis",
            )
        )
    elif _term_hits(segment_scope, _SEGMENT_DEPTH_TERMS) < 4:
        issues.append(
            DecisionDepthIssue(
                "business_segment_breakdown",
                "warning",
                "segment discussion lacks revenue/growth/margin/profit/cash/valuation depth",
            )
        )

    explicit_multi_business = any(
        marker in decision_text.lower()
        for marker in (
            "multi-business",
            "multiple business segments",
            "each material segment",
            "segment prosperity analysis",
            "分业务景气",
            "分部景气",
            "业务板块经济与景气",
            "各业务板块",
            "各业务分部",
        )
    )
    markdown_segment_rows = sum(
        1
        for line in decision_text.splitlines()
        if line.strip().startswith("|")
        and line.count("|") >= 4
        and not re.search(r"\|\s*[-:]+", line)
    )
    if has_segment_section and (explicit_multi_business or markdown_segment_rows >= 3):
        has_prosperity_section = "Segment Prosperity Analysis:" in decision_text or any(
            marker in decision_text
            for marker in ("## 分部景气", "## 业务景气", "分业务景气度", "分部景气度")
        )
        if not has_prosperity_section or _term_hits(decision_text, _SEGMENT_PROSPERITY_TERMS) < 9:
            issues.append(
                DecisionDepthIssue(
                    "segment_prosperity_analysis",
                    "warning",
                    "multi-business report lacks a deep segment-level prosperity matrix with level, direction, dated demand/supply/price/utilization/margin/cash evidence, counterevidence, and EPS/FCF transmission",
                )
            )

    has_peer_section = "Peer Comparison Summary:" in segment or any(
        marker in decision_text
        for marker in ("## 同行", "## 同业", "## 可比公司", "同业/产业对比", "相比同行")
    )
    peer_scope = segment if "Peer Comparison Summary:" in segment else decision_text
    if not has_peer_section:
        issues.append(
            DecisionDepthIssue(
                "peer_comparison_summary",
                "warning",
                "missing explicit Peer Comparison Summary in the final thesis",
            )
        )
    elif _term_hits(peer_scope, _PEER_DEPTH_TERMS) < 5:
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

    order_triggered = any(
        token in decision_text.lower()
        for token in ("order", "backlog", "订单", "新签", "在手订单")
    )
    if order_triggered and _term_hits(decision_text, _PROJECT_ORDER_TRIGGER_TERMS) >= 4 and _term_hits(decision_text, _ORDER_BRIDGE_TERMS) < 6:
        issues.append(
            DecisionDepthIssue(
                "order_backlog_bridge",
                "warning",
                "project/order-driven thesis lacks a full backlog/new-order/delivery/working-capital/cash-collection bridge",
            )
        )

    if _term_hits(decision_text, _TRUE_PEER_TERMS) < 3:
        issues.append(
            DecisionDepthIssue(
                "true_peer_alternatives",
                "warning",
                "peer work does not clearly separate true operating comparables from broad industry screens or substitute expressions",
            )
        )

    if _term_hits(decision_text, _VALUATION_DEPTH_TERMS) >= 2 and _term_hits(decision_text, _SCENARIO_SENSITIVITY_TERMS) < 5:
        issues.append(
            DecisionDepthIssue(
                "scenario_sensitivity_bridge",
                "warning",
                "valuation or safety-price conclusion lacks bull/base/bear, sensitivity, or explicit multi-period assumption bridge",
            )
        )

    second_curve_triggered = any(
        token in decision_text.lower()
        for token in ("second curve", "new business", "shipbuilding", "vessel", "第二曲线", "新业务", "船舶")
    )
    if second_curve_triggered and _term_hits(decision_text, _SECOND_CURVE_TRIGGER_TERMS) >= 3 and _term_hits(decision_text, _SECOND_CURVE_DEPTH_TERMS) < 5:
        issues.append(
            DecisionDepthIssue(
                "second_curve_optionality",
                "warning",
                "second-curve/new-business discussion lacks scenario/core-value treatment, unit economics, utilization, capex, or cash-conversion evidence",
            )
        )

    if _term_hits(decision_text, _EVIDENCE_GRADE_TERMS) < 5:
        issues.append(
            DecisionDepthIssue(
                "evidence_grade_table",
                "warning",
                "decisive claims do not carry enough source/evidence grades such as reported, calculated, estimated, proxy, missing, or unverified",
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

    battery_material_hits = _term_hits(decision_text, _BATTERY_MATERIAL_TRIGGER_TERMS)
    battery_system_hits = _term_hits(
        decision_text,
        ("power battery system", "energy-storage battery system", "动力电池系统", "储能电池系统", "GWh"),
    )
    if battery_material_hits >= 2 and battery_system_hits < 2:
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


def _markdown_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    """Parse simple pipe tables without depending on report-language headings."""
    lines = text.splitlines()
    tables: list[tuple[list[str], list[list[str]]]] = []
    index = 0
    while index + 1 < len(lines):
        header_line = lines[index].strip()
        separator = lines[index + 1].strip()
        if not (header_line.startswith("|") and separator.startswith("|")):
            index += 1
            continue
        if not all(set(cell.strip()) <= {"-", ":"} for cell in separator.strip("|").split("|")):
            index += 1
            continue
        header = [cell.strip().replace("**", "") for cell in header_line.strip("|").split("|")]
        body: list[list[str]] = []
        index += 2
        while index < len(lines) and lines[index].strip().startswith("|"):
            body.append([cell.strip().replace("**", "") for cell in lines[index].strip().strip("|").split("|")])
            index += 1
        tables.append((header, body))
    return tables


def _first_number(text: str) -> float | None:
    match = re.search(r"[-+]?\d[\d,]*(?:\.\d+)?", text or "")
    if not match:
        return None
    try:
        return float(match.group(0).replace(",", ""))
    except ValueError:
        return None


def _range_midpoint(text: str) -> float | None:
    numbers = [
        float(value.replace(",", ""))
        for value in re.findall(r"(?<![\d.])[-+]?\d[\d,]*(?:\.\d+)?", text or "")[:2]
    ]
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def _eps_profit_consistency_issues(decision_text: str) -> list[DecisionDepthIssue]:
    issues: list[DecisionDepthIssue] = []
    for header, rows in _markdown_tables(decision_text):
        year_columns = [index for index, cell in enumerate(header) if re.search(r"20\d{2}(?:E|年|实际)?", cell, re.I)]
        if len(year_columns) < 2:
            continue
        profit_row = next(
            (
                row
                for row in rows
                if row and any(term in row[0].lower() for term in ("net profit", "归母净利润", "净利润"))
            ),
            None,
        )
        eps_row = next(
            (
                row
                for row in rows
                if row and ("eps" in row[0].lower() or "每股收益" in row[0])
            ),
            None,
        )
        if not profit_row or not eps_row:
            continue
        implied_share_proxies: list[float] = []
        for index in year_columns:
            if index >= len(profit_row) or index >= len(eps_row):
                continue
            profit = _range_midpoint(profit_row[index])
            eps = _range_midpoint(eps_row[index])
            if profit is not None and eps is not None and eps > 0:
                implied_share_proxies.append(profit / eps)
        if len(implied_share_proxies) >= 2:
            spread = max(implied_share_proxies) / min(implied_share_proxies) - 1.0
            if spread > 0.05:
                issues.append(
                    DecisionDepthIssue(
                        "eps_profit_share_count_consistency",
                        "error",
                        f"net-profit/EPS rows imply share-count proxies that differ by {spread:.1%}; reconcile units, actual-vs-TTM EPS, dilution, and the share-count assumption",
                    )
                )
                break
    return issues


def _valuation_bridge_issues(decision_text: str) -> list[DecisionDepthIssue]:
    """Reconcile the per-share arithmetic behind PB/PE safety-price claims."""
    issues: list[DecisionDepthIssue] = []
    price_match = re.search(
        r"(?:current price|当前价格|现价)\D{0,18}(\d+(?:\.\d+)?)",
        decision_text,
        re.I,
    )
    combined_pe_pb_match = re.search(
        r"(?:TTM\s*)?PE\s*/\s*PB\D{0,12}(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)",
        decision_text,
        re.I,
    )
    pb_match = re.search(
        r"(?:\bPB\b|P/B|市净率)\s*(?:TTM)?\s*[:：/]?\s*(\d+(?:\.\d+)?)\s*(?:x|倍)?",
        decision_text,
        re.I,
    )
    bvps_match = re.search(
        r"(?:BVPS|每股净资产)\D{0,18}(\d+(?:\.\d+)?)",
        decision_text,
        re.I,
    )
    current_price = float(price_match.group(1)) if price_match else None
    current_pb = (
        float(combined_pe_pb_match.group(2))
        if combined_pe_pb_match
        else float(pb_match.group(1))
        if pb_match
        else None
    )
    stated_bvps = float(bvps_match.group(1)) if bvps_match else None
    derived_bvps: float | None = None
    if current_price and current_pb and current_pb > 0:
        derived_bvps = current_price / current_pb
    if derived_bvps and stated_bvps:
        gap = abs(stated_bvps - derived_bvps) / derived_bvps
        if gap > 0.08:
            issues.append(
                DecisionDepthIssue(
                    "pb_bvps_arithmetic",
                    "error",
                    f"stated BVPS {stated_bvps:.2f} does not reconcile to current price/PB {current_price:.2f}/{current_pb:.2f}={derived_bvps:.2f}",
                )
            )

    safety_lines = [
        line
        for line in decision_text.splitlines()
        if any(token in line.lower() for token in ("安全", "safety", "build anchor", "建仓"))
        and any(token in line.lower() for token in ("p/b", "pb", "市净率"))
    ]
    if derived_bvps:
        for line in safety_lines:
            price_range = re.search(
                r"(?:¥|￥)?\s*(\d+(?:\.\d+)?)\s*(?:-|–|—|至|~)\s*(?:¥|￥)?\s*(\d+(?:\.\d+)?)",
                line,
            )
            pb_range = re.search(
                r"(\d+(?:\.\d+)?)\s*(?:x|倍)?\s*(?:-|–|—|至|~)\s*(\d+(?:\.\d+)?)\s*(?:x|倍)?\s*(?:P/B|PB|市净率)",
                line,
                re.I,
            )
            if not price_range or not pb_range:
                continue
            stated_low, stated_high = sorted(
                (float(price_range.group(1)), float(price_range.group(2)))
            )
            multiple_low, multiple_high = sorted(
                (float(pb_range.group(1)), float(pb_range.group(2)))
            )
            expected_low = derived_bvps * multiple_low
            expected_high = derived_bvps * multiple_high
            if (
                abs(stated_low - expected_low) / max(expected_low, 1.0) > 0.10
                or abs(stated_high - expected_high) / max(expected_high, 1.0) > 0.10
            ):
                issues.append(
                    DecisionDepthIssue(
                        "safety_price_pb_bridge",
                        "error",
                        "safety-price range does not reconcile to current BVPS and the stated PB range",
                    )
                )
                break

    global_share_count_bridge = bool(
        re.search(
            r"(?:diluted\s+share|share\s+count|总股本|稀释股本|股本数).{0,24}?\d+(?:\.\d+)?\s*(?:million|mn|亿股|百万股)",
            decision_text,
            re.I | re.S,
        )
        and re.search(
            r"(?:EPS|每股收益|每股公允价值|每股价值).{0,120}?(?:股本|share)",
            decision_text,
            re.I | re.S,
        )
    )
    for line in decision_text.splitlines():
        lowered_line = line.lower()
        if not (
            ("净利润" in line or "parent net profit" in lowered_line)
            and re.search(r"\d+(?:\.\d+)?\s*(?:x|倍)\s*(?:PE|P/E|市盈率)?", line, re.I)
            and re.search(r"(?:¥|￥)\s*\d|\d+\s*(?:元|cny)", line, re.I)
        ):
            continue
        if not global_share_count_bridge and not any(
            token in lowered_line
            for token in ("eps", "每股收益", "股本", "share count")
        ):
            issues.append(
                DecisionDepthIssue(
                    "profit_pe_per_share_bridge",
                    "error",
                    "a per-share price is derived from aggregate net profit and PE without an explicit diluted share-count/EPS bridge",
                )
            )
            break
    return issues


def _period_semantic_issues(decision_text: str) -> list[DecisionDepthIssue]:
    issues: list[DecisionDepthIssue] = []
    q2_windows = re.findall(
        r"(?:Q2|二季度|第二季度).{0,100}",
        decision_text,
        re.I | re.S,
    )
    h1_windows = re.findall(
        r"(?:H1|上半年|半年报|中报).{0,100}",
        decision_text,
        re.I | re.S,
    )

    def _profit_thresholds(windows: list[str]) -> set[str]:
        values: set[str] = set()
        for window in windows:
            if not any(token in window.lower() for token in ("profit", "净利润", "归母")):
                continue
            for low, high in re.findall(
                r"(\d+(?:\.\d+)?)\s*(?:-|–|—|至|~)\s*(\d+(?:\.\d+)?)\s*亿",
                window,
            ):
                values.add(f"range:{low}-{high}")
            for value in re.findall(
                r"(?:[<>≥≤]|低于|高于|超过|超|不低于|不高于)\s*(?:¥|￥)?\s*(\d+(?:\.\d+)?)\s*亿",
                window,
            ):
                values.add(f"threshold:{value}")
        return values

    reused = _profit_thresholds(q2_windows) & _profit_thresholds(h1_windows)
    if reused:
        issues.append(
            DecisionDepthIssue(
                "q2_h1_period_semantics",
                "error",
                "the same profit threshold is assigned to Q2 single-quarter and H1 cumulative periods; reconcile H1 = Q1 + Q2 and relabel every trigger",
            )
        )

    preview_claimed = re.search(
        r"(?:上半年|H1|半年度).{0,16}(?:业绩预告|earnings preview)",
        decision_text,
        re.I,
    )
    if preview_claimed and not any(
        token in decision_text.lower()
        for token in ("official calendar", "官方日历", "公告日期", "披露规则", "scheduled disclosure")
    ):
        issues.append(
            DecisionDepthIssue(
                "unverified_disclosure_calendar",
                "warning",
                "memo assumes a half-year earnings preview without citing an official calendar, announcement, or applicable disclosure rule",
            )
        )
    return issues


def _scenario_arithmetic_issues(decision_text: str) -> list[DecisionDepthIssue]:
    issues: list[DecisionDepthIssue] = []
    for header, rows in _markdown_tables(decision_text):
        lowered = [cell.lower() for cell in header]
        scenario_idx = next((i for i, cell in enumerate(lowered) if "scenario" in cell or "情景" in cell), None)
        target_idx = next((i for i, cell in enumerate(lowered) if "target" in cell or "目标价" in cell or "fair value" in cell), None)
        probability_idx = next((i for i, cell in enumerate(lowered) if "probability" in cell or "概率" in cell), None)
        contribution_idx = next((i for i, cell in enumerate(lowered) if "contribution" in cell or "贡献" in cell), None)
        if scenario_idx is None or target_idx is None or probability_idx is None:
            continue
        scenario_rows: list[tuple[float, float, float | None]] = []
        expected_value: float | None = None
        for row in rows:
            if len(row) <= max(scenario_idx, target_idx, probability_idx):
                continue
            label = row[scenario_idx].lower()
            if any(token in label for token in ("expected", "期望", "加权")):
                expected_value = _first_number(row[target_idx])
                continue
            if not any(token in label for token in ("bull", "base", "bear", "牛", "基准", "中性", "熊")):
                continue
            target = _first_number(row[target_idx])
            probability = _first_number(row[probability_idx])
            contribution = (
                _first_number(row[contribution_idx])
                if contribution_idx is not None and len(row) > contribution_idx
                else None
            )
            if target is not None and probability is not None:
                scenario_rows.append((target, probability, contribution))
        if len(scenario_rows) < 3:
            continue
        probability_sum = sum(row[1] for row in scenario_rows)
        if abs(probability_sum - 100.0) > 0.6:
            issues.append(DecisionDepthIssue("scenario_probability_math", "error", f"scenario probabilities sum to {probability_sum:.2f}%, not 100%"))
        weighted_value = sum(target * probability / 100.0 for target, probability, _ in scenario_rows)
        if expected_value is not None and abs(weighted_value - expected_value) > max(1.0, expected_value * 0.01):
            issues.append(DecisionDepthIssue("scenario_weighted_value_math", "error", f"reported expected value {expected_value:.2f} does not reconcile to probability-weighted scenario value {weighted_value:.2f}"))
        for target, probability, contribution in scenario_rows:
            expected_contribution = target * probability / 100.0
            if contribution is not None and abs(expected_contribution - contribution) > max(1.0, expected_contribution * 0.02):
                issues.append(DecisionDepthIssue("scenario_contribution_math", "error", f"scenario contribution {contribution:.2f} does not reconcile to target {target:.2f} x probability {probability:.2f}%"))
                break
    return issues


def _forecast_and_valuation_range_issues(
    decision_text: str,
    *,
    earnings_model_context: str = "",
) -> list[DecisionDepthIssue]:
    """Recalculate common range formulas instead of trusting LLM arithmetic."""
    issues: list[DecisionDepthIssue] = []

    annual_revenue_match = re.search(
        r"\|\s*latest annual\s*\|\s*FY\s*\|\s*\d{8}\s*\|\s*([\d,]+(?:\.\d+)?)\s*\|",
        earnings_model_context,
        re.I,
    )
    forecast_revenue_match = re.search(
        r"(?:营业收入|revenue).{0,30}?20\d{2}E\s*[:：]?\s*"
        r"([\d,]+(?:\.\d+)?)\s*[-–—~至]\s*([\d,]+(?:\.\d+)?)\s*亿",
        decision_text,
        re.I | re.S,
    )
    stated_growth_match = re.search(
        r"20\d{2}E.{0,20}?(?:收入增速|revenue growth).{0,12}?"
        r"(?:约|about)?\s*(\d+(?:\.\d+)?)\s*[-–—~至]\s*(\d+(?:\.\d+)?)%",
        decision_text,
        re.I | re.S,
    )
    if annual_revenue_match and forecast_revenue_match and stated_growth_match:
        annual_cny_100m = (
            float(annual_revenue_match.group(1).replace(",", ""))
            / 100_000_000.0
        )
        forecast_low, forecast_high = sorted(
            (
                float(forecast_revenue_match.group(1).replace(",", "")),
                float(forecast_revenue_match.group(2).replace(",", "")),
            )
        )
        calculated_low = (forecast_low / annual_cny_100m - 1.0) * 100.0
        calculated_high = (forecast_high / annual_cny_100m - 1.0) * 100.0
        stated_low, stated_high = sorted(
            (float(stated_growth_match.group(1)), float(stated_growth_match.group(2)))
        )
        if (
            abs(calculated_low - stated_low) > 1.0
            or abs(calculated_high - stated_high) > 1.0
        ):
            issues.append(
                DecisionDepthIssue(
                    "forecast_growth_arithmetic",
                    "error",
                    f"stated revenue growth {stated_low:.1f}-{stated_high:.1f}% does not reconcile to latest annual revenue and forecast range; calculated {calculated_low:.1f}-{calculated_high:.1f}%",
                )
            )

    for match in re.finditer(
        r"(?:收入|revenue)\s*([\d,]+(?:\.\d+)?)\s*亿\s*[×x*]\s*"
        r"(\d+(?:\.\d+)?)\s*(?:x|倍)?\s*PS\s*[×x*]\s*"
        r"(\d+(?:\.\d+)?)%[^=→\n]{0,40}(?:=|→)\s*(?:约|about)?\s*"
        r"([\d,]+(?:\.\d+)?)\s*[-–—~至]\s*([\d,]+(?:\.\d+)?)\s*亿",
        decision_text,
        re.I,
    ):
        revenue = float(match.group(1).replace(",", ""))
        multiple = float(match.group(2))
        probability = float(match.group(3)) / 100.0
        stated_low, stated_high = sorted(
            (
                float(match.group(4).replace(",", "")),
                float(match.group(5).replace(",", "")),
            )
        )
        calculated = revenue * multiple * probability
        if calculated < stated_low * 0.97 or calculated > stated_high * 1.03:
            issues.append(
                DecisionDepthIssue(
                    "option_value_arithmetic",
                    "error",
                    f"option value formula implies {calculated:.1f} CNY 100m, outside the stated {stated_low:.1f}-{stated_high:.1f} range",
                )
            )
            break

    weighted_match = re.search(
        r"(\d+(?:\.\d+)?)%\s*[×x*]\s*\((\d+(?:\.\d+)?)\s*[-–—~至]\s*(\d+(?:\.\d+)?)\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)%\s*[×x*]\s*\((\d+(?:\.\d+)?)\s*[-–—~至]\s*(\d+(?:\.\d+)?)\)\s*\+\s*"
        r"(\d+(?:\.\d+)?)%\s*[×x*]\s*\((\d+(?:\.\d+)?)\s*[-–—~至]\s*(\d+(?:\.\d+)?)\)"
        r".{0,30}?(?:→|=)\s*(?:约)?\s*(\d+(?:\.\d+)?)\s*[-–—~至]\s*(\d+(?:\.\d+)?)",
        decision_text,
        re.I | re.S,
    )
    if weighted_match:
        values = [float(weighted_match.group(i)) for i in range(1, 12)]
        calculated_low = (
            values[0] * values[1] + values[3] * values[4] + values[6] * values[7]
        ) / 100.0
        calculated_high = (
            values[0] * values[2] + values[3] * values[5] + values[6] * values[8]
        ) / 100.0
        stated_low, stated_high = sorted((values[9], values[10]))
        if (
            abs(calculated_low - stated_low) > 0.6
            or abs(calculated_high - stated_high) > 0.6
        ):
            issues.append(
                DecisionDepthIssue(
                    "scenario_weighted_range_math",
                    "error",
                    f"probability-weighted range should be {calculated_low:.1f}-{calculated_high:.1f}, not {stated_low:.1f}-{stated_high:.1f}",
                )
            )

    closure_text = _heading_text(decision_text, "Valuation Closure")
    current_match = re.search(
        r"(?:当前股价|current price)\s*(\d+(?:\.\d+)?)",
        closure_text,
        re.I,
    )
    fair_match = re.search(
        r"(?:公允价值|fair value)\s*(\d+(?:\.\d+)?)\s*[-–—~至]\s*(\d+(?:\.\d+)?)",
        closure_text,
        re.I,
    )
    stated_return_match = re.search(
        r"(?:存在|预期|expected).{0,20}?(?:约)?\s*(\d+(?:\.\d+)?)\s*[-–—~至]\s*(\d+(?:\.\d+)?)%",
        closure_text,
        re.I | re.S,
    )
    if current_match and fair_match and stated_return_match:
        current = float(current_match.group(1))
        fair_low, fair_high = sorted(
            (float(fair_match.group(1)), float(fair_match.group(2)))
        )
        stated_low, stated_high = sorted(
            (
                float(stated_return_match.group(1)),
                float(stated_return_match.group(2)),
            )
        )
        calculated_low = (fair_low / current - 1.0) * 100.0
        calculated_high = (fair_high / current - 1.0) * 100.0
        if (
            abs(calculated_low - stated_low) > 1.0
            or abs(calculated_high - stated_high) > 1.0
        ):
            issues.append(
                DecisionDepthIssue(
                    "expected_return_range_math",
                    "error",
                    f"fair-value range implies {calculated_low:.1f}-{calculated_high:.1f}% return, not {stated_low:.1f}-{stated_high:.1f}%",
                )
            )
    return issues


def audit_decision_integrity(
    decision_text: str,
    *,
    earnings_model_context: str = "",
) -> list[DecisionDepthIssue]:
    """Audit final-output arithmetic, period semantics, and information lineage.

    This deliberately does not judge or rewrite the rating.  It checks whether
    the generated memo obeys the model and evidence contracts supplied to it.
    """
    issues = _scenario_arithmetic_issues(decision_text)
    issues.extend(
        _forecast_and_valuation_range_issues(
            decision_text,
            earnings_model_context=earnings_model_context,
        )
    )
    issues.extend(_eps_profit_consistency_issues(decision_text))
    issues.extend(_valuation_bridge_issues(decision_text))
    issues.extend(_period_semantic_issues(decision_text))
    lowered = decision_text.lower()

    forecast_years = sorted(set(re.findall(r"20\d{2}E", decision_text, re.I)))
    forecast_triggered = any(token in lowered for token in ("forward forecast", "盈利预测", "预测桥", "earnings bridge"))
    rich_company_memo = len(decision_text) >= 2200
    if (forecast_triggered or rich_company_memo) and len(forecast_years) < 3:
        issues.append(DecisionDepthIssue("three_year_forecast_completion", "error", "final memo invokes a forecast bridge but does not provide three distinct forward years"))
    if len(forecast_years) >= 3:
        if sum(token in lowered for token in ("nim", "net interest", "credit cost", "cet1", "净息差", "信用成本", "资本充足")) >= 2:
            forecast_groups = (
                ("nim", "net interest", "净息差", "净利息收入"),
                ("fee income", "手续费", "非息收入"),
                ("credit cost", "信用成本", "拨备"),
                ("net profit", "归母净利润", "eps"),
                ("roe", "净资产收益率"),
                ("cet1", "资本充足", "npl", "不良率"),
            )
        elif sum(token in lowered for token in ("nbv", "embedded value", "solvency", "cor", "新业务价值", "内含价值", "偿付能力")) >= 2:
            forecast_groups = (
                ("premium", "ape", "保费"),
                ("nbv", "新业务价值"),
                ("embedded value", "内含价值", "csm"),
                ("investment spread", "投资收益率", "负债成本"),
                ("cor", "综合成本率"),
                ("net profit", "opat", "归母净利润", "eps"),
                ("solvency", "偿付能力"),
            )
        elif sum(token in lowered for token in ("brokerage", "investment banking", "proprietary trading", "资本充足率", "经纪业务", "投行业务", "自营")) >= 2:
            forecast_groups = (
                ("brokerage", "经纪业务"),
                ("investment banking", "投行业务"),
                ("asset management", "资管业务"),
                ("trading income", "proprietary", "自营", "投资收益"),
                ("net profit", "归母净利润", "eps"),
                ("roe", "资本充足率", "净资本"),
            )
        elif sum(token in lowered for token in ("occupancy", "distributable cash", "noi", "出租率", "可供分配金额")) >= 2:
            forecast_groups = (
                ("occupancy", "出租率"),
                ("rent", "租金"),
                ("noi", "净营业收入"),
                ("distributable cash", "可供分配"),
                ("payout", "分派率"),
            )
        else:
            forecast_groups = (
                ("revenue", "营业收入", "收入"),
                ("net profit", "归母净利润", "净利润"),
                ("eps", "每股收益"),
                ("ocf", "经营现金流"),
                ("capex", "资本开支"),
                ("fcf", "自由现金流"),
            )
        forecast_metric_hits = sum(
            1
            for tokens in forecast_groups
            if any(token in lowered for token in tokens)
        )
        required_hits = max(4, len(forecast_groups) - 1)
        if forecast_metric_hits < required_hits:
            issues.append(
                DecisionDepthIssue(
                    "three_year_forecast_reconciliation",
                    "error",
                    "three forward years are named but the memo does not reconcile enough of revenue, parent profit, EPS, OCF, capex, and FCF",
                )
            )
    if "to be estimated" in lowered or "待估算" in decision_text:
        issues.append(DecisionDepthIssue("forecast_placeholder", "error", "final memo still contains unfilled forecast placeholders"))

    if re.search(r"(?:Q2|二季报|第二季度|半年报|中报).{0,35}(?:10月|october)", decision_text, re.I | re.S):
        issues.append(DecisionDepthIssue("financial_calendar_period", "error", "Q2/half-year disclosure is linked to October; verify whether the memo has confused the half-year and Q3 reporting windows"))

    yoy_claims = re.findall(r"(?:同比|YoY).{0,25}?([-+]?\d+(?:\.\d+)?)\s*(?:pp|个百分点)", decision_text, re.I)
    if yoy_claims and earnings_model_context:
        gross_margin_rows = [line for line in earnings_model_context.splitlines() if "Gross margin" in line]
        for claim in yoy_claims:
            if any(claim in line and "YoY:" not in line for line in gross_margin_rows):
                issues.append(DecisionDepthIssue("period_comparator_lineage", "error", f"final memo labels {claim}pp as YoY, but the matching earnings-model row does not carry a same-period YoY comparison basis"))
                break

    kp_claimed = any(token in lowered for token in ("knowledge planet", "知识星球", "private/proxy", "私域"))
    kp_ids = sorted(set(re.findall(r"KPE\d+", decision_text, re.I)))
    if kp_claimed and not kp_ids:
        issues.append(DecisionDepthIssue("alternative_intelligence_lineage", "warning", "Knowledge Planet affects the memo but no KPE evidence id is cited"))
    if kp_ids and not re.search(
        r"(?:before\s*(?:->|→)\s*after|调整前.{0,30}调整后|拒绝|rejected|unchanged|"
        r"不采纳|不改变|未改变|无模型影响|无模型变化|保持不变)",
        decision_text,
        re.I | re.S,
    ):
        issues.append(DecisionDepthIssue("alternative_intelligence_transmission", "error", "KPE evidence is cited without probability before/after values, an explicit unchanged result, or a rejection reason"))

    for match in re.finditer(
        r"(?:current price|当前价格|现价)\s*[:：]?\s*(\d+(?:\.\d+)?).{0,45}?"
        r"(?:EV|expected value|期望价值|目标价)\s*[:：]?\s*(\d+(?:\.\d+)?).{0,30}?"
        r"(折价|discount|upside|上涨空间)\s*(?:约)?\s*(\d+(?:\.\d+)?)%",
        decision_text,
        re.I | re.S,
    ):
        current, value, label, stated = float(match.group(1)), float(match.group(2)), match.group(3).lower(), float(match.group(4))
        calculated = ((value - current) / value * 100.0) if label in {"折价", "discount"} else ((value - current) / current * 100.0)
        if abs(calculated - stated) > 0.6:
            issues.append(DecisionDepthIssue("upside_discount_math", "error", f"stated {label} {stated:.2f}% does not reconcile to current price {current:.2f} and value {value:.2f}; calculated {calculated:.2f}%"))
            break

    causal_flow_claims = ("forced selling", "institutional rotation", "止损盘", "情绪宣泄", "资金出逃", "机构调仓")
    if any(claim in lowered for claim in causal_flow_claims) and not any(
        evidence in lowered
        for evidence in ("fund flow", "northbound", "block trade", "holder change", "etf flow", "资金流", "北向", "大宗交易", "持有人变化")
    ):
        issues.append(DecisionDepthIssue("price_move_causal_attribution", "warning", "memo makes a causal flow/sentiment attribution without flow, block-trade, holder-change, or equivalent evidence"))

    return issues


def audit_context_alignment(report_dir: str | Path) -> list[DecisionDepthIssue]:
    """Flag industry/playbook mismatches across saved contexts."""
    context_dir = Path(report_dir) / "0_context"
    if not context_dir.exists():
        return []

    combined = "\n".join(
        read_text_fallback(path)
        for path in (
            context_dir / "company_business_model.md",
            context_dir / "industry_kpi.md",
            context_dir / "forecast_model.md",
            context_dir / "supply_chain_comparison.md",
            context_dir / "commodity_context.md",
        )
        if path.exists()
    )
    if _term_hits(combined, _WIND_EQUIPMENT_TERMS) >= 2 and _term_hits(combined, _LITHIUM_BATTERY_ROUTE_TERMS) >= 2:
        return [
            DecisionDepthIssue(
                "industry_playbook_alignment",
                "error",
                "saved contexts mix wind/offshore equipment evidence with lithium-battery playbook, supply-chain, or forecast drivers",
            )
        ]
    if _term_hits(combined, _TELECOM_OPERATOR_TERMS) >= 2 and _term_hits(combined, _LITHIUM_BATTERY_ROUTE_TERMS) >= 2:
        return [
            DecisionDepthIssue(
                "industry_playbook_alignment",
                "error",
                "saved contexts mix telecom-operator evidence with lithium-battery/metals playbook, supply-chain, or forecast drivers",
            )
        ]
    return []


def audit_structured_research_usage(
    report_dir: str | Path,
    decision_text: str,
) -> list[DecisionDepthIssue]:
    path = Path(report_dir) / "0_context" / "structured_research.json"
    if not path.exists():
        return []
    try:
        bundle = json.loads(read_text_fallback(path))
    except Exception as exc:
        return [
            DecisionDepthIssue(
                "structured_research_bundle",
                "error",
                f"structured_research.json is not readable JSON: {exc}",
            )
        ]

    issues: list[DecisionDepthIssue] = []
    invalid_eps_rows = [
        row
        for row in bundle.get("semantic_metrics", [])
        if "eps_profit_share_count_conflict" in row.get("control_flags", [])
    ]
    if invalid_eps_rows:
        row = invalid_eps_rows[0]
        issues.append(
            DecisionDepthIssue(
                "eps_source_sanity",
                "error",
                "reported EPS was rejected as a likely PDF table-column shift: "
                f"period={row.get('period')}, rejected={row.get('rejected_value')}, "
                f"control={row.get('value_text')}",
            )
        )
    preprocessing_mode = str(bundle.get("preprocessing_mode", ""))
    preprocessing_notes = " ".join(
        str(note) for note in bundle.get("preprocessing_notes", [])
    )
    if (
        preprocessing_mode == "deterministic_only"
        and "semantic llm failed" in preprocessing_notes.lower()
    ):
        issues.append(
            DecisionDepthIssue(
                "semantic_preprocessing_failure",
                "error",
                "semantic LLM preprocessing failed; the memo may use deterministic filing-row fallback but cannot claim full semantic segment/conflict/KPE processing",
            )
        )

    underwriting_packet = bundle.get("underwriting_packet", {})
    if not underwriting_packet:
        issues.append(
            DecisionDepthIssue(
                "shared_underwriting_packet",
                "error",
                "shared company underwriting packet is missing; agents may have produced independent narratives instead of one reconciled operating model",
            )
        )
    else:
        readiness = str(underwriting_packet.get("research_readiness", "")).lower()
        readiness_reasons = [
            str(item) for item in underwriting_packet.get("readiness_reasons", [])
        ]
        share_conflict = next(
            (
                reason
                for reason in readiness_reasons
                if reason.startswith(
                    "Reported total_share and market-cap/close share counts conflict"
                )
            ),
            "",
        )
        if share_conflict:
            issues.append(
                DecisionDepthIssue(
                    "share_count_source_conflict",
                    "error",
                    share_conflict,
                )
            )
        if readiness == "blocked":
            issues.append(
                DecisionDepthIssue(
                    "underwriting_readiness",
                    "error",
                    "shared company underwriting packet is blocked: "
                    + "; ".join(
                        str(item)
                        for item in underwriting_packet.get("readiness_reasons", [])[:6]
                    ),
                )
            )
        elif readiness == "partial":
            issues.append(
                DecisionDepthIssue(
                    "underwriting_readiness",
                    "warning",
                    "shared company underwriting packet remains partial; report must disclose the incomplete model lines and cap valuation confidence",
                )
            )
        company_model = underwriting_packet.get("company_model", {})
        if not company_model.get("revenue_equation") or not company_model.get("profit_equation"):
            issues.append(
                DecisionDepthIssue(
                    "company_operating_model",
                    "error",
                    "company revenue/profit operating equations are absent from the shared underwriting packet",
                )
            )
        business_units = list(underwriting_packet.get("business_unit_map", []))
        if not business_units:
            issues.append(
                DecisionDepthIssue(
                    "company_disaggregation",
                    "warning",
                    "shared underwriting packet has no economic business-unit map beyond narrative/accounting labels",
                )
            )
        elif not any(
            str(row.get("revenue_driver_equation", "")).strip()
            or str(row.get("profit_driver_equation", "")).strip()
            for row in business_units
        ):
            issues.append(
                DecisionDepthIssue(
                    "company_disaggregation",
                    "warning",
                    "business units exist but none carries a revenue or profit driver equation",
                )
            )

        thesis_bridges = list(
            underwriting_packet.get("thesis_financial_bridges", [])
        )
        if not thesis_bridges or not any(
            str(row.get("quantification_status", ""))
            in {"quantified", "partially_quantified"}
            for row in thesis_bridges
        ):
            issues.append(
                DecisionDepthIssue(
                    "thesis_financial_bridge",
                    "warning",
                    "shared model has no decisive thesis translated into a quantified or partially quantified financial bridge",
                )
            )

        moat_claims = list(company_model.get("moat_mechanisms", []))
        moat_tests = list(underwriting_packet.get("moat_evidence_tests", []))
        if moat_claims and (
            not moat_tests
            or not any(
                str(row.get("status", "")) in {"proven", "partial"}
                for row in moat_tests
            )
        ):
            issues.append(
                DecisionDepthIssue(
                    "moat_evidence_scorecard",
                    "warning",
                    "claimed moat mechanisms remain narrative because no observable test is proven or partially proven",
                )
            )

        valuation_buckets = list(underwriting_packet.get("valuation_buckets", []))
        valuation_closure = dict(underwriting_packet.get("valuation_closure", {}))
        if (
            not valuation_buckets
            or str(valuation_closure.get("status", "")) != "closed"
            or valuation_closure.get("fair_value_per_share_cny") is None
        ):
            issues.append(
                DecisionDepthIssue(
                    "valuation_closure",
                    "warning",
                    "shared model does not close mutually exclusive valuation buckets to auditable per-share fair value",
                )
            )

        handoff_manifest = dict(underwriting_packet.get("handoff_manifest", {}))
        if not handoff_manifest.get("downstream_must_preserve"):
            issues.append(
                DecisionDepthIssue(
                    "handoff_integrity_audit",
                    "warning",
                    "shared model lacks a loss-prevention manifest for downstream agents",
                )
            )
        question_ids = [
            str(row.get("question_id", "")).strip()
            for row in underwriting_packet.get("underwriting_questions", [])
            if str(row.get("question_id", "")).strip()
        ]
        if question_ids and not any(question_id in decision_text for question_id in question_ids):
            issues.append(
                DecisionDepthIssue(
                    "underwriting_question_usage",
                    "warning",
                    "PM memo does not visibly answer any company-specific question from the shared underwriting packet",
                )
            )
        if not any(
            marker in decision_text.lower()
            for marker in (
                "shared underwriting model change audit",
                "shared model change",
                "model change ledger",
                "承保模型变更",
                "模型变更台账",
            )
        ):
            issues.append(
                DecisionDepthIssue(
                    "shared_model_change_audit",
                    "error",
                    "PM memo does not reconcile the fundamental/bull/bear changes to the shared underwriting model",
                )
            )

    segments = [
        str(row.get("segment", "")).strip()
        for row in bundle.get("segments", [])
        if str(row.get("segment", "")).strip()
        and str(row.get("segment", "")).strip().lower()
        not in {"consolidated", "group", "company", "合并", "公司整体"}
    ]
    if not segments and bundle.get("deterministic_evidence"):
        issues.append(
            DecisionDepthIssue(
                "structured_segment_extraction",
                "error",
                "structured preprocessing produced no segment rows despite having deterministic evidence; segment prosperity cannot be considered complete",
            )
        )
    if len(segments) >= 2:
        segment_rows = [
            row
            for row in bundle.get("segments", [])
            if str(row.get("segment", "")).strip()
            and str(row.get("segment", "")).strip().lower()
            not in {"consolidated", "group", "company", "合并", "公司整体"}
        ]
        material_rows = [
            row
            for row in segment_rows
            if _safe_float(row.get("revenue_weight_pct")) >= 10.0
            or _safe_float(row.get("revenue_reported_value")) > 0.0
            or _safe_float(row.get("revenue_cny_mn")) > 0.0
        ]
        # When semantic preprocessing returns only unquantified rows, preserve
        # the primary company segment without treating every unproven optional
        # business as material merely because its weight is unknown.
        if not material_rows and segment_rows:
            material_rows = segment_rows[:1]
        missing_segments = [
            str(row.get("segment", "")).strip()
            for row in material_rows
            if not _segment_is_mentioned(row, decision_text)
        ]
        if missing_segments:
            issues.append(
                DecisionDepthIssue(
                    "structured_segment_usage",
                    "error",
                    "PM memo omits material structured segment(s): "
                    + ", ".join(missing_segments[:8]),
                )
            )

        growth_rows = [
            row
            for row in bundle.get("segments", [])
            if row.get("revenue_growth_pct") is not None
            and str(row.get("segment", "")).strip()
        ]
        if growth_rows:
            fastest = max(
                growth_rows,
                key=lambda row: float(row.get("revenue_growth_pct") or 0.0),
            )
            for row in growth_rows:
                segment = str(row.get("segment", "")).strip()
                if segment == str(fastest.get("segment", "")).strip():
                    continue
                if re.search(
                    re.escape(segment) + r".{0,28}(?:增长最快|fastest[- ]growing)",
                    decision_text,
                    re.I | re.S,
                ):
                    issues.append(
                        DecisionDepthIssue(
                            "segment_growth_rank_consistency",
                            "error",
                            f"memo calls {segment} the fastest-growing segment, but structured same-period filing rows show {fastest.get('segment')} has the higher revenue growth rate",
                        )
                    )
                    break

    actionable_kpe = [
        row
        for row in bundle.get("kpe_impacts", [])
        if row.get("quantification_status") in {"quantified", "probability_only"}
        and row.get("grounding_status") == "grounded_quote"
    ]
    missing_kpe = [
        str(row.get("evidence_id"))
        for row in actionable_kpe
        if str(row.get("evidence_id")) not in decision_text
    ]
    if missing_kpe:
        issues.append(
            DecisionDepthIssue(
                "structured_kpe_usage",
                "warning",
                "grounded quantified KPE rows are absent from the PM memo: "
                + ", ".join(missing_kpe[:8]),
            )
        )

    incomplete_kpe_outcomes = [
        str(row.get("evidence_id", ""))
        for row in bundle.get("kpe_impacts", [])
        if str(row.get("evidence_id", "")).strip()
        and not str(row.get("decision_outcome", "")).strip()
    ]
    if incomplete_kpe_outcomes:
        issues.append(
            DecisionDepthIssue(
                "structured_kpe_decision_outcome",
                "error",
                "KPE rows lack an explicit quantified/probability/unchanged/rejected outcome: "
                + ", ".join(incomplete_kpe_outcomes[:8]),
            )
        )

    unresolved_conflicts = list(bundle.get("conflicts", []))
    if unresolved_conflicts and not any(
        token in decision_text.lower()
        for token in ("conflict", "contradiction", "口径冲突", "数据冲突", "矛盾")
    ):
        issues.append(
            DecisionDepthIssue(
                "structured_conflict_usage",
                "warning",
                "structured preprocessing found source conflicts, but the PM memo does not reconcile or disclose them",
            )
        )
    return issues


def audit_report_depth(report_dir: str | Path) -> pd.DataFrame:
    """Audit the final portfolio decision for depth and deterministic integrity."""
    report_path = Path(report_dir)
    decision_path = report_path / "5_portfolio" / "decision.md"
    if not decision_path.exists():
        raise FileNotFoundError(f"Missing portfolio decision: {decision_path}")
    decision_text = read_text_fallback(decision_path)
    appendix_path = report_path / "5_portfolio" / "research_appendix.md"
    depth_text = decision_text
    if appendix_path.exists():
        depth_text += "\n\n" + read_text_fallback(appendix_path)
    earnings_path = report_path / "0_context" / "earnings_model.md"
    earnings_context = read_text_fallback(earnings_path) if earnings_path.exists() else ""
    issues = audit_decision_depth(depth_text)
    issues.extend(
        audit_decision_integrity(
            decision_text,
            earnings_model_context=earnings_context,
        )
    )
    issues.extend(audit_structured_research_usage(report_dir, decision_text))
    issues.extend(audit_context_alignment(report_dir))
    issues.extend(audit_handoff_numeric_consistency(report_dir))
    public_h2_count = sum(
        1 for line in decision_text.splitlines() if line.startswith("## ")
    )
    if public_h2_count != 8:
        issues.append(
            DecisionDepthIssue(
                "pm_format_contract",
                "warning",
                "public PM renderer should emit exactly eight fixed H2 sections; "
                f"got sections={public_h2_count}. Re-render from the validated PM payload.",
            )
        )
    generation_status_path = report_path / "5_portfolio" / "generation_status.json"
    if generation_status_path.exists():
        try:
            generation_status = json.loads(
                read_text_fallback(generation_status_path)
            )
            if str(generation_status.get("mode", "")).lower() not in {
                "structured",
                "schema_prompt_structured",
                "schema_repaired_fallback",
            }:
                error = str(generation_status.get("structured_error", "")).strip()
                detail = f"; structured error: {error[:240]}" if error else ""
                issues.append(
                    DecisionDepthIssue(
                        "pm_structured_generation",
                        "error",
                        "Portfolio Manager used free-text fallback; formal publication requires schema-valid SellSidePMDecision output"
                        + detail,
                    )
                )
        except (json.JSONDecodeError, OSError, TypeError) as exc:
            issues.append(
                DecisionDepthIssue(
                    "pm_structured_generation",
                    "error",
                    f"Portfolio Manager generation status is unreadable: {exc}",
                )
            )
    research_manager_status_path = report_path / "2_research" / "generation_status.json"
    if research_manager_status_path.exists():
        try:
            manager_status = json.loads(read_text_fallback(research_manager_status_path))
            if str(manager_status.get("mode", "")).lower() not in {
                "structured",
                "schema_prompt_structured",
                "schema_repaired_fallback",
            }:
                error = str(manager_status.get("structured_error", "")).strip()
                detail = f"; structured error: {error[:240]}" if error else ""
                issues.append(
                    DecisionDepthIssue(
                        "research_manager_structured_generation",
                        "error",
                        "Research Manager used free-text fallback; the canonical debated model handoff is not schema-valid"
                        + detail,
                    )
                )
        except (json.JSONDecodeError, OSError, TypeError) as exc:
            issues.append(
                DecisionDepthIssue(
                    "research_manager_structured_generation",
                    "error",
                    f"Research Manager generation status is unreadable: {exc}",
                )
            )
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


def render_post_generation_audit(report_dir: str | Path) -> str:
    """Render a sidecar QA report after the PM memo has been generated."""
    rows = audit_report_depth(report_dir)
    lines = [
        "# Post-Generation Research Integrity Audit",
        "",
        "- Scope: deterministic checks on final-report depth, arithmetic, period semantics, evidence lineage, and context alignment.",
        "- This audit does not change or independently assign the investment rating.",
        "",
    ]
    if rows.empty:
        lines.extend(["## Verdict", "", "- PASS: no deterministic issue detected."])
        return "\n".join(lines)
    errors = int((rows["severity"] == "error").sum())
    warnings = int((rows["severity"] == "warning").sum())
    blocking_errors = sum(
        _is_publication_blocker(str(row["section"]), str(row["severity"]))
        for _, row in rows.iterrows()
    )
    verdict = "BLOCKED" if blocking_errors else "REVIEW"
    lines.extend(
        [
            "## Verdict",
            "",
            f"- {verdict}: blocking_errors={blocking_errors}, research_errors={errors}, warnings={warnings}.",
            "- Missing, partial or unavailable source data is neutral for investment direction; disclose it with a retrieval or verification task.",
            "- Deterministic contradictions, failed structured generation, blocked company underwriting, and missing mandatory deep-research sections block formal publication.",
            "",
            "## Findings",
            "",
            "| section | severity | publication impact | issue |",
            "| --- | --- | --- | --- |",
        ]
    )
    for _, row in rows.iterrows():
        issue = str(row["issue"]).replace("|", "/")
        impact = (
            "blocks formal publication"
            if _is_publication_blocker(str(row["section"]), str(row["severity"]))
            else "review only"
        )
        lines.append(
            f"| {row['section']} | {row['severity']} | {impact} | {issue} |"
        )
    return "\n".join(lines)


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
