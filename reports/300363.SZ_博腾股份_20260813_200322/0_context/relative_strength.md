# Relative strength and index linkage for 300363.SZ as of 2026-08-13

- Company: 博腾股份
- Tushare industry: 化学制药
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=化学制药; equal-weight daily-return basket from peers: 603259.SH, 600276.SH, 688506.SH, 300759.SZ, 002001.SZ, 002653.SZ, 002422.SZ, 600196.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | 14.16% | -5.33% | 19.48% | 0.60 | 1.12 | strong_outperform |
| ChiNext Index / 创业板指 | 60d | 46.86% | -7.84% | 54.70% | 0.29 | 0.46 | strong_outperform |
| ChiNext Index / 创业板指 | 120d | -9.95% | 8.48% | -18.43% | 0.29 | 0.50 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | -9.50% | 54.71% | -64.21% | 0.37 | 0.61 | strong_underperform |
| Tushare same-industry equal-weight basket / 化学制药 | 20d | 19.19% | -0.30% | 19.49% | 0.81 | 2.13 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 化学制药 | 60d | 41.79% | 22.02% | 19.76% | 0.65 | 1.24 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 化学制药 | 120d | -6.83% | 12.08% | -18.92% | 0.64 | 1.28 | strong_underperform |
| Tushare same-industry equal-weight basket / 化学制药 | 250d | -4.93% | 12.01% | -16.95% | 0.65 | 1.29 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-07-29 to 2026-08-13 |
| style_index_daily | ready | ChiNext Index / 创业板指; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.