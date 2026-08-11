# Forward Forecast Model Scaffold for 002407.SZ as of 2026-08-10

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 3215501075.67 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 27.6087% / +14.14pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.4266% / +0.82pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / -1.832 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 21.2316% / +3.14pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 16.9932% / +1.99pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 新能源电池板块 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 新能源材料 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 电子化学品（半导体级氢氟酸等） revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 氟基新材料 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Battery Forecast And Valuation Controls
| control | Mandatory treatment |
| --- | --- |
| Segment model | start from filing-disclosed revenue mix; model high-weight or thesis-critical segments separately and do not add an undisclosed business bucket unless it is explicitly material to the thesis |
| Revenue bridge | GWh shipments x realized ASP by segment; reconcile mix and consolidation eliminations |
| Margin bridge | ASP/pass-through - lithium/material cost - manufacturing/depreciation/warranty; show utilization sensitivity |
| Earnings bridge | segment gross profit - R&D/SG&A/finance - tax/minority/non-recurring = parent net profit/EPS |
| Cash bridge | net profit + D&A - working capital - capex = FCF; reconcile OCF/NI and capacity expansion |
| Scenario discipline | show bear/base/bull shipment, ASP, utilization, gross margin, EPS, FCF, and valuation multiple |
| Valuation monotonicity | a deterioration case must not receive a higher multiple than base without an explicit, evidence-backed reason |
| Probability audit | record scenario probabilities before and after each private/proxy clue; unexplained probability changes are invalid |
- Missing shipment, ASP, utilization, or segment-margin evidence must remain a neutral explicit model gap; narrative strength cannot fill a numeric cell, and the gap must not mechanically alter the rating.

## Semiconductor Forecast And Valuation Controls
- Semiconductor profile: fabless / chip design. Use this profile before consumer, generic technology, telecom, metals, or battery templates.
| control | Mandatory treatment |
| --- | --- |
| Business buckets | split mature/core products from product-cycle, technology-node, customer, or tool-category optionality; do not bury optionality inside the base multiple |
| Operating bridge | start from sector-native volume x ASP x mix, then explicitly bridge gross margin, R&D, working capital, capex and share count |
| Foundry / manufacturing | use wafer capacity, utilization, wafer ASP, node mix, yield, depreciation, capex, construction-in-progress transfer, and equipment access |
| Chip design | use shipments, ASP, design wins, tape-out/mass-production milestones, customer concentration, foundry/package cost, inventory and R&D/IP moat |
| Semiconductor equipment | use new orders, backlog, delivery/acceptance, tool-category mix, localization rate, installed base/service, inventory, advances and receivables |
| Valuation triangulation | PE is only one cross-check. Also show EV/EBITDA, DCF/FCF, ROIC/PB or SOTP/NAV depending on asset intensity and disclosure |
| Optionality discipline | AI, advanced node, localization or strategic-scarcity value must have explicit probability, payoff, verification gate and overlap key; unverified optionality cannot enter base value |
| Market-implied check | reverse current market cap into required revenue, gross margin, net profit, ROIC, backlog conversion or node/product contribution; compare with the model |
- A semiconductor Buy/Underweight call is incomplete if it relies only on static PE/PB or valuation percentiles without the operating bridge above.

## Consumer-Staples Product, Cost And Cash Controls
| control | Mandatory treatment |
| --- | --- |
| Business buckets | model every material filing product, channel and consolidated subsidiary separately; identify core, growth, scenario, optionality and excluded/double-counted value |
| Revenue bridge | saleable volume x realized ASP x product/channel mix; distinguish end-demand sell-through from distributor restocking and acquisition consolidation |
| Raw-material bridge | map each material input to a dated price range/percentile, company purchase basis and pass-through or inventory-cost lag; do not infer margin directly from one futures move |
| Gross-profit sensitivity | product revenue - grade/product-matched raw material - packaging - energy - logistics - conversion cost; show the CNY mn gross-profit and parent-profit effect of each price/margin shock |
| Channel and cash | reconcile distributor inventory, contract liabilities/advances, receivables, inventory, OCF/NI and promotional rebates before calling shipment growth real demand |
| Subsidiaries / acquisitions | show revenue, margin, minority interest, purchase-price allocation, goodwill/impairment, cash conversion and consolidation effects separately |
| Three-year closure | product/subsidiary revenue and profit must sum to group revenue, operating profit, parent profit, EPS, OCF, capex and FCF for all three years |
| Valuation | connect normalized EPS/FCF and ROE/payout to PE/FCF-yield or SOTP; keep unverified new categories and overseas projects in probability-weighted optionality |
- If product volume/ASP, subsidiary profit or raw-material basis data are unavailable, keep the affected cells missing/partial, quantify a bounded sensitivity, and name the next filing or channel verification instead of filling the gap with a narrative growth rate.

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| 新能源电池板块 | period=annual filing; revenue=2849639910.66 filing table unit not explicit in extracted row; revenue_weight=32.48555110603593%; growth=76.84%; gross_margin=12.57% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 新能源材料 | period=2026H1; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 电子化学品（半导体级氢氟酸等） | period=2026H1; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 氟基新材料 | period=unspecified; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 新能源电池板块 | revenue_weight=32.48555110603593%; growth=76.84%; gross_margin=12.57%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 新能源材料 | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 电子化学品（半导体级氢氟酸等） | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 氟基新材料 | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | missing; generate from revenue mix and business attributes |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | missing; infer and label evidence limits |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | missing; answer qualitatively with evidence boundaries |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | LLM analysis layer unavailable; deterministic facts may be used, but business questions, expectation gap, red-team critique and editorial synthesis must be regenerated before publishing a high-conviction PM report. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | missing; compare against valuation and market-expectation context |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | missing; produce strongest bear/upside mechanism |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | missing; explain operating-variable transmission |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | missing; PM must synthesize and compress |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | net profit / EPS | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | net profit / EPS | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 3215501075.67 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 27.6087% / +14.14pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 11.6787% / +8.59pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.4266% / +0.82pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / -1.832 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -65.92%, gross margin change 13.65pp, operating margin change 13.16p... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2025, 年度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2025年年度报告: 20,841,454.94 -25,650,713.14 -18,522,411.94 122,062,565.58 经常性损益的净利润 经营活动产生的现金流量净额 -210,690,5... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction_in_progress: 2025年年度报告: 我们检查与营业收入相关的信息是否已在财务报表中作出恰当列报。  长期资产减值计提事项 2025 年度多氟多公司固定资产、在建工程及无形资产减值金额为... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2025, 年度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2025年年度报告: 资产减值 -57,654,408.04 -22.29% 否 减值测试，同时叠加部分存货减值因素 影响，计提存货跌价准... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2025, 年度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 2025年年度报告: 产线存在减值迹象，公司根据行业发展 资产减值 -57,654,408.04 -22.29% 否 减值测试，同时叠加部分存货减值因素 / inventory: 2025年年度报告: 资产减值 -57,654,408.04 -22.29% 否 减值测试，同时叠加部分存货减值因... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: （3）报告期内主要产品发展现状 公司目前具备六氟磷酸锂的规模化生产能力，拥有双氟磺酰亚胺锂（LiFSI... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |
| EV041 | company_events | research_context | reported | valuation | unspecified | / earnings guidance / performance preview / 1 / |
| EV042 | company_events | research_context | reported | valuation | 20260711, 2026, 半年 | / 20260711 / earnings guidance / performance preview / 002407.SZ / 多氟多 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002407&announcementId=1225419392&orgId=9900012449&announcementTime=2026-07-11 / |
| EV049 | company_events | research_context | reported | profit_or_eps | unspecified | 基本每股收益 盈利：0.38 元/股–0.47 元/股 盈利：0.0441 元/股 |
| EV052 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 83.0783 / earnings multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 新能源电池板块 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=2849639910.66 (filing table unit not explicit in extracted row); revenue weight=32.48555110603593%; growth=76.84%; gross margin=12.57%; margin change=10.5pp; source=filing_intelligence; mode=deterministic_filing_row |
| 新能源材料 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026H1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model, knowledge_planet; mode=llm_semantic |
| 电子化学品（半导体级氢氟酸等） | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026H1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction, company_business_model, knowledge_planet; mode=llm_semantic |
| 氟基新材料 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=management_capital_allocation; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 43498403550 / current equity value / / / PE TTM / 83.0783 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
OFFICIAL_GUIDANCE_DISCLOSURE: target=002407.SZ; source_scope=company_announcement; numeric_record_status=missing
| supplied official evidence | required model treatment |
| --- | --- |
| / 20260711 / 002407.SZ / 多氟多 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002407&announcementId=1225419392&orgId=9900012449&announcementTime=2026-07-11 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - （一）业绩预告期间：2026 年 1 月 1 日至 2026 年 6 月 30 日 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - （二）业绩预告情况： | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 扣除非经常性损益 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 基本每股收益 盈利：0.38 元/股–0.47 元/股 盈利：0.0441 元/股 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
- If official guidance conflicts with the prior run-rate or sell-side/proxy assumption, update the forecast or state the exact reason it cannot be used. Do not ignore the guidance.
- After guidance is available, the next verification point is the formal report's segment mix, cost bridge, cash conversion and balance-sheet quality, not whether the guided profit strength exists.

## Assumption Change And Valuation Transmission Ledger
| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |
- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.
- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.

## Shared Company Underwriting Packet
- Research readiness: partial
- Readiness reasons: LLM company underwriting failed; deterministic evidence remains usable and the missing analysis should be retried.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 
- Profit: 
- Cash flow: 
- Reinvestment: 

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | revenue |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | gross_margin |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | operating_profit |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | parent_net_profit |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | EPS |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | OCF |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | capex |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | FCF |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE04 | 新能源材料 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 等待8月真实排产数据验证 | 公司具体出货量数据 |
| KPE06 | 新能源材料 | asp_or_price | None 万元/吨 | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 跟踪6F价格月度走势 | 公司6F销量和单位成本 |
| KPE09 | 新能源材料 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 与公司半年报产销量数据交叉验证 | 公司电池出货量 |
| KPE10 | 新能源材料 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 验证8月实际排产数据 | 公司具体排产计划 |
| KPE11 | 新能源材料 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 持续跟踪行业需求数据 | 公司市占率假设 |
| KPE12 | 新能源材料 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 验证8月排产数据 | 公司具体排产计划 |
| KPE01 | 电子化学品（半导体级氢氟酸等） | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE02 | consolidated/unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE03 | consolidated/unmapped | profit_or_eps | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE05 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE07 | 新能源电池板块 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE08 | 新能源电池板块 | profit_or_eps | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-08-06T16:12 | 高时效/4天 | 未披露 | 涨停板：中巨芯、蜀道装备、和远气体、滨化股份、多氟多、中欣氟材 其他强势股：昊华科技、华特气体、金宏气体、中船特气、广钢气体 先进封装/材料 据市场研究机构Yole预估，2025年全球先进封装的市场规模为540亿美元，预计到2031年将增至1090亿美元 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-27T09:14 | 有效窗口/14天 | 未披露 | 未提取到带期间的明确盈利预测 | 投资建议：龙头公司对应27年估值10-15x，低估明显，继续强推格局和盈利稳定龙头电池（推荐宁德时代、亿纬锂能、蔚蓝锂芯、鹏辉能源、比亚迪、中创新航、欣旺达）、以及具备涨价弹性和优质锂电材料龙头，推荐隔膜、铝箔、铜箔、六氟、结构件等环节（推荐璞泰来、恩捷股份、鼎胜新材、佛塑科技、尚太科技、科达利、诺德股份、湖南裕能、天赐材料、富临精工、星源材质、华友钴业、嘉元科技等，关注华盛锂电、海科新源、德福科技、多氟多、万润新能、龙蟠科技、石大胜华等） | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 机构未识别/2026-07-23T13:13 | 有效窗口/18天 | 未披露 | 未提取到带期间的明确盈利预测 | [爱心]投资建议：龙头公司对应27年估值10-15x，低估明显，继续强推格局和盈利稳定龙头电池（推荐宁德时代、亿纬锂能、蔚蓝锂芯、鹏辉能源、比亚迪、中创新航、欣旺达）、以及具备涨价弹性和优质锂电材料龙头，推荐隔膜、铝箔、铜箔、六氟、结构件等环节（推荐璞泰来、鼎胜新材、科达利、恩捷股份、佛塑科技、尚太科技、嘉元科技、诺德股份、湖南裕能、天赐材料、富临精工、星源材质、华友钴业等，关注德福科技、多氟多、万润新能、龙蟠科技、华盛锂电、海科新源、石大胜华等） | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
- Do not average incompatible forecast years, valuation dates or methods.
- A range or median may be called consensus only when a named multi-broker sample and statistical basis are supplied.

## Mandatory Three-Year Table
| item | 2026E | 2027E | 2028E | evidence / assumption status |
| --- | --- | --- | --- | --- |
| Revenue | to be estimated | to be estimated | to be estimated | reconcile segment volume, ASP, mix, and eliminations |
| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |
| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |
| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |
| Operating cash flow / capex / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and reinvestment |

## Analyst Instructions
- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.
- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.
- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.
- If an official earnings preview, guidance or quick report is available, it overrides run-rate extrapolation for the covered period until the formal report supplies segment, cash-flow and balance-sheet detail.
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.
- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.