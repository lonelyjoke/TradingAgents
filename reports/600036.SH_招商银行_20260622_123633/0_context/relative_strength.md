# Relative strength and index linkage for 600036.SH as of 2026-06-22

- Company: 招商银行
- Tushare industry: 银行
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (11 peers) | Tushare stock_basic industry=银行; equal-weight daily-return basket from peers: 601398.SH, 601288.SH, 601988.SH, 601328.SH, 601658.SH, 601998.SH, 601166.SH, 600000.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | 0.30% | 3.31% | -3.02% | -0.16 | -0.14 | modest_underperform_low_correlation |
| CSI 300 / 沪深300 | 60d | -6.26% | 8.20% | -14.47% | 0.19 | 0.16 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 120d | -10.65% | 9.87% | -20.52% | 0.19 | 0.19 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 250d | -16.46% | 27.19% | -43.65% | 0.13 | 0.15 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 银行 | 20d | 0.30% | -1.16% | 1.46% | 0.85 | 0.82 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 银行 | 60d | -6.26% | -3.51% | -2.75% | 0.74 | 0.73 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 银行 | 120d | -10.65% | -5.96% | -4.69% | 0.74 | 0.80 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 银行 | 250d | -16.59% | -6.17% | -10.42% | 0.74 | 0.86 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-06-09 to 2026-06-18 |
| style_index_daily | ready | CSI 300 / 沪深300; 251 observations |
| same_industry_basket | ready | 11 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.