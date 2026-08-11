# Historical price-EPS-PE decomposition for 600096.SH as of 2026-08-11

- Company: 云天化
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-11 |
| close | 29.83 |
| PE TTM | 10.28 |
| EPS TTM proxy = close / PE TTM | 2.902 |
| PE percentile in window | 70.4% |
| EPS proxy percentile in window | 66.0% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-11 | 36.52 | 11.81 | 3.093 | -18.3% | -6.2% | -13.0% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-08-11 | 24.9 | 8.79 | 2.832 | 19.8% | 2.5% | 16.9% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-08-11 | 17.86 | 5.51 | 3.243 | 67.0% | -10.5% | 86.6% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-08-11 | 16.42 | 36.1 | 0.455 | 81.7% | 537.9% | -71.5% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 84 | 2021-09-08 | 2026-06-12 | 10.6 | 10.28 | 2.903 | 2.902 | -0.0% | -3.0% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.