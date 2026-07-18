# Market-expectation context for 300308.SZ as of 2026-07-18

- Company: 中际旭创
- Valuation trade date: 2026-07-17
- Purpose: separate a good company from a good investment by asking what the current price already implies.

## Implied Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| Market cap (CNY) | 1092327779262 | current equity value |
| PE TTM | 73.0709 | earnings multiple the market is paying now |
| PS TTM | 21.3921 | sales multiple the market is paying now |
| Implied TTM earnings (CNY) | 14948875397.2101 | market cap divided by PE TTM |
| Implied TTM sales (CNY) | 51062204237.1717 | market cap divided by PS TTM |
| PE percentile | 87.1 | 5-year valuation position |
| PB percentile | 96.1 | 5-year valuation position |
| PS percentile | 94.3 | 5-year valuation position |

## Earnings Benchmarks Versus Implied TTM Earnings
| benchmark | value | implied_pe_at_benchmark_profit | vs_implied_ttm_earnings |
| --- | --- | --- | --- |
| latest annual parent profit | 10797254300.45 | 101.1672 | 0.7223 |
| latest reported simple-run-rate parent profit (Q1) | 22938006107.32 | 47.6209 | 1.5344 |
| latest reported seasonality-adjusted parent profit (Q1) | 35373496974.8158 | 30.8798 | 2.3663 |

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