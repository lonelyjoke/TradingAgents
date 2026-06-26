# Forward Forecast Model Scaffold for 601168.SH as of 2026-06-26

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 18723663755 / N/A / top-line starting point for volume × price × mix /
- / Gross margin / 22.6008% / +3.04pp / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.8033% / -0.18pp / captures leverage drag or relief /
- / OCF / net profit / 2.587 / N/A / tests earnings quality and cash realization /
- / Receivables / revenue / 0.8783% / -2.46pp / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 7.4074% / -0.94pp / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Mining revenue | equity copper/by-product output x realized selling price | reserve grade, recovery, mine life, ramp schedule, realized price versus SHFE/LME/COMEX proxy |
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