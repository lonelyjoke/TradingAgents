# Forward Forecast Model Scaffold for 603986.SH as of 2026-07-20

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 4188075574.04 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 57.0767% / +19.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 2.3047% / +6.54pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.2202 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 1.7479% / -1.83pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 20.3043% / -11.89pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| consolidated revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
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
| consolidated | period=2026H1E (Q1 actual); revenue=11500000000.0 CNY; revenue_weight=100.0%; growth=None%; gross_margin=57.08% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| consolidated | revenue_weight=100.0%; growth=None%; gross_margin=57.08%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | missing; generate from revenue mix and business attributes |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | missing; infer and label evidence limits |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | missing; answer qualitatively with evidence boundaries |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | missing; state qualitative view and retrieval task |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | missing; compare against valuation and market-expectation context |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | missing; produce strongest bear/upside mechanism |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | missing; explain operating-variable transmission |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | missing; PM must synthesize and compress |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 4188075574.04 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 57.0767% / +19.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 34.8907% / +22.60pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 2.3047% / +6.54pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.2202 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2024, 半年 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 兆易创新2024年半年度报告: 473,449,975.70 275,474,715.87 71.87 性损益的净利润 经营活动产生的现金流量净额 1,248,715,713.30 644,561,466.59 9... |
| EV031 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2024, 半年 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 兆易创新2024年半年度报告: 473,449,975.70 275,474,715.87 71.87 性损益的净利润 经营活动产生的现金流量净额 1,248,715,713.30 644,561,466.5... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2024, 半年 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction_in_progress: 兆易创新2024年半年度报告: 或与设计或合同要求基本相符。 在建工程的减值测试方法和减值准备计提方法详见本节五、27 “长期资产减值”。 23. 借款费用 / const... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2024, 半年 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 兆易创新2024年半年度报告: 投资活动产生的现金流量净额 94,865,632.53 -576,960,897.12 不适用 筹资活动产... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2024, 半年 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 兆易创新2024年半年度报告: 筹资活动产生的现金流量净额变动原因说明：主要是①2024 年上半年取得银行短期借款 4 亿元， 回购限制性股票及二级市场股票共支出约 1.55 亿元；②2023 年上半年支付现金股利 4.14 亿元。 资产减值损失变动原因说明：主要是存货减值 0.77 亿元，比... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | revenue | 2024, 半年, 2023 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 兆易创新2024年半年度报告: 报告期内，营业收入同比增加 21.69%，主要原因是：经历 2023 年市场需求低迷和库存逐... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |
| EV043 | company_events | research_context | reported | valuation | unspecified | / earnings guidance / performance preview / 1 / |
| EV046 | company_events | research_context | reported | valuation | 20260710, 2026, 半年 | / 20260710 / earnings guidance / performance preview / 603986.SH / 兆易创新 / 兆易创新2026年半年度业绩预增公告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603986&announcementId=1225417171&orgId=9900026561&announcementTime=2026-07-10 / |
| EV052 | company_events | research_context | reported | profit_or_eps | 2026, 半年 | 1. 公司预计 2026 年半年度归属于上市公司股东的净利润为 690,000 万元左 |
| EV058 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 105.5312 / earnings multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| consolidated | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026H1E (Q1 actual); reported revenue=11500000000.0 (CNY); revenue weight=100.0%; growth=None%; gross margin=57.08%; margin change=19.64pp; source=company_events; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 303364363500 / current equity value / / / PE TTM / 105.5312 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override

- Parsed official guidance metrics: period=2026H1; revenue_cny_mn=11500; parent_net_profit_cny_mn=6900; deducted_parent_net_profit_cny_mn=4850; unit=CNY mn














| supplied official evidence | required model treatment |
| --- | --- |
| / earnings guidance / performance preview / 1 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260710 / earnings guidance / performance preview / 603986.SH / 兆易创新 / 兆易创新2026年半年度业绩预增公告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603986&announcementId=1225417171&orgId=9900026561&announcementTime=2026-07-10 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260710 / 603986.SH / 兆易创新 / 兆易创新2026年半年度业绩预增公告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603986&announcementId=1225417171&orgId=9900026561&announcementTime=2026-07-10 / N/A / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 1. 公司预计 2026 年半年度归属于上市公司股东的净利润为 690,000 万元左 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 2. 公司预计 2026 年半年度归属于上市公司股东扣除非经常性损益后的净 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 一、本期业绩预告情况 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - （一）业绩预告期间 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
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
- Readiness reasons: Segment revenue, margin, and cost breakdown for memory, MCU, sensors, analog missing – need retrieval from FY2025 annual report and product-level disclosures.; Diluted share count unresolved; total shares not provided; market cap / closing price unavailable; Tushare stock_basic data missing.; Capex, R&D, and detailed cash flow items not supplied; FCF cannot be computed.; Conflict on non-recurring items in H1 2026 parent net profit: sell-side estimates suggest large non-recurring gain (扣非约35亿 vs total 69亿) but company claims no material non-recurring; resolution requires Q2 interim report.; Foundry capacity allocation and ASP specifics for NOR/NAND/DRAM unverified; key price-volume assumptions based on unverified KPE proxies.; Required consolidated three-year forecast lines are incomplete.; Bull/base/bear per-share valuation is incomplete.; bull scenario EPS x PE does not reconcile to fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ(segment volume × ASP). Volume depends on design wins, foundry wafer allocation, and end-demand. ASP driven by memory cycle (NOR, SLC NAND, DRAM), product mix shift to higher-value SKUs, and ASP for MCU/analog.
- Profit: Gross profit = revenue – wafer costs – packaging/test costs – other COGS. Operating profit = gross profit – R&D (~17% of revenue) – SG&A. Non-operating items may include fair value changes on investments; need to isolate recurring net profit.
- Cash flow: OCF = net profit + D&A – working capital changes (inventory, receivables). Fabless model requires low capex; major reinvestment is R&D expense (already in P&L). OCF/net profit ratio historically >1x, indicating high cash conversion.
- Reinvestment: Capital-light: fabless design house with moderate R&D expense. Revenue growth requires working capital build (inventory), but asset base is mainly cash, financial investments, and some tangible assets for test/design. Reinvestment is R&D for next-gen products and customer customization.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ1 | What is the exact split of H1 2026 parent net profit of 6900 million CNY between recurring core earnings and non-recurring items (e.g., investment gains, asset sales, fair value changes)? | Unresolved: sell-side estimates suggest recurring net profit ~3500 mn vs total 6900 mn, implying 3400 mn non-recurring; company claims no material undisclosed non-recurring items, but the conflict indicates note-level disclosure required. | parent_net_profit, operating_profit, non_recurring_items | Parent net profit, EPS, P/E (adjusted for recurring) | Detailed income statement for H1 2026, including non-recurring items and segment-level operating vs non-operating classification, Audited interim report (expected before Aug 31); 2026 semi-annual report (expected Aug 2026) and management's explanation of non-recurring items. |
| UQ2 | What are the realized and expected ASP trends for NOR flash, SLC NAND, and specialty DRAM in 2026-2028, and what is the impact on revenue and gross margin trajectory? | Unverified proxies: TrendForce forecasts SLC NAND price +120-170% in H2 2026; multiple KPEs mention tight supply and price hikes, but no company-specific realized ASP data. Q1 gross margin 57% suggests significant ASP increase already captured. | memory_ASP, revenue, gross_margin, operating_margin | Memory segment revenue, Consolidated revenue, Gross margin, Operating profit | Company-specific realized ASP per product category (NOR, NAND, DRAM) quarterly, Contract/spot mix and pricing structure; Quarterly data from supply chain trackers (TrendForce, IC Insights) and Q2 2026 semi-annual report segment disclosure. |
| UQ3 | What is the actual allocated foundry wafer capacity for GigaDevice in 2026-2028 across TSMC, SMIC, and other foundries, and can it support the volume growth needed to meet the strong demand? | No disclosed capacity figures. Analysts assume company can secure incremental capacity from foundries, but this is unverified. | memory_volume, mcu_volume | Revenue, Gross profit | Foundry wafer allocation agreements, capacity outlook statements from company or foundry partners, Historical wafer input data; Management commentary on capacity outlook in 2026H1 earnings call; foundry public capex plans. |
| UQ4 | What is the diluted share count as of July 2026, including outstanding stock options, restricted shares, and potential convertible bonds? | Unresolved. No reliable share count available. Q1 seasonal share of 26.0% is a profit seasonality metric, not share count. Market cap of 303.36 bn divided by an unknown stock price yields no solution. | diluted_share_count_mn | EPS, Per-share capital metrics | Most recent total shares from Tushare stock_basic or daily_basic, Company filing of share capital (annual report, quarterly), Stock option plan details and dilution calculation; Retrieve total share capital from Tushare / CNINFO filings; check for ESOP and option grants in 2025 annual report. |
| UQ5 | What is the capex and R&D spending plan for 2026-2028, and what free cash flow can be generated after sustaining investment? | No capex breakdown given. Fabless model implies low tangible capex; R&D is expensed, not capitalized, so FCF should be high in the upcycle. Historical R&D ~17% of revenue. But confirmation needed. | capex, operating_cash_flow, free_cash_flow | FCF, Cash balance | FY2025 and Q1 2026 cash flow statements (specifically capex line), Management guidance on capex and R&D capital allocation; Retrieve cash flow statement from Tushare or financial reports; review 2025 annual report management discussion. |
| UQ6 | How sustainable is the current gross margin above 55% beyond 2026, especially if the memory cycle turns or competitors add capacity? | Unclear. Gross margin 57% in Q1 2026 vs 37% in FY2025; some of this is cyclical ASP spike, but product mix shift and higher NOR/DRAM value-add may create a higher floor. However, history shows that margins revert when supply catches up. | gross_margin, operating_margin | Gross margin, Net profit margin, EPS | Industry capacity addition plans from competitors (Winbond, Macronix, Puya) and foundry capex, Company's product mix breakdown and high-margin product share targets; Monitor industry supply announcements; review management's long-term margin guidance during H1 2026 briefing. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 9203.46 | 25000.0 | 30000.0 | 33000.0 | 2026E: H1 guidance 11,500 mn + estimated H2 13,500 mn (price/volume growth continues); 2027E: +20% Y/Y; 2028E: +10% Y/Y | analyst_estimate | Memory ASP and foundry capacity; Segment revenue break |
| consolidated | Gross margin | % | None | 58.0 | 55.0 | 50.0 | Assume peak gross margin in 2026E (Q1 57.08% trend), gradually normalizing as supply improves | analyst_estimate | Memory ASP normalization and wafer cost; FY2025 gross margin actual |
| consolidated | Operating margin | % | None | 45.0 | 40.0 | 35.0 | Operating margin = gross margin - R&D (17% of revenue) - SG&A (3% of revenue) with operating leverage assumption | analyst_estimate | R&D and SG&A scaling; FY2025 operating margin actual |
| consolidated | Operating profit | CNY mn | None | 11250.0 | 12000.0 | 11550.0 | Revenue × operating margin (25,000*0.45=11,250; 30,000*0.40=12,000; 33,000*0.35=11,550) | calculated | Revenue and margin assumptions;  |
| consolidated | Parent net profit | CNY mn | 1648.02 | 15000.0 | 18000.0 | 20000.0 | Based on H1 guidance 6900 mn and assumed H2 contribution; includes possible non-recurring items, so note quality | analyst_estimate | Non-recurring items classification and memory cycle duration; Composition of non-recurring items, Tax rate assumption |
| consolidated | EPS (diluted) | CNY | None | None | None | None | Parent net profit / diluted share count; share count missing | missing | Share count and non-recurring profit; Diluted share count (total shares + options + convertible) |
| consolidated | Operating cash flow | CNY mn | None | 18000.0 | 21600.0 | 24000.0 | Net profit × cash conversion ratio of ~1.2 (based on Q1 2026 ratio); assumes quality maintained | calculated | Working capital changes; FY2025 OCF for ratio validation |
| consolidated | Capex | CNY mn | None | None | None | None | Missing – no capex data available | missing | Investing activity; Cash paid for acquisition of fixed assets and intangibles |
| consolidated | Free cash flow | CNY mn | None | None | None | None | OCF - Capex; both inputs have missing components | missing | Capex and cash conversion; Capex, FY2025 OCF for baseline |
| consolidated | Diluted share count | mn shares | None | None | None | None | Unresolved | missing | Per-share metrics; Total shares outstanding, Dilution from options |
| consolidated | eps | CNY/share | None | 21.394875996518234 | 25.67385119582188 | 28.526501328690976 | parent net profit (CNY mn) / diluted shares (mn) | calculated | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | memory | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific price changes for NOR, SLC NAND, etc. |
| KPE02 | memory | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | impact on 兆易创新's specific product lines |
| KPE03 | memory | market_share | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | company's exposure to SLC NAND |
| KPE04 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific catalyst for 兆易创新 in AI compute |
| KPE05 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | official segment details |
| KPE06 | memory | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific volume assumptions |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-15T08:09 | 高时效/5天 | 未披露 | 近期密集参加展会，产业普遍乐观，而且产业链的沟通交流以及上下游的耦合程度很高，下半年尤其要重视H链公司！ 🔥存储：利基存储涨价开始显现在业绩端，是“此前已涨价，涨价完整放映至Q2业绩”的 📌兆易创新Q2营收约73亿，归母净利润约54亿，扣非归母约35亿 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-15T07:31 | 高时效/5天 | 未披露 | （美股） 存储芯片：太极实业、兆易创新、普冉股份、佰维存储 四、DeepSeek筹备IPO 据媒体报道，DeepSeek 已开始筹备首次公开募股（IPO），最快可能在今年年底或 2027 年初正式递交上市申请 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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