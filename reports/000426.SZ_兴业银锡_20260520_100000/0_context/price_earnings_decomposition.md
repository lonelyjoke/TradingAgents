# Historical price-EPS-PE decomposition for 000426.SZ as of 2026-05-20

- Company: 兴业银锡
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-19 |
| close | 41.72 |
| PE TTM | 27.77 |
| EPS TTM proxy = close / PE TTM | 1.502 |
| PE percentile in window | 27.1% |
| EPS proxy percentile in window | 99.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-11-19 | 31.78 | 35.4 | 0.898 | 31.3% | 67.3% | -21.6% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2025-05-19 | 13.51 | 14.32 | 0.943 | 208.8% | 59.3% | 93.9% | double engine: EPS growth plus multiple expansion |
| 3Y | 2023-05-19 | 8.69 | 125.54 | 0.069 | 380.1% | 2070.2% | -77.9% | earnings-led rerating: price mostly follows EPS improvement |
| 5Y | 2021-05-20 | 7.32 | 3081.77 | 0.002 | 469.9% | 63148.2% | -99.1% | earnings-led rerating: price mostly follows EPS improvement |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 2026-01-06 | 2026-03-19 | 45.58 | 27.77 | 0.898 | 1.502 | 67.3% | -39.1% | At similar historical prices, today's EPS proxy is higher; current price has stronger earnings support than those past episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.