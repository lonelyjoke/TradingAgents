# Historical price-EPS-PE decomposition for 002460.SZ as of 2026-06-11

- Company: 赣锋锂业
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-11 |
| close | 69.94 |
| PE TTM | 38.53 |
| EPS TTM proxy = close / PE TTM | 1.815 |
| PE percentile in window | 73.2% |
| EPS proxy percentile in window | 25.6% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-03-31 | 78.38 | 101.89 | 0.769 | -10.8% | 136.0% | -62.2% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2026-03-31 | 78.38 | 101.89 | 0.769 | -10.8% | 136.0% | -62.2% | derating despite EPS growth: market paid a lower multiple |
| 3Y | 2023-06-12 | 63.09 | 6.57 | 9.605 | 10.9% | -81.1% | 486.6% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-06-11 | 124.41 | 115.78 | 1.075 | -43.8% | 68.9% | -66.7% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56 | 2022-10-10 | 2023-05-22 | 7.9 | 38.53 | 8.701 | 1.815 | -79.1% | 387.5% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.