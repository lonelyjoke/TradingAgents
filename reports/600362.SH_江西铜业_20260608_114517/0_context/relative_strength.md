# Relative strength and index linkage for 600362.SH as of 2026-06-08

- Company: 江西铜业
- Tushare industry: 铜
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 500 / 中证500 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铜; equal-weight daily-return basket from peers: 000630.SZ, 000737.SZ, 000878.SZ, 600490.SH, 601168.SH, 002171.SZ, 002203.SZ, 601899.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| CSI 500 / 中证500 | 60d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| CSI 500 / 中证500 | 120d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| CSI 500 / 中证500 | 250d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| Tushare same-industry equal-weight basket / 铜 | 20d | -9.02% | -9.25% | 0.23% | 0.80 | 1.17 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 60d | -14.31% | -8.82% | -5.49% | 0.85 | 0.98 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 120d | 9.61% | 11.89% | -2.28% | 0.83 | 1.05 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 250d | 108.46% | 75.13% | 33.33% | 0.82 | 1.12 | strong_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-05-26 to 2026-06-05 |
| style_index_daily | failed | CSI 500 / 中证500; 0 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.