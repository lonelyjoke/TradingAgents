# Forward Forecast Model Scaffold for 603986.SH as of 2026-07-19

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 4188075574.04 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 57.0767% / +19.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 2.3047% / +6.54pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.2202 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 1.7479% / -1.83pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 20.3043% / -11.89pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| consolidated revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Semiconductor Forecast And Valuation Controls
- Semiconductor profile: semiconductor equipment / wafer-fab tools. Use this profile before consumer, generic technology, telecom, metals, or battery templates.
| control | Mandatory treatment |
| --- | --- |
| Business buckets | split mature/core products from product-cycle, technology-node, customer, or tool-category optionality; do not bury optionality inside the base multiple |
| Operating bridge | start from sector-native volume x ASP x mix, then explicitly bridge gross margin, R&D, working capital, capex and share count |
| Foundry / manufacturing | use wafer capacity, utilization, wafer ASP, node mix, yield, depreciation, capex, construction-in-progress transfer, and equipment access |
| Chip design | use shipments, ASP, design wins, tape-out/mass-production milestones, customer concentration, foundry/package cost, inventory and R&D/IP moat |
| Semiconductor equipment | use new orders, backlog, delivery/acceptance, tool-category mix, localization rate, installed base/service, inventory, advances and receivables |
| Valuation triangulation | PE is only one cross-check. Also show EV/EBITDA, DCF/FCF, ROIC/PB or SOTP/NAV depending on asset intensity and disclosure |
| Optionality discipline | AI, advanced node, localization or strategic-scarcity value must have explicit probability, payoff, verification gate and overlap key; unverified optionality cannot enter base value |
| Market-implied check | reverse current market cap into required revenue, gross margin, net profit, ROIC, backlog conversion or node/product contribution; compare with the model |
- A semiconductor Buy/Underweight call is incomplete if it relies only on static PE/PB or valuation percentiles without the operating bridge above.

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| consolidated | period=2026H1; revenue=1150000.0 万元; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| consolidated | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | 1. 存储：SLC NAND涨价幅度与持续性？公司产能与客户库存如何？; 2. MCU与传感：何时显著贡献利润？能否在存储下行时提供缓冲？; 3. 毛利率：成本端晶圆代工是否会侵蚀涨价收益？研发费用率趋势？; 4. 现金流：强劲OCF如何分配？并购、回购还是分红？ |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | 存储器业务主导当前利润池，贡献可能超过80%的毛利；MCU是第二增长曲线但规模仍小；传感器和模拟属于种子业务。因此，估值弹性的90%来自存储价格假设，10%来自MCU复苏的超预期。 |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | 公司主要竞争对手包括旺宏、华邦、普冉股份等。NOR Flash领域国内有普冉、恒烁等，竞争激烈但公司凭借大容量和车规产品保持领先。SLC NAND领域，海外巨头退出，公司成为少数本土供应商，短期无强劲对手。MCU领域意法半导体、瑞萨等国际巨头主导，公司靠性价比和替代切入。长期看，晶圆厂可能扶植其他设计公司或自建设计能力，构成潜在替代威胁。 |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | TrendForce的SLC NAND涨价预测来自行业调查，但公司实际受益程度取决于合约价/现货价结构、成本端晶圆价格变化。目前定性结论是强利好，但无法量化到收入增量精确值。需获取公司SLC NAND出货量基线、晶圆采购价、历史价格弹性，才能建立从行业价格到公司EPS的回归模型。 |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | 当前市值3250亿元，隐含TTM盈利仅28.75亿（PE 113x）。而公司H1预告已实现69亿净利，市场显然没有线性外推H1业绩，担忧下半年价格回落或非经常性不可持续。若2026年全年实现120亿净利，对应市盈率仅2.7倍（按当前市值），存在巨大预期差。但若市场定价周期均值回归，则合理PE应用2028年正常化利润68亿，约47倍，仍高于历史中枢，说明当前估值已包含一定溢价。Gap核心在价格持续性。 |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | 牛市反方：存储周期历史上从未超过2年，此次涨价已持续超过1年，产能正在回归，2027年大概率过剩；即使今年赚120亿，未来几年可能回落到20-30亿，应给8-10倍周期底部利润估值，目标市值仅160-300亿，远低于当前。; 熊市反方：AI需求是结构性的，海外巨头永久撤出利基市场，公司已成为主要供应商，有机会维持盈利能力在40%毛利率以上，周期中枢抬高，可给15-20倍估值。 |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | 采用场景加权PE法，核心业务2026E净利120亿（基准），赋予12倍PE（对应存储周期峰值合理倍数），得出核心价值1440亿元。牛市给予15倍，熊市8倍。加权价值=0.5*1440 + 0.25*1800 + 0.25*640 = 1330亿元。长鑫科技股权作为期权价值另计。但当前市值3250亿，显著高于任何合理估值情景，可能反映市场对公司进入新成长阶段的乐观预期，或大量散户资金推动。需谨慎。 |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | 兆易创新正处于存储超级周期的利润爆发期，2026年净利润有望突破百亿。然而，市场定价已远超周期顶部合理估值，显示投资者可能将短期暴利线性外推，忽视了存储价格的强周期性和未来均值回归风险。投资决策应聚焦于价格拐点的领先指标（渠道库存、海外产能重启、客户下单放缓），并在周期高峰时保持谨慎估值，而非追高。 |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | unit cost / gross margin | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE07 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 4188075574.04 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 57.0767% / +19.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 34.8907% / +22.60pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 2.3047% / +6.54pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.2202 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2024, 半年 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 兆易创新2024年半年度报告: 473,449,975.70 275,474,715.87 71.87 性损益的净利润 经营活动产生的现金流量净额 1,248,715,713.30 644,561,466.59 9... |
| EV031 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2024, 半年 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 兆易创新2024年半年度报告: 473,449,975.70 275,474,715.87 71.87 性损益的净利润 经营活动产生的现金流量净额 1,248,715,713.30 644,561,466.5... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2024, 半年 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction_in_progress: 兆易创新2024年半年度报告: 或与设计或合同要求基本相符。 在建工程的减值测试方法和减值准备计提方法详见本节五、27 “长期资产减值”。 23. 借款费用 / const... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2024, 半年 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 兆易创新2024年半年度报告: 投资活动产生的现金流量净额 94,865,632.53 -576,960,897.12 不适用 筹资活动产... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2024, 半年 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 兆易创新2024年半年度报告: 筹资活动产生的现金流量净额变动原因说明：主要是①2024 年上半年取得银行短期借款 4 亿元， 回购限制性股票及二级市场股票共支出约 1.55 亿元；②2023 年上半年支付现金股利 4.14 亿元。 资产减值损失变动原因说明：主要是存货减值 0.77 亿元，比... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | revenue | 2024, 半年, 2023 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 兆易创新2024年半年度报告: 报告期内，营业收入同比增加 21.69%，主要原因是：经历 2023 年市场需求低迷和库存逐... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |
| EV042 | company_events | research_context | reported | valuation | unspecified | / earnings guidance / performance preview / 1 / |
| EV043 | company_events | research_context | reported | valuation | 20260710, 2026, 半年 | / 20260710 / earnings guidance / performance preview / 603986.SH / 兆易创新 / 兆易创新2026年半年度业绩预增公告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603986&announcementId=1225417171&orgId=9900026561&announcementTime=2026-07-10 / |
| EV050 | company_events | research_context | reported | profit_or_eps | 2026, 半年 | 1. 公司预计 2026 年半年度归属于上市公司股东的净利润为 690,000 万元左 |
| EV054 | company_events | research_context | reported | revenue | 2026, 半年, 上年同期 | 3. 公司预计 2026 年半年度实现营业收入 1,150,000 万元左右，与上年同期 |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| consolidated | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026H1; reported revenue=1150000.0 (万元); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_events; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 325013196750 / current equity value / / / PE TTM / 113.0622 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
| / earnings guidance / performance preview / 1 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260710 / earnings guidance / performance preview / 603986.SH / 兆易创新 / 兆易创新2026年半年度业绩预增公告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603986&announcementId=1225417171&orgId=9900026561&announcementTime=2026-07-10 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 20260710 / 603986.SH / 兆易创新 / 兆易创新2026年半年度业绩预增公告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603986&announcementId=1225417171&orgId=9900026561&announcementTime=2026-07-10 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 1. 公司预计 2026 年半年度归属于上市公司股东的净利润为 690,000 万元左 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 2. 公司预计 2026 年半年度归属于上市公司股东扣除非经常性损益后的净 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 一、本期业绩预告情况 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - （一）业绩预告期间 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
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
- Readiness reasons: 分段存储/MCU/传感/模拟收入及毛利未单独披露，无法构建分业务模型; 稀释股份数未从证据中提取，EPS及每股公平价值无法计算; 资本开支历史与预测依赖不足，FCF估计缺乏基础; 长鑫科技持股仅1.8%且计入其他权益工具，经济敞口小但公允价值变动路径不透明; 2026H2及后续存储价格与销量仅存在行业预期，尚无公司层面量化传导; Required consolidated three-year forecast lines are incomplete.; Bull/base/bear per-share valuation is incomplete.; All claimed moat mechanisms remain unproven by observable evidence.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 收入 = Σ(产品出货量 × ASP)，其中存储产品（尤其SLC NAND）价格弹性极大，MCU与传感贡献更稳定的设计导入收入
- Profit: 营业利润 = 收入 - 晶圆/封测成本（先进供应商，部分自研） - 研发费用（~17%收入） - 销售管理费用 - 其他; 净利润受公允价值变动、政府补贴等非经常项目扰动
- Cash flow: 经营性现金流 = 净利润 ± 营运资金变动（应收/应付/库存） - 折旧摊销等非现金调整；历史OCF/净利约1.22x；FCF = OCF - 资本开支（主要为研发投入、IP及测试设备，无重大产能扩张）
- Reinvestment: 轻资产设计公司，资本开支强度低，研发费用是主要再投资（约17%收入），通过新产品导入和工艺迁移实现增长；无重大在建工程或制造基地

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | SLC NAND价格在2026H2-2027的上涨幅度与持续性如何？公司对此的敏感度（收入占比、成本传导）有多高？ | 行业预测上涨120-170%，公司Q2净利率已超50%，但公司未披露SLC NAND收入比重 | SLC NAND ASP, SLC NAND出货量, 毛利率 | 营业收入, 营业利润, 归母净利润 | SLC NAND收入占比及历史ASP, 公司对未来价格的定量展望; 2026年半年报或后续投资者交流中获取产品结构数据 |
| Q2 | 非经常性损益的构成与可持续性：2026H1扣非净利48.5亿 vs 归母净利69亿，差额20.5亿主要来自什么？下半年会否逆转？ | 推测包含政府补贴、投资收益、减值回转等，但公告未说明细节 | 非经常性损益, 归母净利润, 扣非净利润 | 归母净利润, EPS | 非经常性损益的具体构成, 历史非经常性损益占比; 2026年半年报明细 |
| Q3 | 公司MCU及传感器业务复苏的强度与利润率改善空间？ | MCU市场2025年触底回升，公司提及端侧定制化存储业务，但无具体财务数据 | MCU收入增长率, MCU毛利率 | 营业收入, 毛利率 | MCU与传感器的分产品收入及毛利率; 2026年半年报 |
| Q4 | 2027-2028存储周期下行时，公司利润的下降幅度及安全垫？ | 无公司指引；历史上2019年价格下行时净利率曾滑落至个位数 | 2027E ASP, 2027E销量, 毛利率 | 营业收入, 营业利润, 自由现金流 | 行业供需模型与价格预测, 公司成本结构下行保护程度; 跟踪TrendForce等机构存储预测及公司季度展望 |
| Q5 | 稀释股份数（含期权/限制性股票）为多少？ | 未获取 | diluted_share_count_mn | EPS, 公平价值每股 | Tushare total_share, 最新定向增发/回购后的股本; 从Tushare、公司公告或Wind获取最新总股本及稀释效应 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业收入 | CNY mn | 9203.46 | 24500.0 | 28000.0 | 22000.0 | 2026E: H1预告11500 + H2估算13000（季环比略增）; 2027E: 价格高位维持，量增10%；2028E: 价格回调30%，量持平假设 | analyst_estimate | 存储ASP波动10%，收入影响约±8%; 2027年后各产品具体量价假设, MCU/传感贡献度 |
| consolidated | 营业成本 | CNY mn | None | None | None | None | 收入 × (1 - 毛利率) | derived | ; 2025年毛利率起点 |
| consolidated | 毛利率 | % | 57.08 | 55.0 | 52.0 | 40.0 | 2026E: 维持高位，略低于Q1因产品结构；2027E: 价格温和下降但规模经济支撑；2028E: 回归常态，周期中枢约40% | analyst_estimate | 毛利率每变1pp，净利润影响约±245mn（2026E）; 各产品毛利率历史数据 |
| consolidated | 营业利润 | CNY mn | 1621.8 | 12000.0 | 13200.0 | 7000.0 | 收入 × 营业利润率（估算，2026E~49%，含非经常性收益；2027E 47%；2028E 32%） | analyst_estimate | ; 非经常性损益的持续性, 研发费用率假设 |
| consolidated | 归母净利润 | CNY mn | 6900.0 | 12000.0 | 13000.0 | 6800.0 | 2026E: H1 6900 + H2 5100（考虑非经常性可能减小）；2027E: 量价高位维持，微增；2028E: 价格回落至正常，扣非净利降至~60亿，归母因非经常性调整 | analyst_estimate | 归母净利润对存储价格高度敏感; 非经常性损益详细预测, 有效税率 |
| consolidated | EPS | CNY | None | None | None | None | 归母净利润 / 稀释股份数 | missing | ; 稀释股份数 |
| consolidated | 经营性现金流(OCF) | CNY mn | 1783.3 | 14640.0 | 15860.0 | 8500.0 | 归母净利润 × 1.22（参考Q1 OCF/NP比率），2026E: 12000*1.22; 2027E: 13000*1.22; 2028E: 6800*1.25（周期下行时运营资金释放） | analyst_estimate | ; 营运资金详细预测, 折旧摊销 |
| consolidated | 资本开支 | CNY mn | None | None | None | None |  | missing | ; 历史资本开支金额, 未来产能扩张计划 |
| consolidated | 自由现金流(FCF) | CNY mn | None | None | None | None | OCF - 资本开支 | missing | ; 资本开支 |
| consolidated | ocf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 跨境核验美光/海力士季度指引与TrendForce报价 | KeyBanc上调幅度具体数值, 兆易创新直接受益传导系数 |
| KPE02 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 跟踪SK海力士HBM4出货量及对利基存储产能挤压效应 | 兆易创新具体出货量数据, SK海力士产能分配细节 |
| KPE03 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 等待TrendForce正式报告及兆易创新H2产品ASP趋势 | 兆易创新SLC NAND营收占比, 当前SLC NAND价格基线 |
| KPE04 | consolidated | net_profit_parent | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | rejected: no model, valuation, rating, or sizing impact | none |
| KPE05 | consolidated | unit_cost | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 验证兆易创新在AI算力链中的实质业务贡献（MCU/存储）而非仅标签 | 兆易创新AI相关业务收入占比, 单位成本变化依据 |
| KPE06 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 检查与兆易创新业务关联度（其存储产品封装环节） | 兆易创新封装成本占比, 具体先进封装敞口 |
| KPE07 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 确认兆易创新在国产算力中的具体角色（如互联芯片或存储）并量化收入贡献 | 兆易创新算力相关产品收入, 国产算力供应链验证 |
| KPE08 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 等待正式中报披露及后续季度ASP数据 | 各产品线具体涨价幅度, 产量数据 |
| KPE09 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 观察下半年出货量及下游订单能见度 | 兆易创新订单/ backlog数据, 下游客户库存水平 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-15T08:09 | 高时效/4天 | 未披露 | 近期密集参加展会，产业普遍乐观，而且产业链的沟通交流以及上下游的耦合程度很高，下半年尤其要重视H链公司！ 🔥存储：利基存储涨价开始显现在业绩端，是“此前已涨价，涨价完整放映至Q2业绩”的 📌兆易创新Q2营收约73亿，归母净利润约54亿，扣非归母约35亿 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-15T07:31 | 高时效/4天 | 未披露 | （美股） 存储芯片：太极实业、兆易创新、普冉股份、佰维存储 四、DeepSeek筹备IPO 据媒体报道，DeepSeek 已开始筹备首次公开募股（IPO），最快可能在今年年底或 2027 年初正式递交上市申请 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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