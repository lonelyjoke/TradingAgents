# Historical price-EPS-PE decomposition for 301358.SZ as of 2026-06-12

- Company: 湖南裕能
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-11 |
| close | 68.87 |
| PE TTM | 22.88 |
| EPS TTM proxy = close / PE TTM | 3.011 |
| PE percentile in window | 47.1% |
| EPS proxy percentile in window | 60.4% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-11 | 66.7 | 67.83 | 0.983 | 3.3% | 206.2% | -66.3% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-06-11 | 28.29 | 40.48 | 0.699 | 143.4% | 330.8% | -43.5% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-06-12 | 41.67 | 13.81 | 3.016 | 65.3% | -0.2% | 65.6% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2023-02-09 | 53.6 | 14.57 | 3.678 | 28.5% | -18.1% | 57.0% | multiple-led rerating: price relies more on valuation expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45 | 2025-10-30 | 2026-04-09 | 68.96 | 22.88 | 0.983 | 3.011 | 206.2% | -66.8% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.