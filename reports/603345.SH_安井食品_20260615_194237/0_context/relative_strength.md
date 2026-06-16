# Relative strength and index linkage for 603345.SH as of 2026-06-15

- Company: 安井食品
- Tushare industry: 食品
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=食品; equal-weight daily-return basket from peers: 603288.SH, 300999.SZ, 000895.SZ, 300972.SZ, 300765.SZ, 600298.SH, 600737.SH, 600873.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -10.48% | -2.28% | -8.20% | -0.29 | -0.34 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | 1.36% | 6.25% | -4.89% | -0.07 | -0.10 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | 13.76% | 16.54% | -2.77% | 0.11 | 0.15 | in_line_low_correlation |
| CSI 1000 / 中证1000 | 250d | 4.39% | 39.16% | -34.77% | 0.19 | 0.26 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 食品 | 20d | -10.48% | -6.23% | -4.25% | 0.29 | 0.53 | modest_underperform |
| Tushare same-industry equal-weight basket / 食品 | 60d | 1.36% | -6.10% | 7.46% | 0.45 | 0.80 | modest_outperform |
| Tushare same-industry equal-weight basket / 食品 | 120d | 13.76% | -1.02% | 14.79% | 0.46 | 0.80 | strong_outperform |
| Tushare same-industry equal-weight basket / 食品 | 250d | 4.39% | -3.64% | 8.03% | 0.50 | 0.81 | modest_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-03 to 2026-06-15 |
| style_index_daily | ready | CSI 1000 / 中证1000; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.