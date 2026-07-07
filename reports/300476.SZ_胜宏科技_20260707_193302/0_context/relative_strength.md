# Relative strength and index linkage for 300476.SZ as of 2026-07-07

- Company: 胜宏科技
- Tushare industry: 元器件
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=元器件; equal-weight daily-return basket from peers: 002475.SZ, 002384.SZ, 600183.SH, 000725.SZ, 002916.SZ, 300433.SZ, 300408.SZ, 002463.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -9.49% | 2.63% | -12.12% | 0.89 | 1.54 | strong_underperform_high_correlation |
| ChiNext Index / 创业板指 | 60d | -0.34% | 16.86% | -17.19% | 0.77 | 1.62 | strong_underperform_high_correlation |
| ChiNext Index / 创业板指 | 120d | -8.09% | 18.74% | -26.83% | 0.72 | 1.47 | strong_underperform_high_correlation |
| ChiNext Index / 创业板指 | 250d | 132.02% | 83.80% | 48.22% | 0.70 | 1.74 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 20d | -9.49% | 13.30% | -22.80% | 0.87 | 0.96 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 60d | -0.34% | 90.93% | -91.27% | 0.80 | 1.13 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 120d | -8.09% | 98.15% | -106.24% | 0.77 | 1.06 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 250d | 132.02% | 318.73% | -186.71% | 0.74 | 1.23 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-23 to 2026-07-07 |
| style_index_daily | ready | ChiNext Index / 创业板指; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.