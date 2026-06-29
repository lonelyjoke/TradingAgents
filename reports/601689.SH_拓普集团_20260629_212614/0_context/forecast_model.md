# Forward Forecast Model Scaffold for 601689.SH as of 2026-06-29

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 6628185769.77 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 19.2562% / -0.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.455% / +1.36pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.9917 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 21.5404% / -0.89pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 16.3813% / -0.19pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Core product revenue | sum(customer vehicle volume x platform share x content per vehicle), cross-checked with segment units x ASP | customer/model exposure, SOP cadence, annual price reductions and product mix |
| Segment gross profit | sum(segment revenue x segment gross margin) | ASP, material pass-through, utilization, launch/ramp cost and mix |
| Operating profit | segment gross profit - R&D - selling/admin - impairment | R&D conversion, scale leverage, depreciation and credit risk |
| Parent net profit / EPS | operating profit +/- finance and FX - tax - minority; divided by diluted shares | interest versus FX decomposition, subsidies/one-offs and share count |
| OCF / capex / FCF / incremental ROIC | net profit + D&A - working capital - capex; incremental EBIT after tax / incremental invested capital | receivables, inventory, new-plant ramp, capex discipline and cash conversion |
| Second-curve scenario value | qualified delivered units x ASP x margin, valued separately until unit economics and cash conversion are verified | customer nomination, order-to-revenue schedule, capex, utilization and probability |

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 6628185769.77 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 19.2562% / -0.64pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 8.3251% / -1.48pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 1.455% / +1.36pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.9917 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 9/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV030 | financial_report_intelligence | primary_or_structured_filing | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.59%, gross margin change -0.17pp, operating margin change  |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.59%, gross margin change -0.17pp, operating margin chan... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.59%, gross margin change -0.17pp, operating margin c... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 拓普集团2026年第一季度报告: 其他债权投资 长期应收款 长期股权投资 113,137,486.17 105,254,429.52 / long_term_equ... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 拓普集团2026年第一季度报告: 公允价值变动收益（损失以“-”号 填列） 信用减值损失（损失以“-”号填列） 77,642,035.79... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 拓普集团2026年第一季度报告: 交易性金融资产 601,000,000.00 400,000,000.00 衍生金融资产 应收票据 26,062,354.01 15,798,084.56 / receivables: 拓普集团2026年第一季度报告: 衍生金融资产 应收票据 26,062... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 拓普集团2025年年度报告: 余未分配利润滚存至下一年度。 如在本利润分配预案披露之日至实施权益分派的股权登记日期间，公司总... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 32.8978 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 2.9885 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| consolidated | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q1; reported revenue=6628185769.77 (CNY); revenue weight=100.0%; growth=None%; gross margin=19.2562%; margin change=-0.64pp; source=earnings_model; mode=llm_semantic |
| robot_actuator | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 汽车零 减少 1.38 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=27524056756.31 (filing table unit not explicit in extracted row); revenue weight=86.60912686083745%; growth=10.04%; gross margin=18.04%; margin change=11.93pp; source=filing_intelligence; mode=deterministic_filing_row |
| 减震系 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=4255569426.2 (filing table unit not explicit in extracted row); revenue weight=13.390873139162546%; growth=-3.33%; gross margin=20.27%; margin change=-2.32pp; source=filing_intelligence; mode=deterministic_filing_row |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 90975693660 / current equity value / / / PE TTM / 32.8978 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
| KPE01 | robot_actuator | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline scenario probability, baseline revenue assumption for robot segment, unit of measure |
| KPE02 | robot_actuator | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline scenario probability, baseline revenue assumption for robot segment, unit of measure |
| KPE03 | robot_actuator | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline scenario probability, baseline revenue assumption for robot segment, unit of measure |
| KPE04 | robot_actuator | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline scenario probability, baseline revenue assumption for robot segment, unit of measure |
| KPE05 | robot_actuator | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline scenario probability, baseline revenue assumption for robot segment, unit of measure |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

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