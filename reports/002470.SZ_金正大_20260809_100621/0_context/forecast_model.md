# Forward Forecast Model Scaffold for 002470.SZ as of 2026-08-08

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 2955561439.94 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 11.1792% / -0.75pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.2586% / +0.17pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 9.7878 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 10.1266% / +2.35pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 23.8269% / -3.54pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 复合肥及磷化工 (Compound fertilizer & phosphor-chemical) revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 境外业务 (Overseas business) revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 磷石膏制酸/技改项目 (Phosphogypsum-to-acid technical improvement) revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| 复合肥及磷化工 (Compound fertilizer & phosphor-chemical) | period=FY2025 / Q1-2026; revenue=9915868845.35 CNY; revenue_weight=None%; growth=None%; gross_margin=11.1792% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 境外业务 (Overseas business) | period=FY2025; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 磷石膏制酸/技改项目 (Phosphogypsum-to-acid technical improvement) | period=2026; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 复合肥及磷化工 (Compound fertilizer & phosphor-chemical) | revenue_weight=None%; growth=None%; gross_margin=11.1792%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 境外业务 (Overseas business) | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 磷石膏制酸/技改项目 (Phosphogypsum-to-acid technical improvement) | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | 化肥业务：2026年销量和ASP同比变动趋势是什么？经销体系去库存进度如何？; 利润池：若减值计提完毕，2027年最悲观的经营利润中枢是多少？; 竞争：新洋丰等竞对为何能维持20%毛利率，金正大差距是成本、产品结构还是管理效率？; 现金流：不考虑外部融资，仅靠经营现金流能否支持1.5亿技改支出和偿还到期债务？ |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | 国内化肥是决定生死的基本盘，收入占比约85-90%，其毛利率和减值控制决定2027-2028年能否扭亏。境外业务虽超10%但透明度极低，短期难以估值，但若境外高毛利则可能提升合并利润。技改和磷酸铁是改变成长性预期的变量，但需要看到明确投产和订单才能计入核心价值，当前仅作为期权。 |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | 金正大的核心困境在于行业产能过剩和同质化竞争中，没有建立足够的成本壁垒或品牌溢价。新洋丰等企业凭借磷矿原料自给和聚焦高毛利专用肥实现了差异化，而金正大仍依赖经销商销售大路货，议价权弱。在原料上涨周期中，这种劣势被放大。替代品方面，水肥一体化和小型掺混站正在侵蚀传统复合肥需求，未来只有具备技术服务和整套解决方案能力的企业才能胜出。金正大虽然有农化服务布局，但复盘其销售费用和毛利率，尚未转化为经济回报。 |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | 我们判断2026H1巨额亏损中至少70%来自非现金减值，但这一定性分析需要半年报减值附注来证实。若假设为真，则2027年减值大幅下降是大概率事件，使归母净利从-5亿收窄至盈亏平衡。盈利修复的幅度和速度是我们预测中最大的不确定性。技改和磷酸铁项目的量化需要公司给出资本预算和预期收益，在此之前只能设为期权。 |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | 市场给予的估值（PE 172x，PB 3.01且处于87.3百分位）反映出两类预期：其一为减值后净资产缩水但尚可维持经营，其二为潜在重组或资产注入带来的壳价值。我们的基础情况估值（1.5-1.75元）显著低于现价1.95元，意味着当前股价隐含了较强的重组或新业务成功预期。若下半年没有明确的重组进展或技改突破，这一预期差可能通过股价修正来弥合。 |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | 即使2026H1为一次性亏损，化肥行业长期产能过剩和原料价格波动是不容忽视的结构性逆风；公司过去多年未能证明其盈利能力恢复，给予15x PE或3x PB的基础估值可能过于乐观。; 公司可能隐藏更大的债务问题，如果到期债务无法续借，现金流断裂可能使其破产清算，届时股权价值归零，远非0.5元/股。; （反转）尽管2026年巨亏，但经营现金流维持在正数，且控股股东持股约30%，具备潜在重组动力；若有国资或产业资本介入，壳价值或大幅提升，股价弹性极大。 |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | 当前盈利极度低迷，PE失去锚定；我们采用场景化PB/PE方法，将公司价值拆分为经营恢复后的盈利倍数和残余的壳价值。基础情形2028年预计实现1亿净利润，基于同行稳定期15倍PE计算经营价值1500百万元（每股0.46元），但这未反映剩余资产的清算或壳溢价。市场实际交易在高于经营价值3-4倍的水平，这部分溢价对应不确定的重组或资产注入期权，已在加权中通过bull/base/bear场景考虑。加权后每股价值约1.65元，低于市价1.95元，表明当前价格风险报酬比不具吸引力，除非获得颠覆性利好证据。 |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | 金正大是一家拥有国内最大复合肥产能之一的老牌农资企业，但受制于行业产能过剩、原料成本高企、历史滑痕及减值风暴，公司处于从财务废墟中恢复的早期阶段。短期看，2026年的大额减值将彻底压制利润，但可能出清历史包袱；中期看，2027-2028年若原料平稳或技改落地，具备盈利恢复的弹性；长期看，粮食安全政策提供需求底部支撑，但估值已隐含较多重组的乐观预期。建议重点跟踪半年报减值明细、技改立项文件及债务到期安排，等待权责清晰的经营拐点出现。 |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 2955561439.94 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 11.1792% / -0.75pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 0.3871% / +0.01pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.2586% / +0.17pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 9.7878 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | valuation | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / impairment: 2026年一季度报告: 财务费用 37,197,918.29 25,564,076.71 45.51% 投资收益 11,473,763.50 669,944.44 1612.64% 信用减值损失 -4,794,842.46 2,84... |
| EV031 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度, 上年同期 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / inventory: 2026年一季度报告: （3）报告期，投资收益较上年同期增加1612.64%，主要系本期公司对联营企业的投资收益较上期增加所致； （4）报告期，信用减值损失较上年同期增加268.53%，主要系本期公司计提的坏账增加所致； （5）... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 其他债权投资 长期应收款 长期股权投资 919,702,876.41 925,561,279.00 / long_term_equity_i... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 财务费用 37,197,918.29 25,564,076.71 45.51% 投资收益 11,473,763.5... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度, 上年同期 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 2026年一季度报告: （3）报告期，投资收益较上年同期增加1612.64%，主要系本期公司对联营企业的投资收益较上期增加所致； （4）报告期，信用减值损失较上年同期增加268.53%，主要系本期公司计提的坏账增加所致； （5）报告期，资产减值损失较上年同期增加192.77%，主要系本期公司存... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 划、“十三五”、“十四五”国家重点研发计划、山东省重点研发计划等 80 余项国家级和省部级重大科研项目... |
| EV040 | company_events | research_context | reported | valuation | unspecified | / earnings guidance / performance preview / 1 / |
| EV041 | company_events | research_context | reported | valuation | 20260715, 2026, 半年 | / 20260715 / earnings guidance / performance preview / 002470.SZ / 金正大 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002470&announcementId=1225424823&orgId=9900014252&announcementTime=2026-07-15 / |
| EV052 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 172.097 / earnings multiple the market is paying now / |
| EV053 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 0.6089 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 10.1266% / +2.35pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 复合肥及磷化工 (Compound fertilizer & phosphor-chemical) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY2025 / Q1-2026; reported revenue=9915868845.35 (CNY); revenue weight=None%; growth=None%; gross margin=11.1792%; margin change=-0.75pp; source=earnings_model; company_business_model; mode=llm_semantic |
| 境外业务 (Overseas business) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY2025; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 磷石膏制酸/技改项目 (Phosphogypsum-to-acid technical improvement) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 6407754015 / current equity value / / / PE TTM / 172.097 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
OFFICIAL_GUIDANCE_DISCLOSURE: target=002470.SZ; source_scope=company_announcement; numeric_record_status=missing
| supplied official evidence | required model treatment |
| --- | --- |
| / 20260715 / 002470.SZ / 金正大 / 2026年半年度业绩预告 / http://www.cninfo.com.cn/new/disclosure/detail?stockCode=002470&announcementId=1225424823&orgId=9900014252&announcementTime=2026-07-15 / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 1、业绩预告期间：2026 年 1 月 1 日至 2026 年 6 月 30 日 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - 扣除非经常性损益 | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
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
- Readiness reasons: 分产品/分地区收入、成本及毛利率拆分缺失；仅境外收入占比>10%触发披露，但无具体数值; 2026H1业绩预告录得4.5-5.5亿净亏损，但Q2单季亏损构成及性质（减值/主营）未公开; 资本开支、在建工程转固、技改投资、产能利用率、ROIC等关键运营及再投资指标难以量化; 无法从结构化数据中提取净资产及有息负债明细，PB-ROE及信用风险评估受限; 磷酸铁前驱体等项目处于建设期，无投产时间、产能、客户及利润贡献信息; 部分财务比率仅Q1可用，全年预测依赖不完整季节性推断; Material transaction economics are present but legal ownership, attributable consideration, cash received and retained/disposed rights were not reconciled.; One or more filing-reported segments required deterministic restoration.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 收入=∑(各产品线销量×ASP)；主营业务收入约99.2亿(FY2025)；境外销售占比>10%
- Profit: 利润=收入-原料成本(占成本>80%，主要为氮磷钾及硫磺)-能源/制造费用-销售/管理/研发费用-财务费用-信用减值/资产减值+投资收益；FY2025扣非归母净利-16.1m，归母净利34.6m，毛利率~11%
- Cash flow: 经营现金流=净利润+折旧摊销±营运资本变动；FY2025 OCF 455.7m；Q1 2026 OCF/净利润达9.79倍
- Reinvestment: 资本支出集中于技改（硫磺制酸/磷石膏制酸）和在建项目（磷酸铁正极前驱体），历史CAPEX金额未知，中等资本密集度

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 2026H1预计净亏损4.5-5.5亿元，其中主营业务亏损、信用减值、资产减值及其他非经常事项分别贡献了多少？ | 已知Q1投资收益+1612%支撑部分利润，信用减值增加268%，资产减值损失增加193%，但具体分项金额未披露。H1预告净利润为负且同比下降474%-602%。 | 2026E asset_impairment, 2026E credit_impairment, 2026E operating_profit_ex_impairment | 归母净利润, 净资产, EPS | 2026年半年度报告及利润表附注, 减值明细：应收账款坏账准备、存货跌价准备、商誉/长期资产减值具体科目; 公司发布2026年半年度报告时，拆分半年度利润表各项目，并与上年同期对比 |
| Q2 | 硫磺制酸改造为磷石膏制酸的技改项目能否在2027年前落地，预计可降低多少原料成本，对毛利率的拉动幅度有多大？ | 公司表示持续跟踪硫磺价格走势，将综合考虑市场及生产经营情况推进相应技改，未给出时间表或投资预算。 | 2027E gross_margin, 2027E capex, 2028E gross_margin | 营业成本, 毛利率, 资本支出 | 技改投资预算, 预期单吨硫酸成本节约金额, 董事会立项审批文件或投资者交流纪要; 持续跟踪互动易问答、董事会决议公告，关注是否出现技改立项的相关表述 |
| Q3 | 磷酸铁电池正极前驱体材料建设项目当前工程进度如何，预计何时投产，市场供需和潜在盈利能力如何？ | 目前项目正在建设中，尚未投产，公司提示投资风险。 | project_capex, project_commencement_date, project_expected_roic | 在建工程, 资本支出, 未来营业收入及利润 | 项目可研报告或环评公示数据, 设备采购和工程进度节点, 与下游客户的送样验证信息; 关注公司重大项目进展公告，或者向董秘办求证预计中交/投料试车时间 |
| Q4 | 当前真实自由现金流能否覆盖利息和到期债务？公司偿债压力和再融资风险有多大？ | Q1经营现金流约1.12亿（基于Q1 OCF/净利润9.79倒推），但净利润基数极小。财务费用同比增加45.5%。整体杠杆水平不明。 | 2026E OCF, 2026E interest_expense, 2026E total_debt | 经营活动现金流净额, 筹资活动现金流, 资产负债率 | 资产负债表：短期借款、一年内到期非流动负债, 现金流量表：偿还债务支付的现金, 授信及再融资额度; 2026半年报公布后，分析现金流科目和偿债指标 |
| Q5 | 境外业务的具体收入规模、毛利率和客户集中度是怎样的？是否有集中违约或汇率敞口风险？ | 仅披露境外业务营收或净利润占比超过10%，但未公布具体数额。 | overseas_revenue, overseas_gross_margin, overseas_receivables | 营业收入, 毛利, 应收账款, 汇兑损益 | 分地区收入及营业利润, 主要出口国家和客户名称, 结算货币及套保策略; 年度报告附注中“地区分部”信息，或在深交所互动易询问境外销售详情 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业收入 | CNY mn | 9915.87 | 9900.0 | 10050.0 | 10200.0 | base + growth rate; 2026E flat due to demand rigidity and price competition, 2027E/2028E low single-digit growth from demand expansion and mix improvement | analyst_estimate | 农产品价格和政策补贴; 分产品量价拆分为未证实假设, 管理层收入指引缺失 |
| consolidated | 毛利率 | % | 11.18 | 10.5 | 12.0 | 12.5 | base adjusted by raw material cost pressure in 2026E, recovery from tech improvement and cost pass-through in 2027E/2028E | analyst_estimate | 氮磷钾/硫磺价格、技改进度; FY2025全年毛利率未单独提取, 原料价格走势和采购策略不明 |
| consolidated | 营业利润 | CNY mn | None | -420.0 | 50.0 | 150.0 | revenue * operating_margin (including impairment); 2026E heavy impairment drives large loss; 2027E normalize; 2028E modest profit | analyst_estimate | 减值计提金额及投资收益; FY2025营业利润实际数, 2026年减值损失分项预测 |
| consolidated | 归母净利润 | CNY mn | 34.6 | -500.0 | -30.0 | 100.0 | after interest, tax and minority interest; 2026E includes ~500 mn impairment loss from H1 guidance; 2027E gradual recovery; 2028E return to profitability | analyst_estimate | 减值转回/新增、主业毛利率; 2026H2业绩趋势和减值估计, 所得税率和少数股东权益 |
| consolidated | 基本每股收益 | CNY/share | 0.0105 | -0.15215939902149941 | -0.009129563941289965 | 0.030431879804299882 | parent net profit (CNY mn) / diluted shares (mn) | calculated | 归母净利润水平和股本变动; 潜在稀释证券（可转债、期权）未知 |
| consolidated | 经营活动现金流净额 | CNY mn | 455.73 | 200.0 | 250.0 | 350.0 | net_income + depreciation/amortization +/- working capital; OCF remains positive despite losses due to non-cash impairment | analyst_estimate | 应收账款回收和库存变现速度; 折旧摊销金额无单独披露, 营运资本变动假设 |
| consolidated | 资本支出 | CNY mn | None | None | None | None | missing; no capex data extracted from filings or management_allocation | missing | 技改和磷酸铁项目投资进度; 购建固定资产、无形资产支付的现金历史值 |
| consolidated | 自由现金流 | CNY mn | None | None | None | None | OCF - capex; capex missing | missing | CAPEX控制; 资本支出数据 |

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