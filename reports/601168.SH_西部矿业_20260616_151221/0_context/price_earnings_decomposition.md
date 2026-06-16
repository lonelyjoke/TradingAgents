# Historical price-EPS-PE decomposition for 601168.SH as of 2026-06-16

- Company: 西部矿业
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-15 |
| close | 32.84 |
| PE TTM | 17.7 |
| EPS TTM proxy = close / PE TTM | 1.855 |
| PE percentile in window | 84.2% |
| EPS proxy percentile in window | 99.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-15 | 25.21 | 19.1 | 1.32 | 30.3% | 40.6% | -7.3% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-06-16 | 16.68 | 13.24 | 1.26 | 96.9% | 47.2% | 33.7% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-06-15 | 10.69 | 7.55 | 1.416 | 207.2% | 31.0% | 134.5% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-06-16 | 12.47 | 22.66 | 0.55 | 163.4% | 237.1% | -21.9% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | 2026-01-23 | 2026-03-10 | 24.6 | 17.7 | 1.32 | 1.855 | 40.6% | -28.0% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.