# Historical price-EPS-PE decomposition for 603345.SH as of 2026-07-23

- Company: 安井食品
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-23 |
| close | 87.12 |
| PE TTM | 19 |
| EPS TTM proxy = close / PE TTM | 4.584 |
| PE percentile in window | 39.2% |
| EPS proxy percentile in window | 59.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-23 | 89.51 | 21.51 | 4.161 | -2.7% | 10.2% | -11.6% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-07-23 | 74.58 | 17.25 | 4.323 | 16.8% | 6.0% | 10.2% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-07-24 | 148.5 | 34.61 | 4.29 | -41.3% | 6.9% | -45.1% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-07-23 | 172.01 | 60.96 | 2.822 | -49.4% | 62.5% | -68.8% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 153 | 2024-01-22 | 2026-03-30 | 17.55 | 19 | 4.785 | 4.584 | -4.2% | 8.3% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.