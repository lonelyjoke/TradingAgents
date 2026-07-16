# Forward Forecast Model Scaffold for 688981.SH as of 2026-07-15

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 17617218000 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / N/A / N/A / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.1569% / +2.35pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 3.77 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 9.0474% / +0.46pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 38.5167% / +4.98pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 情况 其他主营业务 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Foundry Services revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| 情况 其他主营业务 | period=annual filing; revenue=3786198.0 filing table unit not explicit in extracted row; revenue_weight=100.0%; growth=-2.0%; gross_margin=32.0% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| Foundry Services | period=FY2025; revenue=67323192000.0 人民币元; revenue_weight=98.9%; growth=16.6%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 情况 其他主营业务 | revenue_weight=100.0%; growth=-2.0%; gross_margin=32.0%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| Foundry Services | revenue_weight=98.9%; growth=16.6%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | 先进制程：7nm/5nm 产能何时放量？每片 ASP 溢价与良率如何？; 成熟制程：12英寸和8英寸晶圆代工ASP趋势是否存在价格竞争？; 资本开支节奏：公司是否能在2028年前降低CapEx/营收比？; 设备与材料供应：美国出口管制是否进一步收紧？国产设备替代进度能否支撑扩产？ |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | Foundry Services (晶圆代工) 是唯一重要利润池，贡献>98%收入和几乎所有利润。其他业务毛利近乎为零，可忽略。Foundry Services内部，先进制程虽然当前占比小但高ASP可能成为未来利润增量主力；成熟制程贡献绝大部分收入和现金流，但利润率受竞争压制。关注重心应是先进制程收入弹性与折旧对净利润的压制何时消退。 |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | 直接竞争对手：台积电（技术绝对领先但受地缘因素限制中国客户）、三星（内部产能为主）、华虹宏力（专注特色工艺）、联电（成熟制程）。本土替代逻辑下，中芯国际受益于国内设计公司被迫选择大陆代工，但技术受限使其难以争夺最高端订单。先进封装、Chiplet等技术一定程度上降低对单一片厂先进制程的依赖，构成远期替代风险。客户自建产能（如华为的“南方”产线）未来可能分流需求。 |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | 关键定性结论：中芯国际正处于大规模资本开支周期中，产能快速扩张，但盈利能力被折旧严重拖累。当前高估值隐含市场对远期盈利爆发式增长的一致预期。由于未获得分制程收入和详细折旧表，无法精确量化折旧对净利润的释放节奏，但可以通过观测EBITDA margin（Q1 57.3%）和产能利用率（93.1%）间接推断：若收入持续高增、利用率保持高位，则经营杠杆将带来利润弹性。需要补充的前提数据：未来3年CapEx计划、转固进度、设备折旧年限。 |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | 当前市值约1.38万亿元，TTM PE 273倍，PS 20倍，估值位于5年100%分位。以此反推，市场预期至少未来三年净利润复合增速可能需达到50%以上，且净利润率需从7.7%提升至约15%才能将PE降至50-60倍。而我们的base case假设收入增长15%-12%-10%，净利润率小幅改善，2028年净利润约95亿CNY，对应现市值PE仍高达145倍。换言之，当前价格已经定价了极度乐观的假设，我们的模型与市场定价之间存在巨大期望差：缺口在增长率和利润率幅度，而非方向。 |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | 牛市反面论据 (bear against bull)：即使AI需求强劲，中芯国际无法获得EUV光刻机，其“先进制程”不过是7nm DUV工艺，与台积电3nm/2nm差距仍在拉大，长期竞争力存疑；且国内大量fab扩产可能导致成熟制程供过于求，拉低ASP和利用率，抵消先进制程收益。; 熊市反面论据 (bull against bear)：出口管制恰恰强化了中芯国际不可替代的本地战略地位，即使技术稍落后，国内设计公司必须在本土流片，形成刚性需求；产能绑定和设计服务粘性有助于维持利用率。此外，EBITDA利润率57%表明基础盈利能力强，一旦折旧周期过去，利润可能井喷，使当前估值看起来并非昂贵。 |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | 估值解释：我们采用场景加权法（bull/base/bear with P/E on 2028E parent net profit）。Core bucket基于base case 2028E净利润95亿，给予25倍P/E（考虑高资本密集度及技术风险下合理溢价），得到约2380亿股权价值。Bull场景增量利润（较base多约48亿）按30倍计价，概率30%。隐含公平价值远低于当前市值（1.38万亿），差异来自市场对增长率、利润率及终端估值的极度乐观假设。在将远期净利润转化为每股价值时，因未获稀释股数而无法得出每股目标价；但逻辑上当前市场价格需要持续高增长和估值倍数维持在高位，一旦增长预期下调，股价将面临显著的估值收缩风险。 |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | 基金经理应将中芯国际视为高度依赖宏观政策与资本周期的看涨期权：upside来自先进制程突破和国产替代浪潮加速，downside来自技术封锁和折旧压力。当前定价已充分反映了乐观情景，任何进展不及预期都可能导致估值剧烈修正。在缺乏详细制程数据的情况下，建议重点关注产能利用率、EBITDA利润率趋势和季度CapEx指引作为先行指标，而非盯住PE。投资决策应聚焦于澄清Q1-Q5中的不确定性，确认当前股价是否已过度透支盈利预期，而非简单追涨半导体主题。 |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | unit cost / gross margin | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | net profit / EPS | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 17617218000 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / N/A / N/A / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 7.7266% / -0.59pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.1569% / +2.35pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 3.77 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | industry_kpi | secondary_or_derived_research | reported | revenue | unspecified | / Mobile / mobile subscribers, 5G penetration, mobile ARPU, DOU, churn, package mix / service revenue and margin durability / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | unspecified | / Capex / 5G/cloud/AI capex, depreciation, network utilization, capex-to-revenue / FCF and ROIC / |
| EV031 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 中芯国际2026年第一季度报告: 归属于上市公司股东的扣除非经常 1,232,279 1,169,998 5.3 性损益的净利润 经营活动产生的现金流量净额 5,131,729 -1,171,520 不适用 / o... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 中芯国际2026年第一季度报告: 归属于上市公司股东的扣除非经常 1,232,279 1,169,998 5.3 性损益的净利润 经营活动产生的现金流量净额 5,131,729 -1,171,520 不适用 ... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 中芯国际2026年第一季度报告: 联营企业股权被动稀释 14,763 1,471 - - 按国际财务报告准则 1,375,972 1,357,845 149,806... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | 2025, 年度 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / management_claim_with_evidence: 中芯国际2025年年度报告: 主要业务、主要产品或服务情况 中芯国际是世界领先的集成电路晶圆代工企业之一，也是中国大陆集成电路制造业领导者， 拥有领先的工艺制造能力、产能优势... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 中芯国际2026年第一季度报告: 净敞口套期收益（损失以“-”号填列） - - 公允价值变动收益（损失以“-”号填列） 9,233 -10... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 中芯国际2026年第一季度报告: 交易性金融资产 484,311 608,265 衍生金融资产 184,120 613,090 应收票据 240,747 313,209 / receivables: 中芯国际2026年第一季度报告: 衍生金融资产 184,120 613,090 应收票据 ... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 中芯国际2025年年度报告: 费电子等智能终端迭代升级，产业链在地化转换加速，使得产业对于本土中高端领域芯片制造需 求进一步... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly; answered 9/9; core pack ready. Annual base text and quarterly checkpoint are ... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | revenue | unspecified | Mobile: verify mobile subscribers, 5G penetration, mobile ARPU, DOU, churn, package mix; explain impact on service revenue and margin durability. |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 情况 其他主营业务 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=3786198.0 (filing table unit not explicit in extracted row); revenue weight=100.0%; growth=-2.0%; gross margin=32.0%; margin change=-17.0pp; source=filing_intelligence; mode=deterministic_filing_row |
| Foundry Services | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY2025; reported revenue=67323192000.0 (人民币元); revenue weight=98.9%; growth=16.6%; gross margin=None%; margin change=Nonepp; source=earnings_model, company_business_model; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 1378204157940 / current equity value / / / PE TTM / 273.1514 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
| / 20260714 / sina / N/A / N/A / 【赛伍技术：预计2026年上半年亏损300万元-600万元，同比减亏92%-96%】赛伍技术公告，预计2026年半年度实现归属于上市公司股东的净利润为-300万元至-600万元，与上年同期亏损7209.61万元相比减亏92%-96%；预计扣除非经常性损益后的净利润为-500万元至-900万元，同比减亏88%-93%。业绩减亏主要因传统光伏材料业务毛利率提升、海外胶膜业务营收占比增长，叠加新兴业务板块（锂电PACK、电子电力材料、半导体材料）营收显著增长，以及收购今蓝纳米后协同效应逐步显... | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
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
- Readiness reasons: No diluted share count available; EPS and per-share fair value cannot be computed.; Segment gross margin, operating profit history, and technology-node revenue splits are not disclosed in available filings.; Capex and FCF figures cannot be verified from supplied evidence; OCF-to-profit ratio is available for Q1 2026 only.; 2025 annual report PDF text extraction failed, limiting granular segment data.; Missing breakdown by geography, advanced/mature node, and exact ASP/volume data.; One or more filing-reported segments required deterministic restoration.; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 情况 其他主营业务
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Wafer Shipments (8-inch equivalent wafers) × ASP (CNY/wafer); ASP depends on technology node, product mix, and supply-demand balance.
- Profit: Cost per wafer = Depreciation + Material + Labor + Overhead; Gross Profit = (ASP - Cost per wafer) × Shipments; Operating Profit = Gross Profit - R&D - SG&A; Net Profit = Operating Profit +/- net financial charges - tax.
- Cash flow: OCF = Net Profit + Depreciation +/- Working Capital (receivables, inventory, payables); FCF = OCF - Capex; Capex is massive to build and maintain advanced capacity.
- Reinvestment: 极高资本密集度：持续高额Capex用于先进制程研发和产能扩张，折旧负担重；R&D投入占比收入8.2%（2025）。ROIC目前较低，未来需产能利用率提升和ASP改善来推动。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | Can advanced-node capacity expansion (7nm/5nm) ramp without being blocked by US equipment restrictions, and what ASP premium can it command in 2027-2028? | unresolved | Foundry Services ASP, advanced_node_revenue_share, gross_margin | Revenue, Gross Profit, EPS | official confirmation of advanced node tool deliveries, advanced node wafer price vs mature node; Monitor for 7nm mass production announcements and US BIS rule updates. |
| Q2 | Will utilization stay above 90% post capacity additions, or will incremental demand fail to absorb new capacity, leading to operating margin compression? | unresolved | capacity_utilization, operating_margin | Revenue, Operating Profit, OCF | 2026H2/2027 wafer demand forecasts from major customers, competitor capacity additions; Next quarterly utilization number and forward guidance. |
| Q3 | What is the sustainable level of net profit margin after the current heavy depreciation cycle? Can it reach 15-20% to support a reasonable P/E? | unresolved | depreciation_to_revenue, net_margin | Net Profit, EPS, Valuation | forward depreciation schedule, planned capex and useful life assumptions; FY2026 annual report with depreciation and net margin breakdown. |
| Q4 | Can free cash flow turn positive by 2028, or will ongoing capex for domestic 12-inch expansion keep FCF deeply negative? | unresolved | capex, FCF | Capex, FCF, Net Debt | capex budget for 2026-2028, depreciation and amortization forecast; Company annual capex guidance and interim cash-flow statement. |
| Q5 | Is the current market valuation (>200x PE) already discounting a multi-year super-cycle, leaving no margin of safety if growth disappoints? | unresolved | PE_multiple, EPS_growth_rate | Fair Value per Share, Expected Return | consensus EPS forecasts for 2027/2028, implied growth from reverse DCF; Build a reverse DCF to determine what assumptions are priced in. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foundry Services | Revenue | CNY mn | 66580.2 | 76567.2 | 85715.3 | 94286.8 | Growth 15% / 12% / 10% driven by capacity expansion and strong AI demand | analyst_estimate | ASP and utilization; wafer shipment and ASP split, advanced node contribution |
| consolidated | Revenue | CNY mn | 67323.2 | 77421.7 | 86612.3 | 95283.5 | Foundry revenue + Other (743 mn flat) | analyst_estimate | Overall semiconductor demand; Other business growth |
| consolidated | Gross Profit | CNY mn | 14558.0 | 16645.7 | 19054.7 | 21915.2 | Gross margin 21.5% / 22.0% / 23.0% of revenue | analyst_estimate | Depreciation and product mix; FY2025 consolidated gross margin verification |
| consolidated | Operating Profit | CNY mn | None | 7742.2 | 9527.4 | 11434.0 | Operating margin 10.0% / 11.0% / 12.0% | analyst_estimate | Operating leverage and R&D spend; FY2025 operating profit, detailed R&D and SG&A |
| consolidated | Parent Net Profit | CNY mn | 5040.7 | 6193.7 | 7795.1 | 9528.4 | Net margin ~8% / 9% / 10%; tax ~12% | analyst_estimate | Revenue growth and net margin expansion; exact tax rate, minority interest |
| consolidated | EPS | CNY per share | None | None | None | None | Parent net profit / diluted shares | missing | Share count; diluted share count |
| consolidated | OCF | CNY mn | None | 12387.0 | 15590.0 | 19057.0 | Assumed 2.0x net profit in 2026E, gradually declining to 2.0x | analyst_estimate | Working capital and depreciation; FY2025 OCF, consistent capex definition |
| consolidated | Capex | CNY mn | None | None | None | None | Not available from evidence; typically very high | missing | Expansion spending; FY2025-2028 capex budget |
| consolidated | FCF | CNY mn | None | None | None | None | OCF - Capex | missing | Capex intensity; OCF and Capex missing |
| consolidated | gross_margin |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | Foundry Services | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline volume growth rate, unit of volume |
| KPE04 | Foundry Services | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific capacity utilization impact |
| KPE05 | Foundry Services | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | capacity addition quantification |
| KPE07 | Foundry Services | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | timing of capacity additions, capex amounts |
| KPE12 | Foundry Services | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | specific volume driver |
| KPE02 | consolidated/unmapped | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE03 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE06 | consolidated/unmapped | unit_cost | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE08 | consolidated/unmapped | market_share | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE09 | consolidated/unmapped | revenue | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE10 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE11 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 高盛/2026-07-15T08:49 | 高时效/0天 | 未披露 | 未提取到带期间的明确盈利预测 | 💎中芯国际光刻胶公司 CXMT 确定 IPO 发行价为每股 8.66 元人民币，对应初始估值 5970 亿元人民币 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-14T09:23 | 高时效/1天 | 未披露 | 各晶圆厂已向客户释出2026年涨价信息，预计涨价效应会在二、三季度开始明显显现，Q3/4毛利率改善将会更加明显，今年明年来看，晶圆厂业绩有望超预期！ [太阳]目前估值水平较海外水平并不高，若两存上市各达到几万亿市值，按照海外存储厂：海外代工厂市值比，国内代工厂仍有很大空间，建议关注：晶合集成、中芯国际、华虹公司、燕东微、芯联集成等 | 各晶圆厂已向客户释出2026年涨价信息，预计涨价效应会在二、三季度开始明显显现，Q3/4毛利率改善将会更加明显，今年明年来看，晶圆厂业绩有望超预期！ [太阳]目前估值水平较海外水平并不高，若两存上市各达到几万亿市值，按照海外存储厂：海外代工厂市值比，国内代工厂仍有很大空间，建议关注：晶合集成、中芯国际、华虹公司、燕东微、芯联集成等 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 机构未识别/2026-07-13T11:03 | 高时效/2天 | 未披露 | 3️⃣ 外延切入CMP抛光液： 随先进制程层数增加，需求指数增长，公司预计扩建1.5万吨相关产能，将直接对接中芯微电子、华虹等核心大厂，2027年目标收入达7千万-1亿元 | 未提取到目标价/估值方法与倍数 | 2027E_收入=7 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 中泰电子丨晶圆代工/2026-07-12T10:32 | 高时效/3天 | 未披露 | 未提取到带期间的明确盈利预测 | 相对应的中芯H股4.0倍PB，华虹H股6.1倍PB，大陆晶圆厂还有先进逻辑核心卡位优势 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI05 | 机构未识别/2026-07-10T09:12 | 高时效/5天 | 未披露 | 未提取到带期间的明确盈利预测 | 之前我们讲过，合肥长鑫上市，估值可能来到3万亿RMB，那么港股的中芯国际市值在7200亿港币，折合人民币才6000亿左右 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI06 | 机构未识别/2026-07-10T08:53 | 高时效/5天 | 未披露 | 未提取到带期间的明确盈利预测 | 行业景气：AI需求挤占产能背景下，先进及成熟制程均处于涨价通道，中芯国际、华虹公司已多次公告涨价，国产先进制造进入收获期，将通过量价提升改变Fab厂估值体系 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI07 | 机构未识别/2026-07-10T08:23 | 高时效/5天 | 未披露 | 3）抛光液：主做衬底抛光液，与安集/鼎龙差异化竞争，预计27H1落成5万吨厂房，与奕材、扬杰、中芯等公司合作 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI08 | 天风电新/2026-07-10T08:23 | 高时效/5天 | 未披露 | 2024‑2025年，公司前三大客户分别为长江存储、长鑫存储、中芯国际，前五大客户营收占比在40%-45%，客户复购率86.90%，粘性极强，订单具备极强持续性 / 当前国内干式真空泵整体国产化率仅30%，目标国产化率将提升至80%以上，中科仪作为本土唯一供应商，后续在中芯国际内部份额将持续提升，预计2026‑2028年来自中芯国际的采购额年均增速超50% | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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