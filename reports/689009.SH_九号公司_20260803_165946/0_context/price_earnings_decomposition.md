# Historical price-EPS-PE decomposition for 689009.SH as of 2026-08-03

- Company: 九号公司
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-31 |
| close | 44.22 |
| PE TTM | 21.62 |
| EPS TTM proxy = close / PE TTM | 2.046 |
| PE percentile in window | 12.7% |
| EPS proxy percentile in window | 80.9% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-02 | 50.06 | 18.99 | 2.636 | -11.7% | -22.4% | 13.8% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 1Y | 2025-07-31 | 60.52 | 31 | 1.952 | -26.9% | 4.8% | -30.3% | valuation-led drawdown or mixed signal |
| 3Y | 2023-07-31 | 34.78 | 58 | 0.6 | 27.1% | 241.2% | -62.7% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-08-03 | 65.42 | 220.99 | 0.296 | -32.4% | 591.1% | -90.2% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 135 | 2022-03-14 | 2026-05-11 | 33.43 | 21.62 | 1.355 | 2.046 | 50.9% | -35.3% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.