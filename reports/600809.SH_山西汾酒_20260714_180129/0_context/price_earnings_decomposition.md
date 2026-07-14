# Historical price-EPS-PE decomposition for 600809.SH as of 2026-07-14

- Company: 山西汾酒
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-13 |
| close | 109.56 |
| PE TTM | 12.17 |
| EPS TTM proxy = close / PE TTM | 9.001 |
| PE percentile in window | 0.9% |
| EPS proxy percentile in window | 59.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-13 | 176.98 | 17.56 | 10.08 | -38.1% | -10.7% | -30.7% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-07-14 | 177.97 | 17.19 | 10.351 | -38.4% | -13.0% | -29.2% | double drag: EPS decline plus multiple contraction |
| 3Y | 2023-07-13 | 212.96 | 28.22 | 7.545 | -48.6% | 19.3% | -56.9% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-07-14 | 355.53 | 107.47 | 3.308 | -69.2% | 172.1% | -88.7% | derating despite EPS growth: market paid a lower multiple |

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