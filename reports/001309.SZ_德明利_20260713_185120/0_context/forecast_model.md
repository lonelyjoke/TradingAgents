# Forward Forecast Model Scaffold for 001309.SZ as of 2026-07-13

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 7538357736.63 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 57.4202% / +51.57pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.5682% / -1.17pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / -0.072 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 3.4858% / -8.38pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 40.4323% / -47.33pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Consolidated revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Enterprise Storage revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| Consolidated | period=FY2025 for revenue, Q1 2026 for margin; revenue=10789100246.68 CNY; revenue_weight=100.0%; growth=126.07%; gross_margin=57.4202% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| Enterprise Storage | period=unspecified; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| Consolidated | revenue_weight=100.0%; growth=126.07%; gross_margin=57.4202%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| Enterprise Storage | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | missing; generate from revenue mix and business attributes |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | missing; infer and label evidence limits |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | missing; answer qualitatively with evidence boundaries |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | LLM analysis layer unavailable; deterministic facts may be used, but business questions, expectation gap, red-team critique and editorial synthesis must be regenerated before publishing a high-conviction PM report. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | missing; compare against valuation and market-expectation context |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | missing; produce strongest bear/upside mechanism |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | missing; explain operating-variable transmission |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | missing; PM must synthesize and compress |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | segment revenue | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment gross margin | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 7538357736.63 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 57.4202% / +51.57pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 44.3888% / +49.91pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.5682% / -1.17pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / -0.072 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / receivables: 2026年一季度报告: 致 主要系销售收入增长，收到的银行承兑 应收票据 87,806,024.36 44,174,114.66 98.77% / receivables: 2026年一季度报告: 主要系销售收入增长，收到的银行承... |
| EV031 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: 致 主要系销售收入增长，收到的银行承兑 应收票据 87,806,024.36 44,174,114.66 98.77% / receivables: 2026年一季度报告: 主要系销售收入增长，收到的... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / construction_in_progress: 2026年一季度报告: 资产负债表 项目 主要系公司提升产能，在建厂房装修及 在建工程 187,507,506.34 131,981,261.64 42.07% / con... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 所致 主要系应收账款增加，按账龄计提的坏 信用减值损失 -6,121,967.35 -4,618,191.27 3... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 致 主要系销售收入增长，收到的银行承兑 应收票据 87,806,024.36 44,174,114.66 98.77% / receivables: 2026年一季度报告: 主要系销售收入增长，收到的银行承兑 应收票据 87,806,024.36 44,174,11... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 研发费用 291,693,469.46 203,219,613.59 43.54% 支付费用增加所致 ... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/10; core pack ready. Annual base text and quarterly che... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | asp_or_price | 2025, 年度 | / high_r_and_d_technology / 高研发技术产品型 / quantified disclosure / 2025年年度报告: 片到解决方案的战略闭环。公司通过构建分层、模块化的公共研发平台来厚植技术根基，加速自研算法与关键 IP 的组件 公司将围绕“自主可控、生态共赢”策略，强化产业链上下游深度融合，以此加快客户产品导入，同时构建安全、 5.实施长效激励夯实创新发展根基，以国际化视野建设研发队伍 / 重点验证产品代际、客户认证、研发转化率、ASP/毛利率、供应链瓶颈、资本开支和库存风险。 / |
| EV058 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 44.2226 / earnings multiple the market is paying now / |
| EV059 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 10.6277 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 3.4858% / -8.38pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Consolidated | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY2025 for revenue, Q1 2026 for margin; reported revenue=10789100246.68 (CNY); revenue weight=100.0%; growth=126.07%; gross margin=57.4202%; margin change=51.57pp; source=earnings_model; mode=llm_semantic |
| Enterprise Storage | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 181471943088 / current equity value / / / PE TTM / 44.2226 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Research readiness: blocked
- Readiness reasons: LLM company underwriting failed; only deterministic skeleton is available.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 
- Profit: 
- Cash flow: 
- Reinvestment: 

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | revenue |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | gross_margin |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | operating_profit |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | parent_net_profit |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | EPS |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | OCF |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | capex |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |
| consolidated | FCF |  | None | None | None | None | requires company-specific operating bridge | missing | ; LLM underwriting model unavailable |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | Consolidated | market_share | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE02 | Consolidated | revenue | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE03 | Consolidated | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE04 | Consolidated | segment_margin | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-10T08:45 | 高时效/3天 | 未披露 | 未提取到带期间的明确盈利预测 | 当前市场仅仅把其当作与德明利类似的存储涨价标的，安凯微是稀缺的“芯片设计+内置存储合封”周期成长股，既有存储上行红利，又拥有端侧AI成长叙事，估值修复空间充足 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-10T08:17 | 高时效/3天 | 未披露 | 看好国内设计公司毛利率、利润率高弹性！涨价弹性，利基型存储涨价25Q4后半段刚开始落地，26年利基存储涨价有望贯穿全年且涨幅不小，结合利润率弹性，设计公司是营收↑*利润率↑双重弹性，看好业绩巨大弹性！ 建议关注存储设计公司：兆易、普冉、东芯、君正、恒烁、澜起、聚辰、国科微、联芸等，模组公司：佰维、江波龙、德明利、香农、大普微、朗科等 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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