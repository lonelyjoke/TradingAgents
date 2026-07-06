# Forward Forecast Model Scaffold for 300750.SZ as of 2026-07-06

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
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
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
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 7/7 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV030 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度报告: |
| EV033 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | asp_or_price | 2025, 年度 | / segment_economics_depth / Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. / 2025年年度报告: 四、主营业务分析 1、概述 公司于 2025 年 5 月 20 日在香港联交所主板成功挂牌上市，全球发售股份总数为 155,915,300 股（行 ，发行价格为 263.00 港元/股，募集资金总额... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 宁德时代新能源科技股份有限公司 2026 年第一季度报告 长期应收款 453,654 386,180 长期股权投资 67,874,958 6... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 260,272 25,565 填列） 信用减值损失（损失以“-”号填列） -250,651 -131,798 / ... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度报告: 衍生金融资产 1,754,079 1,133,502... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 球能源结构的根本变革。 而这无限机遇，我们也将始终与股东共同见证、共同分享。公司延续高比例分红的政策，... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 21.9397 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.7014 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 动力电池 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 储能电池 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 电池回收 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 钠电储能 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=; mode=llm_semantic |
| 动力电池系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=316506369.0 (filing table unit not explicit in extracted row); revenue weight=77.80675222711693%; growth=25.08%; gross margin=23.84%; margin change=-0.1pp; source=filing_intelligence; mode=deterministic_filing_row |
| 储能电池系统 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=62439820.0 (filing table unit not explicit in extracted row); revenue weight=15.349579280806763%; growth=8.99%; gross margin=26.71%; margin change=-0.13pp; source=filing_intelligence; mode=deterministic_filing_row |
| 电池材料及回收 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=21860936.0 (filing table unit not explicit in extracted row); revenue weight=5.374073312265196%; growth=-23.83%; gross margin=27.27%; margin change=16.76pp; source=filing_intelligence; mode=deterministic_filing_row |
| 采选冶炼行业 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=5978096.0 (filing table unit not explicit in extracted row); revenue weight=1.469595179811117%; growth=8.83%; gross margin=11.25%; margin change=2.72pp; source=filing_intelligence; mode=deterministic_filing_row |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 1732718115221 / current equity value / / / PE TTM / 21.9397 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: 分部收入和毛利率从年报中获得，但缺少完整的营运资本、资本支出和自由现金流细节，无法提供完整的现金流预测。; 稀释股数根据注册资本初步确定，尚未与Tushare的total_share交叉验证，也未考虑潜在的库存股或股权激励摊薄。; 储能和钠电等新业务的分析性单元尚未披露完整的分部财务数据。; One or more filing-reported segments required deterministic restoration.; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 储能电池, 动力电池, 电池回收, 钠电储能; volume_price_cost driver chain is incomplete; missing: utilization; Three-year values remain missing for consolidated line(s): 资本支出CAPEX, 自由现金流FCF, gross_margin
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 收入 = Σ(各产品出货量GWh × 平均售价ASP元/kWh)。主要包括动力电池系统、储能电池系统和电池材料及回收业务。
- Profit: 毛利 = 收入 – 原材料成本(特别是碳酸锂等) – 制造成本；营业利润 = 毛利 – 研发费用 – 销售与管理费用；净利润 = 营业利润 + 其他收益 – 财务费用 – 所得税。
- Cash flow: 经营现金流 = 净利润 + 折旧摊销 ± 营运资本变动；自由现金流 = 经营现金流 – 资本支出(主要是产能扩张和钠电新项目)。
- Reinvestment: 资本密集度高，持续进行产能扩张(当前在建321GWh)和新技术投入(钠电产能200GWh)，高额资本支出既是增长引擎，也是ROIC的关键制约因素。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 储能电池2026年出货量能否达到250-300GWh，并且保持毛利率≥26%？ | 2025年储能出货约120GWh，2026Q1出货50GWh，符合全年翻番预期；海外高盈利订单支持毛利率，但尚需全面验证。 | 储能出货量(GWh), 储能ASP(元/kWh), 储能毛利率(%) | 储能电池系统收入, 合并毛利, 归母净利润, EPS | 储能分国家/项目毛利率数据; 2026年半年报披露储能出货量和毛利率，以及在手订单情况 |
| Q2 | 动力电池ASP下降速度会否超过成本下降速度，导致2026-2028年毛利率趋势性下滑？ | 2025年动力电池毛利率仅微降0.1pp至23.84%，显示成本管控与ASP降幅平衡良好。2026年锂价低位震荡，ASP可能继续下降，但能否维持毛利率面临挑战。 | 动力电池ASP(元/kWh), 动力电池单位成本(元/kWh) | 动力电池系统收入, 动力电池系统毛利, 合并毛利率, 归母净利润 | 动力电池ASP具体价格变化, 成本拆分明细; 跟踪2026年Q3电池报价和金属价格，评估ASP和单位成本趋势 |
| Q3 | 枧下窝锂矿复产能为公司降低多少碳酸锂采购成本，进而提升毛利率？ | 矿已取得安全生产许可证，复产节奏好于预期，但具体产量和对成本的实际影响未量化。 | 碳酸锂自供比例, 碳酸锂综合采购成本(元/吨) | 合并毛利, 归母净利润, OCF | 矿山产量指引, 自有矿成本与市场价差; 公司关于矿山复产的公告及2026下半年运营数据 |
| Q4 | 美国大选后的贸易政策会不会将动力/储能电池纳入限制清单，严重影响公司海外收入和利润？ | 目前政策主要针对逆变器，公司以电芯及电池系统供应为主，被波及的直接风险较低。但长期地缘政治风险仍在。 | 储能美国业务占比, 海外出货增速 | 境外收入, 合并毛利率, 归母净利润 | 美国具体政策演进和落地时间表; 跟踪美国国会相关立法动态和公司在美国市场的出货数据 |
| Q5 | AIDC（AI数据中心）新业务能否在2027-2028年贡献显著的盈利，成为第三增长曲线？ | 已启动大规模招聘，从战略走向落地，但尚未产生实质性收入，仍处于前期投入阶段。 | AIDC收入(亿元), AIDC利润率(%) | 新增收入项, 运营支出增加, 未来EPS | AIDC收入预测和客户订单; 关注2027年是否有首批订单披露或收入确认 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业收入 | CNY mn | 423701.83 | 540000.0 | 675000.0 | 810000.0 | 动力+储能+回收及其他，假设动力出货量CAGR 15%，储能出货量CAGR 40%，ASP年均下降3-5% | analyst_estimate | 储能出货量高估/低估10%对应收入波动约8%; 具体ASP和市场比价 |
| 动力电池系统 | 营业收入 | CNY mn | 316506.37 | 361000.0 | 405000.0 | 445500.0 | 2025年出货541GWh，ASP 585元/kWh；2026E出货+20%, ASP-5%; 2027E出货+15%, ASP-3%; 2028E出货+10%, ASP-3% | analyst_estimate | 出货量变动1%→收入变动约1%; ASP具体价格, 分技术路线出货 |
| 储能电池系统 | 营业收入 | CNY mn | 62439.82 | 131000.0 | 200000.0 | 270000.0 | 2025年出货约120GWh, ASP 520元/kWh；2026E出货260GWh, ASP-3%; 2027E出货400GWh, ASP-3%; 2028E出货540GWh, ASP-3% | analyst_estimate | 储能出货量变动10%→收入变动约10%; 储能ASP确切变化趋势 |
| 电池材料及回收 | 营业收入 | CNY mn | 21860.94 | 24000.0 | 28000.0 | 33000.0 | 假设回收量随退役电池增加而稳步增长，金属价格温和上涨 | analyst_estimate | 金属价格变化10%→收入/利润波动约5-8%; 回收量体及金属价格弹性 |
| consolidated | 营业利润 | CNY mn | None | 110700.0 | 141750.0 | 174150.0 | 营业收入 × 营业利润率；2026E营收5400亿，营业利润率20.5%；2027E 21%；2028E 21.5% | analyst_estimate | 营业利润率变动1pp→营业利润变动约5%; 详细的费用率和投资收益预测 |
| consolidated | 归母净利润 | CNY mn | 72201.28 | 88200.0 | 113000.0 | 138000.0 | 营业利润 - 财务费用(约0.5%营收) + 其他收益 - 15%所得税 | analyst_estimate | 综合税率和财务费用的小幅变动可影响净利润数亿元; 其他收益（如政府补贴）具体金额 |
| consolidated | EPS | CNY/share | None | 19.06355165638921 | 24.423824684489574 | 29.827325720881074 | parent net profit (CNY mn) / diluted shares (mn) | calculated | 股本变动(+/-1%)→EPS反向变动约1%; 股权激励可能带来的摊薄 |
| consolidated | 经营现金流OCF | CNY mn | 133200.0 | 123480.0 | 158200.0 | 193200.0 | 假设OCF/净利润比率为1.4x (基于历史数据1.62-1.84之间，保守取1.4) | analyst_estimate | 营运资本变动将使实际OCF大幅偏离假设; 具体应收账款和存货周转天数预测 |
| consolidated | 资本支出CAPEX | CNY mn | None | None | None | None |  | missing | ; 2025年及未来资本支出计划金额，需从现金流量表购建固定资产项目获取 |
| consolidated | 自由现金流FCF | CNY mn | None | None | None | None | FCF = OCF - CAPEX，但CAPEX缺失 | missing | ; CAPEX数据 |
| consolidated | gross_margin |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | 储能电池 | segment_volume | None GWh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline storage volume for 2025, share count |
| KPE02 | consolidated | asp_or_price | None CNY/ton | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | VC采购价格对成本的量化影响, VC在BOM中的占比 |
| KPE03 | 钠电储能 | segment_volume | None GWh | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 钠电业务成本与毛利率, 2027年出货量预测 |
| KPE04 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | AIDC业务收入预测, 资本开支 |
| KPE05 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | rejected: no model, valuation, rating, or sizing impact | 与宁德时代直接关联缺失 |
| KPE06 | consolidated | cost | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 矿山产量, 对公司碳酸锂自供比例的影响 |
| KPE07 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | rejected: no model, valuation, rating, or sizing impact | 与宁德时代直接关联缺失 |
| KPE08 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | rejected: no model, valuation, rating, or sizing impact | 与宁德时代直接关联缺失 |
| KPE09 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 公司动力电池出货量具体增速, 公司储能出货量具体值 |
| KPE10 | 电池回收 | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 回收业务规模, 政策对利润的具体影响 |
| KPE11 | 动力电池 | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 具体需求数据 |
| KPE12 | 储能电池 | scenario_probability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | 概率变化具体数值 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-06T09:22 | 高时效/0天 | 未披露 | 价格方面，碳酸锂短期震荡，产业链龙头Q2盈利水平预计依旧亮眼，铜箔、隔膜、铝箔等二轮涨价近期有望落地，估值已回调至27年15xPE，Q3旺季行情确定，首推宁德时代、亿纬锂能等，重点看好恩捷股份、佛塑科技、璞泰来、鼎胜新材、科达利、富临精工、天赐材料、湖南裕能等价格弹性和优质材料龙头标的，关注诺德股份、嘉元科技等，同时继续碳酸锂价格弹性，看好优质龙头赣锋锂业、盛新锂能、大中矿业、国城矿业、永兴材料、中矿资源等 | 价格方面，碳酸锂短期震荡，产业链龙头Q2盈利水平预计依旧亮眼，铜箔、隔膜、铝箔等二轮涨价近期有望落地，估值已回调至27年15xPE，Q3旺季行情确定，首推宁德时代、亿纬锂能等，重点看好恩捷股份、佛塑科技、璞泰来、鼎胜新材、科达利、富临精工、天赐材料、湖南裕能等价格弹性和优质材料龙头标的，关注诺德股份、嘉元科技等，同时继续碳酸锂价格弹性，看好优质龙头赣锋锂业、盛新锂能、大中矿业、国城矿业、永兴材料、中矿资源等 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-01T12:41 | 高时效/5天 | 未披露 | 我们预计26年储能出货250-300GWh，同比翻番以上增长，全球市占率有望进一步提升 / [爱心]盈利预测与投资建议：公司出货量稳步提升、盈利水平稳定，业绩增长确定性好，我们预计26-28年归母净利润962/1215/1469亿元，同增33%/26%/21%，对应PE 20/16/13x | [爱心]盈利预测与投资建议：公司出货量稳步提升、盈利水平稳定，业绩增长确定性好，我们预计26-28年归母净利润962/1215/1469亿元，同增33%/26%/21%，对应PE 20/16/13x / 给予26年30x PE，对应目标价632元，继续强推！ [爆竹]风险提示：盈利能力不及预期，海外贸易政策变化等 | target_price=632元 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 机构未识别/2026-06-26T08:16 | 有效窗口/10天 | 推荐措辞（非标准评级） | 太阳所以在明年永太需要向宁德提供2.6w吨vc太阳目前vc属于紧缺水平，价格已经来到15w左右，预计这次订单，将给永太带来超预期的利润和收入 / 预计今年三季度的新2w产能会立刻对公司本年度利润做贡献 | 结合公司其余锂电材料的产能，目前公司估值看27年 5x左右 | rating=推荐措辞（非标准评级） | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 机构未识别/2026-06-24T17:12 | 有效窗口/12天 | 未披露 | 宁德时代预计今年有1万辆电动汽... 宁德时代预计今年有1万辆电动汽... 宁德时代预计今年有1万辆电动汽车安装钠离子电池 Images: | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI05 | 机构未识别/2026-06-24T08:13 | 有效窗口/12天 | 未披露 | 首批钠电储能解决方案，在中国市场将于2026年9月开始交付，预计到2026年底实现1GWh出货量 / 全球市场预计于2027年6月启动交付 | 钠电更新：宁德时代欧洲储能钠电... 钠电更新：宁德时代欧洲储能钠电... 钠电更新：宁德时代欧洲储能钠电发布会，capex提升到200GWh-6.23 宁德时代发布天恒钠电储能系统 6.22晚间，宁德时代在欧洲举办发布会，正式发布天恒钠电储能系统，系统在25℃环境下循环寿命超过15000次（70% SOH），在-20℃环境下仍可保持92%以上可用能量，在45℃高温环境下循环寿命超过10000次，电芯膨胀率降低40%，提供更高的安全性和可靠性，以500MWh、4小时储能项目为例，该技术可减少超过100万欧元非... | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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