# Historical price-EPS-PE decomposition for 300274.SZ as of 2026-07-04

- Company: 阳光电源
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-03 |
| close | 126.16 |
| PE TTM | 21.93 |
| EPS TTM proxy = close / PE TTM | 5.753 |
| PE percentile in window | 46.0% |
| EPS proxy percentile in window | 64.9% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-05 | 171.83 | 23.26 | 7.389 | -26.6% | -22.1% | -5.7% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-07-03 | 69.77 | 11.33 | 6.158 | 80.8% | -6.6% | 93.6% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-07-03 | 122.79 | 38.88 | 3.158 | 2.7% | 82.2% | -43.6% | price broadly flat; focus on whether EPS and PE offset each other |
| 5Y | 2021-07-05 | 107.72 | 71.94 | 1.497 | 17.1% | 284.2% | -69.5% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121 | 2021-07-14 | 2026-04-28 | 84.44 | 21.93 | 1.44 | 5.753 | 299.5% | -74.0% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.