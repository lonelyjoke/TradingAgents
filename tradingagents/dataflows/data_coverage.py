"""Summarize precomputed data coverage for downstream decision agents."""

from __future__ import annotations

from dataclasses import dataclass
import re

from .research_evidence import (
    build_evidence_record,
    classify_evidence_text,
    line_is_usable_evidence,
)


@dataclass(frozen=True)
class ContextCoverage:
    name: str
    status: str
    note: str


@dataclass(frozen=True)
class KeyFact:
    fact_id: str
    source_module: str
    status: str
    role: str
    evidence: str
    source_tier: str = ""
    evidence_type: str = ""
    period: str = ""


@dataclass(frozen=True)
class CoreVariableGate:
    profile: str
    variable: str
    status: str
    evidence: str


FAILURE_PATTERNS = (
    "context unavailable",
    "# financial-report intelligence unavailable",
    "# thematic catalyst cross-check unavailable",
    "# commodity/product-price context unavailable",
    "# price-move attribution context unavailable",
    "# relative strength / index linkage context unavailable",
    "# shipping cycle context unavailable",
    "# same-industry peer comparison unavailable",
    "# supply-chain position comparison unavailable",
    "# earnings-model context unavailable",
    "# market-expectation context unavailable",
    "# price-eps-pe decomposition unavailable",
    "# management/capital-allocation context unavailable",
    "# shareholder-structure context unavailable",
    "# investor-interaction context unavailable",
    "# policy-planning context unavailable",
    "# baijiu verification context unavailable",
    "# compute-leasing verification layer unavailable",
    "# dividend defensive verification layer unavailable",
    "# building-materials verification context unavailable",
    "# consumer-staples verification context unavailable",
    "# ai optical-module context unavailable",
    "# biopharma verification context unavailable",
    "# software verification context unavailable",
    "# insurance verification context unavailable",
    "# medical-device verification context unavailable",
    "# metals-mining verification context unavailable",
    "# knowledge planet intelligence context unavailable",
    "# knowledge planet daily report unavailable",
    "# industry cycle scan unavailable",
    "# company business model primer unavailable",
    "# industry kpi checklist unavailable",
    "# forward forecast model scaffold unavailable",
    "# sell-side depth and key-number audit unavailable",
    "lookup unavailable",
    "unavailable\n\n- reason",
    "unavailable; do not state freight index",
    "extraction status: financial-report text extraction unavailable",
    "narrative filing text extraction unavailable",
    "financial-report text extraction unavailable",
    "no readable report text",
    "no relevant web fact rows",
    "search provider returned no relevant web fact rows",
    "no commodity mapping found",
    "cycle evidence insufficient",
    "no clean business-model",
    "no compact kpi evidence",
    "no compact earnings/model evidence",
    "weak or incomplete modules:",
    "| failed |",
    "api error",
    "traceback",
    "不可用",
    "无法获取",
    "无法加载",
    "提取失败",
    "调用失败",
    "请指定正确的接口名",
    "无可读",
    "失败",
)

NOT_APPLICABLE_PATTERNS = (
    "status: not_applicable",
    "no shipping mapping found",
    "no mapped public shipping index",
    "no curated consumer-staples mapping",
    "no curated optical-module mapping",
    "no curated building-materials mapping",
    "no curated software mapping",
    "no curated compute-leasing mapping",
    "no curated metals/mining mapping",
    "no curated or inferred supply-chain map is available",
    "not applicable: telecom operators do not have a primary commodity/product-price spread driver",
)

SUCCESS_HINTS = (
    "##",
    "| --- |",
    "reachable",
    "coverage_grade",
    "Earnings Snapshots",
)

FALSE_FAILURE_PATTERNS = (
    "weak or incomplete modules: none detected",
)

FACT_SOURCE_PRIORITY = (
    "financial_report_intelligence",
    "earnings_model",
    "market_expectation",
    "price_eps_pe_decomposition",
    "commodity_product_price",
    "industry_kpi_checklist",
    "peer_comparison",
    "management_capital_allocation",
    "investor_interaction",
    "knowledge_planet",
)

KEY_FACT_TERMS = (
    ("revenue", "core valuation input"),
    ("operating revenue", "core valuation input"),
    ("net profit", "core valuation input"),
    ("gross margin", "core margin input"),
    ("operating cash flow", "cash-quality input"),
    ("ocf", "cash-quality input"),
    ("capex", "cash-quality input"),
    ("cash", "balance-sheet input"),
    ("contract liabilities", "demand-visibility input"),
    ("pe", "valuation input"),
    ("pb", "valuation input"),
    ("roe", "quality/valuation input"),
    ("eps", "valuation input"),
    ("dividend", "shareholder-return input"),
    ("nim", "bank-native input"),
    ("npl", "bank-native input"),
    ("cet1", "bank-native input"),
    ("nbv", "insurance-native input"),
    ("csm", "insurance-native input"),
    ("cor", "insurance-native input"),
    ("hog price", "hog-cycle input"),
    ("piglet", "hog-cycle input"),
    ("sow", "hog-cycle input"),
    ("complete cost", "hog-cycle input"),
    ("copper", "commodity input"),
    ("shfe", "commodity input"),
    ("aisc", "mining-native input"),
    ("reserve", "mining-native input"),
    ("grade", "mining-native input"),
)

PROFILE_RULES = (
    {
        "profile": "automotive components",
        "triggers": (
            "playbook: automotive components / platform supplier",
            "customer / vehicle exposure",
            "content per vehicle",
            "annual price-down",
        ),
        "variables": (
            ("Customer/model volume bridge", ("customer vehicle sales", "vehicle volume", "车型", "客户定点")),
            ("Content per vehicle / ASP", ("content per vehicle", "单车配套", "asp", "annual price-down")),
            ("Segment revenue / gross margin", ("product revenue", "segment revenue", "gross margin", "分产品")),
            ("Capacity utilization / SOP", ("utilization", "sop", "ppap", "产能利用率")),
            ("Working capital / FCF", ("receivables", "inventory", "ocf", "fcf", "capex")),
            ("Incremental ROIC", ("incremental roic", "invested capital", "固定资产", "在建工程")),
            ("Second-curve order-to-revenue", ("order-to-revenue", "customer nomination", "第二曲线", "机器人")),
        ),
    },
    {
        "profile": "battery / energy storage",
        "triggers": (
            "playbook: battery / energy-storage chain",
            "power battery revenue",
            "gwh shipments x asp",
            "动力电池",
            "储能电池",
        ),
        "variables": (
            ("Power-battery shipments / share", ("power-battery", "power battery", "gwh", "动力电池")),
            ("Energy-storage shipments / orders", ("energy-storage", "storage battery", "储能", "storage pipeline")),
            ("Battery ASP / pass-through", ("battery asp", "realized asp", "price pass-through", "pricing clauses")),
            ("Lithium/material cost", ("lithium carbonate", "material cost", "碳酸锂", "原材料")),
            ("Capacity utilization", ("capacity utilization", "utilization", "产能利用率")),
            ("Segment gross margin", ("segment gross margin", "gross margin", "毛利率")),
            ("OCF / FCF / capex", ("ocf", "fcf", "capex", "operating cash flow")),
        ),
    },
    {
        "profile": "bank",
        "triggers": (
            "reading profile: banking",
            "nim",
            "cet1",
            "npl",
            "deposit",
            "provision coverage",
            "bank kpi",
        ),
        "variables": (
            ("NIM / net interest spread", ("nim", "net interest", "interest spread")),
            ("Asset quality", ("npl", "non-performing", "provision coverage", "overdue")),
            ("Capital adequacy", ("cet1", "capital adequacy", "tier 1")),
            ("ROE / PB valuation bridge", ("roe", "pb", "cost of equity")),
            ("Dividend coverage", ("dividend", "payout", "capital constraint")),
        ),
    },
    {
        "profile": "insurance",
        "triggers": (
            "insurance",
            "nbv",
            "embedded value",
            "csm",
            "solvency",
            "combined ratio",
        ),
        "variables": (
            ("NBV growth and margin", ("nbv", "new business value", "nbv margin")),
            ("EV / CSM bridge", ("embedded value", "csm", "contractual service margin")),
            ("Solvency and capital", ("solvency", "capital adequacy")),
            ("P&C COR", ("cor", "combined ratio")),
            ("Dividend coverage", ("dividend", "payout", "solvency")),
        ),
    },
    {
        "profile": "hog breeding",
        "triggers": (
            "hog",
            "piglet",
            "sow",
            "breeding",
            "livestock",
            "complete cost",
        ),
        "variables": (
            ("Hog ASP / futures curve", ("hog price", "dce", "lh", "asp")),
            ("Piglet and sow supply", ("piglet", "sow", "breeding sow")),
            ("Complete breeding cost", ("complete cost", "cost per kg", "breeding cost")),
            ("Monthly sales volume/price", ("monthly sales", "sales volume", "realized price")),
            ("OCF / leverage survival", ("ocf", "operating cash flow", "leverage", "cash")),
            ("PB / NAV stress floor", ("pb", "nav", "book value")),
        ),
    },
    {
        "profile": "consumer staples",
        "triggers": (
            "consumer-staples",
            "beverage",
            "food",
            "distributor",
            "channel inventory",
            "sell-through",
        ),
        "variables": (
            ("Sell-through / channel inventory", ("sell-through", "channel inventory", "distributor")),
            ("Price system / ASP", ("asp", "terminal price", "wholesale price")),
            ("Contract liabilities", ("contract liabilities", "advance receipts")),
            ("Gross margin and raw materials", ("gross margin", "raw material", "promotion")),
            ("Food safety / quality risk", ("food safety", "quality risk")),
        ),
    },
    {
        "profile": "metals/mining",
        "triggers": (
            "metals-mining",
            "mining",
            "copper",
            "shfe",
            "aisc",
            "reserve",
            "grade",
        ),
        "variables": (
            ("Metal price proxy", ("shfe", "copper", "aluminum", "gold")),
            ("Reserve / resource quality", ("reserve", "resource", "grade")),
            ("Equity output / volume", ("equity output", "production", "output")),
            ("AISC / unit cost", ("aisc", "unit cost", "cash cost")),
            ("NAV / SOTP", ("nav", "sotp", "resource value")),
            ("Capex / project ramp", ("capex", "project ramp", "construction")),
        ),
    },
)


def _first_relevant_line(text: str) -> str:
    for raw in text.splitlines():
        line = raw.strip(" -")
        if not line or line.startswith("| ---"):
            continue
        lower = line.lower()
        if any(pattern in lower for pattern in FAILURE_PATTERNS):
            return line
    for raw in text.splitlines():
        line = raw.strip()
        if line:
            return line
    return ""


def _clean_failure_text(text: str) -> str:
    lower = text.lower()
    for pattern in FALSE_FAILURE_PATTERNS:
        lower = lower.replace(pattern, "")
    return lower


def classify_context_coverage(name: str, text: str) -> ContextCoverage:
    """Classify whether one precomputed research context is usable."""
    cleaned = (text or "").strip()
    if not cleaned:
        return ContextCoverage(name, "missing", "context is empty")

    lower = _clean_failure_text(cleaned)
    if any(pattern in lower for pattern in NOT_APPLICABLE_PATTERNS):
        return ContextCoverage(name, "not_applicable", _first_relevant_line(cleaned))

    has_failure = any(pattern in lower for pattern in FAILURE_PATTERNS)
    has_success_hint = any(hint.lower() in lower for hint in SUCCESS_HINTS)

    if has_failure:
        status = "partial" if has_success_hint and len(cleaned) > 500 else "failed"
    else:
        status = "ready" if len(cleaned) > 120 else "thin"

    note = _first_relevant_line(cleaned)
    note = re.sub(r"\s+", " ", note)
    if len(note) > 180:
        note = note[:177] + "..."
    return ContextCoverage(name, status, note)


def _truncate_cell(text: str, limit: int = 160) -> str:
    normalized = re.sub(r"\s+", " ", text).strip().replace("|", "/")
    return normalized[: limit - 3] + "..." if len(normalized) > limit else normalized


def _line_has_number(line: str) -> bool:
    return bool(re.search(r"[-+]?\d+(?:\.\d+)?\s*(?:%|x|倍|亿|万|元|kg|吨|bps)?", line, re.I))


def _find_role(line: str) -> str:
    lower = line.lower()
    for term, role in KEY_FACT_TERMS:
        if term in lower:
            return role
    return "source-backed input"


def _parse_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _knowledge_planet_evidence_fact(line: str) -> tuple[str, str] | None:
    cells = _parse_markdown_row(line)
    if not cells or not re.match(r"^KPE\d+", cells[0], re.I):
        return None
    if len(cells) >= 8:
        role = cells[5] or "private/proxy evidence"
        evidence = f"{cells[0]} {cells[6]} verification: {cells[7]}"
        return role, _truncate_cell(evidence, 190)
    return "private/proxy evidence", _truncate_cell(line, 190)


def _extract_key_facts(
    contexts: dict[str, str],
    coverage_by_name: dict[str, ContextCoverage],
    max_facts: int = 12,
) -> list[KeyFact]:
    facts: list[KeyFact] = []
    fact_no = 1
    prioritized_names = [
        name for name in FACT_SOURCE_PRIORITY if name in contexts
    ] + [
        name for name in contexts if name not in FACT_SOURCE_PRIORITY
    ]
    seen: set[str] = set()
    for name in prioritized_names:
        coverage = coverage_by_name.get(name)
        if not coverage or coverage.status in {"failed", "missing", "not_applicable"}:
            continue
        for raw in contexts.get(name, "").splitlines():
            line = raw.strip(" -")
            kp_fact = (
                _knowledge_planet_evidence_fact(line)
                if name == "knowledge_planet"
                else None
            )
            if kp_fact:
                role, evidence = kp_fact
                if evidence.lower() in seen:
                    continue
                seen.add(evidence.lower())
                facts.append(
                    KeyFact(
                        fact_id=f"KF{fact_no:02d}",
                        source_module=name,
                        status="private_proxy",
                        role=role,
                        evidence=evidence,
                        source_tier="private_alternative",
                        evidence_type="private_proxy",
                        period="see KPE date",
                    )
                )
                fact_no += 1
                if len(facts) >= max_facts:
                    return facts
                continue
            if (
                len(line) < 18
                or line.startswith("| ---")
                or not _line_has_number(line)
            ):
                continue
            if not line_is_usable_evidence(name, line):
                continue
            lower = line.lower()
            if not any(term in lower for term, _ in KEY_FACT_TERMS):
                continue
            evidence = _truncate_cell(line)
            if evidence.lower() in seen:
                continue
            seen.add(evidence.lower())
            semantic = build_evidence_record(f"KF{fact_no:02d}", name, line)
            facts.append(
                KeyFact(
                    fact_id=f"KF{fact_no:02d}",
                    source_module=name,
                    status=semantic.status,
                    role=_find_role(line),
                    evidence=evidence,
                    source_tier=semantic.source_tier,
                    evidence_type=semantic.evidence_type,
                    period=semantic.period,
                )
            )
            fact_no += 1
            if len(facts) >= max_facts:
                return facts
    return facts


def _matching_line(
    source_module: str,
    text: str,
    terms: tuple[str, ...],
) -> tuple[str, str]:
    lowered_terms = tuple(term.lower() for term in terms)
    first_gap = ""
    for raw in text.splitlines():
        line = raw.strip(" -")
        lower = line.lower()
        if not any(term in lower for term in lowered_terms):
            continue
        _, status = classify_evidence_text(source_module, line)
        if status in {"reported", "calculated", "estimated", "private_proxy"}:
            return _truncate_cell(line), status
        if status == "missing" and not first_gap:
            first_gap = _truncate_cell(line)
    return first_gap, "missing"


def _detect_profiles(contexts: dict[str, str]) -> list[dict[str, object]]:
    kpi_text = "\n".join(
        value
        for name, value in contexts.items()
        if "industry_kpi" in name or "forecast_model" in name
    ).lower()
    explicit_markers = (
        ("automotive components / platform supplier", "automotive components"),
        ("battery / energy-storage chain", "battery / energy storage"),
        ("telecom operator / high-dividend soe", "telecom operator"),
        ("insurance / integrated financial services", "insurance"),
        ("hog breeding / live-hog cycle", "hog breeding"),
        ("consumer staples /", "consumer staples"),
        ("nonferrous metals /", "metals/mining"),
        ("lithium / metals cycle", "metals/mining"),
    )
    for marker, profile_name in explicit_markers:
        if marker in kpi_text:
            matched = [rule for rule in PROFILE_RULES if rule["profile"] == profile_name]
            if matched:
                return matched

    blob = "\n".join(contexts.values())
    lower = blob.lower()
    profiles = [
        rule for rule in PROFILE_RULES if any(term in lower for term in rule["triggers"])
    ]
    if not profiles:
        return []
    return profiles[:2]


def _build_core_variable_gates(
    contexts: dict[str, str],
    coverage_by_name: dict[str, ContextCoverage],
) -> list[CoreVariableGate]:
    gates: list[CoreVariableGate] = []
    for rule in _detect_profiles(contexts):
        profile = str(rule["profile"])
        for variable, terms in rule["variables"]:  # type: ignore[index]
            evidence = ""
            evidence_status = "missing"
            for name, text in contexts.items():
                line, semantic_status = _matching_line(name, text, terms)
                if not line:
                    continue
                coverage = coverage_by_name.get(name)
                evidence = f"{name}: {line}"
                if semantic_status == "missing":
                    continue
                if name == "knowledge_planet":
                    if evidence_status != "ready":
                        evidence_status = "private_proxy"
                    continue
                if semantic_status in {"reported", "calculated"} and coverage and coverage.status == "ready":
                    evidence_status = "ready"
                    break
                if semantic_status == "estimated" and evidence_status == "missing":
                    evidence_status = "estimated"
                    continue
                if coverage and coverage.status in {"thin", "partial"}:
                    evidence_status = "partial"
                else:
                    evidence_status = "partial"
            gates.append(
                CoreVariableGate(
                    profile=profile,
                    variable=str(variable),
                    status=evidence_status,
                    evidence=evidence or "No explicit source-backed evidence found.",
                )
            )
    return gates


def build_data_coverage_context(contexts: dict[str, str]) -> str:
    """Render a compact data coverage audit for manager prompts and saved reports."""
    rows = [
        classify_context_coverage(name, value)
        for name, value in contexts.items()
    ]
    if not rows:
        return "# Data Coverage Audit\n\nNo precomputed context modules were supplied."

    lines = [
        "# Data Coverage Audit",
        "",
        "| module | status | note |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        note = row.note.replace("|", "/")
        lines.append(f"| {row.name} | {row.status} | {note} |")

    coverage_by_name = {row.name: row for row in rows}
    key_facts = _extract_key_facts(contexts, coverage_by_name)
    if key_facts:
        lines.extend(
            [
                "",
                "## Key Facts Ledger",
                "",
                "| fact_id | source_module | status | decision_role | evidence | source_tier | evidence_type | source_period |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for fact in key_facts:
            lines.append(
                f"| {fact.fact_id} | {fact.source_module} | {fact.status} | "
                f"{fact.role} | {fact.evidence} | {fact.source_tier} | "
                f"{fact.evidence_type} | {fact.period} |"
            )

    gates = _build_core_variable_gates(contexts, coverage_by_name)
    if gates:
        lines.extend(
            [
                "",
                "## Core Variable Gates",
                "",
                "| profile | core_variable | status | evidence |",
                "| --- | --- | --- | --- |",
            ]
        )
        for gate in gates:
            lines.append(
                f"| {gate.profile} | {gate.variable} | {gate.status} | "
                f"{gate.evidence.replace('|', '/')} |"
            )

    failed = [row.name for row in rows if row.status in {"failed", "missing"}]
    partial = [row.name for row in rows if row.status == "partial"]
    private_proxy_rows = any(fact.status == "private_proxy" for fact in key_facts) or any(
        gate.status == "private_proxy" for gate in gates
    )
    if failed or partial or key_facts or gates:
        lines.extend(
            [
                "",
                "## Required Manager Treatment",
            ]
        )
        if failed or partial:
            lines.extend(
                [
                    "- Treat failed, missing or partial modules as neutral non-evidence. A retrieval failure is neither bullish nor bearish.",
                    "- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.",
                    "- If a failed or partial module touches the core bet, name it as a research gap and add a dated retrieval or verification task; do not mechanically alter rating, sizing or publication status.",
                    "- Keep the rating and expected-value conclusion based only on available verified evidence. Put unavailable fields in Evidence Gaps and the Verification Calendar without converting absence into a negative signal.",
                ]
            )
        if key_facts:
            lines.append(
                "- Use Key Facts Ledger fact_ids as the only source for decisive numeric claims. If a debate participant cites a conflicting number, correct it before changing rating or sizing."
            )
        if gates:
            lines.append(
                "- Use Core Variable Gates as coverage and retrieval guardrails, not rating gates. Missing thesis-critical variables must be disclosed and scheduled for verification, but must not automatically prevent Buy/Overweight, force Hold, or support Underweight/Sell."
            )
        if private_proxy_rows:
            lines.append(
                "- Treat `private_proxy` rows from Knowledge Planet as alternative-intelligence clues only. They may adjust probabilities, timing, sizing, or verification tasks, but they cannot serve as filing-grade facts unless cross-checked by announcements, Tushare/financial data, reputable news, or market price/volume evidence."
            )
    return "\n".join(lines)
