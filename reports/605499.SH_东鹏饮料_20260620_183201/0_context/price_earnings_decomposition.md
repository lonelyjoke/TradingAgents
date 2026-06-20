# Historical price-EPS-PE decomposition for 605499.SH as of 2026-06-20

- Company: 东鹏饮料
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-18 |
| close | 120.6 |
| PE TTM | 18.87 |
| EPS TTM proxy = close / PE TTM | 6.392 |
| PE percentile in window | 0.1% |
| EPS proxy percentile in window | 74.6% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-18 | 266.93 | 31.69 | 8.423 | -54.8% | -24.1% | -40.5% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-06-18 | 324.59 | 46.34 | 7.005 | -62.8% | -8.8% | -59.3% | double drag: EPS decline plus multiple contraction |
| 3Y | 2023-06-19 | 175.39 | 44.04 | 3.983 | -31.2% | 60.5% | -57.2% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-06-21 | 257.56 | 102.99 | 2.501 | -53.2% | 155.6% | -81.7% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | 2022-04-08 | 2022-05-10 | 40.22 | 18.87 | 2.982 | 6.392 | 114.3% | -53.1% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.