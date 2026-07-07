# Forward Forecast Model Scaffold for 000528.SZ as of 2026-07-07

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 10060797784.83 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 21.3094% / -0.70pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.9119% / +2.15pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / -0.9047 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 35.8449% / -1.08pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 24.8202% / -0.23pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
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
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE03 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE04 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 10060797784.83 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 21.3094% / -0.70pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 6.024% / -1.16pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.9119% / +2.15pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / -0.9047 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -69.65%, gross margin change N/A, operating margin change 1.95pp, OCF/n |
| EV031 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / contract_liabilities: 2026年一季度报告: 短期借款 7,534,350,347.67 5,704,135,919.25 32.09% 主要是本期借款增加 衍生金融负债 10,636,778.62 94,203.78 11191.2 |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -69.65%, gross margin change N/A, operating margin change 1.95pp, OC... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / contract_liabilities: 2026年一季度报告: 短期借款 7,534,350,347.67 5,704,135,919.25 32.09% 主要是本期借款增加 衍生金融负债 10,636,778.62 94,203.78 1119... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 其他债权投资 - - 长期应收款 3,541,141,353.35 3,347,480,425.94 长期股权投资 945,305,768.... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: -12,746,217.46 8,394,208.52 “－”号填列） 信用减值损失（损失以“-” / impai... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / contract_liabilities: 2026年一季度报告: 短期借款 7,534,350,347.67 5,704,135,919.25 32.09% 主要是本期借款增加 衍生金融负债 10,636,778.62 94,203.78 11191.24% 主要是本期衍生金融工具公允价值变动 合同负债 744,... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 1.工程机械行业特征 工程机械作为国民经济发展的战略性支柱产业，广泛应用于建筑、矿山、水利、电力、 铁... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade partial; reports seen annual/quarterly/semiannual; answered 9/9; core pack thin. Readable filings exist, but either ... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 10.8137 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 0.4947 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 工程机械 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年度; reported revenue=30060542545.88 (元); revenue weight=90.7%; growth=11.25%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 预应力业务 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年度; reported revenue=2523433700.3 (元); revenue weight=7.61%; growth=0.24%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 租赁业务 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年度; reported revenue=559901998.19 (元); revenue weight=1.69%; growth=None%; gross margin=36.96%; margin change=-2.29pp; source=company_business_model; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 16848671961 / current equity value / / / PE TTM / 10.8137 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: diluted share count not reported and cannot be deterministically derived from provided evidence; EPS, FCF per share, and valuation per share depend on downstream share-count resolution; segment-level gross profit, operating profit, and detailed volume/ASP/mix data not disclosed; profitability assumptions are estimated from consolidated drivers; commodity and input-cost evidence is not mapped; margin sensitivity to steel, components, and energy remains unverified; industry cycle evidence is labelled as insufficient; cycle stage classification relies on external KPE sentiment rather than hard supply/demand/price data; One or more filing-reported segments required deterministic restoration.; Material segment three-year driver lines are missing: 工程机械; Bull/base/bear per-share valuation is incomplete.; Valuation has not closed from mutually exclusive buckets to per-share fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ (Equipment shipments_i × ASP_i) + Parts & service + Prestress product sales + Rental income
- Profit: Gross profit = Revenue - Raw materials - Direct labor - Manufacturing overhead - Equipment depreciation; Operating profit = Gross profit - Selling expenses - G&A - R&D; Net profit = Operating profit - Net finance costs - Tax - Minority interests
- Cash flow: OCF = Net profit + Depreciation ± Working capital (receivables, inventory, payables, contract liabilities); FCF = OCF - Capex. The company carries significant receivables from dealer floor and credit sales, and inventory cycles are long for large machinery.
- Reinvestment: Asset-heavy manufacturing with capacity expansion, overseas production bases, and R&D for electrification. Capex tends to be 3-5% of revenue but can increase during new plant construction. Working capital absorbs cash during upcycles when receivables and inventory build.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | What is the sustainable net profit margin for the core construction machinery segment after factoring in price hikes, input cost trends, and forex normalization? | Q1 2026 consolidated operating margin was 6.97% (-1.74pp YoY), dragged by forex. Managerial guidance and sell-side channel checks suggest margin improvement in H2 2026 as price hikes take effect and forex headwinds ease, but quantification is absent. | engineering machinery gross margin, finance-expense ratio, operating expense ratio, tax rate | consolidated operating profit, parent net profit, EPS, FCF | Segment-level gross margin and operating margin for construction machinery, Quantified forex exposure and impact on profit, Historical normalized operating margin range; H1 2026 report: consolidated and segment gross/operating margins, forex gain/loss detail, management discussion of price-hike realization. |
| Q2 | Is the domestic construction machinery replacement cycle strong enough to offset potential overseas demand deceleration and geopolitical risks? | May 2026 excavator domestic sales +39% YoY (KPE02) signals strong replacement demand. However, the cycle's sustainability beyond 2026 is uncertain; policy support is favorable but hard evidence of multi-year demand is thin. | domestic construction machinery revenue growth, export construction machinery revenue growth | consolidated revenue, operating profit, working capital (receivables) | Industry-level construction machinery demand forecast for 2027-2028, Monthly sales data beyond May 2026, Company order backlog and contract liabilities trend; Monthly excavator sales data from CCMA; H1 2026 revenue breakdown and management's full-year guidance. |
| Q3 | What will be the normalized free cash flow generation and return on invested capital, given elevated working capital and ongoing capex requirements? | Q1 2026 OCF/net profit was -0.90, indicating heavy working capital consumption. Full-year conversion typically improves, but the company has historically high receivables and inventory ratios. Capex is ongoing for overseas expansion. Historical FCF yield is low. | receivables/revenue ratio, inventory/revenue ratio, OCF/net profit ratio, capex/revenue ratio | OCF, FCF, net debt | Full-year OCF and capex for 2025, Clear capital allocation framework, Asset quality details (aged receivables, inventory write-down risk); 2025 annual report cash flow statement; H1 2026 cash flow metrics. |
| Q4 | How much further can the overseas revenue mix shift and will it sustainably lift the consolidated gross margin toward the overseas segment's 29.7% level? | Overseas revenue grew 14.78% in 2025, and management targets >60% overseas share by 2030 (EV024). If achieved, the mix effect is meaningful, but execution risk (geopolitics, local competition, FX) and margin sustainability in newer regions remain unproven. | overseas revenue share, overseas segment gross margin, domestic segment gross margin | consolidated gross margin, consolidated operating profit | Country-level mix and margin breakdown, FX hedging strategy and cost, Competitive landscape in key overseas markets; H1 2026 geographic revenue and margin disclosure; management updates on 2030 target progress. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 工程机械行业 | revenue | CNY mn | 30060.54 | 33700.0 | 36800.0 | 39800.0 | Base revenue × (1 + volume growth + price/mix effect). 2026E growth reflects ~8% domestic volume (+ replacement) + ~17% overseas volume and plus ~2% price hike contribution, resulting in ~12% growth; 2027E/2028E decelerate to ~9% and ~8%. | estimated | Sensitive to domestic infrastructure spending and overseas project sanctions.; Product-wise volume and ASP data |
| 预应力业务 | revenue | CNY mn | 2523.43 | 2600.0 | 2680.0 | 2760.0 | Base revenue × (1 + assumed 3% growth) driven by steady infrastructure demand. | estimated | Low sensitivity to overall company valuation.; Order book or project pipeline |
| 租赁业务 | revenue | CNY mn | 559.9 | 571.0 | 582.0 | 594.0 | Base revenue × (1 + 2% growth reflecting modest fleet expansion offset by competitive rental rates). | estimated | Minimal impact on consolidated.; Fleet size and utilization |
| consolidated | revenue | CNY mn | 33143.88 | 37254.0 | 40600.0 | 43848.0 | Sum of segment revenues. 2026E is anchored on seasonally-adjusted annualized Q1 revenue of CNY 37,254 mn (EV011) as a proxy for full-year run rate, which embeds full-year price hike effect and higher H2 volumes. | calculated | Revenue is the primary value driver; 1% change = ~CNY 370 mn impact on top line, ~CNY 30 mn on net profit.; Q2-Q4 2026 actual revenue trajectory not yet known |
| consolidated | gross margin | % | None | 22.0 | 22.8 | 23.5 | Blended margin improving as price hikes flow through, overseas mix increases, and forex headwinds moderate. 2026E set at 22% vs Q1 21.3% to reflect H2 improvement. | estimated | Each 0.5pp on gross margin = ~CNY 186 mn gross profit; high impact on operating leverage.; 2025 full-year gross margin, Segment-level margins |
| consolidated | operating margin | % | None | 8.0 | 9.0 | 9.5 | Operating margin = Gross margin - SG&A ratio - R&D ratio. Assumes SG&A leverage as revenue grows and R&D remains ~3.5% of sales. | estimated | Highly sensitive; 1pp operating margin shift = ~CNY 373 mn operating profit in 2026E.; 2025 operating margin |
| consolidated | finance expense ratio | % | None | 1.5 | 1.4 | 1.3 | Finance expense ratio expected to normalize from Q1 1.91% as forex volatility potentially declines and debt cost moderate. | estimated | Important given high overseas revenue; 0.5pp reduction adds ~CNY 186 mn to pre-tax profit.; 2025 finance expense ratio, Forex sensitivity exact numbers |
| consolidated | effective tax rate | % | None | 20.0 | 20.0 | 20.0 | Assumed constant effective tax rate based on historical level; subject to change with regional profit mix. | estimated | ; 2025 effective tax rate |
| consolidated | minority interest % | % of net profit | None | 8.0 | 8.0 | 8.0 | Estimated based on typical consolidation structure; stable over forecast period. | estimated | ; 2025 minority interest amount and net profit attributable |
| consolidated | operating profit | CNY mn | None | 2980.0 | 3654.0 | 4166.0 | Revenue × operating margin. 2026E: 37,254 × 8.0% = 2,980. | calculated | ; 2025 actual operating profit |
| consolidated | parent net profit | CNY mn | 1609.23 | 1782.0 | 2271.0 | 2647.0 |  = (Operating profit - Revenue×finance_expense_ratio) × (1 - tax_rate) × (1 - minority_interest_pct). 2026E: (2980 - 37254*1.5%)*(1-20%)*(1-8%) = (2980-559)*0.8*0.92 = 2421*0.736 = 1782. 2027E: (3654 - 40600*1.4%)*0.8*0.92 = 2271. 2028E: (4166 - 43848*1.3%)*0.8*0.92 = 2647. | calculated | Primary driver of fair value; each CNY 100 mn change = ~CNY 0.048 per share at 2,100 mn share count (subject to share count resolution).; Share count for EPS calculation |
| consolidated | EPS | CNY per share | None | None | None | None | parent net profit / diluted share count. Share count missing; EPS set to null pending resolution. Using illustrative 2,100 mn shares: 2026E EPS = 1782/2100 = 0.849; 2027E = 1.081; 2028E = 1.260. | missing | ; diluted share count |
| consolidated | OCF | CNY mn | None | 1604.0 | 2271.0 | 2912.0 | parent net profit × OCF/Net profit conversion ratio (0.9x, 1.0x, 1.1x respectively). 2026E: 1782*0.9 = 1604. 2027E: 2271*1.0 = 2271. 2028E: 2647*1.1 = 2912. | estimated | ; 2025 OCF, historical cash conversion ratio |
| consolidated | capex | CNY mn | None | 1490.0 | 1624.0 | 1754.0 | Revenue × 4% capex intensity. 2026E: 37254*0.04 = 1490; 2027E: 40600*0.04 = 1624; 2028E: 43848*0.04 = 1754. | estimated | ; 2025 capital expenditures actual from cash flow statement |
| consolidated | FCF | CNY mn | None | 114.0 | 647.0 | 1158.0 | OCF - capex. 2026E: 1604 - 1490 = 114; 2027E: 2271 - 1624 = 647; 2028E: 2912 - 1754 = 1158. | calculated | Sensitive to working capital and capex assumptions.;  |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | 工程机械 | segment_volume | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with Q2 2026 filings and monthly excavator sales data | 5月挖机内销增速的绝对量基数, 内销转出口的具体比例 |
| KPE02 | 工程机械 | segment_volume | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with official CCMA data or company announcements | 5月挖掘机销量绝对量, 内销与外销的具体拆分规模 |
| KPE03 | 工程机械 | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until monitor company announcement or distributor channel checks on price list changes | 各产品线提价幅度, 提价对各区域销售的影响 |
| KPE04 | 工程机械 | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until compare implied PE with forward earnings estimates from filings | 柳工2026年预测EPS, 分析师目标价 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-06-15T09:34 | 有效窗口/22天 | 推荐措辞（非标准评级） | 未提取到带期间的明确盈利预测 | （2）工程机械 5月挖机数据表现亮眼，股价此前受交易风格与汇损拖累，但板块基本面数据坚挺、巨头涨价提振情绪，当前主机厂估值安全边际极高，【三一、徐工】在15x左右，【中联、柳工】在10x上下 | rating=推荐措辞（非标准评级） | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 中信机械/2026-06-12T14:35 | 有效窗口/25天 | 未披露 | 未提取到带期间的明确盈利预测 | 2、当前科技股有所回调，前期工程机械受海外战争以及汇率变化等影响，板块出现较大波动回调，当前三一、徐工等龙头主机厂26年估值已跌到15X左右，柳工不到10X | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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