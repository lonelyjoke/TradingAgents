# Forward Forecast Model Scaffold for 601888.SH as of 2026-06-30

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 16906021992.25 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 33.6318% / +0.65pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / -1.013% / +0.20pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.6568 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 0.2455% / -0.16pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 23.4993% / -0.02pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Mobile service revenue | mobile subscribers x mobile ARPU | 5G penetration, package mix, churn, DOU, pricing discipline |
| Broadband / home revenue | broadband subscribers x household ARPU | gigabit penetration, smart-home attach, bundling |
| Enterprise / cloud / AI revenue | customer count x cloud/IDC/AI ARPU or project revenue | cloud growth, AI paid adoption, IDC utilization, contract liabilities |
| EBITDA / operating profit | service revenue x margin - depreciation - SG&A/R&D | network scale, cloud gross margin, depreciation, personnel and maintenance cost |
| net profit/EPS / dividend capacity | operating profit - tax/minority + FCF after capex | capex-to-revenue, OCF/NI, payout ratio, net cash/debt |

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 16906021992.25 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 33.6318% / +0.65pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 13.8903% / +2.32pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / -1.013% / +0.20pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.6568 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV026 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 10/10 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV028 | financial_report_intelligence | primary_or_structured_filing | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -68.51%, gross margin change 0.88pp, operating margin change 6.64pp, OC |
| EV031 | financial_report_intelligence | primary_or_structured_filing | reported | revenue | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 中国旅游集团中免股份有限公司2026年第一季度报告: 2,337,473,944.03 1,935,678,057.03 20.76 经常性损益的净利润 经营活动产生的现金流量净额 3,890,593,863.77 |
| EV032 | industry_kpi | secondary_or_derived_research | reported | revenue | unspecified | / Mobile / mobile subscribers, 5G penetration, mobile ARPU, DOU, churn, package mix / service revenue and margin durability / |
| EV033 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | unspecified | / Capex / 5G/cloud/AI capex, depreciation, network utilization, capex-to-revenue / FCF and ROIC / |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / leverage_funding_growth: 20251231->20260331: revenue growth -68.51%, gross margin change 0.88pp, operating margin change 6.64pp,... |
| EV038 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 中国旅游集团中免股份有限公司2026年第一季度报告: 2,337,473,944.03 1,935,678,057.03 20.76 经常性损益的净利润 经营活动产生的现金流量净额 3,890,593,863... |
| EV039 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 中国旅游集团中免股份有限公司2026年第一季度报告: 其他债权投资 长期应收款 长期股权投资 3,521,892,787.37 3,555,925,424.25 /... |
| EV040 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 中国旅游集团中免股份有限公司2026年第一季度报告: 净敞口套期收益（损失以“-”号填列） 公允价值变动收益（损失以“-”号填列） 信用减... |
| EV041 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 中国旅游集团中免股份有限公司2026年第一季度报告: 衍生金融资产 应收票据 应收账款 165,988,736.55 72,759,182.37 / receivables: 中国旅游集团中免股份有限公司2026年第一季度报告: 应收票据 应收账款 165,988,736.55 72,75... |
| EV042 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 中国旅游集团中免股份有限公司2025年年度报告: 本为基数，向全体股东每10股派发现金红利人民币4.50元（含税）。截至本报... |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 主营业务 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY2025; reported revenue=52552697083.91 (CNY); revenue weight=97.9%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
| 其他业务 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=FY2025; reported revenue=1140882117.61 (CNY); revenue weight=2.1%; growth=None%; gross margin=None%; margin change=Nonepp; source=company_business_model; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 111369897760 / current equity value / / / PE TTM / 27.866 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | / 2026-06-20 / earnings_forecast / pdf_text_available / 归⺟净利润 35.86亿元，同⽐下降 15.96%，降幅较2024年显著收窄 / compare with TradingAgents earnings model, Tushare financials, and forward forecast scaffold / | label broker/date/count; use range or median only when the source is company-specific |
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
- Readiness reasons: Segment-level channel breakdown (Hainan offshore, airport, online, DFS) not disclosed; revenue/profit-weight allocation is missing.; Q1 2025 comparable revenue/earnings figures absent; YoY growth rates are inferred from margin changes only.; No sell-side consensus or internal baseline forecasting assumptions supplied; forecast scaffold uses Q1 2026 annualised/reference PDF figures.; KPE evidence items (KPE01, KPE02) have no content to map to model variables; they remain on watch.; Conflict EV036 (revenue growth -68.51%) unresolved; reliance on direct reported figures from EV011/EV012.; EPS forecast lacks a validated CNY-million parent-profit / diluted-share-count bridge.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Revenue = Σ (Channel footfall × Conversion rate × Average transaction value) ≈ Main business duty-free retail across offshore island, airport, city downtown, online, and DFS Greater China channels. Revenue is volume-driven with some ASP mix uplift from luxury goods.
- Profit: Gross profit = Revenue - cost of goods sold (brand purchases, logistics). Operating profit = Gross profit - selling & administrative expenses (concession fees, labour, marketing, depreciation) - R&D. Net profit = Operating profit + non-operating items - tax. Q1 2026 margin structure: gross 33.6%, operating 16.5%, net 13.9%.
- Cash flow: OCF from strong cash conversion (OCF/net profit ratio 1.66x in Q1 2026) as duty-free sales are largely cash/card; working capital is inventory-heavy but stable (inventory/revenue ~23.5% of annualized revenue). FCF = OCF - capex (store expansion, digital systems, DFS integration).
- Reinvestment: Asset-light retail model; main capex goes to new store fit-out, leasehold improvements, digital platform, and M&A (DFS). FY2025 R&D expense surged 352.74% for digitalization. Intangible amortisation partly capitalised into construction-in-progress.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | What is the sustainable revenue growth rate for the duty-free main business, broken down by Hainan offshore, airport, online, and DFS channels, and what drives volume vs ASP? | unresolved | segment revenue by channel, volume growth (footfall, conversion), ASP trend | revenue, revenue growth, gross profit, EPS | Segmented revenue by channel (Hainan airport/offshore, city, online, DFS), Historical footfall and conversion data, Competitor market share shifts; H1 2026 report segment revenue, Q2 2026 management call commentary on channel trends. |
| Q2 | How sustainable and improvable is the gross margin at ~33.6%, considering brand mix, procurement scale, DFS lower-margin retail, and potential concession fee renegotiations? | unresolved | consolidated gross margin, brand procurement terms, concession cost structure, DFS margin impact | gross margin, operating margin, net profit, EPS | DFS segment gross margin stand-alone, Blended Hainan and airport channel margins, Details of new airport concession fee agreements; H1 2026 gross margin and management discussion of DFS integration and concession costs. |
| Q3 | What is the true cash conversion and free cash flow generation of the business once DFS integration capex, working capital needs, and tax payments are normalised? | unresolved | operating cash flow, capex, free cash flow | OCF, FCF, dividend per share | Detailed capex plan for DFS integration and store network, Normalised working capital cycle, Cash tax rate; H1 2026 cash flow statement and management guidance on capex and dividend. |
| Q4 | What is the EPS impact of the DFS acquisition (including one-off integration costs, H-share issuance dilution, and synergy realisation), and what is the path to accretion? | unresolved | DFS revenue contribution, DFS margin, integration costs, share count | parent net profit, diluted EPS, FCF | DFS segment P&L post-acquisition, Number of new H-shares issued, One-off integration cost schedule; Full-year 2026 filing with DFS pro-forma and segment note. |
| Q5 | Can the current market valuation (PE TTM 27.9x, PS 2.07x) be justified by the earnings growth trajectory implied by our base case (~40% profit growth in 2026E) and structural moat? | unresolved | fair PE multiple, earnings growth, competitive position | fair value per share, P/E ratio | Peer-implied multiple range justified by ROIC and growth, Precise share count for PE computation; Peer analysis using Tushare peer table, review of management capital allocation history. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 主营业务 | revenue | CNY mn | 52552.697 | 57808.0 | 63589.0 | 69948.0 | base_value * (1+10%) for 2026E, then +10%, +10% driven by tourism recovery, DFS contribution, and policy uplift. | assumed | 1% revenue change = ~CNY 580mn in 2026E, affecting gross profit by ~CNY 195mn.; Channel-level build-up, DFS organic growth vs base |
| 其他业务 | revenue | CNY mn | 1140.882 | 1140.882 | 1140.882 | 1140.882 | held flat, given lack of disclosure and immateriality. | assumed | negligible; Business nature and growth prospects |
| consolidated | revenue | CNY mn | 53693.579 | 58948.882 | 64729.882 | 71088.882 | sum of segment revenues; base from EV012. | computed | top-line driver for margins and cash flow;  |
| consolidated | gross_margin | % | None | 34.5 | 35.0 | 35.5 | Q1 2026 actual 33.63%, +1pp improvement per year from mix, scale, and DFS synergies. | assumed | 1pp change shifts gross profit by CNY 590-711mn.; FY2025 actual gross margin for calculation |
| consolidated | operating_margin | % | None | 17.5 | 18.5 | 19.5 | Q1 2026 actual 16.52%, +1pp per year from operating leverage and cost control. | assumed | operating leverage sensitivity; FY2025 actual operating margin |
| consolidated | operating_profit | CNY mn | None | 10316.0 | 11975.0 | 13862.0 | revenue * operating_margin | computed | revenue and margin interaction; FY2025 operating profit for base |
| consolidated | parent_net_profit | CNY mn | 3586.178 | 5000.0 | 5930.0 | 5990.0 | Based on reference research (Great Wall Securities) forecast: 2026E 50亿, 2027E 59.3亿, 2028E 59.9亿; consistent with margin recovery and moderate revenue growth. | assumed (from external PDF reference) | dominant driver of EPS and valuation; Tax rate, minority interest allocation |
| consolidated | eps | CNY | None | 2.41 | 2.85 | 2.88 | parent_net_profit / diluted_share_count (assumed 2078 mn shares from Tushare reg_capital). | calculated | share count and profit; Accurate diluted share count including H-shares post-DFS |
| consolidated | ocf | CNY mn | None | 7500.0 | 8895.0 | 8985.0 | parent_net_profit * 1.5x cash conversion (conservative vs Q1 1.66x). | assumed | cash conversion rate; FY2025 OCF |
| consolidated | capex | CNY mn | None | 2000.0 | 1800.0 | 1600.0 | moderate capex for store maintenance and digital; DFS integration spend front-loaded. | assumed | directly affects FCF; FY2025 capex, DFS capex plan |
| consolidated | fcf | CNY mn | None | 5500.0 | 7095.0 | 7385.0 | OCF - capex | computed | dividend capacity;  |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Cross-check with filings/Tushare/price-volume/announcements before hard use | Full content of the research note, Affected variable mapping, Baseline and revised values, Scenario probabilities |
| KPE02 | consolidated | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until Cross-check with filings/Tushare/price-volume/announcements before hard use | Full content of the research report, Affected variable mapping, Model conflict outcome |
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