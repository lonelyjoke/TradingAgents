# Forward Forecast Model Scaffold for 300750.SZ as of 2026-06-28

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
- Missing shipment, ASP, utilization, or segment-margin evidence must remain an explicit model gap and cap conviction; narrative strength cannot fill a numeric cell.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | scenario probability before->after or watch/reject |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 | numeric assumption delta or explicit rejection |
| KPE03 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | 公告、财务、同行、价格成交、后续调研或可观察代理指标 | scenario probability before->after or watch/reject |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE07 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
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
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 宁德时代新能源科技股份有限公司 2026 年第一季度报告 长期应收款 453,654 386,180 长期股权投资 67,874,958 6... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 260,272 25,565 填列） 信用减值损失（损失以“-”号填列） -250,651 -131,798 / ... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 交易性金融资产 60,352,395 58,993,528 衍生金融资产 1,754,079 1,133,502 应收票据 738,465 1,380,016 / receivables: 2026年一季度报告: 衍生金融资产 1,754,079 1,133,502... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 球能源结构的根本变革。 而这无限机遇，我们也将始终与股东共同见证、共同分享。公司延续高比例分红的政策，... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 22.3199 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.7655 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 15.1878% / -2.62pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Power battery revenue | GWh shipments x ASP | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Energy-storage revenue | GWh shipments x ASP | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Materials / recycling / other | volume x realized spread or service revenue | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Gross profit | segment revenue x segment gross margin | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Operating profit | gross profit - R&D - SG&A | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 1762744925100 / current equity value / / / PE TTM / 22.3199 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | / 2026-06-22 / valuation_method / pdf_text_available / 价格方面，碳酸锂价格高位可持续，电池价格传导顺畅，产业链龙头 Q2 盈利水平预计依旧亮眼，铜 箔、隔膜、铝箔等二轮涨价近期有望落地，估值已回调至27 年 15x，Q3 旺季行情确定，首推宁德时代、亿 纬锂能等，重点看好恩捷股份、佛塑科技、璞泰来、鼎胜新材、科达利、富临精工、天赐材料、湖南裕能... / compare with TradingAgents valuation bridge, PE/PB decomposition, and downside support / | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Assumption Change And Valuation Transmission Ledger
| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |
- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.
- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
| KPE02 | unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
| KPE03 | unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
| KPE04 | unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
| KPE05 | unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
| KPE06 | unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
| KPE07 | unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
| KPE08 | unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | segment mapping, baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Mandatory Three-Year Table
| item | 2026E | 2027E | 2028E | evidence / assumption status |
| --- | --- | --- | --- | --- |
| Revenue | to be estimated | to be estimated | to be estimated | reconcile segment volume, ASP, mix, and eliminations |
| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |
| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |
| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |
| Operating cash flow / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and capex |

## Analyst Instructions
- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.
- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.
- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.
- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.