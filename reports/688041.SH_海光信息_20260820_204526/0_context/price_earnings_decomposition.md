# Historical price-EPS-PE decomposition for 688041.SH as of 2026-08-20

- Company: 海光信息
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-20 |
| close | 246.33 |
| PE TTM | 182.23 |
| EPS TTM proxy = close / PE TTM | 1.352 |
| PE percentile in window | 64.2% |
| EPS proxy percentile in window | 100.0% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-24 | 248.14 | 243.7 | 1.018 | -0.7% | 32.8% | -25.2% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2025-08-20 | 155.79 | 158.89 | 0.981 | 58.1% | 37.9% | 14.7% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-08-21 | 50.34 | 130.08 | 0.387 | 389.3% | 249.3% | 40.1% | double engine: EPS growth plus multiple expansion |
| 5Y | 2022-08-12 | 60.1 | 165.37 | 0.363 | 309.9% | 271.9% | 10.2% | double engine: EPS growth plus multiple expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 52 | 2025-09-16 | 2026-04-21 | 240.3 | 182.23 | 1.018 | 1.352 | 32.8% | -24.2% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.