# Relative strength and index linkage for 601600.SH as of 2026-06-16

- Company: 中国铝业
- Tushare industry: 铝
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铝; equal-weight daily-return basket from peers: 002379.SZ, 000807.SZ, 002532.SZ, 000933.SZ, 600219.SH, 603115.SH, 600595.SH, 603876.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -5.89% | -1.39% | -4.50% | 0.18 | 0.43 | modest_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -20.33% | 5.08% | -25.42% | 0.47 | 0.94 | strong_underperform |
| CSI 500 / 中证500 | 120d | -6.33% | 18.66% | -24.99% | 0.47 | 1.10 | strong_underperform |
| CSI 500 / 中证500 | 250d | 50.75% | 47.45% | 3.30% | 0.49 | 1.11 | modest_outperform |
| Tushare same-industry equal-weight basket / 铝 | 20d | -5.89% | -5.47% | -0.42% | 0.82 | 1.41 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 60d | -20.33% | -0.08% | -20.25% | 0.86 | 1.22 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 120d | -6.33% | 26.19% | -32.51% | 0.87 | 1.33 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 250d | 50.75% | 87.92% | -37.17% | 0.86 | 1.29 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-03 to 2026-06-16 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.