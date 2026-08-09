# Historical price-EPS-PE decomposition for 002470.SZ as of 2026-08-08

- Company: 金正大
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-07 |
| close | 1.95 |
| PE TTM | 172.1 |
| EPS TTM proxy = close / PE TTM | 0.011 |
| PE percentile in window | 67.1% |
| EPS proxy percentile in window | 16.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-04-23 | 2.96 | 281.15 | 0.011 | -34.1% | 7.6% | -38.8% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-08-07 | 1.73 | 136.65 | 0.013 | 12.7% | -10.5% | 25.9% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2025-04-28 | 1.68 | 92.49 | 0.018 | 16.1% | -37.6% | 86.1% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2025-04-28 | 1.68 | 92.49 | 0.018 | 16.1% | -37.6% | 86.1% | multiple-led rerating: price relies more on valuation expansion |

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