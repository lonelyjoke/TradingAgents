# Historical price-EPS-PE decomposition for 000933.SZ as of 2026-07-21

- Company: 神火股份
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-21 |
| close | 24.46 |
| PE TTM | 9.85 |
| EPS TTM proxy = close / PE TTM | 2.484 |
| PE percentile in window | 69.9% |
| EPS proxy percentile in window | 61.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-21 | 31.15 | 16.45 | 1.893 | -21.5% | 31.2% | -40.2% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-07-21 | 18.08 | 10.36 | 1.745 | 35.3% | 42.4% | -5.0% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-07-21 | 14.16 | 4.45 | 3.185 | 72.7% | -22.0% | 121.5% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-07-21 | 11.26 | 28.01 | 0.402 | 117.2% | 518.0% | -64.8% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 47 | 2024-04-11 | 2025-12-18 | 12.64 | 9.85 | 1.893 | 2.484 | 31.2% | -22.1% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.