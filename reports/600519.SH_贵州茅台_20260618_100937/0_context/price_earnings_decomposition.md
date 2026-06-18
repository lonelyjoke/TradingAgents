# Historical price-EPS-PE decomposition for 600519.SH as of 2026-06-18

- Company: 贵州茅台
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-17 |
| close | 1240 |
| PE TTM | 18.74 |
| EPS TTM proxy = close / PE TTM | 66.168 |
| PE percentile in window | 0.5% |
| EPS proxy percentile in window | 79.2% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-17 | 1433.1 | 19.93 | 71.891 | -13.5% | -8.0% | -6.0% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-06-17 | 1427 | 20.14 | 70.857 | -13.1% | -6.6% | -6.9% | double drag: EPS decline plus multiple contraction |
| 3Y | 2023-06-19 | 1744 | 33.06 | 52.751 | -28.9% | 25.4% | -43.3% | derating despite EPS growth: market paid a lower multiple |
| 5Y | 2021-06-18 | 2090.94 | 55.23 | 37.859 | -40.7% | 74.8% | -66.1% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 2024-09-18 | 2024-09-23 | 19.72 | 18.74 | 64.042 | 66.168 | 3.3% | -5.0% | At similar historical prices, EPS and PE are broadly close to history; focus on forward inflection evidence. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.