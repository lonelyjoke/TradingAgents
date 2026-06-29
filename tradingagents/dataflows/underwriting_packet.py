"""Shared company-underwriting model for deep A-share research.

The packet is deliberately rating-free.  It turns verified evidence into a
common operating model that the fundamental analyst, bull/bear researchers,
research manager and PM must all use.  This prevents each agent from writing
an independent narrative with incompatible segment, forecast and valuation
assumptions.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from typing import Any, Literal, Mapping

from pydantic import BaseModel, Field


Readiness = Literal["ready", "partial", "blocked"]


class CompanyOperatingModel(BaseModel):
    model_profile: Literal[
        "corporate",
        "bank",
        "insurance",
        "securities",
        "reit",
        "other",
    ] = "corporate"
    business_archetype: str = ""
    value_proposition_and_customers: str = ""
    revenue_equation: str = ""
    profit_equation: str = ""
    cash_flow_equation: str = ""
    capital_intensity_and_reinvestment: str = ""
    diluted_share_count_mn: float | None = None
    share_count_period: str = ""
    share_count_evidence_id: str = ""
    moat_mechanisms: list[str] = Field(default_factory=list)
    moat_to_financial_transmission: list[str] = Field(default_factory=list)
    structural_risks: list[str] = Field(default_factory=list)
    key_unknowns: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)


class SegmentUnderwritingModel(BaseModel):
    segment: str
    products_or_services: str = ""
    customers_and_channel: str = ""
    revenue_weight_pct: float | None = None
    profit_weight_pct: float | None = None
    base_period: str = "unspecified"
    base_revenue_value: float | None = None
    base_revenue_unit: str = ""
    base_revenue_growth_pct: float | None = None
    base_margin_pct: float | None = None
    base_margin_change_pp: float | None = None
    demand_and_order_drivers: list[str] = Field(default_factory=list)
    industry_supply_and_capacity: str = ""
    volume_share_utilization: str = ""
    price_asp_take_rate: str = ""
    unit_cost_and_input_prices: str = ""
    margin_and_operating_leverage: str = ""
    working_capital_and_cash_conversion: str = ""
    prosperity_level: str = "evidence_limited"
    marginal_direction: str = "unknown"
    causal_analysis: str = ""
    valuation_treatment: str = "evidence_limited"
    strongest_counterevidence: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    missing_inputs: list[str] = Field(default_factory=list)
    next_verification: str = ""


class UnderwritingQuestion(BaseModel):
    question_id: str
    question: str
    why_it_matters: str
    current_answer: str = "unresolved"
    bull_evidence: list[str] = Field(default_factory=list)
    bear_evidence: list[str] = Field(default_factory=list)
    decisive_model_variables: list[str] = Field(default_factory=list)
    affected_financial_lines: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    missing_evidence: list[str] = Field(default_factory=list)
    next_verification: str = ""


class ForecastLine(BaseModel):
    segment: str = "consolidated"
    metric: str
    unit: str = ""
    base_period: str = ""
    base_value: float | None = None
    year_1_value: float | None = None
    year_2_value: float | None = None
    year_3_value: float | None = None
    formula: str = ""
    assumption_status: str = "missing"
    evidence_ids: list[str] = Field(default_factory=list)
    key_sensitivity: str = ""
    missing_inputs: list[str] = Field(default_factory=list)


class ScenarioUnderwriting(BaseModel):
    scenario: Literal["bull", "base", "bear"]
    probability_pct: float | None = None
    operating_assumptions: list[str] = Field(default_factory=list)
    parent_net_profit_cny_mn: float | None = None
    eps_cny: float | None = None
    fcf_cny_mn: float | None = None
    valuation_method: str = ""
    valuation_multiple: float | None = None
    fair_value_per_share: float | None = None
    evidence_ids: list[str] = Field(default_factory=list)
    falsification: str = ""
    missing_inputs: list[str] = Field(default_factory=list)


class ModelChangeRule(BaseModel):
    evidence_id: str
    affected_segment: str = "consolidated"
    affected_variable: str = "unmapped"
    old_assumption: str = "missing"
    new_assumption: str = "unchanged"
    financial_transmission: str = "none until quantified"
    probability_before_after: str = "unchanged/not assigned"
    disposition: str = "watch"
    verification_gate: str = ""


class CompanyUnderwritingPacket(BaseModel):
    schema_version: int = 1
    symbol: str
    as_of_date: str
    forecast_years: list[str]
    research_readiness: Readiness = "partial"
    readiness_reasons: list[str] = Field(default_factory=list)
    company_model: CompanyOperatingModel = Field(default_factory=CompanyOperatingModel)
    segment_models: list[SegmentUnderwritingModel] = Field(default_factory=list)
    underwriting_questions: list[UnderwritingQuestion] = Field(default_factory=list)
    forecast_lines: list[ForecastLine] = Field(default_factory=list)
    scenarios: list[ScenarioUnderwriting] = Field(default_factory=list)
    evidence_change_rules: list[ModelChangeRule] = Field(default_factory=list)
    reconciliation_checks: list[str] = Field(default_factory=list)
    analyst_instructions: list[str] = Field(default_factory=list)
    preprocessing_notes: list[str] = Field(default_factory=list)


def _forecast_years(as_of_date: str) -> list[str]:
    try:
        year = datetime.fromisoformat(str(as_of_date)[:10]).year
    except ValueError:
        year = datetime.now().year
    return [f"{year + offset}E" for offset in range(3)]


def _compact_text(text: str, *, max_chars: int) -> str:
    if len(text or "") <= max_chars:
        return text or ""
    important = re.compile(
        r"(^#{1,5}\s)|revenue|profit|margin|segment|business|customer|order|"
        r"volume|shipment|asp|price|cost|capacity|utilization|cash|capex|roic|"
        r"valuation|risk|KPE|收入|利润|毛利|分部|业务|客户|订单|销量|出货|"
        r"价格|成本|产能|利用率|现金|资本开支|估值|风险|景气",
        re.I,
    )
    rows: list[str] = []
    used = 0
    for raw in (text or "").splitlines():
        line = re.sub(r"\s+", " ", raw.strip())
        if not line or not important.search(line):
            continue
        wide_segment_row = any(
            marker in line.lower()
            for marker in (
                "segment economics pack",
                "filing_segment",
                "分产品",
                "主营业务分产品",
            )
        )
        line = line[:2400] if wide_segment_row else line[:700]
        if used + len(line) > max_chars:
            break
        rows.append(line)
        used += len(line) + 1
    return "\n".join(rows)


def _source_payload(contexts: Mapping[str, str], structured: Mapping[str, Any], max_chars: int) -> dict[str, Any]:
    keys = (
        "filing_intelligence",
        "company_business_model",
        "earnings_model",
        "industry_cycle",
        "industry_kpi",
        "forecast_model",
        "market_expectation",
        "peer_comparison",
        "management_capital_allocation",
        "commodity",
        "policy",
        "investor_interaction",
        "knowledge_planet",
    )
    per_source = max(2200, max_chars // max(len(keys), 1))

    def compact_rows(rows: Any, limit: int) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for raw in list(rows or [])[:limit]:
            row = dict(raw)
            for key, value in list(row.items()):
                if isinstance(value, str) and len(value) > 520:
                    row[key] = value[:517] + "..."
                elif isinstance(value, list):
                    row[key] = value[:8]
            result.append(row)
        return result

    return {
        "structured_evidence": {
            "segments": compact_rows(structured.get("segments", []), 12),
            "semantic_metrics": compact_rows(structured.get("semantic_metrics", []), 40),
            "deterministic_evidence": compact_rows(structured.get("deterministic_evidence", []), 45),
            "conflicts": compact_rows(structured.get("conflicts", []), 16),
            "kpe_impacts": compact_rows(structured.get("kpe_impacts", []), 16),
            "preprocessing_notes": list(structured.get("preprocessing_notes", []))[:12],
        },
        "source_contexts": {
            key: _compact_text(contexts.get(key, ""), max_chars=per_source)
            for key in keys
            if contexts.get(key)
        },
    }


def _prompt(symbol: str, as_of_date: str, years: list[str], payload: Mapping[str, Any]) -> str:
    schema = json.dumps(
        CompanyUnderwritingPacket.model_json_schema(),
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return f"""You are the shared underwriting-model builder for an institutional A-share research system.

Target: {symbol}
As-of date: {as_of_date}
Forward years: {years}

Build a rating-free company underwriting packet. This is the common analytical model that every downstream analyst must challenge and update. It is not a report and must not recommend Buy/Hold/Sell.

Universal rules for all A-share industries:
1. Infer the actual business archetype, `model_profile` and material segments dynamically from filings. Copy supplied filing-backed segment names exactly where available. Never force a battery, bank, software, commodity, consumer, or other fixed template onto an unrelated company.
2. Teach how the company works: who pays, what is delivered, the revenue equation, profit equation, cash-flow equation, reinvestment needs, moat mechanisms and structural risks.
3. For every material segment complete the causal chain: demand/orders -> industry supply/capacity -> company volume/share/utilization -> price/ASP/take rate -> unit cost -> margin/operating leverage -> working capital/cash -> EPS/FCF -> valuation treatment.
4. Generate 4-6 company-specific underwriting questions, ranked by expected EPS/FCF/fair-value sensitivity. The questions are the research agenda: every downstream module must either change a model variable, change a scenario probability, or document why it is irrelevant. Avoid generic questions that could apply to any stock.
5. Build three explicit forward years with the correct model profile. For ordinary non-financial companies include material segment revenue drivers and consolidated revenue, gross/operating margin, operating profit, parent net profit, EPS, OCF, capex and FCF. For banks use earning assets, NIM/net interest income, fee income, operating cost, credit cost/provisions, parent profit, EPS, ROE, asset quality and CET1/capital; do not force manufacturing OCF/FCF. For insurers use premium/APE, NBV, EV/CSM where disclosed, investment spread, COR for P&C, OPAT/parent profit, EPS, solvency and payout; for securities firms use brokerage, investment banking, asset management, proprietary/trading income, parent profit, EPS, ROE and capital adequacy; for REITs use occupancy, rent/unit, NOI, distributable cash flow and payout. Put the unit on every numeric line. Use CNY mn for profit/cash-flow lines and million shares for diluted share count when source conversion supports it. Before using null, complete reproducible calculations from supplied facts: Tushare total_share is in 10,000 shares; share count can also be cross-checked from market cap/price or parent profit/EPS; capex can be derived from cash paid to acquire/construct long-term assets; FCF can be derived from OCF minus consistently defined capex. Label these values calculated with formula, period and evidence ids. Use null plus missing_inputs only when neither reported nor reproducibly calculated evidence supports a number; never invent precision.
6. Create bull/base/bear cases only from the same model variables. Probabilities are underwriting judgments, not facts, and must sum to 100 when all are supplied. Fair value requires a reconciled EPS/share-count or asset-value bridge.
7. Use only supplied EV/KPE evidence ids. Decisive claims without a valid id must remain unverified or missing. Do not promote rows marked unverified_quote.
8. Every KPE or alternative clue has one model outcome: numeric old->new, probability before->after, unchanged/watch, or rejected. Narrative influence without a model outcome is invalid.
9. `research_readiness=ready` only when material segments, three-year consolidated model, scenario valuation, periods/units and decisive evidence are sufficiently complete. Use `partial` for unavailable sources or incomplete cells; those gaps are neutral and non-blocking. Use `blocked` only for a deterministic contradiction, invalid unit/period, or corrupted source that makes supplied facts unsafe—not merely because data is missing.
10. Return exactly one JSON object conforming to the schema. No Markdown, rating, recommendation or commentary outside JSON.
11. Use the LLM for business-model interpretation, causal chains, counterevidence, question selection and assumption design. Numeric historical facts remain controlled by supplied structured/filing evidence. Never overwrite a reported figure with an LLM estimate. A commodity or thematic proxy may enter a causal chain only when the payload proves its economic relevance to the target's revenue or cost structure.
12. Distinguish a descriptive module from a decision-useful one. Do not promote a module into the packet unless verified evidence changes a named forecast line, scenario probability or valuation bucket, or unavailable evidence creates a dated retrieval/verification task.

JSON Schema:
{schema}

Evidence payload:
{json.dumps(payload, ensure_ascii=False)}
"""


def _json_object(text: str) -> dict[str, Any]:
    cleaned = str(text or "").strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.I).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def _response_text(response: Any) -> Any:
    content = getattr(response, "content", response)
    if isinstance(content, list):
        return "\n".join(
            str(item.get("text", ""))
            if isinstance(item, dict) and item.get("type") == "text"
            else str(item)
            if isinstance(item, str)
            else ""
            for item in content
        )
    return content


def _invoke(llm: Any, prompt: str) -> CompanyUnderwritingPacket:
    structured_error: Exception | None = None
    try:
        bound = llm.with_structured_output(CompanyUnderwritingPacket)
        result = bound.invoke(prompt)
        if isinstance(result, CompanyUnderwritingPacket):
            return result
        if result is None:
            raise ValueError("underwriting structured output returned no object")
        return CompanyUnderwritingPacket.model_validate(result)
    except Exception as exc:
        structured_error = exc
    response = llm.invoke(prompt)
    content = _response_text(response)
    if isinstance(content, Mapping):
        return CompanyUnderwritingPacket.model_validate(content)
    if not str(content or "").strip():
        raise ValueError(
            "underwriting free-text fallback returned empty content; "
            f"structured_error={structured_error}"
        )
    try:
        payload = _json_object(str(content))
    except (json.JSONDecodeError, ValueError) as parse_error:
        # Long company-underwriting objects occasionally contain a missing
        # comma or an unescaped quote even when the underlying analysis is
        # useful.  Give the LLM one constrained repair pass instead of losing
        # the entire company model and falling back to a blank skeleton.
        repair_prompt = f"""Repair the malformed JSON below.

Return exactly one valid JSON object and no Markdown or commentary. Preserve the supplied analysis and values. Do not add facts, estimates, ratings, or recommendations. The object must conform to this JSON Schema:
{json.dumps(CompanyUnderwritingPacket.model_json_schema(), ensure_ascii=False, separators=(',', ':'))}

Malformed JSON:
{str(content)[:50000]}
"""
        repaired = _response_text(llm.invoke(repair_prompt))
        try:
            payload = _json_object(str(repaired))
        except (json.JSONDecodeError, ValueError) as repair_error:
            raise ValueError(
                "underwriting JSON parse and repair failed; "
                f"initial={parse_error}; repair={repair_error}; "
                f"structured={structured_error}"
            ) from repair_error
    return CompanyUnderwritingPacket.model_validate(payload)


def _valid_evidence_ids(structured: Mapping[str, Any]) -> set[str]:
    ids = {
        str(row.get("evidence_id", "")).upper()
        for key in ("semantic_metrics", "deterministic_evidence", "kpe_impacts")
        for row in structured.get(key, [])
        if str(row.get("evidence_id", "")).strip()
    }
    return ids


def _dedup_material_segments(structured: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    signatures: set[tuple[Any, ...]] = set()
    for raw in structured.get("segments", []):
        segment = str(raw.get("segment", "")).strip()
        if not segment or segment.lower() in {"consolidated", "group", "company", "合并", "公司整体"}:
            continue
        signature = (
            raw.get("revenue_reported_value"),
            raw.get("revenue_growth_pct"),
            raw.get("gross_margin_pct"),
        )
        if signature != (None, None, None) and signature in signatures:
            continue
        signatures.add(signature)
        rows.append(dict(raw))
    return rows


def _normalize_segment_name(value: str) -> str:
    return re.sub(r"[\W_]+", "", str(value or "")).lower()


def _required_metrics_for_profile(profile: str) -> set[str]:
    profiles = {
        "corporate": {
            "revenue",
            "gross_margin",
            "operating_profit",
            "parent_net_profit",
            "eps",
            "ocf",
            "capex",
            "fcf",
        },
        "bank": {
            "earning_assets",
            "nim",
            "net_interest_income",
            "fee_income",
            "pre_provision_profit",
            "credit_cost",
            "parent_net_profit",
            "eps",
            "roe",
            "cet1",
        },
        "insurance": {
            "premium_or_ape",
            "nbv",
            "investment_spread",
            "opat",
            "parent_net_profit",
            "eps",
            "solvency",
            "dividend_payout",
        },
        "securities": {
            "brokerage_revenue",
            "investment_banking_revenue",
            "asset_management_revenue",
            "trading_investment_income",
            "parent_net_profit",
            "eps",
            "roe",
            "capital_adequacy",
        },
        "reit": {
            "occupancy",
            "rent_per_unit",
            "noi",
            "distributable_cash_flow",
            "payout",
        },
    }
    return profiles.get(profile, profiles["corporate"])


def _fallback_packet(symbol: str, as_of_date: str, structured: Mapping[str, Any], note: str) -> CompanyUnderwritingPacket:
    years = _forecast_years(as_of_date)
    segments = _dedup_material_segments(structured)
    segment_models = [
        SegmentUnderwritingModel(
            segment=str(row.get("segment", "")),
            revenue_weight_pct=row.get("revenue_weight_pct"),
            profit_weight_pct=row.get("gross_profit_or_profit_weight_pct"),
            base_period=str(row.get("period", "unspecified")),
            base_revenue_value=row.get("revenue_reported_value"),
            base_revenue_unit=str(row.get("revenue_reported_unit", "")),
            base_revenue_growth_pct=row.get("revenue_growth_pct"),
            base_margin_pct=row.get("gross_margin_pct"),
            base_margin_change_pp=row.get("gross_margin_change_pp"),
            prosperity_level=str(row.get("prosperity_level", "evidence_limited")),
            marginal_direction=str(row.get("marginal_direction", "unknown")),
            causal_analysis=(
                "Reported segment economics were recovered, but the full demand, supply, "
                "price, utilization, margin and cash causal chain requires LLM underwriting."
            ),
            strongest_counterevidence=list(row.get("counterevidence", [])),
            missing_inputs=list(row.get("missing_inputs", [])),
        )
        for row in segments
    ]
    required_lines = (
        ("consolidated", "revenue"),
        ("consolidated", "gross_margin"),
        ("consolidated", "operating_profit"),
        ("consolidated", "parent_net_profit"),
        ("consolidated", "EPS"),
        ("consolidated", "OCF"),
        ("consolidated", "capex"),
        ("consolidated", "FCF"),
    )
    forecast_lines = [
        ForecastLine(
            segment=segment,
            metric=metric,
            formula="requires company-specific operating bridge",
            missing_inputs=["LLM underwriting model unavailable"],
        )
        for segment, metric in required_lines
    ]
    changes = [
        ModelChangeRule(
            evidence_id=str(row.get("evidence_id", "")),
            affected_segment=str(row.get("segment", "consolidated")),
            affected_variable=str(row.get("variable", "unmapped")),
            disposition=str(row.get("disposition", "watch")),
            verification_gate=str(row.get("verification_gate", "")),
            new_assumption="unchanged",
            financial_transmission=str(row.get("decision_outcome", "none until quantified")),
        )
        for row in structured.get("kpe_impacts", [])
        if row.get("evidence_id")
    ]
    return CompanyUnderwritingPacket(
        symbol=symbol,
        as_of_date=str(as_of_date),
        forecast_years=years,
        research_readiness="blocked",
        readiness_reasons=["LLM company underwriting failed; only deterministic skeleton is available."],
        segment_models=segment_models,
        forecast_lines=forecast_lines,
        scenarios=[ScenarioUnderwriting(scenario=name) for name in ("bull", "base", "bear")],
        evidence_change_rules=changes,
        reconciliation_checks=[
            "Material segment revenue must reconcile to consolidated revenue.",
            "Parent profit / diluted shares must reconcile to EPS.",
            "OCF - capex must reconcile to FCF.",
            "Bull/base/bear probabilities must sum to 100 before expected value is used.",
        ],
        analyst_instructions=[
            "Do not write a final report from this fallback skeleton.",
            "Fill company-specific driver chains and three-year values before valuation or rating.",
        ],
        preprocessing_notes=[note],
    )


def _validate_packet(packet: CompanyUnderwritingPacket, structured: Mapping[str, Any]) -> CompanyUnderwritingPacket:
    valid_ids = _valid_evidence_ids(structured)
    years = packet.forecast_years
    expected_years = _forecast_years(packet.as_of_date)
    if years != expected_years:
        packet.preprocessing_notes.append(
            f"forecast years normalized from {years} to {expected_years}"
        )
        packet.forecast_years = expected_years

    for item in [packet.company_model, *packet.segment_models, *packet.underwriting_questions, *packet.forecast_lines, *packet.scenarios]:
        if not hasattr(item, "evidence_ids"):
            continue
        supplied = list(getattr(item, "evidence_ids", []))
        accepted = [value.upper() for value in supplied if value.upper() in valid_ids]
        if len(accepted) != len(supplied):
            packet.preprocessing_notes.append("unknown evidence ids removed from underwriting packet")
        setattr(item, "evidence_ids", list(dict.fromkeys(accepted)))
    if (
        packet.company_model.share_count_evidence_id
        and packet.company_model.share_count_evidence_id.upper() not in valid_ids
    ):
        packet.preprocessing_notes.append("unknown share-count evidence id removed")
        packet.company_model.share_count_evidence_id = ""

    valid_changes: list[ModelChangeRule] = []
    seen_change_ids: set[str] = set()
    for change in packet.evidence_change_rules:
        evidence_id = change.evidence_id.upper()
        if evidence_id not in valid_ids or evidence_id in seen_change_ids:
            packet.preprocessing_notes.append(
                f"invalid or duplicate model-change evidence id removed: {change.evidence_id}"
            )
            continue
        change.evidence_id = evidence_id
        valid_changes.append(change)
        seen_change_ids.add(evidence_id)
    for row in structured.get("kpe_impacts", []):
        evidence_id = str(row.get("evidence_id", "")).upper()
        if not evidence_id or evidence_id in seen_change_ids:
            continue
        valid_changes.append(
            ModelChangeRule(
                evidence_id=evidence_id,
                affected_segment=str(row.get("segment", "consolidated")),
                affected_variable=str(row.get("variable", "unmapped")),
                old_assumption=str(row.get("baseline_value", "missing")),
                new_assumption=(
                    str(row.get("revised_value"))
                    if row.get("revised_value") is not None
                    else "unchanged"
                ),
                financial_transmission=str(
                    row.get("decision_outcome", "none until quantified")
                ),
                disposition=str(row.get("disposition", "watch")),
                verification_gate=str(row.get("verification_gate", "")),
            )
        )
    packet.evidence_change_rules = valid_changes

    material_name_map = {
        _normalize_segment_name(str(row.get("segment", "")).strip()): str(
            row.get("segment", "")
        ).strip()
        for row in _dedup_material_segments(structured)
        if str(row.get("segment", "")).strip()
        and (
            row.get("revenue_weight_pct") is None
            or float(row.get("revenue_weight_pct") or 0.0) >= 5.0
        )
    }
    material_names = set(material_name_map)
    present_names = {
        _normalize_segment_name(row.segment): row.segment.strip()
        for row in packet.segment_models
    }
    for row in _dedup_material_segments(structured):
        name = str(row.get("segment", "")).strip()
        normalized_name = _normalize_segment_name(name)
        if normalized_name not in present_names:
            packet.segment_models.append(
                SegmentUnderwritingModel(
                    segment=name,
                    revenue_weight_pct=row.get("revenue_weight_pct"),
                    profit_weight_pct=row.get("gross_profit_or_profit_weight_pct"),
                    base_period=str(row.get("period", "unspecified")),
                    base_revenue_value=row.get("revenue_reported_value"),
                    base_revenue_unit=str(row.get("revenue_reported_unit", "")),
                    base_revenue_growth_pct=row.get("revenue_growth_pct"),
                    base_margin_pct=row.get("gross_margin_pct"),
                    base_margin_change_pp=row.get("gross_margin_change_pp"),
                    missing_inputs=["LLM omitted a filing-reported material segment"],
                )
            )
    if material_names - set(present_names):
        packet.research_readiness = "partial"
        packet.readiness_reasons.append("One or more filing-reported segments required deterministic restoration.")

    required_metrics = _required_metrics_for_profile(
        packet.company_model.model_profile
    )
    present_metrics = {
        re.sub(r"\s+", "_", row.metric.strip().lower())
        for row in packet.forecast_lines
        if row.segment.lower() in {"consolidated", "group", "合并", "公司整体"}
    }
    for metric in sorted(required_metrics - present_metrics):
        packet.forecast_lines.append(
            ForecastLine(
                segment="consolidated",
                metric=metric,
                formula="missing; downstream analyst must complete",
                missing_inputs=["required consolidated forecast line omitted"],
            )
        )
    if required_metrics - present_metrics:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append("Required consolidated three-year forecast lines are incomplete.")

    consolidated_rows = [
        row
        for row in packet.forecast_lines
        if row.segment.lower() in {"consolidated", "group", "合并", "公司整体"}
        and re.sub(r"\s+", "_", row.metric.strip().lower()) in required_metrics
    ]
    incomplete_forward_rows = [
        row.metric
        for row in consolidated_rows
        if any(
            value is None
            for value in (row.year_1_value, row.year_2_value, row.year_3_value)
        )
    ]
    if incomplete_forward_rows:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Three-year values remain missing for consolidated line(s): "
            + ", ".join(incomplete_forward_rows[:8])
        )
    numeric_rows_without_unit = [
        row.metric
        for row in packet.forecast_lines
        if any(
            value is not None
            for value in (row.year_1_value, row.year_2_value, row.year_3_value)
        )
        and not row.unit.strip()
    ]
    if numeric_rows_without_unit:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Forecast units are missing for line(s): "
            + ", ".join(numeric_rows_without_unit[:8])
        )

    modeled_segments = {
        _normalize_segment_name(row.segment)
        for row in packet.forecast_lines
        if row.segment.strip().lower() not in {"consolidated", "group", "合并", "公司整体"}
        and all(
            value is not None
            for value in (row.year_1_value, row.year_2_value, row.year_3_value)
        )
    }
    missing_segment_forecasts = material_names - modeled_segments
    if missing_segment_forecasts:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Material segment three-year driver lines are missing: "
            + ", ".join(
                material_name_map.get(name, name)
                for name in sorted(missing_segment_forecasts)[:8]
            )
        )

    probabilities = [row.probability_pct for row in packet.scenarios]
    if all(value is not None for value in probabilities):
        total = sum(float(value) for value in probabilities if value is not None)
        if abs(total - 100.0) > 0.6:
            packet.research_readiness = "partial"
            packet.readiness_reasons.append(f"Scenario probabilities sum to {total:.2f}%, not 100%.")
    else:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append("Bull/base/bear scenario probabilities are incomplete.")
    if len(packet.scenarios) != 3 or any(
        row.fair_value_per_share is None for row in packet.scenarios
    ):
        packet.research_readiness = "partial"
        packet.readiness_reasons.append("Bull/base/bear per-share valuation is incomplete.")

    consolidated_by_metric = {
        re.sub(r"\s+", "_", row.metric.strip().lower()): row
        for row in packet.forecast_lines
        if row.segment.lower() in {"consolidated", "group", "合并", "公司整体"}
    }
    share_count = packet.company_model.diluted_share_count_mn
    profit_row = consolidated_by_metric.get("parent_net_profit")
    eps_row = consolidated_by_metric.get("eps")
    profit_unit = str(profit_row.unit if profit_row else "").lower()
    profit_in_cny_mn = any(
        token in profit_unit
        for token in ("cny mn", "cny_mn", "rmb mn", "百万元", "百万人民币")
    )
    if share_count and share_count > 0 and profit_row and eps_row and profit_in_cny_mn:
        for attr in ("year_1_value", "year_2_value", "year_3_value"):
            profit = getattr(profit_row, attr)
            eps = getattr(eps_row, attr)
            if profit is None or eps is None or eps == 0:
                continue
            implied = profit / share_count
            if abs(implied - eps) / max(abs(eps), 0.01) > 0.05:
                packet.research_readiness = "partial"
                packet.readiness_reasons.append(
                    f"Parent-profit/EPS/share-count reconciliation fails for {attr}."
                )
    elif eps_row and any(
        value is not None
        for value in (eps_row.year_1_value, eps_row.year_2_value, eps_row.year_3_value)
    ):
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "EPS forecast lacks a validated CNY-million parent-profit / diluted-share-count bridge."
        )

    ocf_row = consolidated_by_metric.get("ocf")
    capex_row = consolidated_by_metric.get("capex")
    fcf_row = consolidated_by_metric.get("fcf")
    cash_units_match = bool(
        ocf_row
        and capex_row
        and fcf_row
        and ocf_row.unit
        and ocf_row.unit == capex_row.unit == fcf_row.unit
    )
    if ocf_row and capex_row and fcf_row and cash_units_match:
        for attr in ("year_1_value", "year_2_value", "year_3_value"):
            ocf = getattr(ocf_row, attr)
            capex = getattr(capex_row, attr)
            fcf = getattr(fcf_row, attr)
            if ocf is None or capex is None or fcf is None:
                continue
            expected_fcf = ocf - abs(capex)
            if abs(expected_fcf - fcf) > max(abs(expected_fcf) * 0.05, 1.0):
                packet.research_readiness = "partial"
                packet.readiness_reasons.append(
                    f"OCF-capex-FCF reconciliation fails for {attr}."
                )

    for scenario in packet.scenarios:
        if (
            scenario.eps_cny is not None
            and scenario.valuation_multiple is not None
            and scenario.fair_value_per_share is not None
            and any(token in scenario.valuation_method.lower() for token in ("pe", "p/e", "市盈率"))
        ):
            expected_value = scenario.eps_cny * scenario.valuation_multiple
            if abs(expected_value - scenario.fair_value_per_share) > max(
                abs(expected_value) * 0.03,
                1.0,
            ):
                packet.research_readiness = "partial"
                packet.readiness_reasons.append(
                    f"{scenario.scenario} scenario EPS x PE does not reconcile to fair value."
                )
    if not packet.company_model.revenue_equation or not packet.company_model.profit_equation:
        packet.research_readiness = "blocked"
        packet.readiness_reasons.append("Company revenue/profit operating equations are missing.")
    packet.readiness_reasons = list(dict.fromkeys(packet.readiness_reasons))
    return packet


def build_company_underwriting_packet(
    symbol: str,
    as_of_date: str,
    *,
    contexts: Mapping[str, str],
    structured_research: Mapping[str, Any],
    llm: Any = None,
    enable_llm: bool = True,
    max_prompt_chars: int = 60000,
) -> dict[str, Any]:
    if not enable_llm or llm is None:
        return _fallback_packet(
            symbol,
            as_of_date,
            structured_research,
            "LLM underwriting disabled or unavailable.",
        ).model_dump()
    try:
        payload = _source_payload(contexts, structured_research, max_prompt_chars)
        packet = _invoke(
            llm,
            _prompt(symbol, as_of_date, _forecast_years(as_of_date), payload),
        )
        packet.symbol = symbol
        packet.as_of_date = str(as_of_date)
        return _validate_packet(packet, structured_research).model_dump()
    except Exception as exc:
        return _fallback_packet(
            symbol,
            as_of_date,
            structured_research,
            f"LLM underwriting failed: {exc}",
        ).model_dump()


def compact_underwriting_packet(packet: Mapping[str, Any] | None) -> dict[str, Any]:
    """Return the decision-useful subset shared with downstream prompts."""
    if not packet:
        return {}

    def clip(value: Any, limit: int = 520) -> Any:
        if isinstance(value, str):
            return value if len(value) <= limit else value[: limit - 3] + "..."
        if isinstance(value, list):
            return [clip(item, 300) for item in value[:8]]
        return value

    company = dict(packet.get("company_model", {}))
    company = {key: clip(value) for key, value in company.items()}
    segment_keys = (
        "segment",
        "revenue_weight_pct",
        "profit_weight_pct",
        "base_period",
        "base_revenue_value",
        "base_revenue_unit",
        "base_revenue_growth_pct",
        "base_margin_pct",
        "base_margin_change_pp",
        "demand_and_order_drivers",
        "industry_supply_and_capacity",
        "volume_share_utilization",
        "price_asp_take_rate",
        "unit_cost_and_input_prices",
        "margin_and_operating_leverage",
        "working_capital_and_cash_conversion",
        "prosperity_level",
        "marginal_direction",
        "causal_analysis",
        "valuation_treatment",
        "strongest_counterevidence",
        "evidence_ids",
        "missing_inputs",
        "next_verification",
    )
    segments = [
        {key: clip(row.get(key)) for key in segment_keys if key in row}
        for row in list(packet.get("segment_models", []))[:10]
    ]
    question_keys = (
        "question_id",
        "question",
        "current_answer",
        "decisive_model_variables",
        "affected_financial_lines",
        "evidence_ids",
        "missing_evidence",
        "next_verification",
    )
    questions = [
        {key: clip(row.get(key)) for key in question_keys if key in row}
        for row in list(packet.get("underwriting_questions", []))[:8]
    ]
    return {
        "schema_version": packet.get("schema_version"),
        "symbol": packet.get("symbol"),
        "as_of_date": packet.get("as_of_date"),
        "forecast_years": packet.get("forecast_years", []),
        "research_readiness": packet.get("research_readiness"),
        "readiness_reasons": clip(packet.get("readiness_reasons", [])),
        "company_model": company,
        "segment_models": segments,
        "underwriting_questions": questions,
        "forecast_lines": list(packet.get("forecast_lines", []))[:36],
        "scenarios": list(packet.get("scenarios", []))[:3],
        "evidence_change_rules": list(packet.get("evidence_change_rules", []))[:16],
        "reconciliation_checks": clip(packet.get("reconciliation_checks", [])),
    }
