# Historical price-EPS-PE decomposition for 002594.SZ as of 2026-08-04

- Company: 比亚迪
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-04 |
| close | 91.15 |
| PE TTM | 30.17 |
| EPS TTM proxy = close / PE TTM | 3.022 |
| PE percentile in window | 49.6% |
| EPS proxy percentile in window | 25.9% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-04 | 89.14 | 21.19 | 4.206 | 2.3% | -28.2% | 42.3% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-08-04 | 104.88 | 21.32 | 4.918 | -13.1% | -38.6% | 41.5% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 3Y | 2023-08-04 | 268.3 | 39.16 | 6.851 | -66.0% | -55.9% | -23.0% | double drag: EPS decline plus multiple contraction |
| 5Y | 2021-08-04 | 308.09 | 202.22 | 1.524 | -70.4% | 98.3% | -85.1% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 55 | 2025-11-19 | 2026-06-05 | 22.38 | 30.17 | 4.206 | 3.022 | -28.2% | 34.8% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.