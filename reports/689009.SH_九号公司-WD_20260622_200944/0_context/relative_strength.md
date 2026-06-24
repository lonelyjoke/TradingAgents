# Relative strength and index linkage for 689009.SH as of 2026-06-22

- Company: 九号公司-WD
- Tushare industry: 摩托车
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (11 peers) | Tushare stock_basic industry=摩托车; equal-weight daily-return basket from peers: 601777.SH, 603129.SH, 001696.SZ, 301345.SZ, 603766.SH, 603529.SH, 301322.SZ, 000913.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -14.31% | 1.99% | -16.30% | -0.01 | -0.02 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | -32.67% | 19.66% | -52.33% | 0.16 | 0.21 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | -40.75% | 21.64% | -62.38% | 0.16 | 0.21 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | -45.67% | 43.88% | -89.55% | 0.25 | 0.41 | strong_underperform |
| Tushare same-industry equal-weight basket / 摩托车 | 20d | -14.31% | -7.38% | -6.94% | 0.56 | 0.76 | modest_underperform |
| Tushare same-industry equal-weight basket / 摩托车 | 60d | -32.67% | -3.05% | -29.63% | 0.24 | 0.31 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 摩托车 | 120d | -40.75% | -10.48% | -30.26% | 0.27 | 0.39 | strong_underperform |
| Tushare same-industry equal-weight basket / 摩托车 | 250d | -45.67% | -0.13% | -45.54% | 0.32 | 0.49 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-09 to 2026-06-22 |
| style_index_daily | ready | CSI 1000 / 中证1000; 252 observations |
| same_industry_basket | ready | 11 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.