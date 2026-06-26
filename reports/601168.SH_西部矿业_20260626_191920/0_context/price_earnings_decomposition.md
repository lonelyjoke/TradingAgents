# Historical price-EPS-PE decomposition for 601168.SH as of 2026-06-26

- Company: 西部矿业
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-26 |
| close | 26.37 |
| PE TTM | 14.21 |
| EPS TTM proxy = close / PE TTM | 1.855 |
| PE percentile in window | 65.9% |
| EPS proxy percentile in window | 99.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-26 | 27.47 | 20.82 | 1.32 | -4.0% | 40.6% | -31.7% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-06-26 | 15.87 | 12.6 | 1.26 | 66.2% | 47.2% | 12.8% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-26 | 10.31 | 7.28 | 1.416 | 155.8% | 31.0% | 95.3% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-06-28 | 12.24 | 22.24 | 0.55 | 115.4% | 237.1% | -36.1% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31 | 2025-12-04 | 2026-04-13 | 19.38 | 14.21 | 1.32 | 1.855 | 40.6% | -26.6% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.