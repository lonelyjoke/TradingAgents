# Historical price-EPS-PE decomposition for 603986.SH as of 2026-07-20

- Company: 兆易创新
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-20 |
| close | 432.3 |
| PE TTM | 105.53 |
| EPS TTM proxy = close / PE TTM | 4.096 |
| PE percentile in window | 56.1% |
| EPS proxy percentile in window | 83.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-20 | 292 | 150.3 | 1.943 | 48.0% | 110.9% | -29.8% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-07-21 | 117.11 | 68.68 | 1.705 | 269.1% | 140.2% | 53.7% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-07-20 | 112.37 | 49.42 | 2.274 | 284.7% | 80.1% | 113.6% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-07-20 | 172.8 | 113.2 | 1.527 | 150.2% | 168.4% | -6.8% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2026-05-20 | 2026-05-21 | 106.94 | 105.53 | 4.1 | 4.096 | -0.1% | -1.3% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.