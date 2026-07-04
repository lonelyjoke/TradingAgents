# Relative strength and index linkage for 300274.SZ as of 2026-07-04

- Company: 阳光电源
- Tushare industry: 电气设备
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=电气设备; equal-weight daily-return basket from peers: 300750.SZ, 600406.SH, 300014.SZ, 002028.SZ, 605117.SH, 600089.SH, 601727.SH, 002202.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -23.24% | -1.69% | -21.55% | 0.63 | 1.09 | strong_underperform |
| ChiNext Index / 创业板指 | 60d | 2.30% | 27.63% | -25.33% | 0.55 | 1.01 | strong_underperform |
| ChiNext Index / 创业板指 | 120d | -29.55% | 23.96% | -53.51% | 0.50 | 0.97 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | 97.28% | 99.24% | -1.96% | 0.58 | 1.22 | in_line |
| Tushare same-industry equal-weight basket / 电气设备 | 20d | -23.24% | -4.42% | -18.82% | 0.68 | 1.36 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 电气设备 | 60d | 2.30% | 7.51% | -5.21% | 0.53 | 1.05 | modest_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 120d | -29.55% | 22.88% | -52.43% | 0.51 | 0.97 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 250d | 97.28% | 106.76% | -9.48% | 0.58 | 1.22 | modest_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-19 to 2026-07-03 |
| style_index_daily | ready | ChiNext Index / 创业板指; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.