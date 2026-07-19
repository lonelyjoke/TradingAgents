# Historical price-EPS-PE decomposition for 603986.SH as of 2026-07-19

- Company: 兆易创新
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-17 |
| close | 463.15 |
| PE TTM | 113.06 |
| EPS TTM proxy = close / PE TTM | 4.096 |
| PE percentile in window | 61.0% |
| EPS proxy percentile in window | 83.5% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-19 | 288.45 | 148.47 | 1.943 | 60.6% | 110.9% | -23.9% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-07-17 | 117.99 | 69.19 | 1.705 | 292.5% | 140.2% | 63.4% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-07-17 | 118.36 | 52.05 | 2.274 | 291.3% | 80.1% | 117.2% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-07-19 | 171.18 | 112.14 | 1.527 | 170.6% | 168.4% | 0.8% | earnings-led rerating: price mostly follows EPS improvement |

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