# Relative strength and index linkage for 601166.SH as of 2026-06-22

- Company: 兴业银行
- Tushare industry: 银行
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=银行; equal-weight daily-return basket from peers: 601939.SH, 601398.SH, 601288.SH, 601988.SH, 600036.SH, 601328.SH, 601658.SH, 601998.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -0.29% | 3.31% | -3.60% | -0.30 | -0.35 | modest_underperform_low_correlation |
| CSI 300 / 沪深300 | 60d | -7.82% | 8.20% | -16.03% | 0.10 | 0.09 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 120d | -15.18% | 9.87% | -25.05% | 0.15 | 0.16 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 250d | -27.23% | 27.19% | -54.42% | 0.10 | 0.11 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 银行 | 20d | -0.29% | -1.12% | 0.83% | 0.73 | 0.90 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 银行 | 60d | -7.82% | -2.62% | -5.20% | 0.77 | 0.84 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 银行 | 120d | -15.18% | -4.12% | -11.06% | 0.76 | 0.90 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 银行 | 250d | -27.26% | -3.73% | -23.52% | 0.75 | 0.90 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-06-09 to 2026-06-18 |
| style_index_daily | ready | CSI 300 / 沪深300; 251 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.