# Relative strength and index linkage for 000933.SZ as of 2026-07-21

- Company: 神火股份
- Tushare industry: 铝
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铝; equal-weight daily-return basket from peers: 002379.SZ, 601600.SH, 000807.SZ, 002532.SZ, 600219.SH, 600595.SH, 601677.SH, 603876.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | 6.39% | -10.22% | 16.61% | -0.01 | -0.02 | strong_outperform_low_correlation |
| CSI 500 / 中证500 | 60d | -26.26% | -6.87% | -19.39% | 0.08 | 0.14 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 120d | -22.96% | -5.88% | -17.08% | 0.25 | 0.47 | strong_underperform |
| CSI 500 / 中证500 | 250d | 43.46% | 31.03% | 12.43% | 0.34 | 0.67 | strong_outperform |
| Tushare same-industry equal-weight basket / 铝 | 20d | 6.39% | -8.35% | 14.74% | 0.70 | 1.16 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 60d | -26.26% | -18.64% | -7.62% | 0.74 | 1.06 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 120d | -22.96% | -9.47% | -13.49% | 0.80 | 1.06 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 250d | 43.46% | 55.83% | -12.37% | 0.82 | 1.12 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-07-07 to 2026-07-21 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.