# Historical price-EPS-PE decomposition for 300476.SZ as of 2026-07-07

- Company: 胜宏科技
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-07 |
| close | 284.92 |
| PE TTM | 59.84 |
| EPS TTM proxy = close / PE TTM | 4.762 |
| PE percentile in window | 79.9% |
| EPS proxy percentile in window | 97.4% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-07 | 307.99 | 73.75 | 4.176 | -7.5% | 14.0% | -18.9% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-07-07 | 144.23 | 66.7 | 2.162 | 97.5% | 120.2% | -10.3% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-07-07 | 23.52 | 28.44 | 0.827 | 1111.4% | 475.7% | 110.4% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-07-07 | 21.44 | 27.93 | 0.768 | 1228.9% | 520.3% | 114.2% | double engine: EPS growth plus multiple expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 68 | 2025-09-05 | 2026-04-15 | 68.39 | 59.84 | 4.176 | 4.762 | 14.0% | -12.5% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.