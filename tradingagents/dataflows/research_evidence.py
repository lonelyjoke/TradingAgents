"""Shared evidence semantics for the research pipeline.

The research system receives a large amount of markdown from filings, market
data, private research, checklists, and model scaffolds.  A keyword appearing
in that markdown is not by itself evidence.  This module gives downstream
components one conservative vocabulary for distinguishing facts, estimates,
private proxies, questions, instructions, formulas, and explicit gaps.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Mapping


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    source_module: str
    source_tier: str
    evidence_type: str
    status: str
    model_variable: str
    period: str
    text: str

    @property
    def usable(self) -> bool:
        return self.status in {"reported", "calculated", "estimated", "private_proxy"}


_MISSING_MARKERS = (
    "missing",
    "unavailable",
    "not disclosed",
    "not found",
    "to be estimated",
    "待验证",
    "待估算",
    "未披露",
    "缺失",
    "无法获取",
    "不可用",
    "research gap",
    "model gap",
)

_QUESTION_MARKERS = (
    "?",
    "？",
    "what would",
    "whether ",
    "can the ",
    "does the ",
    "如何",
    "是否",
    "哪些",
    "什么会",
)

_INSTRUCTION_MARKERS = (
    "must ",
    "should ",
    "require ",
    "required ",
    "do not ",
    "analyst instruction",
    "manager instruction",
    "check with",
    "cross-check",
    "track ",
    "verify ",
    "reconcile ",
    "需要",
    "必须",
    "应当",
    "不得",
    "跟踪",
    "验证",
    "检查",
)

_FORMULA_MARKERS = (
    " x ",
    " × ",
    " = ",
    "formula",
    "bridge",
    "volume x",
    "revenue x",
    "收入 =",
    "毛利 =",
)

_ESTIMATE_MARKERS = (
    "estimate",
    "estimated",
    "forecast",
    "assumption",
    "scenario",
    "run-rate",
    "预测",
    "假设",
    "情景",
)

_CALCULATED_MARKERS = (
    "calculated",
    "derived",
    "implied",
    "percentile",
    "annualized",
    "年化",
    "计算",
    "推导",
    "隐含",
    "分位",
)

_PERIOD_RE = re.compile(
    r"(?:(?<!\d)(?:20\d{6}|20\d{2}(?:[-/.]\d{1,2}(?:[-/.]\d{1,2})?)?|20\d{2}[EQH][1-4]?)(?!\d)|"
    r"\bQ[1-4]\b|\bH[12]\b|\bFY\b|\bTTM\b|本报告期|上年同期|年度|季度|半年)",
    re.I,
)

_NUMBER_RE = re.compile(
    r"(?<![A-Za-z])[-+]?\d[\d,]*(?:\.\d+)?\s*(?:%|pp|pct|bps|x|倍|亿|万|元|"
    r"GWh|MWh|GW|MW|吨|kg|股|亿元|万元|千元)?",
    re.I,
)

_VARIABLE_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("segment_volume", ("shipment", "sales volume", "output", "gwh", "装机", "出货", "销量", "产量")),
    ("market_share", ("market share", "global share", "市占率", "市场份额")),
    ("asp_or_price", ("asp", "realized price", "product price", "售价", "价格", "吨价")),
    ("unit_cost", ("unit cost", "cash cost", "complete cost", "aisc", "材料成本", "单位成本", "完全成本", "养殖成本")),
    ("utilization_or_backlog", ("utilization", "backlog", "order", "capacity", "利用率", "订单", "排产", "产能")),
    ("segment_margin", ("gross margin", "net margin", "nim", "cor", "毛利率", "净利率", "息差", "综合成本率")),
    ("revenue", ("revenue", "sales", "营业收入", "营收")),
    ("operating_expense", ("expense ratio", "r&d", "sg&a", "费用率", "研发费用", "销售费用", "管理费用")),
    ("profit_or_eps", ("net profit", "operating profit", "eps", "归母", "净利润", "营业利润", "每股收益")),
    ("cash_conversion", ("ocf", "fcf", "cash flow", "经营现金流", "自由现金流", "现金转化")),
    ("capex_or_roic", ("capex", "construction in progress", "roic", "资本开支", "在建工程", "投入资本回报")),
    ("balance_sheet", ("inventory", "receivable", "contract liabilities", "debt", "存货", "应收", "合同负债", "负债")),
    ("valuation", (" pe", "pb", "ev/", "target price", "估值", "目标价", "市盈率", "市净率")),
    ("scenario_probability", ("probability", "bull", "base", "bear", "概率", "牛市", "基准", "熊市")),
)


def source_tier(source_module: str) -> str:
    lowered = source_module.lower()
    if "knowledge_planet" in lowered:
        return "private_alternative"
    if any(token in lowered for token in ("filing", "financial_report", "earnings_model")):
        return "primary_or_structured_filing"
    if any(token in lowered for token in ("market_expectation", "price", "tushare", "commodity")):
        return "structured_market_data"
    if any(token in lowered for token in ("peer", "industry", "policy", "web_fact")):
        return "secondary_or_derived_research"
    if any(token in lowered for token in ("forecast", "quality", "thesis", "coverage")):
        return "framework_or_control"
    return "research_context"


def infer_model_variable(text: str) -> str:
    lowered = f" {text.lower()} "
    for variable, terms in _VARIABLE_RULES:
        if any(term.lower() in lowered for term in terms):
            return variable
    return "unmapped"


def _period(text: str) -> str:
    matches = _PERIOD_RE.findall(text)
    return ", ".join(dict.fromkeys(match.strip() for match in matches[:3])) or "unspecified"


def classify_evidence_text(source_module: str, text: str) -> tuple[str, str]:
    """Return ``(evidence_type, status)`` for a single candidate line."""
    cleaned = re.sub(r"\s+", " ", text or "").strip()
    lowered = cleaned.lower()
    if not cleaned or cleaned.startswith("#") or set(cleaned.replace("|", "").strip()) <= {"-", ":"}:
        return "formatting", "ignore"
    if any(marker in lowered for marker in _MISSING_MARKERS):
        return "gap", "missing"
    if any(marker in lowered for marker in _QUESTION_MARKERS) and not _NUMBER_RE.search(cleaned):
        return "question", "non_evidence"
    if any(marker in lowered for marker in _INSTRUCTION_MARKERS) and not _NUMBER_RE.search(cleaned):
        return "instruction", "non_evidence"
    if any(marker in lowered for marker in _FORMULA_MARKERS) and not _NUMBER_RE.search(cleaned):
        return "formula", "non_evidence"
    if re.match(r"^\|\s*KPE\d+\s*\|", cleaned, re.I) or "knowledge_planet" in source_module.lower():
        if _NUMBER_RE.search(cleaned) or re.match(r"^\|\s*KPE\d+", cleaned, re.I):
            return "private_proxy", "private_proxy"
    if not _NUMBER_RE.search(cleaned):
        return "narrative", "non_evidence"
    if any(marker in lowered for marker in _ESTIMATE_MARKERS) or re.search(r"20\d{2}E", cleaned, re.I):
        return "model_estimate", "estimated"
    if any(marker in lowered for marker in _CALCULATED_MARKERS):
        return "calculation", "calculated"
    return "reported_fact", "reported"


def build_evidence_record(
    evidence_id: str,
    source_module: str,
    text: str,
) -> EvidenceRecord:
    evidence_type, status = classify_evidence_text(source_module, text)
    return EvidenceRecord(
        evidence_id=evidence_id,
        source_module=source_module,
        source_tier=source_tier(source_module),
        evidence_type=evidence_type,
        status=status,
        model_variable=infer_model_variable(text),
        period=_period(text),
        text=re.sub(r"\s+", " ", text.strip()).replace("|", "/")[:260],
    )


def extract_evidence_records(
    contexts: Mapping[str, str],
    *,
    max_records: int = 40,
) -> list[EvidenceRecord]:
    records: list[EvidenceRecord] = []
    seen: set[tuple[str, str]] = set()
    per_source_limit = max(4, max_records // max(len(contexts), 1))
    for source_module, context in contexts.items():
        source_count = 0
        for raw in (context or "").splitlines():
            cleaned = raw.strip(" -")
            if len(cleaned) < 8:
                continue
            record = build_evidence_record(
                f"EV{len(records) + 1:03d}",
                source_module,
                cleaned,
            )
            if record.status in {"ignore", "non_evidence"}:
                continue
            key = (record.source_module, record.text.lower())
            if key in seen:
                continue
            seen.add(key)
            records.append(record)
            source_count += 1
            if len(records) >= max_records:
                return records
            if source_count >= per_source_limit:
                break
    return records


def line_is_usable_evidence(source_module: str, text: str) -> bool:
    _, status = classify_evidence_text(source_module, text)
    return status in {"reported", "calculated", "estimated", "private_proxy"}
