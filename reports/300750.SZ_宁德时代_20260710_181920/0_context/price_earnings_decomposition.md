# Historical price-EPS-PE decomposition for 300750.SZ as of 2026-07-10

- Company: 宁德时代
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-10 |
| close | 348.76 |
| PE TTM | 20.43 |
| EPS TTM proxy = close / PE TTM | 17.07 |
| PE percentile in window | 21.7% |
| EPS proxy percentile in window | 95.4% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-12 | 361.68 | 25.88 | 13.975 | -3.6% | 22.1% | -21.1% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-07-10 | 272 | 22.88 | 11.887 | 28.2% | 43.6% | -10.7% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-07-10 | 228.8 | 25.75 | 8.884 | 52.4% | 92.1% | -20.7% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-07-12 | 565.79 | 193.91 | 2.918 | -38.4% | 485.0% | -89.5% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | 2022-10-28 | 2026-03-09 | 25.14 | 20.43 | 13.975 | 17.07 | 22.1% | -18.7% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.