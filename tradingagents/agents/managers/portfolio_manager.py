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
    get_earnings_model_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_investor_interaction_instruction,
    get_language_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_material_catalyst_instruction,
    get_policy_planning_instruction,
    get_peer_selection_instruction,
    get_price_earnings_decomposition_instruction,
    get_research_gap_instruction,
    get_supply_demand_fallback_instruction,
    get_supply_chain_selection_instruction,
    get_shareholder_structure_instruction,
    get_three_layer_conclusion_instruction,
    get_thematic_valuation_instruction,
)
from tradingagents.agents.utils.structured import (
    bind_structured,
    invoke_structured_or_freetext,
)
from tradingagents.dataflows.prompt_compaction import (
    compact_debate_history,
    compact_for_prompt,
    compact_risk_history,
    compact_state_fields,
)


def create_portfolio_manager(llm):
    structured_llm = bind_structured(llm, PortfolioDecision, "Portfolio Manager")

    def portfolio_manager_node(state) -> dict:
        instrument_context = build_instrument_context(state["company_of_interest"])

        history = state["risk_debate_state"]["history"]
        risk_debate_state = state["risk_debate_state"]
        research_plan = compact_for_prompt(
            state["investment_plan"],
            label="investment_plan",
            profile="portfolio",
        )
        trader_plan = compact_for_prompt(
            state["trader_investment_plan"],
            label="trader_plan",
            profile="portfolio",
        )
        prompt_contexts = compact_state_fields(state, profile="portfolio")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        filing_intelligence_context = prompt_contexts["filing_intelligence_context"]
        peer_comparison_context = prompt_contexts["peer_comparison_context"]
        supply_chain_comparison_context = prompt_contexts["supply_chain_comparison_context"]
        earnings_model_context = prompt_contexts["earnings_model_context"]
        market_expectation_context = prompt_contexts["market_expectation_context"]
        price_earnings_decomposition_context = prompt_contexts["price_earnings_decomposition_context"]
        management_capital_allocation_context = prompt_contexts["management_capital_allocation_context"]
        shareholder_structure_context = prompt_contexts["shareholder_structure_context"]
        investor_interaction_context = prompt_contexts["investor_interaction_context"]
        policy_planning_context = prompt_contexts["policy_planning_context"]
        data_coverage_context = prompt_contexts["data_coverage_context"]
        investment_debate_state = state.get("investment_debate_state", {})
        bull_bear_context = ""
        if investment_debate_state:
            bull_history = compact_debate_history(
                investment_debate_state.get("bull_history", ""),
                profile="portfolio",
            )
            bear_history = compact_debate_history(
                investment_debate_state.get("bear_history", ""),
                profile="portfolio",
            )
            judge_decision = compact_for_prompt(
                investment_debate_state.get("judge_decision", research_plan),
                label="investment_plan",
                profile="portfolio",
            )
            bull_bear_context = f"""
**Research Team Bull-Bear Debate Context:**
- Bull case history:
{bull_history}
- Bear case history:
{bear_history}
- Research Manager ruling:
{judge_decision}
"""

        past_context = compact_for_prompt(
            state.get("past_context", ""),
            label="past_context",
            profile="portfolio",
        )
        recent_decision_context = compact_for_prompt(
            state.get("recent_decision_context", ""),
            label="recent_decision_context",
            profile="portfolio",
        )
        prompt_risk_history = compact_risk_history(history, profile="portfolio")
        lessons_line = (
            f"- Lessons from prior decisions and outcomes:\n{past_context}\n"
            if past_context
            else ""
        )
        recent_decision_line = (
            f"- Most recent same-ticker decision (may still be pending outcome):\n"
            f"{recent_decision_context}\n"
            if recent_decision_context
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

**Reader Take-away / Holder-vs-Builder Action Rules:**
- Treat the reader as either already holding a full/large position or preparing to build a position. For every rating, give practical advice for both audiences.
- Add a short reader-facing take-away that explains the actionable price band, valuation band, or evidence band that would justify holding, adding, building, waiting, trimming, or exiting.
- For Buy / Overweight: explain how new buyers should build the position in stages, what initial/add-on zones or confirmation signals justify each step, and what full holders should do about holding, adding, or risk controls.
- For Hold: explain what full holders should monitor or rebalance, and what new buyers should wait for before initiating. Avoid calling it investable without a clear valuation or evidence trigger.
- For Underweight / Sell: explain how full holders should reduce exposure or protect downside, and what lower price/valuation band could make new entry reasonable if the company's fundamentals remain intact.
- The band must not be a loose technical level. Anchor it to valuation logic such as normalized earnings, clean EPS, EV/EBITDA, PB/ROE, FCF yield, cycle-midpoint profit, downside asset value, or peer-relative discount, then connect that valuation to business conditions that must remain true.
- If the business quality is structurally poor, governance is severely impaired, solvency is questionable, or the available evidence cannot justify any responsible entry/build band, say that explicitly instead of inventing a buy zone.
- Distinguish four ideas: current rating, intrinsic value, action for full holders, and action for prospective builders. A negative current rating can coexist with a lower price band where probability/payoff becomes attractive.

**Decision-Continuity Rules:**
- Reassess the company fully every run, but treat the most recent same-ticker decision as the reference point for continuity.
- If the final rating changes, state the prior rating, the new decisive evidence, the core facts that are unchanged, and why those changes are sufficient to alter the stance.
- If there is no new decisive evidence, preserve the prior directional stance where possible and adjust conviction, position size, watch levels, or execution posture instead.
- A lower share price or weaker chart alone may change valuation or trading posture, but it must not by itself justify crossing from a positive rating to a negative rating or vice versa.
- If a recent same-ticker decision is present and you are writing free text rather than structured fields, include explicit sections titled **Prior Rating**, **New Evidence Since Prior**, **Unchanged Core Facts**, and **Rating Change Audit**.
- If any verified theme affects the thesis and you are writing free text rather than structured fields, include an explicit section titled **Thematic Valuation Bridge** explaining whether the theme belongs in core valuation, scenario valuation, SOTP/NAV, or only qualitative optionality.

**Fair Cycle-Valuation Calibration:**
- Apply the same fairness standard to low-valuation laggards and high-prosperity winners.
- Low valuation/low prosperity: do not default to Underweight. Test pricing of pessimism, balance-sheet survival, cyclical versus structural decline, inflection evidence, and upside payoff.
- High prosperity/high valuation: do not default to Buy. Test sustainability, crowding, valuation digestion, and drawdown if prosperity peaks.
- Low valuation/high prosperity: possible Buy, but check one-off earnings, accounting quality, and cycle peak risk.
- High valuation/low prosperity: normally cautious, unless there is credible future inflection or scarcity value.

**Public-Excerpt Writing Rules:**
- Write the Portfolio Manager Decision as a self-contained public research note, not as a checklist of every upstream module.
- Important contexts such as policy, investor interaction, management quality, shareholder structure, second-growth curves, investee holdings, and thematic catalysts must inform your reasoning, but they do **not** each need their own standalone section in the public excerpt.
- The public excerpt should read like a compact company deep-dive with a few thick sections, not many thin bullets. Prefer 4-6 integrated sections that each complete a full loop of **claim -> evidence -> implication for the stock**.
- Begin with a short Company Snapshot, then give the rating and a one-line thesis.
- Immediately after the one-line thesis, include the reader take-away / build price band and the holder-vs-builder action guidance so the reader knows what to do with an existing position and how or whether to build a new one.
- In the main Investment Thesis, weave together the decisive business drivers, the industry-native variables, the market-implied expectation, the quality/price/relative-allocation distinction, and only the governance or disclosure evidence that materially strengthens or weakens that argument.
- In the valuation/cycle discussion, integrate the historical price-EPS-PE decomposition: state whether today's quote is earnings-supported, multiple-supported, double-engine, or fragile, and connect that answer to the forward EPS bridge.
- For commodity/resource/cyclical names, integrate the commodity/product-price context into the same valuation/cycle discussion: state whether product-price evidence supports or contradicts the expected EPS/margin/inventory turn.
- Use the Debate & Decision Logic section to summarize the strongest bull case, strongest bear case, the real disagreement, the core bet, and why you choose one side after weighing evidence quality, expectation gap, and probability/payoff.
- Use the Catalysts, Optionality & Falsification section to distinguish what belongs in the base case from what remains scenario valuation or narrative option value. Preserve verified second-growth curves, investee holdings, policy support, and live thematic catalysts, but clearly say why they do or do not change today's rating.
- Keep three judgments **clear in substance** even when integrated into prose rather than broken into separate headings: business quality, today's odds, and relative deployment versus alternatives.
- When hard-signal governance, ownership, investor-interaction, policy, or filing contexts are available, incorporate them where they change the investment argument instead of listing them mechanically.
- Include a Verification & Falsification checklist so readers know what future evidence would confirm, weaken, or overturn the thesis.
- Include a concise Data Coverage Audit when any precomputed module is failed, missing, or partial. Make clear which missing data matters to the rating and which verified evidence still supports the decision.
- Target roughly 2,800-3,800 Chinese characters when the output language is Chinese, or a similar concise long-form excerpt in other languages. Preserve the full research conclusion first, then compress only the execution plan. The goal is **less fragmentation, more synthesis**.
- Preserve the core logic from the full report: company context, decisive business drivers, final rating, core bet, expectation gap, probability/payoff, cycle/valuation setup, catalysts, falsification signals, position posture, risk controls, and evidence gaps.
- Keep the action summary / investment plan compressed. Do not spend a long section on execution mechanics; summarize position, entry/watch level, stop or downgrade trigger, and next verification point in one short paragraph or 3-4 tight bullets.
- Use a public-facing research-note tone: clear, readable, and investment-focused. Avoid micro-headings, repeated restatement, filler, and unsupported claims.

**Context:**
- Research Manager's investment plan: **{research_plan}**
- Trader's transaction proposal: **{trader_plan}**
- Thematic catalyst cross-check and valuation bridge: **{thematic_catalyst_context}**
- Commodity/product-price context: **{commodity_context}**
- Financial-report intelligence: **{filing_intelligence_context}**
- Same-industry peer comparison: **{peer_comparison_context}**
- Cross-position supply-chain comparison: **{supply_chain_comparison_context}**
- Earnings-model context: **{earnings_model_context}**
- Market-expectation context: **{market_expectation_context}**
- Historical price-EPS-PE decomposition context: **{price_earnings_decomposition_context}**
- Management/capital-allocation context: **{management_capital_allocation_context}**
- Shareholder-structure context: **{shareholder_structure_context}**
- Official investor-interaction context: **{investor_interaction_context}**
- Official policy-planning context: **{policy_planning_context}**
- Data coverage audit: **{data_coverage_context}**
{lessons_line}
{recent_decision_line}
{bull_bear_context}
**Risk Analysts Debate History:**
{prompt_risk_history}

---

Be decisive and ground every conclusion in specific evidence from the analysts.
{get_evidence_instruction()}
{get_research_gap_instruction()}
{get_supply_demand_fallback_instruction()}
{get_buy_side_thesis_instruction()}
{get_material_catalyst_instruction()}
{get_thematic_valuation_instruction()}
{get_filing_intelligence_instruction()}
{get_peer_selection_instruction()}
{get_supply_chain_selection_instruction()}
{get_earnings_model_instruction()}
{get_market_expectation_instruction()}
{get_price_earnings_decomposition_instruction()}
{get_investor_interaction_instruction()}
{get_policy_planning_instruction()}
{get_three_layer_conclusion_instruction()}
{get_management_capital_allocation_instruction()}
{get_shareholder_structure_instruction()}
{get_fair_cycle_valuation_instruction()}
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
