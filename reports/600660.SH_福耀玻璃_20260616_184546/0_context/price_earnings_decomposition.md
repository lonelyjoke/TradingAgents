# Historical price-EPS-PE decomposition for 600660.SH as of 2026-06-16

- Company: 福耀玻璃
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-16 |
| close | 50.65 |
| PE TTM | 14.7 |
| EPS TTM proxy = close / PE TTM | 3.446 |
| PE percentile in window | 0.1% |
| EPS proxy percentile in window | 87.9% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-16 | 61.36 | 17.63 | 3.48 | -17.5% | -1.0% | -16.6% | valuation-led drawdown or mixed signal |
| 1Y | 2025-06-16 | 57.95 | 18.58 | 3.119 | -12.6% | 10.5% | -20.9% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-06-16 | 34.28 | 18.64 | 1.839 | 47.8% | 87.4% | -21.2% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-16 | 54.24 | 47.25 | 1.148 | -6.6% | 200.2% | -68.9% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 95 | 2021-07-05 | 2024-09-26 | 36.63 | 14.7 | 1.331 | 3.446 | 158.9% | -59.9% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.