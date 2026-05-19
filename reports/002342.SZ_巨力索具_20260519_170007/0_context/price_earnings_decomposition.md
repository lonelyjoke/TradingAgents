# Historical price-EPS-PE decomposition for 002342.SZ as of 2026-05-19

- Company: 巨力索具
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-19 |
| close | 15.74 |
| PE TTM | 996.61 |
| EPS TTM proxy = close / PE TTM | 0.016 |
| PE percentile in window | 97.2% |
| EPS proxy percentile in window | 32.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-04-10 | 15.5 | 853.39 | 0.018 | 1.5% | -13.0% | 16.8% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2026-04-10 | 15.5 | 853.39 | 0.018 | 1.5% | -13.0% | 16.8% | price broadly flat; focus on whether EPS and PE offset each other |
| 3Y | 2023-05-19 | 4.21 | 637.85 | 0.007 | 273.9% | 139.3% | 56.2% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-05-19 | 4.01 | 114 | 0.035 | 292.5% | -55.1% | 774.2% | multiple-led rerating: price relies more on valuation expansion |

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