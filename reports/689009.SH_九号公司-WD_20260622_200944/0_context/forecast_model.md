# Forward Forecast Model Scaffold for 689009.SH as of 2026-06-22

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 5869970864.48 / N/A / top-line starting point for volume × price × mix /
- / Gross margin / 26.5415% / -3.09pp / main bridge from demand to gross profit /
- / Finance-expense ratio / 3.8088% / +4.71pp / captures leverage drag or relief /
- / OCF / net profit / -2.3433 / N/A / tests earnings quality and cash realization /
- / Receivables / revenue / 7.0628% / -0.57pp / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 13% / -1.88pp / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Core energy-drink revenue | Dongpeng Special Drink volume x realized ASP x channel mix | category growth, weather, terminal coverage, regional penetration, terminal price and same-store productivity |
| Second-curve revenue | new-product volume x ASP x repeat-purchase/channel penetration | electrolyte water, juice tea, coffee/tea shelf penetration, repeat purchase, cannibalization versus incrementality |
| Gross profit | revenue x gross margin by product/channel | sugar, PET/can/packaging, logistics, product mix, price discipline and promotion intensity |
| Operating profit | gross profit - selling expense - admin/R&D | advertising, rebate/lottery policy, salesforce expansion, scale leverage |
| Cash profit / FCF | net profit + D&A - working capital - capex | contract liabilities/prepayments, distributor inventory, receivables, inventory and buyback/dividend execution |
| Valuation bridge | normalized EPS/FCF x consumer-growth multiple with ROE/payout cross-check | H1/H2 revenue growth, margin stability, second-curve proof, channel health and downside entry band |

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