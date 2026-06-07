# Relative strength and index linkage for 002475.SZ as of 2026-06-07

- Company: 立讯精密
- Tushare industry: 元器件
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=元器件; equal-weight daily-return basket from peers: 002384.SZ, 600183.SH, 300476.SZ, 300408.SZ, 002463.SZ, 002916.SZ, 002938.SZ, 300433.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -3.53% | -1.13% | -2.41% | 0.87 | 3.10 | in_line_high_correlation |
| CSI 300 / 沪深300 | 60d | 47.89% | 4.37% | 43.53% | 0.66 | 2.23 | strong_outperform_high_correlation |
| CSI 300 / 沪深300 | 120d | 16.92% | 6.31% | 10.61% | 0.59 | 1.85 | strong_outperform |
| CSI 300 / 沪深300 | 250d | 120.13% | 24.79% | 95.35% | 0.58 | 1.90 | strong_outperform |
| Tushare same-industry equal-weight basket / 元器件 | 20d | -3.53% | 25.07% | -28.60% | 0.73 | 0.90 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 60d | 47.89% | 68.65% | -20.75% | 0.64 | 0.89 | strong_underperform |
| Tushare same-industry equal-weight basket / 元器件 | 120d | 16.92% | 102.82% | -85.91% | 0.60 | 0.75 | strong_underperform |
| Tushare same-industry equal-weight basket / 元器件 | 250d | 120.13% | 271.46% | -151.32% | 0.61 | 0.72 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-23 to 2026-06-05 |
| style_index_daily | ready | CSI 300 / 沪深300; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.