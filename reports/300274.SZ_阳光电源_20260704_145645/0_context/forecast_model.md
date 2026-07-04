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
| 光伏逆变器 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 储能系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=30.0%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| 氢能（电解槽） | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
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
- Readiness reasons: 官方未披露分业务收入、毛利率、出货量等关键运营指标，业务单元均为分析性拆分，缺少官方数据支撑。; 未提供稀释后总股数，无法计算每股收益和每股公允价值。; 资本支出和自由现金流数据仅Q1报告部分可见，全年预测缺乏完整的资本开支基准。; KPE证据仅含方向性摘要，无具体数量化数据，无法量化场景概率变动。; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 储能系统, 光伏逆变器, 氢能（电解槽）; Bull/base/bear per-share valuation is incomplete.; Valuation has not closed from mutually exclusive buckets to per-share fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 收入 = ∑ (业务线出货量 × 单位售价)，核心驱动为光伏新增装机量、储能订单、政策催化和产品溢价。
- Profit: 毛利 = 收入 - 物料/人工/制造成本；营业利润 = 毛利 - 销售/管理/研发费用；归母净利润受财务费用、投资收益及补贴影响。
- Cash flow: 经营现金流 = 净利润 + 折旧摊销 ± 营运资金变动（应收、存货、应付、合同负债等） - 实际税付；投资现金流主要流向产能建设与研发资产；筹资现金流反映借款及分红。
- Reinvestment: 持续高比例研发投入（2025年研发费用41.75亿元）及全球化产能布局，资本支出主要用于逆变器/储能产线、研发设备与数字化升级。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 储能系统毛利率能否维持在30%左右，并在2026-2027年实现正向经营杠杆？ | 2026Q1毛利率约为30%，环比提升归因于欧洲高毛利区域收入占比提升。美国38.4%关税和碳酸锂波动仍是压力。 | 储能系统出货量GWh, 区域收入结构, 碳酸锂现货价格, 储能单位成本 | 储能分部收入, 合并毛利率, 营业利润, EPS, 自由现金流 | 2026Q2及后续储能出货量和区域毛利率, 美国市场新签订单额, 碳酸锂价格趋势; 2026年半年报及投资者关系披露 |
| Q2 | 在贸易壁垒加剧的背景下，美国储能业务能否维持，甚至转化为公司核心利润源？ | 目前美国关税38.4%，2026年有新签订单，但因提前下单效应，2025年订单已透支，2026年订单量可能出现波折。 | 美国储能订单金额, 美国市场毛利率, 关税变化 | 储能分部收入, 营业利润, 经营现金流 | 美国客户合同条款, 供应链转移进展, 政策走向; 公司重大合同公告或美国政策更新 |
| Q3 | 光伏逆变器ASP下降与出货量增速是否足以支撑核心利润？有无市场份额丧失风险？ | 公司逆变器全球领先，但2026Q1毛利率同比下滑1.87个百分点，可能反映价格压力。 | 光伏逆变器出货量GW, ASP, 毛利率 | 逆变器分部收入, 合并毛利率, 营业利润率, EPS | 逆变器出货量及ASP季度数据, 主要区域市场份额, 欧盟政策对逆变器的影响评估; 半年报和行业出货排名 |
| Q4 | 合同负债及预付账款大幅增长（预付款项+201%）是否意味着2026Q2加速交付，并转化为收入和现金？ | 合同负债约122亿元（推测），预付款40亿元主因锁定原材料供货，公司未提供明确Q2指引。 | Q2收入环比增长, 存货与预付款周转天数, 经营性现金流/净利润比率 | 合并收入, 经营现金流, 应收账款周转率 | Q2排产计划数字, 合同负债对应的在手订单转化率, 客户提货时间表; 2026年半年报，尤其现金流量表与收入确认 |
| Q5 | 欧盟拟限制使用中国逆变器的政策对公司欧洲业务的实际影响程度和应对措施？ | 公司初步评估影响有限，主要针对欧盟公共资金项目，公司正加强与欧洲客户沟通并布局本地化供应链。 | 欧洲逆变器收入占比, 本地化产能进度, 政策执行细则 | 逆变器欧洲区收入, 整体毛利率, 销售费用 | 欧盟禁令具体条款和实施时间, 欧洲本地化供应产能, 欧洲在手订单结构; 公司公告本地化投资进展或欧盟政策细化 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业总收入 | CNY mn | 89184.0 | 94535.0 | 99770.0 | 104840.0 | 2025A: 89,184mn; 2026E +6.0%, 2027E +5.5%, 2028E +5.1% | analyst_estimated | 出货量增速与ASP变化; 分业务收入驱动 |
| consolidated | 营业成本 | CNY mn | 60795.0 | 64938.0 | 68290.0 | 71560.0 | 收入 × (1-毛利率)；2026E 毛利率31.3%，2027E 31.5%，2028E 31.7% | analyst_estimated | 原材料价格、竞争程度;  |
| consolidated | 毛利 | CNY mn | 28389.0 | 29597.0 | 31480.0 | 33280.0 | 收入 × 毛利率 | analyst_estimated | 毛利率假设;  |
| consolidated | 营业利润 | CNY mn | 15320.0 | 13600.0 | 14300.0 | 15100.0 | 估计营业利润率：2025A约17.2%，2026E 14.4%承压，2027E 14.3%，2028E 14.4% | analyst_estimated | 费用率控制、财务费用; 2025年准确营业利润和费用结构 |
| consolidated | 归母净利润 | CNY mn | 13461.0 | 11500.0 | 12150.0 | 12880.0 | 营业利润 - 利息 + 其他收益 - 所得税，净利率假设：2026E 12.2%，2027E 12.2%，2028E 12.3% | analyst_estimated | 财务费用、汇兑损益、补贴; 财务费用预测, 投资收益等非经常项 |
| consolidated | 稀释每股收益 | CNY | None | None | None | None | 归母净利润 / 稀释后总股数 | missing | 总股数; 稀释后总股数（百万股） |
| consolidated | 经营活动现金流量净额 | CNY mn | 16918.0 | 9200.0 | 10200.0 | 11000.0 | OCF = 净利润 × 现金转化率；假设转化率0.8-0.85，2026E因营运资金增加偏低 | analyst_estimated | 应收/应付管理、存货消化; 实际营运资金变动 |
| consolidated | 资本支出 | CNY mn | None | 1800.0 | 1600.0 | 1500.0 | 估计基于研发资本化及产能投资，无准确历史数字 | analyst_estimated | 产能扩张节奏; 2025年实际资本支出 |
| consolidated | 自由现金流 | CNY mn | None | 7400.0 | 8600.0 | 9500.0 | OCF - 资本支出 | analyst_estimated | 营运资金与资本支出; 历史资本支出 |
| consolidated | gross_margin |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | ocf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | revenue |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | 排产环比变化, 产能利用率, 合同负债变动, 收入确认节奏 |
| KPE02 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | 排产环比变化, 产能利用率, 合同负债变动, 收入确认节奏 |
| KPE03 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | 排产环比变化, 产能利用率, 合同负债变动, 收入确认节奏 |
| KPE04 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | 排产环比变化, 产能利用率, 合同负债变动, 收入确认节奏 |
| KPE05 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 政策原文、执行细则、受益范围、时间表、预算/补贴落地 | 政策原文, 执行细则, 受益范围, 时间表, 预算/补贴落地 |
| KPE06 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 政策原文、执行细则、受益范围、时间表、预算/补贴落地 | 政策原文, 执行细则, 受益范围, 时间表, 预算/补贴落地 |
| KPE07 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 调研纪要具体内容, 与公开数据交叉验证 |
| KPE08 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | AIDC推荐逻辑, 与公司业务关联度, 具体数据支持 |
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