# Forward Forecast Model Scaffold for 000933.SZ as of 2026-07-21

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 12408562541.64 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 33.4845% / +18.56pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.2215% / -0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.764 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 3.0156% / +0.40pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 7.7454% / -2.03pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Aluminum revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Coal revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Aluminum Foil revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

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

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| Aluminum | period=2025 H1; revenue=14182200791.47 CNY; revenue_weight=69.43%; growth=20.79%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| Coal | period=2025 H1; revenue=2887344129.29 CNY; revenue_weight=14.13%; growth=-18.99%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| Aluminum Foil | period=unspecified; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| Aluminum | revenue_weight=69.43%; growth=20.79%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| Coal | revenue_weight=14.13%; growth=-18.99%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| Aluminum Foil | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | 1. Coal segment: Is the realized coking coal price in H1 2026 above or below 1,275 RMB/ton, and what is the volume trend?; 2. Aluminum segment: What was the actual Q1 2026 aluminum sales volume and unit electricity cost? Can the 33.5% gross margin be sustained if aluminum price stays at 23,000?; 3. Aluminum foil: What customers have qualified the company's 8μm battery foil, and what processing fee is being realized?; 4. Conflict resolution: Is the H1 2026 performance preview reliable, or does the preview contain an error in unit or classification? |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | Aluminum segment contributes ~70% of revenue and likely >80% of gross profit given the recent margin surge. Therefore, aluminum price and power cost are the most influential variables. Coal is a secondary profit pool but declining. Aluminum foil is a potential third pool that could become meaningful by 2028 if battery demand materializes, but currently it is small and should be treated as optionality rather than core. |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | True peers are 云铝股份 (000807), 焦作万方 (000612), 中孚实业 (600595), 天山铝业 (002532), 明泰铝业 (601677). Among them, 云铝股份 and 焦作万方 have similar aluminum-focused business with higher roe and lower leverage. Shenhuo's coal segment differentiates it but also adds commodity cycle correlation. Substitution risk: aluminum in construction faces competition from steel, plastics, and composites; in power, copper is an alternative for some applications but not all. Battery foil competes with rolled copper foil in some battery types. No evidence of disruptive technology threatening aluminum demand in the near term. The main competitive differentiator is location: Shenhuo's Xinjiang base has low-cost self-generated po |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | The qualitative view is that Shenhuo's aluminum smelting enjoys a structural cost advantage, leading to above-average margins through the cycle. Without segment-level cost data, this cannot be quantified precisely. Currently, we have only Q1 2026 consolidated gross margin of 33.48% and peer margins around 35-36%. This suggests the advantage may be real but not unique. To quantify, we need: (1) aluminum output in 2025 and 2026, (2) electricity consumption and tariff per ton for each smelter, (3) alumina purchase cost. Once obtained, we can build a unit margin bridge. The H1 profit preview of 19.0 billion (on 1,904 mn) may include non-recurring items; separating those will reveal true operatin |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | The market values Shenhuo at 9.8x TTM PE (69.9 percentile over 5 years) and 1.25x PS (79.7 percentile), which suggests the market already prices in some recovery but is cautious due to commodity uncertainty. Implied TTM earnings of CNY 5.59 bn are above the latest annual figure of CNY 4.01 bn, implying the market expects >39% earnings growth. If the company only delivers CNY 4.0 bn in 2026 (base case), it would fall short of TTM expectations, potentially causing de-rating. If however, Q2 weakness is temporary and underlying earnings can reach CNY 5-6 bn, the stock may be undervalued. The gap is mainly about the trajectory of aluminum margins and resolution of the H1 profit conflict. |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | Bear thesis: The H1 performance preview indicates a dramatic Q2 loss; if Q1 was boosted by one-off items or unsustainable pricing, full-year profit could be as low as CNY 2 bn, putting the stock at 27.5x FY2026E PE, which is expensive. Aluminum prices may have peaked, and the energy-intensive industry faces carbon costs and potential demand destruction from China's property downturn. Moreover, the shareholder selling suggests insider caution. Falsification signal: If H1 2026 report confirms Q2 operating loss and no non-recurring explanations, base case must be cut.; Bull counter to bear: Even if Q2 was weak, aluminum supply remains constrained and demand from EVs and power grid investment is |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | Under base case, we apply a 9x P/E multiple to 2027E net profit of CNY 4.1 bn, derived from moderate aluminum prices and limited foil contribution. 9x is consistent with the current commodity P/E for Chinese aluminum producers (range 8-10x) and reflects through-cycle earnings. Bull case uses 12x on higher earnings reflecting a premium for growth and cost advantage; bear case uses 8x. The core equity value is CNY 36.9 bn plus optionality of CNY 3.0 bn for aluminum foil, but probability-weighted fair value cannot be calculated without share count. The model is anchored on aluminum price: each CNY 1,000/t change shifts fair value by approximately 15-20%. The valuation is highly sensitive to the |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | Shenhuo is a classic commodity play where the investment case turns on one question: are the recent stellar margins sustainable, or was Q1 a fluke? The Q1 numbers, if annualized, would make the stock look very cheap, but the H1 preview casts serious doubt. A portfolio manager should focus on: (1) The 2026 semi-annual report on July 28 will either confirm the profit cliff or reveal accounting noise. (2) Even if aluminum prices soften, the company's Xinjiang cost advantage should prevent a return to loss-making territory. (3) The aluminum foil business is a free call option on battery demand, but it needs tangible proof of scale and margin before adding to valuation. Position sizing should ref |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE02 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | 产品报价、毛利率、竞品价格、下游接受度、行业价格指数 | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 12408562541.64 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 33.4845% / +18.56pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 18.4525% / +11.10pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.2215% / -0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.764 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 2026年一季度报告: 2,271,764,611.82 714,922,693.47 217.76 净利润（元） 经营活动产生的现金流量净额（元） 4,039,054,901.65 1,687,756,817.4... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026年一季度报告: 2,271,764,611.82 714,922,693.47 217.76 净利润（元） 经营活动产生的现金流量净额（元） 4,039,054,901.65 1,687,756,81... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 其他债权投资 长期应收款 长期股权投资 5,182,180,317.16 5,166,787,905.93 / long_term_equi... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | segment_volume | 2025, 年度 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgrade: 2025年年度报告: 2025 年，煤炭市场供需总体呈现宽松格局，供应方面国内煤炭产量在保供政策引导下维持高位，进口煤量虽同比有所 回落，但仍保持历史较高水平，需求方面受宏观经济增速放缓、能源... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 报告期末，公司铝加工板块应收账 款规模增加，根据会计政策以固定 17 信用减值损失 -7,873,058.09 -... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | revenue | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 价值发生变动。 报告期内，公司铝加工板块量价齐 3 应收账款 1,461,917,412.34 1,069,147,929.52 36.74 升带动营收增长，叠加客户账期较 / receivables: 2026年一季度报告: 报告期内，公司铝加工板块量价齐 3 应... |
| EV041 | company_events | research_context | reported | valuation | unspecified | / earnings guidance / performance preview / 1 / |
| EV043 | company_events | research_context | reported | valuation | 20260710, 2026, 半年 | / 20260710 / earnings guidance / performance preview / 000933.SZ / 神火股份 / 河南神火煤电股份有限公司2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=000933&announcementId=1225416665&orgId=gssz0000933&announcementTime=2026-07-10 / |
| EV047 | company_events | research_context | reported | profit_or_eps | unspecified | 2、业绩预告情况：预计净利润为正值且属于同向上升情形 |
| EV049 | company_events | research_context | reported | profit_or_eps | unspecified | 归属于上市公司股东的净利润 190,445.68 |
| EV052 | company_events | research_context | reported | profit_or_eps | unspecified | 扣除非经常性损益后的净利润 201,006.92 |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Aluminum | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025 H1; reported revenue=14182200791.47 (CNY); revenue weight=69.43%; growth=20.79%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| Coal | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025 H1; reported revenue=2887344129.29 (CNY); revenue weight=14.13%; growth=-18.99%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| Aluminum Foil | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 55010647624 / current equity value / / / PE TTM / 9.8466 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
| / earnings guidance / performance preview / 1 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260710 / earnings guidance / performance preview / 000933.SZ / 神火股份 / 河南神火煤电股份有限公司2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=000933&announcementId=1225416665&orgId=gssz0000933&announcementTime=2026-07-10 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260710 / 000933.SZ / 神火股份 / 河南神火煤电股份有限公司2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=000933&announcementId=1225416665&orgId=gssz0000933&announcementTime=2026-07-10 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 1、业绩预告期间：2026 年 1 月 1 日至 2026 年 6 月 30 日。 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 2、业绩预告情况：预计净利润为正值且属于同向上升情形 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 归属于上市公司股东的净利润 190,445.68 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 扣除非经常性损益后的净利润 201,006.92 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 基本每股收益（元/股） 2.169 0.860 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - Treat official earnings guidance, performance previews, and quick reports as harder evidence than run-rate extrapolation; reconcile stated H1/Q1/Q2/EPS ranges before writing forecast, valuation, rating, or next-verification language. | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
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
- Readiness reasons: Conflict between Q1 2026 net profit (CNY 2,289.7 mn) and H1 2026 performance preview (CNY 1,904.5 mn) not yet resolved; model base case must reflect this contradiction.; Diluted share count not available from supplied evidence; market cap, PE TTM, and parent profit cannot be conclusively combined to derive share count. EPS and per-share valuation remain conditional.; Segment-level gross margin and production volume for Coal and Aluminum are missing; consolidated margins used as proxy.; Aluminum Foil segment revenue and margin are not separately reported; treated as analytical only.; Forward capex and precise working-capital assumptions are not directly reported; OCF and FCF are estimated from reported ratios.; One or more filing-reported segments required deterministic restoration.; Material segment three-year driver lines are missing: Aluminum, Aluminum Foil, Coal; Bull/base/bear per-share valuation is incomplete.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ (segment_volume_i × realized_price_i) where i ∈ {coal (coking/thermal), aluminum (ingot/liquid), aluminum foil (aluminum price + processing fee)}.
- Profit: Gross profit = revenue – (electricity, alumina, coal mining cost, other raw materials, labor); operating profit = gross profit – selling/admin expenses – depreciation; parent profit = operating profit – finance expense – tax – minority interests; margin heavily depends on aluminum price versus electricity and alumina cost spread.
- Cash flow: OCF closely tracks earnings with working-capital noise (Q1 2026 OCF/net profit = 1.76x); capex is maintenance-oriented plus limited growth projects (wind power, mine upgrades); FCF = OCF – capex.
- Reinvestment: Moderate capital intensity with most reinvestment focused on maintaining coal mine capacity (7.95 Mt/year) and aluminum smelter efficiency, plus a recently commissioned wind farm in Xinjiang. New capacity additions in aluminum foil may require growth capex but are not yet quantified.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | What caused the sharp QoQ profit decline implied by the H1 2026 preview (CNY 1,904 mn vs Q1 alone CNY 2,290 mn)? Is the Q2 loss real or due to unit/accounting restatement? | unresolved | 2026E parent net profit, 2026E EPS, scenario probabilities | consolidated net profit 2026E-2028E, EPS, FCF | H1 2026 interim report with detailed segment P&L and explanation of non-recurring items., Confirmation of unit and treatment of impairment or investment losses.; 2026-07-28 semi-annual report release. |
| Q2 | What is the company's realized aluminum price relative to SHFE, and what are the actual unit electricity and alumina costs for its Xinjiang and Yunnan smelters? | unresolved | Aluminum segment gross margin, operating margin | consolidated gross margin, operating profit, net profit | Aluminum segment revenue and cost breakdown from 2025 annual report or 2026 semi-annual report., Electricity procurement contracts and alumina sourcing details.; Review 2025 annual report segment notes (already compacted; may need manual extraction) and 2026H1 report. |
| Q3 | What are the actual production volumes for coal and aluminum in 2025 and 2026 YTD, and what are the expected utilization rates? | unresolved | coal revenue, aluminum revenue, operating leverage | consolidated revenue, gross profit | Annual coal output for 2025, 2026., Aluminum output in metric tons.; 2025 annual report and 2026 semi-annual report production data. |
| Q4 | Does the aluminum foil segment generate meaningful profit, and what is the processing-fee trend across battery, food, and pharma foils? | unresolved | Aluminum foil segment profit, optionality valuation bucket | consolidated net profit (if material), SOTP optionality | Aluminum foil revenue, tonnage, processing fee, and margins by product type.; Seek specific aluminum foil segment disclosure in 2026 semi-annual or annual report, or management commentary. |
| Q5 | How sensitive is consolidated EPS to a USD 1,000/ton decline in aluminum price, assuming no change in aluminum cost? | unmodeled | EPS, FCF | revenue, gross profit, net profit | Aluminum tonnage sold, exact cost structure, and hedging policy.; Build explicit aluminum price sensitivity table from segment-level data when available. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 41241.0 | 51000.0 | 52500.0 | 54000.0 | Base case assumes Q1 2026 annualized revenue of CNY 49,634 Mn adjusted upward for modest volume and price recovery in H2; 2027-2028 assume 3% growth from demand and aluminum foil ramp. | analyst_estimate | Significantly responsive to aluminum price (+/-10% = ~CNY 5,100 mn revenue impact); Q2-Q4 2026 quarterly revenue, breakdown by segment |
| consolidated | Gross Margin | % | None | 20.0 | 19.0 | 18.5 | 2026: Q1 actual 33.48% is considered unsustainable; full-year estimated at ~20% reflecting Q2 margin compression and H2 aluminum price weakness. 2027-2028 normalize toward mid-to-late cycle margins. | analyst_estimate | 1pp change in gross margin = ~CNY 510 mn in gross profit.; FY2025 gross margin (not supplied), quarterly margin trajectory |
| consolidated | Operating Margin | % | None | 15.0 | 14.0 | 13.5 | Gross margin less SG&A and depreciation; Q1 2026 was 29.18%, full-year assumed to moderate to 15% due to higher fixed-cost absorption and H2 commodity weakness. | analyst_estimate | Operating leverage amplifies gross margin changes.; FY2025 operating margin, detailed expense ratios |
| consolidated | Operating Profit | CNY mn | None | 7650.0 | 7350.0 | 7290.0 | Revenue × Operating Margin | derived | ;  |
| consolidated | Parent Net Profit | CNY mn | 4005.0 | 4000.0 | 4100.0 | 4200.0 | 2026E: assumed similar to FY2025 despite higher revenue, because Q1 net profit of CNY 2,289.7 mn annualized would be CNY 9,159 mn, but H1 preview of only CNY 1,904 mn forces a very weak H2. Base case adopts a full-year result near FY2025 level to reflect current uncertain but still healthy profitability. 2027-28 modest growth. | analyst_estimate | Aluminum price and Q2 reconciliation are critical.; H2 2026 quarterly net profit, tax rate, minority interest |
| consolidated | EPS | CNY/share | None | 1.7785647737187908 | 1.8230288930617606 | 1.8674930124047304 | parent net profit (CNY mn) / diluted shares (mn) | calculated | ; diluted share count |
| consolidated | Operating Cash Flow | CNY mn | None | 6000.0 | 6150.0 | 6300.0 | Assumed OCF / NP ratio of 1.5x for 2026-2028, slightly below Q1 1.76x to reflect normalized working-capital build. | analyst_estimate | ; FY2025 OCF |
| consolidated | Capex | CNY mn | None | 1500.0 | 1500.0 | 1500.0 | Estimated maintenance and moderate growth capex for mining and smelting; not directly quoted. | analyst_estimate | ; historical capex, growth project budget |
| consolidated | Free Cash Flow | CNY mn | None | 4500.0 | 4650.0 | 4800.0 | OCF – Capex | derived | ;  |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | Aluminum | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | numeric price impact, baseline price assumption |
| KPE02 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific profit numbers from private channel |
| KPE04 | Coal | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific impact on company's realized price |
| KPE05 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 产品报价、毛利率、竞品价格、下游接受度、行业价格指数 | numeric baseline and revision |
| KPE03 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

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