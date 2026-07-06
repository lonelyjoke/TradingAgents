# Historical price-EPS-PE decomposition for 300750.SZ as of 2026-07-06

- Company: 宁德时代
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-06 |
| close | 374.51 |
| PE TTM | 21.94 |
| EPS TTM proxy = close / PE TTM | 17.07 |
| PE percentile in window | 27.0% |
| EPS proxy percentile in window | 96.6% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-06 | 373.99 | 26.76 | 13.975 | 0.1% | 22.1% | -18.0% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-07-07 | 260.89 | 21.95 | 11.887 | 43.6% | 43.6% | -0.0% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-07-06 | 224.85 | 25.31 | 8.884 | 66.6% | 92.1% | -13.3% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-07-06 | 515.23 | 176.58 | 2.918 | -27.3% | 485.0% | -87.6% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 129 | 2022-04-25 | 2026-04-09 | 27.83 | 21.94 | 13.975 | 17.07 | 22.2% | -21.2% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.