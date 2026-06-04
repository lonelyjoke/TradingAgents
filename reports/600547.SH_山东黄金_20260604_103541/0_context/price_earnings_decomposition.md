# Historical price-EPS-PE decomposition for 600547.SH as of 2026-06-04

- Company: 山东黄金
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-03 |
| close | 29.39 |
| PE TTM | 26.26 |
| EPS TTM proxy = close / PE TTM | 1.119 |
| PE percentile in window | 0.3% |
| EPS proxy percentile in window | 99.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-03 | 36.31 | 34.57 | 1.05 | -19.1% | 6.5% | -24.0% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-06-03 | 30.58 | 41.73 | 0.733 | -3.9% | 52.7% | -37.1% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-06-05 | 25.06 | 81.84 | 0.306 | 17.3% | 265.5% | -67.9% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-04 | 20.47 | 66.58 | 0.307 | 43.6% | 264.0% | -60.6% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 126 | 2024-03-29 | 2025-08-22 | 49.04 | 26.26 | 0.579 | 1.119 | 93.4% | -46.4% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.