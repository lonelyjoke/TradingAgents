# Historical price-EPS-PE decomposition for 603629.SH as of 2026-06-08

- Company: 利通电子
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-08 |
| close | 162.34 |
| PE TTM | 79.69 |
| EPS TTM proxy = close / PE TTM | 2.037 |
| PE percentile in window | 55.3% |
| EPS proxy percentile in window | 98.5% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-08 | 26.27 | 36.65 | 0.717 | 518.0% | 184.2% | 117.4% | double engine: EPS growth plus multiple expansion |
| 1Y | 2025-06-09 | 23.23 | 287.91 | 0.081 | 598.8% | 2424.9% | -72.3% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-06-08 | 24.6 | 98.55 | 0.25 | 559.9% | 716.1% | -19.1% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-08 | 20.38 | 41.95 | 0.486 | 696.6% | 319.4% | 89.9% | double engine: EPS growth plus multiple expansion |

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