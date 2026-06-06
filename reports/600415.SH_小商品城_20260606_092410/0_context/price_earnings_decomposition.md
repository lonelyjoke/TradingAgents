# Historical price-EPS-PE decomposition for 600415.SH as of 2026-06-06

- Company: 小商品城
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-05 |
| close | 11.81 |
| PE TTM | 14.75 |
| EPS TTM proxy = close / PE TTM | 0.801 |
| PE percentile in window | 4.0% |
| EPS proxy percentile in window | 97.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-05 | 16.36 | 21.35 | 0.766 | -27.8% | 4.5% | -30.9% | valuation-led drawdown or mixed signal |
| 1Y | 2025-06-05 | 18.43 | 31.94 | 0.577 | -35.9% | 38.8% | -53.8% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-06-05 | 9.17 | 30.4 | 0.302 | 28.8% | 165.5% | -51.5% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-07 | 5.67 | 30.04 | 0.189 | 108.3% | 324.2% | -50.9% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | 2024-10-15 | 2025-04-08 | 23.99 | 14.75 | 0.49 | 0.801 | 63.3% | -38.5% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.