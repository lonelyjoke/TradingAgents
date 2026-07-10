# Forward Forecast Model Scaffold for 000933.SZ as of 2026-07-09

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 12408562541.64 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 33.4845% / +18.56pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.2215% / -0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.764 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 3.0156% / +0.40pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 7.7454% / -2.03pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
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
| KPE01 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 12408562541.64 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 33.4845% / +18.56pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 18.4525% / +11.10pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.2215% / -0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.764 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 8/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV030 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 2026年一季度报告: 2,271,764,611.82 714,922,693.47 217.76 净利润（元） 经营活动产生的现金流量净额（元） 4,039,054,901.65 1,687,756,817.40 1 |
| EV033 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 2026年一季度报告: 2,271,764,611.82 714,922,693.47 217.76 净利润（元） 经营活动产生的现金流量净额（元） 4,039,054,901.65 1,687,756,817.4... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 2026年一季度报告: 2,271,764,611.82 714,922,693.47 217.76 净利润（元） 经营活动产生的现金流量净额（元） 4,039,054,901.65 1,687,756,81... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 其他债权投资 长期应收款 长期股权投资 5,182,180,317.16 5,166,787,905.93 / long_term_equi... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | segment_volume | 2025, 年度 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgrade: 2025年年度报告: 2025 年，煤炭市场供需总体呈现宽松格局，供应方面国内煤炭产量在保供政策引导下维持高位，进口煤量虽同比有所 回落，但仍保持历史较高水平，需求方面受宏观经济增速放缓、能源... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 报告期末，公司铝加工板块应收账 款规模增加，根据会计政策以固定 17 信用减值损失 -7,873,058.09 -... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | revenue | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: 价值发生变动。 报告期内，公司铝加工板块量价齐 3 应收账款 1,461,917,412.34 1,069,147,929.52 36.74 升带动营收增长，叠加客户账期较 / receivables: 2026年一季度报告: 报告期内，公司铝加工板块量价齐 3 应... |
| EV045 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 8.5946 / earnings multiple the market is paying now / |
| EV046 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 1.0908 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 3.0156% / +0.40pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Aluminum (electrolytic) | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=unspecified; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| Coal | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2025H1; reported revenue=2887344129.29 (CNY); revenue weight=14.13%; growth=-18.99%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| Aluminum Foil | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q2; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=investor_interaction; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 48016243940 / current equity value / / / PE TTM / 8.5946 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: Missing diluted share count; EPS, per-share valuation and fair-value per share cannot be computed.; Aluminum electrolytic and aluminum foil segment-level cost, volume and margin data are not fully disclosed; analytical bridges required.; Capex/FCF derivation relies on limited cash-flow evidence; only Q1 2026 operating cash flow is directly sourced.; Segment revenue for aluminum foil is not separately reported; it is embedded in the non-ferrous metal segment.; One or more filing-reported segments required deterministic restoration.; Material segment three-year driver lines are missing: Aluminum (electrolytic), Aluminum Foil, Coal; Bull/base/bear per-share valuation is incomplete.; All claimed moat mechanisms remain unproven by observable evidence.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ (segment: realized sales volume × realized commodity price / processing fee). Aluminum and coal are priced near exchange benchmarks; coal has no long-term price lock (volume contracts only). Foil revenue is processing fee + aluminum pass-through.
- Profit: Gross profit = revenue – raw material (alumina, petroleum coke, coal for power) – energy (electricity, coal) – labour – depreciation. Operating profit = gross profit – selling/admin expenses – taxes/surcharges. Net profit = operating profit + investment income – finance costs – tax.
- Cash flow: Operating cash flow = net profit + depreciation – working capital change + other adjustments. Free cash flow = OCF – maintenance capex – expansion capex. Margin-driven with high fixed-cost absorption; OCF/ net profit ratio in Q1 2026 was 1.76x.
- Reinvestment: Both electrolytic aluminum and coal mining are capital-intensive with large ongoing maintenance capex. The new aluminum foil project (Shangqiu Phase 3) will require expansion capex. ROIC depends on commodity prices.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | What is the sustainable aluminum net margin per ton, and how does it respond to a 10% move in aluminum price versus alumina and electricity costs? | unresolved | Aluminum realized ASP (CNY/ton), Alumina cost per ton aluminum, Electricity cost per ton aluminum | 有色金属 segment revenue, gross margin, Consolidated parent net profit, OCF/FCF | Detailed unit cost build-up (alumina, electricity, carbon, labor per ton), Company-specific realized aluminum net-back price vs SHFE, Historical sensitivity of EBITDA to aluminum price changes;  |
| Q2 | Can coal segment volume stabilise and recover, and what is the ultimate free cash flow generation potential after maintenance capex, given structural demand headwinds? | unresolved | Coal sales volume (tons), Realized coking coal price (CNY/ton), Cash cost per ton | Coal segment revenue, operating profit, Consolidated parent net profit, FCF after coal mine sustaining capex | Coal production volume (annual), Segment operating margin, Mine maintenance capex required to sustain production;  |
| Q3 | Will the aluminum foil capacity expansion (Shangqiu Phase 3) earn a return on capital above the cost of capital, and can processing margins be preserved as supply increases? | unresolved | Foil processing margin (CNY/ton), Total project capex and commissioning date, Volume and product mix post-expansion | Aluminum foil revenue (within 有色金属), Consolidated capex, Consolidated FCF | Project economics: capex, expected processing fees, payback period, Current processing margin per ton;  |
| Q4 | What proportion of the +18.56pp YoY gross margin improvement in Q1 2026 is sustainable, and what are the main items (inventory gains, one-off cost relief, mix) that could reverse? | unresolved | Underlying core gross margin, Non-recurring adjustments (inventory valuation, asset sales) | Consolidated gross margin %, Consolidated operating margin %, Parent net profit | Quarterly breakdown of non-recurring items and inventory valuation effects, Management commentary on margin sustainability;  |
| Q5 | How will management allocate capital across dividends, buybacks, and growth capex in 2026-2028, and what is the resulting free cash flow yield for shareholders? | unresolved | Maintenance capex, Expansion capex for foil, Dividend payout ratio, Leverage policy | Consolidated FCF, DPS / payout, Share count (if buybacks) | Detailed capex budget by segment, Management capital allocation guidance, Explicit dividend policy;  |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 采掘业 (Coal) | Revenue | CNY mn | 5000.0 | 5200.0 | 5400.0 | 5500.0 | Coal volume × realized coal price. Base assumption: 5.0 Mt volume, ~1,040 CNY/ton (2025), rising to 5.2 Mt, ~1,038 CNY/ton | analyst_estimate | Driven by coking coal price and volume recovery from oversupply; Exact FY2025 coal revenue (derived from H1 weight applied to FY total) is analytical, not reported., Coal volume and ASP are analyst estimates; no disclosure. |
| 有色金属 (Aluminum Electrolytic & Ingot) | Revenue | CNY mn | 31000.0 | 33000.0 | 34000.0 | 35000.0 | Aluminum sales volume × ASP. Base: 1,350 kt × 22,950 CNY/ton (2025 est.), ramping to 1,400 kt × 23,570 CNY/ton (2026E) | analyst_estimate | Aluminum price (SHFE ~23,060 CNY/ton) and volume; foil revenue embedded; Electrolytic aluminum volume and ASP not disclosed; foil revenue is included, causing mix blur., Aluminum average realized price vs. futures unknown. |
| consolidated | Revenue | CNY mn | 41240.76 | 50000.0 | 52500.0 | 55000.0 | Coal revenue + Aluminum revenue (包铝箔) + other minor adjustments. Derived from segment assumptions and Q1 2026 seasonality indication. | analyst_estimate | Driven by commodity prices and volume; +1% revenue ~+180 mn net profit at current margins.; Actual FY2026 quarterly composition; full-year volume/price not reported. |
| consolidated | Gross Margin | % | None | 32.0 | 29.0 | 27.0 | (Revenue - COGS) / Revenue. Q1 2026: 33.48%, assumed gradually declining as commodity prices normalize. | analyst_estimate | Margin assumption directly sets gross profit; each 1pp = ~500 mn pre-tax; FY2025 gross margin not available; only Q1 2026 spike is reported. |
| consolidated | Operating Margin | % | None | 27.0 | 24.0 | 22.0 | Operating profit / revenue. Q1 2026: 29.18%; assuming higher SG&A as foil ramps. | analyst_estimate | Operating profit directly variable; each 1pp = ~500 mn pre-tax; Full-year FY2025 operating margin not disclosed in evidence. |
| consolidated | Operating Profit | CNY mn | None | 13500.0 | 12600.0 | 12100.0 | Revenue × Operating margin | analyst_estimate | Directly drives earnings before financial items; Revenue and margin are estimates; no full-year 2025 operating profit in evidence. |
| consolidated | Parent Net Profit | CNY mn | 4005.36 | 9000.0 | 8500.0 | 8000.0 | Operating profit - finance costs + investment income - tax. Effective tax rate ~25%. Q1 net margin 18.45% suggests 2026E 18%. | analyst_estimate | Core for EPS; each 1% revenue shift changes parent profit ~180 mn; Full-year tax rate and investment income not forecasted; simple margin approach used. |
| consolidated | EPS | CNY | None | None | None | None | Parent net profit / diluted share count. Share count unknown; cannot compute. | missing | ; Diluted share count is missing; cannot calculate EPS. |
| consolidated | OCF | CNY mn | None | 13500.0 | 12750.0 | 12000.0 | Net profit × OCF/NI ratio (assumed 1.5x). Q1 2026 ratio was 1.76x, normalized. | analyst_estimate | OCF funds capex and dividends; ratio reflects working capital quality; FY2025 OCF not provided; estimate based on Q1 dynamics and profit. |
| consolidated | Capex | CNY mn | None | 3000.0 | 3500.0 | 4000.0 | Maintenance + expansion capex. Expansion for Shangqiu Phase 3 assumed to ramp; maintenance ~2,000 mn/year. | analyst_estimate | Capex overruns or delays impact FCF and project returns; No detailed capex breakdown disclosed; Q1 2026 cash flow statement not fully available. |
| consolidated | FCF | CNY mn | None | 10500.0 | 9250.0 | 8000.0 | OCF - Capex | analyst_estimate | FCF yield is the key valuation anchor; each 1,000 mn change alters equity value by ~8,000 mn at 8x; Capex breakdown not verified; OCF relies on profit estimates. |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until cross-check with filings/Tushare/price-volume/announcements before hard use | Clear mapping to company-specific variable; the evidence is a general market structure note with no direct reference to 000933.SZ. |
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