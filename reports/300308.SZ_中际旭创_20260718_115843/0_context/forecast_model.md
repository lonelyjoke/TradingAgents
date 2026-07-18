# Forward Forecast Model Scaffold for 300308.SZ as of 2026-07-18

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 19496398083.95 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 46.0581% / +9.36pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.2862% / +1.55pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.5872 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 12.3717% / -6.04pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 20.0961% / -9.19pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 800G Optical Transceivers revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 1.6T Optical Transceivers revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Next-Generation & Other revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Semiconductor Forecast And Valuation Controls
- Semiconductor profile: fabless / chip design. Use this profile before consumer, generic technology, telecom, metals, or battery templates.
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
| 800G Optical Transceivers | period=2026Q1; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 1.6T Optical Transceivers | period=2026Q1; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| Next-Generation & Other | period=2026-2028; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 800G Optical Transceivers | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 1.6T Optical Transceivers | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| Next-Generation & Other | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | 1.6T和800G的需求预测差异根源在哪？是AI资本开支假设不同还是份额假设？; 价格谈判结果何时能明朗？公司是否能维持优于行业的定价？; CPO与可插拔光模块的竞争格局将如何演变？公司在新架构中是否保持优势？; 物料瓶颈解除后，行业是否会面临供过于求和价格战？ |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | 当前最重要的利润池是1.6T和800G光模块，合计贡献几乎全部利润。1.6T处于快速增长期，盈利能力最强；800G为成熟现金牛。下一代产品（NPO/CPO）短期贡献很小但对估值支撑至关重要。 |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | 直接竞争对手包括新易盛、天孚通信等国内企业，以及Coherent、Lumentum等国际厂商。客户集中且技术迭代快，市场可能从寡头走向更分散。CPO可能改变竞争基础，公司通过提前布局CPO和硅光维持先发优势。 |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | 毛利率预测基于2026Q1强劲改善，但可持续性需确认。我们假设价格年降10%、硅光渗透提升抵消部分降价，毛利率微升至47.5%。若降价幅度超预期，毛利率可能回落至43%附近。目前缺乏合同价格验证，量化推测不确定。 |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | 当前股价隐含市场似乎认为2027年EPS 66元可达，给予16-17x forward PE。我们的base case EPS 66元、20xPE给出1321元，bull case 81元、22xPE给出1782元，bear case 49.5元、18xPE给出891元。市场定价偏向谨慎，若价格和份额超预期，有较大上行空间。 |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | 即使需求强劲，但大幅扩产可能导致供给过剩，价格战将摧毁利润，历史光模块周期证明确实如此。; CPO可能完全取代可插拔模块，公司现有主要业务面临被颠覆风险。; 公司去年利润基数低，2026年增速高不可持续，年报后的增速放缓将杀估值。; 反方：最大的上行风险是AI集群规模远超预期，光模块需求可能翻倍，公司产能准备充分，可获超额收益。如果2.4T/3.2T提前放量，EPS将再次上调。 |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | 采用情景PE估值法。以2027年预测净利润为锚，给予20x PE（与A股科技电子元器件中位数一致），得到核心价值1321元。加入bull/bear概率，并加上下一代产品期权价值，得到加权目标价1376元。此估值对毛利率和出货量高度敏感。若毛利率下降1pp，EPS将减少约0.6元，目标价降低约12元。 |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | 中际旭创是全球光模块龙头，深度受益于AI数据中心建设浪潮。1.6T光模块的放量将驱动今明两年业绩高速增长，而NPO/CPO等下一代技术布局则为长期成长打开空间。但市场对2027年价格降幅和需求分歧较大，短期需关注下半年出货量验证和合同价格落地。当前估值已部分反映高增长预期，但若价格和份额优于预期，仍有上行空间。 |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment revenue | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE02 | segment revenue | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 19496398083.95 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 46.0581% / +9.36pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 29.4131% / +5.70pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.2862% / +1.55pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.5872 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -49.02%, gross margin change 4.02pp, operating margin change 3.09pp,... |
| EV031 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: 增加。 主要原因是本期应收商业承兑汇票 应收票据 112,532,292.72 72,635,260.22 54.93% / receivables: 2026年一季度报告: 主要原因是本期应收商业承... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 公司对不具有重大影响的股权投资，将其作为其他非流动金融资产核算，该类投资均为相关产业领 -3- 中际旭创股份有限公司 2026 年第一季度报... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 号填列） 信用减值损失（损失以“-”号填 -7,537,042.26 7,699,196.48 / impairm... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 增加。 主要原因是本期应收商业承兑汇票 应收票据 112,532,292.72 72,635,260.22 54.93% / receivables: 2026年一季度报告: 主要原因是本期应收商业承兑汇票 应收票据 112,532,292.72 72,635,26... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 确定其公允价值。对于公允价值上升的项目产生的损益计入公允价值变动损益，及收到的分红收益，在这里 列示为... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 7/7; core pack ready. Annual base text and quarterly chec... |
| EV046 | company_events | research_context | reported | valuation | 2026-07-17 | / 2026-07-17 18:55:17 / 华尔街见闻 / 目标价翻倍至2581元！高盛：英伟达推动3.2T光模块需求加速，中际旭创迎来估值重塑 / N/A / |
| EV048 | company_events | research_context | reported | utilization_or_backlog | 20260706 | / 20260706 / 6月份中国物流业景气指数加快扩张 / 央视网消息（新闻联播）：记者从中国物流与采购联合会了解到，6月份中国物流业景气指数为50.6%，较上月上升0.3个百分点。其中，业务总量指数连续回升。从需求看，新订单指数为50.3%，较上月上升0.1个百分点。电子机械设备制造、通信设备制造、交通运输设备制造、节能家电制造等物流需求回升势头较好。从投资看，固定资产投资完成额指数为54.3%，较上月上升0.2个百分点，其中铁路运输业、航空运输业、管道运输业和邮政快递业均在50%以上的扩张区间。 / |
| EV052 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 73.0709 / earnings multiple the market is paying now / |
| EV053 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 21.3921 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 800G Optical Transceivers | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=filing_intelligence, knowledge_planet; mode=llm_semantic |
| 1.6T Optical Transceivers | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=filing_intelligence, knowledge_planet; mode=llm_semantic |
| Next-Generation & Other | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026-2028; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 1092327779262 / current equity value / / / PE TTM / 73.0709 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
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
- Readiness reasons: 公司未按产品线披露收入及利润细分，业务单元收入权重、毛利率、利润贡献均未知，只能进行定性分析。; 股本数据缺失，无法从提供证据（Tushare、filing）中直接获取总股本/稀释股本，EPS及每股价值计算依赖外部预测推导，存在不确定性。; 行业出货量预测存在分歧（800G: 5500万 vs 1亿只），无权威第三方数据解决，高估/低估风险并存。; 2027年价格降幅的市场传闻与公司表态矛盾，无合同或第三方验证，影响毛利率假设。; Q2 2026业绩及港股IPO进度尚未披露，短期催化剂未证实。; NPO/CPO等下一代技术量产时间及收入贡献尚在概念阶段，估值可选性高度不确定。; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 1.6T Optical Transceivers, 800G Optical Transceivers, Next-Generation & Other
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 收入 = Σ(产品出货量 × ASP) + NRE/其他。出货量取决于数据中心资本开支、公司份额、产能利用率；ASP受产品迭代、竞争、年降幅度影响。
- Profit: 毛利 = 收入 - 物料成本（光芯片、电芯片、其他） - 制造费用。主要驱动是产品结构（1.6T及下一代占比）、规模效应、供应链管理、良率。
- Cash flow: 经营现金流 = 净利润 + 折旧摊销 - 营运资本变动。OCF/净利比约0.59(Q1 2026)，偏低，需关注存货和应收管理。资本开支用于产能扩张和研发。
- Reinvestment: 光模块行业技术迭代快，需持续高研发投入。产能扩张需厂房、设备，但轻资产模式。公司通过供应链锁定关键物料。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 2027年800G和1.6T的价格年降幅度究竟是多少？是否会显著侵蚀毛利率？ | 未确定，公司称降价传闻夸大，但无合同证据。野村上调出货量和盈利预测暗示价格乐观。 | ASP 2027E, consolidated gross margin | consolidated revenue, gross profit, net profit, EPS | 2027年客户合同定价, 可比产品历史降价曲线; 2026Q4或2027Q1合同签署后披露 |
| Q2 | 全球800G和1.6T的真实需求规模将达到多少？公司能否维持30%以上份额？ | Nomura预测800G 55M，1.6T 71.5M；渠道预测800G 100M，1.6T 75M。公司称在手订单增长，需求旺盛。 | global_800G_shipment_2027, global_1.6T_shipment_2027, company market share | consolidated revenue, net profit | 权威第三方预测（如LightCounting）, 公司接单量数据; 行业会议或LightCounting等季度更新 |
| Q3 | NPO/CPO等下一代技术的量产时点和收入贡献节奏如何？是否会带来超额收益？ | 康宁Glass Bridge加速CPO量产，公司方案最完整，但量产时间预计2027H2开始放量，2028年贡献千万只级别。 | NPO/CPO revenue 2028E, optionality valuation | 2028E revenue, valuation multiple | 客户PO, 认证完成时间, 量产良率; 公司样品认证公告或客户技术路线图更新 |
| Q4 | 上游物料（磷化铟晶圆、EML激光器、DSP）的供给瓶颈何时解决？会否限制公司产能？ | 供应偏紧但公司已通过长协、预付款保障，H2 2026供应缓解。长远看，日美厂商扩产将在2028年缓解。 | capacity utilization, unit cost | revenue volume, gross margin | 关键物料自给率, 供应商扩产进度详细时间表; Q2 2026和Q3的出货量数据 |
| Q5 | 港股IPO的发行规模、价格和股本稀释对每股价值的影响有多大？ | 港股IPO正在推进，预计发行价格合理，没有大幅折价，但具体发行规模未知。 | diluted share count, eps | EPS, per share value | 发行股数, 发行价, 最终时间表; 港交所聆讯后招股书 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | revenue | CNY mn | 38239.94 | 103299.69 | 261000.0 | 339300.0 | 2026E: seasonality-adjusted from Q1 2026 revenue 19496.4/0.162 (historical median Q1 share 16.2%) = 103299.7 mn; 2027E: Nomura forecast 261000 mn; 2028E: 30% growth over 2027E based on 2.4T/3.2T ramp. | analyst_estimate | +10% 2027E revenue -> +25% net profit;  |
| consolidated | gross_margin | % | 36.7 | 46.0 | 47.5 | 48.5 | 2026E: Q1 2026 actual 46.06% rounded; 2027E: slight improvement from 1.6T mix; 2028E: continued mix upgrade and scale. | analyst_estimate | Each 1pp GM = ~2.6bn net profit at 2027E revenue;  |
| consolidated | operating_margin | % | 28.3 | 38.6 | 40.2 | 41.5 | 2026E: Q1 2026 actual 38.65% annualized; improvement from scale and lower cost ratio. | analyst_estimate | ;  |
| consolidated | parent_net_profit | CNY mn | 10797.25 | 35373.5 | 73400.0 | 95420.0 | 2026E: seasonality-adjusted net profit from Q1 2026 5734.5/0.162 = 35373.5 mn; 2027E: Nomura 73400 mn; 2028E: 30% growth based on 30% revenue growth and margin expansion. | analyst_estimate | ; exact tax rate, non-recurring items |
| consolidated | diluted_eps | CNY/share | 9.72 | 31.83646836468365 | 66.06066060660608 | 85.87885878858789 | parent net profit (CNY mn) / diluted shares (mn) | calculated | EPS highly sensitive to share count changes from HK IPO; exact diluted shares after IPO |
| consolidated | ocf | CNY mn | 8200.0 | 25000.0 | 50000.0 | 65000.0 | OCF estimated as 70% of net profit (improving from Q1 2026 0.59x), assuming working capital improvement. 2025A arbitrary. | analyst_estimate | ; actual capex, working capital details |
| consolidated | capex | CNY mn | 5000.0 | 8000.0 | 10000.0 | 12000.0 | capex as ~10% of revenue, needed for capacity expansion. Rough estimates. | analyst_estimate | ; historic capex from filings |
| consolidated | fcf | CNY mn | 3200.0 | 17000.0 | 40000.0 | 53000.0 | OCF - capex | analyst_estimate | ;  |
| consolidated | operating_profit |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | revenue | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 需提取报告具体数字 | baseline revenue, revision magnitude |
| KPE02 | consolidated | revenue | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 需提取报告具体数字 | baseline revenue, revision magnitude |
| KPE03 | 800G Optical Transceivers | segment_volume | 5.0 million units | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 需要行业数据或公司订单验证 | 公司对应份额 |
| KPE03 | 1.6T Optical Transceivers | segment_volume | 11.5 million units | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 需要行业数据或公司订单验证 | 公司对应份额 |
| KPE03 | Next-Generation & Other | segment_volume | None million units | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 新产品量产进度 | 基线值, 公司份额 |
| KPE03 | consolidated | revenue | 56500.0 million CNY | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 需要公司披露或更广泛共识验证 | 收入拆分, 毛利率假设 |
| KPE03 | consolidated | profit_or_eps | 14900.0 million CNY | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 需要公司披露或更广泛共识验证 | 净利润率假设, 非经常性损益 |
| KPE04 | Next-Generation & Other | market_share | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 需要Glass Bridge技术量产验证和公司CPO产品认证进展 | 概率变化量化, 公司具体CPO收入占比 |
| KPE05 | 800G Optical Transceivers | segment_volume | None million units | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 需要权威预测验证 | 基线值, 公司份额假设 |
| KPE05 | 1.6T Optical Transceivers | segment_volume | None million units | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 需要权威预测验证 | 基线值, 公司份额假设 |
| KPE05 | consolidated | profit_or_eps | None million CNY | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 需要公司半年度报告验证 | 基线预测, 毛利率假设 |
| KPE06 | consolidated | revenue | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 需要Q2实际数据确认 | 基线环比增速, 具体数字 |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-17T08:59 | 高时效/1天 | 未披露 | 中际旭创：黄金坑已现 中际旭创：黄金坑已现 [玫瑰... 中际旭创：黄金坑已现 [玫瑰]Q2经营表现依然强劲，我们预计业绩不会让市场失望 / 随着Q3开始供需两旺，800G、1.6T出货有望环比加速提升，公司全年收入和利润增长具备较强确定性 / 我们预计2027年海外800G需求接近1亿只，1.6T需求约7000-8000万只 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-17T08:12 | 高时效/1天 | 未披露 | 天风通信 ｜ 全球光互联龙头... 天风通信 ｜ 全球光互联龙头... 天风通信 ｜ 全球光互联龙头中际旭创再坚定信心推荐，更新发声！ 1、我们预计公司港股IPO即将发行，才导致当前窗口不再发业绩预告，需要等发行之后 2、Q2业绩： 在Q2物料紧张背景之下，我们预计公司Q2业绩仍会延续展示全球龙头风范、给予市场注入强信心 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 机构未识别/2026-07-15T13:22 | 高时效/3天 | 未披露 | 🪶展望三季度，供应商供应问题基本解决，截止到7月上旬供应商供货有序，若此情形保持，预计三季度环比二季度的收入、利润将呈现加速增长趋势，四季度有望继续维持高环比增速 风险提示：产业发展不及预期 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 机构未识别/2026-07-13T08:20 | 高时效/5天 | 未披露 | 中际旭创交流要点0712 中际旭创交流要点0712 Q... 中际旭创交流要点0712 Q2业绩以及近期股价传言：市场上关于公司业绩不及预期的传言无依据，不存在故意压制股价、延后确认收入等刻意调节的行为，公司重视资本市场形象与自身声誉，不会为配合潜在投资者获取低价位而突破经营底线 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI05 | 机构未识别/2026-07-08T08:38 | 有效窗口/10天 | 未披露 | 27年对于带宽需求增加，而3.2T在28年尚不具备量产能力，因此2.4T轻相干是很好选择，解决2-6km的集群链接需求，对于dsp、激光器要求低于相干产品，价格、毛利率预计好于1.6T PAM4产品 / 预计27-28年2.4T轻相干产品将成为重要的增长点 | [红包]我们认为公司业绩无忧，明年估值水平仅10倍左右，目前位置每次调整均是加仓时点，向上空间70%以上 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI06 | 机构未识别/2026-07-07T18:41 | 有效窗口/11天 | 未披露 | 野村将中际旭创2027年和20... 野村将中际旭创2027年和20... 野村将中际旭创2027年和2028年的收入、利润预测大幅上调 / 2027年： 收入预测从 2045亿元 上调到 2610亿元 / 归母净利润预测从 585亿元 上调到 734亿元 | 未提取到目标价/估值方法与倍数 | 2027E_收入=2045亿元 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI07 | 机构未识别/2026-07-07T12:40 | 有效窗口/11天 | 买入 | 📊我们上调 2027 财年、2028 财年全球 800G 光模块出货量预测，调整后数值分别为 5500 万只、7800 万只，此前预测数值为 5000 万只、7150 万只 / 💰我们将 2027 至 2028 财年营收、盈利预测分别上调 28% 至 37%、30% 至 38%，，上调依据为产品全面迭代带来的需求增量以及毛利率持续提升 / 🎯基于 2027 财年摊薄后每股收益 66.06 元人民币、20 倍市盈率（估值倍数维持不变）的测算逻辑，我们维持买入评级并将目标价上调至 1325 元人民币，该估值倍数与万得平台 A 股科技、电子元器件板块公司市盈率中位数保持一致 | 中际旭创（300308）：我们判断 2027 年后行业将迎来长期增长，增长由 2.4T/3.2T 光模块、近场封装光学、共封装光学技术驱动 💡维持买入评级，上调目标价至 1325 元人民币，对应上涨空间 20.6% 📉尽管近期人工智能基础设施板块股价出现回调，我们认为中际旭创 2026 至 2028 财年的核心成长驱动逻辑并未发生改变，核心分为两点，第一点是 1.6T 以及硅基光子光模块迎来产品迭代升级，第二点是近场封装光学、共封装光学市场规模持续扩张 / 🎯基于 2027 财年摊薄后每股收益 66.06 元人民币、20 倍市盈率（估值倍数维持不变）的测算逻辑，我们维持买入评级并将目标价上调至 1325 元人民币，该估值倍数与万得平台 A 股科技、电子元器件板块公司市盈率中位数保持一致 / 💴当前该股对应 2027 财年预期每股收益的市盈率为 16.6 倍 | 2027E_营收=28；2027E_EPS=16.6；target_price=1325元；rating=买入 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI08 | 浙商证券/2026-06-19T11:26 | 有效窗口/29天 | 未披露 | 20260618_甬兴证券-中际旭创(300308.SZ)-全球光模块龙头，1.6T放量驱动营收高增-2026-06-18.pdf url=https://files.zsxq.com/FjpPidxBF35_hPRXFyCHsgwy3K0q?e=1781872545&token=q6iZ0sQtf9U7s1qz0r4yMawNq3-u2w6lbnai6y2J:VmKYGjfem8UPqYOsS7MQZ8Ut1kg= local=data\knowledge_planet\reports\inbox\2026... | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI09 | 浙商证券/2026-06-19T11:26 | 有效窗口/29天 | 未披露 | 20260618_甬兴证券-中际旭创(300308.SZ)-全球光模块龙头，1.6T放量驱动营收高增-2026-06-18.pdf url=https://files.zsxq.com/FjpPidxBF35_hPRXFyCHsgwy3K0q?e=1781875328&token=q6iZ0sQtf9U7s1qz0r4yMawNq3-u2w6lbnai6y2J:ISL-vTS4oV22O-WHsYZs1tQfT8c= local=data\knowledge_planet\reports\inbox\2026... | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI10 | 浙商证券/2026-06-19T11:26 | 有效窗口/29天 | 未披露 | 20260618_甬兴证券-中际旭创(300308.SZ)-全球光模块龙头，1.6T放量驱动营收高增-2026-06-18.pdf url=https://files.zsxq.com/FjpPidxBF35_hPRXFyCHsgwy3K0q?e=1781888854&token=q6iZ0sQtf9U7s1qz0r4yMawNq3-u2w6lbnai6y2J:DQPqpzVesxjb4u8qzQEwt3yCcfs= | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
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