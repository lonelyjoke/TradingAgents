# Relative strength and index linkage for 300308.SZ as of 2026-07-18

- Company: 中际旭创
- Tushare industry: 通信设备
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus ChiNext Index / 创业板指 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=通信设备; equal-weight daily-return basket from peers: 601138.SH, 300502.SZ, 601869.SH, 300394.SZ, 000063.SZ, 002281.SZ, 600487.SH, 600522.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -28.40% | -19.37% | -9.02% | 0.87 | 1.27 | modest_underperform_high_correlation |
| ChiNext Index / 创业板指 | 60d | 15.23% | -6.77% | 22.00% | 0.82 | 1.35 | strong_outperform_high_correlation |
| ChiNext Index / 创业板指 | 120d | 56.71% | 1.80% | 54.91% | 0.77 | 1.44 | strong_outperform_high_correlation |
| ChiNext Index / 创业板指 | 250d | 624.72% | 60.95% | 563.77% | 0.72 | 1.63 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 通信设备 | 20d | -28.40% | -20.71% | -7.69% | 0.82 | 0.89 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 通信设备 | 60d | 15.23% | 3.98% | 11.25% | 0.72 | 0.81 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 通信设备 | 120d | 56.71% | 59.15% | -2.44% | 0.65 | 0.80 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 通信设备 | 250d | 624.72% | 237.93% | 386.79% | 0.72 | 1.06 | strong_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-07-03 to 2026-07-17 |
| style_index_daily | ready | ChiNext Index / 创业板指; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.