# Historical price-EPS-PE decomposition for 601872.SH as of 2026-06-03

- Company: 招商轮船
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-02 |
| close | 15.49 |
| PE TTM | 15.81 |
| EPS TTM proxy = close / PE TTM | 0.98 |
| PE percentile in window | 76.1% |
| EPS proxy percentile in window | 98.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-02 | 8.7 | 13.94 | 0.624 | 78.0% | 57.0% | 13.4% | double engine: EPS growth plus multiple expansion |
| 1Y | 2025-06-03 | 6.03 | 10.59 | 0.569 | 156.9% | 72.0% | 49.3% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-02 | 6.01 | 9.96 | 0.603 | 157.7% | 62.4% | 58.7% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-06-03 | 5.27 | 18.76 | 0.281 | 193.9% | 248.8% | -15.7% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 2026-02-25 | 2026-03-13 | 25.1 | 15.81 | 0.624 | 0.98 | 57.0% | -37.0% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.