# Relative strength and index linkage for 300476.SZ as of 2026-06-08

- Company: 胜宏科技
- Tushare industry: 元器件
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus ChiNext Index / 创业板指 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=元器件; equal-weight daily-return basket from peers: 002475.SZ, 002384.SZ, 600183.SH, 002463.SZ, 002938.SZ, 002916.SZ, 300408.SZ, 000725.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -16.77% | -2.98% | -13.79% | 0.74 | 1.85 | strong_underperform_high_correlation |
| ChiNext Index / 创业板指 | 60d | 8.93% | 15.29% | -6.37% | 0.71 | 1.49 | modest_underperform_high_correlation |
| ChiNext Index / 创业板指 | 120d | 14.89% | 24.26% | -9.37% | 0.66 | 1.49 | modest_underperform_high_correlation |
| ChiNext Index / 创业板指 | 250d | 293.50% | 91.39% | 202.11% | 0.66 | 1.77 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 20d | -16.77% | 17.24% | -34.01% | 0.89 | 1.46 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 60d | 8.93% | 59.39% | -50.46% | 0.76 | 1.21 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 120d | 14.89% | 96.14% | -81.25% | 0.72 | 1.21 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 250d | 293.50% | 247.10% | 46.40% | 0.71 | 1.38 | strong_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-26 to 2026-06-08 |
| style_index_daily | ready | ChiNext Index / 创业板指; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.