# Historical price-EPS-PE decomposition for 300750.SZ as of 2026-06-27

- Company: 宁德时代
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-26 |
| close | 381 |
| PE TTM | 22.32 |
| EPS TTM proxy = close / PE TTM | 17.07 |
| PE percentile in window | 29.0% |
| EPS proxy percentile in window | 96.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-26 | 374.43 | 26.79 | 13.975 | 1.8% | 22.1% | -16.7% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-06-26 | 252.79 | 21.27 | 11.887 | 50.7% | 43.6% | 5.0% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-06-26 | 225.17 | 25.34 | 8.884 | 69.2% | 92.1% | -11.9% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-28 | 493.9 | 169.27 | 2.918 | -22.9% | 485.0% | -86.8% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 156 | 2022-04-25 | 2026-04-09 | 28.66 | 22.32 | 12.795 | 17.07 | 33.4% | -22.1% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.