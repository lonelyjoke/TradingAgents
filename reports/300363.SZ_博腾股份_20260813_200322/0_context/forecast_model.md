# Forward Forecast Model Scaffold for 300363.SZ as of 2026-08-13

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 886037955.06 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 30.5994% / +4.27pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.8488% / -0.05pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.0864 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 23.4389% / -0.47pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 22.3143% / -0.28pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 小分子原料药CDMO revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 新分子业务 (小分子制剂、多肽与寡核苷酸、蛋白与偶联药物、细胞与基因治疗等) revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 大健康消费品 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Semiconductor Forecast And Valuation Controls
- Semiconductor profile: semiconductor equipment / wafer-fab tools. Use this profile before consumer, generic technology, telecom, metals, or battery templates.
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
| 小分子原料药CDMO | period=2026年上半年（指引），2025年（收入占比）; revenue=90.0 占营收比例约; revenue_weight=90.0%; growth=13.0%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 新分子业务 (小分子制剂、多肽与寡核苷酸、蛋白与偶联药物、细胞与基因治疗等) | period=2025年年度; revenue=0.68 亿元; revenue_weight=10.0%; growth=224.0%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 大健康消费品 | period=2026年7月，公司成立初期; revenue=None; revenue_weight=0.0%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 小分子原料药CDMO | revenue_weight=90.0%; growth=13.0%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 新分子业务 (小分子制剂、多肽与寡核苷酸、蛋白与偶联药物、细胞与基因治疗等) | revenue_weight=10.0%; growth=224.0%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 大健康消费品 | revenue_weight=0.0%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | Will the core CDMO orderbook convert to 2027-2028 revenue, and what is the book-to-bill by phase?; Is the reported H1 2026 profit weakness fully explained by the Slovenia one-off, or are underlying margins still below normalized?; Can OCF conversion improve from 0.0864x to a level that supports FCF-based valuation?; Does the new molecule business have enough sub-line evidence (payload, peptide, formulation) to be valued separately? |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | Small molecule API CDMO is the dominant profit pool because it is ~90% of revenue and drives the current margin recovery. New molecule business is strategically interesting but only ~2% of revenue in 2025 and lacks disclosed profit/cash; it should be treated as optionality. Consumer health is zero-revenue and excluded. |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | Bo Teng competes with larger integrated CDMOs on end-to-end small molecule capability and with specialist ADC/payload players in new modalities. The true peer boundary is not the Tushare industry peer list; it is global CDMO capability for complex molecule development and manufacturing. Customer substitution can be in-house pharma capacity or competing CDMOs; supplier/self-supply risk is highest in commoditized small molecule capacity and lowest in qualified high-activity payload work. New entrants and capacity expansion may pressure price even if demand is growing. |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | The qualitative story is that the CDMO cycle is recovering, high-margin delivery is improving, and AI4S may increase molecule volume. Quantification is limited because the payload provides no backlog value, no segment profit, no capacity utilization, and no reported share count. Therefore margin and revenue directions can be modeled, but EPS/FCF/fair-value per share remain partial. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | Market cap CNY 12.15bn and PE TTM 94.57 imply the market expects strong normalization of clean earnings and probably AI4S/new modality optionality. The model differs by being unable to verify the earnings normalization with cash-flow evidence and by treating the 2026 reported loss as a distortion around a still-small clean profit base. The gap may be more about cash-flow conversion and share count than direction. |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | Bull thesis counter: Q1 OCF/net profit of 0.0864x and low operating margin suggest the margin recovery is not yet cash-backed; if the 2026H1 clean profit growth is driven by one-time high-margin deliveries, the stock is pricing cycle optimism without proof.; Bear thesis counter: Official H1 revenue guidance is positive and the impairment is explicitly described as one-off; ex-impairment H1 profit +196%-343% and tighter high-activity capacity could support a rapid recovery if receivables/inventory normalize. |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | Valuation should be a function of normalized clean EPS and OCF conversion, not the distorted reported 2026 loss. Multiple selection depends on revenue durability and cash conversion; at a PE TTM of 94.57, the market is paying for normalized earnings several years forward. Without share count and full-year clean profit, valuation remains a bounded gap rather than a point estimate. |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | A PM-facing synthesis should explain that Bo Teng is a core global small molecule CDMO seeing recovering revenue and gross margin, but the current equity value embeds high expectations that require proof of backlog, clean profit durability, and cash collection. Slovenia is a one-time accounting shock; the main investment question is whether strong order growth converts to FCF over the next two years. |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | capex / ROIC / scenario probability | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 886037955.06 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 30.5994% / +4.27pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 3.1449% / +3.68pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.8488% / -0.05pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.0864 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2024, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 博腾股份：2024年三季度报告: -39,393,019.51 -211.61% -213,499,138.84 -149.58% 性损益的净利润（元） 经营活动产生的现金流量净额 / operating_cash... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2024, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 博腾股份：2024年三季度报告: -39,393,019.51 -211.61% -213,499,138.84 -149.58% 性损益的净利润（元） 经营活动产生的现金流量净额 / operating_c... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2024, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 博腾股份：2024年三季度报告: 其他债权投资 长期应收款 长期股权投资 344,248,277.17 362,976,190.13 / long_term_equ... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2024, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 博腾股份：2024年三季度报告: 收益 所致 主要系上期应收账款收回，计 信用减值损失 -9,884,621.49 38,295,627.... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2024, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 博腾股份：2024年三季度报告: 货币资金 1,402,462,655.01 1,966,562,994.13 -564,100,339.12 -28.68 主要系本期销售收款减少所致 主要系本期末应收银行承兑汇票增 应收账款融资 14,341,836.08 6,071,888.52 8,... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 低业务波动风险。同时，公司还将通过持续提升产品服务与研发创新能力，打 造自身核心竞争力，在竞争日益加剧... |
| EV043 | company_events | research_context | reported | valuation | unspecified | / earnings guidance / performance preview / 1 / |
| EV049 | company_events | research_context | reported | valuation | 20260714, 2026, 半年 | / 20260714 / earnings guidance / performance preview / 300363.SZ / 博腾股份 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=300363&announcementId=1225423591&orgId=9900022740&announcementTime=2026-07-14 / |
| EV055 | company_events | research_context | reported | revenue | unspecified | 营业收入 收入：162,094 万元 |
| EV058 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 94.5711 / earnings multiple the market is paying now / |
| EV059 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.4672 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 小分子原料药CDMO | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026年上半年（指引），2025年（收入占比）; reported revenue=90.0 (占营收比例约); revenue weight=90.0%; growth=13.0%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 新分子业务 (小分子制剂、多肽与寡核苷酸、蛋白与偶联药物、细胞与基因治疗等) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年年度; reported revenue=0.68 (亿元); revenue weight=10.0%; growth=224.0%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| 大健康消费品 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026年7月，公司成立初期; reported revenue=None (); revenue weight=0.0%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 12151367592 / current equity value / / / PE TTM / 94.5711 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
OFFICIAL_GUIDANCE_DISCLOSURE: target=300363.SZ; source_scope=company_announcement; numeric_record_status=missing
| supplied official evidence | required model treatment |
| --- | --- |
| / 20260714 / 300363.SZ / 博腾股份 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=300363&announcementId=1225423591&orgId=9900022740&announcementTime=2026-07-14 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - （一）业绩预告期间 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - （二）业绩预告情况： | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 归属于上市公司股东的净利润 亏损：-25,000 万元~ -21,000 万元 盈利：2,706 万元 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 本业绩预告相关的财务数据未经会计师事务所审计。 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
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
- Readiness reasons: Material filing-backed segments identified, but full-year 2026 and 2027-2028 profit/cash-flow cells cannot be fully closed from supplied evidence.; Share count is unresolved: market cap is supplied but current price and authoritative total_share are not, so EPS and per-share fair value are partial.; Segment economics are only partially disclosed: small molecule core is ~90% of revenue, but FY2025 segment gross/operating profit and order backlog are not supplied.; 2026H1 official guidance is hard for revenue and impairment; H2 and normalized run-rate profitability require the 2026 interim report.; Cash-flow conversion is a flagged risk because 2026Q1 OCF/net profit is only 0.0864 and reinvestment/capex detail is incomplete.; One or more filing-reported segments required deterministic restoration.; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 小分子原料药CDMO, 新分子业务 (小分子制剂、多肽与寡核苷酸、蛋白与偶联药物、细胞与基因治疗等)
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Core project delivery: opening backlog + new orders - delivered/recognized orders = ending backlog; revenue = recognized project/delivery volume x price/mix. Capacity-output businesses: effective capacity x utilization x yield x saleable volume x realized ASP/mix.
- Profit: Gross profit = revenue - raw materials/direct labor/manufacturing costs; operating profit = gross profit - R&D/selling/admin - impairment/other; parent profit = operating profit - finance costs - tax - minority interest.
- Cash flow: OCF = net profit + depreciation/amortization - working-capital change; FCF = OCF - cash paid for long-term assets/capex.
- Reinvestment: Fixed-asset-intensive CDMO capacity; FY2023-FY2025 fixed assets reported at CNY 2.875bn, 3.073bn, 2.891bn with depreciation CNY 269mn, 311mn, 340mn. Reinvestment includes high-activity facilities and terminates Slovenia project with ~CNY 330mn impairment.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ01 | What is the final cash and income-statement treatment of the Slovenia R&D production base termination beyond the ~CNY 330mn impairment? | Official H1 guidance confirms ~CNY 330mn impairment and guided H1 loss; H2 and final cash impact unresolved. | impairment, operating profit, parent net profit, FCF | 2026E parent net profit, 2026E OCF, 2026E FCF | H2 2026 income/cash effect, exit cost or sale proceeds, tax effect of impairment; 2026 interim report cash-flow and impairment notes |
| UQ02 | Will H1 2026 CDMO order growth of 8%-12% convert into 2027-2028 revenue after current deliveries? | Company and broker channel checks state new orders and revenue grew well in H1 2026, but no backlog/book-to-bill is supplied. | new orders, ending backlog, revenue growth | 2026E-2028E consolidated revenue, small molecule CDMO revenue | backlog in CNY, book-to-bill, order composition by phase; Interim report segment/order disclosure |
| UQ03 | Is the Q1 2026 gross margin increase of +4.27pp sustainable and does it reflect structural mix or temporary high-margin product delivery? | Q1 2026 gross margin 30.60%, +4.27pp; company attributes H1 clean profit growth to high-margin product delivery and scale effects. | gross margin, product mix, utilization | gross profit, operating profit, parent net profit | product mix, cost per batch/unit, fixed cost absorption; H1 2026 segment gross margin and revenue mix |
| UQ04 | When will OCF convert? Q1 2026 OCF/net profit is only 0.0864. | Q1 OCF/net profit 0.0864; receivables/revenue 23.44% and inventory/revenue 22.31% both declined slightly YoY. | OCF, receivables, inventory, FCF | 2026E-2028E OCF, FCF | Q1 cash-flow statement detail, collection terms, inventory aging; H1 2026 cash-flow statement |
| UQ05 | Can the new molecule business scale from CNY 68mn revenue without consuming excess capex and fixed cost? | 2025 new molecule revenue CNY 68mn, +224%, but ~2% of total. No profit or capacity utilization disclosed. | new molecule revenue, capex, margin | new molecule revenue, consolidated capex, gross margin | sub-line revenue/profit, capacity utilization, break-even timeline; Investor interaction and new order announcements |
| UQ06 | Does AI4S actually produce company-specific order flow, or only industry-wide narrative? | Private channel checks cite CDMO beneficiaries including Bo Teng, but there is no company-disclosed AI-related order or revenue. | new orders, revenue growth, scenario probability | 2026E-2028E revenue, valuation multiple | company-specific AI-related order value, AI project pipeline; Company order announcements or interim segment disclosure |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业收入 | CNY mn | 3419.83 | 3761.81 | 4138.0 | 4469.0 | 2026E = FY2025 x 1.10 using official H1 +10% midpoint; 2027E = 2026E x 1.10; 2028E = 2027E x 1.08. Analyst demand-growth assumption, not company guidance for 2027-2028. | calculated | 1pp revenue growth = ~CNY 38mn revenue, ~CNY 12mn gross profit at 32% GM; FY2027-2028 company guidance, order backlog |
| small_molecule_api_cdmo | 小分子原料药CDMO营业收入 | CNY mn | 3077.85 | 3385.63 | 3724.2 | 4022.1 | FY2025 = consolidated FY2025 x 90%; forward values = consolidated forecast x 90% holding share constant. Filing says 2025 share ~90%. | calculated | Core segment share change of 1pp shifts revenue by ~CNY 38mn; actual FY2025 segment revenue in CNY, forward segment mix |
| new_modalities | 新分子业务营业收入 | CNY mn | 68.0 | None | None | None | Reported 2025 base only; forward values withheld because sub-line capacity, orders, and 2026H1 segment revenue are not supplied. | missing | small current base; high growth can lift consolidated growth only modestly until scale exceeds ~5% of revenue; 2026 segment revenue, capacity, order book, sub-line mix |
| consolidated | 毛利率 | % | 30.5994 | 32.0 | 33.0 | 33.5 | 2026E base from Q1 actual; forward assumes mix/utilization improvement continues then moderates. Official H1 says GM +~4pp YoY. | analyst_estimate | 1pp GM on CNY 3,762mn revenue = ~CNY 37.6mn gross profit; FY2025 gross margin, product mix, cost per unit |
| consolidated | 营业利润率(剔除一次性减值) | % | 2.6435 | 7.0 | 8.5 | 9.5 | 2026Q1 actual; forward assumes H1 clean operating leverage and scale effects annualize, then gradual improvement. | analyst_estimate | 1pp op margin on CNY 3,762mn = ~CNY 37.6mn operating profit; FY2025 operating profit, segment opex, R&D and admin structure |
| consolidated | 归母净利润(报告) | CNY mn | 96.34 | None | None | None | FY2025 actual; 2026E not set because H1 includes ~CNY 330mn impairment and H2 normalized profit is not disclosed. 2027-2028 require normalized tax/minority/cash assumptions. | missing | CNY 100mn parent profit on CNY 12.15bn market cap = ~12.2x or ~8.2% earnings yield; H2 2026 net profit, minority interest, tax rate, future one-off items |
| consolidated | EPS(摊薄) | CNY/share | None | None | None | None | Parent net profit / diluted share count; blocked because share count is unresolved. | missing | Per-share value scales inversely with share count; diluted share count |
| consolidated | 经营现金流/净利润 | x | 0.0864 | None | None | None | Q1 actual; forward conversion withheld until H1 cash-flow detail arrives. | missing | If OCF/net profit normalizes to 1.0x on CNY 200mn clean profit, OCF adds ~CNY 183mn vs Q1 implied conversion; H1 2026 OCF, working capital movement and collection terms |
| consolidated | 资本支出 | CNY mn | None | None | None | None | Not supplied. Fixed asset evidence shows high historical depreciation; capex cannot be reliably derived without cash paid to acquire/construct long-term assets. | missing | Growth capex consumes OCF and lowers FCF; cash paid to acquire/construct long-term assets, maintenance vs growth capex |
| consolidated | eps |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | fcf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | operating_profit |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | 小分子原料药CDMO | utilization_or_backlog | None  | 162.09400000000002 | None | None | None | bull None->None; base None->None; bear None->None | unverified | model assumption changed through the deterministic financial bridge | 具体新签订单金额及构成, 产能利用率数据, incremental_net_margin_pct |
| KPE02 | 小分子原料药CDMO | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 跟进公司AI制药相关项目合作披露及行业趋势数据 | 公司获得AI相关新签订单的具体情况 |
| KPE03 | 小分子原料药CDMO | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 跟进公司AI相关新签订单的具体情况 | 公司获得AI相关新签订单的具体情况 |
| KPE04 | consolidated | capex_or_roic | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 分析行业资本开支与公司订单的传导路径，跟踪公司产能投入与ROIC变化 | 公司与具体客户的合作项目及金额数据 |
| KPE05 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 评估AI算力需求向医药研发服务传导的机制和时间线 | 公司AI算力相关业务的布局及收入占比 |
| KPE06 | 小分子原料药CDMO | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 跟踪行业产能利用率、新签订单及客户资本开支动态 | 公司国内外产能利用率的具体数据 |
| KPE07 | 小分子原料药CDMO | profit_or_eps | None  | 162.09400000000002 | None | None | None | bull None->None; base None->None; bear None->None | quantified | model assumption changed through the deterministic financial bridge | 剔除减值影响后利润的可持续性, incremental_net_margin_pct |
| KPE08 | 小分子原料药CDMO | utilization_or_backlog | None  | 162.09400000000002 | None | None | None | bull None->None; base None->None; bear None->None | quantified | model assumption changed through the deterministic financial bridge | 具体的在手订单和毛利数据, incremental_net_margin_pct |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 高盛/2026-08-07T17:31 | 高时效/6天 | 未披露 | 涨停板：博腾股份、凯莱英、昭衍新药、普洛药业、泓博医药、百花医药、海正药业、誉衡药业、毕得医药、药康生物、瑞康医药、百普赛斯、哈药股份、近岸蛋白、哈三联、开开实业 其他强势股：皓元医药、美迪西、泽璟制药 PCB 高盛：球AI服务器PCB市场将在2027年达到375亿美元，较此前预测上调38%，2028年进一步增至840亿美元 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 中泰医药祝嘉琦、崔少煜/2026-07-20T09:51 | 有效窗口/24天 | 推荐措辞（非标准评级） | ④博腾股份 发布2026年中报业绩预告，预计上半年剔除斯洛文尼亚研发生产基地终止建设计提减值后归母净利润同比+196%-343% | 未提取到目标价/估值方法与倍数 | rating=推荐措辞（非标准评级） | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 国泰海通/2026-07-15T08:20 | 有效窗口/29天 | 未披露 | 【国泰海通医药】博腾股份二季度... 【国泰海通医药】博腾股份二季度... 【国泰海通医药】博腾股份二季度业绩预告：26H1营收预计同比增长8%~12%，新签订单和收入均实现良好增长 [玫瑰]从26H1来看 [太阳]预计实现营业收入17.50-18.20亿元，同比增长8%~12% / [太阳]预计实现归母净利润-2.50至-2.10亿元（上年同期盈利0.27亿元） / [太阳]预计实现扣非归母净利润-2.70~-2.30亿元（上年同期盈利0.06亿元） | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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