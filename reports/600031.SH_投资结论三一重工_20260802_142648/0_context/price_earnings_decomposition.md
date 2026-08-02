# Historical price-EPS-PE decomposition for 600031.SH as of 2026-08-02

- Company: 三一重工
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-31 |
| close | 20.55 |
| PE TTM | 22.44 |
| EPS TTM proxy = close / PE TTM | 0.916 |
| PE percentile in window | 29.8% |
| EPS proxy percentile in window | 77.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-02 | 21.38 | 23.85 | 0.896 | -3.9% | 2.1% | -5.9% | valuation-led drawdown or mixed signal |
| 1Y | 2025-07-31 | 19.94 | 24.61 | 0.81 | 3.1% | 13.0% | -8.8% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-07-31 | 17.75 | 35.91 | 0.494 | 15.8% | 85.3% | -37.5% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-08-02 | 27.3 | 12.35 | 2.211 | -24.7% | -58.6% | 81.8% | earnings-led drawdown: price mainly reflects EPS deterioration |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 159 | 2022-01-27 | 2026-05-15 | 23.3 | 22.44 | 0.896 | 0.916 | 2.1% | -3.7% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.