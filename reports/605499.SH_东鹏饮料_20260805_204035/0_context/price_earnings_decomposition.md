# Historical price-EPS-PE decomposition for 605499.SH as of 2026-08-05

- Company: 东鹏饮料
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-04 |
| close | 126.45 |
| PE TTM | 18.92 |
| EPS TTM proxy = close / PE TTM | 6.684 |
| PE percentile in window | 0.7% |
| EPS proxy percentile in window | 78.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-04 | 268.65 | 34.4 | 7.809 | -52.9% | -14.4% | -45.0% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-08-04 | 295.17 | 38.65 | 7.636 | -57.2% | -12.5% | -51.1% | double drag: EPS decline plus multiple contraction |
| 3Y | 2023-08-04 | 182.16 | 45.74 | 3.983 | -30.6% | 67.8% | -58.6% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-08-05 | 205.72 | 78.63 | 2.616 | -38.5% | 155.5% | -75.9% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22 | 2022-03-28 | 2022-10-12 | 43.25 | 18.92 | 2.986 | 6.684 | 123.9% | -56.3% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.