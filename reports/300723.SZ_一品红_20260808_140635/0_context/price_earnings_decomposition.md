# Historical price-EPS-PE decomposition for 300723.SZ as of 2026-08-08

- Company: 一品红
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-08-07 |
| close | 37.99 |
| PE TTM | 85.8 |
| EPS TTM proxy = close / PE TTM | 0.443 |
| PE percentile in window | 91.4% |
| EPS proxy percentile in window | 18.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-04-24 | 37.49 | 84.67 | 0.443 | 1.3% | -0.0% | 1.3% | price broadly flat; focus on whether EPS and PE offset each other |
| 1Y | 2026-04-24 | 37.49 | 84.67 | 0.443 | 1.3% | -0.0% | 1.3% | price broadly flat; focus on whether EPS and PE offset each other |
| 3Y | 2023-08-07 | 20.44 | 28.83 | 0.709 | 85.9% | -37.6% | 197.6% | multiple-led rerating: price relies more on valuation expansion |
| 5Y | 2021-08-09 | 36.16 | 39.67 | 0.912 | 5.1% | -51.4% | 116.3% | multiple-led rerating: price relies more on valuation expansion |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38 | 2021-08-09 | 2026-06-05 | 39.72 | 85.8 | 0.912 | 0.443 | -51.4% | 116.0% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.