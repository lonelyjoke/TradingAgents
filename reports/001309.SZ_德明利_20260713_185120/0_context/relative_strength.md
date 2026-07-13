# Relative strength and index linkage for 001309.SZ as of 2026-07-13

- Company: 德明利
- Tushare industry: 半导体
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 500 / 中证500 and same-industry basket (12 peers).
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=半导体; equal-weight daily-return basket from peers: 688981.SH, 688256.SH, 688041.SH, 688347.SH, 002371.SZ, 603986.SH, 688012.SH, 688802.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | 26.51% | 5.83% | 20.68% | 0.45 | 1.32 | strong_outperform |
| CSI 500 / 中证500 | 60d | 66.15% | 6.73% | 59.42% | 0.53 | 1.62 | strong_outperform |
| CSI 500 / 中证500 | 120d | 233.59% | 7.72% | 225.87% | 0.48 | 1.35 | strong_outperform |
| CSI 500 / 中证500 | 250d | 576.00% | 43.76% | 532.24% | 0.43 | 1.52 | strong_outperform |
| Tushare same-industry equal-weight basket / 半导体 | 20d | 26.51% | 26.47% | 0.04% | 0.56 | 0.71 | in_line |
| Tushare same-industry equal-weight basket / 半导体 | 60d | 66.15% | 78.97% | -12.82% | 0.58 | 0.71 | strong_underperform |
| Tushare same-industry equal-weight basket / 半导体 | 120d | 233.59% | 75.38% | 158.21% | 0.60 | 0.83 | strong_outperform |
| Tushare same-industry equal-weight basket / 半导体 | 250d | 574.01% | 250.61% | 323.40% | 0.54 | 0.87 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-06-30 to 2026-07-10 |
| style_index_daily | ready | CSI 500 / 中证500; 251 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.