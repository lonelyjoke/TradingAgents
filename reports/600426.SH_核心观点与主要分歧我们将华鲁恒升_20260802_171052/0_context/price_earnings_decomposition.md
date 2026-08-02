# Historical price-EPS-PE decomposition for 600426.SH as of 2026-08-02

- Company: 华鲁恒升
- Look-back window: 5 years
- Method: join Tushare daily close with daily_basic PE TTM, then infer `EPS TTM proxy = close / PE TTM`.
- Caveat: this is an internally consistent market-implied EPS proxy, not a substitute for reported EPS. Loss-making or non-positive-PE days are excluded.

## Latest Snapshot
| metric | value |
| --- | --- |
| latest trade date | 2026-07-31 |
| close | 21.55 |
| PE TTM | 15.91 |
| EPS TTM proxy = close / PE TTM | 1.355 |
| PE percentile in window | 73.4% |
| EPS proxy percentile in window | 0.7% |

## Price Move Decomposition
| window | anchor_date | anchor_close | anchor_pe_ttm | anchor_eps_proxy | price_change | eps_proxy_change | pe_change | primary_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6M | 2026-02-02 | 34.5 | 22.69 | 1.52 | -37.5% | -10.9% | -29.9% | double drag: EPS decline plus multiple contraction |
| 1Y | 2025-07-31 | 23.98 | 14.37 | 1.669 | -10.1% | -18.8% | 10.7% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 3Y | 2023-07-31 | 33.82 | 15.47 | 2.186 | -36.3% | -38.0% | 2.8% | earnings-led drawdown: price mainly reflects EPS deterioration |
| 5Y | 2021-08-02 | 32.6 | 23.41 | 1.393 | -33.9% | -2.7% | -32.0% | valuation-led drawdown or mixed signal |

## Same-Price History Check
| similar_price_days | first_similar_date | last_similar_date | median_pe_ttm_at_similar_price | latest_pe_ttm | median_eps_proxy_at_similar_price | latest_eps_proxy | latest_eps_vs_same_price_history | latest_pe_vs_same_price_history | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 163 | 2024-08-14 | 2025-07-18 | 12.35 | 15.91 | 1.741 | 1.355 | -22.2% | 28.8% | At similar historical prices, today's EPS proxy is lower; current price relies more on valuation hope than past same-price episodes. |

## Analyst Instructions
- Use this module to explain price, not to replace the earnings model. The investment question is whether today’s price is supported by EPS improvement, PE expansion, or both.
- Bulls should prefer cases where price upside can be paid for by EPS growth or credible EPS trough recovery, not only multiple expansion.
- Bears should challenge cases where the stock has risen mainly through PE expansion while the EPS proxy is flat or declining.
- Portfolio Manager should integrate this into the valuation/cycle setup: state whether the current quote is earnings-supported, multiple-supported, double-engine, or fragile.
- If the same-price history shows lower current EPS support than prior same-price episodes, require stronger forward evidence before calling the stock cheap.