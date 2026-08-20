# Forward Forecast Model Scaffold for 688041.SH as of 2026-08-20

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 4033592186.34 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 55.604% / -5.59pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / -0.8866% / +0.76pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.0984 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 23.7548% / +2.75pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 45.4516% / -14.90pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 高端处理器（CPU 与 DCU） revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 服务器/超节点系统集成与交付 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
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
| 高端处理器（CPU 与 DCU） | period=2025 年度 (revenue); 2026 Q1 (margins); revenue=14376889476.95 元; revenue_weight=100.0%; growth=56.92%; gross_margin=55.604% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 服务器/超节点系统集成与交付 | period=unspecified; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 高端处理器（CPU 与 DCU） | revenue_weight=100.0%; growth=56.92%; gross_margin=55.604%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 服务器/超节点系统集成与交付 | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | 需求：公司收入多少由训练vs推理负载驱动？CPU和DCU在收入中各占多少？; 行业供给：公司能否拿到足够先进制程/CoWoS/HBM产能，良率与成本如何？; 竞争：寒武纪/昇腾/天数智芯在哪些客户群和产品性能上直接争夺公司份额？; 盈利：毛利率-5.59pp的分产品归因是什么，是CPU/DCU结构还是价格竞争？ |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | 高端处理器是唯一报告的利润池，权重100%；收入和利润都取决于它的CPU/DCU量价与毛利。系统集成可能是未来第二利润池，但毛利率低、收入未披露，不能替代核心芯片业务。先解决CPU/DCU拆分和毛利率归因，再解决现金转化，最后才能评价182x估值是否合理。 |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | 直接对手中，寒武纪AI芯片纯粹度高，昇腾有华为生态和系统交付能力。公司差异化在于x86兼容CPU和重点行业粘性，但DCU仍面临寒武纪等直接替代。客户自研ASIC是中长期最大不可验证威胁。竞争对手的系统级交付可能绕开单芯片、以整机方案竞争，使芯片毛利率和份额更难预测。 |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | 定性结论是高景气+国产替代+产品迭代。可量化：FY2025收入+56.92%、Q1 2026毛利率55.604%但同比-5.59pp、2026H1研发/收入29.15%、OCF -427.54 mn。无法量化：分产品出货量、ASP、产能利用率、订单额、OCF全年。必须检索：分产品工艺/量产时点、毛利率下降归因、现金流量表补充资料、权威总股本。 |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | 市场正在为AI算力国产替代的强斜率和高估值付费，PE TTM 182x和PS TTM 31.8x表明，价格隐含了超节点渗透率快速兑现和公司成为AI工厂核心供应商。模型差异在于：用可获得的2026H1 run-rate计算，2026E base利润约3,100 mn，当前价需要的估值仍很高；差距主要不是方向，而是幅度（2027/2028收入利润还能否线性外推）和时机（OCF和毛利率何时修复）。 |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | 最强牛市论点：DCU4对标H200/B系列，超节点渗透率2027翻倍，公司是国产AI算力稀缺标的；击穿点：三季报毛利率继续下滑、OCF仍为负、DCU4出货指引弱。; 最强熊市论点：极高估值+负经营现金流+毛利率下滑，显示增长质量差；反转点：毛利率环比企稳回升、OCF/净利润恢复至0.5以上、CPU/DCU收入均放量。; 对国产替代叙事的反击：竞争者同样受益，且系统级交付可能让利润留在整机厂而不是芯片厂；验证信号：公司份额、订单额和单GW价值量。 |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | 用情景化PE而非单一目标价：bull给180x对应高增长和利润改善，base给140x反映毛利率和现金流风险，bear给70x反映成长下修。核心驱动是2026E利润，missing FCF和权威股份数使其只能视为区间，而非确定价值。 |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | 写成投资者可理解的叙事应是：公司是国产高端处理器稀缺资产，AI capex和DCU4为增长发动机，但当前需要验证的不是需求有无，而是增长质量——毛利率、现金流、产能和估值能承受多大兑现风险。避免暴露原始数据表和证据清单，只留下方向上可检验的经营变量和现金质量拐点。 |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE02 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 4033592186.34 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 55.604% / -5.59pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 17.0343% / -4.04pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / -0.8866% / +0.76pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.0984 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV026 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 9/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 半年 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 海光信息技术股份有限公司2026年半年度报告: 1,631,411,695.35 1,090,013,467.67 49.67 性损益的净利润 经营活动产生的现金流量净额 -427,541,001.36 2,176... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 半年 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 海光信息技术股份有限公司2026年半年度报告: 1,631,411,695.35 1,090,013,467.67 49.67 性损益的净利润 经营活动产生的现金流量净额 -427,541,001.36 2,... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 半年 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 海光信息技术股份有限公司2026年半年度报告: 开发支出 422,290,530.46 1.17 306,912,222.40 0.86 37.59 增投入所致 主... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 半年 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 海光信息技术股份有限公司2026年半年度报告: 其中：利息费用 33,896,689.85 22,675,965.57 利息收入 100,... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 半年 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / inventory: 海光信息技术股份有限公司2026年半年度报告: （三）财务风险 1. 存货跌价风险 公司战略备货增加，期末存货账面价值 751,822.21 万元，占期末资产总额的比例为 20.86%。 / inventory: 海光信息技术股份有限公司2026年半年度报告: 1. 存货跌价风险 公司战略备货... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | revenue | 2026, 半年 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 海光信息技术股份有限公司2026年半年度报告: 6.86 5.22 增加1.64个百分点 资产收益率（%） 研发投入占营业收... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |
| EV052 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 182.2314 / earnings multiple the market is paying now / |
| EV053 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 31.7879 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 23.7548% / +2.75pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 高端处理器（CPU 与 DCU） | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025 年度 (revenue); 2026 Q1 (margins); reported revenue=14376889476.95 (元); revenue weight=100.0%; growth=56.92%; gross margin=55.604%; margin change=-5.59pp; source=company_business_model, earnings_model, filing_intelligence; mode=llm_semantic |
| 服务器/超节点系统集成与交付 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 572554204173 / current equity value / / / PE TTM / 182.2314 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: 仅一个披露分部，但CPU/DCU产品收入拆分缺失，无法独立检验两大赛道。; 未取得2026全年指引；2026E仅能用2026H1研发投入/占比反推收入，再以H1 run-rate推算，属计算值而非公司指引。; 2026H1 OCF转负与利润增长之间存在未调阅附表就无法解释的缺口；研发资本化/费用化口径也未完全核对。; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 服务器/超节点系统集成与交付, 高端处理器（CPU 与 DCU）; Valuation has not closed from mutually exclusive buckets to per-share fair value.; volume_price_cost driver chain is incomplete; missing: volume; Three-year values remain missing for consolidated line(s): revenue, parent_net_profit, operating_cash_flow, capex, eps, fcf, gross_margin, operating_profit
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 收入 = CPU出货量 x CPU ASP + DCU出货量 x DCU ASP + 其他业务；未披露CPU/DCU拆分。FY2025收入14,376.89 mn，Q1 2026收入4,033.59 mn。
- Profit: 毛利 = 收入 x 毛利率，Q1 2026毛利率55.604%（同比-5.59pp）；扣除高研发/销售/管理费用后，Q1 2026净利率17.034%。
- Cash flow: 经营现金流 = 净利润 + 营运资本变动；Q1 2026 OCF/净利润仅0.0984；2026H1 OCF -427.54 mn，存货7,518.22 mn。
- Reinvestment: 高研发投入，2026H1研发投入2,652.38 mn，占收入29.15%；开发支出由306.91 mn增至422.29 mn；现金流转化能力仍需验证。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ01 | DCU4和系统级交付能否在2026H2-2027转化为可确认的收入和订单，而不只是行业叙事？ | unresolved | segment_volume, revenue, gross_margin | revenue, parent_net_profit, EPS | DCU4订单额, 分产品收入, 系统集成收入占比; 跟踪2026中报/三季报分产品收入、订单和公司指引。 |
| UQ02 | Q1毛利率-5.59pp是产品结构、成本上升还是价格竞争，2026-2028毛利率中枢会落在哪里？ | unresolved | segment_margin, asp_or_price, unit_cost | gross_margin, operating_margin, net_margin, parent_net_profit | CPU/DCU成本拆分, 分产品ASP, 毛利率变动原因; 调阅中报分产品毛利与成本表，跟踪三季报毛利率。 |
| UQ03 | 2026H1 OCF -427.5 mn是战略性备货还是需求/回款恶化，现金转化何时恢复？ | unresolved | working_capital, ocf_to_net_profit, inventory | operating_cash_flow, FCF, receivables, inventory | 存货-产品结构, 应收周转天数, 全年OCF指引; 调阅现金流量表补充资料，分解存货/应收/应付变化。 |
| UQ04 | 公司实际产能、利用率和先进制程/先进封装瓶颈能否支撑爆发式出货，不出现良率或成本失控？ | unresolved | capacity, utilization, yield, segment_volume | revenue, gross_margin, capex | 产能/产量, 代工/封测供应商, 良率; 获取公司产能/订单信息披露，与客户capex交叉验证。 |
| UQ05 | 在PE TTM 182x下，当前价格隐含的3-5年利润和ROIC路径是什么，已披露年度利润与EPS proxy是否可靠？ | unresolved | valuation_multiple, diluted_share_count, parent_net_profit | EPS, fair_value_per_share | 权威总股本, TTM parent profit, 真实列位口径; 用Tushare stock_basic/daily_basic总股本和最新母公司净利润重算EPS。 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | revenue | CNY mn | 14376.89 | 18198.17 | None | None | 2026E = 2026H1收入 x2; 2026H1收入 = 研发投入2,652.38 / 29.15% = 9,099.08 mn | calculated_run_rate_not_guidance | H2需求与DCU4出货节奏; 2026全年收入指引, 直接披露的H1总收入 |
| consolidated | parent_net_profit | CNY mn | 2544.89 | 3099.93 | None | None | 2026E = 2026E revenue x Q1 2026 net margin 17.0343% | analyst_estimate | 毛利率与研发费用率; 2026全年利润指引, 毛利率中枢 |
| consolidated | eps_cny | CNY | 1.095 | 1.334 | None | None | parent_net_profit / diluted_share_count 2324.338 mn | calculated | 利润及股份数; 权威总股本, 摊薄收益率 |
| consolidated | operating_cash_flow | CNY mn | -427.54 | None | None | None | reported 2026H1 OCF | reported | 存货/应收/应付变动; FY2026 OCF, 2025H1 OCF口径确认 |
| consolidated | rd_spend | CNY mn | 2652.38 | 5304.76 | None | None | 2026E = 2026H1 x2 run-rate | calculated_run_rate | 研发投入强度; 研发资本化/费用化拆分, 全年研发预算 |
| consolidated | inventory_book_value | CNY mn | 7518.22 | None | None | None | reported期末存货账面价值 | reported | 战略备货是否转化为收入; 存货结构, 跌价准备 |
| consolidated | capex |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | eps | CNY/share | None | 1.333682909556058 | None | None | parent net profit (CNY mn) / diluted shares (mn) | calculated | ; required consolidated forecast line omitted |
| consolidated | fcf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | gross_margin |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |
| consolidated | operating_profit |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE02 | consolidated | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 跟踪 2026 年中报与三季报中毛利率变化，以及 DCU4 新品定价。 | 分产品 ASP 数据, 毛利率变动拆分 |
| KPE03 | consolidated | utilization_or_backlog | None  | None | None | None | None | bull None->55.0; base None->35.0; bear None->10.0 | unverified | scenario probabilities changed; use only the validated before/after triplets | 公司具体订单量, 产能利用率 |
| KPE05 | consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 跟踪公司产品出货量/收入指引，并与客户 capex 计划交叉验证。 | 公司出货量预测, 客户采购份额 |
| KPE08 | 服务器/超节点系统集成与交付 | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 关注公司超节点相关产品出货与收入确认，评估系统集成业务利润率。 | 系统集成收入占比, 系统集成毛利率 |
| KPE01 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE04 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE06 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE07 | consolidated/unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE09 | 高端处理器（CPU 与 DCU） | scenario_probability | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE10 | consolidated/unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE11 | consolidated/unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE12 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-08-17T22:52 | 高时效/3天 | 未披露 | 国产算力集体迭代，加速出货 26H1，寒武纪、海光信息、摩尔线程、壁仞科技收入同比均高增 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-08-17T21:52 | 高时效/3天 | 推荐措辞（非标准评级） | ②HG芯片生态：定制化产品测试指标达到海光极限要求，下游服务器厂商已明确140万支MOQ，预计获得海光生态50%+份额，2027年进入大批量采购阶段 / ⑤盈利预测及投资建议：2027年国产算力方向迎来大爆发，有望兑现近80亿增量收入（HW50亿+海光8亿+半导体14亿+光8亿），对应12-15亿利润，叠加主业军用连接器年化5亿利润，整体利润近20亿，给30XPE第一阶段目标看到600亿，国产放量阶段看到1000亿市值，当下仅300亿市值，显著低估，重点推荐！ | ⑤盈利预测及投资建议：2027年国产算力方向迎来大爆发，有望兑现近80亿增量收入（HW50亿+海光8亿+半导体14亿+光8亿），对应12-15亿利润，叠加主业军用连接器年化5亿利润，整体利润近20亿，给30XPE第一阶段目标看到600亿，国产放量阶段看到1000亿市值，当下仅300亿市值，显著低估，重点推荐！ | rating=推荐措辞（非标准评级） | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 民生证券/2026-08-17T08:47 | 高时效/3天 | 未披露 | 再次深度PPT解读 https://1ij.cn/TKrQM （四）20260301第四期 1、KIMI“龙虾”玩法演示 2、“龙虾”受益方向：国产大模型、云与数据安全 3、再谈Token需求“通胀”云涨价 https://1ij.cn/d3EWx （五）20260307第五期 OpenClaw爆发增长、智能体云平台与华为昇腾算力 https://1ij.cn/Q2rVy （六）20260314第六期 “龙虾”之火，可以燎原 https://1ij.cn/uU9vX （七）20260328第七期 1、AI存算... | 再次深度PPT解读 https://1ij.cn/TKrQM （四）20260301第四期 1、KIMI“龙虾”玩法演示 2、“龙虾”受益方向：国产大模型、云与数据安全 3、再谈Token需求“通胀”云涨价 https://1ij.cn/d3EWx （五）20260307第五期 OpenClaw爆发增长、智能体云平台与华为昇腾算力 https://1ij.cn/Q2rVy （六）20260314第六期 “龙虾”之火，可以燎原 https://1ij.cn/uU9vX （七）20260328第七期 1、AI存算... | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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