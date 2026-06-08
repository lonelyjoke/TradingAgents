# Relative strength and index linkage for 601318.SH as of 2026-06-08

- Company: 中国平安
- Tushare industry: 保险
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (4 peers) | Tushare stock_basic industry=保险; equal-weight daily-return basket from peers: 601628.SH, 601601.SH, 601319.SH, 601336.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -10.96% | -1.13% | -9.83% | 0.24 | 0.26 | modest_underperform_low_correlation |
| CSI 300 / 沪深300 | 60d | -12.90% | 4.37% | -17.26% | 0.63 | 0.86 | strong_underperform |
| CSI 300 / 沪深300 | 120d | -8.35% | 6.31% | -14.66% | 0.53 | 0.98 | strong_underperform |
| CSI 300 / 沪深300 | 250d | 0.15% | 24.79% | -24.64% | 0.50 | 0.81 | strong_underperform |
| Tushare same-industry equal-weight basket / 保险 | 20d | -10.96% | -12.85% | 1.89% | 0.78 | 0.75 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 保险 | 60d | -12.90% | -21.00% | 8.11% | 0.89 | 0.82 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 保险 | 120d | -8.35% | -17.02% | 8.67% | 0.86 | 0.84 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 保险 | 250d | 0.15% | -7.63% | 7.78% | 0.84 | 0.77 | modest_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-05-26 to 2026-06-05 |
| style_index_daily | ready | CSI 300 / 沪深300; 251 observations |
| same_industry_basket | ready | 4 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.