# Forward Forecast Model Scaffold for 300274.SZ as of 2026-07-05

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 15560645284.03 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 33.2629% / -1.87pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 2.1051% / +2.42pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.5274 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 40.0672% / +4.58pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 44.5972% / +3.67pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Core revenue | category volume x ASP x product/channel mix | category growth, traffic/weather/catering recovery, regional penetration and product mix |
| Gross profit | revenue x gross margin | raw-material and packaging costs, price/mix, promotion intensity and logistics |
| Operating profit | gross profit - selling/admin/R&D expense | sales expense, channel rebates, scale leverage and brand investment |
| Cash profit / FCF | net profit + D&A - working capital - capex | contract liabilities/prepayments, inventory, receivables, OCF/NI and capex |
| Valuation bridge | normalized EPS/FCF x category-appropriate multiple with ROE/payout cross-check | growth durability, channel health, margin stability and shareholder return |

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE05 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 15560645284.03 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 33.2629% / -1.87pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 14.7248% / -5.37pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 2.1051% / +2.42pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.5274 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV026 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 9/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / gross_margin_not_reaching_operating_profit: 20251231->20260331: revenue growth -82.55%, gross margin change 1.43pp, operating margi |
| EV031 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026年一季度报告: 2,032,367,774.89 3,676,394,413.73 -44.72% 损益的净利润（元） 经营活动产生的现金流量净额（元） 1,208,404,186.03 1,790,260 |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / gross_margin_not_reaching_operating_profit: 20251231->20260331: revenue growth -82.55%, gross margin change 1.43pp, operating ma... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026年一季度报告: 2,032,367,774.89 3,676,394,413.73 -44.72% 损益的净利润（元） 经营活动产生的现金流量净额（元） 1,208,404,186.03 1,790,... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 其他债权投资 189,029,030.12 187,855,030.13 长期应收款 259,500,000.00 269,000,000.... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 80,128,206.97 36,832,829.23 43,295,377.74 117.55% 益 动所致； ... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 7,129,735,973.85 致； 主要系收到的银行承兑汇票 应收票据 2,513,346,567.63 1,233,619,771.56 1,279,726,796.07 103.74% / receivables: 2026年一季度报告: 主要系收到的银行承... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 公司设立中央研究院，做好前期高价值专利布局和技术难点攻关，为集团产品、技术开发提供高效的平台服务和创新... |
| EV046 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 21.9309 / earnings multiple the market is paying now / |
| EV047 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 3.0517 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| PV Inverters | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| Energy Storage Systems | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026 Q1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=30.0%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| Hydrogen Business | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
| AIDC Power Solutions | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 261556362840 / current equity value / / / PE TTM / 21.9309 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: Segment revenue and gross margin not disclosed for PV Inverters, ESS, Hydrogen, or AIDC; disaggregation relies on unverified sell-side proxies.; Diluted share count cannot be reliably computed from supplied evidence (Tushare total_share missing; market cap/price inconsistent; parent profit/EPS conflict).; Capex and FCF derived from limited Q1 filing extracts; full-year FY2025 cash-flow detail is unavailable.; AIDC Power Solutions and Hydrogen business are nascent and unquantified; only qualitative cue exists.; US exposure and tariff impact are debated but not reconciled with segment-level order data.; Forecast lines are analytical estimates pending company disclosure or verified third-party data.; Material segment three-year driver lines are missing: AIDC Power Solutions, Energy Storage Systems, Hydrogen Business, PV Inverters; Valuation closure conflicts with probability-weighted scenario value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Consolidated Revenue (CNY) ≈ Σ [segment shipments (GW/GWh/units) × segment ASP (CNY/W or CNY/Wh)] adjusted for regional mix and service/warranty revenue.
- Profit: Gross Profit = Revenue − Material/Battery/Component costs − Manufacturing overhead; Operating Profit = Gross Profit − R&D − Selling & Distribution − G&A; Parent Net Profit = Operating Profit + Investment/Fair-value movements − Finance costs − Tax − Minority interests.
- Cash flow: Operating Cash Flow = Parent Net Profit + Non-cash items (depreciation, impairment) ± Δ Working Capital (receivables, inventory, contract liabilities, prepayments); FCF = Operating Cash Flow − Capex (production lines, Poland factory, R&D facilities).
- Reinvestment: Revenue growth requires continuous R&D (≈4.7% of revenue) and capacity/buildout capex. ESS and PV inverter manufacturing is asset-light relative to chemicals/mining, but project-linked contract liabilities and receivables tie up working capital. Mid-term capex includes the Poland ESS factory (ramp-up H1 2027).

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ01 | What is the quantified impact of US inverter ban and EU public-fund exclusion on SunGrow's PV inverter revenue and margin? | Unresolved. Brokers (Citi, Goldman) suggest expectations are conservative; official IR notes EU exclusion is still administrative guidance. No segment revenue split available. | PV Inverter segment volume (GW) -> US/EU share, PV Inverter segment ASP, PV Inverter gross margin | Segment revenue; Consolidated revenue; Gross profit; Operating profit; Parent net profit; EPS | Company's US PV inverter order book and backlog in GW/CNY, Segment-level regulatory stress-test quantification, Q1 2026 US-specific revenue run rate; Track FCC rulemaking, Q2 2026 order commentary, and any company US/EU revenue disclosure. |
| UQ02 | Can SunGrow sustain >30% gross margin in Energy Storage Systems through 2026-2028 given battery cost trends, regional mix, and US tariff pull-forward? | Q1 2026 ESS gross margin improved to ~30%, mainly from regional mix shift to Europe. Company confirms cost pass-through varies by region (EV091). | ESS segment gross margin %, ESS segment revenue growth %, Regional mix (EU vs. US vs. China) share | ESS segment gross profit; Consolidated gross margin; Operating profit; Parent net profit; EPS | Monthly/quarterly ESS ASP and battery cost spread, Q2-Q4 2026 margin guidance from company, US vs. Europe order book by quarter; Q2 2026 ESS revenue and gross margin update; Polish factory commissioning progress. |
| UQ03 | When will contract liabilities of CNY 122 bn convert into revenue and at what margin? Can SunGrow accelerate delivery and cash collection? | Company refuses to give Q2 guidance. Contract liabilities up sharply; prepayments up 201% for material lock-in. Suggests confidence in large delivery pipeline. | Revenue recognition rate from backlog, Operating cash flow margin, Inventory turnover days | Consolidated revenue; Operating cash flow; Free cash flow; Net working capital | Project delivery schedule and revenue recognition milestones, Breakdown of contract liabilities by expected conversion quarter, Inventory composition (finished goods vs. raw materials); Q2 2026 quarterly report: revenue, OCF, and change in contract liabilities. |
| UQ04 | What is the capital allocation strategy—balancing high R&D/capex for AIDC and Hydrogen with shareholder returns? | R&D intensity about 4.7%; no explicit FCF or ROIC target given. Dividend of 0.69 CNY/share implemented May 2026 (yield ~1.7%). | Capex/Revenue ratio, FCF conversion rate, Dividend payout ratio | Free cash flow; Diluted EPS; Net cash position; ROIC | FY2026-2028 capex plan and expected ROIC for Poland and SST lines, Management's medium-term shareholder return policy (payout ratio target), Dilution from employee incentives or acquisitions; FY2026 interim report capex breakout and management discussion on capital allocation. |
| UQ05 | What is the realistic size and timeline of AIDC SST monetization, and should it receive explicit optionality value? | SST prototype ready; pilot orders in hundreds of MWh; no revenue or contract value disclosed. | AIDC segment revenue (CNY mn) in 2027-2028, AIDC segment gross margin | Optionality value per share; Fair value | First named customer and contract size, Expected commercial delivery date, Unit economics (ASP/unit, cost, margin); Company SST partnership announcement or first commercial order. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 89184.0 | 96318.0 | 100170.0 | 104177.0 | Base (FY2025) = 89,184 mn. 2026E growth +8% (moderate gain from ESS backlog conversion offset by US tariff drag). 2027E +4% (US gap partially offset by Europe/AIDC). 2028E +4% (steady state organic). | analyst_estimate | 1% revenue miss → ~CNY 963 mn; impacts EPS by ~0.25 CNY/share (using estimated 2,300 mn shares).; US policy outcome, Poland factory start-up delay or acceleration, AIDC SST first revenue, Detailed R&D breakdown by segment, One-off costs from Poland start-up |
| consolidated | Gross Margin | % | 31.83 | 32.7 | 33.0 | 33.4 | 2025 base = 31.8%. 2026E +0.9pp to 32.7% driven by ESS regional mix improvement and continued cost control. 2027E +0.3pp to 33% with ESS margin stabilizing and PV innovation. 2028E +0.4pp to 33.4% from AIDC SST high-margin contribution. | analyst_estimate | 50bp GM miss → ~CNY 480 mn less gross profit; ~0.12 CNY EPS impact.; ESS battery cost trajectory, PV inverter component cost inflation |
| consolidated | Gross Profit | CNY mn | 28390.0 | 31496.0 | 33056.0 | 34795.0 | Gross Profit = Revenue × Gross Margin %. | analyst_estimate | Derived from Revenue and GM.;  |
| consolidated | Operating Profit | CNY mn | 10500.0 | 12232.0 | 13323.0 | 14481.0 | Operating Profit = Gross Profit − (Revenue × SG&A/R&D ratio) − Other operating costs (assumed ~0.5% of revenue). | analyst_estimate | Benchmark for segment aggregation.;  |
| consolidated | Finance and Other Items | CNY mn | -500.0 | -600.0 | -400.0 | -300.0 | Net finance income/expense including interest, FX, and investment gains. 2026E slightly negative due to higher rates; 2027-2028E improvement from net cash interest income. | analyst_estimate | Small relative to operating profit.; FX hedge ratio and exposure, Interest rate assumptions |
| consolidated | Parent Net Profit | CNY mn | 13461.0 | 13726.0 | 15100.0 | 16474.0 | Parent Net Profit = (Operating Profit + Finance & Other Items) × (1 − effective tax rate ~12%) − minority interest (~2%). | analyst_estimate | EPS driver; 5% profit miss = ~0.30 CNY EPS (@ est. 2,300 mn shares).; Diluted share count for EPS calculation, One-off items or impairment |
| consolidated | EPS | CNY | None | None | None | None | EPS = Parent Net Profit / Diluted Shares. Not calculated because diluted shares are unresolved (Rule 5a). | missing | Cannot state without share count.; Diluted share count |
| consolidated | Operating Cash Flow | CNY mn | 16918.0 | 13726.0 | 15100.0 | 16474.0 | Assumed OCF/Net Profit ratio improves from 0.53 → 0.70 by 2028. 2026E ratio 0.60, 2027E 0.65, 2028E 0.70. | analyst_estimate | Cash conversion critical for valuation; 0.1 ratio swing = ~1.5 bn FCF difference.; Exact cash conversion cycle improvement milestones |
| consolidated | Capex | CNY mn | 6000.0 | 8000.0 | 6500.0 | 5500.0 | 2025 base estimated from R&D+core capex. 2026E elevated for Poland factory (EV040). 2027-2028E normalize to maintenance + expansion. | analyst_estimate | Capex/revenue ratio drops from 8.3% to 5.3%.; Detailed FY2026-2028 capex budget |
| consolidated | Free Cash Flow | CNY mn | 10918.0 | 5726.0 | 8600.0 | 10974.0 | FCF = Operating Cash Flow − Capex. | analyst_estimate | FCF yield improves from ~2.2% to ~4.2%.;  |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | Scenario probability before/after, Segment impact quantification |
| KPE02 | PV Inverters | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Cross-check with actual Q2 revenue and US shipment data | US revenue weight, Order cancellation probability |
| KPE03 | PV Inverters | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Cross-check with Q2 actual results and US policy developments | Scenario probability shifts |
| KPE04 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Cross-check with actual Q2 results | No variable mapped; narrative challenge only |
| KPE05 | PV Inverters | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Monitor FCC rulemaking and company US orders | Probability shifts |
| KPE06 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until Listen to transcript for specific guidance numbers | Content of exchange, Specific guidance |
| KPE07 | AIDC Power Solutions | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Track SST orders, customer qualifications, and AIDC capex announcements | Revenue base for AIDC, Order pipeline value |
| KPE08 | Energy Storage Systems | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Check Q2 ESS margin and product launch impact on valuation | Probability changes, Valuation multiple assumptions |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-03T09:35 | 高时效/2天 | 未披露 | 并配套电力成套开关、变电智能监测设备等 适配主网+风光氢储、火电、石油天然气、钢铁冶炼等多个领域，产品已出口至美/欧/澳及东南亚等市场 厂房 7.4 万㎡，设计年产能1800万kVA变电容量（产值估计可达到16-22亿元），具备成套生产和全套型式试验能力 海外缺什么？——排除主网进口禁令、AIDC中压段需求5年5倍 Wood Mackenzie认为2025-2030年美国AIDC电气设备市场将从200亿美元增至650亿美元，其中中压设备（10-110KV）包括开关柜、pad-mount箱变预计均有5倍增长 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-01T18:03 | 高时效/4天 | 未披露 | 另外即使是去年已经落地的OBBA法案，也预留了较长的缓冲期，目前公司在美国直到28H1的项目都已进入“安全港”，不受政策影响，后续即使有新政策落地，预计也影响有限 / 欧洲储能订单上修： 近期欧洲光储展会斩获较多订单，预计明年欧洲储能增速由40-50%上修至60%，且波兰产能明年上半年建成，进一步加强本地化服务能力 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI03 | 机构未识别/2026-07-01T18:03 | 高时效/4天 | 未披露 | 公司波兰工厂预计2027H1建成投产，主要满足欧洲本地化需求，助力获取更多本地订单 / 美国市场 • 美国本土逆变器品牌市场份额仅10%左右，构建完善的本土逆变器产业链预计需要5年时间，且存在建设周期长、成本高、供应链配套不足、功率半导体/MLCC等元器件短缺等难点 / • AIDC配储：数据中心配储趋势明确，未来将逐步成为标配，预计2026年下半年订单逐步增多，2027、2028年需求持续上量，欧洲、东南亚等地区的数据中心也有配储需求 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI04 | 中信建投/2026-07-01T11:12 | 高时效/4天 | 未披露 | 未提取到带期间的明确盈利预测 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI05 | 机构未识别/2026-06-26T10:33 | 有效窗口/9天 | 未披露 | 阳光电源：已成功研制出35k... 阳光电源：已成功研制出35k... author: 纪要小能手 阳光电源：已成功研制出35kV直降800V的6MVA的SST，进度领先全行业，完全简化整体配电架构，实现降维打击！预计2030年50GW2000亿市场，若获30%份额可贡献 超150亿元利润增量，给予20倍可再造一个阳光！ 同时，在海外大单支撑下，其储能毛利率已回升至约30%且量价稳固 / 保守预计明年公司主业利润将达180亿元（光伏50亿+储能120亿+其他10亿），按20倍PE测算，主业安全边际市值为3600亿元 | 保守预计明年公司主业利润将达180亿元（光伏50亿+储能120亿+其他10亿），按20倍PE测算，主业安全边际市值为3600亿元 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI06 | 中信建投/2026-06-22T13:51 | 有效窗口/13天 | 未披露 | 同时美国订单去年Q4已回复，下半年交付起量，预计对盈利能力形成明显支撑，IEEPA关税退还、碳酸锂跌价，也将助力业绩修复 | ➡投资建议： 主业：保守给予明年主业180亿（光伏50亿+储能120亿+其他10亿），储能120亿=明年出货80GWh×单位盈利0.15元/Wh，估值20X给予3600亿主业市值 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
| KSI07 | 机构未识别/2026-06-15T08:46 | 有效窗口/20天 | 推荐措辞（非标准评级） | 海外储能集成壁垒高（本地化服务、快速交付、产品可靠性、认证等），公司长期竞争力转化为盈利优势，我们预计中长期储能毛利率维持25%-30% / 礼物预计2026-2027年归母净利润135、190亿元，对应PE 23、16倍，继续重点推荐！ | 礼物预计2026-2027年归母净利润135、190亿元，对应PE 23、16倍，继续重点推荐！ | 2026E_归母净利润=135；rating=推荐措辞（非标准评级） | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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