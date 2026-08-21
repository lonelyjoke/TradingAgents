# Relative strength and index linkage for 300136.SZ as of 2026-08-21

- Company: 信维通信
- Tushare industry: 元器件
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus ChiNext Index / 创业板指 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=元器件; equal-weight daily-return basket from peers: 002475.SZ, 002384.SZ, 600183.SH, 300476.SZ, 002916.SZ, 300408.SZ, 002463.SZ, 000725.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -10.32% | -2.24% | -8.08% | 0.86 | 1.39 | modest_underperform_high_correlation |
| ChiNext Index / 创业板指 | 60d | -46.76% | -13.60% | -33.16% | 0.67 | 1.29 | strong_underperform_high_correlation |
| ChiNext Index / 创业板指 | 120d | -20.79% | 4.50% | -25.29% | 0.61 | 1.31 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | 150.29% | 49.77% | 100.52% | 0.51 | 1.20 | strong_outperform |
| Tushare same-industry equal-weight basket / 元器件 | 20d | -10.32% | -1.60% | -8.72% | 0.93 | 1.07 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 60d | -46.76% | -13.64% | -33.12% | 0.74 | 1.05 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 120d | -20.79% | 32.87% | -53.66% | 0.69 | 1.06 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 250d | 150.29% | 114.26% | 36.03% | 0.53 | 0.90 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-08-06 to 2026-08-20 |
| style_index_daily | ready | ChiNext Index / 创业板指; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.