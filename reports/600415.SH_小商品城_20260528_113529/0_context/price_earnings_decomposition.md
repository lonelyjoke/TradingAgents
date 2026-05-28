# Historical price-EPS-PE decomposition for 600415.SH as of 2026-05-28

- Company: 小商品城
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-27 |
| close | 13.17 |
| PE TTM | 16.45 |
| EPS TTM proxy = close / PE TTM | 0.801 |
| PE percentile in window | 11.2% |
| EPS proxy percentile in window | 98.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-11-27 | 15.91 | 20.76 | 0.766 | -17.2% | 4.5% | -20.8% | valuation-led drawdown or mixed signal |
| 1Y | 2025-05-27 | 16.86 | 29.22 | 0.577 | -21.9% | 38.8% | -43.7% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-05-29 | 8.04 | 26.66 | 0.302 | 63.8% | 165.5% | -38.3% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-05-28 | 5.2 | 27.55 | 0.189 | 153.3% | 324.2% | -40.3% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 71 | 2024-11-08 | 2026-03-27 | 26.48 | 16.45 | 0.49 | 0.801 | 63.3% | -37.9% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.