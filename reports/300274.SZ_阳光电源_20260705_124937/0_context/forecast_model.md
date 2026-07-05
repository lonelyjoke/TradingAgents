# Forward Forecast Model Scaffold for 300274.SZ as of 2026-07-05

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
| Cathode / material revenue | shipment volume x cathode ASP | LFP/ternary demand, customer order cadence, pass-through clauses |
| Manufacturing spread | cathode ASP - lithium carbonate / precursor / energy / processing cost | raw-material price, inventory-cost lag, processing fee |
| Gross profit | shipment volume x unit spread | capacity utilization, yield, depreciation, product mix |
| Operating profit | gross profit - R&D - SG&A - credit impairment | customer concentration, receivables, scale leverage |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | OCF/NI, inventory, capex, expansion cycle |

## Battery Forecast And Valuation Controls
| control | Mandatory treatment |
| --- | --- |
| Segment model | model power battery, energy storage, materials/recycling, and other businesses separately |
| Revenue bridge | GWh shipments x realized ASP by segment; reconcile mix and consolidation eliminations |
| Margin bridge | ASP/pass-through - lithium/material cost - manufacturing/depreciation/warranty; show utilization sensitivity |
| Earnings bridge | segment gross profit - R&D/SG&A/finance - tax/minority/non-recurring = parent net profit/EPS |
| Cash bridge | net profit + D&A - working capital - capex = FCF; reconcile OCF/NI and capacity expansion |
| Scenario discipline | show bear/base/bull shipment, ASP, utilization, gross margin, EPS, FCF, and valuation multiple |
| Valuation monotonicity | a deterioration case must not receive a higher multiple than base without an explicit, evidence-backed reason |
| Probability audit | record scenario probabilities before and after each private/proxy clue; unexplained probability changes are invalid |
- Missing shipment, ASP, utilization, or segment-margin evidence must remain a neutral explicit model gap; narrative strength cannot fill a numeric cell, and the gap must not mechanically alter the rating.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE04 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | scenario probability | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
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
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 21.9309 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.0517 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Photovoltaic (PV) Inverters | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年度; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| Energy Storage Systems (ESS) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=30.0%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| Wind Power Converters | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| Hydrogen Electrolyzers | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026-05-13; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| AIDC Energy Storage | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| AIDC Power (SST) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 261556362840 / current equity value / / / PE TTM / 21.9309 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: Segments lack reported revenue/volume/margin breakdown; segment economics rely on analytical mapping.; Diluted share count cannot be confirmed from supplied evidence (no close price or total_share from Tushare).; AIDC energy storage and SST are in early commercialization with only private proxy evidence; forward revenue/profit assumptions are unverified.; Forward growth heavily depends on energy storage volume, unit profit, and policy outcomes, all requiring mid-year updates.; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: AIDC Energy Storage, AIDC Power (SST), Energy Storage Systems (ESS), Hydrogen Electrolyzers, Photovoltaic (PV) Inverters, Wind Power Converters; Bull/base/bear per-share valuation is incomplete.; Valuation has not closed from mutually exclusive buckets to per-share fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Consolidated Revenue = sum(segment volume × segment ASP + system integration/service fees). Key segments are PV inverters (volume x ASP), ESS (shipment GWh x ASP per GWh), and emerging AIDC products.
- Profit: Gross Profit = Revenue - COGS (raw materials, manufacturing, tariffs). Operating Profit = Gross Profit - R&D - SG&A. Net profit parent = Operating Profit - Finance costs - Tax. R&D spend ~5% of revenue.
- Cash flow: OCF = Net profit + D&A - change in working capital (receivables, inventory, prepayments). FCF = OCF - Capex (manufacturing capacity, R&D infrastructure).
- Reinvestment: Moderately capital-light asset profile; main reinvestment is R&D (41.75 B CNY in FY2025) and global manufacturing/service network. Capex typically 3-5% of revenue.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ01 | What is the trajectory of ESS shipment volume and unit profitability (CNY/Wh) over 2026-2028? | Q1 2026 shipments flat YoY; unit profit 0.11 CNY/Wh. Sell-side expects 2027E 80GWh at 0.15 CNY/Wh, but competitive dynamics may compress margin. | ESS shipment volume GWh, ESS unit profit CNY/Wh (or gross margin %), Revenue contribution from AIDC storage | Consolidated revenue, Gross profit / operating profit, EPS, FCF | Monthly/quarterly shipment track record, Breakdown of backlog by region and margin profile; Q2 2026 quarterly disclosure and management commentary on shipments and margins |
| UQ02 | Do US trade policy actions (FCC inverter rule, IRA adjustments, tariff escalation) materially reduce Sunpower's US revenue or margins? | Company claims compliance (no remote communication) and existing projects in 'safe harbor' through 2028H1. FCC rule probability low, but uncertainty persists. | US ESS inverter revenue share, Probability of FCC/ITA restrictions and loss of market | US segment revenue, US segment margin, Group EPS | Official FCC or Department of Energy timeline/scope, Exact US revenue and profit breakdown from audited filings; FCC public docket or formal announcement on inverter rules |
| UQ03 | Can the company sustain gross margin above 28% in the face of lithium price volatility and intense competition? | Q1 2026 gross margin 33.3% but includes high-margin Europe mix. Sell-side expects ~27% in neutral scenario because of lithium cost pressure. | ESS gross margin %, Lithium carbonate price outlook, Mix of high-margin vs low-margin orders | Consolidated gross margin, Operating profit, Net profit | Forward lithium cost hedges or long-term supply contracts, Unit cost breakdown and sensitivity; Q2 and Q3 2026 margin commentary and industry lithium price data |
| UQ04 | Will European demand acceleration (60% CAGR) translate into profitable market share gains for Sunpower? | The company reports strong order intake at recent exhibitions; Poland factory (2027H1) to strengthen local presence. However, EU financing restrictions may cap addressable pool. | European ESS volume growth %, European gross margin, Service and local cost advantage | European segment revenue, Blended group margin, Operating cash flow | Quantified European revenue & profit, Poland factory capacity and ramp timeline; H1 2026 order book release or European industry shipment data |
| UQ05 | What is the realistic revenue and profit contribution from AIDC storage and SST by 2028? | AIDC storage: orders of hundreds of MWh, expect meaningful revenue from H2 2026. SST: first commercial product launched in July 2026, revenue likely 2028+. Both carry high technical barriers. | AIDC storage backlog GWh and likely revenue timing, SST order pipeline and launch month customer traction | New business revenue & profit, Group valuation multiple | Signed multi-year AIDC storage contracts, SST pilot project list and expected revenue per unit; H2 2026 AIDC order announcements and SST customer test results |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 92587.0 | 92587.0 | 110000.0 | 130000.0 | 2026E = Q1 2026 seasonally-adjusted annualized (median share 17.5%); 2027E-2028E based on ESS volume growth and stable PV inverter | base_assumption | 1% revenue change ≈ 0.9B operating profit; segment revenue split, actual Q1 2025 base, actual segment cost structures |
| consolidated | Gross Profit | CNY mn | 28389.0 | 30815.0 | 37620.0 | 45500.0 | Revenue - COGS | base_assumption | see COGS;  |
| consolidated | SG&A and R&D | CNY mn | None | None | None | None | ( | missing | ;  |
| consolidated | Operating Profit (EBIT) | CNY mn | 15700.0 | 15800.0 | 21500.0 | 27000.0 | 2026E: Q1 op margin 17.1% applied to 92.6B revenue -> 15800; 2027E: op margin 19.5% on 110B -> 21450; 2028E: 20.8% on 130B -> 27040. | base_assumption | 1pp move in op margin = ~900mn;  |
| consolidated | Net Profit (Parent) | CNY mn | 13461.0 | 13500.0 | 18500.0 | 23500.0 | 2026E: derived from implied TTM earnings ~11.9B but seasonality-adjusted 13.1B from Q1; 2027E and 2028E from sell-side and demand scenarios; 2026E net margin 14.6% on 92.6B = ~13500. | base_assumption | net profit drives EPS/FCF; 10% change = ~1.8B;  |
| consolidated | EPS (Parent) | CNY per share | None | None | None | None | EPS = Net Profit / Diluted Shares; share count unresolved | missing | ; diluted share count |
| consolidated | Operating Cash Flow | CNY mn | 16918.0 | 10800.0 | 14800.0 | 18800.0 | 2026E: assume OCF/Net Profit ratio improves from Q1 0.53 to 0.80 due to working-capital normalization, thus 13500*0.8=10800; 2027E 18500*0.8=14800; 2028E 23500*0.8=18800 | analytical | OCF quality impacts DCF and dividend capacity; historical OCF ratio |
| consolidated | Capex | CNY mn | 0.0 | 4000.0 | 5000.0 | 6000.0 | assumed ~4-5% of revenue for manufacturing and R&D capex; FY2025 data missing | analytical | ; FY2025 actual capex from cash flow statement |
| consolidated | Free Cash Flow | CNY mn | None | 6800.0 | 9800.0 | 12800.0 | FCF = OCF - Capex | analytical | ; FY2025 capex and OCF |
| consolidated | eps |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | gross_margin |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | scenario_probability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | audio content not extracted, quantified before/after probabilities |
| KPE02 | AIDC Power (SST) | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | order pipeline, SST revenue forecast |
| KPE03 | Energy Storage Systems (ESS) | segment_margin | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline margin assumption, margin sensitivity |
| KPE04 | Energy Storage Systems (ESS) | segment_volume | None % CAGR | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline CAGR, absolute volume base |
| KPE05 | Energy Storage Systems (ESS) | segment_volume | 15.0 % YoY growth | None | None | None | None | bull None->None; base None->None; bear None->None | assumption_quantified_financial_bridge_missing | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | revenue base for European storage, share count |
| KPE06 | Energy Storage Systems (ESS) | segment_margin | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline margin, lithium price assumption |
| KPE07 | AIDC Energy Storage | segment_volume | None GWh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | company market share assumption, revenue per GWh |
| KPE08 | consolidated | scenario_probability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | quantified probability before/after, revenue exposure breakdown |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-01T18:03 | 高时效/4天 | 未披露 | 另外即使是去年已经落地的OBBA法案，也预留了较长的缓冲期，目前公司在美国直到28H1的项目都已进入“安全港”，不受政策影响，后续即使有新政策落地，预计也影响有限 / 欧洲储能订单上修： 近期欧洲光储展会斩获较多订单，预计明年欧洲储能增速由40-50%上修至60%，且波兰产能明年上半年建成，进一步加强本地化服务能力 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-01T18:03 | 高时效/4天 | 未披露 | 公司波兰工厂预计2027H1建成投产，主要满足欧洲本地化需求，助力获取更多本地订单 / 美国市场 • 美国本土逆变器品牌市场份额仅10%左右，构建完善的本土逆变器产业链预计需要5年时间，且存在建设周期长、成本高、供应链配套不足、功率半导体/MLCC等元器件短缺等难点 / • AIDC配储：数据中心配储趋势明确，未来将逐步成为标配，预计2026年下半年订单逐步增多，2027、2028年需求持续上量，欧洲、东南亚等地区的数据中心也有配储需求 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 中信建投/2026-07-01T11:12 | 高时效/4天 | 未披露 | 未提取到带期间的明确盈利预测 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 机构未识别/2026-06-29T08:05 | 高时效/6天 | 未披露 | d.电容（Q3预计高斜率） 通胀链： 1.存储：大普微、德明利、佰维存储、香农、海外原厂等 2.PCB上游：凌玮科技、德福科技、圣泉集团、世名科技、 宏和科技、联瑞新材、 东材科技、呈和科技、同宇新材、瑞丰高材、东岳集团、容大感光，CCL：华正新材、宝鼎科技（联系岚琪） 3.光上游&OCS：唯科科技、海泰新光 4.算力租赁：协创数据、盈峰环境、利通电子等（联系思琪） 5.电容：江海股份、嘉德利、昀冢科技、王子新材、三环风华等 0～1产业链 液冷&电源&玻璃基板： 电源：京泉华、海伦哲（3x阳光电源） 液冷（1... | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI05 | 机构未识别/2026-06-26T10:33 | 有效窗口/9天 | 未披露 | 阳光电源：已成功研制出35k... 阳光电源：已成功研制出35k... author: 纪要小能手 阳光电源：已成功研制出35kV直降800V的6MVA的SST，进度领先全行业，完全简化整体配电架构，实现降维打击！预计2030年50GW2000亿市场，若获30%份额可贡献 超150亿元利润增量，给予20倍可再造一个阳光！ 同时，在海外大单支撑下，其储能毛利率已回升至约30%且量价稳固 / 保守预计明年公司主业利润将达180亿元（光伏50亿+储能120亿+其他10亿），按20倍PE测算，主业安全边际市值为3600亿元 | 保守预计明年公司主业利润将达180亿元（光伏50亿+储能120亿+其他10亿），按20倍PE测算，主业安全边际市值为3600亿元 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI06 | 中信建投/2026-06-22T13:51 | 有效窗口/13天 | 未披露 | 同时美国订单去年Q4已回复，下半年交付起量，预计对盈利能力形成明显支撑，IEEPA关税退还、碳酸锂跌价，也将助力业绩修复 | ➡投资建议： 主业：保守给予明年主业180亿（光伏50亿+储能120亿+其他10亿），储能120亿=明年出货80GWh×单位盈利0.15元/Wh，估值20X给予3600亿主业市值 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI07 | 机构未识别/2026-06-15T08:46 | 有效窗口/20天 | 推荐措辞（非标准评级） | 海外储能集成壁垒高（本地化服务、快速交付、产品可靠性、认证等），公司长期竞争力转化为盈利优势，我们预计中长期储能毛利率维持25%-30% / 礼物预计2026-2027年归母净利润135、190亿元，对应PE 23、16倍，继续重点推荐！ | 礼物预计2026-2027年归母净利润135、190亿元，对应PE 23、16倍，继续重点推荐！ | 2026E_归母净利润=135；rating=推荐措辞（非标准评级） | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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