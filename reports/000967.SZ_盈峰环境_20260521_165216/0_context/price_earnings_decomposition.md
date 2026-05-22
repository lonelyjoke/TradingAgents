# Historical price-EPS-PE decomposition for 000967.SZ as of 2026-05-21

- Company: 盈峰环境
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-21 |
| close | 12.05 |
| PE TTM | 67.89 |
| EPS TTM proxy = close / PE TTM | 0.177 |
| PE percentile in window | 95.7% |
| EPS proxy percentile in window | 60.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-11-21 | 6.42 | 53.34 | 0.12 | 87.7% | 47.5% | 27.3% | double engine: EPS growth plus multiple expansion |
| 1Y | 2025-05-21 | 6.62 | 40.19 | 0.165 | 82.0% | 7.7% | 68.9% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-05-22 | 5.51 | 40.4 | 0.136 | 118.7% | 30.1% | 68.1% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-05-21 | 7.97 | 18.08 | 0.441 | 51.2% | -59.7% | 275.6% | multiple-led rerating: price relies more on valuation expansion |

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