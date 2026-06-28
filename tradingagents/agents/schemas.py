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
from typing import Optional

from pydantic import BaseModel, Field


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


# ---------------------------------------------------------------------------
# Research Manager
# ---------------------------------------------------------------------------


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
        description=(
            "One or two sentences stating the core bet: what future business, "
            "cycle, policy, product-price, demand, cost, or valuation variable "
            "the investor is underwriting."
        ),
    )
    expectation_gap: str = Field(
        description=(
            "Explain whether the market appears to have priced the thesis, or "
            "where a plausible expectation gap remains. Mention evidence and caveats."
        ),
    )
    probability_payoff: str = Field(
        description=(
            "Summarize probability and payoff: likelihood of the core bet, upside "
            "if it works, downside if it fails, and why the rating follows."
        ),
    )
    cycle_valuation_assessment: str = Field(
        description=(
            "Classify the valuation x prosperity setup and explain the fair "
            "calibration: low/high valuation versus low/high prosperity, why the "
            "setup deserves the recommendation, and what would change it."
        ),
    )
    catalyst_path: str = Field(
        description=(
            "Near- to medium-term events or data releases that could make the "
            "market reprice the thesis."
        ),
    )
    falsification_signals: str = Field(
        description=(
            "Specific signals that would prove the thesis wrong or require a "
            "rating downgrade."
        ),
    )
    conviction_level: str = Field(
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
            "missing evidence from adverse evidence, and explain how it caps the "
            "rating, position size, or conviction."
        ),
    )
    data_coverage_audit: Optional[str] = Field(
        default=None,
        description=(
            "Summarize which supplied data modules were ready, partial, failed, or "
            "missing when that affects the recommendation. Name thesis-critical gaps "
            "and state how they cap conviction."
        ),
    )


def render_research_plan(plan: ResearchPlan) -> str:
    """Render a ResearchPlan to markdown for storage and the trader's prompt context."""
    parts = [
        "**Investment Decision Memo**",
        "",
        f"**Rating**: {plan.recommendation.value}",
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
        parts.extend(["", "### Investor Communication Verdict", plan.investor_communication_verdict])
    if plan.policy_direction_verdict:
        parts.extend(["", "### Policy Direction Verdict", plan.policy_direction_verdict])
    if plan.industry_driver_verdict:
        parts.extend(["", "### Industry Driver Verdict", plan.industry_driver_verdict])
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
        parts.extend(["", "### Strategic Optionality Verdict", plan.strategic_optionality_verdict])
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
            "case. If the justified action is only a starter/observation position "
            "pending one decisive disclosure, prefer Hold with positive-bias "
            "guidance unless the report independently proves Overweight through "
            "business quality, operating trend, valuation gap, catalyst path, and "
            "bounded downside."
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
            "not a simple average. If evidence is unavailable, mark it missing and cap "
            "confidence rather than filling the matrix with generic industry prose."
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
            "List thesis-critical data gaps and explain how they limit conviction. "
            "Do not use this as a vague disclaimer: name the exact missing product, "
            "spread, inventory, freight, capacity, policy, or demand data and what "
            "would change the rating if verified. For banks, name the exact missing "
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
            "timing, or data coverage. For each weakness, say whether it caps "
            "conviction, requires follow-up, or merely stays out of valuation."
        ),
    )
    data_coverage_audit: Optional[str] = Field(
        default=None,
        description=(
            "Concise audit of the supplied evidence set: which precomputed data "
            "modules were ready, partial, failed, or missing; whether any gap is "
            "thesis-critical; and how the gap affects confidence or next checks."
        ),
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
