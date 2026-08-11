# Market-expectation context for 600096.SH as of 2026-08-11

- Company: 云天化
- Valuation trade date: 2026-08-11
- Purpose: separate a good company from a good investment by asking what the current price already implies.

## Implied Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| Market cap (CNY) | 54379812581 | current equity value |
| PE TTM | 10.2794 | earnings multiple the market is paying now |
| PS TTM | 1.1481 | sales multiple the market is paying now |
| Implied TTM earnings (CNY) | 5290173802.0702 | market cap divided by PE TTM |
| Implied TTM sales (CNY) | 47365048846.7904 | market cap divided by PS TTM |
| PE percentile | 70.4 | 5-year valuation position |
| PB percentile | 45.1 | 5-year valuation position |
| PS percentile | 89.2 | 5-year valuation position |

## Earnings Benchmarks Versus Implied TTM Earnings
| benchmark | value | implied_pe_at_benchmark_profit | vs_implied_ttm_earnings |
| --- | --- | --- | --- |
| latest annual parent profit | 5156043643.98 | 10.5468 | 0.9746 |
| latest reported simple-run-rate parent profit (Q1) | 5699070850.76 | 9.5419 | 1.0773 |
| latest reported seasonality-adjusted parent profit (Q1) | 5209984395.5932 | 10.4376 | 0.9848 |

## External Consensus Integration Contract
| layer | status in this module | permitted interpretation |
| --- | --- | --- |
| Current-price implied expectation | calculated | reverse market cap/valuation into earnings or sales power; this is not analyst consensus |
| Company-specific analyst consensus | not supplied by Tushare daily-basic | use only when a dated company-specific forecast set is supplied; retain broker/count/range or median |
| One broker or industry report | secondary hypothesis | compare assumptions, but never relabel it as consensus |
| TradingAgents forecast | downstream estimate | compare exact volume/price/margin/EPS/FCF variables and periods with the other layers |

## Analyst Instructions
- Do not call a stock cheap or expensive from PE/PB alone. State what earnings power, sales scale, or durability the current quote appears to require.
- Compare the implied TTM earnings with latest annual, simple-run-rate interim earnings, and seasonality-adjusted interim earnings before claiming an expectation gap.
- Treat implied PE at benchmark profit as a forward/normalized earnings proxy, not analyst-consensus forward PE; for resource or cyclical companies, make this proxy and explicit bull/base/bear profit scenarios more important than trailing PE TTM.
- Do not forecast a full year by mechanically multiplying Q1 by four when historical seasonal shares are available; treat simple run-rate as downside/upside stress only.
- If current valuation already assumes recovery, say so; if it still prices in deterioration despite improving drivers, say so.
- Translate every rating into a view on mispricing: which assumption in the market quote is too optimistic or too pessimistic?
- A valid expectation gap must state variable, period, magnitude, evidence grade, and the next disclosure capable of resolving the disagreement.