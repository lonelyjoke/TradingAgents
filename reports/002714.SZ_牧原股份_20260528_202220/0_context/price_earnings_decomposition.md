# Historical price-EPS-PE decomposition for 002714.SZ as of 2026-05-28

- Company: 牧原股份
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-05-28 |
| close | 37.05 |
| PE TTM | 21.87 |
| EPS TTM proxy = close / PE TTM | 1.694 |
| PE percentile in window | 80.7% |
| EPS proxy percentile in window | 11.2% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-11-28 | 50.75 | 12.5 | 4.06 | -27.0% | -58.3% | 74.9% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 1Y | 2025-05-28 | 38.4 | 8.48 | 4.531 | -3.5% | -62.6% | 158.0% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 3Y | 2023-05-29 | 41.74 | 13.24 | 3.153 | -11.2% | -46.3% | 65.2% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 5Y | 2021-05-28 | 90.36 | 11.22 | 8.055 | -59.0% | -79.0% | 95.0% | earnings-led drawdown: price mainly reflects EPS deterioration |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 2023-09-28 | 2025-05-29 | 21.14 | 21.87 | 1.814 | 1.694 | -6.6% | 3.4% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.