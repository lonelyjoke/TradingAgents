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
    get_baijiu_instruction,
    get_buy_side_thesis_instruction,
    get_buy_side_underwriting_modules_instruction,
    get_compute_leasing_instruction,
    get_dividend_defensive_instruction,
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
    get_web_fact_check_instruction,
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
        web_fact_check_context = prompt_contexts["web_fact_check_context"]
        baijiu_context = prompt_contexts["baijiu_context"]
        compute_leasing_context = prompt_contexts["compute_leasing_context"]
        dividend_defensive_context = prompt_contexts["dividend_defensive_context"]
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
- Missing data is not bearish evidence by itself. A data outage can justify lower conviction, smaller sizing, a wait-for-confirmation plan, or a temporary Hold, but it must not be the decisive reason for Underweight/Sell.
- Do not let PE/PB and technical indicators replace missing product price, spread, inventory, freight-rate, capacity, policy, or order-book evidence.
- If micro evidence is unavailable, use product-specific macro supply-demand evidence where possible: upstream cost, downstream demand, capacity, utilization, imports/exports, substitution, policy, seasonality, and storability.
- Macro proxies can support an evidence-limited directional view, but cannot be treated as exact product-price or spread facts.
- If too many thesis-critical assumptions are unverified, reduce conviction and state what data would upgrade or downgrade the rating.
- If the decisive variable is missing for both bull and bear interpretations, use the verified evidence to decide direction; if verified evidence is mixed, prefer Hold/watch rather than treating uncertainty itself as negative expected value.
- Do not use an unverified exact product price, wholesale price, spread, inventory level, or date-specific market statistic as a hard entry/exit trigger. Use it only as a watch item unless the source context labels it verified.
- If web fact-check context exists, use it only to corroborate high-frequency facts. A single web result can support a watch item, but hard holder/builder triggers require multiple recent independent sources or an official source.

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
- Use seasonality-adjusted or normalized earnings for valuation bands when available. If you cite a simple annualized Q1 profit number, label it as a run-rate stress case, not the base forecast.
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
- The public excerpt should read like a buy-side company deep-dive with a few thick sections, not many thin bullets. It is acceptable for the report to be longer when the company and industry require it; information density matters more than brevity. Prefer integrated sections that each complete a full loop of **claim -> evidence -> financial impact -> valuation/position implication**.
- Begin with a short Company Snapshot, then give the rating and a one-line thesis.
- Immediately after the one-line thesis, include the reader take-away / build price band and the holder-vs-builder action guidance so the reader knows what to do with an existing position and how or whether to build a new one.
- Add a compact **PM Summary** front box when the evidence set is rich enough: rating, action, sizing, time horizon, core bet, why now, biggest risk, and next verification date. This is generic and should work for any company, not only one ticker.
- For value stocks, blue chips, mature cash-flow compounders, banks, or defensive dividend names with resilient financials, add a **Safety Price / Defensive Build Anchor**. This is a conservative slow-accumulation price or price band for builders, not a target price and not a stop-loss. Derive it from financial state: normalized low-cycle EPS or FCF, sustainable dividend yield, book value/PB and ROE, cash conversion, net cash/leverage, asset quality, payout capacity, and historical/peer valuation floors. Explain why that level has a margin of safety, why a temporary break below it could mean-revert if fundamentals hold, how to build slowly around it, and which financial deterioration would invalidate it. If the company is structurally impaired, highly leveraged, deep cyclical, concept-driven, or evidence-thin, explicitly say no reliable safety price can be assigned.
- In the main Investment Thesis, make the reader understand the company, its industry, and why price may differ from value. Cover: how the company makes money; where the industry is in its cycle; what the market currently appears to price in; where your view differs; how the difference can turn into EPS/ROE/cash-flow or multiple change; and what could prove the view wrong.
- Include a **Key Data Check** inside the Investment Thesis when numeric evidence is important. Reconcile thesis-critical figures and explicitly flag conflicting signs, units, periods, or magnitudes from the debate before using the final number.
- The final decision must visibly use financial-report text when financial-report intelligence is ready. Include a **Business Segment Breakdown** in the public memo: business line / disclosed revenue scale / growth / gross margin or net margin / profit or cash-quality read / valuation treatment. If a metric is not disclosed, write "not disclosed" and explain whether this caps SOTP confidence. Do not leave the reader unsure what the company actually does.
- When the financial-report context contains **Internal Filing Quality Modules**, synthesize them into the PM Summary and main memo rather than listing them mechanically. Cover the material conclusions from accounting reconciliation, segment economics, footnote radar, cash-flow quality, capex/CIP return bridge, MD&A text changes, non-recurring profit quality, balance-sheet forward signals, shareholder-return authenticity, and disclosure quality. It is acceptable for the latest version to be longer if that creates a clearer investment-manager summary.
- Buy-side segment depth standard: do not stop at "the company has several businesses." For each material segment, answer: what it sells, how large it is, how fast it is growing, whether margin/profit/cash quality is better or worse than the group, whether it deserves core valuation or only scenario/SOTP value, and what exact disclosure would change that treatment. If filings give only a header or noisy table fragment, say the segment economics are not disclosed and reduce SOTP confidence rather than inventing precision.
- For unfamiliar or multi-business companies, explicitly start from financial-report evidence on main businesses, then build a split valuation view. Separate mature/core businesses from new businesses or second curves; discuss each bucket's revenue scale, margin, growth, cash conversion, asset intensity, peer multiple or SOTP treatment, and evidence threshold. Examples: environmental core business versus compute-leasing new business, or legacy mobility products versus newer high-end/smart product lines.
- If the filing context includes a Business Segment Valuation Map, include a compact markdown table titled **Business Segment Valuation / Evidence Gate** unless the company is clearly single-business. Columns should cover: business bucket, filing evidence, valuation treatment, what is already proven, what is still unproven, and report impact. If segment revenue or margin is unavailable, write "not disclosed" rather than reverting to one blended PE.
- The final decision must visibly integrate same-industry peer comparison when peer context is ready. Include a **Peer Comparison Summary** that names the target's peer rank, 2-4 relevant peers, key valuation/profitability/growth/leverage/cash-return differences, and whether those peers are truly business-comparable. If the broad industry peer pool is imperfect, say so and use it as a screen rather than ignoring it.
- Buy-side peer depth standard: split the peer set into true operating comparables and broad-industry screening names. Explain whether the target's valuation premium/discount is deserved by ROE, margin, growth, leverage, cash conversion, dividend/buyback, or business durability. Name at least one peer that strengthens the target case and one peer that challenges it when the peer context supplies candidates; otherwise say why no peer changes the allocation.
- Do not merely say a stock is cheap or expensive. Translate valuation into assumptions: what today's PE/PB/EV/EBITDA/FCF yield/dividend yield implies about earnings durability, ROE, growth, risk premium, or cycle normalization, and compare that with the evidence.
- Build an earnings or value driver bridge. Name the 3-6 variables that actually move value, explain their direction, and state which ones are verified, which are inferred, and which remain research gaps.
- For any second curve or new business, include a **Unit-Economics Bridge** if the evidence exists; if take rate, margin, breakeven, utilization, or customer retention is not disclosed, say so and keep that business in scenario value rather than core valuation.
- For any material new capacity, project, store base, platform ramp, mine, ship, property project, or data center, include a **Project Ramp / Capacity Bridge** covering capacity/area/users, utilization or occupancy, price/rent, ramp timetable, incremental margin, capex, and ROIC/payback where disclosed.
- For any H-share/secondary listing, placement, convertible, debt refinancing, major capex funding, or asset-sale event, include a **Financing / Listing Scenario** that shows bull/base/bear pricing or cost-of-capital paths, dilution, use of proceeds, and whether it creates an anchor or overhang.
- When discussing industry context, teach the reader what variables matter for that industry and where the company sits versus peers. Avoid generic sector background unless it changes the investment case.
- The report must include a differentiated view: what consensus or market pricing appears to believe, which part you agree with, which part you challenge, and what future evidence would cause the market to reprice.
- In the valuation/cycle discussion, integrate the historical price-EPS-PE decomposition: state whether today's quote is earnings-supported, multiple-supported, double-engine, or fragile, and connect that answer to the forward EPS bridge.
- For commodity/resource/cyclical names, integrate the commodity/product-price context into the same valuation/cycle discussion: state whether product-price evidence supports or contradicts the expected EPS/margin/inventory turn.
- For A-share compute-leasing names, use the gated compute-leasing context only when it says `Status: triggered` or official evidence in the prompt independently proves the business. If it says `Status: not_applicable`, do not mention compute leasing as a valuation driver. When triggered, explicitly separate legacy business value, verified compute-leasing value, and unverified compute optionality; discuss asset ownership/delivery, customer contracts, unit economics, capex/funding, transition credibility, and falsification signals.
- For defensive/high-dividend candidates, use the gated dividend defensive context only when it says `Status: triggered` or when other supplied evidence independently proves a stable dividend defensive thesis. Decide whether the target is a true defensive dividend asset, a dividend-trap risk, inferior to alternatives, or best used as one sleeve in a diversified defensive basket.
- Use the Debate & Decision Logic section to summarize the strongest bull case, strongest bear case, the real disagreement, the core bet, and why you choose one side after weighing evidence quality, expectation gap, and probability/payoff.
- Use the Catalysts, Optionality & Falsification section to distinguish what belongs in the base case from what remains scenario valuation or narrative option value. Preserve verified second-growth curves, investee holdings, policy support, and live thematic catalysts, but clearly say why they do or do not change today's rating.
- When verified primary investments, non-listed equity holdings, investee IPOs, or asset-revaluation candidates are material, include a **Primary Investment NAV / Asset Revaluation** bridge. Separate this from recurring operating earnings; show conservative/base/upside values with carrying value, latest financing or IPO reference where available, exit probability, lock-up/liquidity haircuts, tax/dilution or double-counting checks, and the resulting per-share or market-cap impact. Market theme enthusiasm may affect probability/payoff, but only the haircut-adjusted incremental NAV should enter pure value investing estimates.
- Shallow-section guardrail: valuation/expectation gap, catalysts, management/capital allocation, shareholder structure, market/technical timing, and thematic optionality must not be standalone data dumps. Use them only when they complete a loop of **evidence -> financial transmission -> valuation/position implication**. If a module is present but does not change the investment case, summarize it as non-decisive instead of padding the report.
- Add a brief **Buy-Side Depth Audit** when any important section remains thin. Typical weak spots to flag are: no clean segment margin, broad-but-not-true peer universe, valuation not linked to forward EPS/ROE/cash, catalysts without timetable, management praise without ROIC/capital-return proof, ownership data without supply-demand implication, and technical signals not linked to fundamental odds.
- Keep three judgments **clear in substance** even when integrated into prose rather than broken into separate headings: business quality, today's odds, and relative deployment versus alternatives.
- When hard-signal governance, ownership, investor-interaction, policy, or filing contexts are available, incorporate them where they change the investment argument instead of listing them mechanically.
- Include a Verification & Falsification checklist so readers know what future evidence would confirm, weaken, or overturn the thesis.
- Include a **Verification Calendar** for the next disclosures or operating data points that would lead to add, hold, trim, downgrade, or exit decisions.
- Include a concise Data Coverage Audit when any precomputed module is failed, missing, or partial. Make clear which missing data matters to the rating and which verified evidence still supports the decision.
- If financial-report intelligence only says readable report-body/narrative filing text was unavailable, do not use "the system failed to retrieve any readable annual/semiannual/quarterly reports" as the core reason for the rating. Check whether structured statements, valuation, market, peer, and earnings-model evidence are present, then describe the issue narrowly as a missing filing-text/segment/management-discussion evidence gap.
- Target roughly 3,800-5,800 Chinese characters when the output language is Chinese and the evidence set is rich, or a similar long-form excerpt in other languages. Preserve the full research conclusion first, then compress only the execution plan. The goal is **higher information density, less fragmentation, more synthesis**.
- Preserve the core logic from the full report: company context, decisive business drivers, final rating, core bet, expectation gap, probability/payoff, cycle/valuation setup, catalysts, falsification signals, position posture, risk controls, and evidence gaps.
- Keep the action summary / investment plan compressed. Do not spend a long section on execution mechanics; summarize position, entry/watch level, stop or downgrade trigger, and next verification point in one short paragraph or 3-4 tight bullets.
- Use a public-facing research-note tone: clear, readable, and investment-focused. Avoid micro-headings, repeated restatement, filler, and unsupported claims.

**Bank Buy-Side Memo Overlay:**
- If the target is a bank, a financial institution, or the filing context says `Reading profile: banking`, write the final decision through a bank-specific buy-side framework. Do not use orders, contract liabilities, gross margin, inventory, commodity cycles, or manufacturing-style cash conversion as core evidence.
- If the target is not a bank and the filing context does not say `Reading profile: banking`, do **not** use bank-specific KPI language such as NIM, deposit cost, credit cost, NPL, provision coverage, CET1, RWA, PB/ROE/COE bank framing, or payout-capital regulatory analysis unless those terms are directly relevant to the company's disclosed business. Route non-bank companies through their own industry-native drivers instead.
- Make the reader understand the bank's economic engine: earning assets, deposit franchise, NIM/net interest yield, fee income/AUM, credit cost, asset quality, capital/RWA, payout capacity, and regulatory constraints.
- Include a compact bank KPI decision table in prose or markdown: NIM/net interest yield and deposit cost; loan/deposit mix; fee income and wealth-management/AUM; NPL/special-mention/overdue or provision coverage; CET1/capital adequacy/RWA growth; dividend or payout safety. For each item, state latest evidence, direction, thesis implication, and next verification point.
- Build the bank earnings bridge through earning assets x NIM, fee income, credit cost/provisioning, operating efficiency, tax/minority items, capital consumption, and payout. If a driver is missing, say it is missing and do not substitute generic revenue, margin, OCF, orders, or contract-liability evidence.
- Build the bank valuation bridge through PB/ROE/COE, PE as a cross-check, dividend yield, and peer-relative quality. Explain what today's PB/PE implies about sustainable ROE or risk premium, then compare it with the bank's actual ROE, asset quality, deposit franchise, and capital position.
- Explain why this bank rather than another bank: compare quality paid for versus quality received, including PB/ROE, asset quality, deposit franchise, fee resilience, capital, payout, and whether the quality premium is justified.
- Scenario analysis for banks must attach probabilities to explicit banking variables: NIM bps, credit cost/provision coverage, fee-income growth, NPL movement, ROE, PB or dividend yield, and position action. Do not use generic bull/base/bear labels without these variables.
- Keep NIM terminology precise: `净利息收益率`, `净息差`, and `净利差` are not interchangeable. Never invent a NIM number that is not supported by the supplied filing or KPI context.

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
- Web fact-check context: **{web_fact_check_context}**
- Gated baijiu verification context: **{baijiu_context}**
- Gated compute-leasing verification context: **{compute_leasing_context}**
- Gated dividend defensive verification context: **{dividend_defensive_context}**
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
{get_buy_side_underwriting_modules_instruction()}
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
{get_web_fact_check_instruction()}
{get_baijiu_instruction()}
{get_compute_leasing_instruction()}
{get_dividend_defensive_instruction()}
{get_fair_cycle_valuation_instruction()}
{get_focused_report_instruction()}
If an important investment claim depends on an unverified commodity price, product spread, inventory, policy detail, wholesale price, or exact percentage, list it under an "Unverified Key Assumptions" paragraph instead of treating it as fact. Do not place unverified exact prices in the holder/builder action plan as hard triggers; turn them into verification items.{get_language_instruction()}"""

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
