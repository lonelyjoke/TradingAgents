# Forward Forecast Model Scaffold for 002714.SZ as of 2026-06-24

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 29893668691.43 / N/A / top-line starting point for volume × price × mix /
- / Gross margin / 5.1719% / -12.65pp / main bridge from demand to gross profit /
- / Finance-expense ratio / 1.9415% / +0.24pp / captures leverage drag or relief /
- / OCF / net profit / 0.7573 / N/A / tests earnings quality and cash realization /
- / Receivables / revenue / 0.7116% / +0.15pp / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 33.1991% / +7.41pp / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Life NBV | new business value = new premium x NBV margin by channel | agent productivity, agent count, bancassurance mix, product margin, persistency/surrender |
| Embedded value / CSM | opening EV + expected return + operating variance + NBV contribution +/- market variance | EV growth, CSM/NCSM movement, insurance-service result, assumption changes |
| P&C underwriting profit | earned premium x (1 - COR) | premium growth, loss ratio, expense ratio, catastrophe losses, auto-pricing discipline |
| Investment income | investment assets x net/total/comprehensive yield - liability cost pressure | bond yield, equity-market beta, impairment, duration mismatch, accounting classification |
| OPAT / net profit / EPS | insurance service result + investment spread + bank/subsidiary contribution - tax/minority/non-recurring | core operating profit, Ping An Bank contribution, one-offs, share count |
| Dividend / SOTP value | capital generation and solvency-supported payout + insurance core P/EV + bank/asset-management/tech value | solvency ratio, payout policy, holding-company discount, double-counting checks |

## Hog-Breeding Sensitivity Requirement
| item | Formula / requirement |
| --- | --- |
| Sales kg | commodity-hog output x average sale weight |
| Unit spread | realized commodity-hog ASP - complete hog-breeding cost |
| Breeding profit | sales kg x unit spread |
| Sensitivity | show at least bear/base/bull hog ASP cases and each 1 CNY/kg move where data permits |
| Implied cycle | reverse-engineer the hog ASP implied by current market cap under normalized PE/PB bands |
| Valuation floor | stress-case book value / NAV after losses and impairment, cross-checked with trough PB |
- No Buy/Overweight or Underweight/Sell conclusion is complete without linking rating triggers to hog ASP, complete cost, breeding-sow inventory, OCF, leverage, and current-market-cap implied hog price.
- The scenario table must be monotonic in economic logic: a positive-spread recovery case cannot have a selected fair-value range below a worse loss-making stress case unless the report explicitly explains why PB support disappears.
- Use PE only on normalized cycle earnings. Do not use TTM PE or a one-year trough/peak EPS as the primary hog-breeder valuation anchor.

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