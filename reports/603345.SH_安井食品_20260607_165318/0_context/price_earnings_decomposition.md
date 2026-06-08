# Historical price-EPS-PE decomposition for 603345.SH as of 2026-06-07

- Company: 安井食品
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-05 |
| close | 86.68 |
| PE TTM | 18.91 |
| EPS TTM proxy = close / PE TTM | 4.584 |
| PE percentile in window | 36.9% |
| EPS proxy percentile in window | 60.9% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-05 | 80.04 | 19.23 | 4.161 | 8.3% | 10.2% | -1.7% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-06-05 | 83.06 | 16.91 | 4.913 | 4.4% | -6.7% | 11.8% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-06-05 | 149.78 | 34.91 | 4.29 | -42.1% | 6.9% | -45.8% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-06-07 | 232.07 | 82.24 | 2.822 | -62.6% | 62.5% | -77.0% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 156 | 2024-01-22 | 2026-03-30 | 17.49 | 18.91 | 4.785 | 4.584 | -4.2% | 8.1% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.