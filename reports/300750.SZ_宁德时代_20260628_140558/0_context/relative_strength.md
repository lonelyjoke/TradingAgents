# Relative strength and index linkage for 300750.SZ as of 2026-06-28

- Company: 宁德时代
- Tushare industry: 电气设备
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=电气设备; equal-weight daily-return basket from peers: 300274.SZ, 600406.SH, 002028.SZ, 300014.SZ, 605117.SH, 600089.SH, 601727.SH, 002202.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -8.34% | 1.68% | -10.02% | 0.64 | 0.61 | strong_underperform |
| ChiNext Index / 创业板指 | 60d | -8.45% | 27.26% | -35.71% | 0.58 | 0.66 | strong_underperform |
| ChiNext Index / 创业板指 | 120d | 0.77% | 30.86% | -30.10% | 0.51 | 0.60 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | 54.46% | 103.87% | -49.40% | 0.60 | 0.77 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 20d | -8.34% | -8.03% | -0.32% | 0.63 | 0.63 | in_line |
| Tushare same-industry equal-weight basket / 电气设备 | 60d | -8.45% | 1.43% | -9.88% | 0.57 | 0.64 | modest_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 120d | 0.77% | 24.07% | -23.30% | 0.42 | 0.45 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 250d | 54.46% | 116.06% | -61.59% | 0.51 | 0.61 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-13 to 2026-06-26 |
| style_index_daily | ready | ChiNext Index / 创业板指; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.