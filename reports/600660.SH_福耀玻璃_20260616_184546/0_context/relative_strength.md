# Relative strength and index linkage for 600660.SH as of 2026-06-16

- Company: 福耀玻璃
- Tushare industry: 汽车配件
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=汽车配件; equal-weight daily-return basket from peers: 000338.SZ, 601689.SH, 002920.SZ, 600741.SH, 301656.SZ, 000559.SZ, 002126.SZ, 603049.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -8.04% | -1.39% | -6.65% | 0.01 | 0.01 | modest_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -12.29% | 5.08% | -17.38% | 0.30 | 0.23 | strong_underperform |
| CSI 500 / 中证500 | 120d | -18.24% | 18.66% | -36.90% | 0.27 | 0.23 | strong_underperform |
| CSI 500 / 中证500 | 250d | -12.58% | 47.45% | -60.03% | 0.29 | 0.32 | strong_underperform |
| Tushare same-industry equal-weight basket / 汽车配件 | 20d | -8.04% | -11.39% | 3.34% | 0.31 | 0.22 | modest_outperform |
| Tushare same-industry equal-weight basket / 汽车配件 | 60d | -12.29% | -6.42% | -5.87% | 0.37 | 0.27 | modest_underperform |
| Tushare same-industry equal-weight basket / 汽车配件 | 120d | -18.24% | -0.22% | -18.02% | 0.36 | 0.28 | strong_underperform |
| Tushare same-industry equal-weight basket / 汽车配件 | 250d | -12.58% | 33.04% | -45.62% | 0.37 | 0.34 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-03 to 2026-06-16 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.