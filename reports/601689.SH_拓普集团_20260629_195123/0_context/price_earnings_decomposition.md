# Historical price-EPS-PE decomposition for 601689.SH as of 2026-06-29

- Company: 拓普集团
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-29 |
| close | 52.35 |
| PE TTM | 32.9 |
| EPS TTM proxy = close / PE TTM | 1.591 |
| PE percentile in window | 27.0% |
| EPS proxy percentile in window | 51.4% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-29 | 71.95 | 45.75 | 1.573 | -27.2% | 1.2% | -28.1% | valuation-led drawdown or mixed signal |
| 1Y | 2025-06-30 | 47.25 | 28.11 | 1.681 | 10.8% | -5.3% | 17.0% | multiple-led rerating: price relies more on valuation expansion |
| 3Y | 2023-06-29 | 79.97 | 49.95 | 1.601 | -34.5% | -0.6% | -34.1% | valuation-led drawdown or mixed signal |
| 5Y | 2021-06-29 | 35.71 | 51.74 | 0.69 | 46.6% | 130.6% | -36.4% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 172 | 2021-10-26 | 2025-08-20 | 32.84 | 32.9 | 1.601 | 1.591 | -0.6% | 0.2% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.