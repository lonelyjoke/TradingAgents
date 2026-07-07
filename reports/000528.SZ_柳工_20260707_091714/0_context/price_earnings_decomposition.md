# Historical price-EPS-PE decomposition for 000528.SZ as of 2026-07-07

- Company: 柳工
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-06 |
| close | 8.27 |
| PE TTM | 10.81 |
| EPS TTM proxy = close / PE TTM | 0.765 |
| PE percentile in window | 14.8% |
| EPS proxy percentile in window | 80.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-01-06 | 12.33 | 17.15 | 0.719 | -32.9% | 6.4% | -36.9% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-07-07 | 9.89 | 13.44 | 0.736 | -16.4% | 3.9% | -19.5% | valuation-led drawdown or mixed signal |
| 3Y | 2023-07-06 | 7.75 | 22.92 | 0.338 | 6.7% | 126.2% | -52.8% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-07-07 | 7.97 | 7.45 | 1.071 | 3.8% | -28.6% | 45.2% | multiple-led rerating: price relies more on valuation expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 96 | 2021-07-07 | 2024-04-02 | 9.62 | 10.81 | 0.83 | 0.765 | -7.9% | 12.4% | At similar historical prices, today's multiple is higher; check whether the business quality or cycle outlook justifies the premium. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.