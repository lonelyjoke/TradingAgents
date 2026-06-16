# Historical price-EPS-PE decomposition for 603345.SH as of 2026-06-15

- Company: 安井食品
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-15 |
| close | 88.85 |
| PE TTM | 19.38 |
| EPS TTM proxy = close / PE TTM | 4.584 |
| PE percentile in window | 39.3% |
| EPS proxy percentile in window | 59.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-15 | 78.75 | 18.92 | 4.161 | 12.8% | 10.2% | 2.4% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-06-16 | 78.91 | 16.06 | 4.913 | 12.6% | -6.7% | 20.7% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-06-15 | 161.52 | 37.65 | 4.29 | -45.0% | 6.9% | -48.5% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-06-15 | 238.2 | 84.42 | 2.822 | -62.7% | 62.5% | -77.0% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 132 | 2024-01-08 | 2026-03-31 | 17.94 | 19.38 | 4.785 | 4.584 | -4.2% | 8.0% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.