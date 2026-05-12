"""Portfolio Manager: synthesises the risk-analyst debate into the final decision.

Uses LangChain's ``with_structured_output`` so the LLM produces a typed
``PortfolioDecision`` directly, in a single call.  The result is rendered
back to markdown for storage in ``final_trade_decision`` so memory log,
CLI display, and saved reports continue to consume the same shape they do
today.  When a provider does not expose structured output, the agent falls
back gracefully to free-text generation.
"""

from __future__ import annotations

from tradingagents.agents.schemas import PortfolioDecision, render_pm_decision
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_buy_side_thesis_instruction,
    get_evidence_instruction,
    get_focused_report_instruction,
    get_language_instruction,
    get_research_gap_instruction,
    get_supply_demand_fallback_instruction,
)
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)


def create_portfolio_manager(llm):
    structured_llm = bind_structured(llm, PortfolioDecision, "Portfolio Manager")

    def portfolio_manager_node(state) -> dict:
        instrument_context = build_instrument_context(state["company_of_interest"])

        history = state["risk_debate_state"]["history"]
        risk_debate_state = state["risk_debate_state"]
        research_plan = state["investment_plan"]
        trader_plan = state["trader_investment_plan"]

        past_context = state.get("past_context", "")
        lessons_line = (
            f"- Lessons from prior decisions and outcomes:\n{past_context}\n"
            if past_context
            else ""
        )

        prompt = f"""As the Portfolio Manager, synthesize the risk analysts' debate and deliver the final trading decision.

{instrument_context}

---

**Rating Scale** (use exactly one):
- **Buy**: Clear core bet, strong evidence/proxy support, attractive probability/payoff, and identifiable catalysts
- **Overweight**: Positive expected value but some evidence gaps remain; suitable for gradual or partial exposure
- **Hold**: No clear tradable thesis, weak expectation gap, or ordinary probability/payoff
- **Underweight**: Negative expected value or unattractive payoff, but not enough evidence for a full exit call
- **Sell**: Core thesis deteriorated or downside probability/payoff is clearly unfavorable

**Market-Regime Calibration Rules:**
- The rating is not static. Calibrate it against broad-market mood, market valuation, sector risk, and the stock's own traits.
- Normal bull market: you may be slightly more constructive for reasonably valued, high-quality stocks with catalysts, but do not chase crowded/high-valuation names.
- Normal bear market: be more conservative unless the stock has strong balance sheet, low valuation, resilient cash flow, and clear catalysts.
- Extreme pessimism: do not become mechanically bearish. For resilient companies or depressed value opportunities, consider staged-entry/watch-zone logic.
- Extreme optimism: do not become mechanically bullish. For expensive or high-beta names, emphasize profit-taking and tighter risk control.
- Cyclical, commodity, shipping, high-beta, and event-driven stocks require specific cycle evidence; market mood alone must not determine the rating.
- If bullish/constructive, provide a profit-taking or trimming range. If bearish/cautious, provide an entry or re-entry watch range.

**Research-Gap and Supply-Demand Rules:**
- Missing core operating data is a research gap, not neutral evidence.
- Do not let PE/PB and technical indicators replace missing product price, spread, inventory, freight-rate, capacity, policy, or order-book evidence.
- If micro evidence is unavailable, use product-specific macro supply-demand evidence where possible: upstream cost, downstream demand, capacity, utilization, imports/exports, substitution, policy, seasonality, and storability.
- Macro proxies can support an evidence-limited directional view, but cannot be treated as exact product-price or spread facts.
- If too many thesis-critical assumptions are unverified, reduce conviction and state what data would upgrade or downgrade the rating.

**Buy-Side Decision Rules:**
- The final decision must identify the Core Bet. If there is no Core Bet, explain why the rating is Hold or Underweight.
- Evaluate whether the relevant boom-bust expectation can plausibly realize through macro context, industry cycle, company exposure, and available high-frequency/proxy data.
- Use expectation gap: a good company is not enough if the market already priced the thesis; an imperfect company can be interesting if the market underprices an improving driver.
- Use probability/payoff instead of simple evidence counting. Conflicting evidence can still justify a direction when the payoff is asymmetric and the thesis is falsifiable.
- Match position size to conviction. Evidence-limited Overweight should usually be a staged or starter position, not a full-conviction Buy.

**Context:**
- Research Manager's investment plan: **{research_plan}**
- Trader's transaction proposal: **{trader_plan}**
{lessons_line}
**Risk Analysts Debate History:**
{history}

---

Be decisive and ground every conclusion in specific evidence from the analysts.
{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_focused_report_instruction()}
If an important investment claim depends on an unverified commodity price, product spread, inventory, policy detail, or exact percentage, list it under an "Unverified Key Assumptions" paragraph instead of treating it as fact.{get_language_instruction()}"""

        final_trade_decision = invoke_structured_or_freetext(
            structured_llm,
            llm,
            prompt,
            render_pm_decision,
            "Portfolio Manager",
        )

        new_risk_debate_state = {
            "judge_decision": final_trade_decision,
            "history": risk_debate_state["history"],
            "aggressive_history": risk_debate_state["aggressive_history"],
            "conservative_history": risk_debate_state["conservative_history"],
            "neutral_history": risk_debate_state["neutral_history"],
            "latest_speaker": "Judge",
            "current_aggressive_response": risk_debate_state["current_aggressive_response"],
            "current_conservative_response": risk_debate_state["current_conservative_response"],
            "current_neutral_response": risk_debate_state["current_neutral_response"],
            "count": risk_debate_state["count"],
        }

        return {
            "risk_debate_state": new_risk_debate_state,
            "final_trade_decision": final_trade_decision,
        }

    return portfolio_manager_node
