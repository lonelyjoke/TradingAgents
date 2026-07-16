# Historical price-EPS-PE decomposition for 688981.SH as of 2026-07-15

- Company: 中芯国际
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-14 |
| close | 160.99 |
| PE TTM | 273.15 |
| EPS TTM proxy = close / PE TTM | 0.589 |
| PE percentile in window | 99.8% |
| EPS proxy percentile in window | 30.6% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-14 | 124.49 | 207.04 | 0.601 | 29.3% | -2.0% | 31.9% | multiple-led rerating: price relies more on valuation expansion |
| 1Y | 2025-07-14 | 87.52 | 153.75 | 0.569 | 83.9% | 3.5% | 77.7% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-07-14 | 49.46 | 36.03 | 1.373 | 225.5% | -57.1% | 658.2% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-07-15 | 55.17 | 88.46 | 0.624 | 191.8% | -5.5% | 208.8% | multiple-led rerating: price relies more on valuation expansion |

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