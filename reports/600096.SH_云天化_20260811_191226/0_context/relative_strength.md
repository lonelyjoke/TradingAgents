# Relative strength and index linkage for 600096.SH as of 2026-08-11

- Company: 云天化
- Tushare industry: 农药化肥
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=农药化肥; equal-weight daily-return basket from peers: 000792.SZ, 000408.SZ, 600426.SH, 000893.SZ, 600141.SH, 600331.SH, 002545.SZ, 600486.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | 7.50% | -3.73% | 11.22% | 0.31 | 0.23 | strong_outperform |
| CSI 500 / 中证500 | 60d | -5.63% | -6.86% | 1.23% | 0.27 | 0.35 | in_line |
| CSI 500 / 中证500 | 120d | -16.51% | -4.14% | -12.38% | 0.34 | 0.54 | strong_underperform |
| CSI 500 / 中证500 | 250d | 18.37% | 26.17% | -7.80% | 0.41 | 0.69 | modest_underperform |
| Tushare same-industry equal-weight basket / 农药化肥 | 20d | 7.50% | 12.42% | -4.93% | 0.90 | 0.84 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农药化肥 | 60d | -5.63% | -12.75% | 7.12% | 0.81 | 1.00 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 农药化肥 | 120d | -16.51% | -18.92% | 2.41% | 0.80 | 1.08 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 农药化肥 | 250d | 18.37% | 24.09% | -5.72% | 0.80 | 1.05 | modest_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-07-28 to 2026-08-11 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.