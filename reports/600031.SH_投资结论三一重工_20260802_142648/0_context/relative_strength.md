# Relative strength and index linkage for 600031.SH as of 2026-08-02

- Company: 三一重工
- Tushare industry: 工程机械
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=工程机械; equal-weight daily-return basket from peers: 601100.SH, 000425.SZ, 000157.SZ, 603298.SH, 000811.SZ, 603338.SH, 601399.SH, 688425.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | 10.72% | -14.31% | 25.03% | -0.04 | -0.03 | strong_outperform_low_correlation |
| CSI 500 / 中证500 | 60d | -2.05% | -13.83% | 11.78% | 0.06 | 0.07 | strong_outperform_low_correlation |
| CSI 500 / 中证500 | 120d | -7.10% | -12.02% | 4.92% | 0.33 | 0.43 | modest_outperform |
| CSI 500 / 中证500 | 250d | 5.28% | 21.63% | -16.35% | 0.35 | 0.47 | strong_underperform |
| Tushare same-industry equal-weight basket / 工程机械 | 20d | 10.72% | 0.16% | 10.56% | 0.56 | 0.64 | strong_outperform |
| Tushare same-industry equal-weight basket / 工程机械 | 60d | -2.05% | -5.31% | 3.26% | 0.71 | 1.10 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 工程机械 | 120d | -7.10% | -8.05% | 0.96% | 0.80 | 1.07 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 工程机械 | 250d | 5.28% | 21.56% | -16.28% | 0.75 | 0.96 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-07-18 to 2026-07-31 |
| style_index_daily | ready | CSI 500 / 中证500; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.