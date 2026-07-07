# Forward Forecast Model Scaffold for 300476.SZ as of 2026-07-07

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 5519485066.85 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 34.4585% / +1.08pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.8924% / +1.23pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.6428 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 25.7759% / -3.07pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 17.6884% / +4.18pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Mobile service revenue | mobile subscribers x mobile ARPU | 5G penetration, package mix, churn, DOU, pricing discipline |
| Broadband / home revenue | broadband subscribers x household ARPU | gigabit penetration, smart-home attach, bundling |
| Enterprise / cloud / AI revenue | customer count x cloud/IDC/AI ARPU or project revenue | cloud growth, AI paid adoption, IDC utilization, contract liabilities |
| EBITDA / operating profit | service revenue x margin - depreciation - SG&A/R&D | network scale, cloud gross margin, depreciation, personnel and maintenance cost |
| net profit/EPS / dividend capacity | operating profit - tax/minority + FCF after capex | capex-to-revenue, OCF/NI, payout ratio, net cash/debt |

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
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 5519485066.85 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 34.4585% / +1.08pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 23.3433% / +1.99pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.8924% / +1.23pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.6428 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 9/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV030 | financial_report_intelligence | primary_or_structured_filing | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -71.39%, gross margin change -0.77pp, operating margin change 1.01pp, O |
| EV032 | industry_kpi | secondary_or_derived_research | reported | revenue | unspecified | / Mobile / mobile subscribers, 5G penetration, mobile ARPU, DOU, churn, package mix / service revenue and margin durability / |
| EV033 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | unspecified | / Capex / 5G/cloud/AI capex, depreciation, network utilization, capex-to-revenue / FCF and ROIC / |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -71.39%, gross margin change -0.77pp, operating margin change 1.01pp... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / contract_liabilities: 2026年一季度报告: 加所致。 报告期内，主要系预收货款减 合同负债 7,164,590.26 11,422,898.80 -37.28% / contract_liabilities: 2026年一季度... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction_in_progress: 2026年一季度报告: 增加所致。 报告期内，主要系扩大产能资 在建工程 5,169,689,299.24 3,609,874,903.28 43.21% / constr... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 45,872,271.81 0.00 100.00% 失以“-”号填列） 票的公允价值增加所致。 信用减值损失（损... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / construction_in_progress: 2026年一季度报告: 增加所致。 报告期内，主要系扩大产能资 在建工程 5,169,689,299.24 3,609,874,903.28 43.21% / construction_in_progress: 2026年一季度报告: 报告期内，主要系扩大产能资 ... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: PCB 厂商第 3 名。 （3）“中国+N”全球化布局，保障供应交付能力 2025 年度，公司坚定实施... |
| EV042 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| AI PCB | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY26E; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| Non-AI PCB | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY26E; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 280015045216 / current equity value / / / PE TTM / 59.8352 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: Diluted share count not available from supplied evidence; EPS and per-share metrics cannot be populated. Total equity value used for scenario valuation.; Segment revenue, margin and profit weights are analytical estimates derived from private channel evidence (KPE02, KPE06) because official segment disclosures are missing.; Capital expenditure beyond FY26 is estimated; only FY26 guidance of ~RMB 18 bn is supplied.; Working capital and cash conversion assumptions rely on a single quarter OCF/net profit ratio (Q1 2026).; Conflicts between market rumours (KPE10, KPE11) and company guidance are unresolved; scenario probabilities reflect underwriting judgement.; Material segment three-year driver lines are missing: AI PCB, Non-AI PCB; Bull/base/bear per-share valuation is incomplete.; Valuation has not closed from mutually exclusive buckets to per-share fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 收入 = Σ (各工厂产能 × 利用率) × 产品结构ASP × (1-退换率); 总ASP受产品组合（高端AI vs 普通）和成本传导机制影响
- Profit: 营业利润 = 收入 - 原材料成本(覆铜板、铜箔等) - 人工及制造费用 - 研发/销售/管理费用; 核心毛利率由产品结构、良率和原材料成本决定，运营杠杆来自规模效应和产能爬坡
- Cash flow: OCF = 净利润 + 折旧摊销 ± 营运资本变动; FCF = OCF - 资本支出; 典型成长期资本支出巨大，FCF可能为负，但产能释放后现金回收加快
- Reinvestment: 重资产制造，单位收入需持续投入产能建设与设备；FY26资本支出指引约人民币180亿元，主要用于惠州工厂10/11及后续项目；折旧压力随产能转固逐步上升

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ01 | AI PCB部门的ASIC/GPU收入组合及V8 TPU渗透速度如何？ | 公司目标ASIC/GPU收入各占50%，并预计2026年底前进入V8 TPU供应；当前证据来自管理层路演，未披露含具体数字的合同。 | segment_volume (AI PCB), ASP/mix (AI PCB) | consolidated revenue, parent net profit, EPS | 正式订单公告, V8 TPU的PCB价值量测算; CSP的TPU路线图更新或胜宏的供应商资质确认公告 |
| UQ02 | Rubin Ultra平台正交背板是否真的延迟，延迟对胜宏的远期收入冲击有多大？ | Jefferies称正交背板推迟至2028年，2027年Kyber出货概率极低；胜宏认为进度未延迟，正在评估多种材料方案。冲突未解决。 | segment_volume (AI PCB) in 2027E/2028E | consolidated revenue 2027E-2028E, parent net profit, FCF | NVIDIA Rubin Ultra官方硬件路线图, 胜宏在正交背板上的预估订单值; NVIDIA GTC或官网架构发布，Q2 FY27供应链核实 |
| UQ03 | FY26资本支出180亿元能否在FY27-FY28实现产能转化为收入，回报（ROIC）何时能达到可接受水平？ | 管理层指引工厂10/11主要2026年建设，工厂12/13后续；产能爬坡通常需要数季度，大规模贡献可能从FY27开始。 | capacity / utilization, revenue growth FY27-28, capex / depreciation, FCF | fixed asset depreciation, operating margin, OCF/FCF, ROIC | 工厂级产能、投资回收期测算, 折旧政策明细; 2026中报或全年折旧新增额，管理层对爬坡节奏的更新 |
| UQ04 | 英伟达是否真正实施PCB降价10%，公司能否通过成本传导和产品组合维持毛利率？ | 市场传闻叠加公司否认；管理层表示原材料成本稳定且新一代产品成本传导顺畅，FY26毛利率与FY25大致持平。 | ASP / price (AI PCB), gross margin | consolidated gross margin, operating profit, EPS | 与英伟达的实际合同条款, Q2 2026毛利率趋势; Q2 2026季度报告毛利率以及与客户的季度议价结果 |
| UQ05 | 在股份稀释风险（员工持股计划、股权激励）下，EPS增长能否跟上净利润增长？ | 已公布员工持股计划框架，具体股本影响未知；过往存在定向增发计划（2025年注册稿）。 | diluted share count | EPS, per-share valuation | 员工持股计划的具体执行时间、价格及股份数量, 定向增发最新进展; 公司公告员工持股计划实施结果或定向增发发行结果 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | revenue | CNY mn | 19292.31 | 27600.0 | 35900.0 | 44900.0 | FY26=FY25×(1+43%) driven by AI ramp; FY27+30%, FY28+25%; incorporates KPE02 revenue share targets and capacity expansion | analyst_estimate | AI PCB volume and ASP;  |
| consolidated | cost_of_sales | CNY mn | 12848.0 | 18080.0 | 23520.0 | 29634.0 | Revenue × (1 - gross margin); FY25 GM ~33.4% (implied from Q1 YoY), FY26E 34.5%, FY27E 34.5%, FY28E 34.0% | analyst_estimate | Gross margin;  |
| consolidated | gross_profit | CNY mn | 6444.31 | 9520.0 | 12380.0 | 15266.0 | Revenue - COS | calculated | ;  |
| consolidated | gross_margin | % | 33.4 | 34.5 | 34.5 | 34.0 | Gross profit / revenue; FY25 estimated from Q1 2025 implied 33.38%; FY26 guided flat, FY27 stable, FY28 slight compression from depreciation | analyst_estimate | ASP vs input cost;  |
| consolidated | operating_profit | CNY mn | 4919.0 | 7590.0 | 9693.0 | 11899.0 | Revenue × operating margin; FY25 ~25.5% (implied Q1 2025), FY26 27.5%, FY27 27.0%, FY28 26.5% | analyst_estimate | Operating leverage and depreciation;  |
| consolidated | operating_margin | % | 25.5 | 27.5 | 27.0 | 26.5 | Operating profit / revenue; FY25 estimated from Q1 2025 (25.31% + 1.91pp gives 27.22% Q1 2026); FY26 slightly above Q1 on scale, then gradual normalisation | analyst_estimate | SG&A and R&D efficiency;  |
| consolidated | parent_net_profit | CNY mn | 4312.0 | 6210.0 | 7719.0 | 9205.0 | Revenue × net margin; FY25 ~21.5% (implied), FY26 22.5%, FY27 21.5%, FY28 20.5% | analyst_estimate | Finance cost, tax rate, non-recurring items;  |
| consolidated | net_margin | % | 21.5 | 22.5 | 21.5 | 20.5 | Parent net profit / revenue; FY25 estimated from Q1 2025 21.35%; FY26 improved by mix, then gradually mean-reverting | analyst_estimate | Interest expense and effective tax rate;  |
| consolidated | eps | CNY per share | None | None | None | None | Parent net profit / diluted shares; diluted shares unavailable | missing | share count; diluted share count |
| consolidated | ocf | CNY mn | 5174.0 | 7452.0 | 8800.0 | 10200.0 | Parent net profit × OCF/NI ratio; FY25 ~1.20x, FY26-28 gradually moderating to 1.15x | analyst_estimate | working capital management;  |
| consolidated | capex | CNY mn | 8000.0 | 18000.0 | 12000.0 | 8000.0 | FY26 = management guidance ~RMB 18 bn (KPE02); FY27-28 assumed step-down as major factories complete | analyst_estimate | Company capacity expansion roadmap; FY27 and FY28 exact capex plans |
| consolidated | fcf | CNY mn | -2826.0 | -10548.0 | -3200.0 | 2200.0 | OCF - Capex; heavy investment period turns FCF-negative until FY28 | calculated | capex and OCF conversion;  |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | capital_allocation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Verify actual repurchase progress and dilution impact in subsequent filings. | Share count base, Employee plan details (price, duration) |
| KPE02 | AI PCB | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Check quarterly margin reports for sustained gross margin stability. | Quantified ASP change, Exact gross margin delta per product line |
| KPE03 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Monitor capacity utilization disclosures and order backlog comments in next earnings call. | Quantified utilization rate, Order backlog value |
| KPE04 | AI PCB | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Track AI server shipment data and associated PCB orders. | Market share data, Demand growth rate |
| KPE05 | AI PCB | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Monitor industry shift to AI factory model and company's involvement. | Quantified utilization improvement, Revenue exposure to AI factory model |
| KPE06 | AI PCB | market_share | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Track Nvidia supplier lists and quarterly share disclosures from customer reports. | Current market share %, Revenue base for share calculation |
| KPE07 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Not a fundamental catalyst; noise. | none |
| KPE08 | AI PCB | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Check for adoption of third-party inspection equipment; low materiality for core thesis. | Volume or value of detection contracts |
| KPE09 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Confirm company-specific price increase announcements and customer acceptance. | Company-specific price change, Impact on volume/mix |
| KPE10 | AI PCB | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Monitor Q2 2026 ASP and margin; check for any contract renegotiations. | Quantified ASP change if true, Company's cost pass-through ability |
| KPE11 | AI PCB | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Track Nvidia Rubin Ultra official timeline and company-specific exposure. | Company-specific revenue at risk, Mitigation through other products |
| KPE12 | consolidated | revenue | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Low materiality; indicates supply chain depth but not revenue driver. | none |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-02T08:11 | 高时效/5天 | 未披露 | 📊 因此，它预计FY26（2026财年）毛利率与FY25（2025财年）大致持平，而AI收入占比应从低于50%提升至60-70%，产出价值从2025年的350亿元人民币增长到2030年的约3-4倍 / 🌐 除了关键GPU客户外，VGT正在向更多ASIC（专用集成电路）客户多元化拓展，并目标是ASIC/GPU收入占比达到50/50，因为ASIC设计也正从HLC（高密度互连板）转向HDI | 💰 FY26资本支出（capex）指引约为180亿元人民币，其中约150亿元用于惠州的工厂10和11 | 2025E_收入=50 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 摩根大通/2026-06-30T18:57 | 高时效/7天 | 未披露 | 涨停板：锐捷网络、星网锐捷、长光华芯、铭普光磁、紫光股份、联创电子、共进股份、光电股份、 其他强势股：胜宏科技、太辰光、源杰科技、菲菱科思、瑞斯康达 算力租赁 ①DeepSeek官宣正式版V4将于7月中旬正式上线，并宣布API服务引入峰谷定价策略，其中高峰价格为平时价格两倍(12元/百万tokens),而平时价格与先行V4API定价一致 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 中信电子/2026-06-17T21:12 | 有效窗口/20天 | 推荐措辞（非标准评级） | 礼物由此我们判断26Q3 PCB厂商有望释放更强的业绩增长动能，27/28年业绩能见度有望进一步强化，盈利预测及估值水平仍有进一步提升空间，重点推荐：沪电股份、胜宏科技、深南电路、生益科技、兴森科技 | 礼物由此我们判断26Q3 PCB厂商有望释放更强的业绩增长动能，27/28年业绩能见度有望进一步强化，盈利预测及估值水平仍有进一步提升空间，重点推荐：沪电股份、胜宏科技、深南电路、生益科技、兴森科技 | rating=推荐措辞（非标准评级） | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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