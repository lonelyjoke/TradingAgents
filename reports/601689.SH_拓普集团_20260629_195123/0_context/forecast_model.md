# Forward Forecast Model Scaffold for 601689.SH as of 2026-06-29

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 6628185769.77 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 19.2562% / -0.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.455% / +1.36pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.9917 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 21.5404% / -0.89pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 16.3813% / -0.19pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Core product revenue | sum(customer vehicle volume x platform share x content per vehicle), cross-checked with segment units x ASP | customer/model exposure, SOP cadence, annual price reductions and product mix |
| Segment gross profit | sum(segment revenue x segment gross margin) | ASP, material pass-through, utilization, launch/ramp cost and mix |
| Operating profit | segment gross profit - R&D - selling/admin - impairment | R&D conversion, scale leverage, depreciation and credit risk |
| Parent net profit / EPS | operating profit +/- finance and FX - tax - minority; divided by diluted shares | interest versus FX decomposition, subsidies/one-offs and share count |
| OCF / capex / FCF / incremental ROIC | net profit + D&A - working capital - capex; incremental EBIT after tax / incremental invested capital | receivables, inventory, new-plant ramp, capex discipline and cash conversion |
| Second-curve scenario value | qualified delivered units x ASP x margin, valued separately until unit economics and cash conversion are verified | customer nomination, order-to-revenue schedule, capex, utilization and probability |

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 6628185769.77 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 19.2562% / -0.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 8.3251% / -1.48pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.455% / +1.36pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.9917 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 9/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV030 | financial_report_intelligence | primary_or_structured_filing | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.59%, gross margin change -0.17pp, operating margin change  |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.59%, gross margin change -0.17pp, operating margin chan... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.59%, gross margin change -0.17pp, operating margin c... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 拓普集团2026年第一季度报告: 其他债权投资 长期应收款 长期股权投资 113,137,486.17 105,254,429.52 / long_term_equ... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 拓普集团2026年第一季度报告: 公允价值变动收益（损失以“-”号 填列） 信用减值损失（损失以“-”号填列） 77,642,035.79... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 拓普集团2026年第一季度报告: 交易性金融资产 601,000,000.00 400,000,000.00 衍生金融资产 应收票据 26,062,354.01 15,798,084.56 / receivables: 拓普集团2026年第一季度报告: 衍生金融资产 应收票据 26,062... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 拓普集团2025年年度报告: 余未分配利润滚存至下一年度。 如在本利润分配预案披露之日至实施权益分派的股权登记日期间，公司总... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 32.8978 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 2.9885 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 汽车零部件 (八大业务板块) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 机器人执行器 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 液冷服务器 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 车规级制氧 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 90975693660 / current equity value / / / PE TTM / 32.8978 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: 稀释后总股本缺失，EPS和每股公允价值无法计算; 资本支出（capex）及自由现金流（FCF）历史数据与计划未充分披露，前瞻估计依赖假设; 机器人执行器、液冷服务器、车规级制氧等新兴业务缺乏收入、毛利率、订单等量化数据，仅作期权价值处理; 分部收入未按八大板块拆分，仅使用主营业务/其他业务总额; 存在关键冲突：Q1毛利率变动-0.64pp与财年化变动-0.17pp，需明确比较期间; 2025Q1实际收入基数未提供，无法计算Q1 2026真实同比增速; Three-year values remain missing for consolidated line(s): EPS, Capex, FCF; Material segment three-year driver lines are missing: 机器人执行器, 汽车零部件 (八大业务板块), 液冷服务器, 车规级制氧
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 营收 = 单车配套价值（产品组合×ASP） × 配套车型数量 × 车型产销量 + 新业务零星收入。核心由定点订单、整车销量、新能源渗透率驱动。
- Profit: 毛利 = 营收 - 营业成本（直接材料约60-70%、人工、制造费用）；营业利润 = 毛利 - 销售/管理/研发费用（研发费用约占收入5%） - 财务费用（利息支出等）；税前利润 - 所得税 = 净利润；少数股东损益极小，归母净利润接近净利润。
- Cash flow: 经营性现金流≈归母净利润 + 折旧摊销 - 营运资本增加（应收账款和存货占比高，OEM账期3-6个月）；资本开支主要用于海内外产能建设和研发设备，规模较大；自由现金流 = 经营现金流 - 资本支出，现阶段可能偏弱。
- Reinvestment: 资本密集：年研发投入约占收入5%，产能扩张（波兰二期、泰国一期等）需要大量资本开支，在建工程和固定资产占比较高。再投资回报需待产能爬坡后释放，短期内ROIC承压。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 机器人执行器何时获得首批量产定点订单，订单金额和毛利率预期如何？ | 未获得公开定点，无明确时间表，公司处于产能筹备和研发阶段 | 机器人执行器分部收入、毛利率, SOTP中机器人业务估值倍数, bull scenario概率 | 2027E/2028E机器人业务收入, 归母净利润, EPS, 公允价值/股 | 定点公告或合同金额, 样品客户测试反馈, 产能建设和时间表; 等待特斯拉Optimus或国内人形机器人厂商的Tier1定点公告，或公司半年报/年报中披露具体订单金额 |
| Q2 | 海外工厂（波兰二期、泰国一期）产能爬坡进度和成本结构能否支撑毛利率回升？ | 泰国一期计划2026年投产并逐步放量；波兰二期筹划扩建。无具体爬坡曲线和毛利率指引。 | 汽车零部件毛利率假设, 2026E/2027E营收增速, capex与折旧 | 2027E/2028E毛利率, 营业利润, FCF | 分工厂产能利用率, 海外工厂盈亏数据, 单位制造成本变化; 2026半年报是否披露海外工厂营收、利润或产能利用率；并与公司互动中‘爬坡放量’定性描述对照 |
| Q3 | 全球汽车销量（尤其中国和欧洲）2026-2028年增长斜率会否低于公司隐含的客户订单增长？ | 2025年全球销量温和增长，中国新能源乘用车仍保持中高增速，但2026年不确定性上升。 | 汽车零部件收入增速, 估值倍数（PE）, bull/base概率 | 2026E-2028E营收, 归母净利润, EPS | 公司按客户/区域的销量指引, 核心客户（如特斯拉）的整车产量计划; 密切关注全球主要汽车市场月度销量数据和公司主要客户季度交付数据 |
| Q4 | 融资成本和杠杆率上升（财务费用率YoY+1.36pp）是否会持续侵蚀净利润？ | Q1 2026财务费用率1.455%，同比+1.36pp，大幅上升。原因未明。 | 财务费用率假设, 净利润率, EPS, FCF | 归母净利润, 利润率, FCF | 新增有息负债规模与利率, 2026年利息费用指引; 2026年半年报披露利息支出和负债结构，分析融资租赁义务 |
| Q5 | 液冷服务器和车规级制氧等第一批新业务能否在2027年前产生可辨识的收入和利润？ | 液冷获15亿订单，但交付时间和盈利不明；制氧无实质进展。 | 其他新业务收入, SOTP选项价值, bull场景概率 | 2027E/2028E营收, 归母净利润, 估值 | 液冷订单交付计划、毛利率, 制氧产品进度和客户; 2026年半年报是否将液冷、制氧业务收入单独列示 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 29581.5 | 31264.0 | 35016.0 | 38518.0 | 基于Q1 2026年化估算，叠加温和增长 | model_driven | 需求驱动：汽车销量、新订单，新业务贡献;  |
| consolidated | Gross Margin | % | 19.43 | 19.5 | 20.0 | 20.5 | 毛利率随产能利用率和产品结构改善温和回升 | estimated | 原材料成本、年降压力、新厂爬坡;  |
| consolidated | Operating Margin | % | None | 11.0 | 12.0 | 12.5 | 毛利率改善叠加经营杠杆，但研发和管理费用刚性增长 | estimated | 费用控制、收入增速; FY2025营业利润及营业利润率 |
| consolidated | Operating Profit | CNY mn | None | 3439.0 | 4202.0 | 4815.0 | 营收 × 营业利润率 | computed | 同上;  |
| consolidated | Parent Net Profit | CNY mn | 2779.1 | 2814.0 | 3151.0 | 3478.0 | 从营业利润减去财务费用、非经常损益和所得税，净利率约9.0-9.5% | estimated | 财务费用率、有效税率、非经常项目;  |
| consolidated | EPS | CNY | None | None | None | None | 归母净利润 / 稀释后总股本 | missing | 股本数量、净利润; 稀释后总股本 |
| consolidated | OCF | CNY mn | None | 2786.0 | 3120.0 | 3443.0 | 归母净利润 × 0.99 (Q1 OCF/NI ratio) | model_driven | 营运资本波动; 折旧摊销 |
| consolidated | Capex | CNY mn | None | None | None | None | 产能建设资本开支，无公开指引 | missing | 扩张节奏、外部融资; 资本支出计划 |
| consolidated | FCF | CNY mn | None | None | None | None | OCF - Capex | missing | Capex; Capex |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | market_sentiment | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline_value, revised_value, revenue_base_cny_mn, revenue_impact_pct, margin_impact_pp, incremental_net_margin_pct, tax_rate_pct, share_count_mn, cash_conversion_ratio, bull_probability_before_pct, bull_probability_after_pct, base_probability_before_pct, base_probability_after_pct, bear_probability_before_pct, bear_probability_after_pct |
| KPE02 | 机器人执行器 | industry_sentiment | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline_value, revised_value, revenue_base_cny_mn, revenue_impact_pct, margin_impact_pp, incremental_net_margin_pct, tax_rate_pct, share_count_mn, cash_conversion_ratio, bull_probability_before_pct, bull_probability_after_pct, base_probability_before_pct, base_probability_after_pct, bear_probability_before_pct, bear_probability_after_pct |
| KPE03 | 机器人执行器 | demand_signal | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline_value, revised_value, revenue_base_cny_mn, revenue_impact_pct, margin_impact_pp, incremental_net_margin_pct, tax_rate_pct, share_count_mn, cash_conversion_ratio, bull_probability_before_pct, bull_probability_after_pct, base_probability_before_pct, base_probability_after_pct, bear_probability_before_pct, bear_probability_after_pct |
| KPE04 | 机器人执行器 | industry_sentiment | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline_value, revised_value, revenue_base_cny_mn, revenue_impact_pct, margin_impact_pp, incremental_net_margin_pct, tax_rate_pct, share_count_mn, cash_conversion_ratio, bull_probability_before_pct, bull_probability_after_pct, base_probability_before_pct, base_probability_after_pct, bear_probability_before_pct, bear_probability_after_pct |
| KPE05 | consolidated | supply_chain_input | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline_value, revised_value, revenue_base_cny_mn, revenue_impact_pct, margin_impact_pp, incremental_net_margin_pct, tax_rate_pct, share_count_mn, cash_conversion_ratio, bull_probability_before_pct, bull_probability_after_pct, base_probability_before_pct, base_probability_after_pct, bear_probability_before_pct, bear_probability_after_pct |
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