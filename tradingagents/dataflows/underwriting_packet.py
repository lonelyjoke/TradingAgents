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

from pydantic import BaseModel, Field, model_validator

from .official_guidance import parse_official_guidance_record


Readiness = Literal["ready", "partial", "blocked"]


class NullDefaultModel(BaseModel):
    """Accept provider-emitted ``null`` for fields that have safe defaults.

    Structured-output providers commonly emit JSON ``null`` for optional
    descriptive strings and arrays even when the schema advertises an empty
    string/list default.  Treating that harmless shape difference as a fatal
    company-model failure discarded otherwise complete underwriting packets.
    Required fields and fields whose declared default is ``None`` remain
    strict.
    """

    @model_validator(mode="before")
    @classmethod
    def _replace_null_with_declared_default(cls, value: Any) -> Any:
        if not isinstance(value, Mapping):
            return value
        normalized = dict(value)
        for name, field in cls.model_fields.items():
            if normalized.get(name) is not None or field.is_required():
                continue
            default = field.get_default(call_default_factory=True)
            if default is not None:
                normalized[name] = default
        return normalized


class CompanyOperatingModel(NullDefaultModel):
    model_profile: Literal[
        "corporate",
        "bank",
        "insurance",
        "securities",
        "reit",
        "other",
    ] = "corporate"
    operating_model_family: Literal[
        "volume_price_cost",
        "store_traffic_conversion_ticket",
        "users_arpu_retention",
        "project_backlog_delivery",
        "commodity_volume_price_cost",
        "financial_spread_credit",
        "insurance_value",
        "reit_occupancy_rent",
        "other",
    ] = "other"
    business_archetype: str = ""
    value_proposition_and_customers: str = ""
    revenue_equation: str = ""
    profit_equation: str = ""
    cash_flow_equation: str = ""
    capital_intensity_and_reinvestment: str = ""
    diluted_share_count_mn: float | None = None
    share_count_period: str = ""
    share_count_evidence_id: str = ""
    share_count_source_type: Literal[
        "reported_total_share",
        "registered_capital",
        "market_cap_div_close",
        "model_supplied",
        "unresolved",
    ] = "unresolved"
    share_count_formula: str = ""
    share_count_cross_checks: list[str] = Field(default_factory=list)
    moat_mechanisms: list[str] = Field(default_factory=list)
    moat_to_financial_transmission: list[str] = Field(default_factory=list)
    structural_risks: list[str] = Field(default_factory=list)
    key_unknowns: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)


class SegmentUnderwritingModel(NullDefaultModel):
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


class BusinessUnitMap(NullDefaultModel):
    """Economic unit used to understand the company, not merely an accounting label."""

    unit_id: str
    unit_name: str
    unit_type: Literal[
        "reported_segment",
        "product",
        "channel",
        "geography",
        "customer_group",
        "project_or_asset",
        "financial_business",
        "other",
    ] = "reported_segment"
    disclosure_basis: Literal["reported", "calculated", "analytical", "missing"] = "missing"
    parent_unit: str = "company"
    economic_role: str = ""
    revenue_driver_equation: str = ""
    profit_driver_equation: str = ""
    cash_and_capital_equation: str = ""
    reported_metrics: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    missing_inputs: list[str] = Field(default_factory=list)
    next_verification: str = ""


class UnderwritingQuestion(NullDefaultModel):
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


class ForecastLine(NullDefaultModel):
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


class ScenarioUnderwriting(NullDefaultModel):
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


class ModelChangeRule(NullDefaultModel):
    evidence_id: str
    affected_segment: str = "consolidated"
    affected_variable: str = "unmapped"
    old_assumption: str = "missing"
    new_assumption: str = "unchanged"
    financial_transmission: str = "none until quantified"
    probability_before_after: str = "unchanged/not assigned"
    disposition: str = "watch"
    verification_gate: str = ""


class ThesisFinancialBridge(NullDefaultModel):
    """Translate one investment claim into auditable financial consequences."""

    bridge_id: str
    thesis_or_question: str
    affected_unit: str = "consolidated"
    operating_driver: str = ""
    driver_formula: str = ""
    base_assumption: str = "missing"
    bull_assumption: str = "missing"
    bear_assumption: str = "missing"
    revenue_impact: str = "unquantified"
    profit_impact: str = "unquantified"
    eps_impact: str = "unquantified"
    fcf_or_capital_impact: str = "unquantified"
    valuation_impact: str = "unquantified"
    quantification_status: Literal["quantified", "partially_quantified", "unquantified"] = "unquantified"
    evidence_ids: list[str] = Field(default_factory=list)
    missing_inputs: list[str] = Field(default_factory=list)


class MoatEvidenceTest(NullDefaultModel):
    """Require a claimed moat to pass an observable economic test."""

    moat_mechanism: str
    observable_test: str = ""
    comparison_basis: str = ""
    evidence_result: str = "missing"
    financial_transmission: str = ""
    strongest_counterevidence: str = ""
    status: Literal["proven", "partial", "unproven", "rejected"] = "unproven"
    evidence_ids: list[str] = Field(default_factory=list)
    next_verification: str = ""


class ValuationBucket(NullDefaultModel):
    """One mutually exclusive value bucket with explicit overlap control."""

    bucket: str
    inclusion: Literal["core", "scenario", "optionality", "excluded"] = "excluded"
    valuation_method: str = ""
    metric_and_period: str = ""
    metric_value: float | None = None
    valuation_multiple: float | None = None
    ownership_pct: float | None = None
    haircut_pct: float | None = None
    equity_value_cny_mn: float | None = None
    per_share_value_cny: float | None = None
    overlap_key: str = ""
    double_counting_treatment: str = ""
    evidence_ids: list[str] = Field(default_factory=list)
    missing_inputs: list[str] = Field(default_factory=list)


class ValuationClosure(NullDefaultModel):
    current_price_cny: float | None = None
    diluted_share_count_mn: float | None = None
    core_value_per_share_cny: float | None = None
    probability_weighted_fair_value_per_share_cny: float | None = None
    option_value_per_share_cny: float | None = None
    other_adjustments_per_share_cny: float | None = None
    fair_value_per_share_cny: float | None = None
    expected_return_pct: float | None = None
    formula: str = ""
    rating_consistency_check: str = ""
    double_counting_checks: list[str] = Field(default_factory=list)
    status: Literal["closed", "partial", "not_valued"] = "not_valued"
    missing_inputs: list[str] = Field(default_factory=list)


class LLMAnalysisLayer(NullDefaultModel):
    """Where LLM judgment should improve depth beyond deterministic extraction."""

    business_question_tree: list[str] = Field(default_factory=list)
    profit_pool_priority: str = ""
    competition_and_substitution_analysis: str = ""
    qualitative_to_quantitative_bridge: str = ""
    expectation_gap_analysis: str = ""
    red_team_counterarguments: list[str] = Field(default_factory=list)
    valuation_explanation: str = ""
    final_editorial_synthesis: str = ""
    evidence_boundaries: list[str] = Field(default_factory=list)


class ModelHandoffManifest(NullDefaultModel):
    handoff_version: str = "underwriting-v2"
    source_of_truth: str = "structured_research.underwriting_packet"
    frozen_reported_facts: list[str] = Field(default_factory=list)
    analyst_estimates: list[str] = Field(default_factory=list)
    unresolved_model_cells: list[str] = Field(default_factory=list)
    downstream_must_preserve: list[str] = Field(default_factory=list)


class CompanyUnderwritingPacket(NullDefaultModel):
    schema_version: int = 2
    symbol: str
    as_of_date: str
    forecast_years: list[str]
    research_readiness: Readiness = "partial"
    readiness_reasons: list[str] = Field(default_factory=list)
    company_model: CompanyOperatingModel = Field(default_factory=CompanyOperatingModel)
    business_unit_map: list[BusinessUnitMap] = Field(default_factory=list)
    segment_models: list[SegmentUnderwritingModel] = Field(default_factory=list)
    underwriting_questions: list[UnderwritingQuestion] = Field(default_factory=list)
    forecast_lines: list[ForecastLine] = Field(default_factory=list)
    scenarios: list[ScenarioUnderwriting] = Field(default_factory=list)
    thesis_financial_bridges: list[ThesisFinancialBridge] = Field(default_factory=list)
    moat_evidence_tests: list[MoatEvidenceTest] = Field(default_factory=list)
    valuation_buckets: list[ValuationBucket] = Field(default_factory=list)
    valuation_closure: ValuationClosure = Field(default_factory=ValuationClosure)
    llm_analysis_layer: LLMAnalysisLayer = Field(default_factory=LLMAnalysisLayer)
    handoff_manifest: ModelHandoffManifest = Field(default_factory=ModelHandoffManifest)
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
1a. Do not confuse accounting disclosure segments with the economic units needed to understand the company. Build `business_unit_map` across the dimensions that actually drive economics: product, channel, geography, customer group, project/asset or financial business. Mark every unit reported/calculated/analytical/missing. An analytical unit may organize questions and forecasts, but it may not receive invented revenue, margin or value.
1b. Select exactly one `operating_model_family` from the real economics. Product/chemical/manufacturing companies normally require capacity -> utilization -> volume -> ASP -> input/unit cost -> spread/margin -> working capital -> capex/ROIC. Retail/consumer companies require traffic/store/customer count -> conversion -> ticket/ARPU -> mix -> margin. Software requires users -> paid penetration -> ARPU -> retention/churn -> delivery/cloud cost. Project companies require opening backlog + new orders - delivery = ending backlog -> acceptance -> receivables/collection. Resource companies require reserves/capacity -> output -> realized price -> cash cost/AISC -> sustaining capex. Banks, insurers and REITs use their native spread/credit, value/solvency, or occupancy/rent models. Do not call a forecast autonomous unless the selected family's decisive driver chain is represented or explicitly missing.
2. Teach how the company works: who pays, what is delivered, the revenue equation, profit equation, cash-flow equation, reinvestment needs, moat mechanisms and structural risks.
3. For every material segment complete the causal chain: demand/orders -> industry supply/capacity -> company volume/share/utilization -> price/ASP/take rate -> unit cost -> margin/operating leverage -> working capital/cash -> EPS/FCF -> valuation treatment.
4. Generate 4-6 company-specific underwriting questions, ranked by expected EPS/FCF/fair-value sensitivity. The questions are the research agenda: every downstream module must either change a model variable, change a scenario probability, or document why it is irrelevant. Avoid generic questions that could apply to any stock.
5. Build three explicit forward years with the correct model profile. For ordinary non-financial companies include material segment revenue drivers and consolidated revenue, gross/operating margin, operating profit, parent net profit, EPS, OCF, capex and FCF. For banks use earning assets, NIM/net interest income, fee income, operating cost, credit cost/provisions, parent profit, EPS, ROE, asset quality and CET1/capital; do not force manufacturing OCF/FCF. For insurers use premium/APE, NBV, EV/CSM where disclosed, investment spread, COR for P&C, OPAT/parent profit, EPS, solvency and payout; for securities firms use brokerage, investment banking, asset management, proprietary/trading income, parent profit, EPS, ROE and capital adequacy; for REITs use occupancy, rent/unit, NOI, distributable cash flow and payout. Put the unit on every numeric line. Use CNY mn for profit/cash-flow lines and million shares for diluted share count when source conversion supports it. Before using null, complete reproducible calculations from supplied facts: Tushare total_share is in 10,000 shares; share count can also be cross-checked from market cap/price or parent profit/EPS; capex can be derived from cash paid to acquire/construct long-term assets; FCF can be derived from OCF minus consistently defined capex. Seasonal annualization must be arithmetically consistent: annual run-rate = quarterly value x 4, while seasonal-share full-year estimate = quarterly value / quarterly_share; never divide an already annualized run-rate by the seasonal share. Label these values calculated with formula, period and evidence ids. Use null plus missing_inputs only when neither reported nor reproducibly calculated evidence supports a number; never invent precision.
5a. Diluted shares are controlled downstream and cannot be chosen to make a reported EPS fit. Prefer current Tushare stock_basic registered capital or daily_basic total_share and cross-check market cap / close. The pledge_stat total_share field is only a pledge-table proxy, not authoritative company shares. Treat parent-profit / EPS only as a diagnostic. If a filing-text EPS conflicts with parent profit / deterministic shares, label it a suspected PDF column shift and do not use it.
6. Create bull/base/bear cases only from the same model variables. Probabilities are underwriting judgments, not facts, and must sum to 100 when all are supplied. Fair value requires a reconciled EPS/share-count or asset-value bridge.
6a. Build 3-6 `thesis_financial_bridges` for the claims that actually decide the recommendation. Each bridge must state the operating formula and bull/base/bear assumption, then quantify or explicitly leave missing the revenue, profit, EPS, FCF/capital and valuation effect. Narrative influence without a named financial line is incomplete.
6b. Turn every claimed moat into a `moat_evidence_test`. Test scale, license, brand, switching cost, network effect, cost advantage or customer stickiness with an observable metric versus history or true peers. State counterevidence and the exact route from the moat to price/share/margin/turnover/cash/ROIC. A management claim alone is `unproven`.
6c. Build mutually exclusive `valuation_buckets`, then one `valuation_closure`. State what is core, scenario, optionality or excluded; identify overlap keys; reconcile share count, scenario probabilities, per-share conversion and current-price expected return. `probability_weighted_fair_value_per_share_cny` is the total probability-weighted value, not an incremental bucket to add again to core value. A subsidiary, acquired business or second curve already inside consolidated earnings must not be added again in SOTP unless the consolidated earnings base explicitly excludes it.
6d. When `COMMODITY_MODEL_CONTROL` rows are supplied, reverse-underwrite valuation from the commodity distribution instead of applying a commodity-price story directly to a multiple. Use the dated P20/P50/P80 range, percentile and volatility to set bear/base/bull proxy prices; bridge proxy price -> company realized price/basis/lag -> volume capped by reported capacity -> grade/product-matched input costs -> segment gross profit -> tax/minority interest -> parent profit/EPS/FCF -> normalized PE, EV/EBITDA, PB-ROE or NAV/SOTP fair value. Keep different products and cost legs separate. A futures price is a proxy, not the company's realized price. If power, anode, grade mix, unit cost, ownership or realized-price basis is missing, leave the affected valuation cell missing/partial rather than inventing the spread.
7. Use only supplied EV/KPE evidence ids. Decisive claims without a valid id must remain unverified or missing. Do not promote rows marked unverified_quote.
8. Every KPE or alternative clue has one model outcome: numeric old->new, probability before->after, unchanged/watch, or rejected. Narrative influence without a model outcome is invalid.
9. `research_readiness=ready` only when material segments, three-year consolidated model, scenario valuation, periods/units and decisive evidence are sufficiently complete. Use `partial` for unavailable sources or incomplete cells; those gaps are neutral and non-blocking. Use `blocked` only for a deterministic contradiction, invalid unit/period, or corrupted source that makes supplied facts unsafe—not merely because data is missing.
10. Return exactly one JSON object conforming to the schema. No Markdown, rating, recommendation or commentary outside JSON.
11. Populate `llm_analysis_layer` as the explicit LLM analysis intervention map. The LLM must improve quality in all eight places while respecting numeric evidence boundaries:
   - `business_question_tree`: after reading filing revenue mix, generate segment-specific questions that decide demand, competition, profitability, cash flow, valuation or rating.
   - `profit_pool_priority`: explain which businesses matter most after considering revenue weight, margin, growth, cash conversion, capex intensity, competitive erosion and valuation sensitivity.
   - `competition_and_substitution_analysis`: reason about true peers, customer switching, supplier diversification, self-supply, substitutes, new entrants and technology/regulatory change.
   - `qualitative_to_quantitative_bridge`: when ideal data are missing, state the qualitative conclusion, what partial data support or limit it, what cannot be quantified, and what must be retrieved.
   - `expectation_gap_analysis`: infer what the market or consensus may be pricing, where the model differs, and whether the gap is variable, magnitude or timing.
   - `red_team_counterarguments`: act as a skeptical analyst and list the strongest bear case for a positive thesis and strongest upside case for a negative thesis, each with a falsification signal.
   - `valuation_explanation`: explain valuation as a function of operating assumptions; code controls arithmetic, while the LLM explains method, multiple, risk premium and business-variable sensitivity.
   - `final_editorial_synthesis`: state how a PM should synthesize the above into investor-facing prose without exposing raw questions, evidence ledgers or workbench tables.
11a. Use the LLM for business-model interpretation, causal chains, counterevidence, question selection and assumption design. Numeric historical facts remain controlled by supplied structured/filing evidence. Never overwrite a reported figure with an LLM estimate. A commodity or thematic proxy may enter a causal chain only when the payload proves its economic relevance to the target's revenue or cost structure.
12. Distinguish a descriptive module from a decision-useful one. Do not promote a module into the packet unless verified evidence changes a named forecast line, scenario probability or valuation bucket, or unavailable evidence creates a dated retrieval/verification task.
13. Populate `handoff_manifest` as the loss-prevention contract. Separate frozen reported facts from analyst estimates and unresolved cells. Downstream agents must preserve the full three-year model, all material business units, every accepted financial bridge and every valuation bucket; any change requires an evidence id, old/new assumption and recalculated EPS/FCF/value impact.

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


def _schema_prompt(prompt: str) -> str:
    return f"""{prompt}

Provider compatibility constraints:
- Do not use tools or function calls for this response.
- Return strict RFC 8259 JSON only: one object, double-quoted keys/strings, no Markdown, no comments, no trailing commas, no NaN/Infinity.
- If the full analysis risks exceeding the output budget, prefer a compact schema-valid object with explicit missing_inputs/readiness_reasons over malformed or truncated JSON.
- Close every array and object before ending the response.
"""


def _repair_prompt(raw_content: str, initial_error: Exception) -> str:
    return f"""Repair the malformed JSON below so it validates against the schema.

Return exactly one valid JSON object and no Markdown or commentary. Preserve the supplied analysis and values. Do not add facts, estimates, ratings, or recommendations. If a long field prevents valid JSON, shorten that field rather than dropping required structure. Use empty arrays or nulls for unsupported optional fields. The object must conform to this JSON Schema:
{json.dumps(CompanyUnderwritingPacket.model_json_schema(), ensure_ascii=False, separators=(',', ':'))}

Initial validation error:
{initial_error}

JSON to repair:
{raw_content[:50000]}
"""


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
    response = llm.invoke(_schema_prompt(prompt))
    content = _response_text(response)
    if not str(content or "").strip():
        raise ValueError(
            "underwriting free-text fallback returned empty content; "
            f"structured_error={structured_error}"
        )
    raw_content = (
        json.dumps(content, ensure_ascii=False)
        if isinstance(content, Mapping)
        else str(content)
    )
    try:
        payload = _json_object(raw_content)
        return CompanyUnderwritingPacket.model_validate(payload)
    except Exception as initial_error:
        # Long company-underwriting objects occasionally contain a missing
        # comma, an unescaped quote, or a provider-specific schema mismatch even
        # when the underlying analysis is useful. Give the LLM one constrained
        # repair pass for both JSON parsing and schema-validation failures
        # instead of losing the entire company model.
        repaired = _response_text(llm.invoke(_repair_prompt(raw_content, initial_error)))
        try:
            payload = _json_object(str(repaired))
            return CompanyUnderwritingPacket.model_validate(payload)
        except Exception as repair_error:
            raise ValueError(
                "underwriting JSON validation and repair failed; "
                f"initial={initial_error}; repair={repair_error}; "
                f"structured={structured_error}"
            ) from repair_error


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


_METRIC_ALIASES: dict[str, tuple[str, ...]] = {
    "revenue": ("revenue", "operating_revenue", "营业收入", "营收"),
    "gross_margin": ("gross_margin", "grossprofit_margin", "毛利率", "综合毛利率"),
    "operating_profit": ("operating_profit", "营业利润", "经营利润"),
    "parent_net_profit": (
        "parent_net_profit",
        "net_profit_parent",
        "归母净利润",
        "归属于母公司股东的净利润",
    ),
    "eps": (
        "eps",
        "basic_eps",
        "diluted_eps",
        "diluted earnings per share",
        "基本每股收益",
        "稀释每股收益",
        "每股收益",
    ),
    "ocf": (
        "ocf",
        "operating_cash_flow",
        "经营活动现金流净额",
        "经营现金流",
    ),
    "capex": ("capex", "capital_expenditure", "资本开支", "资本支出"),
    "fcf": ("fcf", "free_cash_flow", "自由现金流"),
    "earning_assets": ("earning_assets", "生息资产"),
    "nim": ("nim", "净息差", "净利差"),
    "net_interest_income": ("net_interest_income", "净利息收入"),
    "fee_income": ("fee_income", "手续费及佣金净收入", "非息收入"),
    "pre_provision_profit": ("pre_provision_profit", "拨备前利润"),
    "credit_cost": ("credit_cost", "信用成本"),
    "roe": ("roe", "净资产收益率"),
    "cet1": ("cet1", "核心一级资本充足率"),
    "premium_or_ape": ("premium_or_ape", "premium", "ape", "保费"),
    "nbv": ("nbv", "新业务价值"),
    "investment_spread": ("investment_spread", "投资利差"),
    "opat": ("opat", "营运利润"),
    "solvency": ("solvency", "偿付能力"),
    "dividend_payout": ("dividend_payout", "分红率", "派息率"),
    "brokerage_revenue": ("brokerage_revenue", "经纪业务收入"),
    "investment_banking_revenue": ("investment_banking_revenue", "投行业务收入"),
    "asset_management_revenue": ("asset_management_revenue", "资管业务收入"),
    "trading_investment_income": ("trading_investment_income", "自营投资收益"),
    "capital_adequacy": ("capital_adequacy", "资本充足率"),
    "occupancy": ("occupancy", "出租率"),
    "rent_per_unit": ("rent_per_unit", "单位租金"),
    "noi": ("noi", "净营业收入"),
    "distributable_cash_flow": ("distributable_cash_flow", "可供分配现金流"),
    "payout": ("payout", "分派率"),
}


_OPERATING_MODEL_DRIVER_GROUPS: dict[
    str, tuple[tuple[str, tuple[str, ...]], ...]
] = {
    "volume_price_cost": (
        ("capacity", ("capacity", "产能")),
        ("utilization", ("utilization", "operating rate", "开工率", "产能利用率")),
        ("volume", ("volume", "shipment", "sales volume", "销量", "产量")),
        ("price/ASP", ("asp", "price", "售价", "均价", "价格")),
        ("unit/input cost", ("unit cost", "input cost", "raw material", "单位成本", "原料", "成本")),
        ("spread/margin", ("spread", "margin", "价差", "毛利率", "利润率")),
        ("capex/ROIC", ("capex", "roic", "capital expenditure", "资本开支", "投入资本回报")),
    ),
    "store_traffic_conversion_ticket": (
        ("store/customer base", ("store", "customer count", "门店", "客户数")),
        ("traffic", ("traffic", "passenger", "客流", "人流")),
        ("conversion", ("conversion", "转化率", "购买率")),
        ("ticket/ARPU", ("ticket", "arpu", "客单价", "单客收入")),
        ("mix/margin", ("mix", "margin", "品类结构", "毛利率", "利润率")),
    ),
    "users_arpu_retention": (
        ("users", ("user", "seat", "用户", "客户数")),
        ("paid penetration", ("paid", "penetration", "付费", "渗透率")),
        ("ARPU", ("arpu", "客单价", "单用户收入")),
        ("retention/churn", ("retention", "churn", "续费率", "留存率", "流失率")),
        ("delivery/cloud cost", ("delivery cost", "cloud cost", "交付成本", "云成本")),
    ),
    "project_backlog_delivery": (
        ("opening backlog", ("opening backlog", "期初在手订单", "期初订单")),
        ("new orders", ("new order", "新签订单")),
        ("delivery/acceptance", ("delivery", "acceptance", "交付", "验收")),
        ("ending backlog", ("ending backlog", "期末在手订单", "期末订单")),
        ("receivable/collection", ("receivable", "collection", "应收", "回款")),
    ),
    "commodity_volume_price_cost": (
        ("reserves/capacity", ("reserve", "capacity", "储量", "产能")),
        ("output", ("output", "production", "产量")),
        ("realized price", ("realized price", "selling price", "售价", "结算价")),
        ("cash cost/AISC", ("cash cost", "aisc", "现金成本", "全维持成本")),
        ("sustaining capex", ("sustaining capex", "维持性资本开支")),
        ("margin/FCF", ("margin", "fcf", "利润率", "自由现金流")),
    ),
    "financial_spread_credit": (
        ("earning assets", ("earning asset", "生息资产")),
        ("NIM/spread", ("nim", "net interest margin", "净息差")),
        ("fee income", ("fee income", "手续费", "中收")),
        ("credit cost", ("credit cost", "信用成本")),
        ("asset quality", ("npl", "non-performing", "不良率", "拨备覆盖率")),
        ("capital", ("capital adequacy", "cet1", "资本充足率", "核心一级资本")),
    ),
    "insurance_value": (
        ("premium/APE", ("premium", "ape", "保费", "新单保费")),
        ("NBV", ("nbv", "new business value", "新业务价值")),
        ("EV/CSM", ("embedded value", "csm", "内含价值", "合同服务边际")),
        ("investment spread", ("investment yield", "spread", "投资收益率", "利差")),
        ("claims/cost", ("claim", "combined ratio", "赔付率", "综合成本率")),
        ("solvency", ("solvency", "偿付能力")),
    ),
    "reit_occupancy_rent": (
        ("occupancy", ("occupancy", "出租率")),
        ("rent", ("rent", "租金", "租约")),
        ("NOI", ("noi", "net operating income", "净运营收入")),
        ("distributable cash", ("distributable", "可供分配")),
        ("payout/leverage", ("payout", "leverage", "分派率", "杠杆率")),
    ),
}


def _operating_model_driver_coverage(
    packet: CompanyUnderwritingPacket,
) -> tuple[list[str], list[str]]:
    """Return represented and missing driver groups for the selected model family."""
    family = packet.company_model.operating_model_family
    groups = _OPERATING_MODEL_DRIVER_GROUPS.get(family, ())
    if not groups:
        return [], []
    corpus_parts = [
        packet.company_model.revenue_equation,
        packet.company_model.profit_equation,
        packet.company_model.cash_flow_equation,
        packet.company_model.capital_intensity_and_reinvestment,
    ]
    for row in packet.business_unit_map:
        corpus_parts.extend(
            (
                row.revenue_driver_equation,
                row.profit_driver_equation,
                row.cash_and_capital_equation,
                " ".join(row.reported_metrics),
            )
        )
    for row in packet.segment_models:
        corpus_parts.extend(
            (
                " ".join(row.demand_and_order_drivers),
                row.industry_supply_and_capacity,
                row.volume_share_utilization,
                row.price_asp_take_rate,
                row.unit_cost_and_input_prices,
                row.margin_and_operating_leverage,
                row.working_capital_and_cash_conversion,
            )
        )
    for row in packet.forecast_lines:
        if any(
            value is not None
            for value in (row.base_value, row.year_1_value, row.year_2_value, row.year_3_value)
        ) or row.assumption_status.lower() not in {"", "missing"}:
            corpus_parts.extend((row.metric, row.formula, row.key_sensitivity))
    corpus = " ".join(str(value) for value in corpus_parts if value).lower()
    represented = [
        label
        for label, terms in groups
        if any(term.lower() in corpus for term in terms)
    ]
    missing = [label for label, _terms in groups if label not in represented]
    return represented, missing


def _canonical_metric_name(value: str) -> str:
    normalized = re.sub(r"[\W_]+", "", str(value or "")).lower()
    # Rates must not be mistaken for amount lines such as operating profit.
    is_rate = any(token in str(value or "").lower() for token in ("率", "ratio", "margin"))
    for canonical, aliases in _METRIC_ALIASES.items():
        for alias in aliases:
            alias_normalized = re.sub(r"[\W_]+", "", alias).lower()
            if normalized == alias_normalized:
                return canonical
            if len(alias_normalized) >= 4 and alias_normalized in normalized:
                if canonical == "operating_profit" and is_rate:
                    continue
                return canonical
    return re.sub(r"\s+", "_", str(value or "").strip().lower())


def _derive_market_snapshot(
    contexts: Mapping[str, str] | None,
) -> tuple[float | None, float | None, str]:
    """Derive diluted shares (mn) from same-snapshot market cap and close."""
    if not contexts:
        return None, None, ""
    preferred_keys = (
        "forecast_model",
        "price_earnings_decomposition",
        "price_move_attribution",
        "peer_comparison",
        "management_capital_allocation",
    )
    text = "\n".join(
        f"[{key}]\n{contexts.get(key, '') or contexts.get(key + '_context', '')}"
        for key in preferred_keys
        if contexts.get(key) or contexts.get(key + "_context")
    )
    market_cap_match = re.search(
        r"market\s*cap\s*\(cny\)\s*[|/]\s*([\d,]+(?:\.\d+)?)",
        text,
        re.I,
    )
    close_match = re.search(
        r"\|\s*(?:close|latest\s+close|current\s+price)\s*\|\s*"
        r"([\d,]+(?:\.\d+)?)\s*\|",
        text,
        re.I,
    )
    if not market_cap_match or not close_match:
        return None, None, ""
    market_cap_cny = float(market_cap_match.group(1).replace(",", ""))
    current_price_cny = float(close_match.group(1).replace(",", ""))
    if market_cap_cny <= 0 or current_price_cny <= 0:
        return None, None, ""
    diluted_share_count_mn = market_cap_cny / current_price_cny / 1_000_000.0
    if not 1.0 <= diluted_share_count_mn <= 10_000_000.0:
        return None, None, ""
    return (
        diluted_share_count_mn,
        current_price_cny,
        "market cap / close, using forecast_model and price_earnings_decomposition",
    )


def _derive_reported_share_count(
    contexts: Mapping[str, str] | None,
) -> tuple[float | None, str, str]:
    """Read the latest Tushare pledge table total_share (10,000 shares)."""
    if not contexts:
        return None, "", ""
    text = str(
        contexts.get("shareholder_structure", "")
        or contexts.get("shareholder_structure_context", "")
        or ""
    )
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if "total_share" not in line.lower() or "|" not in line:
            continue
        headers = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
        try:
            total_share_index = headers.index("total_share")
        except ValueError:
            continue
        period_index = headers.index("end_date") if "end_date" in headers else 0
        for row in lines[index + 1 : index + 12]:
            if re.search(r"\|\s*[-:]+", row):
                continue
            cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
            if len(cells) <= total_share_index:
                continue
            try:
                total_share_10k = float(cells[total_share_index].replace(",", ""))
            except ValueError:
                continue
            if total_share_10k <= 0:
                continue
            period = cells[period_index] if len(cells) > period_index else ""
            return (
                total_share_10k / 100.0,
                period,
                "Tushare pledge_stat.total_share (10,000 shares) / 100",
            )
    return None, "", ""


def _derive_registered_capital_share_count(
    contexts: Mapping[str, str] | None,
) -> tuple[float | None, str]:
    """Derive shares from Tushare stock_basic reg_capital (CNY 10k)."""

    if not contexts:
        return None, ""
    text = str(
        contexts.get("management_capital_allocation", "")
        or contexts.get("management_capital_allocation_context", "")
        or ""
    )
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if "reg_capital" not in line.lower() or "|" not in line:
            continue
        headers = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
        try:
            capital_index = headers.index("reg_capital")
        except ValueError:
            continue
        for row in lines[index + 1 : index + 8]:
            if re.search(r"\|\s*[-:]+", row):
                continue
            cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
            if len(cells) <= capital_index:
                continue
            try:
                registered_capital_10k_cny = float(
                    cells[capital_index].replace(",", "")
                )
            except ValueError:
                continue
            if registered_capital_10k_cny <= 0:
                continue
            return (
                registered_capital_10k_cny / 100.0,
                "Tushare stock_basic.reg_capital (CNY 10,000) / 100; CNY 1 par value",
            )
    return None, ""


def derive_share_count_control(
    contexts: Mapping[str, str] | None,
) -> dict[str, Any]:
    """Return the canonical share count plus independent cross-checks."""
    pledge_proxy_mn, pledge_period, pledge_formula = _derive_reported_share_count(
        contexts
    )
    registered_mn, registered_formula = _derive_registered_capital_share_count(
        contexts
    )
    market_mn, current_price, market_formula = _derive_market_snapshot(contexts)
    conflict_pct: float | None = None
    if registered_mn and market_mn:
        conflict_pct = abs(registered_mn - market_mn) / registered_mn * 100.0
    canonical_mn = registered_mn or market_mn or pledge_proxy_mn
    source_type = (
        "registered_capital"
        if registered_mn is not None
        else "market_cap_div_close"
        if market_mn is not None
        else "pledge_stat_proxy"
        if pledge_proxy_mn is not None
        else "unresolved"
    )
    period = (
        "latest stock_basic"
        if registered_mn is not None
        else "market snapshot"
        if market_mn is not None
        else pledge_period
    )
    formula = (
        registered_formula
        if registered_mn is not None
        else market_formula
        if market_mn is not None
        else pledge_formula
    )
    cross_checks: list[str] = []
    if registered_mn is not None:
        cross_checks.append(f"registered capital proxy={registered_mn:.3f} mn")
    if market_mn is not None:
        cross_checks.append(f"market cap / close={market_mn:.3f} mn")
    if pledge_proxy_mn is not None:
        cross_checks.append(
            f"pledge_stat total_share proxy={pledge_proxy_mn:.3f} mn (not canonical)"
        )
    if conflict_pct is not None:
        cross_checks.append(f"registered-vs-market difference={conflict_pct:.3f}%")
    return {
        "canonical_share_count_mn": canonical_mn,
        "source_type": source_type,
        "period": period,
        "formula": formula,
        "current_price_cny": current_price,
        "reported_share_count_mn": registered_mn,
        "pledge_stat_share_count_proxy_mn": pledge_proxy_mn,
        "market_implied_share_count_mn": market_mn,
        "conflict_pct": conflict_pct,
        "cross_checks": cross_checks,
    }


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
    business_units = [
        BusinessUnitMap(
            unit_id=f"BU{index:02d}",
            unit_name=model.segment,
            unit_type="reported_segment",
            disclosure_basis="reported",
            economic_role="Filing-reported segment; economic sub-unit decomposition still required.",
            reported_metrics=[
                metric
                for metric, value in (
                    ("revenue", model.base_revenue_value),
                    ("revenue growth", model.base_revenue_growth_pct),
                    ("margin", model.base_margin_pct),
                )
                if value is not None
            ],
            missing_inputs=["product/channel/geography/customer economics not deterministically available"],
        )
        for index, model in enumerate(segment_models, start=1)
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
        schema_version=2,
        symbol=symbol,
        as_of_date=str(as_of_date),
        forecast_years=years,
        research_readiness="blocked",
        readiness_reasons=["LLM company underwriting failed; only deterministic skeleton is available."],
        business_unit_map=business_units,
        segment_models=segment_models,
        forecast_lines=forecast_lines,
        scenarios=[ScenarioUnderwriting(scenario=name) for name in ("bull", "base", "bear")],
        valuation_buckets=[
            ValuationBucket(
                bucket="consolidated business",
                inclusion="excluded",
                missing_inputs=["reconciled autonomous forecast and valuation basis unavailable"],
            )
        ],
        valuation_closure=ValuationClosure(
            status="not_valued",
            missing_inputs=["LLM underwriting model unavailable"],
        ),
        llm_analysis_layer=LLMAnalysisLayer(
            qualitative_to_quantitative_bridge=(
                "LLM analysis layer unavailable; deterministic facts may be used, but "
                "business questions, expectation gap, red-team critique and editorial synthesis "
                "must be regenerated before publishing a high-conviction PM report."
            ),
            evidence_boundaries=[
                "No LLM business-question tree was produced.",
                "No LLM profit-pool prioritization was produced.",
                "No LLM competition/substitution analysis was produced.",
                "No LLM expectation-gap analysis was produced.",
                "No LLM red-team critique was produced.",
                "No LLM valuation explanation was produced.",
                "No LLM final editorial synthesis was produced.",
            ],
        ),
        handoff_manifest=ModelHandoffManifest(
            unresolved_model_cells=["all company-specific driver and valuation cells"],
            downstream_must_preserve=[
                "filing-reported segments",
                "three forward years",
                "missing cells and retrieval tasks",
            ],
        ),
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


def _text_mentions_cny_mn(text: str, target_cny_mn: float) -> bool:
    """Return whether prose contains ``target_cny_mn`` in a supported CNY unit."""

    number = r"[-+]?\d[\d,]*(?:\.\d+)?"
    values: list[float] = []
    suffix_scales = {
        "cny mn": 1.0,
        "cny_mn": 1.0,
        "rmb mn": 1.0,
        "\u767e\u4e07\u5143": 1.0,
        "\u4e07\u5143": 0.01,
        "\u4ebf\u5143": 100.0,
        "cny": 0.000001,
        "rmb": 0.000001,
        "\u4eba\u6c11\u5e01\u5143": 0.000001,
        "\u5143": 0.000001,
    }
    unit_pattern = "|".join(
        re.escape(unit) for unit in sorted(suffix_scales, key=len, reverse=True)
    )
    for match in re.finditer(
        rf"(?P<value>{number})\s*(?P<unit>{unit_pattern})(?![a-z_])",
        str(text or ""),
        re.I,
    ):
        raw = float(match.group("value").replace(",", ""))
        values.append(raw * suffix_scales[match.group("unit").lower()])
    for match in re.finditer(rf"\b(?:CNY|RMB)\s*(?P<value>{number})", str(text or ""), re.I):
        raw = float(match.group("value").replace(",", ""))
        values.append(raw / 1_000_000.0)
    tolerance = max(abs(float(target_cny_mn)) * 0.005, 0.5)
    return any(abs(value - float(target_cny_mn)) <= tolerance for value in values)


def _remove_mislabeled_prior_guidance_claims(
    lines: list[str],
    period: str,
    prior_values_cny_mn: list[float],
) -> tuple[list[str], list[str]]:
    """Drop prose that promotes an official comparison-column value to current H1."""

    retained: list[str] = []
    rejected: list[str] = []
    scope_pattern = re.compile(
        rf"(?:{re.escape(period)}|\bH1\b|performance\s+preview|earnings\s+guidance|"
        r"\u534a\u5e74\u5ea6\u4e1a\u7ee9\u9884\u544a|\u4e1a\u7ee9\u9884\u544a)",
        re.I,
    )
    prior_pattern = re.compile(
        r"(?:prior|previous|last\s+year|comparison|comparative|"
        r"\u4e0a\u5e74\u540c\u671f|\u53bb\u5e74\u540c\u671f|\u540c\u6bd4\u57fa\u6570|\u6bd4\u8f83\u671f)",
        re.I,
    )
    for value in lines:
        line = str(value or "")
        mislabeled = (
            bool(scope_pattern.search(line))
            and not prior_pattern.search(line)
            and any(_text_mentions_cny_mn(line, amount) for amount in prior_values_cny_mn)
        )
        if mislabeled:
            rejected.append(line)
        else:
            retained.append(line)
    return retained, rejected


def _validate_packet(
    packet: CompanyUnderwritingPacket,
    structured: Mapping[str, Any],
    contexts: Mapping[str, str] | None = None,
) -> CompanyUnderwritingPacket:
    valid_ids = _valid_evidence_ids(structured)
    years = packet.forecast_years
    expected_years = _forecast_years(packet.as_of_date)
    if years != expected_years:
        packet.preprocessing_notes.append(
            f"forecast years normalized from {years} to {expected_years}"
        )
        packet.forecast_years = expected_years

    for item in [
        packet.company_model,
        *packet.business_unit_map,
        *packet.segment_models,
        *packet.underwriting_questions,
        *packet.forecast_lines,
        *packet.scenarios,
        *packet.thesis_financial_bridges,
        *packet.moat_evidence_tests,
        *packet.valuation_buckets,
    ]:
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

    share_control = derive_share_count_control(contexts)
    canonical_shares_mn = share_control["canonical_share_count_mn"]
    supplied_shares_mn = packet.company_model.diluted_share_count_mn
    share_count_materially_replaced = False
    if canonical_shares_mn is not None:
        if supplied_shares_mn is not None and supplied_shares_mn > 0:
            supplied_difference_pct = (
                abs(supplied_shares_mn - canonical_shares_mn)
                / canonical_shares_mn
                * 100.0
            )
            if supplied_difference_pct > 2.0:
                share_count_materially_replaced = True
                packet.preprocessing_notes.append(
                    "LLM-supplied diluted shares rejected: "
                    f"{supplied_shares_mn:.3f} mn vs deterministic "
                    f"{canonical_shares_mn:.3f} mn ({supplied_difference_pct:.2f}% difference)."
                )
        packet.company_model.diluted_share_count_mn = canonical_shares_mn
        packet.company_model.share_count_period = (
            f"{packet.as_of_date}; {share_control['period']}; {share_control['formula']}"
        )
        packet.company_model.share_count_source_type = share_control["source_type"]
        packet.company_model.share_count_formula = share_control["formula"]
        packet.company_model.share_count_cross_checks = share_control["cross_checks"]
        packet.preprocessing_notes.append(
            "diluted shares set deterministically: "
            f"{canonical_shares_mn:.3f} mn ({share_control['source_type']})"
        )
    elif supplied_shares_mn is not None and supplied_shares_mn > 0:
        packet.company_model.share_count_source_type = "model_supplied"
        packet.company_model.share_count_formula = (
            packet.company_model.share_count_formula
            or "model supplied; no deterministic cross-check available"
        )
    conflict_pct = share_control.get("conflict_pct")
    if conflict_pct is not None and conflict_pct > 2.0:
        packet.research_readiness = "blocked"
        packet.readiness_reasons.append(
            "Registered-capital and market-cap/close share counts conflict by "
            f"{conflict_pct:.2f}% (>2%)."
        )
    derived_price_cny = share_control["current_price_cny"]
    if derived_price_cny is not None:
        packet.valuation_closure.current_price_cny = derived_price_cny
        packet.preprocessing_notes.append(
            f"valuation current price restored from market snapshot: CNY {derived_price_cny:.4f}"
        )

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

    if not packet.business_unit_map:
        packet.business_unit_map = [
            BusinessUnitMap(
                unit_id=f"BU{index:02d}",
                unit_name=row.segment,
                unit_type="reported_segment",
                disclosure_basis=(
                    "reported" if row.base_revenue_value is not None else "missing"
                ),
                economic_role="Filing segment restored as the minimum company decomposition.",
                revenue_driver_equation="missing; decompose with company-specific volume/price/channel drivers",
                profit_driver_equation="missing; connect revenue to segment margin and operating cost",
                cash_and_capital_equation="missing; connect working capital, capex and return on capital",
                evidence_ids=list(row.evidence_ids),
                missing_inputs=["economic unit decomposition omitted by underwriting model"],
            )
            for index, row in enumerate(packet.segment_models, start=1)
        ]
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Economic business-unit map was omitted; filing segments were restored as a minimum decomposition."
        )

    if not packet.thesis_financial_bridges:
        packet.thesis_financial_bridges = [
            ThesisFinancialBridge(
                bridge_id=f"TFB{index:02d}",
                thesis_or_question=row.question,
                affected_unit=(row.decisive_model_variables[0] if row.decisive_model_variables else "consolidated"),
                operating_driver=", ".join(row.decisive_model_variables[:3]),
                evidence_ids=list(row.evidence_ids),
                missing_inputs=[
                    "claim has not been translated into revenue/profit/EPS/FCF/value impact"
                ],
            )
            for index, row in enumerate(packet.underwriting_questions[:6], start=1)
        ]
        if packet.underwriting_questions:
            packet.research_readiness = "partial"
            packet.readiness_reasons.append(
                "Thesis questions lack explicit financial-transmission bridges."
            )

    if not packet.moat_evidence_tests and packet.company_model.moat_mechanisms:
        packet.moat_evidence_tests = [
            MoatEvidenceTest(
                moat_mechanism=mechanism,
                observable_test="missing; compare an operating or financial outcome with history and true peers",
                financial_transmission=(
                    packet.company_model.moat_to_financial_transmission[index]
                    if index < len(packet.company_model.moat_to_financial_transmission)
                    else "missing"
                ),
                status="unproven",
                next_verification="retrieve reported KPI or true-peer evidence",
            )
            for index, mechanism in enumerate(packet.company_model.moat_mechanisms)
        ]
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Claimed moat mechanisms lack observable evidence tests."
        )

    if not packet.valuation_buckets:
        packet.valuation_buckets = [
            ValuationBucket(
                bucket="consolidated business",
                inclusion="excluded",
                missing_inputs=["mutually exclusive valuation buckets were not supplied"],
            )
        ]
        packet.research_readiness = "partial"
        packet.readiness_reasons.append("Valuation buckets are missing.")

    packet.handoff_manifest.handoff_version = "underwriting-v2"
    if not packet.handoff_manifest.downstream_must_preserve:
        packet.handoff_manifest.downstream_must_preserve = [
            "all material business units and disclosure limitations",
            "three forward years and every industry-native consolidated line",
            "thesis financial bridges and moat evidence status",
            "mutually exclusive valuation buckets and double-counting checks",
            "reported facts, estimates, unresolved cells and evidence ids",
        ]

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

    present_unit_names = {
        _normalize_segment_name(row.unit_name) for row in packet.business_unit_map
    }
    for index, row in enumerate(packet.segment_models, start=1):
        if _normalize_segment_name(row.segment) in present_unit_names:
            continue
        packet.business_unit_map.append(
            BusinessUnitMap(
                unit_id=f"BU{len(packet.business_unit_map) + index:02d}",
                unit_name=row.segment,
                unit_type="reported_segment",
                disclosure_basis=(
                    "reported" if row.base_revenue_value is not None else "missing"
                ),
                economic_role="Filing segment restored after structured evidence reconciliation.",
                evidence_ids=list(row.evidence_ids),
                missing_inputs=["economic sub-unit driver equations require analyst completion"],
            )
        )
    if not packet.business_unit_map:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "No reported or analytical economic business unit could be identified."
        )

    required_metrics = _required_metrics_for_profile(
        packet.company_model.model_profile
    )
    consolidated_groups: dict[str, list[ForecastLine]] = {}
    for row in packet.forecast_lines:
        if row.segment.lower() not in {"consolidated", "group", "合并", "公司整体"}:
            continue
        consolidated_groups.setdefault(_canonical_metric_name(row.metric), []).append(row)
    for canonical, rows in consolidated_groups.items():
        if canonical not in required_metrics or len(rows) < 2:
            continue
        ranked = sorted(
            rows,
            key=lambda row: sum(
                value is not None
                for value in (
                    row.base_value,
                    row.year_1_value,
                    row.year_2_value,
                    row.year_3_value,
                )
            ),
            reverse=True,
        )
        keeper = ranked[0]
        for duplicate in ranked[1:]:
            keeper.evidence_ids = list(
                dict.fromkeys([*keeper.evidence_ids, *duplicate.evidence_ids])
            )
            keeper.missing_inputs = list(
                dict.fromkeys([*keeper.missing_inputs, *duplicate.missing_inputs])
            )
            packet.forecast_lines.remove(duplicate)
        packet.preprocessing_notes.append(
            f"duplicate consolidated forecast aliases merged into {canonical}"
        )
    present_metrics = {
        _canonical_metric_name(row.metric)
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
        and _canonical_metric_name(row.metric) in required_metrics
    ]
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
        _canonical_metric_name(row.metric): row
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
            if profit is None:
                continue
            implied = profit / share_count
            if eps is not None and abs(implied - eps) / max(abs(implied), 0.01) > 0.02:
                packet.research_readiness = "partial"
                packet.readiness_reasons.append(
                    f"Parent-profit/EPS/share-count conflict corrected for {attr}."
                )
                packet.preprocessing_notes.append(
                    f"{attr} EPS replaced: {eps:.6g} -> {implied:.6g} CNY/share."
                )
            setattr(eps_row, attr, implied)
            eps_row.unit = "CNY/share"
            eps_row.assumption_status = "calculated"
            eps_row.formula = "parent net profit (CNY mn) / diluted shares (mn)"
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
            if ocf is None or capex is None:
                continue
            expected_fcf = ocf - abs(capex)
            if fcf is None:
                setattr(fcf_row, attr, expected_fcf)
                fcf_row.assumption_status = "calculated"
                fcf_row.formula = fcf_row.formula or "OCF - abs(capex)"
                continue
            if abs(expected_fcf - fcf) > max(abs(expected_fcf) * 0.05, 1.0):
                packet.research_readiness = "partial"
                packet.readiness_reasons.append(
                    f"OCF-capex-FCF reconciliation fails for {attr}."
                )

    guidance_context = "\n".join(
        str(value or "")
        for key, value in (contexts or {}).items()
        if key in {"forecast_model", "company_events", "news", "earnings_model"}
    )
    official_guidance = parse_official_guidance_record(guidance_context)
    guidance_period = str(official_guidance.get("period", ""))
    prior_values = [
        float(value)
        for key in (
            "parent_net_profit_prior_cny_mn",
            "deducted_parent_net_profit_prior_cny_mn",
            "revenue_prior_cny_mn",
        )
        if (value := official_guidance.get(key)) is not None
    ]
    if guidance_period and prior_values:
        frozen, rejected_frozen = _remove_mislabeled_prior_guidance_claims(
            packet.handoff_manifest.frozen_reported_facts,
            guidance_period,
            prior_values,
        )
        notes, rejected_notes = _remove_mislabeled_prior_guidance_claims(
            packet.preprocessing_notes,
            guidance_period,
            prior_values,
        )
        packet.handoff_manifest.frozen_reported_facts = frozen
        packet.preprocessing_notes = notes
        if rejected_frozen or rejected_notes:
            packet.preprocessing_notes.append(
                f"Rejected {len(rejected_frozen) + len(rejected_notes)} mislabeled "
                f"{guidance_period} guidance claim(s) that matched the official prior-period column."
            )
    first_forecast_year = str(packet.forecast_years[0] if packet.forecast_years else "")
    guidance_is_h1_for_first_year = bool(
        guidance_period.endswith("H1")
        and first_forecast_year.startswith(guidance_period[:4])
    )
    if guidance_is_h1_for_first_year:
        metric_rows = {
            "revenue_cny_mn": consolidated_by_metric.get("revenue"),
            "parent_net_profit_cny_mn": profit_row,
        }
        frozen_parts: list[str] = []
        for metric_key, row in metric_rows.items():
            h1_value = official_guidance.get(metric_key)
            if h1_value is None:
                continue
            frozen_parts.append(f"{metric_key}={float(h1_value):g} CNY mn")
            if row is None or row.year_1_value is None:
                packet.research_readiness = "blocked"
                packet.readiness_reasons.append(
                    f"Official {guidance_period} {metric_key} lacks a full-year forecast bridge."
                )
                continue
            if not any(
                token in str(row.unit).lower()
                for token in ("cny mn", "cny_mn", "rmb mn", "百万元", "百万人民币")
            ):
                packet.research_readiness = "blocked"
                packet.readiness_reasons.append(
                    f"Official {guidance_period} {metric_key} cannot be reconciled to forecast unit {row.unit!r}."
                )
                continue
            full_year_value = float(row.year_1_value)
            implied_h2 = full_year_value - float(h1_value)
            bridge = (
                f"official {guidance_period}={float(h1_value):g} CNY mn; "
                f"{first_forecast_year}={full_year_value:g} CNY mn; "
                f"implied H2={implied_h2:g} CNY mn"
            )
            if bridge.lower() not in str(row.formula).lower():
                row.formula = f"{row.formula}; {bridge}".strip("; ")
            packet.reconciliation_checks.append(bridge)
            if implied_h2 < -max(abs(float(h1_value)) * 0.02, 1.0):
                packet.research_readiness = "blocked"
                packet.readiness_reasons.append(
                    f"{first_forecast_year} {metric_key} is below official {guidance_period}; "
                    "an explicit, evidenced H2 loss/reversal bridge is required."
                )
        deducted = official_guidance.get("deducted_parent_net_profit_cny_mn")
        if deducted is not None:
            frozen_parts.append(
                f"deducted_parent_net_profit_cny_mn={float(deducted):g} CNY mn"
            )
            packet.reconciliation_checks.append(
                f"official {guidance_period} deducted parent net profit="
                f"{float(deducted):g} CNY mn; do not relabel parent-profit forecasts as recurring/deducted profit"
            )
        if frozen_parts:
            frozen_fact = f"Official {guidance_period}: " + "; ".join(frozen_parts)
            if frozen_fact not in packet.handoff_manifest.frozen_reported_facts:
                packet.handoff_manifest.frozen_reported_facts.append(frozen_fact)
            preserve_rule = (
                f"Preserve the official {guidance_period} metrics and the H1 + implied H2 = FY bridge; "
                "never store recurring/deducted profit in a parent-net-profit field."
            )
            if preserve_rule not in packet.handoff_manifest.downstream_must_preserve:
                packet.handoff_manifest.downstream_must_preserve.append(preserve_rule)

    for scenario in packet.scenarios:
        if guidance_is_h1_for_first_year and scenario.parent_net_profit_cny_mn is not None:
            h1_parent_profit = official_guidance.get("parent_net_profit_cny_mn")
            if (
                h1_parent_profit is not None
                and float(scenario.parent_net_profit_cny_mn)
                < float(h1_parent_profit) * 0.98
            ):
                scenario.missing_inputs.append(
                    f"explicit evidenced H2 loss/reversal bridge required because FY parent profit is below official {guidance_period}"
                )
                scenario.parent_net_profit_cny_mn = None
                scenario.eps_cny = None
                scenario.fair_value_per_share = None
                packet.research_readiness = "blocked"
                packet.readiness_reasons.append(
                    f"{scenario.scenario} FY parent-profit scenario is below official {guidance_period}."
                )
        if (
            scenario.parent_net_profit_cny_mn is not None
            and share_count
            and share_count > 0
        ):
            implied_scenario_eps = scenario.parent_net_profit_cny_mn / share_count
            if (
                scenario.eps_cny is not None
                and abs(scenario.eps_cny - implied_scenario_eps)
                / max(abs(implied_scenario_eps), 0.01)
                > 0.02
            ):
                packet.preprocessing_notes.append(
                    f"{scenario.scenario} scenario EPS replaced: "
                    f"{scenario.eps_cny:.6g} -> {implied_scenario_eps:.6g}."
                )
            scenario.eps_cny = implied_scenario_eps
        pe_method = any(
            token in scenario.valuation_method.lower()
            for token in ("pe", "p/e", "市盈率")
        )
        if scenario.eps_cny is not None and scenario.valuation_multiple is not None and pe_method:
            expected_value = scenario.eps_cny * scenario.valuation_multiple
            if scenario.fair_value_per_share is None or abs(
                expected_value - scenario.fair_value_per_share
            ) > max(abs(expected_value) * 0.03, 1.0):
                packet.research_readiness = "partial"
                packet.readiness_reasons.append(
                    f"{scenario.scenario} scenario EPS x PE does not reconcile to fair value."
                )
                scenario.fair_value_per_share = expected_value
                packet.preprocessing_notes.append(
                    f"{scenario.scenario} fair value replaced by deterministic EPS x PE calculation."
                )
        elif share_count_materially_replaced and scenario.fair_value_per_share is not None:
            packet.preprocessing_notes.append(
                f"{scenario.scenario} fair value removed because its non-PE per-share bridge "
                "used a rejected share-count basis."
            )
            scenario.fair_value_per_share = None
            scenario.missing_inputs.append(
                "rebuild PB/DCF per-share valuation after deterministic share-count correction"
            )
            packet.research_readiness = "partial"
            packet.readiness_reasons.append(
                f"{scenario.scenario} non-PE scenario valuation was invalidated by share-count correction."
            )

    quantified_bridges = [
        row
        for row in packet.thesis_financial_bridges
        if row.quantification_status in {"quantified", "partially_quantified"}
    ]
    if packet.thesis_financial_bridges and not quantified_bridges:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "No decisive thesis has been translated into a quantified financial bridge."
        )
    for test in packet.moat_evidence_tests:
        if test.status not in {"proven", "partial"} or test.evidence_ids:
            continue
        previous = test.status
        test.status = "unproven"
        test.evidence_result = (
            f"Downgraded from {previous}: no valid EV/KPE evidence id supports the test."
        )
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            f"Moat claim lacks traceable evidence ids: {test.moat_mechanism}."
        )
    if packet.company_model.moat_mechanisms and not any(
        row.status in {"proven", "partial"} for row in packet.moat_evidence_tests
    ):
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "All claimed moat mechanisms remain unproven by observable evidence."
        )

    closure = packet.valuation_closure
    if share_count_materially_replaced:
        closure.core_value_per_share_cny = None
        closure.probability_weighted_fair_value_per_share_cny = None
        closure.option_value_per_share_cny = None
        closure.other_adjustments_per_share_cny = None
        closure.fair_value_per_share_cny = None
        closure.expected_return_pct = None
        closure.status = "partial"
        closure.missing_inputs.append(
            "valuation closure reset after deterministic share-count correction"
        )
    closure.diluted_share_count_mn = packet.company_model.diluted_share_count_mn
    scenario_values = [
        (row.probability_pct, row.fair_value_per_share)
        for row in packet.scenarios
        if row.probability_pct is not None and row.fair_value_per_share is not None
    ]
    if len(scenario_values) == 3:
        closure.probability_weighted_fair_value_per_share_cny = sum(
            float(probability) * float(value) / 100.0
            for probability, value in scenario_values
        )
    if (
        closure.fair_value_per_share_cny is None
        and closure.probability_weighted_fair_value_per_share_cny is not None
    ):
        closure.fair_value_per_share_cny = (
            closure.probability_weighted_fair_value_per_share_cny
        )
    if (
        closure.current_price_cny is not None
        and closure.current_price_cny > 0
        and closure.fair_value_per_share_cny is not None
    ):
        calculated_return = (
            closure.fair_value_per_share_cny / closure.current_price_cny - 1.0
        ) * 100.0
        if (
            closure.expected_return_pct is not None
            and abs(closure.expected_return_pct - calculated_return) > 0.6
        ):
            closure.status = "partial"
            closure.missing_inputs.append(
                "reported expected return does not reconcile to current price and fair value"
            )
            packet.research_readiness = "partial"
            packet.readiness_reasons.append(
                "Valuation expected-return arithmetic does not reconcile."
            )
        closure.expected_return_pct = calculated_return
    if (
        closure.probability_weighted_fair_value_per_share_cny is not None
        and closure.fair_value_per_share_cny is not None
        and abs(
            closure.probability_weighted_fair_value_per_share_cny
            - closure.fair_value_per_share_cny
        )
        > max(abs(closure.fair_value_per_share_cny) * 0.03, 0.5)
    ):
        closure.status = "partial"
        closure.missing_inputs.append(
            "fair value does not reconcile to the probability-weighted scenario value"
        )
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Valuation closure conflicts with probability-weighted scenario value."
        )
    included_buckets = [
        row for row in packet.valuation_buckets if row.inclusion != "excluded"
    ]
    if len(included_buckets) > 1 and not closure.double_counting_checks:
        closure.status = "partial"
        closure.missing_inputs.append(
            "multiple included valuation buckets lack explicit double-counting checks"
        )
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Multiple valuation buckets lack explicit double-counting checks."
        )
    if closure.diluted_share_count_mn and closure.diluted_share_count_mn > 0:
        for bucket in included_buckets:
            if bucket.equity_value_cny_mn is not None:
                deterministic_per_share = (
                    bucket.equity_value_cny_mn / closure.diluted_share_count_mn
                )
                if (
                    bucket.per_share_value_cny is not None
                    and abs(bucket.per_share_value_cny - deterministic_per_share)
                    > max(abs(deterministic_per_share) * 0.02, 0.1)
                ):
                    packet.preprocessing_notes.append(
                        f"valuation bucket per-share value replaced for {bucket.bucket}: "
                        f"{bucket.per_share_value_cny:.6g} -> {deterministic_per_share:.6g}."
                    )
                bucket.per_share_value_cny = deterministic_per_share
            if (
                bucket.equity_value_cny_mn is None
                or bucket.per_share_value_cny is None
            ):
                continue
            implied_per_share = (
                bucket.equity_value_cny_mn / closure.diluted_share_count_mn
            )
            if abs(implied_per_share - bucket.per_share_value_cny) > max(
                abs(implied_per_share) * 0.03, 0.2
            ):
                closure.status = "partial"
                closure.missing_inputs.append(
                    f"{bucket.bucket} equity-value/per-share conversion does not reconcile"
                )
                packet.research_readiness = "partial"
                packet.readiness_reasons.append(
                    f"Valuation per-share conversion fails for bucket: {bucket.bucket}."
                )
    overlap_keys = [
        row.overlap_key.strip().lower()
        for row in packet.valuation_buckets
        if row.inclusion != "excluded" and row.overlap_key.strip()
    ]
    duplicate_overlap_keys = sorted(
        {key for key in overlap_keys if overlap_keys.count(key) > 1}
    )
    if duplicate_overlap_keys:
        closure.status = "partial"
        closure.missing_inputs.append(
            "resolve duplicate valuation overlap keys: "
            + ", ".join(duplicate_overlap_keys)
        )
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Valuation buckets contain potential double counting."
        )
    if closure.status != "closed" or closure.fair_value_per_share_cny is None:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Valuation has not closed from mutually exclusive buckets to per-share fair value."
        )

    profile_family = {
        "bank": "financial_spread_credit",
        "insurance": "insurance_value",
        "reit": "reit_occupancy_rent",
    }
    if packet.company_model.operating_model_family == "other":
        inferred_family = profile_family.get(packet.company_model.model_profile)
        if inferred_family:
            packet.company_model.operating_model_family = inferred_family
            packet.preprocessing_notes.append(
                f"operating model family inferred from profile: {inferred_family}"
            )
        elif packet.company_model.model_profile == "corporate":
            packet.research_readiness = "partial"
            packet.readiness_reasons.append(
                "Industry-native operating model family was not selected."
            )
    represented_drivers, missing_drivers = _operating_model_driver_coverage(packet)
    if missing_drivers:
        packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            f"{packet.company_model.operating_model_family} driver chain is incomplete; "
            "missing: " + ", ".join(missing_drivers)
        )
    if represented_drivers:
        packet.preprocessing_notes.append(
            f"operating model driver coverage ({packet.company_model.operating_model_family}): "
            + ", ".join(represented_drivers)
        )
    if not packet.company_model.revenue_equation or not packet.company_model.profit_equation:
        packet.research_readiness = "blocked"
        packet.readiness_reasons.append("Company revenue/profit operating equations are missing.")
    packet.readiness_reasons = [
        reason
        for reason in packet.readiness_reasons
        if not reason.startswith("Three-year values remain missing for consolidated line(s):")
    ]
    final_incomplete_rows = [
        row.metric
        for row in packet.forecast_lines
        if row.segment.lower() in {"consolidated", "group", "鍚堝苟", "鍏徃鏁翠綋"}
        and _canonical_metric_name(row.metric) in required_metrics
        and any(
            value is None
            for value in (row.year_1_value, row.year_2_value, row.year_3_value)
        )
    ]
    if final_incomplete_rows:
        if packet.research_readiness != "blocked":
            packet.research_readiness = "partial"
        packet.readiness_reasons.append(
            "Three-year values remain missing for consolidated line(s): "
            + ", ".join(final_incomplete_rows[:8])
        )
    packet.readiness_reasons = list(dict.fromkeys(packet.readiness_reasons))
    if any(
        reason.startswith(
            (
                "Company revenue/profit operating equations are missing.",
                "Registered-capital and market-cap/close share counts conflict",
                "Official ",
            )
        )
        or "below official" in reason
        for reason in packet.readiness_reasons
    ):
        packet.research_readiness = "blocked"
    packet.schema_version = 2
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
        return _validate_packet(packet, structured_research, contexts).model_dump()
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
        if isinstance(value, Mapping):
            return {key: clip(item, limit) for key, item in value.items()}
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
    unit_keys = (
        "unit_id",
        "unit_name",
        "unit_type",
        "disclosure_basis",
        "parent_unit",
        "economic_role",
        "revenue_driver_equation",
        "profit_driver_equation",
        "cash_and_capital_equation",
        "reported_metrics",
        "evidence_ids",
        "missing_inputs",
        "next_verification",
    )
    business_units = [
        {key: clip(row.get(key)) for key in unit_keys if key in row}
        for row in list(packet.get("business_unit_map", []))[:16]
    ]
    return {
        "schema_version": packet.get("schema_version"),
        "symbol": packet.get("symbol"),
        "as_of_date": packet.get("as_of_date"),
        "forecast_years": packet.get("forecast_years", []),
        "research_readiness": packet.get("research_readiness"),
        "readiness_reasons": clip(packet.get("readiness_reasons", [])),
        "company_model": company,
        "business_unit_map": business_units,
        "segment_models": segments,
        "underwriting_questions": questions,
        "forecast_lines": [
            clip(row) for row in list(packet.get("forecast_lines", []))[:36]
        ],
        "scenarios": [clip(row) for row in list(packet.get("scenarios", []))[:3]],
        "thesis_financial_bridges": [
            clip(row)
            for row in list(packet.get("thesis_financial_bridges", []))[:8]
        ],
        "moat_evidence_tests": [
            clip(row) for row in list(packet.get("moat_evidence_tests", []))[:10]
        ],
        "valuation_buckets": [
            clip(row) for row in list(packet.get("valuation_buckets", []))[:12]
        ],
        "valuation_closure": clip(dict(packet.get("valuation_closure", {}))),
        "llm_analysis_layer": clip(dict(packet.get("llm_analysis_layer", {}))),
        "handoff_manifest": clip(dict(packet.get("handoff_manifest", {}))),
        "evidence_change_rules": [
            clip(row) for row in list(packet.get("evidence_change_rules", []))[:16]
        ],
        "reconciliation_checks": clip(packet.get("reconciliation_checks", [])),
    }
