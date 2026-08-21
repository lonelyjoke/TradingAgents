# Historical price-EPS-PE decomposition for 300136.SZ as of 2026-08-21

- Company: 信维通信
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-20 |
| close | 59.62 |
| PE TTM | 78.37 |
| EPS TTM proxy = close / PE TTM | 0.761 |
| PE percentile in window | 87.4% |
| EPS proxy percentile in window | 89.8% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-24 | 73.08 | 115 | 0.635 | -18.4% | 19.7% | -31.9% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-08-20 | 27.17 | 42.35 | 0.642 | 119.4% | 18.6% | 85.0% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-08-21 | 16.66 | 24.5 | 0.68 | 257.9% | 11.9% | 219.9% | double engine: EPS growth plus multiple expansion |
| 5Y | 2021-08-23 | 25.23 | 29.91 | 0.844 | 136.3% | -9.8% | 162.0% | multiple-led rerating: price relies more on valuation expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | 2025-12-31 | 2026-04-07 | 97.2 | 78.37 | 0.635 | 0.761 | 19.7% | -19.4% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.