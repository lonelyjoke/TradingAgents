# Historical price-EPS-PE decomposition for 002487.SZ as of 2026-06-12

- Company: 大金重工
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-11 |
| close | 58.48 |
| PE TTM | 33.01 |
| EPS TTM proxy = close / PE TTM | 1.772 |
| PE percentile in window | 40.7% |
| EPS proxy percentile in window | 97.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-11 | 57.61 | 34.05 | 1.692 | 1.5% | 4.7% | -3.0% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-06-11 | 30.13 | 29.48 | 1.022 | 94.1% | 73.3% | 12.0% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-12 | 32.45 | 44.72 | 0.726 | 80.2% | 144.2% | -26.2% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-15 | 7.47 | 8.45 | 0.884 | 682.9% | 100.4% | 290.6% | double engine: EPS growth plus multiple expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | 2022-07-20 | 2026-02-06 | 34.05 | 33.01 | 1.692 | 1.772 | 4.7% | -3.0% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.