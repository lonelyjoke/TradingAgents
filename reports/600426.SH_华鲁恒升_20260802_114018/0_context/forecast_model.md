# Forward Forecast Model Scaffold for 600426.SH as of 2026-08-02

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 8343592884.31 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 22.2802% / +5.93pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.9018% / +0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.7977 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 0.3245% / -0.20pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 4.9801% / +0.04pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 化肥产品 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 煤化工基础产品 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 化工新材料 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| 化肥产品 | period=annual filing; revenue=7305674635.46 filing table unit not explicit in extracted row; revenue_weight=100.0%; growth=0.12%; gross_margin=32.3% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 煤化工基础产品 | period=2025年报/2026Q1/KPE窗口2026-07; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 化工新材料 | period=2025年报/2026Q1/KPE窗口2026-07; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 化肥产品 | revenue_weight=100.0%; growth=0.12%; gross_margin=32.3%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 煤化工基础产品 | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 化工新材料 | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | 需求：下游农业、化纤、聚氨酯等行业的需求驱动力究竟是来自出口替代还是内需复苏？; 竞争：宝丰能源、鲁西化工等竞争对手的产能扩张和成本曲线如何演变？公司能否维持成本第一梯队？; 盈利：主要产品（甲醇、醋酸、己二酸等）的历史价差区间及当前分位数，未来回升空间几何？; 现金流：荆州项目资本开支高峰期何时结束？FCF能否在2028年大幅转正并支撑分红？ |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | 煤化工基础产品贡献当前约70%以上的收入和利润（推测），且周期性波动大，是估值核心驱动轮。化工新材料虽前景诱人，但目前体量小且不确定性高，只能作为次要利润池。化肥业务则提供稳定现金流，但增量有限。因此，投资决策应优先聚焦基础产品的价差方向和持续性，其次跟踪新材料产能释放节奏，最后考量化肥的出口弹性。 |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | 华鲁恒升在深化煤化工成本曲线方面处国内领先地位，与宝丰能源、鲁西化工构成第一梯队。宝丰立足宁东优质煤源，成本可能更低；鲁西在有机硅、己内酰胺有先发优势；公司的优势在于多品种柔性联产和德州-荆州双基地布局，抗产能过剩风险能力较强。替代方面，最大的威胁来自油头化工和海外低成本产能，但当前油价中枢上移反而强化了煤头优势。新进入者几乎被政策与资本壁垒排除。长期需警惕新能源和生物基化学品可能颠覆部分产品市场。 |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | 卖方及管理层叙事中频繁出现“底部利润30亿增至50亿”、“成本优势”、“行业景气反转”等定性观点。本模型已通过情景分析将其转化为2026E-2028E的具体利润数字。但缺乏分产品量价支撑，量化仍较粗放。例如，“成本优势”体现为毛利率从16.5%提升至21%，但每一步提升需对应到具体产品价差改善，目前尚无精确证据。后续若取得公司出厂价与原料成本的回归分析，可大幅改善量化精度。 |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | 市场当前定价PE TTM 15.9x，隐含TTM盈利37.25亿，明显低于公司2026年化利润45.4亿，说明市场并未完全定价2026年的高盈利持续性。我们的base情景2026E利润42.5亿，forward PE降至13.9x，显示估值存在折价。然而，市场可能担忧：1）2026H2需求转弱导致利润环比下滑；2）新项目回报不及预期；3）油价反转风险。因此，差距主要在于盈利可持续性和风险溢价的判断。若2026H1中报进一步确认利润高增，市场可能上调盈利预期，驱动估值修复。 |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | 针对bull论点：1）油价上行可能刺激OPEC+额外增产，且美国页岩油可能复产，油价能否维持高位存疑；2）高价化工品会吸引部分闲置产能复产，甚至刺激技术替代，破坏供给秩序；3）公司荆州项目处于需求下行通道的品种（如TDI），若投产即亏损，将拖累整体ROE。bull情景50亿利润或许过度线性外推。; 针对bear论点：1）煤化工行业资本开支已实际停滞两年，供给端刚性极强，即便需求弱，价格也不会深跌至2015年水平；2）公司持续的技改和降本能不断抬高安全垫，底部利润30亿的含金量较高；3）当前PB分位仍处25.8%低位，下行空间有限。bear情景20%概率也许偏高，实际可能仅10% |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | 采用情景PE法。该公司为周期成长公司，适用于PE估值，但需选择跨周期或forecast PE。我们以2026E为基准，给予base 15x PE，略低于历史中枢16-18x，体现周期峰位的谨慎。bull情景给予18x，反映成长溢价和景气高点；bear情景给予12x，反映周期低谷。概率加权后得到目标价24.42元，较现价21.55元有13.3%上行空间。此估值方法对盈利假设和PE倍数高度敏感，若2026E利润下调至38亿或PE倍数下调至13x，目标价将降至18元附近。 |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | 华鲁恒升是典型的低成本煤化工龙头，正处于行业景气底部反转与自身产能扩张的交汇期。投资该公司的核心问题并非它是不是好公司，而是当前价格是否对复苏给予了充分预期。我们建议投资经理关注两个验证节点：2026年中报能否证明毛利率修复已成趋势，以及荆州项目投产公告能否点燃盈利新引擎。在确认这两个信号前，可将其作为周期品贝塔配置，控制仓位；一旦信号转绿，可提升至进攻仓位并重估估值倍数。 |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE02 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 8343592884.31 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 22.2802% / +5.93pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 13.3826% / +4.29pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.9018% / +0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.7977 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 华鲁恒升2026年一季度报告: 1,112,802,620.71 703,113,957.51 58.27 经常性损益的净利润 经营活动产生的现金流量净额 890,668,396.41 930,375,592.80... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 华鲁恒升2026年一季度报告: 1,112,802,620.71 703,113,957.51 58.27 经常性损益的净利润 经营活动产生的现金流量净额 890,668,396.41 930,375,592... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 华鲁恒升2026年一季度报告: 其他非流动金融资产 投资性房地产 固定资产 32,889,707,075.45 32,993,654,001.92 / constr... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | asp_or_price | 2025, 年度 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgrade: 华鲁恒升2025年年度报告: 二、报告期内公司所处行业情况 2025 年，全球经济增长放缓，行业内卷和结构性产能过剩与需求偏弱的矛盾依然存在，化工 市场景气度较低，化工产品价格低谷震荡，企业盈... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 华鲁恒升2026年一季度报告: 净敞口套期收益（损失以“-”号填列） 公允价值变动收益（损失以“-”号填列） 9,246.58 信用减值损... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 华鲁恒升2026年一季度报告: 交易性金融资产 50,009,246.58 衍生金融资产 应收票据 36,455,065.71 18,372,770.00 / receivables: 华鲁恒升2026年一季度报告: 衍生金融资产 应收票据 36,455,065.71 18,372,770... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 华鲁恒升2025年年度报告: 数为基数，向全体股东每10股派发现金红利2.50元（含税），以资本公积每10股转增3.00股；... |
| EV045 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 15.9081 / earnings multiple the market is paying now / |
| EV046 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 1.8789 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 0.3245% / -0.20pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |
| EV010 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Inventory / revenue / 4.9801% / +0.04pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 化肥产品 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=7305674635.46 (filing table unit not explicit in extracted row); revenue weight=100.0%; growth=0.12%; gross margin=32.3%; margin change=2.4pp; source=filing_intelligence; mode=deterministic_filing_row |
| 煤化工基础产品 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年报/2026Q1/KPE窗口2026-07; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model+earnings_model+knowledge_planet; mode=llm_semantic |
| 化工新材料 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025年报/2026Q1/KPE窗口2026-07; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model+knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 59261271650 / current equity value / / / PE TTM / 15.9081 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: 缺少分产品（尤其是煤化工基础产品与新材料）的收入、成本、毛利、销量及实现价格数据; 化工新材料分部及荆州项目投产时间、资本开支、预期回报等关键数据缺失; 公司整体FY2025毛利率、营业利润、资本支出等需从完整年报补充; 商品价格映射缺失，无法通过期货数据精准推算公司产品实现价; 第三方卖方预测（如底部利润30亿增至50亿）未经公司验证，仅作为分析线索; One or more filing-reported segments required deterministic restoration.; Material segment three-year driver lines are missing: 化工新材料, 化肥产品, 煤化工基础产品; EPS forecast lacks a validated CNY-million parent-profit / diluted-share-count bridge.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ(产品销量 × 实现均价)，销量受产能利用率与荆州新产能驱动，价格受煤炭/原油价差、行业供需及政策影响
- Profit: Profit = Σ[销量 × (实现均价 - 单位原料成本 - 单位加工成本)] - 期间费用(含研发) - 财务费用 - 税费，原料以煤炭为主，加工成本通过柔性联产优化
- Cash flow: OCF = 净利润 + 折旧摊销 - 营运资金变动; FCF = OCF - 资本支出(维护+扩张)
- Reinvestment: 高资本密集，固定资产+在建工程占总资产比重超过60%；当前处于德州基地改造、荆州新材料项目投资期，但行业新增产能审批收紧，预计2027年后资本开支逐步回落

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 煤化工基础产品的综合价差（产品售价-煤炭成本）能否在2026H2持续改善，还是仅为补库带来的短期脉冲？ | unresolved | 产品综合ASP, 煤炭成本, 毛利率 | 营业收入, 营业成本, 净利润 | 公司出厂价与市场价折价系数, 分产品销量, 煤炭采购价与煤耗单耗; 2026年中报分产品毛利率及三季度行业价格数据 |
| Q2 | 荆州基地新材料项目（TDI/草酸等）能否按计划投产、达产并产生正面利润贡献，资本开支节奏如何？ | unresolved | 荆州项目产能, 开工率, 产品价差, 资本支出 | 营业收入, 营业成本, 资本支出, 自由现金流 | 荆州项目具体投产时间表、投资规模、预期内部收益率; 关注公司项目投产公告及第三方调研 |
| Q3 | 在行业供给端长期受限的背景下，公司能否将成本优势转化为持续高于0%的ROIC，并穿越周期？ | unresolved | ROIC, 毛利率相对行业均值, 资本开支强度 | 营业利润, 自由现金流, 估值倍数 | 同行业可比公司如宝丰能源的ROIC与毛利率, 公司分板块ROIC; 对比宝丰能源、鲁西化工年报及财务比率 |
| Q4 | 化肥业务出口政策能否实质性放开，从而贡献增量销量和利润，并缓释国内尿素价格波动风险？ | unresolved | 化肥出口量, 尿素价格 | 化肥营业收入, 毛利 | 化肥出口政策动向, 国际尿素与国内价差; 跟踪化肥出口关税和配额政策，对比国际尿素价格 |
| Q5 | 当前市场估值（PE TTM 15.9x，PB 1.73x）是否已定价了2026年盈利改善？若2026E净利润实现42.5亿以上，forward PE降至13.9x，市场会否重估？ | unresolved | 2026E归母净利润, 合理PE倍数, 转增后股本基数 | 估值, 目标价 | 至少3家券商一致预期盈利, 转增后股价的历史PE分位; 收集1-3家券商盈利预测，统一股本后计算forward PE和分位 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业收入 | mn CNY | 30968.88 | 34000.0 | 37000.0 | 40000.0 | 以2026Q1年化收入34,474百万为参照，考虑后续产品价格波动及荆州新产能逐步释放，给予温和增长 | 分析估算，受限于分产品量价缺失 | 产品综合售价每下跌1%，收入减少约340百万；销量受新产能影响，不确定性更高; 分产品销量与ASP, 新项目投产对收入的量化贡献 |
| consolidated | 营业成本 | mn CNY | 25855.0 | 27710.0 | 29600.0 | 31600.0 | 成本 = 营业收入 × (1 - 毛利率)；FY2025毛利率按约16.5%估算（成本约25,855百万） | 估算 | ; FY2025准确毛利率及成本结构 |
| consolidated | 毛利率 | % | 16.5 | 18.5 | 20.0 | 21.0 | 基于2026Q1 22.28%及行业复苏预期，假设逐渐改善但未回到历史极端高位 | 假设 | 毛利率每变动1个百分点，营业利润变动约340-400百万; 煤价与产品价格对毛利率的弹性系数 |
| consolidated | 期间费用率（不含财务费用） | % | 5.0 | 4.8 | 4.5 | 4.5 | 包括销售、管理、研发费用，基于Q1隐含水平，规模增长摊薄 | 假设 | ; 费用明细 |
| consolidated | 财务费用率 | % | 0.7 | 0.9 | 0.8 | 0.7 | Q1 2026为0.90%，随有息负债逐步偿还和利率环境改善略降 | 假设 | ; 有息负债规模与利率 |
| consolidated | 营业利润 | mn CNY | 4200.0 | 5100.0 | 6100.0 | 6900.0 | 营业利润 ≈ 收入×(毛利率 - 期间费用率) - 其他影响，辅以实际税率反推核对 | 估算，与FY2025实际数字可能存在偏差 | ; FY2025营业利润确切值 |
| consolidated | 归母净利润 | mn CNY | 3315.49 | 4250.0 | 5100.0 | 5800.0 | 归母净利润 = (营业利润 - 财务费用) × (1 - 有效税率约16%) - 少数股东损益 | 假设，以2026Q1年化利润45.4亿为基准，考虑全年波动和季节性，下调至42.5亿 | 收入增长1%影响净利润约42.5百万；毛利率1pp变动影响约250百万; 有效税率, 少数股东损益 |
| consolidated | EPS | CNY/share | 1.206 | 1.545 | 1.855 | 2.109 | EPS = 归母净利润 / 2,750百万股 | 基于转增后股本，假设无稀释 | ; 潜在稀释工具 |
| consolidated | 经营现金流净额(OCF) | mn CNY | 3500.0 | 3600.0 | 4300.0 | 4900.0 | OCF = 归母净利润 × 0.85（基于Q1比率0.80，略有提高） | 估算，实际受营运资本变动影响大 | ; 营运资金变动明细, 折旧摊销 |
| consolidated | 资本支出(Capex) | mn CNY | None | 4000.0 | 3500.0 | 3000.0 | 根据公司在建工程及德州、荆州投资计划主观估计；须从现金流量表核实 | 大幅假设，缺少财报数据支撑 | Capex超预期1,000百万直接减少FCF 1,000百万; FY2025购建固定资产支付现金, 在建工程预算 |
| consolidated | 自由现金流(FCF) | mn CNY | None | -400.0 | 800.0 | 1900.0 | FCF = OCF - Capex | 基于OCF及Capex估算，FCF预计2027年转正 | Capex节奏决定FCF转正时点和分红能力; 准确Capex数据 |
| 化肥 | 营业收入 | mn CNY | 7305.67 | 7500.0 | 7800.0 | 8000.0 | 假设尿素价格温和，销量因出口政策利好小幅增长 | 假设，需跟踪尿素内销/出口价量 | ; 尿素销量与价格 |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | bottom_profit_bridge | 20.0 亿元 | None | None | None | None | bull None->None; base None->None; bear None->None | assumption_quantified_financial_bridge_missing | unchanged/watch: no model assumption or scenario probability change until 待德州区气化炉/净化装置改造投产及2026中报/年报验证；底部利润口径需与公司公告净利润/EBITDA对齐。 | 6-10亿利润提升的税后口径与时间表, 底部利润30亿对应的产能利用率与产品组合, 荆州TDI/草酸项目投产爬坡节奏, 转增前/后的股本基数与估值计算口径 |
| KPE02 | 煤化工基础产品 | asp_or_price | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 用公司出厂价/结算价和周度市场价交叉验证，并匹配煤炭成本变动。 | 公司各产品收入权重, 市场周度价到公司实现价格的传导系数, 煤炭价格与单位煤耗 |
| KPE02 | 化工新材料 | asp_or_price | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 确认己二酸/己内酰胺/TDI收入占比及公司实际价格敞口。 | 己二酸/己内酰胺/TDI收入占比, 公司新材料价格敞口 |
| KPE03 | 煤化工基础产品 | segment_prosperity | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 用2026中报分产品收入和毛利率验证底部反转；避免把板块代理数据直接等同于公司已实现价格。 | 公司分产品量价拆分, 价格中枢抬升的持续性与库存回补斜率 |
| KPE04 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 观察中报订单/库存、开工率及三季报补库证据；若三季度量价未改善，则该情景概率下修。 | 公司开工率, 产成品库存, 下游补库订单见单量 |
| KPE05 | consolidated | valuation | None x | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 与2026-07-31市值推算的PE TTM 15.91/PB 1.73核对；确认是否采用转增后股本及底部/正常化盈利。 | KPE05所用PE盈利口径与日期, 转增后股本27.50亿股下的估值, PB分位数计算基准 |
| KPE06 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 跟踪公司主要产品9-10月报价及中报业绩预告/正式报告。 | 公司产品提价范围, 补库对销量弹性, 油价平稳假设 |
| KPE07 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 区分油价上行对煤化工是成本推动还是需求拉动；跟踪公司价差与煤价。 | 油价-煤价价差, 公司销量对下游补库的敏感性 |
| KPE08 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 验证海峡冲突对全球化工供给和公司出口/能源成本的传导；若油价上行未传导至公司主要产品价差，则仅成本端压制。 | 公司煤化工价差, 海外供给收缩传导路径 |
| KPE09 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 把油价中枢上行转化为公司主要产品价差和销量，否则仅作为情景方向。 | 公司主要产品价格/成本敏感性, 海外受损装置涉及的产品线 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-17T08:17 | 有效窗口/16天 | 未披露 | 德州追求提质增效，计划更换第一平台、二平台的气化炉和净化装置，预计实现约6-10亿利润提升空间，表内增量显著，测算底部利润30e增厚至50e以上，当前底部估值仅11X | 德州追求提质增效，计划更换第一平台、二平台的气化炉和净化装置，预计实现约6-10亿利润提升空间，表内增量显著，测算底部利润30e增厚至50e以上，当前底部估值仅11X | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-07T08:15 | 有效窗口/26天 | 未披露 | 未提取到带期间的明确盈利预测 | 目前龙头万华化学和华鲁恒升的PE约为12倍，PB仅有2.1倍和1.6倍，PB位于2020年以来10%和13%的分位数（按照7月6日收盘价测算） | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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