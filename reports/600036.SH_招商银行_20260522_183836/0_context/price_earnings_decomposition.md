# Historical price-EPS-PE decomposition for 600036.SH as of 2026-05-22

- Company: 招商银行
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-22 |
| close | 37.02 |
| PE TTM | 6.19 |
| EPS TTM proxy = close / PE TTM | 5.977 |
| PE percentile in window | 30.3% |
| EPS proxy percentile in window | 99.6% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-11-24 | 42.63 | 7.22 | 5.907 | -13.2% | 1.2% | -14.2% | valuation-led drawdown or mixed signal |
| 1Y | 2025-05-22 | 44.51 | 7.61 | 5.852 | -16.8% | 2.1% | -18.6% | valuation-led drawdown or mixed signal |
| 3Y | 2023-05-22 | 34.2 | 6.12 | 5.584 | 8.2% | 7.0% | 1.1% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-05-24 | 54.08 | 13.43 | 4.027 | -31.5% | 48.4% | -53.9% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 165 | 2022-04-25 | 2026-03-23 | 6.68 | 6.19 | 5.472 | 5.977 | 9.2% | -7.3% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.