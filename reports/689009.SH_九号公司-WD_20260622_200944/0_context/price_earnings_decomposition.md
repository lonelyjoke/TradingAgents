# Historical price-EPS-PE decomposition for 689009.SH as of 2026-06-22

- Company: 九号公司-WD
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-22 |
| close | 34 |
| PE TTM | 16.52 |
| EPS TTM proxy = close / PE TTM | 2.059 |
| PE percentile in window | 0.2% |
| EPS proxy percentile in window | 83.2% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-22 | 58.97 | 22.34 | 2.64 | -42.3% | -22.0% | -26.1% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-06-23 | 59 | 30.13 | 1.958 | -42.4% | 5.1% | -45.2% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-06-26 | 35.43 | 59.09 | 0.6 | -4.0% | 243.3% | -72.0% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-06-22 | 77.86 | 262.79 | 0.296 | -56.3% | 594.8% | -93.7% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 214 | 2022-04-25 | 2024-04-25 | 56.94 | 16.52 | 0.6 | 2.059 | 243.3% | -71.0% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.