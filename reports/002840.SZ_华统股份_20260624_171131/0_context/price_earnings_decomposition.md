# Historical price-EPS-PE decomposition for 002840.SZ as of 2026-06-24

- Company: 华统股份
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-04-24 |
| close | 12.12 |
| PE TTM | 107.27 |
| EPS TTM proxy = close / PE TTM | 0.113 |
| PE percentile in window | 74.4% |
| EPS proxy percentile in window | 12.9% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-10-24 | 10.71 | 32.14 | 0.333 | 13.2% | -66.1% | 233.8% | multiple-led rerating: price relies more on valuation expansion |
| 1Y | 2025-04-25 | 10.89 | 94.38 | 0.115 | 11.3% | -2.1% | 13.7% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-04-28 | 16.65 | 143.61 | 0.116 | -27.2% | -2.5% | -25.3% | valuation-led drawdown or mixed signal |
| 5Y | 2021-06-24 | 8.96 | 21 | 0.427 | 35.3% | -73.5% | 410.8% | multiple-led rerating: price relies more on valuation expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 2021-10-08 | 2025-11-17 | 36.28 | 107.27 | 0.333 | 0.113 | -66.1% | 195.7% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.