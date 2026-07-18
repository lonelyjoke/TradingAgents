# Historical price-EPS-PE decomposition for 300308.SZ as of 2026-07-18

- Company: 中际旭创
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-17 |
| close | 979.46 |
| PE TTM | 73.07 |
| EPS TTM proxy = close / PE TTM | 13.404 |
| PE percentile in window | 87.1% |
| EPS proxy percentile in window | 95.4% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-19 | 605.5 | 78.68 | 7.696 | 61.8% | 74.2% | -7.1% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-07-17 | 176.85 | 34.2 | 5.171 | 453.8% | 159.2% | 113.6% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-07-17 | 157.71 | 100.77 | 1.565 | 521.1% | 756.4% | -27.5% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-07-19 | 33.32 | 28.12 | 1.185 | 2839.6% | 1031.2% | 159.9% | double engine: EPS growth plus multiple expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2026-05-11 | 2026-05-12 | 72.93 | 73.07 | 13.424 | 13.404 | -0.1% | 0.2% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.