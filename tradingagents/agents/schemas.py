"""Pydantic schemas used by agents that produce structured output.

The framework's primary artifact is still prose: each agent's natural-language
reasoning is what users read in the saved markdown reports and what the
downstream agents read as context.  Structured output is layered onto the
three decision-making agents (Research Manager, Trader, Portfolio Manager)
so that:

- Their outputs follow consistent section headers across runs and providers
- Each provider's native structured-output mode is used (json_schema for
  OpenAI/xAI, response_schema for Gemini, tool-use for Anthropic)
- Schema field descriptions become the model's output instructions, freeing
  the prompt body to focus on context and the rating-scale guidance
- A render helper turns the parsed Pydantic instance back into the same
  markdown shape the rest of the system already consumes, so display,
  memory log, and saved reports keep working unchanged
"""

from __future__ import annotations

from enum import Enum
import re
from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------------------------
# Shared rating types
# ---------------------------------------------------------------------------


class PortfolioRating(str, Enum):
    """5-tier rating used by the Research Manager and Portfolio Manager."""

    BUY = "Buy"
    OVERWEIGHT = "Overweight"
    HOLD = "Hold"
    UNDERWEIGHT = "Underweight"
    SELL = "Sell"


class TraderAction(str, Enum):
    """3-tier transaction direction used by the Trader.

    The Trader's job is to translate the Research Manager's investment plan
    into a concrete transaction proposal: should the desk execute a Buy, a
    Sell, or sit on Hold this round.  Position sizing and the nuanced
    Overweight / Underweight calls happen later at the Portfolio Manager.
    """

    BUY = "Buy"
    HOLD = "Hold"
    SELL = "Sell"


class CanonicalModelLine(BaseModel):
    """One machine-comparable model value carried across agent boundaries."""

    line_id: str = Field(description="Stable id such as shares, 2026E_revenue or base_fair_value.")
    period: str = Field(description="Reported or forecast period, for example 2026E.")
    metric: str = Field(description="Canonical metric name, not a prose alias.")
    value: float | None = Field(description="Numeric value; null only when explicitly unresolved.")
    unit: str = Field(description="Exact unit, for example CNY mn, CNY/share, %, or mn shares.")
    status: Literal["reported", "calculated", "estimated", "missing"] = Field(
        description="Evidence status of this value."
    )
    evidence_ids: list[str] = Field(
        default_factory=list,
        description="Traceable EV/KPE/KF evidence ids; estimates cite their input ids.",
    )
    formula: str = Field(default="", description="Reproducible formula when calculated or estimated.")


class ModelHandoffChange(BaseModel):
    """Explicit, auditable revision to a canonical model line."""

    line_id: str
    old_value: float | None
    new_value: float | None
    unit: str
    evidence_ids: list[str] = Field(default_factory=list)
    reason: str
    eps_fcf_valuation_impact: str
    disposition: Literal["accepted", "rejected", "unchanged", "unresolved"]

    @field_validator("old_value", "new_value", mode="before")
    @classmethod
    def normalize_unresolved_non_numeric_value(cls, value):
        """Keep rating/unknown labels from invalidating a numeric ledger."""
        if isinstance(value, str):
            cleaned = value.strip().lower()
            if cleaned in {
                "buy", "overweight", "hold", "underweight", "sell",
                "n/a", "na", "none", "null", "unknown", "unresolved", "-", "--",
            }:
                return None
        return value


class ForecastTakeaway(BaseModel):
    """One reader-facing conclusion from the independent forecast."""

    takeaway: str = Field(description="A decisive forecast conclusion, not a table recap.")
    evidence_anchor: str = Field(
        description="The reported history, current evidence, or explicit model fact supporting it."
    )
    financial_implication: str = Field(
        description="Transmission to revenue, margin, earnings, cash/capital, or valuation."
    )
    confidence_and_risk: str = Field(
        description="Confidence level and the assumption or evidence that could invalidate it."
    )


class ForecastAssumption(BaseModel):
    """Auditable operating assumption; flexible across A-share business models."""

    parameter: str
    affected_business: str = Field(
        description="Segment, product, geography, customer, project/asset, or group line affected."
    )
    historical_anchor: str = Field(
        description="Reported historical level/range and period, or explicitly 'not disclosed'."
    )
    evidence_status: Literal[
        "reported", "calculated", "proxy", "analyst_estimate", "missing"
    ]
    base_case: str = Field(description="Base value or bounded range with period and unit.")
    bull_case: str = Field(description="Bull value/range and the condition required.")
    bear_case: str = Field(description="Bear value/range and the condition required.")
    rationale_and_evidence: str = Field(
        description="Why this assumption is selected and the evidence ids or source period."
    )
    sensitivity: str = Field(
        description="Auditable impact on revenue, profit/EPS, FCF/capital, or fair value."
    )
    confidence: Literal["high", "medium", "low"]
    verification_gate: str = Field(
        description="Dated disclosure or observable data that will confirm or falsify the assumption."
    )

    @field_validator("evidence_status", mode="before")
    @classmethod
    def normalize_evidence_status(cls, value):
        aliases = {
            "estimated": "analyst_estimate",
            "estimate": "analyst_estimate",
            "analyst estimate": "analyst_estimate",
            "analyst-estimate": "analyst_estimate",
            "not disclosed": "missing",
            "unavailable": "missing",
            "unverified": "proxy",
        }
        key = str(value or "").strip().lower()
        return aliases.get(key, value)


class InvestmentThesisCard(BaseModel):
    """One ranked investment conclusion with a complete evidence-to-value loop."""

    rank: int = Field(ge=1, le=6)
    takeaway: str = Field(description="One sentence stating the investment conclusion.")
    decisive_question: str = Field(description="The company-specific question this thesis answers.")
    evidence: str = Field(description="Dated reported/calculated evidence and evidence ids.")
    strongest_counterevidence: str = Field(
        description="The strongest observed contradiction, not a generic risk list."
    )
    financial_transmission: str = Field(
        description="Driver/formula to revenue, margin, profit/EPS, cash/capital, and value."
    )
    market_pricing: str = Field(
        description="What current price appears to imply and whether the thesis is already priced."
    )
    falsification_gate: str = Field(
        description="Observable threshold and period that would reject or materially weaken the thesis."
    )
    verdict: Literal["proven", "partial", "unproven", "rejected"]


class SegmentEconomicsRow(BaseModel):
    """One material economic unit in the public company map."""

    business_unit: str
    economic_role: str = Field(description="Mature core, growth engine, asset/cash unit, or optionality.")
    disclosure_basis: Literal["reported", "calculated", "analyst_estimate", "missing"]
    scale_and_growth: str = Field(description="Revenue/weight/growth with period, or explicitly not disclosed.")
    margin_and_cash: str = Field(description="Margin, cash conversion and capital intensity with disclosure limits.")
    driver_equation: str = Field(description="Industry-native volume/price/mix/cost or asset equation.")
    valuation_treatment: Literal["core", "scenario", "optionality", "excluded"]
    evidence_ids: list[str] = Field(default_factory=list)
    missing_or_next_check: str = ""


class BusinessModelMechanismRow(BaseModel):
    """A reader-facing link in how the company creates and realizes value."""

    link: str = Field(description="Customer/value proposition/order/pricing/delivery/service/cash link.")
    how_it_works: str
    economic_driver: str = Field(description="Volume, price, mix, cost, utilization, service or repeat-purchase mechanism.")
    cash_and_capital_feature: str
    evidence_or_gap: str
    analyst_conclusion: str = Field(description="What this mechanism means for quality, growth or risk; no valuation multiple.")


class MoatMechanismRow(BaseModel):
    """One claimed moat tested through observable economic outcomes."""

    moat_source: str
    operating_mechanism: str = Field(description="Why a customer pays, stays, switches less, or accepts the company's product.")
    observed_proof: str = Field(description="Dated history or true-peer evidence, not awards or slogans.")
    economic_result: str = Field(description="Share, win rate, ASP, margin, turnover, cash conversion or ROIC consequence.")
    durability_and_threat: str
    verdict: Literal["proven", "partial", "unproven", "eroding"]


class IndustryDriverRow(BaseModel):
    """Sector-native driver with an explicit financial transmission."""

    driver: str
    current_state_and_direction: str
    dated_evidence: str
    affected_business: str
    financial_transmission: str
    confidence: Literal["high", "medium", "low"]
    next_verification: str


class AccountingQualityRow(BaseModel):
    """One accounting/capital-allocation issue tied to value creation."""

    item: str
    latest_evidence_and_period: str
    trend_or_comparator: str
    causal_interpretation: str
    earnings_cash_roic_effect: str
    verdict: Literal["positive", "neutral", "warning", "negative", "missing"]
    evidence_ids: list[str] = Field(default_factory=list)


class AlternativeIntelligenceDecision(BaseModel):
    """Auditable use or rejection of one deduplicated Knowledge Planet claim."""

    kpe_ids: list[str] = Field(description="One or more deduplicated KPE ids supporting the same claim.")
    claim: str = Field(description="Concrete claim from full topic text, not a truncated title.")
    source_type: Literal["channel_check", "company_research", "industry_data", "sell_side_view", "policy", "rumor", "other"]
    affected_business_and_variable: str
    public_crosscheck: str = Field(description="Official/public corroboration, contradiction, or not verified.")
    evidence_grade: Literal["A_verified", "B_private_edge", "C_market_narrative", "D_reject"]
    disposition: Literal["model_change", "probability_change", "verification_change", "rejected"]
    before_after: str = Field(description="Numeric model/probability before->after, changed clock/gate, or rejection reason.")
    report_use: str = Field(description="Exact public chapter and thesis affected.")
    falsification_or_next_check: str
    freshness_and_shelf_life: str = Field(
        default="",
        description="Age as of report date and how long the channel/industry/valuation clue remains decision-useful.",
    )

    @field_validator("source_type", mode="before")
    @classmethod
    def normalize_source_type(cls, value: object) -> str:
        """Map upstream Knowledge Planet classes into the public PM taxonomy."""
        normalized = str(value or "other").strip().lower()
        aliases = {
            "industry_weekly_data": "industry_data",
            "industry_data_snippet": "industry_data",
            "broker_survey_data": "industry_data",
            "company_research_feedback": "company_research",
            "expert_call": "company_research",
            "sell_side_push": "sell_side_view",
            "strategy_view": "sell_side_view",
            "broker_report_summary": "sell_side_view",
            "unverified_rumor": "rumor",
            "raw_note": "other",
        }
        return aliases.get(normalized, normalized)


class SellSideExpectationRow(BaseModel):
    """One broker observation reconciled against the independent model."""

    source_ids: list[str] = Field(description="KSI ids and supporting KPE ids.")
    institution: str
    published_at: str
    observation_type: Literal["single_broker", "multi_broker_range", "verified_consensus"] = "single_broker"
    forecast_and_valuation: str = Field(description="Period-specific forecast, method, multiple and target price; mark missing fields.")
    revision_or_dispersion: str = Field(description="Change versus the same institution's prior view or dispersion across institutions.")
    comparison_with_our_model: str = Field(description="Exact variable, period and magnitude difference versus TradingAgents.")
    evidence_status: Literal["public_verified", "private_text", "partial", "stale", "rejected"]
    decision_use: str = Field(description="Forecast, valuation, scenario probability, verification, or rejection outcome.")


class ValuationScenarioInput(BaseModel):
    """LLM-selected assumptions; all valuation outputs are calculated in code."""

    scenario: Literal["bull", "base", "bear"]
    probability_pct: float = Field(ge=0, le=100)
    valuation_method: Literal["PE", "direct_equity_value"] = "PE"
    parent_net_profit_cny_mn: float | None = Field(default=None, ge=0)
    valuation_multiple: float | None = Field(default=None, ge=0)
    direct_equity_value_cny_mn: float | None = Field(default=None, ge=0)
    assumption_summary: str
    evidence_ids: list[str] = Field(default_factory=list)


class OptionalityValuationInput(BaseModel):
    """One explicitly modelled second-curve value bucket."""

    name: str
    metric_name: str = Field(description="Revenue, profit, asset value or direct equity value.")
    metric_value_cny_mn: float = Field(ge=0)
    valuation_multiple: float = Field(default=1.0, ge=0)
    probability_pct: float = Field(default=100.0, ge=0, le=100)
    ownership_pct: float = Field(default=100.0, ge=0, le=100)
    execution_haircut_pct: float = Field(default=0.0, ge=0, le=100)
    evidence_ids: list[str] = Field(default_factory=list)
    assumption_summary: str = ""


class SafeValuationAssumptions(BaseModel):
    """PM risk/return requirements used by the deterministic safety-price engine."""

    current_price_cny: float | None = Field(default=None, ge=0)
    required_annual_return_pct: float = Field(default=20.0, ge=0, le=100)
    holding_period_years: float = Field(default=1.0, gt=0, le=10)
    margin_of_safety_pct: float = Field(default=20.0, ge=0, le=80)
    maximum_bear_loss_pct: float = Field(default=15.0, ge=0, lt=100)
    optionality_equity_value_cny_mn: float = Field(default=0.0, ge=0)
    optionality_inputs: list[OptionalityValuationInput] = Field(
        default_factory=list,
        description=(
            "Structured optionality buckets. Application code calculates metric x multiple x probability x "
            "ownership x (1-execution haircut). Probability and haircut must represent distinct risks; do not "
            "apply a 75% haircut as a second copy of a 25% probability. When populated, these rows replace the "
            "legacy aggregate optionality_equity_value_cny_mn input."
        ),
    )
    other_adjustments_equity_value_cny_mn: float = 0.0
    scenarios: list[ValuationScenarioInput] = Field(default_factory=list)


class DeterministicValuationOutput(BaseModel):
    """Calculated output. The LLM must leave this object at defaults."""

    status: Literal["closed", "partial", "unavailable"] = "unavailable"
    diluted_share_count_mn: float | None = None
    scenario_rows: list[dict] = Field(default_factory=list)
    optionality_rows: list[dict] = Field(default_factory=list)
    probability_weighted_core_value_cny: float | None = None
    optionality_per_share_cny: float | None = None
    other_adjustments_per_share_cny: float | None = None
    fair_value_per_share_cny: float | None = None
    expected_return_pct: float | None = None
    required_return_price_cny: float | None = None
    margin_of_safety_price_cny: float | None = None
    bear_loss_constraint_price_cny: float | None = None
    safe_buy_price_ceiling_cny: float | None = None
    suggested_buy_zone_low_cny: float | None = None
    fundamental_floor_cny: float | None = None
    formula_notes: list[str] = Field(default_factory=list)


class ResearchQuestionVerdict(BaseModel):
    """Analyst-style answer to one question that can change the decision."""

    question: str = Field(description="Company-specific underwriting question.")
    why_decisive: str = Field(
        description="Why this question can change earnings, cash/capital, valuation, or rating."
    )
    conclusion: str = Field(
        description="Current evidence-weighted answer; avoid a generic module summary."
    )
    evidence_used: list[str] = Field(
        description="Dated EV/KPE/KF evidence and the relevant result from each source."
    )
    strongest_counterevidence: str = Field(
        description="Strongest observed contradiction or unresolved alternative explanation."
    )
    model_or_valuation_effect: str = Field(
        description="Named forecast line, probability, fair value, or explicit unchanged result."
    )
    confidence: Literal["high", "medium", "low"]
    next_verification: str = Field(
        description="Dated disclosure or observable threshold that can confirm or reject the answer."
    )


class PMEditorialFinding(BaseModel):
    """One company-specific revision request from the sell-side editor."""

    section: Literal[
        "investment_conclusion",
        "company_disaggregation",
        "industry_cycle_and_competition",
        "three_year_forecast",
        "thesis_moat_financial_bridge",
        "accounting_and_capital_allocation",
        "valuation_and_expectation_gap",
        "risks_catalysts_verification",
        "cross_section_consistency",
    ]
    priority: Literal["must_revise", "should_revise", "optional"]
    issue: str
    evidence_or_logic_gap: str
    revision_instruction: str


class SellSideEditorialReview(BaseModel):
    """LLM research-editor judgment; advisory and revision-driving, not a hard gate."""

    revision_required: bool = Field(
        description=(
            "True when one or more sections need substantive revision before the memo is useful. "
            "Do not require revision for style preference or missing unavailable data alone."
        )
    )
    company_understanding_score: int = Field(ge=1, le=5)
    independent_model_score: int = Field(ge=1, le=5)
    evidence_and_counterevidence_score: int = Field(ge=1, le=5)
    valuation_closure_score: int = Field(ge=1, le=5)
    readability_and_synthesis_score: int = Field(ge=1, le=5)
    strongest_aspects: list[str] = Field(default_factory=list)
    findings: list[PMEditorialFinding] = Field(default_factory=list)
    overall_editorial_verdict: str


# ---------------------------------------------------------------------------
# Research Manager
# ---------------------------------------------------------------------------


class UnderwritingResearchPlan(BaseModel):
    """Compact model-referee handoff from research debate to PM/Trader."""

    recommendation: PortfolioRating = Field(
        description=(
            "Provisional research recommendation derived only after reconciling the "
            "shared three-year underwriting model and scenario expected value."
        )
    )
    research_readiness: Literal["ready", "partial", "blocked"] = Field(
        description="Readiness of the accepted underwriting model after debate."
    )
    core_bet: str = Field(
        default="Not supplied; derive from the accepted underwriting model.",
        description="The few operating variables that decide the investment outcome."
    )
    research_questions: list[str] = Field(
        default_factory=list,
        description=(
            "The 3-5 company-specific questions that decide earnings, cash/capital and valuation. "
            "They organize the model and debate; do not list generic checklist topics."
        ),
    )
    question_verdicts: list[ResearchQuestionVerdict] = Field(
        default_factory=list,
        description=(
            "Evidence-weighted answers to the 3-5 decisive research questions. Each answer must "
            "synthesize multiple relevant sources, the strongest conflict, and the exact model effect."
        ),
    )
    forecast_takeaways: list[ForecastTakeaway] = Field(
        default_factory=list,
        description="Two or three post-debate forecast conclusions for the reader.",
    )
    forecast_assumptions: list[ForecastAssumption] = Field(
        default_factory=list,
        description=(
            "The small set of assumptions responsible for most forecast variance. Missing industry-native "
            "data must remain missing or use an explicitly top-down bounded assumption."
        ),
    )
    core_theses: list[InvestmentThesisCard] = Field(
        default_factory=list,
        description="Two to four ranked theses that close evidence, counterevidence, finance and pricing.",
    )
    company_disaggregation: str = Field(
        description=(
            "Post-debate economic unit map. Separate filing segments from the product, "
            "channel, geography, customer, project/asset or financial-business units that "
            "actually drive economics. Carry reported scale/margin/cash metrics and mark "
            "analytical or missing cells explicitly."
        )
    )
    autonomous_forecast_model: str = Field(
        description=(
            "The accepted independent three-year model, built from operating drivers rather "
            "than copied consensus. Reconcile every material unit to industry-native group "
            "earnings, cash/capital, per-share lines and sources."
        )
    )
    thesis_financial_bridge: str = Field(
        description=(
            "Ledger for the 3-6 decisive claims: operating formula, bull/base/bear assumptions, "
            "and revenue/profit/EPS/FCF-or-capital/fair-value impact. Leave unsupported effects missing."
        )
    )
    moat_evidence_verdict: str = Field(
        description=(
            "Evidence tests for every claimed moat versus history and true peers, including "
            "counterevidence and the transmission to share, price, margin, turnover, cash or ROIC."
        )
    )
    valuation_closure: str = Field(
        description=(
            "Mutually exclusive core/scenario/optionality/excluded value buckets, share-count "
            "and probability reconciliation, double-counting checks, current-price expected "
            "return and consistency with the provisional recommendation."
        )
    )
    canonical_model_snapshot: list[CanonicalModelLine] = Field(
        min_length=4,
        description=(
            "Machine-readable accepted source of truth. Include diluted shares and every "
            "three-year consolidated forecast line plus scenario fair values. Copy unchanged "
            "values exactly; any revision must also appear in model_change_rows."
        ),
    )
    model_change_rows: list[ModelHandoffChange] = Field(
        default_factory=list,
        description=(
            "Every difference from the underwriting packet, including unit corrections. "
            "Silent changes are prohibited."
        ),
    )
    accepted_underwriting_model: str = Field(
        description=(
            "Detailed Markdown model accepted after the debate. Cover company operating "
            "equations, every material segment causal chain, three forward years of segment "
            "drivers and the model-profile-appropriate consolidated earnings, balance-sheet, "
            "cash/capital and per-share lines, plus bull/base/bear "
            "probabilities and valuation. Use missing/not disclosed rather than invention."
        )
    )
    model_change_ledger: str = Field(
        description=(
            "Markdown ledger: question or forecast line, original assumption, bull proposal, "
            "bear proposal, accepted assumption, evidence ids, EPS/FCF/value impact and next check."
        )
    )
    debate_verdict: str = Field(
        description=(
            "Explain which side improved the model on each decisive question and why, without "
            "turning the result into a rhetorical winner/loser recap."
        )
    )
    probability_payoff: str = Field(
        description=(
            "Reconciled bull/base/bear probability, fair value, expected value, downside and "
            "the operating assumptions responsible for the distribution."
        )
    )
    unresolved_questions_and_gaps: str = Field(
        description=(
            "Company-specific unresolved questions, missing model cells, conflicting evidence, "
            "and the exact disclosure or operating data required."
        )
    )
    handoff_to_pm_and_trader: str = Field(
        description=(
            "Concise handoff: accepted model version, position constraints, catalysts, "
            "falsification and what the PM must not assume beyond the model."
        )
    )
    handoff_integrity_audit: str = Field(
        description=(
            "Loss-prevention manifest: model version; frozen reported facts; accepted estimates; "
            "unresolved cells; and every business unit, forecast line, financial bridge and "
            "valuation bucket the PM must preserve or explicitly revise."
        )
    )


class ResearchPlan(BaseModel):
    """Structured investment plan produced by the Research Manager.

    Hand-off to the Trader: the recommendation pins the directional view,
    the rationale captures which side of the bull/bear debate carried the
    argument, and the strategic actions translate that into concrete
    instructions the trader can execute against.
    """

    recommendation: PortfolioRating = Field(
        description=(
            "The investment recommendation. Exactly one of Buy / Overweight / "
            "Hold / Underweight / Sell. Reserve Hold for situations where there "
            "is no clear tradable thesis, the expectation gap is weak, or the "
            "probability/payoff is not attractive; otherwise commit to a "
            "directional stance with calibrated conviction."
        ),
    )
    core_bet: str = Field(
        default="Not supplied; derive from the accepted underwriting model.",
        description=(
            "One or two sentences stating the core bet: what future business, "
            "cycle, policy, product-price, demand, cost, or valuation variable "
            "the investor is underwriting."
        ),
    )
    expectation_gap: str = Field(
        default="Not supplied; compare the model with market-implied expectations.",
        description=(
            "Explain whether the market appears to have priced the thesis, or "
            "where a plausible expectation gap remains. Mention evidence and caveats."
        ),
    )
    probability_payoff: str = Field(
        default="Not supplied; complete bull/base/bear probabilities and payoff.",
        description=(
            "Summarize probability and payoff: likelihood of the core bet, upside "
            "if it works, downside if it fails, and why the rating follows."
        ),
    )
    cycle_valuation_assessment: str = Field(
        default="Not supplied; reconcile prosperity, valuation and cash returns.",
        description=(
            "Classify the valuation x prosperity setup and explain the fair "
            "calibration: low/high valuation versus low/high prosperity, why the "
            "setup deserves the recommendation, and what would change it."
        ),
    )
    catalyst_path: str = Field(
        default="Not supplied; identify dated model-changing events.",
        description=(
            "Near- to medium-term events or data releases that could make the "
            "market reprice the thesis."
        ),
    )
    falsification_signals: str = Field(
        default="Not supplied; define model-variable falsification gates.",
        description=(
            "Specific signals that would prove the thesis wrong or require a "
            "rating downgrade."
        ),
    )
    conviction_level: str = Field(
        default="Low until the shared underwriting model is complete.",
        description=(
            "Conviction level and why: High / Medium / Low, tied to evidence "
            "quality, data gaps, and probability/payoff."
        ),
    )
    rationale: str = Field(
        description=(
            "Detailed informative discussion of the bull/bear debate. Name the "
            "bull's core bet, the bear's core bet, which evidence carries more "
            "weight, which claims are unverified, and why the final recommendation "
            "follows. This should read like an investment committee chair's "
            "reasoned ruling, not a short recap."
        ),
    )
    question_led_debate_audit: Optional[str] = Field(
        default=None,
        description=(
            "Mandatory when financial-report intelligence supplies Pre-Debate "
            "Underwriting Questions. Write a compact investment-committee issue "
            "log for the 4-7 questions that can change rating, valuation, sizing, "
            "or next verification. Prefer a markdown table with columns such as "
            "question, initial skepticism, bull answer, bear attack, evidence "
            "verdict, valuation/sizing impact, and next verification. Preserve "
            "question IDs or short labels when available, and explicitly mark any "
            "unanswered thesis-critical question as a research gap."
        ),
    )
    strategic_actions: str = Field(
        description=(
            "Concrete steps for the trader to implement the recommendation, "
            "including position sizing guidance consistent with the rating."
        ),
    )
    prior_rating: Optional[str] = Field(
        default=None,
        description=(
            "If a recent same-ticker decision exists, state its rating exactly; "
            "otherwise omit."
        ),
    )
    new_evidence_since_prior: Optional[str] = Field(
        default=None,
        description=(
            "List the decisive new evidence since the most recent same-ticker "
            "decision. If there is no decisive new evidence, say so explicitly."
        ),
    )
    unchanged_core_facts: Optional[str] = Field(
        default=None,
        description=(
            "Summarize the thesis-critical facts that remain unchanged versus the "
            "most recent same-ticker decision."
        ),
    )
    rating_change_audit: Optional[str] = Field(
        default=None,
        description=(
            "Explain why the recommendation was preserved or changed relative to "
            "the prior same-ticker decision. A price move alone is not enough for "
            "a directional reversal."
        ),
    )
    material_catalysts: Optional[str] = Field(
        default=None,
        description=(
            "List only verified material catalysts that pass the four-gate test: "
            "verifiable evidence, economic transmission, timetable, and materiality. "
            "Classify each as asset-revaluation or business-realization."
        ),
    )
    thematic_valuation_bridge: Optional[str] = Field(
        default=None,
        description=(
            "Explain how each verified theme does or does not enter valuation. "
            "For asset-revaluation themes, discuss ownership value, listed-company "
            "materiality, and whether SOTP/NAV treatment is justified. For "
            "business-realization themes, state whether disclosed monetization "
            "evidence is strong enough for scenario or core valuation."
        ),
    )
    rejected_themes: Optional[str] = Field(
        default=None,
        description=(
            "List thematic claims reviewed but rejected from valuation because "
            "they lack primary-source verification, economic transmission, "
            "timetable, or materiality."
        ),
    )
    peer_selection_verdict: Optional[str] = Field(
        default=None,
        description=(
            "State whether the target is the best same-industry build candidate, "
            "merely acceptable, or inferior to one or more peers. If a peer is "
            "better, name it and explain the concrete valuation, quality, growth, "
            "leverage, cash, or operating reasons plus the key caveat."
        ),
    )
    supply_chain_position_verdict: Optional[str] = Field(
        default=None,
        description=(
            "When a curated industrial-chain comparison exists, state whether the "
            "target's own segment is the best place in the chain to build exposure "
            "now or whether another chain position offers a better profit pool. "
            "Explain why in terms of economics, valuation, pricing power, earnings "
            "revision potential, or balance-sheet quality."
        ),
    )
    earnings_model_bridge: Optional[str] = Field(
        default=None,
        description=(
            "Summarize the earnings bridge that connects the thesis to revenue, "
            "margin, profit, cash generation, and valuation under bull/base/bear "
            "cases. Name the decisive modeled levers."
        ),
    )
    market_implied_expectation: Optional[str] = Field(
        default=None,
        description=(
            "State what the current quote appears to imply about earnings power, "
            "sales scale, growth persistence, or margin durability, and where the "
            "research view differs from that market expectation."
        ),
    )
    company_quality_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Answer only whether this is a good business / good company, based on "
            "moat, profitability, cash quality, balance sheet, management, and "
            "durability rather than share price."
        ),
    )
    current_odds_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Answer only whether today's price offers attractive expected value, "
            "based on valuation, implied expectations, catalysts, downside, and "
            "probability/payoff."
        ),
    )
    relative_allocation_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Answer only whether this is the best current place to deploy capital "
            "relative to same-industry peers and alternative chain positions."
        ),
    )
    management_capital_allocation_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Judge stewardship from hard evidence: management alignment, capital "
            "returns, capex discipline, financing, buybacks/dividends, M&A, and "
            "whether capital allocation has compounded or diluted value."
        ),
    )
    shareholder_structure_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Judge ownership and chip structure: concentration, holder-count trend, "
            "insider increases/decreases, pledge, unlocks, and whether these create "
            "stability or supply overhang."
        ),
    )
    investor_communication_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Judge official investor communication: recurring investor concerns, "
            "substantiveness of management answers, disclosure quality, and whether "
            "the answer pattern raises or lowers thesis confidence."
        ),
    )
    policy_direction_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Judge whether official national or industry policy strengthens the "
            "company's demand lane, how directly it reaches the firm's economics, "
            "and what bridge evidence remains missing."
        ),
    )
    industry_driver_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Judge the sector-native variables that truly decide the thesis, using "
            "the filing industry reading pack and outside confirmation or contradiction."
        ),
    )
    business_segment_valuation_verdict: Optional[str] = Field(
        default=None,
        description=(
            "If filing evidence supports a segment or SOTP view, split the mature "
            "core, emerging second curves, channels, geographies, and optionality. "
            "Explain which parts deserve core valuation, scenario valuation, or no "
            "valuation credit because revenue, margin, capex, customers, or cash "
            "conversion are missing."
        ),
    )
    commodity_cycle_verdict: Optional[str] = Field(
        default=None,
        description=(
            "For commodity, product-price, spread, channel-price, or other cycle "
            "variables, state whether verified price evidence supports or "
            "contradicts the revenue, margin, inventory, or EPS thesis. If missing, "
            "say exactly how that limits confidence."
        ),
    )
    baijiu_channel_verification_verdict: Optional[str] = Field(
        default=None,
        description=(
            "For baijiu/liquor targets only. Separate wholesale price evidence, "
            "channel inventory/payment quality, contract-liability seasonality, "
            "product mix, peer-basket comparison, and missing data. If not a "
            "baijiu target, omit."
        ),
    )
    compute_leasing_verification_verdict: Optional[str] = Field(
        default=None,
        description=(
            "For compute-leasing targets only. Separate legacy business value, "
            "verified compute-leasing revenue/value, unverified optionality, "
            "unit-economics gaps, capex/funding risk, customer contract quality, "
            "and transition credibility. If not applicable, omit."
        ),
    )
    dividend_defensive_verdict: Optional[str] = Field(
        default=None,
        description=(
            "For defensive/high-dividend targets only. Decide whether this is a "
            "true defensive dividend candidate, a dividend-trap risk, inferior to "
            "peer alternatives, or only a partial defensive sleeve. If not "
            "applicable, omit."
        ),
    )
    strategic_optionality_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Summarize important but non-base-case optionality such as second growth "
            "curves, investee holdings, asset revaluation, or thematic catalysts, "
            "including why they matter and what would upgrade them."
        ),
    )
    evidence_gap_confidence_cap: Optional[str] = Field(
        default=None,
        description=(
            "State the thesis-critical missing or partial evidence, distinguish "
            "neutral absence from adverse evidence, identify the affected model cell, "
            "and specify the exact retrieval task. Missing data must not mechanically "
            "change rating, position size, or conviction tier."
        ),
    )
    data_coverage_audit: Optional[str] = Field(
        default=None,
        description=(
            "Summarize which supplied data modules were ready, partial, failed, or "
            "missing. Name thesis-critical gaps and retrieval tasks, while keeping "
            "absence neutral and separate from the recommendation."
        ),
    )


def _render_canonical_model_table(lines: list[CanonicalModelLine]) -> str:
    rows = [
        "| line_id | period | metric | value | unit | status | evidence/formula |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for line in lines:
        value = "missing" if line.value is None else f"{line.value:.8g}"
        lineage = ", ".join(line.evidence_ids) or line.formula or "unresolved"
        rows.append(
            f"| {line.line_id} | {line.period} | {line.metric} | {value} | "
            f"{line.unit} | {line.status} | {lineage} |"
        )
    return "\n".join(rows)


def _render_model_change_table(rows_in: list[ModelHandoffChange]) -> str:
    if not rows_in:
        return "No numeric or unit changes; canonical snapshot preserved exactly."
    rows = [
        "| line_id | old | new | unit | evidence | reason | impact | disposition |",
        "| --- | ---: | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows_in:
        old = "missing" if row.old_value is None else f"{row.old_value:.8g}"
        new = "missing" if row.new_value is None else f"{row.new_value:.8g}"
        rows.append(
            f"| {row.line_id} | {old} | {new} | {row.unit} | "
            f"{', '.join(row.evidence_ids) or 'none'} | {row.reason} | "
            f"{row.eps_fcf_valuation_impact} | {row.disposition} |"
        )
    return "\n".join(rows)


def _demote_embedded_headings(text: str) -> str:
    """Keep model-authored subheads from breaking the fixed public H2 contract."""
    return re.sub(r"(?m)^#{1,6}\s+", "### ", str(text or "").strip())


def _render_research_questions(questions: list[str]) -> str:
    if not questions:
        return ""
    rows = ["### 本报告要回答的关键问题", ""]
    rows.extend(f"{index}. {question}" for index, question in enumerate(questions[:5], 1))
    return "\n".join(rows)


def _render_question_verdicts(items: list[ResearchQuestionVerdict]) -> str:
    if not items:
        return ""
    rows = ["### 核心问题裁决", ""]
    for index, item in enumerate(items[:5], 1):
        evidence = "；".join(item.evidence_used[:6]) or "未形成可用证据"
        rows.extend(
            [
                f"**Q{index}：{item.question}**",
                f"- **为何关键：** {item.why_decisive}",
                f"- **当前结论：** {item.conclusion}",
                f"- **采用证据：** {evidence}",
                f"- **最强反证：** {item.strongest_counterevidence}",
                f"- **模型/估值影响：** {item.model_or_valuation_effect}",
                f"- **置信度与下次验证：** {item.confidence}；{item.next_verification}",
                "",
            ]
        )
    return "\n".join(rows).rstrip()


def _render_forecast_takeaways(items: list[ForecastTakeaway]) -> str:
    if not items:
        return "### 预测结论\n\n- 暂无结构化take-away；以模型解释与风险披露为准。"
    rows = ["### 预测take-aways", ""]
    for index, item in enumerate(items[:3], 1):
        rows.extend(
            [
                f"**{index}. {item.takeaway}**",
                f"- 证据锚：{item.evidence_anchor}",
                f"- 财务含义：{item.financial_implication}",
                f"- 置信度与风险：{item.confidence_and_risk}",
                "",
            ]
        )
    return "\n".join(rows).rstrip()


def _canonical_metric_name(metric: str) -> str:
    raw = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", str(metric or "").lower())
    aliases = {
        "consolidatedrevenue": "revenue", "revenue": "revenue", "营业收入": "revenue",
        "costofsales": "cost_of_sales", "consolidatedcostofsales": "cost_of_sales", "营业成本": "cost_of_sales",
        "consolidatedgrossmargin": "gross_margin", "grossmargin": "gross_margin", "毛利率": "gross_margin",
        "grossprofit": "gross_profit", "consolidatedgrossprofit": "gross_profit", "毛利润": "gross_profit",
        "operatingprofit": "operating_profit", "consolidatedoperatingprofit": "operating_profit", "营业利润": "operating_profit",
        "operatingmargin": "operating_margin", "consolidatedoperatingmargin": "operating_margin", "营业利润率": "operating_margin",
        "financeandotheritems": "finance_other", "financeotheritems": "finance_other", "财务及其他项目": "finance_other",
        "pretaxprofit": "pretax_profit", "profittotal": "pretax_profit", "利润总额": "pretax_profit",
        "incometax": "income_tax", "incometaxexpense": "income_tax", "所得税": "income_tax",
        "minorityinterest": "minority_interest", "minorityinterests": "minority_interest", "少数股东损益": "minority_interest",
        "parentnetprofit": "parent_profit", "consolidatedparentnetprofit": "parent_profit", "归母净利润": "parent_profit",
        "netmargin": "net_margin", "consolidatednetmargin": "net_margin", "净利率": "net_margin",
        "eps": "eps", "epsbasic": "eps", "dilutedeps": "eps", "每股收益": "eps",
        "operatingcashflow": "ocf", "ocf": "ocf", "经营活动现金流净额": "ocf",
        "capitalexpenditure": "capex", "capex": "capex", "资本开支": "capex",
        "freecashflow": "fcf", "fcf": "fcf", "自由现金流": "fcf",
    }
    aliases.update(
        {
            "经营现金流": "ocf",
            "经营现金流ocf": "ocf",
            "经营活动现金流": "ocf",
            "资本开支": "capex",
            "资本性支出": "capex",
            "自由现金流": "fcf",
        }
    )
    return aliases.get(raw, raw)


def _display_number(value: float | None) -> str:
    if value is None:
        return "—"
    if abs(value) >= 1000:
        return f"{value:,.0f}"
    return f"{value:,.2f}".rstrip("0").rstrip(".")


def _render_reader_forecast_table(lines: list[CanonicalModelLine]) -> str:
    labels = {
        "revenue": "营业收入", "cost_of_sales": "营业成本", "gross_margin": "毛利率", "gross_profit": "毛利润",
        "operating_profit": "营业利润", "operating_margin": "营业利润率",
        "parent_profit": "归母净利润", "net_margin": "净利率", "eps": "EPS",
        "ocf": "经营现金流", "capex": "资本开支", "fcf": "自由现金流",
    }
    order = list(labels)
    data: dict[str, dict[str, CanonicalModelLine]] = {}
    periods: list[str] = []
    for line in lines:
        metric = _canonical_metric_name(line.metric)
        period = str(line.period)
        if metric not in labels or not re.search(r"(?:A|E)$", period, re.I):
            continue
        data.setdefault(metric, {})[period] = line
        if period not in periods:
            periods.append(period)
    periods.sort(key=lambda value: (re.sub(r"\D", "", value), value))
    if not periods or not data:
        return "### 三年财务预测\n\n暂无可可靠展示的标准化预测行。"
    rows = [
        "### 三年财务预测",
        "",
        "| 指标 | 单位 | " + " | ".join(periods) + " |",
        "| --- | --- | " + " | ".join("---:" for _ in periods) + " |",
    ]
    for metric in order:
        metric_rows = data.get(metric)
        if not metric_rows:
            continue
        exemplar = next(iter(metric_rows.values()))
        values = [
            _display_number(metric_rows[period].value) if period in metric_rows else "—"
            for period in periods
        ]
        rows.append(
            f"| {labels[metric]} | {exemplar.unit} | " + " | ".join(values) + " |"
        )
    return "\n".join(rows)


def _render_forecast_assumptions(items: list[ForecastAssumption]) -> str:
    if not items:
        return "### 核心假设与敏感性\n\n尚未形成结构化参数台账；不得将缺失参数表述为已验证。"
    rows = [
        "### 核心假设与敏感性",
        "",
        "| 参数/业务 | 历史锚与证据状态 | Bear / Base / Bull | 敏感度 | 置信度与验证门槛 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in items[:10]:
        anchor = f"{item.historical_anchor}；{item.evidence_status}"
        cases = f"{item.bear_case} / {item.base_case} / {item.bull_case}"
        gate = f"{item.confidence}；{item.verification_gate}"
        rows.append(
            f"| {item.parameter}（{item.affected_business}） | {anchor} | {cases} | "
            f"{item.sensitivity} | {gate} |"
        )
    return "\n".join(rows)


def _render_thesis_cards(items: list[InvestmentThesisCard]) -> str:
    rows: list[str] = []
    for item in sorted(items, key=lambda value: value.rank)[:4]:
        rows.extend(
            [
                f"### 论点{item.rank}：{item.takeaway}",
                "",
                f"- **关键问题：** {item.decisive_question}",
                f"- **核心证据：** {item.evidence}",
                f"- **最强反证：** {item.strongest_counterevidence}",
                f"- **财务传导：** {item.financial_transmission}",
                f"- **市场定价：** {item.market_pricing}",
                f"- **证伪条件：** {item.falsification_gate}",
                f"- **当前裁决：** {item.verdict}",
                "",
            ]
        )
    return "\n".join(rows).rstrip()


def render_underwriting_research_plan(plan: UnderwritingResearchPlan) -> str:
    """Render one reconciled model-referee handoff without optional-field sprawl."""
    if isinstance(plan, ResearchPlan):
        return render_research_plan(plan)
    return "\n\n".join(
        [
            "# Research Manager Accepted Underwriting Model",
            f"**Rating**: {plan.recommendation.value}",
            f"**Research Readiness**: {plan.research_readiness}",
            f"**Core Bet**: {plan.core_bet}",
            _render_research_questions(plan.research_questions),
            _render_question_verdicts(plan.question_verdicts),
            "## Forecast Takeaways\n\n" + _render_forecast_takeaways(plan.forecast_takeaways),
            "## Forecast Assumption Registry\n\n" + _render_forecast_assumptions(plan.forecast_assumptions),
            "## Ranked Core Theses\n\n" + (
                _render_thesis_cards(plan.core_theses)
                if plan.core_theses
                else "No structured thesis cards supplied."
            ),
            "## Company Disaggregation\n\n" + plan.company_disaggregation.strip(),
            "## Autonomous Three-Year Forecast Model\n\n"
            + plan.autonomous_forecast_model.strip(),
            "## Thesis-to-Financial Bridge\n\n" + plan.thesis_financial_bridge.strip(),
            "## Moat Evidence Verdict\n\n" + plan.moat_evidence_verdict.strip(),
            "## Valuation Closure\n\n" + plan.valuation_closure.strip(),
            "## Canonical Model Snapshot\n\n"
            + _render_canonical_model_table(plan.canonical_model_snapshot),
            "## Accepted Underwriting Model\n\n" + plan.accepted_underwriting_model.strip(),
            "## Model Change Ledger\n\n"
            + _render_model_change_table(plan.model_change_rows)
            + "\n\n"
            + plan.model_change_ledger.strip(),
            "## Debate Verdict\n\n" + plan.debate_verdict.strip(),
            "## Probability and Payoff\n\n" + plan.probability_payoff.strip(),
            "## Unresolved Questions and Evidence Gaps\n\n"
            + plan.unresolved_questions_and_gaps.strip(),
            "## Handoff to PM and Trader\n\n" + plan.handoff_to_pm_and_trader.strip(),
            "## Handoff Integrity Audit\n\n" + plan.handoff_integrity_audit.strip(),
        ]
    )


def render_research_plan(plan: ResearchPlan) -> str:
    """Render a ResearchPlan to markdown for storage and the trader's prompt context."""
    parts = [
        "**Investment Decision Memo**",
        "",
        f"**Rating**: {plan.recommendation.value}",
        f"**Recommendation**: {plan.recommendation.value}",
        "",
    ]
    if plan.prior_rating:
        parts.extend(["### Prior Rating", plan.prior_rating])
    if plan.new_evidence_since_prior:
        parts.extend(["", "### New Evidence Since Prior", plan.new_evidence_since_prior])
    if plan.unchanged_core_facts:
        parts.extend(["", "### Unchanged Core Facts", plan.unchanged_core_facts])
    if plan.rating_change_audit:
        parts.extend(["", "### Rating Change Audit", plan.rating_change_audit])
    if plan.company_quality_verdict:
        parts.extend(["", "### Company Quality Verdict", plan.company_quality_verdict])
    if plan.current_odds_verdict:
        parts.extend(["", "### Current Odds Verdict", plan.current_odds_verdict])
    if plan.relative_allocation_verdict:
        parts.extend(["", "### Relative Allocation Verdict", plan.relative_allocation_verdict])
    if plan.material_catalysts:
        parts.extend(["", "### Material Catalysts", plan.material_catalysts])
    if plan.thematic_valuation_bridge:
        parts.extend(["", "### Thematic Valuation Bridge", plan.thematic_valuation_bridge])
    if plan.rejected_themes:
        parts.extend(["", "### Rejected Themes", plan.rejected_themes])
    if plan.peer_selection_verdict:
        parts.extend(["", "### Peer Selection Verdict", plan.peer_selection_verdict])
    if plan.supply_chain_position_verdict:
        parts.extend(["", "### Supply-Chain Position Verdict", plan.supply_chain_position_verdict])
    if plan.earnings_model_bridge:
        parts.extend(["", "### Earnings Model Bridge", plan.earnings_model_bridge])
    if plan.market_implied_expectation:
        parts.extend(["", "### Market-Implied Expectation", plan.market_implied_expectation])
    if plan.management_capital_allocation_verdict:
        parts.extend(["", "### Management & Capital Allocation Verdict", plan.management_capital_allocation_verdict])
    if plan.shareholder_structure_verdict:
        parts.extend(["", "### Shareholder Structure Verdict", plan.shareholder_structure_verdict])
    if plan.investor_communication_verdict:
        parts.extend(["", f"**Investor Communication Verdict**: {plan.investor_communication_verdict}"])
    if plan.policy_direction_verdict:
        parts.extend(["", f"**Policy Direction Verdict**: {plan.policy_direction_verdict}"])
    if plan.industry_driver_verdict:
        parts.extend(["", f"**Industry Driver Verdict**: {plan.industry_driver_verdict}"])
    if plan.business_segment_valuation_verdict:
        parts.extend(["", "### Business Segment Valuation Verdict", plan.business_segment_valuation_verdict])
    if plan.commodity_cycle_verdict:
        parts.extend(["", "### Commodity Cycle Verdict", plan.commodity_cycle_verdict])
    if plan.baijiu_channel_verification_verdict:
        parts.extend(["", "### Baijiu Channel Verification Verdict", plan.baijiu_channel_verification_verdict])
    if plan.compute_leasing_verification_verdict:
        parts.extend(["", "### Compute-Leasing Verification Verdict", plan.compute_leasing_verification_verdict])
    if plan.dividend_defensive_verdict:
        parts.extend(["", "### Dividend Defensive Verdict", plan.dividend_defensive_verdict])
    if plan.strategic_optionality_verdict:
        parts.extend(["", f"**Strategic Optionality Verdict**: {plan.strategic_optionality_verdict}"])
    if plan.evidence_gap_confidence_cap:
        parts.extend(["", "### Evidence Gap And Confidence Cap", plan.evidence_gap_confidence_cap])
    if plan.data_coverage_audit:
        parts.extend(["", "### Data Coverage Audit", plan.data_coverage_audit])
    if plan.question_led_debate_audit:
        parts.extend(["", "### Question-Led Debate Audit", plan.question_led_debate_audit])
    parts.extend(
        [
            "",
            "### Informative Discussion Of The Debate",
            plan.rationale,
            f"**Rationale**: {plan.rationale}",
            "",
            "### Recommendation",
            f"**Core Bet:** {plan.core_bet}",
            "",
            f"**Expectation Gap:** {plan.expectation_gap}",
            "",
            f"**Probability And Payoff:** {plan.probability_payoff}",
            "",
            f"**Cycle-Valuation Assessment:** {plan.cycle_valuation_assessment}",
            "",
            f"**Catalyst Path:** {plan.catalyst_path}",
            "",
            f"**Falsification Signals:** {plan.falsification_signals}",
            "",
            f"**Conviction Level:** {plan.conviction_level}",
            "",
            f"**Strategic Actions:** {plan.strategic_actions}",
            f"**Strategic Actions**: {plan.strategic_actions}",
        ]
    )
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Trader
# ---------------------------------------------------------------------------


class TraderProposal(BaseModel):
    """Structured transaction proposal produced by the Trader.

    The trader reads the Research Manager's investment plan and the analyst
    reports, then turns them into a concrete transaction: what action to
    take, the reasoning that justifies it, and the practical levels for
    entry, stop-loss, and sizing.
    """

    action: TraderAction = Field(
        description="The transaction direction. Exactly one of Buy / Hold / Sell.",
    )
    reasoning: str = Field(
        description=(
            "The case for this action, anchored in the analysts' reports and "
            "the research plan. Two to four sentences."
        ),
    )
    entry_price: Optional[float] = Field(
        default=None,
        description="Optional entry price target in the instrument's quote currency.",
    )
    stop_loss: Optional[float] = Field(
        default=None,
        description="Optional stop-loss price in the instrument's quote currency.",
    )
    profit_taking_range: Optional[str] = Field(
        default=None,
        description=(
            "Optional staged profit-taking or trimming range. Use this when the "
            "view is bullish or the action is Buy/Hold with upside; express as "
            "a price range or scenario range grounded in the research plan."
        ),
    )
    entry_watch_range: Optional[str] = Field(
        default=None,
        description=(
            "Optional entry or re-entry watch range. Use this when the view is "
            "bearish/cautious or action is Sell/Hold; express where risk/reward "
            "may become attractive again."
        ),
    )
    position_sizing: Optional[str] = Field(
        default=None,
        description="Optional sizing guidance, e.g. '5% of portfolio'.",
    )


def render_trader_proposal(proposal: TraderProposal) -> str:
    """Render a TraderProposal to markdown.

    The trailing ``FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**`` line is
    preserved for backward compatibility with the analyst stop-signal text
    and any external code that greps for it.
    """
    parts = [
        f"**Action**: {proposal.action.value}",
        "",
        f"**Reasoning**: {proposal.reasoning}",
    ]
    if proposal.entry_price is not None:
        parts.extend(["", f"**Entry Price**: {proposal.entry_price}"])
    if proposal.stop_loss is not None:
        parts.extend(["", f"**Stop Loss**: {proposal.stop_loss}"])
    if proposal.profit_taking_range:
        parts.extend(["", f"**Profit-Taking / Trimming Range**: {proposal.profit_taking_range}"])
    if proposal.entry_watch_range:
        parts.extend(["", f"**Entry / Re-entry Watch Range**: {proposal.entry_watch_range}"])
    if proposal.position_sizing:
        parts.extend(["", f"**Position Sizing**: {proposal.position_sizing}"])
    parts.extend([
        "",
        f"FINAL TRANSACTION PROPOSAL: **{proposal.action.value.upper()}**",
    ])
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Portfolio Manager
# ---------------------------------------------------------------------------


class SellSidePMDecision(BaseModel):
    """Compact PM schema whose main artifact is one integrated sell-side report.

    The legacy PortfolioDecision remains available for compatibility, but its
    many optional fields encouraged checklist writing and made provider-level
    structured output fragile.  This smaller schema keeps rating metadata
    structured while allowing the report itself to be a coherent long-form
    analytical document built from the shared underwriting packet.
    """

    rating: PortfolioRating = Field(
        description=(
            "Final system rating: Buy, Overweight, Hold, Underweight, or Sell. "
            "It must follow from the reconciled bull/base/bear underwriting model, "
            "not merely from missing evidence or a pending disclosure."
        )
    )
    rating_posture: str = Field(
        description="Concise position posture consistent with the final rating."
    )
    research_readiness: Literal["ready", "partial", "blocked"] = Field(
        description=(
            "Readiness of the shared company-underwriting model. Copy and explain "
            "the underwriting packet status. Partial means disclosed coverage gaps and "
            "does not mechanically alter the investment rating; blocked is reserved for "
            "deterministic fact, unit, period, or arithmetic contradictions."
        )
    )
    one_line_thesis: str = Field(
        description=(
            "One sentence connecting the decisive operating variable, expectation gap, "
            "valuation/payoff and principal caveat."
        )
    )
    research_questions: list[str] = Field(
        default_factory=list,
        description=(
            "Internal planning only: copy/refine the 3-5 company-specific questions that decide the rating. "
            "Use them to direct research, but do not expose them as a public Q&A outline or repeat them in "
            "the reader-facing report. Their conclusions must be synthesized into the relevant chapters."
        ),
    )
    question_verdicts: list[ResearchQuestionVerdict] = Field(
        default_factory=list,
        description=(
            "Internal analytical ledger: three to five evidence-weighted answers to the decisive questions. "
            "Cite the evidence actually used, reconcile the strongest conflicting observation, and state the "
            "named forecast/probability/valuation effect. Do not render this ledger as a public Q&A section; "
            "weave each accepted conclusion into company, industry, thesis, forecast or valuation prose."
        ),
    )
    forecast_takeaways: list[ForecastTakeaway] = Field(
        default_factory=list,
        description=(
            "Two or three decisive forecast conclusions. Each must state evidence, financial implication, "
            "confidence and invalidation risk rather than merely repeat table values."
        ),
    )
    forecast_assumptions: list[ForecastAssumption] = Field(
        default_factory=list,
        description=(
            "Auditable driver registry. Use historical anchors and bull/base/bear ranges. If shipment, ASP, "
            "utilization or another industry-native input is unavailable, label the model top-down and low "
            "confidence instead of inventing bottom-up precision."
        ),
    )
    core_theses: list[InvestmentThesisCard] = Field(
        default_factory=list,
        description=(
            "Two to four ranked investment conclusions. Each closes takeaway -> evidence -> strongest "
            "counterevidence -> financial transmission -> market pricing -> falsification."
        ),
    )
    segment_economics: list[SegmentEconomicsRow] = Field(
        default_factory=list,
        description="Material economic units with disclosure basis, driver equation, cash/capital profile and valuation treatment.",
    )
    business_model_mechanisms: list[BusinessModelMechanismRow] = Field(
        default_factory=list,
        description=(
            "Four to seven links explaining who pays, why they buy, how orders become revenue/cash, "
            "where gross profit is earned and what capital is required. Keep valuation out of this map."
        ),
    )
    industry_driver_matrix: list[IndustryDriverRow] = Field(
        default_factory=list,
        description="Dated sector-native demand, supply/capacity, price/cost and policy drivers with financial transmission.",
    )
    moat_mechanisms: list[MoatMechanismRow] = Field(
        default_factory=list,
        description=(
            "Three to five economic moat mechanisms tested against history and true peers; awards, market-share "
            "claims and R&D spend alone are not proof."
        ),
    )
    accounting_quality_matrix: list[AccountingQualityRow] = Field(
        default_factory=list,
        description="Working-capital, cash-conversion, capex/ROIC, leverage/impairment and shareholder-return checks.",
    )
    alternative_intelligence_decisions: list[AlternativeIntelligenceDecision] = Field(
        default_factory=list,
        description="Deduplicated full-text KPE claims with a model, probability, verification or rejection outcome.",
    )
    sell_side_expectation_matrix: list[SellSideExpectationRow] = Field(
        default_factory=list,
        description=(
            "KSI sell-side forecast, revision and valuation observations reconciled against the independent model. "
            "A single broker or repost must never be labelled consensus."
        ),
    )
    safe_valuation_assumptions: SafeValuationAssumptions = Field(
        default_factory=SafeValuationAssumptions,
        description="Bull/base/bear valuation inputs and PM safety requirements; application code calculates all outputs.",
    )
    deterministic_valuation: DeterministicValuationOutput = Field(
        default_factory=DeterministicValuationOutput,
        description="Leave at defaults; application code overwrites this field.",
    )
    investment_conclusion_and_core_conflict: str = Field(
        description=(
            "Public opening section. State the rating, central operating conclusion, decisive evidence and "
            "strongest unresolved counterpoint in two or three connected paragraphs. Keep execution mechanics "
            "and detailed valuation out; do not repeat later tables."
        ),
    )
    canonical_model_snapshot: list[CanonicalModelLine] = Field(
        min_length=4,
        description=(
            "Copy the Research Manager canonical model snapshot exactly. If the PM changes "
            "a value, include the replacement here and a matching handoff_change_rows entry."
        ),
    )
    handoff_change_rows: list[ModelHandoffChange] = Field(
        default_factory=list,
        description=(
            "Every PM change versus the Research Manager snapshot. An empty list means exact "
            "preservation; prose claims of no change do not override numeric differences."
        ),
    )
    company_disaggregation: str = Field(
        description=(
            "Reader-facing company chapter for someone unfamiliar with the company. Explain who pays, what each "
            "product solves, purchase/tender and delivery cycles, pricing/revenue recognition, service obligations, "
            "cost stack, working capital, capital intensity and profit pools. Separate reported "
            "segments from analytical product/channel/geography/customer/project/asset units; "
            "show what each unit sells, drivers, disclosed scale/margin/cash, valuation treatment "
            "and missing disclosure without invented allocations. Explain the operating mechanism and end with "
            "the boundary or unresolved disclosure that matters to the thesis."
        )
    )
    industry_cycle_and_competition: str = Field(
        description=(
            "Reader-facing industry chapter with a core judgment, key evidence, causal mechanism and strongest "
            "counter-case. Analyze cycle and competitive structure using sector-native supply, demand, "
            "capacity, utilization, price/spread and true-peer evidence. Separate verified "
            "facts from proxies and explain the financial transmission."
        ),
    )
    autonomous_forecast_model: str = Field(
        description=(
            "Narrative explanation of the final accepted three-year independent forecast. Explain material-unit "
            "drivers, model type, reconciliation and the most fragile assumption, but do not reproduce another "
            "consolidated forecast table because the renderer supplies the canonical table. Reconcile to "
            "model-profile-appropriate group earnings, cash/capital, per-share lines, "
            "formulas, evidence status and share count. Do not substitute consensus narrative."
        )
    )
    thesis_financial_bridge: str = Field(
        description=(
            "Integrated reader-facing investment-logic chapter. Write two or three connected analyst subsections, "
            "not a question list, module recap or visible checklist of conclusion/evidence/counterevidence labels. "
            "For each decisive thesis make clear the conclusion, strongest evidence, mechanism, "
            "strongest counterevidence/boundary, driver formula, bull/base/bear assumptions and the "
            "resulting revenue, profit, EPS, FCF/capital and fair-value effect. Explicit missing "
            "inputs are acceptable; qualitative claims posing as quantified effects are not. Close each thesis "
            "with the expectation difference and falsification condition. Exact target prices, multiples and "
            "scenario fair values belong only in section 7."
        )
    )
    moat_evidence_scorecard: str = Field(
        description=(
            "Synthesize the moat judgment in prose after the structured mechanism table. Test every claimed moat "
            "using observable history "
            "or true-peer evidence, counterevidence and financial transmission to share, price, "
            "margin, turnover, cash conversion or ROIC."
        )
    )
    valuation_closure: str = Field(
        description=(
            "Interpret the program-calculated valuation: justify method and assumption selection, identify "
            "core/scenario/optionality/excluded buckets, double-counting controls, evidence limits and what "
            "would change the inputs. Do not publish competing hand-calculated EPS, per-share values, "
            "probability-weighted values or safety prices."
        )
    )
    accounting_and_capital_allocation: str = Field(
        description=(
            "Accounting quality, cash conversion, working capital, capex/CIP, leverage, "
            "impairment, dividend/buyback and management capital-allocation assessment. "
            "Connect each material item to earnings quality, FCF, ROIC and valuation."
        ),
    )
    expectation_gap_and_market_pricing: str = Field(
        description=(
            "What the current price implies versus the independent model, company-specific "
            "consensus when available, and true-peer alternatives. Name the exact variable, "
            "period and magnitude of the expectation gap."
        ),
    )
    risks_catalysts_verification: str = Field(
        description=(
            "Integrated downside, catalysts, falsification and dated verification calendar. "
            "Separate verified adverse evidence from missing data and state add/hold/trim/"
            "downgrade consequences consistent with the final rating."
        ),
    )
    handoff_integrity_audit: str = Field(
        description=(
            "Compare the final memo with the Research Manager accepted model and underwriting "
            "manifest. List preserved units/years/bridges/buckets and every revision with old value, "
            "new value, evidence and recalculated financial/valuation impact."
        )
    )
    report_markdown: str = Field(
        default="",
        description=(
            "Legacy compatibility field. Keep empty. It is not rendered and cannot replace "
            "the fixed eight-section memo."
        )
    )
    shared_model_change_audit: str = Field(
        description=(
            "Compact ledger of the final accepted changes to the shared underwriting model: "
            "question/forecast line, old assumption, challenged evidence, new assumption, "
            "EPS/FCF/value impact, and disposition. Include unchanged/rejected important clues."
        )
    )
    report_quality_self_check: str = Field(
        description=(
            "State whether segment coverage, three-year reconciliation, scenario valuation, "
            "evidence lineage, period/unit arithmetic and KPE transmission are complete. Name "
            "any remaining gap without changing or rationalizing the rating."
        )
    )


class PortfolioDecision(BaseModel):
    """Structured output produced by the Portfolio Manager.

    The model fills every field as part of its primary LLM call; no separate
    extraction pass is required. Field descriptions double as the model's
    output instructions, so the prompt body only needs to convey context and
    the rating-scale guidance.
    """

    rating: PortfolioRating = Field(
        description=(
            "The final position rating. Exactly one of Buy / Overweight / Hold / "
            "Underweight / Sell, picked based on the analysts' debate. All other "
            "text fields must be consistent with this final rating; upstream "
            "Research Manager, Trader, or risk-analyst ratings may be discussed "
            "only as non-final prior/upstream views, never as the current or final "
            "Portfolio Manager rating. The rating must follow from the company's "
            "standalone fundamental chain, not from the failure of the opposite "
            "case. A pending disclosure or missing field is neutral and must not "
            "mechanically force Hold; choose Hold only when the available verified "
            "evidence and expected-value distribution are genuinely balanced."
        ),
    )
    rating_posture: Optional[str] = Field(
        default=None,
        description=(
            "A short action qualifier for the final rating. Keep the clean rating "
            "field unchanged, but label the actual PM posture so Hold does not "
            "hide the trade. For Hold, choose one of: Hold / Positive Watch, "
            "Hold / Defensive Starter, Hold / Neutral Wait, Hold / Negative Watch. "
            "Then explain in one sentence whether new capital should wait, "
            "open only a starter, or avoid. For Overweight, state whether it is "
            "staged/cautious or normal. For Underweight, state whether it is "
            "absolute risk reduction or relative low-weight/watch."
        ),
    )
    company_snapshot: str = Field(
        description=(
            "A short, self-contained company introduction for public sharing. "
            "Identify what the company does, its main business or profit drivers, "
            "where the company sits in its industry cycle, and why those drivers "
            "matter to this investment case. Keep it clear, information-dense, "
            "and useful to a reader who does not already know the company."
        ),
    )
    one_line_thesis: str = Field(
        description=(
            "One sentence that states the investable view in plain language: "
            "what the market may be missing, why the rating follows, and the "
            "main caveat if needed. The stated action and tone must match the "
            "final rating field."
        ),
    )
    reader_takeaway_entry_band: Optional[str] = Field(
        default=None,
        description=(
            "A reader-facing take-away that answers: if the company's fundamentals "
            "are not structurally impaired, what price band or valuation band would "
            "make the stock worth building or rebuilding a position, even when the "
            "current rating is Underweight or Sell. Give the range, the valuation or "
            "earnings logic behind it, and the business conditions that must still "
            "hold. If the business is fundamentally broken or no responsible entry "
            "band can be justified, say so explicitly."
        ),
    )
    value_stock_safety_price: Optional[str] = Field(
        default=None,
        description=(
            "Standalone Safety Price / Defensive Build Anchor section content. "
            "For financially resilient mature companies, provide a conservative "
            "safety price or safety price band for slow accumulation by new "
            "builders. For commodity/resource/cyclical companies, provide a "
            "cycle-trough or stress-case build anchor if the evidence supports "
            "one; otherwise explicitly state that no reliable safety price can "
            "be assigned. This is not a target price and not a stop-loss. Anchor "
            "it in financial state such as normalized low-cycle EPS or FCF, "
            "cycle-midpoint earnings, sustainable dividend yield, book value/PB "
            "and ROE, net cash or leverage, cash conversion, asset quality, "
            "payout capacity, and peer/historical valuation floors. Include the "
            "price band, formula or valuation bridge, business conditions that "
            "must remain true, how builders should accumulate around it, and "
            "what financial or operating deterioration would invalidate it."
            " Keep it concise: this is a margin-of-safety anchor, not a second "
            "valuation essay. Prefer one short paragraph or a compact 3-4 row "
            "table; put detailed valuation debate in the Investment Thesis."
        ),
    )
    reader_action_guidance: Optional[str] = Field(
        default=None,
        description=(
            "Reader-facing action guidance split into two audiences: investors who "
            "already hold a full or large position, and investors who are preparing "
            "to build a position. The advice must fit the final rating. For Buy or "
            "Overweight, explain how to build or add in stages, what evidence or "
            "price/valuation zone justifies adding, and how much dry powder to keep. "
            "For Hold, do not write a low-information neutral paragraph; explain "
            "the live thesis, whether a starter/observation position is justified, "
            "what full holders should monitor or rebalance, what new buyers should "
            "wait for before initiating or adding, and the exact upgrade/downgrade "
            "triggers. For Underweight or "
            "Sell, explain how full holders should reduce or hedge, and what lower "
            "price/valuation band would make new entry reasonable if fundamentals "
            "remain intact. If no responsible build zone exists, say so explicitly. "
            "For insurance or defensive-dividend names, if the final rating is "
            "Overweight but recommended sizing is only a starter or below normal "
            "target weight, reconcile why Overweight is independently proven; "
            "otherwise use Hold with positive-bias starter guidance and name the "
            "disclosure that unlocks full sizing. "
            "Do not tell holders to reduce to Underweight or tell new buyers to "
            "avoid the stock when the final rating is Buy or Overweight, unless that "
            "sentence is explicitly framed as a rejected upstream view."
        ),
    )
    business_driver_map: str = Field(
        description=(
            "A compact map of the 3-5 variables that really drive the company's "
            "business value and stock performance. Name the variables, explain "
            "their direction of impact, and tie them to this company rather than "
            "generic industry factors. Include the industry-native variables that "
            "a buy-side analyst would track. For banks, map earning assets, NIM/"
            "deposit cost, fee income/AUM, asset quality/credit cost, capital/RWA, "
            "and payout capacity rather than generic revenue, gross margin, orders, "
            "inventory, or OCF. For insurers, map life NBV/EV and channel quality, "
            "investment yield versus liability cost, P&C COR, solvency/capital, "
            "dividend capacity, and subsidiary/SOTP value rather than generic PE "
            "or one-quarter OCF alone."
        ),
    )
    business_segment_breakdown: Optional[str] = Field(
        default=None,
        description=(
            "Mandatory for unfamiliar or multi-business companies when financial-report "
            "intelligence is available. Write this like a buy-side segment memo, "
            "not a company-introduction paragraph. Cover five items: (1) what each "
            "business line actually sells or delivers; (2) disclosed revenue scale "
            "and growth by segment; (3) gross margin, net margin, profit contribution, "
            "cash conversion, or why those economics are not disclosed; (4) whether "
            "the segment is mature core, cyclical core, geography/channel mix, or "
            "second curve; and (5) valuation treatment for each bucket. If revenue, "
            "growth, margin, or profit by segment is not disclosed, write 'not "
            "disclosed' for that item and state how the gap caps SOTP confidence."
        ),
    )
    segment_prosperity_analysis: Optional[str] = Field(
        default=None,
        description=(
            "A mandatory deep segment-level prosperity analysis for multi-business "
            "companies. Analyze every material business separately before assigning "
            "a consolidated prosperity label. For each segment provide: revenue and "
            "profit weight; current prosperity level (high, medium-high, neutral, "
            "weakening, low, bottom-testing, or recovery); marginal direction; a "
            "written demand -> supply/capacity -> price/volume -> utilization/mix -> "
            "margin -> cash-flow causal explanation; dated supporting data across at "
            "least three relevant dimensions; strongest counterevidence; confidence; "
            "EPS/FCF and valuation implication; and the next verification point. "
            "Distinguish level from direction. Aggregate to the company using revenue, "
            "gross-profit/profit contribution, cash intensity, and capital intensity, "
            "not a simple average. If evidence is unavailable, mark the cell missing and "
            "add a retrieval task rather than filling the matrix with generic prose or "
            "mechanically changing the rating."
        ),
    )
    business_model_supply_chain_primer: Optional[str] = Field(
        default=None,
        description=(
            "A standalone reader-education section for the Portfolio Manager memo. "
            "Explain the company's business model in plain language: what it sells, "
            "who pays, how revenue turns into profit and cash flow, and which cost, "
            "price, volume, utilization, asset-turnover, or credit variables matter. "
            "Then explain the industry value chain: upstream inputs or suppliers, "
            "midstream manufacturing/service/platform links, downstream customers "
            "or application markets, and where this company sits in that chain. "
            "When supplied context names listed upstream/downstream companies or "
            "true peers, mention a few as examples and state their chain role; do "
            "not invent listed-company names that are not supported by the prompt. "
            "If names are unavailable, describe the categories and say names are "
            "not verified. Keep the section educational but investment-relevant."
        ),
    )
    core_research_questions: Optional[str] = Field(
        default=None,
        description=(
            "A standalone Core Research Questions section for the Portfolio Manager "
            "memo when the financial-report intelligence supplies Pre-Debate "
            "Underwriting Questions. Do not paste the upstream question table. "
            "Select the 4-7 most decision-relevant, company-specific questions, "
            "then answer them using the post-debate PM judgment: what the bull "
            "case proved, what the bear case exposed, which evidence settled the "
            "question, what remains unresolved, and how the answer changes rating, "
            "valuation, sizing, or the next verification action. Prefer a compact "
            "markdown table with columns such as core question, initial skeptical "
            "prior, bull evidence, bear evidence, PM ruling, earnings/valuation "
            "impact, and next verification. When writing "
            "Chinese, title the section `核心投研问题与辩论后的答案`."
        ),
    )
    bull_bear_debate: str = Field(
        description=(
            "A compact public-facing summary of the strongest bull argument and "
            "the strongest bear argument from the research debate. Present it as "
            "a real clash of views, not a generic pro/con list, and keep it short "
            "enough to fit inside the Portfolio Manager excerpt."
        ),
    )
    debate_verdict: str = Field(
        description=(
            "One concise paragraph explaining why the Portfolio Manager leans "
            "toward one side, or stays balanced, after weighing the bull and bear "
            "arguments. Tie the verdict to evidence quality, expectation gap, "
            "probability/payoff, and research gaps."
        ),
    )
    investment_logic_chain: str = Field(
        description=(
            "Explain the thesis as a causal chain: if the key business variables "
            "move or are verified, then fundamentals change, then market "
            "expectations or valuation may reprice, leading to the rating. Keep "
            "it readable and information-dense. Make clear how the reader should "
            "connect company economics, industry conditions, financial drivers, "
            "valuation assumptions, and position action."
        ),
    )
    executive_summary: str = Field(
        description=(
            "A concise action plan covering entry strategy, position sizing, "
            "key risk levels, and time horizon. Write for readers who may only "
            "see this Portfolio Manager Decision excerpt. Keep it compressed: "
            "two to three sentences or a short paragraph, not a full investment plan. "
            "The action plan must use the same final rating as the rating field."
        ),
    )
    verification_and_falsification: str = Field(
        description=(
            "A concise checklist of the next verification points and the signals "
            "that would falsify or downgrade the thesis. Use concrete observable "
            "items from the report, such as earnings, orders, product prices, "
            "margins, cash flow, policy, inventory, technical levels, or sector data. "
            "Each item should say what data would confirm, what data would weaken, "
            "and what action/rating change would follow."
        ),
    )
    investment_thesis: str = Field(
        description=(
            "Focused reasoning anchored in specific evidence from the analysts' "
            "debate. Preserve the main analytical path from the full report "
            "without turning it into an exhaustive data dump; explain why the "
            "rating follows from thesis, expectation gap, probability/payoff, "
            "and key risks. The reader should understand what the market appears "
            "to price in, where the memo agrees or disagrees, why price and value "
            "may be mismatched, and which facts would close that mismatch."
        ),
    )
    core_bet: Optional[str] = Field(
        default=None,
        description=(
            "The core investment bet: what future variable must move or be "
            "recognized by the market for the thesis to work."
        ),
    )
    boom_bust_expectation: Optional[str] = Field(
        default=None,
        description=(
            "Assess whether the relevant industry/business cycle expectation is "
            "likely to realize, using macro context, industry data, product or "
            "route evidence, company exposure, and bounded inference."
        ),
    )
    expectation_gap: Optional[str] = Field(
        default=None,
        description=(
            "Explain the potential expectation gap: what the market may be "
            "underpricing or overpricing, what assumptions today's valuation "
            "appears to embed, and what evidence suggests those assumptions are "
            "too pessimistic, too optimistic, or fair. Translate the gap into "
            "specific revenue, margin, EPS, ROE, cash-flow, order, or multiple "
            "assumptions rather than saying only that valuation is cheap/expensive."
        ),
    )
    probability_payoff: Optional[str] = Field(
        default=None,
        description=(
            "Summarize win probability, upside payoff, downside risk, and whether "
            "the risk/reward justifies the rating. For scenario analysis, attach "
            "probabilities to concrete driver assumptions, not generic labels. "
            "For banks, specify NIM bps, fee-income growth, credit cost/provision "
            "coverage, NPL movement, ROE, PB or dividend-yield assumptions, and "
            "the corresponding position action. For insurers, label probabilities "
            "as subjective PM underwriting weights unless they come from a supplied "
            "source, and attach them to NBV growth, EV/P-EV, OPAT/core profit, "
            "investment spread, solvency, COR, dividend coverage, and SOTP discount "
            "assumptions."
        ),
    )
    cycle_valuation_assessment: Optional[str] = Field(
        default=None,
        description=(
            "Classify the stock's valuation x prosperity setup and explain why "
            "the final rating is fair: low valuation/low prosperity, high "
            "valuation/high prosperity, low valuation/high prosperity, or high "
            "valuation/low prosperity."
        ),
    )
    catalyst_path: Optional[str] = Field(
        default=None,
        description=(
            "List concrete catalysts or data checkpoints that could cause "
            "repricing, such as freight indexes, product prices, policy, earnings, "
            "orders, inventory, or sector moves. For banks, focus on NIM/net "
            "interest yield, deposit cost, fee income/AUM, NPL/provision coverage, "
            "capital/RWA, dividend policy, and rate-policy transmission."
        ),
    )
    falsification_signals: Optional[str] = Field(
        default=None,
        description=(
            "Specific observable signals that would invalidate the thesis or "
            "force a lower rating/position."
        ),
    )
    conviction_and_position: Optional[str] = Field(
        default=None,
        description=(
            "State conviction level and matching position posture: full position, "
            "overweight, starter position, watch only, trim, or avoid. Keep this "
            "concise and avoid repeating the executive summary."
        ),
    )
    market_regime_adjustment: Optional[str] = Field(
        default=None,
        description=(
            "Explain how broad-market mood, market valuation, sector risk, and "
            "the stock's own characteristics adjusted the rating. Be specific: "
            "quality defensives, high-beta cyclicals, distressed value, and "
            "commodity/shipping names should not be calibrated mechanically."
        ),
    )
    profit_taking_range: Optional[str] = Field(
        default=None,
        description=(
            "If the final view is bullish or constructive, provide a reasonable "
            "staged profit-taking or trimming range, grounded in valuation, "
            "technical levels, market regime, and evidence. If not applicable, omit."
        ),
    )
    entry_watch_range: Optional[str] = Field(
        default=None,
        description=(
            "If the final view is bearish or cautious, provide a reasonable entry "
            "or re-entry watch range where risk/reward may improve, grounded in "
            "valuation, support levels, market regime, and evidence. If not applicable, omit."
        ),
    )
    unverified_key_assumptions: Optional[str] = Field(
        default=None,
        description=(
            "List any important but unverified assumptions, especially product "
            "prices, shipping rates, inventory, route-level TCE, policy details, "
            "or exact percentage claims that lack tool evidence."
        ),
    )
    evidence_limited_research_gaps: Optional[str] = Field(
        default=None,
        description=(
            "List thesis-critical data gaps as neutral non-evidence and identify the "
            "affected model cells. "
            "Do not use this as a vague disclaimer: name the exact missing product, "
            "spread, inventory, freight, capacity, policy, or demand data and what "
            "model assumption it would update if retrieved. For banks, name the exact missing "
            "NIM, deposit-cost, loan-yield, fee-rate, credit-cost, NPL, provision, "
            "CET1/RWA, or payout data instead of generic operating gaps."
        ),
    )
    supply_demand_fallback_view: Optional[str] = Field(
        default=None,
        description=(
            "When micro operating data is missing, summarize the product-specific "
            "macro supply-demand fallback view: upstream cost drivers, downstream "
            "demand, capacity/utilization, inventories or proxies, import/export "
            "exposure, policy, seasonality, substitution, and evidence strength."
        ),
    )
    price_target: Optional[float] = Field(
        default=None,
        description="Optional target price in the instrument's quote currency.",
    )
    time_horizon: Optional[str] = Field(
        default=None,
        description="Optional recommended holding period, e.g. '3-6 months'.",
    )
    prior_rating: Optional[str] = Field(
        default=None,
        description=(
            "If a recent same-ticker decision exists, state its rating exactly; "
            "otherwise omit."
        ),
    )
    new_evidence_since_prior: Optional[str] = Field(
        default=None,
        description=(
            "List the decisive new evidence since the most recent same-ticker "
            "decision. If there is no decisive new evidence, say so explicitly."
        ),
    )
    unchanged_core_facts: Optional[str] = Field(
        default=None,
        description=(
            "Summarize the thesis-critical facts that remain unchanged versus the "
            "most recent same-ticker decision."
        ),
    )
    rating_change_audit: Optional[str] = Field(
        default=None,
        description=(
            "Explain why the final rating was preserved or changed relative to "
            "the prior same-ticker decision. A price move alone is not enough for "
            "a directional reversal."
        ),
    )
    rating_evidence_audit: Optional[str] = Field(
        default=None,
        description=(
            "A compact rating-quality audit that makes the final rating easy to "
            "understand without reader interpretation. Separate at least five "
            "items: absolute company view, sector-relative allocation view, data "
            "sufficiency, key-number or unit conflicts, and why the selected "
            "rating tier follows instead of the adjacent tiers. Explain why the "
            "rating follows from the fundamental chain itself rather than from the "
            "failure of the opposite case. If choosing Overweight with only starter "
            "sizing, explicitly prove why this is not merely Hold/positive watch; "
            "if choosing Hold, make it useful by stating the live thesis, upgrade "
            "gate, downgrade gate, and current position implication. If a negative "
            "rating relies mainly on peer substitution, state whether the peer "
            "is verified on the same industry-native drivers. For insurers, a "
            "peer screen based only on PE/PB/ROE/dividend yield/one-quarter "
            "profit growth is insufficient for Underweight/Sell unless the peer "
            "is also checked on NBV growth, NBV margin, EV or P/EV, OCF/cash "
            "quality, solvency, investment spread, payout coverage, channel mix, "
            "and P&C COR where applicable."
        ),
    )
    information_utilization_audit: Optional[str] = Field(
        default=None,
        description=(
            "A compact PM audit of how the report used the available information. "
            "Cover five buckets when available: filings/official disclosures, "
            "Tushare market and financial data, Knowledge Planet stream or PDF "
            "intelligence, peer/industry KPI context, and price-volume/relative "
            "strength. For each bucket, state the decision-use: core valuation "
            "input, probability adjustment, catalyst/verification item, sizing/"
            "timing adjustment, rejected/noisy clue, or missing. If Knowledge "
            "Planet contains high-quality private/proxy clues, do not dismiss "
            "them merely as unofficial; say how they changed bull/base/bear "
            "probabilities, what objective anchor is still needed, and whether "
            "the clue affects rating, posture, or only the verification calendar."
            " Cite promoted clues by KPE id and show a numeric assumption old->new, "
            "scenario probability before->after, unchanged/watch result, or rejection "
            "reason. Do not claim a probability change without values."
        ),
    )
    material_catalysts: Optional[str] = Field(
        default=None,
        description=(
            "List only verified material catalysts that pass the four-gate test: "
            "verifiable evidence, economic transmission, timetable, and materiality. "
            "Classify each as asset-revaluation or business-realization."
        ),
    )
    thematic_valuation_bridge: Optional[str] = Field(
        default=None,
        description=(
            "Explain the valuation bridge for each verified theme: asset "
            "revaluation versus business realization, disclosed value or monetization "
            "evidence, materiality, whether it belongs in core valuation, scenario "
            "valuation, SOTP/NAV, or only qualitative optionality, and the main "
            "counterargument."
        ),
    )
    rejected_themes: Optional[str] = Field(
        default=None,
        description=(
            "List thematic claims reviewed but rejected from valuation because "
            "they lack primary-source verification, economic transmission, "
            "timetable, or materiality."
        ),
    )
    peer_selection_verdict: Optional[str] = Field(
        default=None,
        description=(
            "State the final cross-sectional verdict: whether the target is the "
            "best build candidate in its sampled peer set, an acceptable but not "
            "best option, or inferior to named peers. Explain the metrics and "
            "business reasons, and how that affects position posture."
            " For insurers, name whether the target is a higher-beta NBV/SOTP "
            "recovery expression, a cleaner insurance-quality compounder, a "
            "dividend sleeve, or inferior to true insurer peers. Do not call a "
            "peer a verified superior substitute from PE/PB/ROE alone; require "
            "same-driver insurance evidence or label the switch as a hypothesis."
        ),
    )
    peer_comparison_summary: Optional[str] = Field(
        default=None,
        description=(
            "Mandatory when same-industry peer comparison context is available. "
            "Write this like a buy-side peer-relative allocation memo. Cover five "
            "items: (1) peer-universe hygiene: which peers are true operating comps "
            "and which are only broad-industry screens; (2) target rank and key "
            "metrics versus peers; (3) whether valuation discount/premium is earned "
            "by ROE, margin, growth, balance-sheet risk, cash return, or business "
            "quality; (4) named better/worse alternatives and their caveats; and "
            "(5) what the peer screen changes in sizing, rating, or follow-up work."
            " For insurers, compare true life/P&C/integrated-insurer peers separately "
            "from broad financial screens, and explain why the target is preferable "
            "or inferior versus named alternatives."
        ),
    )
    supply_chain_position_verdict: Optional[str] = Field(
        default=None,
        description=(
            "When a curated chain map exists, state whether the best current "
            "opportunity lies in the target's own segment or another segment of "
            "the same industrial chain, and explain how that affects the final "
            "position decision."
        ),
    )
    earnings_model_bridge: Optional[str] = Field(
        default=None,
        description=(
            "Summarize the earnings bridge behind the final decision: which "
            "volume, price, mix, margin, working-capital, or financing levers "
            "must move under bull/base/bear cases. For banks, use earning assets "
            "x NIM, fee income, credit cost/provisioning, operating efficiency, "
            "capital consumption, and payout rather than manufacturing-style "
            "volume, gross margin, inventory, OCF, orders, or contract liabilities."
        ),
    )
    forward_forecast_model: Optional[str] = Field(
        default=None,
        description=(
            "A sell-side-style forward forecast bridge for the next two to three "
            "years or the next four quarters. State revenue, gross margin, expense "
            "ratio, operating profit, net profit, EPS, cash-flow, capex, and balance-"
            "sheet assumptions where material. Distinguish disclosed facts, model "
            "assumptions, and scenario estimates. If exact forecasts cannot be "
            "supported, provide a driver-based model skeleton and say which inputs "
            "must be verified before target valuation can carry high confidence. "
            "Use the supplied business-bucket matrix and provide three distinct "
            "forward years (or four quarters), with segment-to-consolidated revenue, "
            "profit/EPS, OCF/FCF reconciliation and evidence status for each decisive "
            "assumption. Do not leave placeholder cells in the final report."
        ),
    )
    valuation_framework: Optional[str] = Field(
        default=None,
        description=(
            "The valuation framework that follows from the company research, not "
            "a generic target-price paragraph. Explain which method is primary "
            "for each business bucket or scenario: PE, PB/ROE, EV/EBITDA, DCF, "
            "NAV/SOTP, dividend yield, liquidation/asset value, or peer-relative "
            "valuation. State why the chosen method fits the business economics, "
            "which parts enter core value, which stay in scenario value, and what "
            "current price implies versus the research view. For insurers, include "
            "or explicitly mark missing P/EV or EV growth, NBV multiple, PB-ROE, "
            "dividend yield with payout/solvency coverage, and SOTP with segment "
            "formula, ownership/stake, per-share conversion, holding-company "
            "discount, and double-counting checks. If current EV is missing, use "
            "latest annual EV only as a stale-base cross-check and label it."
        ),
    )
    market_behavior_validation: Optional[str] = Field(
        default=None,
        description=(
            "Use historical daily and minute K-line behavior as a validation and "
            "timing layer after the fundamental thesis. Discuss intraday reversal, "
            "high-low range, first/last-30-minute behavior, volume concentration, "
            "liquidity, and whether recent action looks like company alpha, sector "
            "beta, commodity beta, or broad risk appetite. Do not let technical or "
            "minute-line behavior replace company research; connect it only to "
            "confidence, sizing, entry timing, or verification."
        ),
    )
    market_implied_expectation: Optional[str] = Field(
        default=None,
        description=(
            "State what the current price seems to imply about earnings power, "
            "growth, or margin durability, and identify the key disagreement "
            "between the market quote and the research view."
        ),
    )
    pm_summary: Optional[str] = Field(
        default=None,
        description=(
            "A 5-8 line buy-side PM summary: rating, action, position size, time "
            "horizon, core bet, why now, biggest risk, and next verification date. "
            "This should be useful as a one-page investment committee front box."
        ),
    )
    key_data_check: Optional[str] = Field(
        default=None,
        description=(
            "Reconcile the thesis-critical numbers used in the memo. Include 6-10 "
            "items such as revenue, net profit, EPS, market cap, PE/PB, operating "
            "cash flow, contract liabilities/orders/backlog, capex, dividend, net "
            "debt, and key segment metrics. If the debate contains conflicting "
            "signs, units, periods, or magnitudes, flag the conflict and state the "
            "source-backed figure used in the final decision."
        ),
    )
    filing_internal_quality_review: Optional[str] = Field(
        default=None,
        description=(
            "A synthesized review of the ten filing-only quality modules when "
            "financial-report intelligence supplies them: accounting reconciliation, "
            "segment economics depth, footnote radar, cash-flow quality, capex/CIP "
            "return bridge, MD&A text change, non-recurring profit quality, "
            "balance-sheet forward signals, shareholder-return authenticity, and "
            "disclosure quality. Integrate the material conclusions into the PM "
            "summary and investment case rather than listing all ten mechanically."
        ),
    )
    expectation_gap_evidence: Optional[str] = Field(
        default=None,
        description=(
            "Evidence that the expectation gap is real rather than asserted: "
            "valuation percentile, price-EPS-multiple decomposition, consensus or "
            "sell-side expectations when supplied, institutional/holder behavior, "
            "technical price action, and investor-interaction question patterns."
        ),
    )
    unit_economics_bridge: Optional[str] = Field(
        default=None,
        description=(
            "For any second curve, platform, service, new product, project, channel, "
            "or financing business, build a unit-economics bridge such as revenue/"
            "GMV/volume x take rate or ASP x gross margin/net margin x reinvestment "
            "or working capital. If take rate, margin, breakeven, utilization, "
            "retention, or loss rate is not disclosed, say 'not disclosed' and keep "
            "the business in scenario value rather than core valuation."
        ),
    )
    project_ramp_bridge: Optional[str] = Field(
        default=None,
        description=(
            "For new plants, mines, stores, malls, data centers, ships, property "
            "projects, or platforms, track capacity/area/users, utilization or "
            "occupancy, price/rent, ramp timetable, incremental margin, capex, "
            "ROIC/payback, and the source of demand. Omit if there is no material "
            "project or capacity ramp."
        ),
    )
    financing_listing_scenario: Optional[str] = Field(
        default=None,
        description=(
            "For H-share or secondary listings, private placements, convertibles, "
            "debt refinancing, major capex funding, or asset sales, provide bull/"
            "base/bear pricing or cost-of-capital scenarios, use of proceeds, "
            "dilution, ROE/FCF impact, and whether the event creates an anchor or "
            "an overhang. Omit if no financing/listing/dilution event matters."
        ),
    )
    verification_calendar: Optional[str] = Field(
        default=None,
        description=(
            "A date- or event-based verification calendar. For each next disclosure "
            "or operating data point, state what would trigger add/hold/trim/"
            "downgrade/exit. Keep it concrete and action-linked."
        ),
    )
    company_quality_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on business quality alone, independent of the stock "
            "price: good / mixed / weak, with the main reason."
        ),
    )
    current_odds_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on today's risk/reward alone: attractive / neutral / "
            "unattractive, with the main reason."
        ),
    )
    relative_allocation_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on relative deployment: best option / acceptable but "
            "not best / inferior to alternatives, grounded in peer and chain "
            "comparisons."
        ),
    )
    management_capital_allocation_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on stewardship and capital allocation, grounded in "
            "hard signals such as capex, buybacks, dividends, financing, M&A, "
            "goodwill, leverage, and management alignment."
        ),
    )
    shareholder_structure_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on ownership/chip structure, grounded in top holders, "
            "float holders, holder count, insider trade, pledge, repurchase, and "
            "unlock evidence."
        ),
    )
    investor_communication_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on official investor communication: what investors "
            "are asking about, whether management answers are substantive or "
            "evasive, and whether disclosure quality strengthens or weakens "
            "confidence in the thesis."
        ),
    )
    policy_direction_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on official policy direction: whether national or "
            "industry policy supports the demand lane, how directly it reaches "
            "the company economics, and what bridge evidence is still missing."
        ),
    )
    industry_driver_verdict: Optional[str] = Field(
        default=None,
        description=(
            "A clean verdict on the industry-native variables that truly decide "
            "the thesis, grounded in filing evidence plus outside confirmation "
            "or contradiction."
        ),
    )
    strategic_optionality_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Summarize important but non-base-case optionality such as new "
            "business lines, investee holdings, asset revaluation, or thematic "
            "catalysts. State why they matter, why they do or do not change the "
            "rating today, and what would upgrade them."
        ),
    )
    buy_side_depth_audit: Optional[str] = Field(
        default=None,
        description=(
            "A short self-audit of the final memo's weak spots. Name any section "
            "that remains evidence-light or potentially generic: segment economics, "
            "peer comparability, valuation assumptions, catalyst timetable, "
            "management/capital allocation, ownership overhang, market/technical "
            "timing, or data coverage. For each weakness, separate verified adverse "
            "evidence from neutral missing data and state the follow-up or valuation treatment."
        ),
    )
    data_coverage_audit: Optional[str] = Field(
        default=None,
        description=(
            "Concise audit of the supplied evidence set: which precomputed data "
            "modules were ready, partial, failed, or missing; whether any gap is "
            "thesis-critical; and the exact retrieval or verification task. Do not "
            "convert unavailable data into directional evidence."
        ),
    )


def normalize_sell_side_pm_decision(
    value: SellSidePMDecision | dict,
) -> tuple[SellSidePMDecision, list[str]]:
    """Freeze dependent PM outputs with deterministic arithmetic.

    The model supplies assumptions.  This function owns EPS, FCF, scenario
    per-share values, probability weighting, optionality conversion, expected
    return and the safety-price ceiling.
    """
    decision = value if isinstance(value, SellSidePMDecision) else SellSidePMDecision.model_validate(value)
    payload = decision.model_dump()
    notes: list[str] = []
    lines = list(payload.get("canonical_model_snapshot", []))

    def _metric(row: dict) -> str:
        return _canonical_metric_name(str(row.get("metric", "")))

    share_row = next(
        (
            row
            for row in lines
            if any(
                token in re.sub(r"[^a-z0-9一-鿿]+", "", str(row.get("metric", "")).lower())
                for token in ("dilutedshare", "sharecount", "totalshare", "稀释股本", "总股本")
            )
            and row.get("value") is not None
        ),
        None,
    )
    shares = float(share_row["value"]) if share_row and float(share_row["value"]) > 0 else None

    by_metric_period = {
        (_metric(row), str(row.get("period", ""))): row for row in lines
    }
    accepted_ocf_ratio: float | None = None
    for change in payload.get("handoff_change_rows", []) or []:
        line_id = re.sub(r"[^a-z0-9]+", "", str(change.get("line_id", "")).lower())
        if (
            "ocf" in line_id
            and ("ni" in line_id or "netincome" in line_id or "profit" in line_id)
            and str(change.get("disposition", "")).lower() == "accepted"
        ):
            try:
                candidate_ratio = float(change.get("new_value"))
            except (TypeError, ValueError):
                continue
            if candidate_ratio > 0:
                accepted_ocf_ratio = candidate_ratio
    profit_rows = [row for row in lines if _metric(row) == "parent_profit" and row.get("value") is not None]
    if shares:
        for profit in profit_rows:
            period = str(profit.get("period", ""))
            eps_value = float(profit["value"]) / shares
            eps = by_metric_period.get(("eps", period))
            if eps is None:
                eps = {
                    "line_id": f"{period}_eps",
                    "period": period,
                    "metric": "eps",
                    "value": eps_value,
                    "unit": "CNY/share",
                    "status": "calculated",
                    "evidence_ids": list(profit.get("evidence_ids", [])),
                    "formula": "parent net profit (CNY mn) / diluted shares (mn)",
                }
                lines.append(eps)
                by_metric_period[("eps", period)] = eps
                notes.append(f"added deterministic {period} EPS={eps_value:.4f}")
            else:
                old = eps.get("value")
                if old is None or abs(float(old) - eps_value) > max(abs(eps_value) * 0.005, 0.005):
                    notes.append(f"replaced {period} EPS {old} -> {eps_value:.4f}")
                eps.update(
                    value=eps_value,
                    unit="CNY/share",
                    status="calculated",
                    formula="parent net profit (CNY mn) / diluted shares (mn)",
                )

    periods = sorted({str(row.get("period", "")) for row in lines if re.search(r"20\d{2}E", str(row.get("period", "")), re.I)})
    for period in periods:
        revenue = by_metric_period.get(("revenue", period))
        gross_margin = by_metric_period.get(("gross_margin", period))
        gross_profit = by_metric_period.get(("gross_profit", period))
        if revenue and gross_margin and revenue.get("value") is not None and gross_margin.get("value") is not None:
            margin_value = float(gross_margin["value"])
            if margin_value > 1.0:
                margin_value /= 100.0
            calculated_gp = float(revenue["value"]) * margin_value
            if gross_profit is None:
                gross_profit = {
                    "line_id": f"{period}_gross_profit",
                    "period": period,
                    "metric": "gross_profit",
                    "value": calculated_gp,
                    "unit": str(revenue.get("unit", "CNY mn")),
                    "status": "calculated",
                    "evidence_ids": list(dict.fromkeys([*revenue.get("evidence_ids", []), *gross_margin.get("evidence_ids", [])])),
                    "formula": "revenue x gross margin",
                }
                lines.append(gross_profit)
                by_metric_period[("gross_profit", period)] = gross_profit
                notes.append(f"added deterministic {period} gross profit={calculated_gp:.4f}")
            else:
                old = gross_profit.get("value")
                if old is None or abs(float(old) - calculated_gp) > max(abs(calculated_gp) * 0.005, 1.0):
                    notes.append(f"replaced {period} gross profit {old} -> {calculated_gp:.4f}")
                gross_profit.update(value=calculated_gp, status="calculated", formula="revenue x gross margin")
            cost_of_sales = by_metric_period.get(("cost_of_sales", period))
            calculated_cost = float(revenue["value"]) - calculated_gp
            if cost_of_sales is None:
                cost_of_sales = {
                    "line_id": f"{period}_cost_of_sales",
                    "period": period,
                    "metric": "cost_ofsales",
                    "value": calculated_cost,
                    "unit": str(revenue.get("unit", "CNY mn")),
                    "status": "calculated",
                    "evidence_ids": list(gross_profit.get("evidence_ids", [])),
                    "formula": "revenue - gross profit",
                }
                lines.append(cost_of_sales)
                by_metric_period[("cost_of_sales", period)] = cost_of_sales
            else:
                old = cost_of_sales.get("value")
                if old is None or abs(float(old) - calculated_cost) > max(abs(calculated_cost) * 0.005, 1.0):
                    notes.append(f"replaced {period} cost of sales {old} -> {calculated_cost:.4f}")
                cost_of_sales.update(
                    value=calculated_cost,
                    status="calculated",
                    formula="revenue - gross profit",
                )

        operating_profit = by_metric_period.get(("operating_profit", period))
        finance_other = by_metric_period.get(("finance_other", period))
        income_tax = by_metric_period.get(("income_tax", period))
        minority = by_metric_period.get(("minority_interest", period))
        parent_profit = by_metric_period.get(("parent_profit", period))
        if revenue and revenue.get("value") not in (None, 0) and operating_profit and operating_profit.get("value") is not None:
            calculated_margin = float(operating_profit["value"]) / float(revenue["value"]) * 100.0
            operating_margin = by_metric_period.get(("operating_margin", period))
            if operating_margin is not None:
                operating_margin.update(
                    value=calculated_margin,
                    unit="%",
                    status="calculated",
                    formula="operating profit / revenue",
                )
        if all(
            row is not None and row.get("value") is not None
            for row in (operating_profit, finance_other, income_tax, minority)
        ):
            calculated_parent = (
                float(operating_profit["value"])
                + float(finance_other["value"])
                - abs(float(income_tax["value"]))
                - abs(float(minority["value"]))
            )
            if parent_profit is None:
                parent_profit = {
                    "line_id": f"{period}_parent_profit",
                    "period": period,
                    "metric": "parent_profit",
                    "value": calculated_parent,
                    "unit": str(operating_profit.get("unit", "CNY mn")),
                    "status": "calculated",
                    "evidence_ids": [],
                    "formula": "operating profit + finance/other - tax - minority interest",
                }
                lines.append(parent_profit)
                by_metric_period[("parent_profit", period)] = parent_profit
            else:
                old = parent_profit.get("value")
                if old is None or abs(float(old) - calculated_parent) > max(abs(calculated_parent) * 0.005, 1.0):
                    notes.append(f"replaced {period} parent profit {old} -> {calculated_parent:.4f}")
                parent_profit.update(
                    value=calculated_parent,
                    status="calculated",
                    formula="operating profit + finance/other - tax - minority interest",
                )

        if revenue and revenue.get("value") not in (None, 0) and parent_profit and parent_profit.get("value") is not None:
            calculated_margin = float(parent_profit["value"]) / float(revenue["value"]) * 100.0
            net_margin = by_metric_period.get(("net_margin", period))
            if net_margin is not None:
                net_margin.update(
                    value=calculated_margin,
                    unit="%",
                    status="calculated",
                    formula="parent net profit / revenue",
                )

        ocf = by_metric_period.get(("ocf", period))
        if (
            accepted_ocf_ratio is not None
            and parent_profit is not None
            and parent_profit.get("value") is not None
        ):
            calculated_ocf = float(parent_profit["value"]) * accepted_ocf_ratio
            formula = (
                "OCF = parent net profit x accepted OCF/NI ratio "
                f"({accepted_ocf_ratio:.6g}x)"
            )
            if ocf is None:
                ocf = {
                    "line_id": f"{period}_ocf",
                    "period": period,
                    "metric": "ocf",
                    "value": calculated_ocf,
                    "unit": str(parent_profit.get("unit", "CNY mn")),
                    "status": "calculated",
                    "evidence_ids": list(parent_profit.get("evidence_ids", [])),
                    "formula": formula,
                }
                lines.append(ocf)
                by_metric_period[("ocf", period)] = ocf
                notes.append(f"added deterministic {period} OCF={calculated_ocf:.4f}")
            else:
                old = ocf.get("value")
                if old is None or abs(float(old) - calculated_ocf) > max(
                    abs(calculated_ocf) * 0.005, 1.0
                ):
                    notes.append(
                        f"replaced {period} OCF {old} -> {calculated_ocf:.4f}"
                    )
                ocf.update(
                    value=calculated_ocf,
                    unit=str(parent_profit.get("unit", "CNY mn")),
                    status="calculated",
                    formula=formula,
                )
        capex = by_metric_period.get(("capex", period))
        if not ocf or not capex or ocf.get("value") is None or capex.get("value") is None:
            continue
        fcf_value = float(ocf["value"]) - abs(float(capex["value"]))
        fcf = by_metric_period.get(("fcf", period))
        if fcf is None:
            fcf = {
                "line_id": f"{period}_fcf",
                "period": period,
                "metric": "fcf",
                "value": fcf_value,
                "unit": str(ocf.get("unit", "CNY mn")),
                "status": "calculated",
                "evidence_ids": list(dict.fromkeys([*ocf.get("evidence_ids", []), *capex.get("evidence_ids", [])])),
                "formula": "OCF - abs(capex)",
            }
            lines.append(fcf)
            by_metric_period[("fcf", period)] = fcf
            notes.append(f"added deterministic {period} FCF={fcf_value:.4f}")
        else:
            old = fcf.get("value")
            if old is None or abs(float(old) - fcf_value) > max(abs(fcf_value) * 0.01, 1.0):
                notes.append(f"replaced {period} FCF {old} -> {fcf_value:.4f}")
            fcf.update(value=fcf_value, status="calculated", formula="OCF - abs(capex)")

    # A growth assumption must reconcile to the canonical revenue series.  The
    # model can explain the driver, but application code owns the arithmetic.
    revenue_by_period = {
        str(row.get("period", "")): float(row["value"])
        for row in lines
        if _metric(row) == "revenue" and row.get("value") is not None
    }
    growth_by_period: dict[str, float] = {}
    for period, current in revenue_by_period.items():
        match = re.fullmatch(r"(20\d{2})E", period, re.I)
        if not match:
            continue
        prior_period = f"{int(match.group(1)) - 1}E"
        prior = revenue_by_period.get(prior_period)
        if prior not in (None, 0):
            growth_by_period[period] = (current / prior - 1.0) * 100.0

    def _reconcile_public_revenue_growth(text: object) -> tuple[str, int]:
        rendered = str(text or "")
        replacements = 0
        for period, growth in growth_by_period.items():
            year = period[:4]
            period_pattern = rf"(?:FY)?{year[-2:]}E|{year}E"
            lines_out: list[str] = []
            for line in rendered.splitlines():
                if (
                    re.search(period_pattern, line, re.I)
                    and not re.search(r"牛市|熊市|bull|bear|敏感", line, re.I)
                ):
                    pattern = re.compile(
                        rf"((?:(?:FY)?(?:{year[-2:]}|{year})E).{{0,8}}?"
                        r"(?:收入|营收|revenue).{0,24}?(?:增速|增长|growth)"
                        r"[^\d+\-]{0,16})([+\-]?\d+(?:\.\d+)?)(\s*%)",
                        re.I,
                    )
                    line, count = pattern.subn(
                        lambda match: match.group(1) + f"{growth:+.1f}" + match.group(3),
                        line,
                        count=1,
                    )
                    replacements += count
                    compact_pattern = re.compile(
                        rf"((?:FY)?(?:{year[-2:]}|{year})E\s*"
                        r"[\d,.]+\s*(?:亿元|CNY\s*(?:mn|bn))\s*[（(])"
                        r"([+\-]?\d+(?:\.\d+)?)(\s*%[）)])",
                        re.I,
                    )
                    line, count = compact_pattern.subn(
                        lambda match: match.group(1) + f"{growth:+.1f}" + match.group(3),
                        line,
                        count=1,
                    )
                    replacements += count
                lines_out.append(line)
            rendered = "\n".join(lines_out)
        return rendered, replacements

    public_growth_fields = (
        "investment_conclusion_and_core_conflict",
        "company_disaggregation",
        "industry_cycle_and_competition",
        "autonomous_forecast_model",
        "thesis_financial_bridge",
        "accounting_and_capital_allocation",
        "expectation_gap_and_market_pricing",
        "valuation_closure",
        "risks_catalysts_verification",
    )
    growth_replacements = 0
    for field in public_growth_fields:
        reconciled, count = _reconcile_public_revenue_growth(payload.get(field, ""))
        payload[field] = reconciled
        growth_replacements += count
    for row in payload.get("forecast_takeaways", []) or []:
        for field in ("takeaway", "evidence_anchor", "financial_implication", "confidence_and_risk"):
            reconciled, count = _reconcile_public_revenue_growth(row.get(field, ""))
            row[field] = reconciled
            growth_replacements += count
    for row in payload.get("core_theses", []) or []:
        for field in ("takeaway", "financial_transmission", "market_pricing", "falsification_gate"):
            reconciled, count = _reconcile_public_revenue_growth(row.get(field, ""))
            row[field] = reconciled
            growth_replacements += count
    if growth_replacements:
        notes.append(
            f"reconciled {growth_replacements} public revenue growth claim(s) to canonical series"
        )

    for assumption in payload.get("forecast_assumptions", []) or []:
        parameter = str(assumption.get("parameter", ""))
        if not re.search(r"revenue\s*growth|收入增速", parameter, re.I):
            continue
        match = re.search(r"(?:FY)?(20\d{2}|\d{2})E", parameter, re.I)
        if not match:
            continue
        year = int(match.group(1))
        if year < 100:
            year += 2000
        period = f"{year}E"
        prior_period = f"{year - 1}E"
        current = revenue_by_period.get(period)
        prior = revenue_by_period.get(prior_period)
        if current is None or prior in (None, 0):
            continue
        growth = (current / prior - 1.0) * 100.0
        old = str(assumption.get("base_case", ""))
        assumption["base_case"] = (
            f"{growth:+.1f}% ({current:,.0f} CNY mn; calculated from "
            f"canonical {prior_period}/{period} revenue)"
        )
        if old != assumption["base_case"]:
            notes.append(
                f"reconciled {period} revenue growth assumption to {growth:+.1f}%"
            )

    # Segment mix/margin figures are often analytical estimates while the
    # consolidated margin is anchored to reported accounts.  If an LLM writes
    # an explicit weighted equation that does not add up, withdraw that bridge
    # instead of silently plugging one segment to force the consolidated line.
    weighted_margin_pattern = re.compile(
        r"(\d+(?:\.\d+)?)\s*%\s*[×x*]\s*[^+\n]{0,80}?"
        r"(\d+(?:\.\d+)?)\s*%\s*\+\s*[^%\n]{0,40}?"
        r"(\d+(?:\.\d+)?)\s*%\s*[×x*]\s*[^=→\n]{0,80}?"
        r"(\d+(?:\.\d+)?)\s*%\s*(?:=|→)\s*[^\d\n]{0,24}"
        r"(\d+(?:\.\d+)?)\s*%",
        re.I,
    )
    fy26_gm = by_metric_period.get(("gross_margin", "2026E"))
    canonical_gm = (
        float(fy26_gm["value"])
        if fy26_gm is not None and fy26_gm.get("value") is not None
        else None
    )

    def _withdraw_bad_segment_margin_bridge(text: object) -> tuple[str, int]:
        output_lines: list[str] = []
        withdrawals = 0
        for line in str(text or "").splitlines():
            match = weighted_margin_pattern.search(line)
            if not match:
                output_lines.append(line)
                continue
            weight_a, margin_a, weight_b, margin_b, stated = map(float, match.groups())
            total_weight = weight_a + weight_b
            if total_weight <= 0 or abs(total_weight - 100.0) > 2.0:
                output_lines.append(line)
                continue
            calculated = (weight_a * margin_a + weight_b * margin_b) / total_weight
            if abs(calculated - stated) <= 0.2:
                output_lines.append(line)
                continue
            canonical_note = (
                f"FY26E合并毛利率{canonical_gm:.1f}%仅作为基于合并报表历史锚的情景假设，"
                if canonical_gm is not None
                else "合并毛利率仅保留为独立情景假设，"
            )
            output_lines.append(
                "分部毛利率桥已撤销：现有分部估计机械加权为"
                f"{calculated:.1f}%，与原文{stated:.1f}%不一致，且公司未披露相关分部毛利率。"
                + canonical_note
                + "不得由该分部拆分证明；待正式分部披露后重建。"
            )
            withdrawals += 1
        return "\n".join(output_lines), withdrawals

    margin_bridge_fields = (
        "investment_conclusion_and_core_conflict",
        "company_disaggregation",
        "autonomous_forecast_model",
        "thesis_financial_bridge",
        "expectation_gap_and_market_pricing",
        "valuation_closure",
    )
    margin_withdrawals = 0
    for field in margin_bridge_fields:
        reconciled, count = _withdraw_bad_segment_margin_bridge(payload.get(field, ""))
        payload[field] = reconciled
        margin_withdrawals += count
    for row in payload.get("core_theses", []) or []:
        reconciled, count = _withdraw_bad_segment_margin_bridge(
            row.get("financial_transmission", "")
        )
        row["financial_transmission"] = reconciled
        margin_withdrawals += count
    for row in payload.get("question_verdicts", []) or []:
        reconciled, count = _withdraw_bad_segment_margin_bridge(
            row.get("model_or_valuation_effect", "")
        )
        row["model_or_valuation_effect"] = reconciled
        margin_withdrawals += count
    if margin_withdrawals:
        notes.append(
            f"withdrew {margin_withdrawals} unreconciled segment margin bridge(s)"
        )

    # Income-statement reconciliation above may have replaced parent profit;
    # make EPS the final dependent calculation, never an LLM-authored residue.
    if shares:
        for row in lines:
            if _metric(row) != "parent_profit" or row.get("value") is None:
                continue
            period = str(row.get("period", ""))
            eps = by_metric_period.get(("eps", period))
            eps_value = float(row["value"]) / shares
            if eps is not None:
                eps.update(
                    value=eps_value,
                    unit="CNY/share",
                    status="calculated",
                    formula="parent net profit (CNY mn) / diluted shares (mn)",
                )

    assumptions = SafeValuationAssumptions.model_validate(payload.get("safe_valuation_assumptions") or {})
    output = DeterministicValuationOutput(diluted_share_count_mn=shares)
    scenario_rows: list[dict] = []
    scenario_values: dict[str, float] = {}
    probability_total = sum(row.probability_pct for row in assumptions.scenarios)
    unique_scenarios = {row.scenario for row in assumptions.scenarios}
    if shares and len(assumptions.scenarios) == 3 and unique_scenarios == {"bull", "base", "bear"}:
        for row in assumptions.scenarios:
            equity_value: float | None = None
            eps: float | None = None
            if row.valuation_method == "PE" and row.parent_net_profit_cny_mn is not None and row.valuation_multiple is not None:
                eps = row.parent_net_profit_cny_mn / shares
                equity_value = row.parent_net_profit_cny_mn * row.valuation_multiple
            elif row.valuation_method == "direct_equity_value" and row.direct_equity_value_cny_mn is not None:
                equity_value = row.direct_equity_value_cny_mn
            fair_value = equity_value / shares if equity_value is not None else None
            if fair_value is not None:
                scenario_values[row.scenario] = fair_value
            scenario_rows.append(
                {
                    "scenario": row.scenario,
                    "probability_pct": row.probability_pct,
                    "parent_net_profit_cny_mn": row.parent_net_profit_cny_mn,
                    "eps_cny": eps,
                    "valuation_method": row.valuation_method,
                    "valuation_multiple": row.valuation_multiple,
                    "equity_value_cny_mn": equity_value,
                    "fair_value_per_share_cny": fair_value,
                    "assumption_summary": row.assumption_summary,
                }
            )
        output.scenario_rows = scenario_rows
        if len(scenario_values) == 3 and abs(probability_total - 100.0) <= 0.6:
            weighted = sum(
                row.probability_pct * scenario_values[row.scenario] / 100.0
                for row in assumptions.scenarios
            )
            option_equity_value = assumptions.optionality_equity_value_cny_mn
            optionality_rows: list[dict] = []
            if assumptions.optionality_inputs:
                option_equity_value = 0.0
                for item in assumptions.optionality_inputs:
                    metric_key = re.sub(
                        r"[^a-z0-9]+", "", str(item.metric_name or "").lower()
                    )
                    # An incremental bull-vs-base value is already represented
                    # by the probability-weighted scenario distribution. Adding
                    # it again as optionality double counts the same operating
                    # outcome. Independent direct-equity-value second curves
                    # remain eligible.
                    if metric_key == "incrementalequityvalue":
                        notes.append(
                            f"excluded overlapping optionality '{item.name}': "
                            "incremental scenario value is already probability-weighted"
                        )
                        continue
                    equity_value = (
                        item.metric_value_cny_mn
                        * item.valuation_multiple
                        * item.probability_pct / 100.0
                        * item.ownership_pct / 100.0
                        * (1.0 - item.execution_haircut_pct / 100.0)
                    )
                    option_equity_value += equity_value
                    optionality_rows.append(
                        {
                            "name": item.name,
                            "metric_name": item.metric_name,
                            "metric_value_cny_mn": item.metric_value_cny_mn,
                            "valuation_multiple": item.valuation_multiple,
                            "probability_pct": item.probability_pct,
                            "ownership_pct": item.ownership_pct,
                            "execution_haircut_pct": item.execution_haircut_pct,
                            "equity_value_cny_mn": equity_value,
                            "per_share_value_cny": equity_value / shares,
                            "evidence_ids": item.evidence_ids,
                            "assumption_summary": item.assumption_summary,
                        }
                    )
            option_per_share = option_equity_value / shares
            other_per_share = assumptions.other_adjustments_equity_value_cny_mn / shares
            fair_value = weighted + option_per_share + other_per_share
            output.probability_weighted_core_value_cny = weighted
            output.optionality_rows = optionality_rows
            output.optionality_per_share_cny = option_per_share
            output.other_adjustments_per_share_cny = other_per_share
            output.fair_value_per_share_cny = fair_value
            if assumptions.current_price_cny and assumptions.current_price_cny > 0:
                output.expected_return_pct = (fair_value / assumptions.current_price_cny - 1.0) * 100.0
            base_value = scenario_values["base"]
            bear_value = scenario_values["bear"]
            required_price = base_value / ((1.0 + assumptions.required_annual_return_pct / 100.0) ** assumptions.holding_period_years)
            mos_price = base_value * (1.0 - assumptions.margin_of_safety_pct / 100.0)
            bear_constraint = bear_value / (1.0 - assumptions.maximum_bear_loss_pct / 100.0)
            safe_price = min(required_price, mos_price, bear_constraint)
            output.required_return_price_cny = required_price
            output.margin_of_safety_price_cny = mos_price
            output.bear_loss_constraint_price_cny = bear_constraint
            output.safe_buy_price_ceiling_cny = safe_price
            output.suggested_buy_zone_low_cny = safe_price * 0.9
            output.fundamental_floor_cny = bear_value
            output.status = "closed"
            output.formula_notes = [
                "scenario EPS = parent net profit (CNY mn) / diluted shares (mn)",
                "PE fair value/share = scenario EPS x selected PE",
                "probability-weighted core value = sum(probability x scenario fair value/share)",
                "optionality equity value = metric x multiple x probability x ownership x (1-execution haircut)",
                "safe ceiling = min(base/(1+required return)^years, base x (1-MOS), bear/(1-max bear loss))",
            ]
            if any("excluded overlapping optionality" in note for note in notes):
                output.formula_notes.append(
                    "incremental bull-vs-base optionality excluded because it overlaps scenario value"
                )

            # Publish the deterministic probability-weighted core value as its
            # own canonical row.  A base-scenario value is not the same metric
            # and must never be overwritten by the weighted result.
            weighted_equity_value = weighted * shares
            weighted_line = None
            for line in lines:
                raw_metric = re.sub(
                    r"[^a-z0-9]+", "", str(line.get("metric", "")).lower()
                )
                raw_id = re.sub(
                    r"[^a-z0-9]+", "", str(line.get("line_id", "")).lower()
                )
                if raw_metric == "equityvalueweighted" or raw_id in {
                    "probabilityweightedcorevalue",
                    "weightedfairvalue",
                }:
                    weighted_line = line
                    old = line.get("value")
                    line.update(
                        line_id="probability_weighted_core_value",
                        period="scenario",
                        metric="equity_value_weighted",
                        value=weighted_equity_value,
                        unit="CNY mn",
                        status="calculated",
                        formula="deterministic probability-weighted scenario equity value",
                    )
                    if old != weighted_equity_value:
                        notes.append(
                            "synchronized weighted equity value "
                            f"{old} -> {weighted_equity_value:.4f}"
                        )
                    break
            if weighted_line is None:
                lines.append(
                    {
                        "line_id": "probability_weighted_core_value",
                        "period": "scenario",
                        "metric": "equity_value_weighted",
                        "value": weighted_equity_value,
                        "unit": "CNY mn",
                        "status": "calculated",
                        "formula": "deterministic probability-weighted scenario equity value",
                    }
                )
                notes.append(
                    "added deterministic probability-weighted core equity value "
                    f"{weighted_equity_value:.4f}"
                )

            # The consolidated per-share fair value is also application-owned
            # once the deterministic closure succeeds.  Synchronize only the
            # exact total-fair-value metric; legacy option/base rows remain
            # untouched and retain their distinct meanings.
            for line in lines:
                raw_metric = re.sub(
                    r"[^a-z0-9]+", "", str(line.get("metric", "")).lower()
                )
                raw_id = re.sub(
                    r"[^a-z0-9]+", "", str(line.get("line_id", "")).lower()
                )
                if raw_metric in {"fairvalueshare", "fairvaluepershare"} or raw_id == "fairvaluepershare":
                    old = line.get("value")
                    line.update(
                        value=fair_value,
                        unit="CNY/share",
                        status="calculated",
                        formula="deterministic total fair value per share",
                    )
                    if old != fair_value:
                        notes.append(
                            "synchronized total fair value per share "
                            f"{old} -> {fair_value:.4f}"
                        )
                    break
        else:
            output.status = "partial"
            output.formula_notes = [f"scenario probabilities must sum to 100%; got {probability_total:.2f}%"]
    elif assumptions.scenarios:
        output.status = "partial"
        output.formula_notes = ["valuation requires bull/base/bear inputs and a validated diluted share count"]

    if output.status == "closed":
        # The application-owned table is the sole source for scenario values,
        # weighted fair value, expected return and safety prices.  Remove stale
        # hand calculations from LLM prose while preserving method rationale.
        valuation_lines = str(payload.get("valuation_closure", "") or "").splitlines()
        deterministic_terms = re.compile(
            r"概率加权|加权股权价值|加权内在价值|每股价值|公允价值|目标价|"
            r"安全买入价|预期收益|expected\s+return|weighted\s+(?:value|equity)",
            re.I,
        )
        kept_lines: list[str] = []
        removed_manual_values = 0
        for line in valuation_lines:
            has_number = bool(re.search(r"\d", line))
            has_manual_math = bool(re.search(r"[=×*]|\bx\b", line, re.I))
            if deterministic_terms.search(line) and (has_number or has_manual_math):
                removed_manual_values += 1
                continue
            kept_lines.append(line)
        if removed_manual_values:
            kept_text = "\n".join(kept_lines).strip()
            payload["valuation_closure"] = (
                kept_text
                + ("\n\n" if kept_text else "")
                + "情景价值、概率加权结果、预期收益与安全价格以本节程序化估值表为唯一数值口径。"
            )
            notes.append(
                f"removed {removed_manual_values} manual deterministic valuation line(s) from prose"
            )

    if (
        output.status == "closed"
        and assumptions.current_price_cny is not None
        and output.safe_buy_price_ceiling_cny is not None
        and assumptions.current_price_cny > output.safe_buy_price_ceiling_cny * 1.02
    ):
        rating_zh = {
            "Buy": "买入",
            "Overweight": "增持",
            "Hold": "中性",
            "Underweight": "减持",
            "Sell": "卖出",
        }[decision.rating.value]
        payload["rating_posture"] = (
            f"{rating_zh}；当前价{assumptions.current_price_cny:.2f}元高于程序化安全买入上限"
            f"{output.safe_buy_price_ceiling_cny:.2f}元，已有持仓按评级管理，"
            "新资金等待价格进入安全区间或基本面证据推动估值输入上修。"
        )
        execution_field = str(payload.get("risks_catalysts_verification", "") or "")
        # Normalization may run more than once (generation, revision, render).
        # Remove the previous application-owned constraint before inserting the
        # current one so the public report never duplicates it.
        execution_field = re.sub(
            r"\*\*程序化执行约束\*\*：[^\n]*(?:\n\n)?",
            "",
            execution_field,
        )
        execution_field = re.sub(
            r"(?:首仓|初始仓位)[^。；\n]{0,160}(?:建立|建仓)[^。；\n]*[。；]?",
            "",
            execution_field,
            flags=re.I,
        )
        safe_lines: list[str] = []
        removed_unsafe_lines = 0
        affirmative_build = re.compile(
            r"(?:建议|可以|可考虑|启动|分批|逐步|择机).{0,24}(?:买入|建仓|加仓)|"
            r"(?:买入|建仓|加仓).{0,24}(?:建议|可以|可考虑|启动|分批|逐步|择机)",
            re.I,
        )
        for line in execution_field.splitlines():
            prices = [
                float(value)
                for value in re.findall(r"(\d+(?:\.\d+)?)\s*元", line)
            ]
            if (
                prices
                and max(prices) > output.safe_buy_price_ceiling_cny * 1.02
                and affirmative_build.search(line)
            ):
                removed_unsafe_lines += 1
                continue
            safe_lines.append(line)
        execution_field = "\n".join(safe_lines).strip()
        if removed_unsafe_lines:
            notes.append(
                f"removed {removed_unsafe_lines} unsafe buy/build line(s) above deterministic ceiling"
            )
        deterministic_constraint = (
            f"**程序化执行约束**：当前价{assumptions.current_price_cny:.2f}元高于安全买入上限"
            f"{output.safe_buy_price_ceiling_cny:.2f}元；不得表述为已经替投资者建仓，也不得建议新资金在安全价之上主动加仓。"
        )
        payload["risks_catalysts_verification"] = (
            deterministic_constraint + "\n\n" + execution_field.strip()
        ).strip()
        notes.append("enforced safe-price execution constraint above the buy ceiling")

    posture = str(payload.get("rating_posture", "") or "")
    latin_chars = len(re.findall(r"[A-Za-z]", posture))
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff]", posture))
    if latin_chars >= 12 and latin_chars > cjk_chars * 1.2:
        payload["rating_posture"] = {
            "Buy": "买入；基本面与估值同时满足要求，按风险预算分阶段执行。",
            "Overweight": "增持；维持积极但审慎的持仓姿态，后续加仓取决于估值与关键证据验证。",
            "Hold": "中性；当前风险收益较均衡，等待盈利、现金流或估值出现更明确的偏离。",
            "Underweight": "减持；降低相对配置，等待下行风险收敛或估值补偿改善。",
            "Sell": "卖出；基本面下行与估值补偿不足，优先控制绝对风险。",
        }[decision.rating.value]
        notes.append("localized English-heavy rating posture into Chinese")

    payload["canonical_model_snapshot"] = lines
    payload["deterministic_valuation"] = output.model_dump()
    return SellSidePMDecision.model_validate(payload), notes


def _table_cell(value: object) -> str:
    return str(value or "—").replace("|", "/").replace("\n", " ").strip()


def _render_segment_economics(rows_in: list[SegmentEconomicsRow]) -> str:
    if not rows_in:
        return ""
    rows = [
        "### 分部经济与价值归属",
        "",
        "| 业务单元 | 经济角色/口径 | 规模与增长 | 利润与现金 | 驱动方程 | 价值归属 | 证据/缺口 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows_in[:8]:
        evidence = ", ".join(row.evidence_ids) or "无编号"
        rows.append(
            f"| {_table_cell(row.business_unit)} | {_table_cell(row.economic_role)}；{row.disclosure_basis} | "
            f"{_table_cell(row.scale_and_growth)} | {_table_cell(row.margin_and_cash)} | "
            f"{_table_cell(row.driver_equation)} | {row.valuation_treatment} | "
            f"{_table_cell(evidence)}；{_table_cell(row.missing_or_next_check)} |"
        )
    return "\n".join(rows)


def _render_business_model_mechanisms(rows_in: list[BusinessModelMechanismRow]) -> str:
    if not rows_in:
        return ""
    rows = [
        "### 商业模式如何运转",
        "",
        "| 经营环节 | 运作方式 | 核心经济变量 | 现金与资本特征 | 证据或缺口 | 分析结论 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows_in[:7]:
        rows.append(
            "| "
            + " | ".join(
                _table_cell(value)
                for value in (
                    row.link,
                    row.how_it_works,
                    row.economic_driver,
                    row.cash_and_capital_feature,
                    row.evidence_or_gap,
                    row.analyst_conclusion,
                )
            )
            + " |"
        )
    return "\n".join(rows)


def _render_industry_drivers(rows_in: list[IndustryDriverRow]) -> str:
    if not rows_in:
        return ""
    rows = [
        "### 行业驱动与财务传导",
        "",
        "| 核心变量 | 状态与方向 | 日期化证据 | 影响业务 | 财务传导 | 置信度/验证 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows_in[:8]:
        rows.append(
            f"| {_table_cell(row.driver)} | {_table_cell(row.current_state_and_direction)} | "
            f"{_table_cell(row.dated_evidence)} | {_table_cell(row.affected_business)} | "
            f"{_table_cell(row.financial_transmission)} | {row.confidence}；{_table_cell(row.next_verification)} |"
        )
    return "\n".join(rows)


def _render_moat_mechanisms(rows_in: list[MoatMechanismRow]) -> str:
    if not rows_in:
        return ""
    rows = [
        "### 护城河的形成机制与经济结果",
        "",
        "| 护城河来源 | 运作机制 | 可观察证据 | 经济结果 | 持续性与威胁 | 判断 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows_in[:5]:
        rows.append(
            "| "
            + " | ".join(
                _table_cell(value)
                for value in (
                    row.moat_source,
                    row.operating_mechanism,
                    row.observed_proof,
                    row.economic_result,
                    row.durability_and_threat,
                    row.verdict,
                )
            )
            + " |"
        )
    return "\n".join(rows)


def _render_accounting_quality(rows_in: list[AccountingQualityRow]) -> str:
    if not rows_in:
        return ""
    rows = [
        "### 财务质量核查",
        "",
        "| 项目 | 最新证据 | 趋势/对照 | 原因判断 | 盈利/现金/ROIC影响 | 裁决 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows_in[:8]:
        rows.append(
            f"| {_table_cell(row.item)} | {_table_cell(row.latest_evidence_and_period)} | "
            f"{_table_cell(row.trend_or_comparator)} | {_table_cell(row.causal_interpretation)} | "
            f"{_table_cell(row.earnings_cash_roic_effect)} | {row.verdict} |"
        )
    return "\n".join(rows)


def _render_alternative_intelligence(rows_in: list[AlternativeIntelligenceDecision]) -> str:
    material = [row for row in rows_in if row.disposition != "rejected"][:4]
    if not material:
        return ""
    rows = [
        "### 私域信息对核心假设的影响",
        "",
        "| 来源/证据 | 有效增量 | 对模型或情景的影响 | 公共验证与下一节点 |",
        "| --- | --- | --- | --- |",
    ]
    for row in material:
        ids = "/".join(row.kpe_ids) or "未编号"
        rows.append(
            f"| {_table_cell(ids + ' / ' + row.evidence_grade)} | {_table_cell(row.claim)} | "
            f"{_table_cell(row.before_after)} | {_table_cell(row.public_crosscheck + '；' + row.falsification_or_next_check)} |"
        )
    rows.append("- 表中私域内容仅呈现已影响核心假设或验证时点的结论；拒绝项与处理日志保留在结构化审计文件中。")
    return "\n".join(rows)


def _render_deterministic_valuation(output: DeterministicValuationOutput) -> str:
    if not output.scenario_rows:
        return "### 程序化估值与安全价\n\n尚无完整牛/基/熊结构化输入；不得发布伪精确安全价。"
    rows = [
        "### 程序化情景估值",
        "",
        "| 情景 | 概率 | 归母净利润(CNY mn) | EPS | 方法/倍数 | 股权价值(CNY mn) | 每股价值 |",
        "| --- | ---: | ---: | ---: | --- | ---: | ---: |",
    ]
    for row in output.scenario_rows:
        multiple = row.get("valuation_multiple")
        method = row.get("valuation_method") or "—"
        method_text = f"{method}/{multiple:.2f}x" if multiple is not None else method
        scenario_label = {
            "bull": "乐观",
            "base": "基准",
            "bear": "悲观",
        }.get(str(row.get("scenario", "")).lower(), str(row.get("scenario", "")))
        rows.append(
            f"| {scenario_label} | {row.get('probability_pct', 0):.1f}% | "
            f"{_display_number(row.get('parent_net_profit_cny_mn'))} | {_display_number(row.get('eps_cny'))} | "
            f"{method_text} | {_display_number(row.get('equity_value_cny_mn'))} | "
            f"{_display_number(row.get('fair_value_per_share_cny'))} |"
        )
    if output.optionality_rows:
        rows.extend(
            [
                "",
                "### 程序化期权价值",
                "",
                "| 期权 | 指标/规模(CNY mn) | 倍数 | 概率 | 权益 | 执行折价 | 股权价值(CNY mn) | 每股价值 |",
                "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in output.optionality_rows:
            metric_label = {
                "direct_equity_value": "直接权益价值",
                "revenue": "收入",
                "profit": "利润",
                "asset_value": "资产价值",
            }.get(str(row.get("metric_name", "")).lower(), row.get("metric_name"))
            rows.append(
                f"| {_table_cell(row.get('name'))} | {_table_cell(metric_label)}/"
                f"{_display_number(row.get('metric_value_cny_mn'))} | "
                f"{_display_number(row.get('valuation_multiple'))}x | "
                f"{_display_number(row.get('probability_pct'))}% | "
                f"{_display_number(row.get('ownership_pct'))}% | "
                f"{_display_number(row.get('execution_haircut_pct'))}% | "
                f"{_display_number(row.get('equity_value_cny_mn'))} | "
                f"{_display_number(row.get('per_share_value_cny'))} |"
            )
    if output.status == "closed":
        rows.extend(
            [
                "",
                "### 安全估值与建仓价格",
                "",
                f"- 概率加权核心价值：{_display_number(output.probability_weighted_core_value_cny)}元/股",
                f"- 期权价值：{_display_number(output.optionality_per_share_cny)}元/股；其他调整：{_display_number(output.other_adjustments_per_share_cny)}元/股",
                f"- 综合公允价值：{_display_number(output.fair_value_per_share_cny)}元/股；相对现价预期收益：{_display_number(output.expected_return_pct)}%",
                f"- 收益率要求价格：{_display_number(output.required_return_price_cny)}元；安全边际价格：{_display_number(output.margin_of_safety_price_cny)}元；熊市约束价格：{_display_number(output.bear_loss_constraint_price_cny)}元",
                f"- **安全买入价上限：{_display_number(output.safe_buy_price_ceiling_cny)}元；建议关注区间：{_display_number(output.suggested_buy_zone_low_cny)}-{_display_number(output.safe_buy_price_ceiling_cny)}元；基本面压力价值：{_display_number(output.fundamental_floor_cny)}元。**",
            ]
        )
    else:
        rows.extend(["", "- 估值输入不完整或概率未闭合，仅供REVIEW，不给出安全买入价。"])
    return "\n".join(rows)


def _render_sell_side_expectations(rows_in: list[SellSideExpectationRow]) -> str:
    observation_labels = {
        "single_broker": "单家机构",
        "multi_broker_range": "多机构区间",
        "verified_consensus": "已核验一致预期",
    }
    evidence_labels = {
        "public_verified": "公开信息已核验",
        "private_text": "私域文字信息",
        "partial": "部分核验",
        "stale": "信息过期",
        "rejected": "未采纳",
    }
    rows = [
        "### 卖方预测、估值与预期差",
        "",
        "| 来源 | 机构/日期 | 预测与估值 | 修订或分歧 | 与本模型差异 | 证据状态 | 决策用途 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows_in:
        source = "/".join(row.source_ids) or "未编号"
        observation = observation_labels.get(row.observation_type, row.observation_type)
        evidence = evidence_labels.get(row.evidence_status, row.evidence_status)
        label = f"{row.institution}（{observation}）/{row.published_at}"
        rows.append(
            "| "
            + " | ".join(
                _table_cell(value)
                for value in (
                    source,
                    label,
                    row.forecast_and_valuation,
                    row.revision_or_dispersion,
                    row.comparison_with_our_model,
                    evidence,
                    row.decision_use,
                )
            )
            + " |"
        )
    rows.append("- 单家机构观点仅代表单点观察；只有明确提供多机构样本和统计口径时才可称为一致预期。")
    return "\n".join(rows)


def _render_valuation_snapshot(output: DeterministicValuationOutput) -> str:
    if output.status != "closed":
        return ""
    return (
        "| 程序化公允价值 | 安全买入价上限 | 建议关注区间 | 熊市压力价值 |\n"
        "| ---: | ---: | ---: | ---: |\n"
        f"| {_display_number(output.fair_value_per_share_cny)}元 | "
        f"{_display_number(output.safe_buy_price_ceiling_cny)}元 | "
        f"{_display_number(output.suggested_buy_zone_low_cny)}-"
        f"{_display_number(output.safe_buy_price_ceiling_cny)}元 | "
        f"{_display_number(output.fundamental_floor_cny)}元 |"
    )


def _render_sell_side_internal_appendix(decision: SellSidePMDecision) -> str:
    """Render detailed workbench material that should not crowd the public memo."""
    sections: list[str] = []
    business_detail = "\n\n".join(
        part
        for part in (
            _render_business_model_mechanisms(decision.business_model_mechanisms),
            _render_segment_economics(decision.segment_economics),
        )
        if part
    ).strip()
    if business_detail:
        sections.append("## 内部附录A：业务机制与分部经济\n\n" + business_detail)

    industry_detail = "\n\n".join(
        part
        for part in (
            _render_industry_drivers(decision.industry_driver_matrix),
            _render_moat_mechanisms(decision.moat_mechanisms),
        )
        if part
    ).strip()
    if industry_detail:
        sections.append("## 内部附录B：行业驱动与护城河机制\n\n" + industry_detail)

    accounting_detail = _render_accounting_quality(decision.accounting_quality_matrix)
    if accounting_detail:
        sections.append("## 内部附录C：财务质量核查明细\n\n" + accounting_detail)

    expectation_detail = "\n\n".join(
        part
        for part in (
            _render_alternative_intelligence(decision.alternative_intelligence_decisions),
            _render_sell_side_expectations(decision.sell_side_expectation_matrix)
            if decision.sell_side_expectation_matrix
            else "",
        )
        if part
    ).strip()
    if expectation_detail:
        sections.append("## 内部附录D：替代信息与卖方预期审计\n\n" + expectation_detail)

    audit_parts = [
        "### 交接完整性审计\n\n" + decision.handoff_integrity_audit.strip(),
        "### 共享模型变更审计\n\n" + decision.shared_model_change_audit.strip(),
        "### 报告质量自检\n\n" + decision.report_quality_self_check.strip(),
    ]
    sections.append(
        "## 内部附录E：模型交接与报告质量审计\n\n"
        + "\n\n".join(part for part in audit_parts if part.strip())
    )
    return "\n\n".join(sections)


def render_sell_side_pm_decision(decision: SellSidePMDecision) -> str:
    """Render one continuous reader-facing Chinese deep-dive report.

    Research questions and their verdict ledger are intentionally internal.
    They guide analysis but are not exposed as a repetitive public Q&A spine.
    """
    if isinstance(decision, PortfolioDecision):
        return render_pm_decision(decision)
    decision, _ = normalize_sell_side_pm_decision(decision)
    rating_label = {
        "Buy": "买入",
        "Overweight": "增持",
        "Hold": "中性",
        "Underweight": "减持",
        "Sell": "卖出",
    }[decision.rating.value]
    return "\n\n".join(
        [
            "# 公司深度研究与投资决策",
            "| 最终评级 | 投资观点 |\n"
            "| --- | --- |\n"
            f"| {rating_label}（{decision.rating.value}） | {decision.rating_posture} |",
            f"> **一句话结论：** {decision.one_line_thesis}",
            "## 一、投资结论\n\n"
            + _demote_embedded_headings(decision.investment_conclusion_and_core_conflict),
            "## 二、公司画像、商业模式与利润池\n\n"
            + _demote_embedded_headings(decision.company_disaggregation),
            "## 三、行业格局、竞争优势与护城河\n\n"
            + _demote_embedded_headings(decision.industry_cycle_and_competition)
            + "\n\n### 护城河判断\n\n"
            + _demote_embedded_headings(decision.moat_evidence_scorecard),
            "## 四、经营质量、财务特征与资本配置\n\n"
            + _demote_embedded_headings(decision.accounting_and_capital_allocation),
            "## 五、核心投资逻辑与关键分歧\n\n"
            + _demote_embedded_headings(decision.thesis_financial_bridge),
            "## 六、盈利预测与关键变量\n\n"
            + _render_forecast_takeaways(decision.forecast_takeaways)
            + "\n\n"
            + _render_reader_forecast_table(decision.canonical_model_snapshot)
            + "\n\n"
            + _render_forecast_assumptions(decision.forecast_assumptions)
            + "\n\n### 模型解释与局限\n\n"
            + _demote_embedded_headings(decision.autonomous_forecast_model),
            "## 七、市场预期差与估值\n\n"
            + _demote_embedded_headings(decision.expectation_gap_and_market_pricing)
            + "\n\n"
            + _render_deterministic_valuation(decision.deterministic_valuation)
            + "\n\n### 估值解释与局限\n\n"
            + _demote_embedded_headings(decision.valuation_closure),
            "## 八、风险、催化剂与跟踪\n\n"
            + _demote_embedded_headings(decision.risks_catalysts_verification),
            _render_sell_side_internal_appendix(decision),
        ]
    )


def render_pm_decision(decision: PortfolioDecision) -> str:
    """Render a PortfolioDecision to the public markdown report shape.

    This final definition intentionally uses ASCII labels for internally joined
    optional details so report rendering remains stable across Windows console
    encodings and saved markdown files.
    """

    def _join(*items: Optional[str]) -> str:
        return "\n\n".join(item for item in items if item)

    thesis = _join(
        decision.investment_thesis,
        f"Business Segment Breakdown: {decision.business_segment_breakdown}"
        if decision.business_segment_breakdown
        else None,
        f"Segment Prosperity Analysis: {decision.segment_prosperity_analysis}"
        if decision.segment_prosperity_analysis
        else None,
        f"Business and industry verdict: {decision.business_driver_map}"
        if decision.business_driver_map
        else None,
        f"Valuation and expectation gap: {decision.expectation_gap}"
        if decision.expectation_gap
        else None,
        f"Market-implied expectation: {decision.market_implied_expectation}"
        if decision.market_implied_expectation
        else None,
        f"Expectation-gap evidence: {decision.expectation_gap_evidence}"
        if decision.expectation_gap_evidence
        else None,
        f"Key data check: {decision.key_data_check}" if decision.key_data_check else None,
        f"Earnings bridge: {decision.earnings_model_bridge}"
        if decision.earnings_model_bridge
        else None,
        f"Forward forecast model: {decision.forward_forecast_model}"
        if decision.forward_forecast_model
        else None,
        f"Valuation framework: {decision.valuation_framework}"
        if decision.valuation_framework
        else None,
        f"Unit-economics bridge: {decision.unit_economics_bridge}"
        if decision.unit_economics_bridge
        else None,
    )

    supporting_evidence = _join(
        f"Industry-native variables: {decision.industry_driver_verdict}"
        if decision.industry_driver_verdict
        else None,
        f"Policy and demand backdrop: {decision.policy_direction_verdict}"
        if decision.policy_direction_verdict
        else None,
        f"Filing internal quality review: {decision.filing_internal_quality_review}"
        if decision.filing_internal_quality_review
        else None,
        (
            "Investment verdict split: "
            + "; ".join(
                part
                for part in [
                    f"company quality={decision.company_quality_verdict}"
                    if decision.company_quality_verdict
                    else None,
                    f"current odds={decision.current_odds_verdict}"
                    if decision.current_odds_verdict
                    else None,
                    f"relative allocation={decision.relative_allocation_verdict}"
                    if decision.relative_allocation_verdict
                    else None,
                ]
                if part
            )
            if any(
                [
                    decision.company_quality_verdict,
                    decision.current_odds_verdict,
                    decision.relative_allocation_verdict,
                ]
            )
            else None
        ),
        f"Management and capital allocation: {decision.management_capital_allocation_verdict}"
        if decision.management_capital_allocation_verdict
        else None,
        f"Shareholder and float structure: {decision.shareholder_structure_verdict}"
        if decision.shareholder_structure_verdict
        else None,
        f"Investor communication: {decision.investor_communication_verdict}"
        if decision.investor_communication_verdict
        else None,
        f"Peer comparison: {decision.peer_selection_verdict}"
        if decision.peer_selection_verdict
        else None,
        f"Peer Comparison Summary: {decision.peer_comparison_summary}"
        if decision.peer_comparison_summary
        else None,
        f"Supply-chain position: {decision.supply_chain_position_verdict}"
        if decision.supply_chain_position_verdict
        else None,
        f"Market behavior validation: {decision.market_behavior_validation}"
        if decision.market_behavior_validation
        else None,
    )

    debate_and_decision_logic = _join(
        decision.bull_bear_debate,
        decision.debate_verdict,
        f"Core bet: {decision.core_bet}" if decision.core_bet else None,
        f"Cycle/prosperity view: {decision.boom_bust_expectation}"
        if decision.boom_bust_expectation
        else None,
        decision.investment_logic_chain,
        f"Probability and payoff: {decision.probability_payoff}"
        if decision.probability_payoff
        else None,
        f"Cycle and valuation: {decision.cycle_valuation_assessment}"
        if decision.cycle_valuation_assessment
        else None,
    )

    catalysts_and_optionality = _join(
        f"Verified catalysts: {decision.material_catalysts}"
        if decision.material_catalysts
        else None,
        f"Thematic valuation bridge: {decision.thematic_valuation_bridge}"
        if decision.thematic_valuation_bridge
        else None,
        f"Strategic optionality: {decision.strategic_optionality_verdict}"
        if decision.strategic_optionality_verdict
        else None,
        f"Project ramp / capacity bridge: {decision.project_ramp_bridge}"
        if decision.project_ramp_bridge
        else None,
        f"Financing / listing scenario: {decision.financing_listing_scenario}"
        if decision.financing_listing_scenario
        else None,
        f"Catalyst path: {decision.catalyst_path}" if decision.catalyst_path else None,
        f"Rejected themes: {decision.rejected_themes}" if decision.rejected_themes else None,
    )

    evidence_gaps_and_coverage = _join(
        f"Unverified key assumptions: {decision.unverified_key_assumptions}"
        if decision.unverified_key_assumptions
        else None,
        f"Research gaps: {decision.evidence_limited_research_gaps}"
        if decision.evidence_limited_research_gaps
        else None,
        f"Supply-demand fallback view: {decision.supply_demand_fallback_view}"
        if decision.supply_demand_fallback_view
        else None,
        f"Data coverage audit: {decision.data_coverage_audit}"
        if decision.data_coverage_audit
        else None,
        f"Buy-side depth audit: {decision.buy_side_depth_audit}"
        if decision.buy_side_depth_audit
        else None,
    )

    execution_posture = _join(
        decision.executive_summary,
        f"Position and conviction: {decision.conviction_and_position}"
        if decision.conviction_and_position
        else None,
        f"Market regime adjustment: {decision.market_regime_adjustment}"
        if decision.market_regime_adjustment
        else None,
        f"Profit-taking / trimming range: {decision.profit_taking_range}"
        if decision.profit_taking_range
        else None,
        f"Watch / re-entry range: {decision.entry_watch_range}"
        if decision.entry_watch_range
        else None,
        f"Target price: {decision.price_target}" if decision.price_target is not None else None,
        f"Time horizon: {decision.time_horizon}" if decision.time_horizon else None,
    )

    continuity = _join(
        f"Prior rating: {decision.prior_rating}" if decision.prior_rating else None,
        f"New evidence since prior: {decision.new_evidence_since_prior}"
        if decision.new_evidence_since_prior
        else None,
        f"Unchanged core facts: {decision.unchanged_core_facts}"
        if decision.unchanged_core_facts
        else None,
        f"Rating change audit: {decision.rating_change_audit}"
        if decision.rating_change_audit
        else None,
    )

    take_away_parts = []
    if decision.reader_takeaway_entry_band:
        take_away_parts.extend(
            [
                f"**Reader Take-away / Build Price Band**: {decision.reader_takeaway_entry_band}",
                "",
            ]
        )
    if decision.value_stock_safety_price:
        take_away_parts.extend(
            [
                "## Safety Price / Defensive Build Anchor",
                "",
                decision.value_stock_safety_price,
                "",
            ]
        )
    if decision.reader_action_guidance:
        take_away_parts.extend(
            [
                f"**Reader Action Guidance / Holders vs Builders**: {decision.reader_action_guidance}",
                "",
            ]
        )
    pm_summary_parts = []
    if decision.pm_summary:
        pm_summary_parts.extend([f"**PM Summary**: {decision.pm_summary}", ""])

    primer_parts = []
    if decision.business_model_supply_chain_primer:
        primer_parts.extend(
            [
                (
                    "**Business Model & Industry Chain Primer**: "
                    f"{decision.business_model_supply_chain_primer}"
                ),
                "",
            ]
        )

    core_question_parts = []
    if decision.core_research_questions:
        core_question_parts.extend(
            [
                (
                    "**Core Research Questions & Debate-Informed Answers**: "
                    f"{decision.core_research_questions}"
                ),
                "",
            ]
        )

    parts = [
        f"**Company Snapshot**: {decision.company_snapshot}",
        "",
        f"**Rating**: {decision.rating.value}",
        "",
        f"**One-Line Thesis**: {decision.one_line_thesis}",
        "",
    ]
    if decision.rating_posture:
        parts.extend([f"**Rating Posture**: {decision.rating_posture}", ""])
    if decision.rating_evidence_audit:
        parts.extend([f"**Rating Evidence Audit**: {decision.rating_evidence_audit}", ""])
    if decision.information_utilization_audit:
        parts.extend(
            [
                f"**Information Utilization Audit**: {decision.information_utilization_audit}",
                "",
            ]
        )
    parts.extend(
        [
            *pm_summary_parts,
            *primer_parts,
            *core_question_parts,
            f"**Investment Thesis**: {thesis}",
            "",
        ]
    )
    if supporting_evidence:
        parts.extend([f"**Supporting Evidence Integration**: {supporting_evidence}", ""])
    parts.extend([f"**Debate & Decision Logic**: {debate_and_decision_logic}", ""])
    parts.extend([f"**Executive Summary**: {decision.executive_summary}", ""])
    if catalysts_and_optionality:
        parts.extend(
            [
                f"**Catalysts & Optionality**: {catalysts_and_optionality}",
                "",
            ]
        )
    if evidence_gaps_and_coverage:
        parts.extend([f"**Evidence Gaps & Data Coverage**: {evidence_gaps_and_coverage}", ""])
    verification_and_falsification = _join(
        decision.verification_and_falsification,
        f"Falsification signals: {decision.falsification_signals}"
        if decision.falsification_signals
        else None,
    )
    parts.extend([f"**Verification & Falsification**: {verification_and_falsification}", ""])
    if decision.verification_calendar:
        parts.extend([f"**Verification Calendar**: {decision.verification_calendar}", ""])
    parts.extend([*take_away_parts, f"**Execution Posture**: {execution_posture}"])
    if continuity:
        parts.extend(["", f"**Decision Continuity**: {continuity}"])
    return "\n".join(parts)


# Some test/plugin loaders execute this module through ``spec_from_file_location``
# without first registering it in ``sys.modules``.  Pydantic then cannot resolve
# postponed enum/Literal annotations lazily.  Rebuild against the module globals
# once so both normal imports and plugin-style loads receive complete schemas.
for _schema_model in (
    UnderwritingResearchPlan,
    ResearchPlan,
    TraderProposal,
    SellSidePMDecision,
    PortfolioDecision,
):
    if hasattr(_schema_model, "model_rebuild"):
        _schema_model.model_rebuild(_types_namespace=globals())
