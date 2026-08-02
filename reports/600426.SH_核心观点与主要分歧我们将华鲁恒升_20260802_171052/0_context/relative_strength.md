# Relative strength and index linkage for 600426.SH as of 2026-08-02

- Company: 华鲁恒升
- Tushare industry: 农药化肥
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=农药化肥; equal-weight daily-return basket from peers: 000792.SZ, 000408.SZ, 600096.SH, 000893.SZ, 600141.SH, 600331.SH, 002545.SZ, 600486.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -13.38% | -14.31% | 0.92% | 0.12 | 0.27 | in_line_low_correlation |
| CSI 500 / 中证500 | 60d | -40.34% | -13.83% | -26.51% | 0.10 | 0.18 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 120d | -42.84% | -12.02% | -30.82% | 0.17 | 0.31 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 250d | -7.51% | 21.63% | -29.14% | 0.21 | 0.39 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 农药化肥 | 20d | -13.38% | 3.57% | -16.95% | 0.40 | 0.97 | strong_underperform |
| Tushare same-industry equal-weight basket / 农药化肥 | 60d | -40.34% | -17.17% | -23.16% | 0.53 | 0.91 | strong_underperform |
| Tushare same-industry equal-weight basket / 农药化肥 | 120d | -42.84% | -20.01% | -22.82% | 0.61 | 0.92 | strong_underperform |
| Tushare same-industry equal-weight basket / 农药化肥 | 250d | -7.51% | 32.49% | -40.00% | 0.62 | 0.90 | strong_underperform |

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