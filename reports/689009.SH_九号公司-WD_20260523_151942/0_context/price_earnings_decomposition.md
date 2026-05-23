# Historical price-EPS-PE decomposition for 689009.SH as of 2026-05-23

- Company: 九号公司-WD
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-22 |
| close | 39.68 |
| PE TTM | 19.05 |
| EPS TTM proxy = close / PE TTM | 2.083 |
| PE percentile in window | 2.2% |
| EPS proxy percentile in window | 84.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-11-24 | 56.22 | 21.21 | 2.65 | -29.4% | -21.4% | -10.2% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-05-22 | 67.85 | 34.65 | 1.958 | -41.5% | 6.4% | -45.0% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-05-22 | 35.23 | 58.59 | 0.601 | 12.6% | 246.4% | -67.5% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-05-24 | 66.97 | 226.04 | 0.296 | -40.7% | 603.1% | -91.6% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 92 | 2022-03-15 | 2024-09-26 | 41 | 19.05 | 0.999 | 2.083 | 108.4% | -53.5% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.