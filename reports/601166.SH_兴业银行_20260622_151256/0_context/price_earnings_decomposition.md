# Historical price-EPS-PE decomposition for 601166.SH as of 2026-06-22

- Company: 兴业银行
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-18 |
| close | 17.32 |
| PE TTM | 4.73 |
| EPS TTM proxy = close / PE TTM | 3.662 |
| PE percentile in window | 44.8% |
| EPS proxy percentile in window | 29.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-18 | 20.94 | 5.73 | 3.652 | -17.3% | 0.3% | -17.5% | valuation-led drawdown or mixed signal |
| 1Y | 2025-06-18 | 23.91 | 6.6 | 3.623 | -27.6% | 1.1% | -28.3% | valuation-led drawdown or mixed signal |
| 3Y | 2023-06-19 | 15.79 | 3.69 | 4.28 | 9.7% | -14.4% | 28.2% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-06-22 | 20.02 | 5.98 | 3.345 | -13.5% | 9.5% | -21.0% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 334 | 2021-07-27 | 2026-03-04 | 4.09 | 4.73 | 4.21 | 3.662 | -13.0% | 15.6% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.