# Relative strength and index linkage for 603345.SH as of 2026-07-23

- Company: 安井食品
- Tushare industry: 食品
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=食品; equal-weight daily-return basket from peers: 603288.SH, 300999.SZ, 000895.SZ, 300765.SZ, 300972.SZ, 600298.SH, 600737.SH, 600873.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | 3.10% | -18.17% | 21.27% | -0.09 | -0.10 | strong_outperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | -9.93% | -13.96% | 4.02% | -0.10 | -0.13 | modest_outperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | -3.75% | -12.07% | 8.32% | 0.01 | 0.01 | modest_outperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | 13.97% | 12.31% | 1.66% | 0.11 | 0.14 | in_line_low_correlation |
| Tushare same-industry equal-weight basket / 食品 | 20d | 5.15% | 6.42% | -1.27% | 0.74 | 1.09 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 食品 | 60d | -11.82% | -4.07% | -7.76% | 0.63 | 1.15 | modest_underperform |
| Tushare same-industry equal-weight basket / 食品 | 120d | -2.11% | -2.12% | 0.00% | 0.53 | 0.87 | in_line |
| Tushare same-industry equal-weight basket / 食品 | 250d | 14.12% | 7.61% | 6.51% | 0.54 | 0.88 | modest_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-07-08 to 2026-07-23 |
| style_index_daily | ready | CSI 1000 / 中证1000; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.