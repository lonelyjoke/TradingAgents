# Historical price-EPS-PE decomposition for 001309.SZ as of 2026-07-13

- Company: 德明利
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-10 |
| close | 799.98 |
| PE TTM | 44.22 |
| EPS TTM proxy = close / PE TTM | 18.09 |
| PE percentile in window | 34.1% |
| EPS proxy percentile in window | 97.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-03-02 | 246.55 | 81.25 | 3.034 | 224.5% | 496.2% | -45.6% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-07-10 | 83.1 | 218.91 | 0.38 | 862.7% | 4665.4% | -79.8% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-07-10 | 103.55 | 1871.13 | 0.055 | 672.6% | 32588.1% | -97.6% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2022-07-01 | 38.22 | 30.54 | 1.251 | 1993.1% | 1345.6% | 44.8% | double engine: EPS growth plus multiple expansion |

## Same-Price History Check
| similar_price_days | interpretation |
| --- | --- |
| 0 | No sufficiently old same-price observations in the look-back window. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.