# Historical price-EPS-PE decomposition for 002407.SZ as of 2026-08-10

- Company: 多氟多
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-07 |
| close | 36.54 |
| PE TTM | 83.08 |
| EPS TTM proxy = close / PE TTM | 0.44 |
| PE percentile in window | 80.1% |
| EPS proxy percentile in window | 35.0% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-04-16 | 30.1 | 168.4 | 0.179 | 21.4% | 146.1% | -50.7% | earnings-led rerating: price mostly follows EPS improvement |
| 1Y | 2026-04-16 | 30.1 | 168.4 | 0.179 | 21.4% | 146.1% | -50.7% | earnings-led rerating: price mostly follows EPS improvement |
| 3Y | 2023-08-07 | 18.49 | 14.94 | 1.237 | 97.6% | -64.5% | 456.0% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-08-10 | 52.58 | 286.42 | 0.184 | -30.5% | 139.6% | -71.0% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 2022-03-08 | 2026-05-28 | 12.55 | 83.08 | 2.939 | 0.44 | -85.0% | 561.9% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.