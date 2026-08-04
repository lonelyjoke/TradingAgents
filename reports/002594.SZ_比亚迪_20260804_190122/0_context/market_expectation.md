# Market-expectation context for 002594.SZ as of 2026-08-04

- Company: 比亚迪
- Valuation trade date: 2026-08-04
- Purpose: separate a good company from a good investment by asking what the current price already implies.

## Implied Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| Market cap (CNY) | 831032561240 | current equity value |
| PE TTM | 30.1661 | earnings multiple the market is paying now |
| PS TTM | 1.0602 | sales multiple the market is paying now |
| Implied TTM earnings (CNY) | 27548558190.8168 | market cap divided by PE TTM |
| Implied TTM sales (CNY) | 783845087002.4524 | market cap divided by PS TTM |
| PE percentile | 49.6 | 5-year valuation position |
| PB percentile | 2.1 | 5-year valuation position |
| PS percentile | 16.4 | 5-year valuation position |

## Earnings Benchmarks Versus Implied TTM Earnings
| benchmark | value | implied_pe_at_benchmark_profit | vs_implied_ttm_earnings |
| --- | --- | --- | --- |
| latest annual parent profit | 32619022000 | 25.4769 | 1.1841 |
| latest reported simple-run-rate parent profit (Q1) | 16338204000 | 50.8644 | 0.5931 |
| latest reported seasonality-adjusted parent profit (Q1) | 32548833341.969 | 25.5319 | 1.1815 |

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