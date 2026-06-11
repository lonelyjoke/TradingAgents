# Relative strength and index linkage for 002460.SZ as of 2026-06-11

- Company: 赣锋锂业
- Tushare industry: 小金属
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=小金属; equal-weight daily-return basket from peers: 603993.SH, 000657.SZ, 600111.SH, 001280.SZ, 600549.SH, 002466.SZ, 603799.SH, 601958.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -12.55% | -7.32% | -5.24% | 0.60 | 1.09 | modest_underperform |
| CSI 500 / 中证500 | 60d | -0.13% | -2.48% | 2.35% | 0.42 | 0.82 | in_line |
| CSI 500 / 中证500 | 120d | 11.90% | 12.84% | -0.94% | 0.48 | 0.96 | in_line |
| CSI 500 / 中证500 | 250d | 131.74% | 41.70% | 90.05% | 0.49 | 1.20 | strong_outperform |
| Tushare same-industry equal-weight basket / 小金属 | 20d | -12.55% | 0.39% | -12.94% | 0.69 | 0.67 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 小金属 | 60d | -0.13% | 12.44% | -12.57% | 0.58 | 0.69 | strong_underperform |
| Tushare same-industry equal-weight basket / 小金属 | 120d | 11.90% | 58.75% | -46.85% | 0.59 | 0.64 | strong_underperform |
| Tushare same-industry equal-weight basket / 小金属 | 250d | 131.74% | 193.00% | -61.25% | 0.61 | 0.78 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-05-27 to 2026-06-11 |
| style_index_daily | ready | CSI 500 / 中证500; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.