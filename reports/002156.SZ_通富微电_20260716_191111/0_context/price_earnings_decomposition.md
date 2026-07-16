# Historical price-EPS-PE decomposition for 002156.SZ as of 2026-07-16

- Company: 通富微电
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-15 |
| close | 78.71 |
| PE TTM | 82.59 |
| EPS TTM proxy = close / PE TTM | 0.953 |
| PE percentile in window | 83.1% |
| EPS proxy percentile in window | 99.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-15 | 42.6 | 65.6 | 0.649 | 84.8% | 46.8% | 25.9% | double engine: EPS growth plus multiple expansion |
| 1Y | 2025-07-15 | 25.61 | 57.11 | 0.448 | 207.3% | 112.6% | 44.6% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-07-17 | 22.39 | 99.11 | 0.226 | 251.5% | 321.9% | -16.7% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-07-16 | 21.97 | 57.68 | 0.381 | 258.3% | 150.2% | 43.2% | double engine: EPS growth plus multiple expansion |

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