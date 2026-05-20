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
            "Conversational summary of the key points from both sides of the "
            "debate, ending with which arguments led to the recommendation. "
            "Speak naturally, as if to a teammate."
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
    strategic_optionality_verdict: Optional[str] = Field(
        default=None,
        description=(
            "Summarize important but non-base-case optionality such as second growth "
            "curves, investee holdings, asset revaluation, or thematic catalysts, "
            "including why they matter and what would upgrade them."
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
        f"**Recommendation**: {plan.recommendation.value}",
        "",
        f"**Core Bet**: {plan.core_bet}",
        "",
        f"**Expectation Gap**: {plan.expectation_gap}",
        "",
        f"**Probability And Payoff**: {plan.probability_payoff}",
        "",
        f"**Cycle-Valuation Assessment**: {plan.cycle_valuation_assessment}",
        "",
        f"**Catalyst Path**: {plan.catalyst_path}",
        "",
        f"**Falsification Signals**: {plan.falsification_signals}",
        "",
        f"**Conviction Level**: {plan.conviction_level}",
        "",
        f"**Rationale**: {plan.rationale}",
        "",
        f"**Strategic Actions**: {plan.strategic_actions}",
    ]
    if plan.prior_rating:
        parts.extend(["", f"**Prior Rating**: {plan.prior_rating}"])
    if plan.new_evidence_since_prior:
        parts.extend(["", f"**New Evidence Since Prior**: {plan.new_evidence_since_prior}"])
    if plan.unchanged_core_facts:
        parts.extend(["", f"**Unchanged Core Facts**: {plan.unchanged_core_facts}"])
    if plan.rating_change_audit:
        parts.extend(["", f"**Rating Change Audit**: {plan.rating_change_audit}"])
    if plan.material_catalysts:
        parts.extend(["", f"**Material Catalysts**: {plan.material_catalysts}"])
    if plan.thematic_valuation_bridge:
        parts.extend(["", f"**Thematic Valuation Bridge**: {plan.thematic_valuation_bridge}"])
    if plan.rejected_themes:
        parts.extend(["", f"**Rejected Themes**: {plan.rejected_themes}"])
    if plan.peer_selection_verdict:
        parts.extend(["", f"**Peer Selection Verdict**: {plan.peer_selection_verdict}"])
    if plan.supply_chain_position_verdict:
        parts.extend(["", f"**Supply-Chain Position Verdict**: {plan.supply_chain_position_verdict}"])
    if plan.earnings_model_bridge:
        parts.extend(["", f"**Earnings Model Bridge**: {plan.earnings_model_bridge}"])
    if plan.market_implied_expectation:
        parts.extend(["", f"**Market-Implied Expectation**: {plan.market_implied_expectation}"])
    if plan.company_quality_verdict:
        parts.extend(["", f"**Company Quality Verdict**: {plan.company_quality_verdict}"])
    if plan.current_odds_verdict:
        parts.extend(["", f"**Current Odds Verdict**: {plan.current_odds_verdict}"])
    if plan.relative_allocation_verdict:
        parts.extend(["", f"**Relative Allocation Verdict**: {plan.relative_allocation_verdict}"])
    if plan.management_capital_allocation_verdict:
        parts.extend(["", f"**Management & Capital Allocation Verdict**: {plan.management_capital_allocation_verdict}"])
    if plan.shareholder_structure_verdict:
        parts.extend(["", f"**Shareholder Structure Verdict**: {plan.shareholder_structure_verdict}"])
    if plan.investor_communication_verdict:
        parts.extend(["", f"**Investor Communication Verdict**: {plan.investor_communication_verdict}"])
    if plan.policy_direction_verdict:
        parts.extend(["", f"**Policy Direction Verdict**: {plan.policy_direction_verdict}"])
    if plan.industry_driver_verdict:
        parts.extend(["", f"**Industry Driver Verdict**: {plan.industry_driver_verdict}"])
    if plan.strategic_optionality_verdict:
        parts.extend(["", f"**Strategic Optionality Verdict**: {plan.strategic_optionality_verdict}"])
    if plan.data_coverage_audit:
        parts.extend(["", f"**Data Coverage Audit**: {plan.data_coverage_audit}"])
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
            "Underweight / Sell, picked based on the analysts' debate."
        ),
    )
    company_snapshot: str = Field(
        description=(
            "A short, self-contained company introduction for public sharing. "
            "Identify what the company does, its main business or profit drivers, "
            "and why those drivers matter to this investment case. Keep it clear "
            "and concise rather than encyclopedic."
        ),
    )
    one_line_thesis: str = Field(
        description=(
            "One sentence that states the investable view in plain language: "
            "what the market may be missing, why the rating follows, and the "
            "main caveat if needed."
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
    reader_action_guidance: Optional[str] = Field(
        default=None,
        description=(
            "Reader-facing action guidance split into two audiences: investors who "
            "already hold a full or large position, and investors who are preparing "
            "to build a position. The advice must fit the final rating. For Buy or "
            "Overweight, explain how to build or add in stages, what evidence or "
            "price/valuation zone justifies adding, and how much dry powder to keep. "
            "For Hold, explain what full holders should monitor or rebalance, and "
            "what new buyers should wait for before initiating. For Underweight or "
            "Sell, explain how full holders should reduce or hedge, and what lower "
            "price/valuation band would make new entry reasonable if fundamentals "
            "remain intact. If no responsible build zone exists, say so explicitly."
        ),
    )
    business_driver_map: str = Field(
        description=(
            "A compact map of the 3-5 variables that really drive the company's "
            "business value and stock performance. Name the variables, explain "
            "their direction of impact, and tie them to this company rather than "
            "generic industry factors. Prefer a dense paragraph or short semicolon "
            "separated list."
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
            "it readable and information-dense."
        ),
    )
    executive_summary: str = Field(
        description=(
            "A concise action plan covering entry strategy, position sizing, "
            "key risk levels, and time horizon. Write for readers who may only "
            "see this Portfolio Manager Decision excerpt. Keep it compressed: "
            "two to three sentences or a short paragraph, not a full investment plan."
        ),
    )
    verification_and_falsification: str = Field(
        description=(
            "A concise checklist of the next verification points and the signals "
            "that would falsify or downgrade the thesis. Use concrete observable "
            "items from the report, such as earnings, orders, product prices, "
            "margins, cash flow, policy, inventory, technical levels, or sector data."
        ),
    )
    investment_thesis: str = Field(
        description=(
            "Focused reasoning anchored in specific evidence from the analysts' "
            "debate. Preserve the main analytical path from the full report "
            "without turning it into an exhaustive data dump; explain why the "
            "rating follows from thesis, expectation gap, probability/payoff, "
            "and key risks."
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
            "underpricing or overpricing, and what evidence suggests that."
        ),
    )
    probability_payoff: Optional[str] = Field(
        default=None,
        description=(
            "Summarize win probability, upside payoff, downside risk, and whether "
            "the risk/reward justifies the rating."
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
            "orders, inventory, or sector moves."
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
            "would change the rating if verified."
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
            "must move under bull/base/bear cases."
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
        f"Business and industry verdict: {decision.business_driver_map}"
        if decision.business_driver_map
        else None,
        f"Industry-native variables: {decision.industry_driver_verdict}"
        if decision.industry_driver_verdict
        else None,
        f"Policy and demand backdrop: {decision.policy_direction_verdict}"
        if decision.policy_direction_verdict
        else None,
        f"Valuation and expectation gap: {decision.expectation_gap}"
        if decision.expectation_gap
        else None,
        f"Market-implied expectation: {decision.market_implied_expectation}"
        if decision.market_implied_expectation
        else None,
        f"Earnings bridge: {decision.earnings_model_bridge}"
        if decision.earnings_model_bridge
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
        f"Supply-chain position: {decision.supply_chain_position_verdict}"
        if decision.supply_chain_position_verdict
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

    catalysts_optionality_and_falsification = _join(
        f"Verified catalysts: {decision.material_catalysts}"
        if decision.material_catalysts
        else None,
        f"Thematic valuation bridge: {decision.thematic_valuation_bridge}"
        if decision.thematic_valuation_bridge
        else None,
        f"Strategic optionality: {decision.strategic_optionality_verdict}"
        if decision.strategic_optionality_verdict
        else None,
        f"Catalyst path: {decision.catalyst_path}" if decision.catalyst_path else None,
        f"Rejected themes: {decision.rejected_themes}" if decision.rejected_themes else None,
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
    if decision.reader_action_guidance:
        take_away_parts.extend(
            [
                f"**Reader Action Guidance / Holders vs Builders**: {decision.reader_action_guidance}",
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
        *take_away_parts,
        f"**Investment Thesis**: {thesis}",
        "",
        f"**Debate & Decision Logic**: {debate_and_decision_logic}",
        "",
    ]
    if catalysts_optionality_and_falsification:
        parts.extend(
            [
                f"**Catalysts, Optionality & Falsification**: {catalysts_optionality_and_falsification}",
                "",
            ]
        )
    parts.extend(
        [
            f"**Verification & Falsification**: {decision.verification_and_falsification}",
            "",
            f"**Executive Summary**: {execution_posture}",
        ]
    )
    if continuity:
        parts.extend(["", f"**Decision Continuity**: {continuity}"])
    if decision.falsification_signals:
        parts.extend(["", f"**Falsification Signals**: {decision.falsification_signals}"])
    return "\n".join(parts)
