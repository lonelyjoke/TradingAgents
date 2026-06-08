# Relative strength and index linkage for 000425.SZ as of 2026-06-08

- Company: 徐工机械
- Tushare industry: 工程机械
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=工程机械; equal-weight daily-return basket from peers: 600031.SH, 601100.SH, 000157.SZ, 603298.SH, 000811.SZ, 601399.SH, 603338.SH, 601106.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -4.51% | -5.10% | 0.58% | 0.13 | 0.31 | in_line_low_correlation |
| CSI 500 / 中证500 | 60d | -19.19% | -0.34% | -18.84% | 0.42 | 0.82 | strong_underperform |
| CSI 500 / 中证500 | 120d | -9.33% | 17.93% | -27.27% | 0.42 | 0.77 | strong_underperform |
| CSI 500 / 中证500 | 250d | 14.29% | 45.54% | -31.25% | 0.35 | 0.63 | strong_underperform |
| Tushare same-industry equal-weight basket / 工程机械 | 20d | -4.51% | -3.57% | -0.95% | 0.58 | 1.47 | in_line |
| Tushare same-industry equal-weight basket / 工程机械 | 60d | -19.19% | -1.87% | -17.31% | 0.72 | 1.33 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 工程机械 | 120d | -9.33% | 16.37% | -25.70% | 0.67 | 1.04 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 工程机械 | 250d | 17.82% | 47.75% | -29.92% | 0.61 | 0.93 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-05-26 to 2026-06-05 |
| style_index_daily | ready | CSI 500 / 中证500; 251 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.