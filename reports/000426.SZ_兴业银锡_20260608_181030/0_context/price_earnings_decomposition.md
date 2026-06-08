# Historical price-EPS-PE decomposition for 000426.SZ as of 2026-06-08

- Company: 兴业银锡
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-08 |
| close | 35.06 |
| PE TTM | 23.34 |
| EPS TTM proxy = close / PE TTM | 1.502 |
| PE percentile in window | 26.3% |
| EPS proxy percentile in window | 99.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-08 | 34.99 | 38.97 | 0.898 | 0.2% | 67.3% | -40.1% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-06-09 | 16.09 | 17.06 | 0.943 | 117.9% | 59.3% | 36.8% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-08 | 9.12 | 131.75 | 0.069 | 284.4% | 2070.2% | -82.3% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-08 | 8.68 | 3654.34 | 0.002 | 303.9% | 63148.2% | -99.4% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 29 | 2025-10-09 | 2026-03-23 | 39.52 | 23.34 | 0.898 | 1.502 | 67.3% | -40.9% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.