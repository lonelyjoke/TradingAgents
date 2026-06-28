# Forward Forecast Model Scaffold for 300750.SZ as of 2026-06-27

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 129131041000 / N/A / top-line starting point for volume × price × mix /
- / Gross margin / 24.8156% / -1.46pp / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.0482% / +1.92pp / captures leverage drag or relief /
- / OCF / net profit / 1.6241 / N/A / tests earnings quality and cash realization /
- / Receivables / revenue / 15.1878% / -3.65pp / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 21.0912% / -1.22pp / tests inventory build and demand quality; interim periods use annualized revenue /
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
| evidence_id | affected model variable | permitted use | verification gate |
| --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 |
| KPE02 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | 订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏 |
| KPE03 | new-business revenue / capex / scenario probability | private/proxy prior; quantify delta or reject, never use as a hard fact | 公告、财务、同行、价格成交、后续调研或可观察代理指标 |
| KPE04 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use |
| KPE05 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use |
| KPE06 | new-business revenue / capex / scenario probability | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use |
| KPE07 | new-business revenue / capex / scenario probability | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use |
| KPE08 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

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