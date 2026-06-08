# Historical price-EPS-PE decomposition for 689009.SH as of 2026-06-08

- Company: 九号公司-WD
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-08 |
| close | 36.95 |
| PE TTM | 17.95 |
| EPS TTM proxy = close / PE TTM | 2.059 |
| PE percentile in window | 0.6% |
| EPS proxy percentile in window | 83.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-08 | 58.35 | 22.02 | 2.65 | -36.7% | -22.3% | -18.5% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-06-09 | 62.78 | 32.06 | 1.958 | -41.1% | 5.1% | -44.0% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-06-08 | 37.56 | 62.64 | 0.6 | -1.6% | 243.3% | -71.3% | price broadly flat; focus on whether EPS and PE offset each other |
| 5Y | 2021-06-08 | 83 | 280.14 | 0.296 | -55.5% | 594.8% | -93.6% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 106 | 2022-04-20 | 2024-07-29 | 58.65 | 17.95 | 0.624 | 2.059 | 230.0% | -69.4% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.