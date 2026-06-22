# Historical price-EPS-PE decomposition for 601318.SH as of 2026-06-21

- Company: 中国平安
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-18 |
| close | 49.38 |
| PE TTM | 6.73 |
| EPS TTM proxy = close / PE TTM | 7.333 |
| PE percentile in window | 1.5% |
| EPS proxy percentile in window | 85.0% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-18 | 68.5 | 8.84 | 7.747 | -27.9% | -5.3% | -23.8% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-06-18 | 53.81 | 8.38 | 6.42 | -8.2% | 14.2% | -19.7% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-06-19 | 47.5 | 8.52 | 5.572 | 4.0% | 31.6% | -21.0% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-06-21 | 64.16 | 8.13 | 7.892 | -23.0% | -7.1% | -17.2% | double drag: EPS decline plus multiple contraction |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 329 | 2021-08-24 | 2025-05-09 | 8.02 | 6.73 | 6.42 | 7.333 | 14.2% | -16.0% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.