# Historical price-EPS-PE decomposition for 688981.SH as of 2026-07-15

- Company: 中芯国际
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-15 |
| close | 153.64 |
| PE TTM | 260.68 |
| EPS TTM proxy = close / PE TTM | 0.589 |
| PE percentile in window | 99.4% |
| EPS proxy percentile in window | 30.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-15 | 124.44 | 206.96 | 0.601 | 23.5% | -2.0% | 26.0% | multiple-led rerating: price relies more on valuation expansion |
| 1Y | 2025-07-15 | 87.89 | 154.4 | 0.569 | 74.8% | 3.5% | 68.8% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-07-17 | 48.77 | 35.53 | 1.373 | 215.0% | -57.1% | 633.8% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-07-15 | 55.17 | 88.46 | 0.624 | 178.5% | -5.5% | 194.7% | multiple-led rerating: price relies more on valuation expansion |

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