# Forward Forecast Model Scaffold for 300285.SZ as of 2026-06-12

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 1064111443.98 / N/A / top-line starting point for volume × price × mix /
- / Gross margin / 36.7357% / N/A / main bridge from demand to gross profit /
- / OCF / net profit / 1.1869 / N/A / tests earnings quality and cash realization /
- / Receivables / revenue / 47.0828% / -0.10pp / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 22.2817% / +5.34pp / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.
- - Do not upgrade a rating because a story is attractive; upgrade only when the earnings bridge or valuation bridge improves.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Cathode / material revenue | shipment volume x cathode ASP | LFP/ternary demand, customer order cadence, pass-through clauses |
| Manufacturing spread | cathode ASP - lithium carbonate / precursor / energy / processing cost | raw-material price, inventory-cost lag, processing fee |
| Gross profit | shipment volume x unit spread | capacity utilization, yield, depreciation, product mix |
| Operating profit | gross profit - R&D - SG&A - credit impairment | customer concentration, receivables, scale leverage |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | OCF/NI, inventory, capex, expansion cycle |

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