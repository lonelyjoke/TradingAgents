# Relative strength and index linkage for 603345.SH as of 2026-06-07

- Company: 安井食品
- Tushare industry: 食品
- Verdict: relative_neutral
- Buy-side read: Relative performance is broadly in line with benchmarks; price action is not a strong independent thesis signal. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Keep fundamentals, valuation, and catalysts as the primary rating drivers.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=食品; equal-weight daily-return basket from peers: 603288.SH, 300999.SZ, 000895.SZ, 300972.SZ, 300765.SZ, 600737.SH, 600298.SH, 600873.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -15.84% | -4.58% | -11.27% | -0.27 | -0.38 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | -2.74% | 1.67% | -4.41% | -0.02 | -0.02 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | 6.37% | 15.08% | -8.71% | 0.15 | 0.21 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | 2.75% | 38.35% | -35.60% | 0.21 | 0.30 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 食品 | 20d | -15.84% | -9.21% | -6.64% | 0.33 | 0.61 | modest_underperform |
| Tushare same-industry equal-weight basket / 食品 | 60d | -2.74% | -6.31% | 3.57% | 0.49 | 0.88 | modest_outperform |
| Tushare same-industry equal-weight basket / 食品 | 120d | 6.37% | -2.59% | 8.96% | 0.47 | 0.82 | modest_outperform |
| Tushare same-industry equal-weight basket / 食品 | 250d | 2.75% | -0.62% | 3.37% | 0.51 | 0.82 | modest_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-23 to 2026-06-05 |
| style_index_daily | ready | CSI 1000 / 中证1000; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.