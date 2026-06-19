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
    get_biopharma_instruction,
    get_building_materials_instruction,
    get_buy_side_thesis_instruction,
    get_buy_side_underwriting_modules_instruction,
    get_compute_leasing_instruction,
    get_consumer_staples_instruction,
    get_dividend_defensive_instruction,
    get_evidence_instruction,
    get_earnings_model_instruction,
    get_fair_cycle_valuation_instruction,
    get_filing_intelligence_instruction,
    get_focused_report_instruction,
    get_insurance_instruction,
    get_knowledge_planet_instruction,
    get_medical_device_instruction,
    get_metals_mining_instruction,
    get_optical_module_instruction,
    get_price_move_attribution_instruction,
    get_investor_interaction_instruction,
    get_language_instruction,
    get_market_expectation_instruction,
    get_management_capital_allocation_instruction,
    get_material_catalyst_instruction,
    get_policy_planning_instruction,
    get_peer_selection_instruction,
    get_price_earnings_decomposition_instruction,
    get_question_led_debate_instruction,
    get_research_gap_instruction,
    get_supply_demand_fallback_instruction,
    get_supply_chain_selection_instruction,
    get_shareholder_structure_instruction,
    get_software_instruction,
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
            max_chars=11000,
        )
        trader_plan = compact_for_prompt(
            state["trader_investment_plan"],
            label="trader_plan",
            profile="portfolio",
        )
        prompt_contexts = compact_state_fields(state, profile="portfolio")
        thematic_catalyst_context = prompt_contexts["thematic_catalyst_context"]
        commodity_context = prompt_contexts["commodity_context"]
        price_move_attribution_context = prompt_contexts["price_move_attribution_context"]
        intraday_behavior_context = prompt_contexts["intraday_behavior_context"]
        relative_strength_context = prompt_contexts["relative_strength_context"]
        shipping_context = prompt_contexts["shipping_context"]
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
        knowledge_planet_context = prompt_contexts["knowledge_planet_context"]
        baijiu_context = prompt_contexts["baijiu_context"]
        compute_leasing_context = prompt_contexts["compute_leasing_context"]
        dividend_defensive_context = prompt_contexts["dividend_defensive_context"]
        building_materials_context = prompt_contexts["building_materials_context"]
        consumer_staples_context = prompt_contexts["consumer_staples_context"]
        optical_module_context = prompt_contexts["optical_module_context"]
        biopharma_context = prompt_contexts["biopharma_context"]
        software_context = prompt_contexts["software_context"]
        insurance_context = prompt_contexts["insurance_context"]
        medical_device_context = prompt_contexts["medical_device_context"]
        metals_mining_context = prompt_contexts["metals_mining_context"]
        industry_cycle_context = prompt_contexts["industry_cycle_context"]
        company_business_model_context = prompt_contexts["company_business_model_context"]
        industry_kpi_context = prompt_contexts["industry_kpi_context"]
        forecast_model_context = prompt_contexts["forecast_model_context"]
        quality_audit_context = prompt_contexts["quality_audit_context"]
        thesis_question_context = prompt_contexts["thesis_question_context"]
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
                max_chars=10000,
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
- **Hold**: Balanced or transition setup where the company may be investable, but the decisive variable is unresolved or the justified position is only an observation/starter weight pending validation
- **Underweight**: Negative expected value or unattractive payoff, but not enough evidence for a full exit call
- **Sell**: Core thesis deteriorated or downside probability/payoff is clearly unfavorable

**Final-Rating Consistency Rules:**
- The structured `rating` field is the final Portfolio Manager rating. Every PM summary, one-line thesis, holder/builder action, position posture, and execution paragraph must be consistent with that final rating.
- Research Manager, Trader, and risk-analyst ratings are upstream, non-final inputs. If you discuss a different upstream rating, label it explicitly as `upstream Research Manager view`, `upstream Trader view`, or `prior non-final view`; never call it the current, final, or PM rating.
- Before finalizing, check that no sentence says `current rating`, `final rating`, `本次评级`, `当前评级`, or `最终评级` equals a tier different from the structured final rating.
- If the final PM rating differs from the Research Manager or Trader rating, explain the change in Debate & Decision Logic or Rating Change Audit, then make the action guidance follow the final PM rating only.
- For Buy / Overweight, do not tell holders to reduce to Underweight or avoid new positions unless you clearly mark that as a rejected upstream view. For Underweight / Sell, do not tell builders to add or overweight unless it is a lower-price re-entry watch condition.
- The final rating must be derived from the company's full fundamental chain, not from the failure of the opposite rating. `The Underweight case is not proven` is not a reason to choose Overweight; `the Overweight case is not proven` is not a reason to choose Underweight. First prove the positive or negative expected-value chain on its own merits.
- Before choosing Buy/Overweight/Underweight/Sell, complete a rating-strength ladder: company quality, segment economics, key operating drivers, cash-flow and balance-sheet quality, management/capital allocation, valuation-implied expectations, catalyst path, downside case, peer opportunity cost, and falsification path.
- If the action plan is only a starter/observation position, or if full sizing explicitly waits for one decisive disclosure, the default tier is Hold with positive bias unless the memo proves enough company-specific upside evidence to justify Overweight despite the pending gate.
- Hold must not be a vague neutral label. A high-quality Hold should be useful: state the live thesis, justified current position, valuation band, exact upgrade triggers, exact downgrade triggers, and the next verification date.

**Market-Regime Calibration Rules:**
- The rating is not static. Calibrate it against broad-market mood, market valuation, sector risk, and the stock's own traits.
- Normal bull market: you may be slightly more constructive for reasonably valued, high-quality stocks with catalysts, but do not chase crowded/high-valuation names.
- Normal bear market: be more conservative unless the stock has strong balance sheet, low valuation, resilient cash flow, and clear catalysts.
- Extreme pessimism: do not become mechanically bearish. For resilient companies or depressed value opportunities, consider staged-entry/watch-zone logic.
- Extreme optimism: do not become mechanically bullish. For expensive or high-beta names, emphasize profit-taking and tighter risk control.
- Cyclical, commodity, shipping, high-beta, and event-driven stocks require specific cycle evidence; market mood alone must not determine the rating.
- If bullish/constructive, provide a profit-taking or trimming range. If bearish/cautious, provide an entry or re-entry watch range.

**Research-Gap and Supply-Demand Rules:**
- Missing core operating data is neutral evidence for direction, but not neutral for conviction. It is a research gap that should reduce confidence in the affected thesis.
- Missing data is not bearish evidence by itself. A data outage can justify lower conviction, smaller sizing, a wait-for-confirmation plan, or a temporary Hold, but it must not be the decisive reason for Underweight/Sell.
- Do not let PE/PB and technical indicators replace missing product price, spread, inventory, freight-rate, capacity, policy, or order-book evidence.
- If micro evidence is unavailable, use product-specific macro supply-demand evidence where possible: upstream cost, downstream demand, capacity, utilization, imports/exports, substitution, policy, seasonality, and storability.
- Macro proxies can support an evidence-limited directional view, but cannot be treated as exact product-price or spread facts.
- If too many thesis-critical assumptions are unverified, reduce conviction and state what data would upgrade or downgrade the rating.
- For aluminum names, missing alumina, power, or anode cost evidence cannot by itself support Underweight/Sell, margin-collapse claims, or "perfect scenario priced" language. Require independent verified cost squeeze, segment-margin compression, cash-flow deterioration, inventory loss, peer opportunity cost, or valuation stress.
- Keep the rating label itself clean: use exactly Buy / Overweight / Hold / Underweight / Sell. Do not append phrases such as "evidence-limited" or "证据受限" to the rating name. Put evidence limitations in conviction, sizing, Evidence Gaps & Data Coverage, and Verification Calendar instead.
- Do not label the whole conclusion evidence-limited just because a non-core module is partial, not_applicable, or failed. For example, web fact-check partial or an unrelated gated industry context must not cap the rating when filings, statements, commodity data, peer data, and valuation context are ready.
- If the decisive variable is missing for both bull and bear interpretations, use the verified evidence to decide direction; if verified evidence is mixed, prefer Hold/watch rather than treating uncertainty itself as negative expected value.
- Do not use an unverified exact product price, wholesale price, spread, inventory level, or date-specific market statistic as a hard entry/exit trigger. Use it only as a watch item unless the source context labels it verified.
- If web fact-check context exists, use it only to corroborate high-frequency facts. A single web result can support a watch item, but hard holder/builder triggers require multiple recent independent sources or an official source.

**Buy-Side Decision Rules:**
- The final decision must identify the Core Bet. If there is no Core Bet, explain why the rating is Hold or Underweight.
- Evaluate whether the relevant boom-bust expectation can plausibly realize through macro context, industry cycle, company exposure, and available high-frequency/proxy data.
- Use expectation gap: a good company is not enough if the market already priced the thesis; an imperfect company can be interesting if the market underprices an improving driver.
- Use probability/payoff instead of simple evidence counting. Conflicting evidence can still justify a direction when the payoff is asymmetric and the thesis is falsifiable.
- Match position size to conviction. Evidence-limited Overweight should usually be a staged or starter position, not a full-conviction Buy.
- However, a starter position alone does not make a stock Overweight. If the fundamental chain supports only a small test position until the next report, call the rating Hold/positive watch or Hold with starter-position guidance unless upside evidence, valuation gap, catalyst path, and downside containment are strong enough on a standalone basis.

**Reader Take-away / Holder-vs-Builder Action Rules:**
- Treat the reader as either already holding a full/large position or preparing to build a position. For every rating, give practical advice for both audiences.
- Add a short reader-facing take-away, but keep it subordinate to the company research. The action plan should be a compact conclusion from the business analysis, not the organizing spine of the memo.
- For Buy / Overweight: explain staged exposure only after the company thesis, segment economics, and evidence gates are clear. Limit execution mechanics to a concise paragraph or compact table.
- For Hold: explain what business evidence, valuation evidence, or disclosure would make the stock investable; avoid filling space with passive trading instructions.
- For Underweight / Sell: explain how holders should reduce exposure or protect downside, but spend more depth on the company-quality and expectation-gap evidence than on exit mechanics.
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
- The public excerpt should read like a buy-side company deep-dive with a few thick sections, not many thin bullets. The report's center of gravity must be company research: business model, segment economics, industry position, unit economics, financial-statement quality, competitive alternatives, and why those facts lead to valuation and position conclusions. Prefer integrated sections that each complete a full loop of **claim -> evidence -> financial impact -> valuation/position implication**.
- Treat the memo as a company-depth research report first and a transaction note second. Build valuation and holder/builder actions only after explaining the company's economics, forward earnings model, and expectation gap.
- Include a forward forecast model when evidence permits: next two to three years or next four quarters of revenue, margin, expense ratio, net profit/EPS, cash-flow/capex, and the 3-6 operating drivers that would make those forecasts right or wrong. Label estimates and assumptions clearly.
- Include a valuation framework that follows from the business buckets: PE/PB/ROE/EV-EBITDA/DCF/NAV/SOTP/dividend yield as appropriate, with core value separated from scenario value or optionality. Do not write valuation as a generic multiple paragraph detached from segment economics.
- Use historical minute K-line context as market-behavior validation only after the fundamental work: intraday reversal, high-low range, first/last-30-minute behavior, volume concentration, liquidity, and whether the move is company alpha, sector beta, commodity beta, or broad risk appetite. Minute-line behavior may adjust timing, confidence, or sizing; it must not replace company research or valuation.
- Use this narrative order: (1) what the company is and the decision, (2) how the business model and industry chain work, (3) business segment breakdown and unit economics, (4) the core investment thesis and earnings/valuation bridge, (5) supporting evidence that changes confidence or sizing, (6) bull/bear decision logic, (7) catalysts/optionality and evidence gaps, (8) verification/falsification, and only then (9) concise holder/builder execution posture.
- Include the Industry Cycle Scan in the valuation/cycle discussion. State the cycle stage before using cycle valuation multiples, and downgrade language from `cycle bottom confirmed` to `bottom-right validation` or `bottom-testing` when the scan is not decisive.
- Include the Company Business Model Primer before valuation. The reader should understand the revenue engine, profit pools, customers/channels, cost drivers, moat, capital intensity, and second-curve evidence gates before seeing PE/PB/SOTP.
- Include the Industry KPI Checklist as the operating-data agenda. The final memo should say which sector-native KPIs are verified, partial, or missing, and which ones most affect rating, valuation, sizing, or next verification.
- Include the Forward Forecast Model Scaffold in the earnings bridge. A constructive or negative rating should be tied to two-to-three-year revenue, margin, net profit/EPS, and cash-flow assumptions, even if some cells are explicitly evidence-limited.
- Include the Sell-Side Depth And Key-Number Audit in the background discipline. Decisive PE/PB/EV multiples, target price, safety price, dividend yield, margins, ASP, shipments, utilization, backlog, and contract-liability claims need formula, source period, and evidence status.
- Include the Thesis Question Context as the core-question spine. Answer the target-specific question IDs that matter most, state which side won each question after the debate, and move unanswered thesis-critical questions into Evidence Gaps or Verification Calendar.
- Deep sell-side bridge standard: when the business is project/order/backlog driven, include an explicit order bridge (opening backlog + new orders - delivered/revenue-recognized orders = ending backlog) and reconcile contract liabilities, receivables, inventory/goods shipped, and cash collection. When valuation uses a safety price, target price, or downside anchor, show bull/base/bear or sensitivity assumptions rather than jumping from one profit number to a price. When peers are broad industry screens, split true operating peers from broad screens and name substitute expressions if the context supports them. When a second curve/new business/capacity/ship/mine/platform is mentioned, state whether it is core value, scenario value, or rejected optionality and what evidence would change that status. Include a compact evidence-grade table or paragraph for decisive numbers: reported, calculated, estimated, proxy, stale, missing, or unverified.
- Treat structured optional fields as materiality gates, not a checklist. Fill a specialized field only when it changes the rating, valuation, position size, confidence, or next verification action. If a module is merely background, summarize it in one sentence inside the main thesis or omit it; if it is missing/partial, put it in Data Coverage Audit or Buy-Side Depth Audit rather than creating a standalone mini-section.
- Avoid repeating the same fact in Company Snapshot, Business Model & Industry Chain Primer, Business Segment Breakdown, Investment Thesis, and Business Driver Map. Let each section do one job: primer teaches the operating model, segment breakdown explains disclosed economics, thesis explains why price may diverge from value, and supporting evidence explains what changed conviction.
- If the financial-report intelligence contains **Growth Sustainability & Ramp Conditions**, include a standalone Chinese section titled `## 营收与利润增长可持续性 / 放量条件`. Explain the 3-6 variables that decide whether revenue and profit growth can continue, which are verified by filings, which are inferred, what must happen for growth to keep ramping, and what would falsify the thesis. Do not treat analyst estimates or back-solved profit buckets as facts; label estimates, formulas, periods, and uncertainty explicitly.
- If the financial-report intelligence contains **Pre-Debate Underwriting Questions**, include a standalone Chinese section titled `## 核心投研问题与辩论后的答案` after the Business Model & Industry Chain Primer and before the main Investment Thesis. Select the 4-7 questions that actually drive the rating, valuation, sizing, or next verification action. Answer them with the post-debate PM judgment in a compact issue-log table: core question, initial skeptical prior, bull evidence, bear evidence, PM ruling, earnings/valuation impact, and next verification. Do not paste the upstream question table mechanically; make the section read like the investment committee's answer to the company's hardest questions.
- If relative-strength/index-linkage context is available, include a standalone Chinese section titled `## 相对走势与指数联动`. This section should be richer than one sentence: summarize the selected style/broad index and same-industry basket, 20/60/120/250-day relative performance, whether the stock is stronger or weaker, correlation/Beta, whether the move looks like company alpha or benchmark/sector beta, and what it means for position sizing, entry timing, holder action, and thesis validation. Do not let relative strength override fundamental evidence; use it as market-confirmation and timing evidence.
- Begin with a short Company Snapshot, then give the rating and a one-line thesis.
- Do not place the holder/builder action plan immediately after the headline unless the memo is very short. For normal rich evidence sets, put the company deep-dive first and place the holder/builder action guidance near the end under a concise `Execution Posture` or `持仓与建仓结论` section.
- Add a compact **PM Summary** front box when the evidence set is rich enough: rating, action, sizing, time horizon, core bet, why now, biggest risk, and next verification date. This is generic and should work for any company, not only one ticker.
- Include a standalone **Business Model & Industry Chain Primer** section before the main Investment Thesis. This is a small educational column for readers who do not know the company: explain how the company makes money, who pays it, what cost/price/volume/capacity/utilization/cash-conversion variables matter, where it sits in the upstream-midstream-downstream chain, and why that chain position affects valuation or risk.
- In that primer, briefly name relevant upstream/downstream listed companies or true peers only when the supplied filing, peer, supply-chain, or analyst context supports the names. If listed-company examples are not verified, describe the upstream/downstream categories instead and explicitly say names are not verified. Do not invent A-share/H-share/U.S.-listed companies just to make the primer feel complete.
- Include a concise **Safety Price / Defensive Build Anchor** only after the valuation/earnings bridge has been explained; when writing Chinese, title it `## 安全价格区间 / 防御性建仓锚`. This section must be derived from the prior company analysis, not used as a substitute for it. Prefer one short paragraph or a compact 3-4 row table; if the company is structurally impaired, highly leveraged, deep cyclical without survivable trough economics, concept-driven, or evidence-thin, explicitly say no reliable safety price can be assigned.
- In the main Investment Thesis, avoid re-teaching the primer. Focus on why price may differ from value: where the industry is in its cycle, what the market currently appears to price in, where your view differs, how the difference can turn into EPS/ROE/cash-flow or multiple change, and what could prove the view wrong.
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
- When price-move attribution context is available, integrate it into the action plan: separate market, same-metal equity, cross-metal equity, mapped commodity, company-event, valuation, and failed-rebound explanations. A large drop with mild commodity futures is not automatically an emotion-kill buy; require valuation/NAV support, no material company event, and stabilization evidence before upgrading.
- For shipping names, integrate the shipping/freight-rate context into the same valuation/cycle discussion: separate broad freight proxies from route-level rates, identify the route economics that matter for the company, and test two-sided Hormuz reopening/restocking mechanisms before calling the setup bullish or bearish. If VLCC TD3C/TCE/CTFI is missing, cap conviction and define the exact evidence that would turn a watch thesis into an add/trim decision; do not use the missing data alone as the decisive Underweight/Sell reason.
- For A-share compute-leasing names, use the gated compute-leasing context only when it says `Status: triggered` or official evidence in the prompt independently proves the business. If it says `Status: not_applicable`, do not mention compute leasing as a valuation driver. If the context only contains weak/non-triggering mentions, put it in rejected optionality or evidence gaps rather than giving it a standalone thesis section. When triggered, explicitly separate legacy business value, verified compute-leasing value, and unverified compute optionality; discuss asset ownership/delivery, customer contracts, unit economics, capex/funding, transition credibility, and falsification signals.
- For defensive/high-dividend candidates, use the gated dividend defensive context only when it says `Status: triggered` or when other supplied evidence independently proves a stable dividend defensive thesis. Decide whether the target is a true defensive dividend asset, a dividend-trap risk, inferior to alternatives, or best used as one sleeve in a diversified defensive basket.
- For building-materials candidates, use the gated building-materials context only when it says `Status: triggered` or when other supplied evidence independently proves a cement, waterproofing, glass/fiberglass, gypsum-board, pipe, coating, ceramic-tile, hardware, wood-panel, or adjacent building-materials business. Treat it as a discipline layer, not the whole memo: anchor first on company filings and management wording, then classify the industry stage and likely evolution path, then explain low-PB/high-dividend setups through asset value, product cycle, cash conversion, payout safety, and capital allocation. Add a dedicated **Building Materials Operating Cycle Verdict** only when it changes the rating, valuation, sizing, or action plan; otherwise integrate the relevant points into the business, valuation, or risk sections. Treat buybacks and dividends as shareholder-return, safety-margin, and controlling-shareholder-attitude evidence, not as the whole thesis.
- For consumer-staples / food-beverage candidates, use the gated consumer-staples context only when it says `Status: triggered` or when other supplied evidence independently proves a food, beverage, dairy, meat, condiment, snack, frozen-food, or prepared-dish business. For Anjoy/frozen-food names, the PM memo must explicitly decide what Q1 strength means: Spring Festival seasonality, distributor restocking after destocking, lower input cost, product-mix improvement, prepared-dish ramp, or durable end-demand acceleration. Tie the rating to restaurant/household demand, channel sell-through, distributor inventory, contract liabilities or advance receipts, inventory/revenue, receivables, gross margin, raw-material cost proxies, promotion intensity, and food-safety risk. Do not write a generic "consumption recovery" or "cheap consumer leader" memo unless those variables support it.
- For optical-module / AI datacom candidates, use the gated optical-module context only when it says `Status: triggered` or when other supplied evidence independently proves an optical-module, optical-component, optical-chip, or AI datacom hardware business. For Zhongji Innolight, Eoptolink, and similar names, the PM memo must explicitly decide whether growth is driven by 800G share gain, 1.6T ramp, overseas cloud customer orders, price/mix, exchange rate, capacity/yield, or temporary supply shortage. Tie the rating to hyperscaler AI capex, switch-speed upgrade, customer qualification, shipment mix, gross margin, inventory/revenue, receivables/revenue, operating cash flow, customer concentration, export/tariff risk, and CPO/LPO/silicon-photonics route risk. Do not write a generic "AI high-growth leader" memo unless those variables support it.
- For software/SaaS candidates, use the gated software context only when it says `Status: triggered` or when other supplied evidence independently proves a software, SaaS, financial IT, cybersecurity, industrial software, AI software, or hardware-plus-service business. Classify the model before valuation. For SaaS/product-led names, require paid users, ARPU, renewal/churn, contract-liability conversion, and AI paid adoption before giving SaaS-like or AI-uplift valuation credit. For project-heavy software, require backlog, acceptance, receivables, and collection. Broad software-service peer baskets are not final relative-value proof.
- For insurance candidates, use the gated insurance context only when it says `Status: triggered` or when other supplied evidence independently proves an insurance business. Write through insurance-native drivers: NBV, EV/P-EV, channel quality, solvency, investment yield versus liability cost, P&C COR, dividend capacity, and SOTP for bank/technology/asset-management subsidiaries. Do not let a bank subsidiary turn an integrated insurer into a pure bank memo.
- For insurance/high-dividend defensive candidates, calibrate rating language carefully: one-quarter net profit, non-recurring profit, or operating cash flow deterioration is a warning signal, not a standalone proof of franchise deterioration. A sharp OCF decline is a **hard negative cash-flow signal with unresolved attribution**; do not soften it into a vague concern, but also do not treat it as conclusive franchise impairment until NBV, EV/P-EV, OPAT/core operating profit, CSM/NCSM, solvency, investment-yield spread, payout coverage, and P&C COR confirm the downside. If those core insurance indicators are missing or mixed while low PB and dividend yield still provide some defensive value, prefer Hold or Underweight as a clearly labeled **relative low-weight / wait-for-H1-validation** stance, not a high-conviction absolute exit call.
- Insurance rating-strength reconciliation: if the recommended position is only a starter, 1/3-1/2 target weight, or below normal allocation while full sizing waits for H1/annual validation, the default clean rating should be Hold/positive watch unless the insurance-native evidence already proves positive expected value on a standalone basis. Use **staged/cautious Overweight** only when the report proves all three: (1) verified NBV/OPAT/COR or EV evidence is strong enough to outweigh unresolved OCF/channel risks, (2) valuation-implied expectations are explicitly too pessimistic, and (3) the downside case is bounded by capital, payout, and solvency evidence. Do not let "Overweight" and "stay below normal weight" read like conflicting conclusions.
- Insurance valuation bridge requirement: include or explicitly mark missing a compact bridge across P/EV or EV growth, NBV multiple, PB-ROE, dividend yield and payout/solvency coverage, and SOTP for life/health, P&C, bank, asset-management/technology, and holding-company discount. If current EV is not disclosed, use latest annual EV only as a stale-base cross-check and label it as such. Every dividend claim must reconcile interim dividend, final dividend, full-year DPS, payout ratio, yield-price base, and disclosure period; conflicting DPS figures must be flagged as a data issue. SOTP must show segment formula, ownership/stake where relevant, per-share conversion, group discount, and double-counting checks. State whether the final action is absolute downside, insurance-sector relative allocation, or defensive-basket suitability.
- Insurance peer-deployment requirement: compare the target with true insurer alternatives and name the portfolio role. For China Ping An-like integrated insurers, decide whether the stock is a higher-beta NBV/SOTP recovery expression, a cleaner insurance-quality compounder, a dividend sleeve, or inferior to peers such as China Life, CPIC, PICC, or New China Life. If using subjective scenario probabilities, label them as PM underwriting weights rather than verified facts.
- Insurance peer-substitution rating gate: an exchange-industry peer screen based only on PE/PB/ROE/dividend yield/one-quarter profit growth is a screen, not a verified substitute. Do not make it the decisive reason for Underweight/Sell unless the proposed peer is also validated on comparable insurance-native drivers: NBV growth, NBV margin, EV or P/EV, OCF/cash-quality trend, solvency, investment spread, payout coverage, channel mix, and P&C COR where applicable. If the target has low PB/high dividend and mixed but non-broken NBV/OPAT/COR evidence, while peer superiority is not insurance-native verified, cap the PM rating at Hold or clearly labeled relative low-weight/watch rather than absolute Underweight. The memo must include a compact **Rating Evidence Audit** that separates: absolute company view, sector-relative allocation view, data sufficiency, key number conflicts, and why the rating tier follows.
- For telecom operators / high-dividend SOE candidates, write through operator-native drivers rather than generic software, optical-module, compute-leasing, or commodity templates. Use mobile subscribers, 5G penetration, mobile ARPU, broadband/home ARPU, enterprise/cloud/AI revenue, cloud gross margin, IDC/AI utilization, capex-to-revenue, depreciation, OCF/NI, FCF after capex, payout ratio, net cash/debt, dividend yield, and relative allocation versus China Mobile / China Unicom. Treat cloud/AI as core only when revenue, margin, utilization, customer, and capex-return evidence support it; otherwise keep it in scenario value. High dividend yield is not enough: test payout sustainability, FCF coverage, capex cycle, and dividend-trap risk.
- For medical-device candidates, use the gated medical-device context only when it says `Status: triggered` or when other supplied evidence independently proves a medical equipment, IVD, reagent/consumables, or high-value device business. Write through device-native drivers: installed base, replacement cycle, tender/procurement cadence, reagent pull-through, VBP price-volume offset, registration, overseas channel quality, service attach rate, receivables, cash conversion, product mix, and gross-margin durability. Do not value the company like an innovative-drug pipeline unless it owns drug-like asset economics.
- For metals/mining candidates, use the gated metals/mining context only when it says `Status: triggered` or when other supplied evidence independently proves a mining, smelting, refining, or metal-resource business. Write through mining-native drivers: exchange price proxies, realized selling price, reserve/resource quality, grade, equity output, AISC/unit cost, smelting/trading split, hedging/inventory, project capex/ramp, jurisdiction risk, balance-sheet survival, and NAV/SOTP. Do not let metal-price beta alone carry a Buy or Sell call.
- Use the Debate & Decision Logic section to summarize the strongest bull case, strongest bear case, the real disagreement, the core bet, and why you choose one side after weighing evidence quality, expectation gap, and probability/payoff.
- Use the Catalysts & Optionality section to distinguish what belongs in the base case from what remains scenario valuation or narrative option value. Preserve verified second-growth curves, investee holdings, policy support, and live thematic catalysts, but clearly say why they do or do not change today's rating.
- When verified primary investments, non-listed equity holdings, investee IPOs, or asset-revaluation candidates are material, include a **Primary Investment NAV / Asset Revaluation** bridge. Separate this from recurring operating earnings; show conservative/base/upside values with carrying value, latest financing or IPO reference where available, exit probability, lock-up/liquidity haircuts, tax/dilution or double-counting checks, and the resulting per-share or market-cap impact. Market theme enthusiasm may affect probability/payoff, but only the haircut-adjusted incremental NAV should enter pure value investing estimates.
- Shallow-section guardrail: valuation/expectation gap, catalysts, management/capital allocation, shareholder structure, market/technical timing, and thematic optionality must not be standalone data dumps. Use them only when they complete a loop of **evidence -> financial transmission -> valuation/position implication**. If a module is present but does not change the investment case, summarize it as non-decisive instead of padding the report.
- Add a brief **Buy-Side Depth Audit** when any important section remains thin. Typical weak spots to flag are: no clean segment margin, broad-but-not-true peer universe, valuation not linked to forward EPS/ROE/cash, catalysts without timetable, management praise without ROIC/capital-return proof, ownership data without supply-demand implication, and technical signals not linked to fundamental odds.
- Keep three judgments **clear in substance** even when integrated into prose rather than broken into separate headings: business quality, today's odds, and relative deployment versus alternatives.
- When hard-signal governance, ownership, investor-interaction, policy, or filing contexts are available, incorporate them where they change the investment argument instead of listing them mechanically.
- Use Evidence Gaps & Data Coverage only when a missing, partial, or weak module changes confidence, sizing, valuation, or the next verification action. Put unverified assumptions, research gaps, fallback views, coverage audit, and buy-side depth audit there rather than mixing them into catalysts.
- Include a Verification & Falsification checklist so readers know what future evidence would confirm, weaken, or overturn the thesis. Fold specific falsification signals into this checklist rather than creating a separate final section.
- Use precise Chinese signal labels when writing in Chinese: use `看多验证/上调信号` for evidence that would support adding or upgrading, and `看空验证/下调信号` or `看多证伪信号` for evidence that would weaken, trim, downgrade, or exit. Do not write contradictory labels such as `看多证伪信号（出现后将上调）`.
- Include a **Verification Calendar** for the next disclosures or operating data points that would lead to add, hold, trim, downgrade, or exit decisions.
- Include a concise Data Coverage Audit when any precomputed module is failed, missing, or partial. Make clear which missing data matters to the rating and which verified evidence still supports the decision.
- If financial-report intelligence only says readable report-body/narrative filing text was unavailable, do not use "the system failed to retrieve any readable annual/semiannual/quarterly reports" as the core reason for the rating. Check whether structured statements, valuation, market, peer, and earnings-model evidence are present, then describe the issue narrowly as a missing filing-text/segment/management-discussion evidence gap.
- Target roughly 3,800-5,800 Chinese characters when the output language is Chinese and the evidence set is rich, or a similar long-form excerpt in other languages. Preserve the full research conclusion first, then compress only the execution plan. The goal is **higher information density, less fragmentation, more synthesis**.
- Readability discipline: keep the PM memo to roughly 8-12 meaningful sections. Start each major section with the conclusion, then give the evidence and implication. Prefer compact tables for PM summary, core research questions, segment/evidence gates, scenarios, and verification calendars; prefer paragraphs for thesis logic and debate verdict. Avoid repeating the same action plan, valuation range, contract-liability fact, or catalyst in multiple sections unless the later mention adds a new implication.
- Do not let the report become a tool-output catalog. Merge supporting modules into the nearest decision loop: business model, core questions, thesis/valuation, debate verdict, catalysts/optionality, evidence gaps, verification calendar, and execution. If a module is non-decisive, say so once and move on.
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
- Industry cycle scan: **{industry_cycle_context}**
- Company business-model primer: **{company_business_model_context}**
- Industry KPI checklist: **{industry_kpi_context}**
- Forward forecast-model scaffold: **{forecast_model_context}**
- Sell-side depth and key-number audit: **{quality_audit_context}**
- Thesis-question context: **{thesis_question_context}**
- Commodity/product-price context: **{commodity_context}**
- Price-move attribution context: **{price_move_attribution_context}**
- Historical minute K-line / intraday behavior context: **{intraday_behavior_context}**
- Relative-strength / index-linkage context: **{relative_strength_context}**
- Shipping/freight-rate context: **{shipping_context}**
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
- Knowledge Planet stream/PDF intelligence: **{knowledge_planet_context}**
- Gated baijiu verification context: **{baijiu_context}**
- Gated compute-leasing verification context: **{compute_leasing_context}**
- Gated dividend defensive verification context: **{dividend_defensive_context}**
- Gated building-materials verification context: **{building_materials_context}**
- Gated consumer-staples verification context: **{consumer_staples_context}**
- Gated AI optical-module verification context: **{optical_module_context}**
- Gated biopharma verification context: **{biopharma_context}**
- Gated software verification context: **{software_context}**
- Gated insurance verification context: **{insurance_context}**
- Gated medical-device verification context: **{medical_device_context}**
- Gated metals/mining verification context: **{metals_mining_context}**
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
{get_question_led_debate_instruction()}
{get_insurance_instruction()}
{get_medical_device_instruction()}
{get_metals_mining_instruction()}
{get_price_move_attribution_instruction()}
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
{get_knowledge_planet_instruction()}
{get_baijiu_instruction()}
{get_compute_leasing_instruction()}
{get_dividend_defensive_instruction()}
{get_building_materials_instruction()}
{get_consumer_staples_instruction()}
{get_optical_module_instruction()}
{get_biopharma_instruction()}
{get_software_instruction()}
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
