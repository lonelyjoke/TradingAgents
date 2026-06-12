# Historical price-EPS-PE decomposition for 002594.SZ as of 2026-06-12

- Company: 比亚迪
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-06-11 |
| close | 89.8 |
| PE TTM | 29.72 |
| EPS TTM proxy = close / PE TTM | 3.022 |
| PE percentile in window | 46.9% |
| EPS proxy percentile in window | 28.4% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2025-12-11 | 96.23 | 22.88 | 4.206 | -6.7% | -28.2% | 29.9% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 1Y | 2025-06-11 | 361.99 | 44.36 | 8.161 | -75.2% | -63.0% | -33.0% | double drag: EPS decline plus multiple contraction |
| 3Y | 2023-06-12 | 260.51 | 38.03 | 6.851 | -65.5% | -55.9% | -21.8% | double drag: EPS decline plus multiple contraction |
| 5Y | 2021-06-15 | 232.32 | 152.49 | 1.524 | -61.3% | 98.3% | -80.5% | derating despite EPS growth: market paid a lower multiple |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31 | 2025-11-20 | 2026-03-06 | 21.94 | 29.72 | 4.206 | 3.022 | -28.2% | 35.5% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.