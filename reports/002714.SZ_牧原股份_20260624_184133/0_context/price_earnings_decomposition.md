# Historical price-EPS-PE decomposition for 002714.SZ as of 2026-06-24

- Company: 牧原股份
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-24 |
| close | 32.53 |
| PE TTM | 19.2 |
| EPS TTM proxy = close / PE TTM | 1.694 |
| PE percentile in window | 61.4% |
| EPS proxy percentile in window | 15.3% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-24 | 48.12 | 11.85 | 4.06 | -32.4% | -58.3% | 62.0% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 1Y | 2025-06-24 | 41.82 | 9.23 | 4.531 | -22.2% | -62.6% | 108.0% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 3Y | 2023-06-26 | 42.33 | 13.42 | 3.153 | -23.2% | -46.3% | 43.0% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 5Y | 2021-06-24 | 56.18 | 9.76 | 5.754 | -42.1% | -70.6% | 96.6% | earnings-led drawdown: price mainly reflects EPS deterioration |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 2023-10-19 | 2023-10-25 | 10.11 | 19.2 | 3.142 | 1.694 | -46.1% | 90.0% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.