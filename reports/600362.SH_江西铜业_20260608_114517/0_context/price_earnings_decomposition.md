# Historical price-EPS-PE decomposition for 600362.SH as of 2026-06-08

- Company: 江西铜业
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-05 |
| close | 44.36 |
| PE TTM | 19.21 |
| EPS TTM proxy = close / PE TTM | 2.309 |
| PE percentile in window | 85.7% |
| EPS proxy percentile in window | 90.0% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-05 | 43.32 | 18.75 | 2.311 | 2.4% | -0.1% | 2.5% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-06-05 | 21.86 | 10.51 | 2.079 | 102.9% | 11.0% | 82.7% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-05 | 18.97 | 10.47 | 1.812 | 133.8% | 27.4% | 83.5% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-06-08 | 24.1 | 27.64 | 0.872 | 84.1% | 164.8% | -30.5% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | 2025-10-29 | 2026-04-03 | 19.25 | 19.21 | 2.311 | 2.309 | -0.1% | -0.2% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.