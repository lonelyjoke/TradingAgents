# Relative strength and index linkage for 002156.SZ as of 2026-07-16

- Company: 通富微电
- Tushare industry: 半导体
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 500 / 中证500 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=半导体; equal-weight daily-return basket from peers: 688981.SH, 688256.SH, 688041.SH, 688347.SH, 002371.SZ, 603986.SH, 688012.SH, 688802.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | 25.08% | -4.24% | 29.31% | 0.68 | 1.66 | strong_outperform_high_correlation |
| CSI 500 / 中证500 | 60d | 63.91% | -0.40% | 64.31% | 0.67 | 1.88 | strong_outperform_high_correlation |
| CSI 500 / 中证500 | 120d | 95.21% | 0.05% | 95.16% | 0.67 | 1.68 | strong_outperform_high_correlation |
| CSI 500 / 中证500 | 250d | 210.00% | 37.57% | 172.44% | 0.65 | 1.64 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 20d | 25.08% | 13.09% | 11.98% | 0.76 | 0.82 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 60d | 63.91% | 57.39% | 6.52% | 0.81 | 0.96 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 120d | 95.21% | 73.20% | 22.01% | 0.80 | 1.01 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 250d | 210.00% | 258.67% | -48.66% | 0.73 | 0.85 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-07-01 to 2026-07-15 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.