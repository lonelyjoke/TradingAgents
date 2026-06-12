# Historical price-EPS-PE decomposition for 300750.SZ as of 2026-06-11

- Company: 宁德时代
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-11 |
| close | 382.2 |
| PE TTM | 22.39 |
| EPS TTM proxy = close / PE TTM | 17.07 |
| PE percentile in window | 29.1% |
| EPS proxy percentile in window | 97.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-11 | 388.99 | 27.83 | 13.975 | -1.7% | 22.1% | -19.6% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-06-11 | 250.5 | 21.07 | 11.887 | 52.6% | 43.6% | 6.3% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-12 | 211.95 | 23.86 | 8.884 | 80.3% | 92.1% | -6.1% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-11 | 451.98 | 154.93 | 2.917 | -15.4% | 485.1% | -85.5% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 161 | 2022-04-25 | 2026-04-09 | 28.81 | 22.39 | 12.795 | 17.07 | 33.4% | -22.3% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.