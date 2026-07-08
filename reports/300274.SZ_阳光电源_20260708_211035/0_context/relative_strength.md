# Relative strength and index linkage for 300274.SZ as of 2026-07-08

- Company: 阳光电源
- Tushare industry: 电气设备
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=电气设备; equal-weight daily-return basket from peers: 300750.SZ, 600406.SH, 002028.SZ, 300014.SZ, 605117.SH, 601727.SH, 600089.SH, 600875.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -18.37% | -2.94% | -15.43% | 0.54 | 0.98 | strong_underperform |
| ChiNext Index / 创业板指 | 60d | 0.56% | 15.71% | -15.15% | 0.54 | 1.02 | strong_underperform |
| ChiNext Index / 创业板指 | 120d | -27.67% | 15.85% | -43.52% | 0.50 | 0.96 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | 94.15% | 81.86% | 12.29% | 0.58 | 1.22 | strong_outperform |
| Tushare same-industry equal-weight basket / 电气设备 | 20d | -18.37% | -8.84% | -9.53% | 0.58 | 1.14 | modest_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 60d | 0.56% | -4.50% | 5.06% | 0.52 | 1.02 | modest_outperform |
| Tushare same-industry equal-weight basket / 电气设备 | 120d | -27.67% | 10.15% | -37.82% | 0.50 | 0.93 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 250d | 94.15% | 85.63% | 8.52% | 0.58 | 1.19 | modest_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-23 to 2026-07-08 |
| style_index_daily | ready | ChiNext Index / 创业板指; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.