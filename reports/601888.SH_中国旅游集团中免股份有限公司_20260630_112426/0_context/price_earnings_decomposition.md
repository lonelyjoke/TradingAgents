# Historical price-EPS-PE decomposition for 601888.SH as of 2026-06-30

- Company: 中国中免
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-29 |
| close | 53.6 |
| PE TTM | 27.87 |
| EPS TTM proxy = close / PE TTM | 1.923 |
| PE percentile in window | 20.2% |
| EPS proxy percentile in window | 22.1% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-29 | 91.48 | 55.67 | 1.643 | -41.4% | 17.0% | -49.9% | derating despite EPS growth: market paid a lower multiple |
| 1Y | 2025-06-30 | 60.97 | 32.36 | 1.884 | -12.1% | 2.1% | -13.9% | valuation-led drawdown or mixed signal |
| 3Y | 2023-06-29 | 110.89 | 48.12 | 2.304 | -51.7% | -16.5% | -42.1% | double drag: EPS decline plus multiple contraction |
| 5Y | 2021-06-30 | 300.1 | 64.33 | 4.665 | -82.1% | -58.8% | -56.7% | double drag: EPS decline plus multiple contraction |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | 2024-09-09 | 2024-09-23 | 18.51 | 27.87 | 2.963 | 1.923 | -35.1% | 50.6% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.