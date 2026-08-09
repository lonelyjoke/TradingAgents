# Relative strength and index linkage for 002470.SZ as of 2026-08-08

- Company: 金正大
- Tushare industry: 农药化肥
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=农药化肥; equal-weight daily-return basket from peers: 000792.SZ, 000408.SZ, 600426.SH, 600096.SH, 000893.SZ, 600141.SH, 600331.SH, 002545.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | 1.04% | -6.33% | 7.36% | 0.61 | 0.53 | modest_outperform |
| CSI 1000 / 中证1000 | 60d | -29.60% | -12.52% | -17.08% | 0.34 | 0.43 | strong_underperform |
| CSI 1000 / 中证1000 | 120d | -2.01% | -4.82% | 2.81% | 0.30 | 0.66 | in_line |
| CSI 1000 / 中证1000 | 250d | 10.17% | 14.11% | -3.94% | 0.32 | 0.64 | modest_underperform |
| Tushare same-industry equal-weight basket / 农药化肥 | 20d | 1.04% | 15.31% | -14.27% | 0.76 | 0.89 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农药化肥 | 60d | -29.60% | -14.14% | -15.47% | 0.46 | 0.54 | strong_underperform |
| Tushare same-industry equal-weight basket / 农药化肥 | 120d | -2.01% | -15.84% | 13.83% | 0.45 | 0.85 | strong_outperform |
| Tushare same-industry equal-weight basket / 农药化肥 | 250d | 10.17% | 28.46% | -18.29% | 0.44 | 0.69 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-07-24 to 2026-08-07 |
| style_index_daily | ready | CSI 1000 / 中证1000; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.