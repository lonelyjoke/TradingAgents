# Historical price-EPS-PE decomposition for 300285.SZ as of 2026-06-12

- Company: 国瓷材料
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-12 |
| close | 56.33 |
| PE TTM | 91.05 |
| EPS TTM proxy = close / PE TTM | 0.619 |
| PE percentile in window | 99.3% |
| EPS proxy percentile in window | 60.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-12 | 28 | 45.61 | 0.614 | 101.2% | 0.8% | 99.6% | multiple-led rerating: price relies more on valuation expansion |
| 1Y | 2025-06-12 | 16.68 | 27.39 | 0.609 | 237.7% | 1.6% | 232.4% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-06-12 | 26.78 | 65.19 | 0.411 | 110.3% | 50.6% | 39.7% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-06-15 | 50.51 | 78.64 | 0.642 | 11.5% | -3.7% | 15.8% | multiple-led rerating: price relies more on valuation expansion |

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