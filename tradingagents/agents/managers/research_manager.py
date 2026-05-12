"""Research Manager: turns the bull/bear debate into a structured investment plan for the trader."""

from __future__ import annotations

from tradingagents.agents.schemas import ResearchPlan, render_research_plan
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_buy_side_thesis_instruction,
    get_evidence_instruction,
    get_fair_cycle_valuation_instruction,
    get_focused_report_instruction,
    get_research_gap_instruction,
    get_supply_demand_fallback_instruction,
)
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)


def create_research_manager(llm):
    structured_llm = bind_structured(llm, ResearchPlan, "Research Manager")

    def research_manager_node(state) -> dict:
        instrument_context = build_instrument_context(state["company_of_interest"])
        history = state["investment_debate_state"].get("history", "")

        investment_debate_state = state["investment_debate_state"]

        prompt = f"""As the Research Manager and debate facilitator, your role is to critically evaluate this round of debate and deliver a clear, actionable investment plan for the trader.

{instrument_context}

---

**Rating Scale** (use exactly one):
- **Buy**: Strong conviction in the bull thesis; recommend taking or growing the position
- **Overweight**: Constructive view; recommend gradually increasing exposure
- **Hold**: Balanced view; recommend maintaining the current position
- **Underweight**: Cautious view; recommend trimming exposure
- **Sell**: Strong conviction in the bear thesis; recommend exiting or avoiding the position

Commit to a clear stance whenever the core bet has attractive probability/payoff. Reserve Hold for cases where there is no clear tradable thesis, the expectation gap is weak, or the risk/reward is not attractive. Do not use Hold merely because the evidence set is imperfect.

**Buy-Side Thesis Framework:**
- First answer: if we are bullish, what exactly are we betting on?
- Judge whether that boom-bust or business-cycle expectation can plausibly realize using verified evidence, proxy evidence, and bounded inference.
- Separate facts, proxy evidence, inference, and unverified assumptions.
- A thesis can be investable before every data point is proven if the probability/payoff is attractive and the falsification path is clear.
- Prefer Overweight over Hold when the thesis has positive expected value but still has important evidence gaps.
- Prefer Underweight over Hold when the negative thesis has positive expected value but still needs confirmation.
- For every direction, specify expectation gap, probability/payoff, catalyst path, falsification signals, and conviction level.

**Fair Cycle-Valuation Calibration:**
- Judge every stock through the same valuation x prosperity lens.
- Low valuation/low prosperity is not automatically bearish; ask whether pessimism is priced and whether an inflection is plausible.
- High prosperity/high valuation is not automatically bullish; ask whether growth durability and earnings upgrades can digest valuation.
- Low valuation/high prosperity can be attractive, but test whether earnings are sustainable or temporarily inflated.
- High valuation/low prosperity normally requires a clear future inflection, scarce growth, or other special evidence to avoid Underweight.
- The rating should reflect expected value, not style preference.

**Market-Regime Calibration:**
- Start from company evidence, then adjust for market/sector mood.
- In a normal bull market, a high-quality stock with reasonable valuation can receive a slightly more constructive rating, but an expensive/crowded stock should not be upgraded mechanically.
- In a normal bear market, keep ratings more conservative unless valuation, balance sheet, and catalysts are strong.
- In extreme pessimism with depressed valuations, allow contrarian watch or staged-entry logic for resilient companies, but avoid upgrading fragile balance sheets simply because prices are low.
- In extreme optimism with high valuations, require stronger evidence for Buy/Overweight and emphasize trimming discipline.
- For cyclical, commodity, shipping, high-beta, or event-driven stocks, calibrate the rating using the stock's own cycle drivers, not only broad-market mood.

**Evidence-Gap Calibration:**
- Missing core operating data is not neutral evidence. It is a research gap that should reduce conviction in the affected thesis.
- Do not let PE/PB and technical indicators replace missing product-price, spread, inventory, freight-rate, policy, capacity, or order-book evidence.
- If the unavailable data is central to the bull thesis, prefer evidence-limited Overweight/Hold or a staged watch plan over a high-conviction Buy.
- If the unavailable data is central to the bear thesis, do not issue a strong Sell solely because evidence is missing; explain the risk scenario and what would confirm it.
- Hold should mean balanced verified evidence, not "we could not fetch the important data."

**Supply-Demand Fallback:**
- If micro product price, spread, inventory, or freight data is missing, ask whether macro supply-demand evidence can still say something useful.
- This fallback must be specific to the product or route: upstream cost, downstream demand, capacity, utilization, imports/exports, substitution, policy, seasonality, and storability.
- Treat macro proxies as lower-confidence evidence than verified micro prices. They can shape scenarios and watch ranges, but should not be presented as exact product-price conclusions.
- If macro supply-demand evidence points clearly one way, do not default to Hold purely because product quotes are missing; instead state an evidence-limited directional view and what data would confirm or refute it.

---

**Debate History:**
{history}

{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_fair_cycle_valuation_instruction()}
{get_focused_report_instruction()}
If a bull or bear argument contains an exact product price, inventory figure, product spread, percentage change, or date-specific market claim that is not supported by the analyst reports, downgrade that argument and list it as an unverified key assumption."""

        investment_plan = invoke_structured_or_freetext(
            structured_llm,
            llm,
            prompt,
            render_research_plan,
            "Research Manager",
        )

        new_investment_debate_state = {
            "judge_decision": investment_plan,
            "history": investment_debate_state.get("history", ""),
            "bear_history": investment_debate_state.get("bear_history", ""),
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": investment_plan,
            "count": investment_debate_state["count"],
        }

        return {
            "investment_debate_state": new_investment_debate_state,
            "investment_plan": investment_plan,
        }

    return research_manager_node
