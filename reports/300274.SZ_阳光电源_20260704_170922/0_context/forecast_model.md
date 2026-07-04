# Forward Forecast Model Scaffold for 300274.SZ as of 2026-07-04

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

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | scenario probability before->after or watch/reject |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | scenario probability before->after or watch/reject |
| KPE05 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | 政策原文、执行细则、受益范围、时间表、预算/补贴落地 | model conflict result and accepted/rejected reason |
| KPE06 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | 政策原文、执行细则、受益范围、时间表、预算/补贴落地 | model conflict result and accepted/rejected reason |
| KPE07 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
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
| consolidated | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=20260331; reported revenue=15560645284.03 (CNY); revenue weight=None%; growth=None%; gross margin=33.2629%; margin change=-1.87pp; source=earnings_model; mode=llm_semantic |
| energy_storage | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=20260331; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=30.0%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| hydrogen | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
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
- Readiness reasons: Segment revenue breakdown (PV/wind inverters, energy storage, hydrogen) not disclosed in filings; only consolidated revenue and margin available.; Diluted share count could not be determined from supplied evidence (no total_share, market price, or EPS with share count). Fair value per share and EPS cannot be calculated.; Key operating metrics missing: storage GWh shipments, utilization rates, order backlog by segment, capex for 2025/2026, working-capital detail by segment.; Hydrogen segment has qualitative direction only; no revenue, margin, or capacity data.; Net profit YoY decline of -40% (peer comparison) conflicts with management narrative of brand premium and scale advantage; resolution requires breakdown of cost/expense increases.; Material segment three-year driver lines are missing: energy_storage, hydrogen; Bull/base/bear per-share valuation is incomplete.; Valuation buckets contain potential double counting.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ (shipment volume × ASP) + system integration project revenue. Volume depends on global solar/wind/storage installations and market share. ASP is under pressure from competition and regional mix shifts.
- Profit: Gross profit = revenue - raw material & component costs. Operating profit = gross profit - R&D (41.75 bn in FY2025, ~4.7% of revenue) - selling expenses (48.32 bn, ~5.4%) - G&A. Net margin is further hit by finance expense and tax.
- Cash flow: OCF = net profit + depreciation ± working capital. Receivables/revenue at 40.1% and inventory/revenue at 44.6% (Q1 2026 annualized) indicate heavy cash absorption. OCF/net profit = 0.53 in Q1 2026.
- Reinvestment: R&D dominates reinvestment (31.97% YoY growth in FY2025). Capex for manufacturing capacity expansion is ongoing but not separately quantified. ROIC is likely under pressure as margins decline and capital employed grows.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 储能系统毛利率能否维持在30%以上？若碳酸锂涨价且竞争加剧，是否被迫牺牲价格抢份额？ | Q1 2026毛利率约30%，环比改善因高毛利欧洲区占比提升。管理层称通过技术降本和增值服务维持利润空间。但缺乏份额与价格定量信息。 | energy_storage gross margin, energy_storage shipment volume growth, energy_storage ASP | consolidated revenue, consolidated gross profit, consolidated net profit | 储能板块季度价格与量级, 特朗普关税下美国实际订单损失, 碳酸锂价格预测; 2026年二季度及半年报将揭示毛利率趋势和出货量变化。 |
| Q2 | 合同负债22bn及预付款4bn是否能在2026年顺利转化为收入，且毛利率如何？ | 合同负债12.2亿，预付款项4亿；公司未给出指引。前期订单可能已在Q4或Q1交付，但Q1收入环比下滑，暗示转化节奏不及预期或需求前置。 | consolidated revenue, contract liabilities conversion | consolidated revenue, consolidated OCF, consolidated net profit | 合同负债所对应项目的毛利率和交付时间表; 2026年二季度和三季度报告将反映交付进度及收入确认；管理层交流会可能给出全年指引。 |
| Q3 | 逆变器产品线是否能保持或提升市场份额，且毛利率止跌？ | 逆变器收入与毛利率未单独披露；公司声称有品牌溢价和技术优势。但Q1综合毛利率同比下滑，暗示逆变器毛利率可能也在承压。 | pv_wind revenue, pv_wind gross margin, global PV installations | consolidated revenue, consolidated gross profit | 逆变器出货量及ASP, 竞争对手定价; 2026年报披露分部收入或行业出货量数据。 |
| Q4 | 氢能业务何时能产生实质性的收入贡献？需要多少前期投入？ | 公司表示氢能订单良好，但无任何定量数据。处于早期，收入占比极小。 | hydrogen revenue, hydrogen margin | hydrogen revenue, consolidated capex | 氢能项目合同额, 产能规划; 重大合同公告或中报首次披露氢能收入。 |
| Q5 | 营运资本（应收/存货/预付款）的高水位是否会触发减值或现金流危机？ | 应收/收入40.1%，存货/收入44.6%，同比均升。预付款激增201%备料。现金转换率低至0.53。未出现明显的减值，但需监测。 | receivables/revenue, inventory/revenue, OCF/net profit | consolidated OCF, consolidated net profit (via impairment) | 账龄分析, 客户集中度; 2026年中报资产减值测试及经营活动现金流量表。 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | revenue | CNY mn | 89184.357 | 85500.0 | 89775.0 | 94264.0 | Base year FY2025 revenue, 2026E ~ -4.1% (weighted by Q1 run-rate and tariff headwinds), 2027E +5%, 2028E +5%. | analyst_estimate | Assumes global installations remain supportive, no major market share loss, but US tariff and pre-ordering weigh on 2026.;  |
| consolidated | gross_margin | % | 31.83 | 31.5 | 31.8 | 32.0 | Reflects Q1 2026 margin of 33.26% annualizing but offset by expected further ASP pressure and mix normalization, stabilizing after. | analyst_estimate | Every 1pp change in gross margin impacts parent net profit by ~850 mn CNY.;  |
| consolidated | operating_profit | CNY mn | None | None | None | None | Operating profit = gross profit - operating expenses. Operating expenses not disclosed for FY2025; unable to estimate reliably. | missing | ; FY2025 operating expense split, Q1 2026 total operating expenses |
| consolidated | parent_net_profit | CNY mn | 13461.28 | 10350.0 | 11250.0 | 11980.0 | Assume 2026E net profit decline ~23% (mirroring H2 2025 + Q1 run-rate), followed by moderate recovery. | analyst_estimate | Driven by revenue, gross margin, and expense control; uncertain.;  |
| consolidated | eps | CNY | None | None | None | None | EPS = parent net profit / diluted shares. Share count unresolved. | missing | ; diluted_share_count_mn |
| consolidated | ocf | CNY mn | 16918.0 | 9000.0 | 10000.0 | 10500.0 | OCF/net profit ratio assumed gradually improving from 0.53 towards 0.8 as working capital normalizes. 2026E OCF ~0.55 × 10350 = 5692 mn, rounded up for cautious recovery. | analyst_estimate | Working-capital cycle is key; receivables/contract liabilities release could boost OCF.;  |
| consolidated | capex | CNY mn | None | None | None | None | No capex figure available (cash paid to acquire fixed assets not extracted). | missing | ; 2025 capex, 2026E capex guidance |
| consolidated | fcf | CNY mn | None | None | None | None | FCF = OCF - capex; both inputs missing or incomplete. | missing | ; capex |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | baseline utilization rate, baseline backlog, probability distributions |
| KPE02 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | baseline utilization rate, baseline backlog, probability distributions |
| KPE03 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | baseline utilization rate, baseline backlog, probability distributions |
| KPE04 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | baseline utilization rate, baseline backlog, probability distributions |
| KPE05 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 政策原文、执行细则、受益范围、时间表、预算/补贴落地 | policy details, impact quantification |
| KPE06 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 政策原文、执行细则、受益范围、时间表、预算/补贴落地 | policy details, impact quantification |
| KPE07 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific content, quantified impact |
| KPE08 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific content, quantified impact |
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
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.
- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.