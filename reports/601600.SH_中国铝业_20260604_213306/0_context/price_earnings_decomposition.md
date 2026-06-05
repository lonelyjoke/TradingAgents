# Historical price-EPS-PE decomposition for 601600.SH as of 2026-06-04

- Company: 中国铝业
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-04 |
| close | 10.9 |
| PE TTM | 12.75 |
| EPS TTM proxy = close / PE TTM | 0.855 |
| PE percentile in window | 22.0% |
| EPS proxy percentile in window | 99.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-04 | 10.89 | 13.11 | 0.831 | 0.1% | 2.9% | -2.7% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-06-04 | 6.68 | 8.36 | 0.799 | 63.2% | 7.0% | 52.5% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-05 | 5.49 | 21.27 | 0.258 | 98.5% | 231.1% | -40.0% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-04 | 5.16 | 52.38 | 0.099 | 111.2% | 767.6% | -75.7% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38 | 2025-11-06 | 2026-04-03 | 13.09 | 12.75 | 0.831 | 0.855 | 2.9% | -2.6% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.