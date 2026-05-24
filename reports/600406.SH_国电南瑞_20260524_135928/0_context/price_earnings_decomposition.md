# Historical price-EPS-PE decomposition for 600406.SH as of 2026-05-24

- Company: 国电南瑞
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-22 |
| close | 25.83 |
| PE TTM | 24.93 |
| EPS TTM proxy = close / PE TTM | 1.036 |
| PE percentile in window | 21.2% |
| EPS proxy percentile in window | 95.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-11-24 | 22.15 | 22.26 | 0.995 | 16.6% | 4.1% | 12.0% | multiple-led rerating: price relies more on valuation expansion |
| 1Y | 2025-05-22 | 23.08 | 24.09 | 0.958 | 11.9% | 8.1% | 3.5% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-05-22 | 27.82 | 28.25 | 0.985 | -7.2% | 5.2% | -11.7% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-05-24 | 27.83 | 25.84 | 1.077 | -7.2% | -3.8% | -3.5% | valuation-led drawdown or mixed signal |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 312 | 2021-07-07 | 2026-03-23 | 28.28 | 24.93 | 0.912 | 1.036 | 13.6% | -11.8% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.