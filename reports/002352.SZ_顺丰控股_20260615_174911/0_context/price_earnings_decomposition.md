# Historical price-EPS-PE decomposition for 002352.SZ as of 2026-06-15

- Company: 顺丰控股
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-15 |
| close | 33.59 |
| PE TTM | 15.5 |
| EPS TTM proxy = close / PE TTM | 2.167 |
| PE percentile in window | 0.7% |
| EPS proxy percentile in window | 92.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-15 | 37.41 | 17.36 | 2.155 | -10.2% | 0.5% | -10.7% | valuation-led drawdown or mixed signal |
| 1Y | 2025-06-16 | 49.8 | 23.7 | 2.102 | -32.6% | 3.1% | -34.6% | valuation-led drawdown or mixed signal |
| 3Y | 2023-06-15 | 49.65 | 35.37 | 1.404 | -32.3% | 54.4% | -56.2% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-06-15 | 69.51 | 58.33 | 1.192 | -51.7% | 81.8% | -73.4% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52 | 2024-01-30 | 2024-08-28 | 19.84 | 15.5 | 1.75 | 2.167 | 23.8% | -21.9% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.