# Forward Forecast Model Scaffold for 300750.SZ as of 2026-07-01

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
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | scenario probability before->after or watch/reject |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | numeric assumption delta or explicit rejection |
| KPE03 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | 公告、财务、同行、价格成交、后续调研或可观察代理指标 | scenario probability before->after or watch/reject |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE07 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 129131041000 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 24.8156% / +0.41pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 16.0594% / -0.42pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.0482% / +2.75pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.6241 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 7/7 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV030 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度报告: |
| EV033 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | asp_or_price | 2025, 年度 | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告: 四、主营业务分析 1、概述 公司于 2025 年 5 月 20 日在香港联交所主板成功挂牌上市，全球发售股份总数为 155,915,300 股（行 ，发行价格为 263.00 港元/股，募集资金总额... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 宁德时代新能源科技股份有限公司 2026 年第一季度报告 长期应收款 453,654 386,180 长期股权投资 67,874,958 6... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 260,272 25,565 填列） 信用减值损失（损失以“-”号填列） -250,651 -131,798 / ... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度报告: 衍生金融资产 1,754,079 1,133,502... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 球能源结构的根本变革。 而这无限机遇，我们也将始终与股东共同见证、共同分享。公司延续高比例分红的政策，... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 22.4863 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.7936 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| consolidated | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=20251231; reported revenue=423701834000.0 (yuan); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| power_battery | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| energy_storage | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| battery_recycling | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 动力电池系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=316506369.0 (filing table unit not explicit in extracted row); revenue weight=77.80675222711693%; growth=25.08%; gross margin=23.84%; margin change=-0.1pp; source=filing_intelligence; mode=deterministic_filing_row |
| 储能电池系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=62439820.0 (filing table unit not explicit in extracted row); revenue weight=15.349579280806763%; growth=8.99%; gross margin=26.71%; margin change=-0.13pp; source=filing_intelligence; mode=deterministic_filing_row |
| 电池材料及回收 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=21860936.0 (filing table unit not explicit in extracted row); revenue weight=5.374073312265196%; growth=-23.83%; gross margin=27.27%; margin change=16.76pp; source=filing_intelligence; mode=deterministic_filing_row |
| 采选冶炼行业 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=5978096.0 (filing table unit not explicit in extracted row); revenue weight=1.469595179811117%; growth=8.83%; gross margin=11.25%; margin change=2.72pp; source=filing_intelligence; mode=deterministic_filing_row |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 1775884546064.0002 / current equity value / / / PE TTM / 22.4863 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | / 2026-06-22 / valuation_method / pdf_text_available / 价格方面，碳酸锂价格高位可持续，电池价格传导顺畅，产业链龙头 Q2 盈利水平预计依旧亮眼，铜 箔、隔膜、铝箔等二轮涨价近期有望落地，估值已回调至27 年 15x，Q3 旺季行情确定，首推宁德时代、亿 纬锂能等，重点看好恩捷股份、佛塑科技、璞泰来、鼎胜新材、科达利、富临精工、天赐材料、湖南裕能... / compare with TradingAgents valuation bridge, PE/PB decomposition, and downside support / | label broker/date/count; use range or median only when the source is company-specific |
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
- Readiness reasons: 分部营收和毛利率可从2025年年报提取；缺少产能利用率、分产品均价和出货量，导致预测依赖粗略假设; 股份数量未从可靠来源获取，使用推算值并标记为计算值，可能影响每股指标精度; 资本开支和自由现金流缺乏具体数值，仅基于比例粗估; 新业务（如AIDC、固态电池）尚无收入确认，估值仅作为情景期权处理; One or more filing-reported segments required deterministic restoration.; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: battery_recycling, energy_storage, power_battery; Valuation closure conflicts with probability-weighted scenario value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 营收 = Σ(各板块出货量 × 均价) = 动力电池出货量×动力电池均价 + 储能系统出货量×储能均价 + 其他收入
- Profit: 营业利润 = 营收 - 营业成本 - 期间费用；营业成本主要受锂等原材料价格、制造费用和规模效应影响；期间费用含研发、销售、管理、财务费用
- Cash flow: OCF = 净利润 + 折旧摊销 - 营运资本变动；FCF = OCF - 资本开支（主要用于产能建设和维护）
- Reinvestment: 重资产模式，需持续高额资本开支以扩张产能；2025年末锂电池产能772GWh，在建321GWh；资本开支回报周期较长

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 动力电池全球渗透率增速是否可持续，以及公司市占率能否维持在39%左右？ | 根据2025年销量541GWh、增长41.85%，市占率提升至39.2%，近期订单和渗透率仍积极，但明年增速可能放缓至20%左右。 | 动力电池出货量增长率, 动力电池ASP变化 | 营收, 毛利率, 净利润 | 2026年H1销量数据, 车企订单指引; 中报及行业装机数据 |
| Q2 | 在行业产能过剩风险下，公司储能电池业务的毛利率能否保持25%以上？ | 2025年毛利率26.71%，同比略降，但储能价格仍有下降趋势，公司大电芯和系统方案有助于维持溢价。钠电可能降低成本。 | 储能电池出货量增速, 储能系统毛利率 | 储能分部营收, 毛利, 应收账款质量 | 储能售价与成本明细, 在手订单金额; 下半年大型储能项目招标结果 |
| Q3 | 钠离子电池和固态电池的商业化进度对营收和利润的贡献何时启动？ | 公司表示2027年固态电池有望小批量生产，钠电池已发布产品并在储能/商用车应用。目前未产生显著收入。 | 新电池营收规模, 资本开支相关折旧 | 新增收入来源, 研发费用, 资本开支 | 小批量量产时间和成本, 客户签约; 公司技术更新公告 |
| Q4 | 海外产能（匈牙利基地）建设的回报和风险，何时能贡献利润？ | 在建产能321GWh，包含匈牙利项目；预计2026-2027年部分投产，但初期可能低利用率。 | 海外产能利用率, 资本开支强度, 折旧额 | 折旧, 成本, FCF | 海外项目IRR估算, 当期资本开支金额; 年报披露海外基地运营数据 |
| Q5 | 锂价止跌和原材料成本传导机制是否足以支撑毛利率继续提升？ | 锂价在16.5万/吨附近磨底，公司可通过长协和库存周期管理获得成本优势，但向下传导给客户的电池降价压力可能抵消。 | 锂价变化, 动力电池ASP变化 | 毛利率, 存货减值 | 锂价与电池售价之间的相关系数, 库存跌价准备; 季度存货和利润跟踪 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 423701.834 | 478800.0 | 536300.0 | 589900.0 | base * (1+ g1) where g1=13%, g2=12%, g3=10% | analyst_estimate | +/- 5% growth shift changes year-3 revenue by ~30B, impacting EPS ~7%; 具体销量和均价假设, 分部增长拆分 |
| consolidated | Gross Profit | CNY mn | 105120.0 | 119700.0 | 134100.0 | 147500.0 | Revenue * assumed gross margin (25%) | analyst_estimate | 1pp gross margin shift affects year-3 op profit ~6B; 成本明细, 价格料动假设 |
| consolidated | Operating Profit | CNY mn | None | 93500.0 | 105000.0 | 115500.0 | Gross Profit - SGA & other Opex; assumed opex/revenue ~5.5% | analyst_estimate | ; 详细费用拆分, 研发费率趋势 |
| consolidated | Net Profit (Parent) | CNY mn | 72201.282 | 83800.0 | 93800.0 | 103200.0 | Operating Profit less net finance cost (lower leverage) and tax; assumed tax rate ~12% | analyst_estimate | 1% change in net margin = ~5B profit change; 有效税率, 利息收支明细 |
| consolidated | EPS (Basic, CNY) | CNY | 15.09 | 17.52 | 19.62 | 21.58 | Net profit / diluted shares (4783 mn) | analyst_estimate | ; 精确稀释股数确认 |
| consolidated | OCF | CNY mn | 133200.0 | 125700.0 | 140000.0 | 150000.0 | Net profit * OCF/NI ratio (1.5x gradually); based on historical 1.84x in 2025 | analyst_estimate | ; WC detail forecast, 折旧与摊销 |
| consolidated | Capex | CNY mn | None | None | None | None | Not reliably derived; expected to be high given 321GWh under construction | missing | ; 现金支付购建固定资产金额, 资本开支计划 |
| consolidated | FCF | CNY mn | None | None | None | None | OCF - capex; cannot compute due to missing capex | missing | ; capex |
| 动力电池系统 | Revenue | CNY mn | 316506.369 | 355000.0 | 393000.0 | 430000.0 | growing at ~12% -> 10.7% -> 9.4% | analyst_estimate | ; 出货量和均价假设 |
| 储能电池系统 | Revenue | CNY mn | 62439.82 | 80000.0 | 100000.0 | 120000.0 | growth ~28% -> 25% -> 20% reflecting strong demand | analyst_estimate | ; 项目订单 |
| 电池材料及回收 | Revenue | CNY mn | 21860.936 | 25000.0 | 28000.0 | 31000.0 | modest recovery in volume and price | analyst_estimate | ; 回收量 |
| 采选冶炼行业 | Revenue | CNY mn | 5978.096 | 6200.0 | 6500.0 | 6800.0 | stable | analyst_estimate | ; 采矿量 |
| consolidated | eps | CNY/share | None | 17.520384695797617 | 19.611122726322392 | 21.57641647501568 | parent net profit (CNY mn) / diluted shares (mn) | calculated | ; required consolidated forecast line omitted |
| consolidated | gross_margin |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | 永太科技合同金额, 供货量/时长, 当前基线利用率 |
| KPE02 | energy_storage | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | 钠电储能订单金额, 欧洲储能市场规模, 储能基线收入 |
| KPE03 | consolidated | new_business_opportunity | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 公告、财务、同行、价格成交、后续调研或可观察代理指标 | AIDC电力需求预估, 公司产品方案, 潜在收入规模 |
| KPE04 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 外资研报内容, 目标价, 关键假设 |
| KPE05 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 永太科技合同金额, 供货量/时长, 当前基线利用率 |
| KPE06 | energy_storage | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 钠电储能订单金额, 欧洲储能市场规模, 储能基线收入 |
| KPE07 | consolidated | new_business_opportunity | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | AIDC电力需求预估, 公司产品方案, 潜在收入规模 |
| KPE08 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 具体段子内容, 可验证线索 |
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