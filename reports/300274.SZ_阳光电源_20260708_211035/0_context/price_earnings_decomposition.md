# Historical price-EPS-PE decomposition for 300274.SZ as of 2026-07-08

- Company: 阳光电源
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-08 |
| close | 124.49 |
| PE TTM | 21.64 |
| EPS TTM proxy = close / PE TTM | 5.753 |
| PE percentile in window | 45.7% |
| EPS proxy percentile in window | 64.6% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-08 | 170.95 | 23.14 | 7.389 | -27.2% | -22.1% | -6.5% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-07-08 | 73.77 | 11.98 | 6.158 | 68.8% | -6.6% | 80.6% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-07-10 | 117.75 | 37.29 | 3.158 | 5.7% | 82.2% | -42.0% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-07-08 | 118.35 | 79.04 | 1.497 | 5.2% | 284.2% | -72.6% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 126 | 2021-07-08 | 2026-04-28 | 83.65 | 21.64 | 1.44 | 5.753 | 299.5% | -74.1% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.