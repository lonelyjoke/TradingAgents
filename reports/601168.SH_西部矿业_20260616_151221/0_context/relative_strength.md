# Relative strength and index linkage for 601168.SH as of 2026-06-16

- Company: 西部矿业
- Tushare industry: 铜
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 500 / 中证500 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铜; equal-weight daily-return basket from peers: 601899.SH, 600362.SH, 000630.SZ, 002203.SZ, 603979.SH, 601212.SH, 000878.SZ, 688102.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | 8.38% | -1.72% | 10.11% | 0.68 | 1.34 | strong_outperform_high_correlation |
| CSI 500 / 中证500 | 60d | 17.24% | 4.87% | 12.37% | 0.77 | 1.44 | strong_outperform_high_correlation |
| CSI 500 / 中证500 | 120d | 31.52% | 18.69% | 12.83% | 0.68 | 1.48 | strong_outperform_high_correlation |
| CSI 500 / 中证500 | 250d | 103.22% | 46.48% | 56.73% | 0.65 | 1.39 | strong_outperform |
| Tushare same-industry equal-weight basket / 铜 | 20d | 8.38% | 10.57% | -2.19% | 0.82 | 0.85 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 60d | 17.24% | 16.36% | 0.88% | 0.85 | 1.00 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 120d | 31.52% | 37.96% | -6.45% | 0.86 | 1.10 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 250d | 103.22% | 131.47% | -28.25% | 0.85 | 1.06 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-03 to 2026-06-15 |
| style_index_daily | ready | CSI 500 / 中证500; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.