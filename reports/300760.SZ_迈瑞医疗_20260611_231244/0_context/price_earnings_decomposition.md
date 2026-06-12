# Historical price-EPS-PE decomposition for 300760.SZ as of 2026-06-11

- Company: 迈瑞医疗
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-11 |
| close | 146.88 |
| PE TTM | 22.72 |
| EPS TTM proxy = close / PE TTM | 6.464 |
| PE percentile in window | 3.1% |
| EPS proxy percentile in window | 9.2% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-11 | 195.77 | 27.6 | 7.094 | -25.0% | -8.9% | -17.7% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-06-11 | 237.32 | 25.84 | 9.186 | -38.1% | -29.6% | -12.0% | double drag: EPS decline plus multiple contraction |
| 3Y | 2023-06-12 | 299.35 | 36.03 | 8.308 | -50.9% | -22.2% | -36.9% | double drag: EPS decline plus multiple contraction |
| 5Y | 2021-06-11 | 470 | 80.94 | 5.807 | -68.7% | 11.3% | -71.9% | derating despite EPS growth: market paid a lower multiple |

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