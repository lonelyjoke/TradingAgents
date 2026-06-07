# Relative strength and index linkage for 300751.SZ as of 2026-06-07

- Company: 迈为股份
- Tushare industry: 专用机械
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus ChiNext Index / 创业板指 and same-industry basket (12 peers). Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=专用机械; equal-weight daily-return basket from peers: 000988.SZ, 301200.SZ, 002008.SZ, 300757.SZ, 002837.SZ, 688777.SH, 300450.SZ, 300316.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -14.84% | 4.26% | -19.10% | 0.08 | 0.18 | strong_underperform_low_correlation |
| ChiNext Index / 创业板指 | 60d | -11.12% | 23.35% | -34.48% | 0.30 | 0.69 | strong_underperform |
| ChiNext Index / 创业板指 | 120d | 94.83% | 30.33% | 64.50% | 0.24 | 0.82 | strong_outperform_low_correlation |
| ChiNext Index / 创业板指 | 250d | 220.86% | 97.38% | 123.48% | 0.34 | 0.92 | strong_outperform |
| Tushare same-industry equal-weight basket / 专用机械 | 20d | -14.84% | 9.03% | -23.87% | 0.27 | 0.43 | strong_underperform |
| Tushare same-industry equal-weight basket / 专用机械 | 60d | -11.12% | 33.66% | -44.79% | 0.31 | 0.55 | strong_underperform |
| Tushare same-industry equal-weight basket / 专用机械 | 120d | 94.83% | 96.96% | -2.13% | 0.31 | 0.71 | in_line |
| Tushare same-industry equal-weight basket / 专用机械 | 250d | 220.86% | 206.94% | 13.91% | 0.34 | 0.72 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-23 to 2026-06-05 |
| style_index_daily | ready | ChiNext Index / 创业板指; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.