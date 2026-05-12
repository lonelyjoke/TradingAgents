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


def render_research_plan(plan: ResearchPlan) -> str:
    """Render a ResearchPlan to markdown for storage and the trader's prompt context."""
    return "\n".join([
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
    ])


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
    executive_summary: str = Field(
        description=(
            "A concise action plan covering entry strategy, position sizing, "
            "key risk levels, and time horizon. Two to four sentences."
        ),
    )
    investment_thesis: str = Field(
        description=(
            "Focused reasoning anchored in specific evidence from the analysts' "
            "debate. Do not provide an exhaustive data dump; explain why the "
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
            "overweight, starter position, watch only, trim, or avoid."
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


def render_pm_decision(decision: PortfolioDecision) -> str:
    """Render a PortfolioDecision back to the markdown shape the rest of the system expects.

    Memory log, CLI display, and saved report files all read this markdown,
    so the rendered output preserves the exact section headers (``**Rating**``,
    ``**Executive Summary**``, ``**Investment Thesis**``) that downstream
    parsers and the report writers already handle.
    """
    parts = [
        f"**Rating**: {decision.rating.value}",
        "",
        f"**Executive Summary**: {decision.executive_summary}",
        "",
        f"**Investment Thesis**: {decision.investment_thesis}",
    ]
    if decision.core_bet:
        parts.extend(["", f"**Core Bet**: {decision.core_bet}"])
    if decision.boom_bust_expectation:
        parts.extend(["", f"**Boom-Bust Expectation**: {decision.boom_bust_expectation}"])
    if decision.expectation_gap:
        parts.extend(["", f"**Expectation Gap**: {decision.expectation_gap}"])
    if decision.probability_payoff:
        parts.extend(["", f"**Probability And Payoff**: {decision.probability_payoff}"])
    if decision.cycle_valuation_assessment:
        parts.extend(["", f"**Cycle-Valuation Assessment**: {decision.cycle_valuation_assessment}"])
    if decision.catalyst_path:
        parts.extend(["", f"**Catalyst Path**: {decision.catalyst_path}"])
    if decision.falsification_signals:
        parts.extend(["", f"**Falsification Signals**: {decision.falsification_signals}"])
    if decision.conviction_and_position:
        parts.extend(["", f"**Conviction And Position**: {decision.conviction_and_position}"])
    if decision.market_regime_adjustment:
        parts.extend(["", f"**Market Regime Adjustment**: {decision.market_regime_adjustment}"])
    if decision.profit_taking_range:
        parts.extend(["", f"**Profit-Taking / Trimming Range**: {decision.profit_taking_range}"])
    if decision.entry_watch_range:
        parts.extend(["", f"**Entry / Re-entry Watch Range**: {decision.entry_watch_range}"])
    if decision.unverified_key_assumptions:
        parts.extend(["", f"**Unverified Key Assumptions**: {decision.unverified_key_assumptions}"])
    if decision.evidence_limited_research_gaps:
        parts.extend(["", f"**Evidence-Limited Research Gaps**: {decision.evidence_limited_research_gaps}"])
    if decision.supply_demand_fallback_view:
        parts.extend(["", f"**Supply-Demand Fallback View**: {decision.supply_demand_fallback_view}"])
    if decision.price_target is not None:
        parts.extend(["", f"**Price Target**: {decision.price_target}"])
    if decision.time_horizon:
        parts.extend(["", f"**Time Horizon**: {decision.time_horizon}"])
    return "\n".join(parts)
