# Historical price-EPS-PE decomposition for 601888.SH as of 2026-06-06

- Company: 中国中免
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-05 |
| close | 57.2 |
| PE TTM | 29.74 |
| EPS TTM proxy = close / PE TTM | 1.923 |
| PE percentile in window | 24.8% |
| EPS proxy percentile in window | 21.2% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-05 | 81.02 | 49.3 | 1.643 | -29.4% | 17.0% | -39.7% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-06-05 | 61.35 | 32.56 | 1.884 | -6.8% | 2.1% | -8.7% | valuation-led drawdown or mixed signal |
| 3Y | 2023-06-05 | 119.55 | 51.88 | 2.304 | -52.2% | -16.5% | -42.7% | double drag: EPS decline plus multiple contraction |
| 5Y | 2021-06-07 | 317 | 67.95 | 4.665 | -82.0% | -58.8% | -56.2% | double drag: EPS decline plus multiple contraction |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | 2024-08-27 | 2025-06-23 | 19.76 | 29.74 | 2.963 | 1.923 | -35.1% | 50.5% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.