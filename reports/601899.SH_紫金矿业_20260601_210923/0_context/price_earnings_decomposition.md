# Historical price-EPS-PE decomposition for 601899.SH as of 2026-06-01

- Company: 紫金矿业
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-01 |
| close | 30.19 |
| PE TTM | 13.01 |
| EPS TTM proxy = close / PE TTM | 2.32 |
| PE percentile in window | 11.6% |
| EPS proxy percentile in window | 99.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-01 | 30.06 | 17.54 | 1.714 | 0.4% | 35.3% | -25.8% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-06-03 | 18.06 | 13.35 | 1.353 | 67.2% | 71.5% | -2.5% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-06-01 | 11.05 | 15.03 | 0.735 | 173.2% | 215.5% | -13.4% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-01 | 11.44 | 36.52 | 0.313 | 163.9% | 640.6% | -64.4% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 47 | 2025-09-29 | 2026-03-23 | 17.74 | 13.01 | 1.714 | 2.32 | 35.3% | -26.6% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.