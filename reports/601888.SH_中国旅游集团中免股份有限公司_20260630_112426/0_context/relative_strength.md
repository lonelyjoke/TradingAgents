# Relative strength and index linkage for 601888.SH as of 2026-06-30

- Company: 中国中免
- Tushare industry: 旅游服务
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (7 peers) | Tushare stock_basic industry=旅游服务; equal-weight daily-return basket from peers: 600185.SH, 000796.SZ, 002707.SZ, 300859.SZ, 002159.SZ, 000610.SZ, 000524.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -10.04% | 5.52% | -15.56% | 0.19 | 0.22 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -24.36% | 13.77% | -38.12% | 0.14 | 0.18 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 120d | -38.99% | 19.98% | -58.98% | 0.15 | 0.23 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 250d | -11.59% | 53.39% | -64.98% | 0.23 | 0.40 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 旅游服务 | 20d | -10.04% | -16.02% | 5.98% | 0.45 | 0.56 | modest_outperform |
| Tushare same-industry equal-weight basket / 旅游服务 | 60d | -24.36% | -28.40% | 4.04% | 0.50 | 0.61 | modest_outperform |
| Tushare same-industry equal-weight basket / 旅游服务 | 120d | -38.99% | -37.20% | -1.79% | 0.45 | 0.61 | in_line |
| Tushare same-industry equal-weight basket / 旅游服务 | 250d | -11.59% | -26.96% | 15.36% | 0.53 | 0.74 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-16 to 2026-06-29 |
| style_index_daily | ready | CSI 500 / 中证500; 252 observations |
| same_industry_basket | ready | 7 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.