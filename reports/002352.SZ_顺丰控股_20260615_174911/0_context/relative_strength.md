# Relative strength and index linkage for 002352.SZ as of 2026-06-15

- Company: 顺丰控股
- Tushare industry: 仓储物流
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=仓储物流; equal-weight daily-return basket from peers: 600233.SH, 001391.SZ, 601598.SH, 601156.SH, 600153.SH, 600704.SH, 002468.SZ, 002120.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -5.99% | -1.72% | -4.27% | -0.31 | -0.21 | modest_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -10.40% | 4.87% | -15.28% | 0.13 | 0.09 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 120d | -9.41% | 18.69% | -28.10% | 0.11 | 0.08 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 250d | -28.91% | 46.48% | -75.39% | 0.16 | 0.15 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 仓储物流 | 20d | -5.99% | -5.97% | -0.02% | 0.26 | 0.27 | in_line |
| Tushare same-industry equal-weight basket / 仓储物流 | 60d | -10.40% | -8.92% | -1.48% | 0.59 | 0.54 | in_line |
| Tushare same-industry equal-weight basket / 仓储物流 | 120d | -9.41% | -3.69% | -5.72% | 0.56 | 0.51 | modest_underperform |
| Tushare same-industry equal-weight basket / 仓储物流 | 250d | -28.91% | 7.19% | -36.10% | 0.55 | 0.60 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-03 to 2026-06-15 |
| style_index_daily | ready | CSI 500 / 中证500; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.