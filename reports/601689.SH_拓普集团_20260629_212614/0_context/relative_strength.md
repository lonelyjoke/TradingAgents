# Relative strength and index linkage for 601689.SH as of 2026-06-29

- Company: 拓普集团
- Tushare industry: 汽车配件
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=汽车配件; equal-weight daily-return basket from peers: 000338.SZ, 600660.SH, 600741.SH, 002920.SZ, 000559.SZ, 301656.SZ, 603049.SH, 002126.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -16.11% | 5.52% | -21.63% | 0.27 | 0.50 | strong_underperform |
| CSI 500 / 中证500 | 60d | -8.80% | 13.77% | -22.56% | 0.37 | 0.69 | strong_underperform |
| CSI 500 / 中证500 | 120d | -24.33% | 19.98% | -44.31% | 0.38 | 0.64 | strong_underperform |
| CSI 500 / 中证500 | 250d | 15.59% | 53.39% | -37.80% | 0.37 | 0.81 | strong_underperform |
| Tushare same-industry equal-weight basket / 汽车配件 | 20d | -16.11% | -9.01% | -7.10% | 0.46 | 0.90 | modest_underperform |
| Tushare same-industry equal-weight basket / 汽车配件 | 60d | -8.80% | -6.73% | -2.07% | 0.63 | 1.22 | in_line |
| Tushare same-industry equal-weight basket / 汽车配件 | 120d | -24.33% | -1.82% | -22.50% | 0.59 | 1.00 | strong_underperform |
| Tushare same-industry equal-weight basket / 汽车配件 | 250d | 15.59% | 32.87% | -17.28% | 0.62 | 1.24 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-16 to 2026-06-29 |
| style_index_daily | ready | CSI 500 / 中证500; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.