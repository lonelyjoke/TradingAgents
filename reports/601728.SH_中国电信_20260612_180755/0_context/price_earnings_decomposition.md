# Historical price-EPS-PE decomposition for 601728.SH as of 2026-06-12

- Company: 中国电信
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-12 |
| close | 6.05 |
| PE TTM | 17.48 |
| EPS TTM proxy = close / PE TTM | 0.346 |
| PE percentile in window | 48.8% |
| EPS proxy percentile in window | 64.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-12 | 6.7 | 17.78 | 0.377 | -9.7% | -8.2% | -1.7% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 1Y | 2025-06-12 | 7.62 | 20.95 | 0.364 | -20.6% | -4.8% | -16.6% | valuation-led drawdown or mixed signal |
| 3Y | 2023-06-12 | 6.28 | 20.27 | 0.31 | -3.7% | 11.7% | -13.8% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-08-20 | 6.11 | 22.64 | 0.27 | -1.0% | 28.2% | -22.8% | price broadly flat; focus on whether EPS and PE offset each other |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 291 | 2021-08-20 | 2026-04-13 | 17.82 | 17.48 | 0.339 | 0.346 | 2.0% | -1.9% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.