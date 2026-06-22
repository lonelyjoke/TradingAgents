# Forward Forecast Model Scaffold for 601166.SH as of 2026-06-22

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Net profit run-rate / 23832000000 / 0.1513% / starting point for bank EPS; use seasonality-adjusted profit, not generic sales-volume logic /
- / ROE / ROA / ROE 2.6272% / ROA N/A / N/A / connect PB valuation to sustainable profitability and cost of equity /
- / Required bank filing metrics / NIM, loan yield, deposit cost, NPL, special-mention, overdue, provision coverage, CET1 / read from Banking KPI Pack / core bank earnings bridge; do not substitute gross margin, inventory, receivables, or OCF ratios /
- - Do not use manufacturing-style revenue = volume × price × mix, gross margin, inventory, receivables, or OCF conversion as primary bank drivers.
- - Do not upgrade a rating because PB/PE is low; upgrade only when the bank-specific earnings or valuation bridge improves.
- # Company Business Model Primer for 601166.SH as of 2026-06-22
- - Purpose: make the reader understand how the company earns money before valuation or cycle language.
- - / core_revenue_engine / annual / 兴业银行2025年年度报告: 息科技投入76.14亿元，占公司营业收入的比重为3.58%。 能交互，报告期内服务客户超5,500万人次 ；AI营销策略累 / Defines what actually drives the income statement. /
- - / geography / annual / 兴业银行2025年年度报告: 线上下、本外币、离在岸、商投行“五位一体”的国际业务 1,432个。 / Explains whether growth depends on a specific geography or expansion lane. /

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Mining revenue | equity output by metal x realized selling price | reserve grade, recovery rate, mine life, ramp schedule, realized price versus SHFE/LME/COMEX proxy |
| Smelting / refining spread | processed volume x TC/RC or processing margin | concentrate supply, treatment/refining charges, utilization, power and energy cost |
| Trading / pass-through revenue | traded volume x thin gross spread | inventory exposure, customer credit, working-capital intensity; do not value like scarce resources |
| Gross profit | mining gross profit + smelting spread + by-product credits - unit cash/AISC cost | cash cost, AISC/unit cost, sustaining capex, FX, energy/labor, product mix |
| NAV / SOTP value | mine-by-mine NAV + smelting/trading earnings value + project optionality | capex, construction-in-progress, commissioning, permitting, jurisdiction risk, discount/haircut |
| net profit/EPS / FCF | operating profit - tax/minority/finance cost + working-capital/capex bridge | minority interest, debt maturity, OCF/NI, hedging/derivatives, inventory marks |

## Mandatory Three-Year Table
| item | 2026E | 2027E | 2028E | evidence / assumption status |
| --- | --- | --- | --- | --- |
| Revenue | to be estimated | to be estimated | to be estimated | tie to segment volume, ASP, and mix |
| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |
| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |
| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |
| Operating cash flow / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and capex |

## Analyst Instructions
- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.
- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.
- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.