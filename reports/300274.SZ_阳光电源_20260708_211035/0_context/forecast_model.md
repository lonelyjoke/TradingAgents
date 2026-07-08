# Forward Forecast Model Scaffold for 300274.SZ as of 2026-07-08

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 15560645284.03 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 33.2629% / -1.87pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 2.1051% / +2.42pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.5274 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 40.0672% / +4.58pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 44.5972% / +3.67pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Core revenue | category volume x ASP x product/channel mix | category growth, traffic/weather/catering recovery, regional penetration and product mix |
| Gross profit | revenue x gross margin | raw-material and packaging costs, price/mix, promotion intensity and logistics |
| Operating profit | gross profit - selling/admin/R&D expense | sales expense, channel rebates, scale leverage and brand investment |
| Cash profit / FCF | net profit + D&A - working capital - capex | contract liabilities/prepayments, inventory, receivables, OCF/NI and capex |
| Valuation bridge | normalized EPS/FCF x category-appropriate multiple with ROE/payout cross-check | growth durability, channel health, margin stability and shareholder return |

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE03 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | scenario probability | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 15560645284.03 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 33.2629% / -1.87pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 14.7248% / -5.37pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 2.1051% / +2.42pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.5274 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV026 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 9/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / gross_margin_not_reaching_operating_profit: 20251231->20260331: revenue growth -82.55%, gross margin change 1.43pp, operating margi |
| EV031 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026年一季度报告: 2,032,367,774.89 3,676,394,413.73 -44.72% 损益的净利润（元） 经营活动产生的现金流量净额（元） 1,208,404,186.03 1,790,260 |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / gross_margin_not_reaching_operating_profit: 20251231->20260331: revenue growth -82.55%, gross margin change 1.43pp, operating ma... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026年一季度报告: 2,032,367,774.89 3,676,394,413.73 -44.72% 损益的净利润（元） 经营活动产生的现金流量净额（元） 1,208,404,186.03 1,790,... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 其他债权投资 189,029,030.12 187,855,030.13 长期应收款 259,500,000.00 269,000,000.... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 80,128,206.97 36,832,829.23 43,295,377.74 117.55% 益 动所致； ... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 7,129,735,973.85 致； 主要系收到的银行承兑汇票 应收票据 2,513,346,567.63 1,233,619,771.56 1,279,726,796.07 103.74% / receivables: 2026年一季度报告: 主要系收到的银行承... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 公司设立中央研究院，做好前期高价值专利布局和技术难点攻关，为集团产品、技术开发提供高效的平台服务和创新... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 21.6406 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.0113 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Energy Storage Systems | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=Q1 2026; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=30.0%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| PV Inverters | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| SST/AIDC Power | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 258094099635 / current equity value / / / PE TTM / 21.6406 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Assumption Change And Valuation Transmission Ledger
| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |
- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.
- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.

## Shared Company Underwriting Packet
- Research readiness: partial
- Readiness reasons: Missing segment-level revenue and profit splits from filings; all segment models are analytical; Total shares outstanding unknown, preventing EPS and per-share valuation; SST/AIDC business is pre-revenue; all financial estimates are speculative; No Q2 2026 order backlog or delivery schedule available; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: PV Inverters, SST/AIDC Power; Bull/base/bear per-share valuation is incomplete.; Valuation has not closed from mutually exclusive buckets to per-share fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Project delivery (GWh) × Average system price (CNY/Wh) + Inverter shipments (GW) × ASP (CNY/W) + emerging SST/AIDC revenue.
- Profit: Gross profit = Revenue - battery cost - inverter components - installation costs; Operating profit = Gross profit - R&D - SG&A; Net profit after finance cost (interest & FX) and tax.
- Cash flow: OCF = Net profit + depreciation ± working capital changes; Capex for factory and R&D; FCF = OCF - capex.
- Reinvestment: High R&D (¥4.175B in FY2025) and overseas capacity expansion (Poland factory 2027H1). Working capital heavily influenced by contract liabilities (¥122B) and prepayments.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ01 | Can the European ESS market sustain 60% CAGR and deliver high-margin orders through 2028? | Unresolved; channel checks claim 60% 3-year CAGR, but no official filings confirm. Q1 2026 overall revenue declined sharply, creating doubt. | ESS revenue growth rate, ESS gross margin, ESS unit profit (CNY/Wh) | Revenue, Gross margin, Net profit, FCF | Official company guidance on European ESS growth and order book, Q2 2026 delivery data; SunGrow H1 2026 results and any public order announcements |
| UQ02 | Will SunGrow convert its massive contract liabilities (122B CNY) into cash profit with acceptable margin, or will working capital drag and cost overruns erode equity value? | Unresolved; OCF/net profit only 0.53x in Q1 2026, indicating poor cash conversion. | Cash conversion ratio (OCF/net profit), Receivables days, Inventory turns | OCF, FCF, Net profit (if impairments) | Aging of receivables and contract liabilities, Delivery schedule for the 122B contract liabilities; Q2 2026 cash flow statement and management discussion |
| UQ03 | Are US regulatory risks for inverters and storage material enough to impair ~20% revenue exposure, or will safe-harbor provisions and local production (Poland) sufficiently insulate earnings? | Risk probability disputed; company claims products are compliant and safe-harbor extends to 2028H1; Goldman sees risk, CITIC sees low probability. | US revenue weight, US segment margin, Probability of US ban scenario | Revenue, Net profit, EPS | Official FCC rulemaking docket, Quantified impact under worst-case ban; FCC/FERC announcements and company's product certification updates |
| UQ04 | What is the realistic revenue and profit contribution from AIDC storage and SST power beyond 2027, and can SunGrow's first-mover advantage translate into durable moats and high ROIC? | Speculative; SST product launch imminent but no orders yet. AIDC storage has small orders (hundreds of MWh) but no large-scale contracts. | SST revenue (CNY mn) from 2027, AIDC storage GWh and margin | Revenue, Gross margin, Terminal value / PER | Customer pipeline size, First commercial orders and pricing; July 9 SST launch and subsequent H2 2026 order announcements |
| UQ05 | Can the solar inverter business maintain profitability while facing severe pricing pressure and a potential US ban, or will it become a drag on consolidated returns? | Margins likely under pressure; no separate disclosure. US risk overhang. | Inverter segment margin, Inverter US revenue exposure | Segment profit, Consolidated net profit | Inverter segment profitability and shipments; H1 2026 segment reporting or management commentary on inverter trends |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 89184.0 | 80000.0 | 100000.0 | 115000.0 | Base assumption: FY2026 -10% decline due to weak Q1, recovery in H2 from ESS deliveries; FY2027 +25% driven by European ESS 60% growth and AIDC initial ramp; FY2028 +15% continued growth. | analyst_estimate | European ESS demand realization and AIDC order conversion; Segment revenue breakdown, Q2 2026 revenue run-rate |
| consolidated | Gross Margin | % | 31.83 | 31.5 | 32.0 | 32.5 | Q1 2026 gross margin 33.26%, but full-year pressure from mix and tariffs. Assumes gradual improvement as higher-margin European ESS share increases. | analyst_estimate | Regional mix and battery cost pass-through; Segment-level gross margins |
| consolidated | Operating Margin | % | 17.5 | 14.0 | 16.0 | 18.0 | FY2025 estimated from net profit and finance cost; Q1 2026 17.1% but full-year weak top-line leverage. Gradual recovery as revenue scale improves. | analyst_estimate | Revenue growth and R&D efficiency; Exact FY2025 operating profit, R&D and SG&A growth rate |
| consolidated | Parent Net Profit | CNY mn | 13461.0 | 11000.0 | 14500.0 | 17500.0 | Net profit = Revenue * Operating Margin * (1 - tax rate) adjusted for finance costs. Tax rate assumed 15%. | analyst_estimate | Operating leverage and finance costs; Effective tax rate, Finance expense/income split |
| consolidated | EPS | CNY per share | None | None | None | None | Parent net profit / diluted share count | missing | Share count unknown; Diluted share count |
| consolidated | Operating Cash Flow | CNY mn | 16918.0 | 9000.0 | 12000.0 | 15000.0 | Assumes OCF/net profit ratio improves from 0.52x in Q1 2026 to 0.82x by 2028 as working capital normalizes. | analyst_estimate | Receivables collection and inventory turnover; Q2 2026 cash flow data |
| consolidated | Capex | CNY mn | None | 4000.0 | 4500.0 | 4500.0 | Estimated for Poland factory completion, R&D equipment. FY2025 figure not available in evidence. | analyst_estimate | Capacity expansion needs; FY2025 capex actual, Capital expenditure guidance |
| consolidated | Free Cash Flow | CNY mn | None | 5000.0 | 7500.0 | 10500.0 | OCF - Capex | calculated | Both OCF and capex assumptions; FY2025 FCF |
| Energy Storage Systems | Shipments | GWh | None | None | None | None | No disclosed baseline; KPE suggests 2027E 80GWh in bull scenario | missing | Volume drives ESS revenue; Historical ESS shipments, Order book conversion rate |
| Energy Storage Systems | Unit Profit | CNY/Wh | 0.11 | 0.1 | 0.12 | 0.13 | Assumes slight improvement as battery costs stabilize and higher-margin regions grow | analyst_estimate | Battery procurement cost and regional mix; Q2 2026 unit profit |
| consolidated | operating_profit |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | scenario_probability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Cross-check with official FCC/FERC filings and Q2 2026 earnings call | Probability weights for bull/base/bear scenarios under US ban vs no-ban |
| KPE02 | consolidated | scenario_probability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Cross-check with official FCC/FERC filings and Q2 2026 earnings call | Probability weights for bull/base/bear scenarios under US ban vs no-ban |
| KPE03 | Energy Storage Systems | segment_volume_growth_cagr | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Requires revenue/volume breakdown from filings or company IR; compare with analyst forecasts | Baseline CAGR, Absolute GWh numbers, Revenue base for Europe |
| KPE04 | Energy Storage Systems | segment_volume_growth_1year | 15.0 % | None | None | None | None | bull None->None; base None->None; bear None->None | assumption_quantified_financial_bridge_missing | unchanged/watch: no model assumption or scenario probability change until Check company's public growth guidance (if any) and subsequent order intake | Baseline absolute value, Unit for growth (volume or revenue), Europe-specific revenue base |
| KPE05 | Energy Storage Systems | unit_profit | None yuan/Wh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Verify with Q1 2026 financials or earnings call transcript; reconcile with reported gross margin | Prior quarter unit profit, Revenue mix contribution |
| KPE06 | Energy Storage Systems | demand_visibility_aidc | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Track concrete AIDC storage order announcements and FERC regulatory updates | Size of addressable AIDC storage market for SunGrow, Competitive position vs. peers |
| KPE07 | PV Inverters | scenario_probability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Monitor FCC rulemaking docket and any public comments from SunGrow | Probability distribution for ban scenarios, Quantified revenue/margin impact under worst case |
| KPE08 | Energy Storage Systems | bidding_volume_gwh | None GWh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Cross-check with CNESA monthly report and company backlog reporting | SunGrow's conversion rate from bidding to orders, Revenue lag from bidding to recognition |
| KPE09 | SST/AIDC Power | siC_supply_availability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Assess SiC wafer and device availability from supplier checks (e.g., Wolfspeed, II-VI) | SunGrow's SiC sourcing contracts, SiC cost impact on SST margin |
| KPE10 | SST/AIDC Power | siC_supply_availability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Cross-check with SiC industry data and SunGrow's SST supply chain | SunGrow's specific SiC procurement, Cost pass-through ability |
| KPE11 | SST/AIDC Power | supply_chain_bottleneck | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Monitor SiC pricing and availability; check SunGrow's SST production timeline | SunGrow's SST bill of materials, SiC content per unit |
| KPE12 | Energy Storage Systems | demand_visibility_na | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Track PJM capacity auction results and SunGrow's U.S. order announcements | U.S. revenue exposure quantification, Competitive win rate against Fluence/Tesla |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-01T18:03 | 高时效/7天 | 未披露 | 另外即使是去年已经落地的OBBA法案，也预留了较长的缓冲期，目前公司在美国直到28H1的项目都已进入“安全港”，不受政策影响，后续即使有新政策落地，预计也影响有限 / 欧洲储能订单上修： 近期欧洲光储展会斩获较多订单，预计明年欧洲储能增速由40-50%上修至60%，且波兰产能明年上半年建成，进一步加强本地化服务能力 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-01T18:03 | 高时效/7天 | 未披露 | 公司波兰工厂预计2027H1建成投产，主要满足欧洲本地化需求，助力获取更多本地订单 / 美国市场 • 美国本土逆变器品牌市场份额仅10%左右，构建完善的本土逆变器产业链预计需要5年时间，且存在建设周期长、成本高、供应链配套不足、功率半导体/MLCC等元器件短缺等难点 / • AIDC配储：数据中心配储趋势明确，未来将逐步成为标配，预计2026年下半年订单逐步增多，2027、2028年需求持续上量，欧洲、东南亚等地区的数据中心也有配储需求 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 中信建投/2026-07-01T11:12 | 高时效/7天 | 未披露 | 未提取到带期间的明确盈利预测 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 机构未识别/2026-06-26T10:33 | 有效窗口/12天 | 未披露 | 阳光电源：已成功研制出35k... 阳光电源：已成功研制出35k... 阳光电源：已成功研制出35kV直降800V的6MVA的SST，进度领先全行业，完全简化整体配电架构，实现降维打击！预计2030年50GW2000亿市场，若获30%份额可贡献 超150亿元利润增量，给予20倍可再造一个阳光！ 同时，在海外大单支撑下，其储能毛利率已回升至约30%且量价稳固 / 保守预计明年公司主业利润将达180亿元（光伏50亿+储能120亿+其他10亿），按20倍PE测算，主业安全边际市值为3600亿元 | 保守预计明年公司主业利润将达180亿元（光伏50亿+储能120亿+其他10亿），按20倍PE测算，主业安全边际市值为3600亿元 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI05 | 中信建投/2026-06-22T13:51 | 有效窗口/16天 | 未披露 | 同时美国订单去年Q4已回复，下半年交付起量，预计对盈利能力形成明显支撑，IEEPA关税退还、碳酸锂跌价，也将助力业绩修复 | ➡投资建议： 主业：保守给予明年主业180亿（光伏50亿+储能120亿+其他10亿），储能120亿=明年出货80GWh×单位盈利0.15元/Wh，估值20X给予3600亿主业市值 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.
- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.