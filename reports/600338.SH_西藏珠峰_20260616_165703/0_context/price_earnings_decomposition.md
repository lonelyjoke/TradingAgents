# Historical price-EPS-PE decomposition for 600338.SH as of 2026-06-16

- Company: 西藏珠峰
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-16 |
| close | 18.43 |
| PE TTM | 29.78 |
| EPS TTM proxy = close / PE TTM | 0.619 |
| PE percentile in window | 20.3% |
| EPS proxy percentile in window | 53.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-16 | 13 | 26.59 | 0.489 | 41.8% | 26.6% | 12.0% | double engine: EPS growth plus multiple expansion |
| 1Y | 2025-06-16 | 10.36 | 24.91 | 0.416 | 77.9% | 48.8% | 19.5% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-16 | 18.33 | 50.81 | 0.361 | 0.5% | 71.6% | -41.4% | price broadly flat; focus on whether EPS and PE offset each other |
| 5Y | 2021-06-16 | 13.32 | 97.93 | 0.136 | 38.4% | 355.1% | -69.6% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 95 | 2021-07-12 | 2026-04-15 | 49.32 | 29.78 | 0.361 | 0.619 | 71.6% | -39.6% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.