# Forward Forecast Model Scaffold for 300750.SZ as of 2026-07-10

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 129131041000 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 24.8156% / +0.41pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.0482% / +2.75pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.6241 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 15.1878% / -2.62pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 21.0912% / +1.72pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Power battery revenue | GWh shipments x ASP | installation demand, share, customer mix, price clauses |
| Energy-storage revenue | GWh shipments x ASP | storage tenders, overseas demand, project delivery |
| Materials / recycling / other | volume x realized spread or service revenue | vertical integration and utilization |
| Gross profit | segment revenue x segment gross margin | lithium/material cost, yield, depreciation, warranty |
| Operating profit | gross profit - R&D - SG&A | R&D capitalization/expense, scale leverage |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion and capex cycle |

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
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE03 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 129131041000 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 24.8156% / +0.41pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 16.0594% / -0.42pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.0482% / +2.75pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.6241 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度... |
| EV030 | industry_kpi | secondary_or_derived_research | reported | asp_or_price | 2025, 年度 | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告: 四、主营业务分析 1、概述 公司于 2025 年 5 月 20 日在香港联交所主板成功挂牌上市，全球发售股份总数为 155,915,300 股（行 ，发行价格为 263.00 港元/股，募集资金总额... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 宁德时代新能源科技股份有限公司 2026 年第一季度报告 长期应收款 453,654 386,180 长期股权投资 67,874,958 6... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 260,272 25,565 填列） 信用减值损失（损失以“-”号填列） -250,651 -131,798 / ... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度报告: 衍生金融资产 1,754,079 1,133,502... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 球能源结构的根本变革。 而这无限机遇，我们也将始终与股东共同见证、共同分享。公司延续高比例分红的政策，... |
| EV058 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 20.4313 / earnings multiple the market is paying now / |
| EV059 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.4469 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 15.1878% / -2.62pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |
| EV010 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Inventory / revenue / 21.0912% / +1.72pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 动力电池系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026 Q1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=earnings_model; mode=llm_semantic |
| 储能系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| 锂电池回收利用 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 储能电池系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=62439820.0 (filing table unit not explicit in extracted row); revenue weight=15.349579280806763%; growth=8.99%; gross margin=26.71%; margin change=-0.13pp; source=filing_intelligence; mode=deterministic_filing_row |
| 电池材料及回收 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=21860936.0 (filing table unit not explicit in extracted row); revenue weight=5.374073312265196%; growth=-23.83%; gross margin=27.27%; margin change=16.76pp; source=filing_intelligence; mode=deterministic_filing_row |
| 采选冶炼行业 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=5978096.0 (filing table unit not explicit in extracted row); revenue weight=1.469595179811117%; growth=8.83%; gross margin=11.25%; margin change=2.72pp; source=filing_intelligence; mode=deterministic_filing_row |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 1613590733008 / current equity value / / / PE TTM / 20.4313 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
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
- Readiness reasons: Segmental volume and ASP data for forward years are not available from filings; reliant on unverified channel checks and sell-side estimates.; Diluted share count derived from registered capital, not directly from Tushare total_share; need cross-check with market cap/close price or precise filing data.; Key assumptions on lithium cost pass-through, segment-level margins, and competitive intensity require monitoring of upcoming quarterly disclosures and management briefing.; One or more filing-reported segments required deterministic restoration.; Material segment three-year driver lines are missing: 储能电池系统, 储能系统, 动力电池系统, 电池材料及回收, 锂电池回收利用; Valuation has not closed from mutually exclusive buckets to per-share fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 营业收入 = Σ(出货量 GWh × 销售单价 CNY/GWh)，主要来源于动力电池系统和储能电池系统；电池材料及回收和采选冶炼贡献有限。ASP受锂电原材料价格、产品组合和技术溢价影响。
- Profit: 营业利润 = 营收 – 营业成本(锂/正负极/电解液等原材料 + 人工与制造费用 + 折旧) – 研发/销售/管理费用 – 财务费用 + 其他收益。毛利率由锂价、产能利用率、产品组合和规模效应共同决定。
- Cash flow: 经营活动现金流 = 净利润 + 折旧摊销 – 营运资金变动；自由现金流 = 经营现金流 – 资本开支。资本开支主要用于产能建设、垂直整合及技术升级。
- Reinvestment: 资本开支密集；当前产能772 GWh，在建产能321 GWh；规模和技术壁垒支撑较高ROIC，但若需求放缓则存在资本回报下降风险。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 2026-2028年公司动力电池出货量增速能否维持25%以上，且全球市占率稳固在39%以上？ | unresolved | 动力电池出货量 GWh, ASP 下降速度, 毛利率 | Revenue, Gross Profit, EPS | 2026年上半年实际出货量数据, 分客户/车型的ASP信息; 2026年二季度或半年度出货公告 |
| Q2 | 储能电池2026年出货量能否达到250-300 GWh，且毛利率维持在26%以上？ | unresolved | 储能出货量 GWh, 储能ASP, 储能毛利率 | Revenue 增长, Gross Profit, FCF | 储能系统海外项目具体毛利, 钠电储能产品售价与成本; 2026年Q2/Q3出货数据和储能业务分项财务 |
| Q3 | 枧下窝锂矿复产能否在2026年以合理成本提供显著自供锂精矿，从而稳定并改善毛利率？ | unresolved | 锂矿自供比例, 锂矿现金成本, 锂价预期 | COGS, Gross Margin, FCF | 矿山复产具体时间表、产量规划及成本曲线, 自供锂对毛利率贡献的量化测算; 公司业绩电话会或公告中关于锂矿的详细说明 |
| Q4 | 固态电池和钠电等新技术的商业化进度是否会重塑竞争格局，公司能否保持技术溢价？ | unresolved | 固态电池量产时间表, 研发与资本开支节奏, 现有产品生命周期 | R&D expenses, Capex, Depreciation, Long-term growth rate | 固态电池的成本结构及与现有产线的兼容性, 客户导入时间表; 2026年下半年技术进展公告和业界会议 |
| Q5 | 美国贸易壁垒和海外本地化生产的推进是否会显著拖累海外业务的盈利能力和投资回报？ | unresolved | 海外收入占比, 海外毛利率与有效税率, 海外资本开支与回报周期 | Revenue, Operating Profit, Capex and FCF | 海外工厂产能爬坡曲线和盈利时间表, 对关税/政策的情景量化; 2026年下半年海外政策动态和公司海外业务指引 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 423701.8 | 560000.0 | 680000.0 | 800000.0 | Volume (GWh) × ASP; base year actual, forward estimates based on scenario-driven volume and price assumptions. | estimated | ±5% volume or ±3% ASP move effects ~±30bn revenue; Official guidance, Segment-level volume |
| consolidated | Gross Margin | % | 23.31 | 24.5 | 25.0 | 25.2 | Calculated from segment mix in FY2025; forward assumes scale, lithium cost pass-through, mix improvement. | estimated | Each 1pp change = ~6bn pre-tax profit; Detailed cost breakdown |
| consolidated | Operating Profit | CNY mn | None | 117000.0 | 153000.0 | 184000.0 | Revenue × Operating Margin; FY2025 operating margin not reported, estimated ~20.6% from Q1 2026. Forward assumes 20.9%, 22.5%, 23.0%. | estimated | Operating margin up/down 1pp changes profit by ~6-8bn; FY2025 operating profit/margin actual |
| consolidated | Parent Net Profit | CNY mn | 72201.3 | 96000.0 | 115000.0 | 135000.0 | (Operating Profit + Net Finance Income) × (1 - Tax Rate ~15%); forward growth 33%, 20%, 17%. | estimated | Net profit ±10% changes EPS by 2.1 CNY; Precise tax rate and non-operating items |
| consolidated | EPS | CNY/share | 15.61 | 20.749443979743354 | 24.856104767400893 | 29.17890559651409 | parent net profit (CNY mn) / diluted shares (mn) | calculated | Share count fluctuations not expected;  |
| consolidated | OCF | CNY mn | 133200.0 | 158000.0 | 190000.0 | 225000.0 | OCF/NI ratio ~1.6-1.7 applied to projected net profit; base year actual 133.2bn CNY. | estimated | Working capital changes can swing OCF by 10-20bn; Working capital detailed components |
| consolidated | Capex | CNY mn | None | 75000.0 | 70000.0 | 65000.0 | Estimated from capacity expansion plan (321 GWh under construction) and maintenance capex. | estimated | Capex = key to FCF; overspend risk on overseas projects; FY2025 actual capex from cash flow statement |
| consolidated | FCF | CNY mn | None | 83000.0 | 120000.0 | 160000.0 | OCF - Capex; forward years show improving FCF as capex moderates. | calculated | Significant free cash flow generation supports dividend and reinvestment; FY2025 actual capex and FCF |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until earnings call | JXW矿复产规模, 成本, 时间表 |
| KPE02 | 储能系统 | segment_volume | None GWh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 2026年9月交付启动 | 钠电储能系统价格, 毛利率, 总出货目标 |
| KPE03 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 具体业务合同或订单 | AIDC业务收入预期, 投资规模, 时间线 |
| KPE04 | 动力电池系统 | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 中试线建设 / 设备采购公告 | 固态电池量产时间表, 成本曲线, 对现有业务的影响 |
| KPE05 | 储能系统 | segment_volume | None GWh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 季度出货数据 | 储能业务毛利率, 具体出货量确认 |
| KPE06 | 动力电池系统 | asp_or_price | None 万元/吨 | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 永太科技公告确认 | VC订单价格, 对宁德时代成本影响, VC在电池中的添加比例 |
| KPE07 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 与宁德时代无关 |
| KPE08 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 矿山实际复产日期 | 复产规模, 成本, 对锂价影响的具体量化 |
| KPE09 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 与宁德时代关联度低 |
| KPE10 | consolidated | market_share | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 正式方案公告 | HVDC业务收入规模, 整合后市场份额, 盈利能力 |
| KPE11 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 与宁德时代无关 |
| KPE12 | 动力电池系统 | segment_volume | None GWh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 季度出货数据 | 排产数据的官方确认, 产能利用率, 产品结构 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 花旗/2026-07-10T12:41 | 高时效/0天 | 未披露 | 我们的解读如下—— (1) 我们预计宁德时代将在即将到来的业绩电话会议上向投资者提供更多关于JXW矿复产、新电池产能时间表以及全年电池产量/出货量目标的信息，我们估计这对锂基本面的影响偏向正面 | 16:10) 估值 基于宁德时代A股目标价人民币603元/股，并给予28%的溢价（即宁德时代历史H/A股溢价），我们将宁德时代H股估值定为港币888元/股 / 可能导致宁德时代H股未能达到我们目标价的下行风险包括：1) 电动汽车需求低于预期 / 15:00) 估值 基于2026年预期EV/EBITDA的17.5倍（较该股上市以来的历史平均水平高出0.25个标准差），我们将宁德时代A股估值定为人民币603元/股 | 2026E_EVEBITDA=17.5x；target_price=603元 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-10T10:22 | 高时效/0天 | 推荐措辞（非标准评级） | 公司海外业务快速推进，包括三方面进展：1）4月公告宁德时代入主，目前具体方案顺利推进中，我们预计距离公告正式方案已不远 | 未提取到目标价/估值方法与倍数 | rating=推荐措辞（非标准评级） | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 机构未识别/2026-07-01T12:41 | 有效窗口/9天 | 未披露 | 我们预计26年储能出货250-300GWh，同比翻番以上增长，全球市占率有望进一步提升 / [爱心]盈利预测与投资建议：公司出货量稳步提升、盈利水平稳定，业绩增长确定性好，我们预计26-28年归母净利润962/1215/1469亿元，同增33%/26%/21%，对应PE 20/16/13x | [爱心]盈利预测与投资建议：公司出货量稳步提升、盈利水平稳定，业绩增长确定性好，我们预计26-28年归母净利润962/1215/1469亿元，同增33%/26%/21%，对应PE 20/16/13x / 给予26年30x PE，对应目标价632元，继续强推！ [爆竹]风险提示：盈利能力不及预期，海外贸易政策变化等 | target_price=632元 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 机构未识别/2026-06-26T08:16 | 有效窗口/14天 | 推荐措辞（非标准评级） | 太阳所以在明年永太需要向宁德提供2.6w吨vc太阳目前vc属于紧缺水平，价格已经来到15w左右，预计这次订单，将给永太带来超预期的利润和收入 / 预计今年三季度的新2w产能会立刻对公司本年度利润做贡献 | 结合公司其余锂电材料的产能，目前公司估值看27年 5x左右 | rating=推荐措辞（非标准评级） | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI05 | 机构未识别/2026-06-24T17:12 | 有效窗口/16天 | 未披露 | 宁德时代预计今年有1万辆电动汽... 宁德时代预计今年有1万辆电动汽... 宁德时代预计今年有1万辆电动汽车安装钠离子电池 Images: | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI06 | 机构未识别/2026-06-24T08:13 | 有效窗口/16天 | 未披露 | 首批钠电储能解决方案，在中国市场将于2026年9月开始交付，预计到2026年底实现1GWh出货量 / 全球市场预计于2027年6月启动交付 | 钠电更新：宁德时代欧洲储能钠电... 钠电更新：宁德时代欧洲储能钠电... 钠电更新：宁德时代欧洲储能钠电发布会，capex提升到200GWh-6.23 宁德时代发布天恒钠电储能系统 6.22晚间，宁德时代在欧洲举办发布会，正式发布天恒钠电储能系统，系统在25℃环境下循环寿命超过15000次（70% SOH），在-20℃环境下仍可保持92%以上可用能量，在45℃高温环境下循环寿命超过10000次，电芯膨胀率降低40%，提供更高的安全性和可靠性，以500MWh、4小时储能项目为例，该技术可减少超过100万欧元非... | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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