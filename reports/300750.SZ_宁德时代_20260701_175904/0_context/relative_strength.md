# Relative strength and index linkage for 300750.SZ as of 2026-07-01

- Company: 宁德时代
- Tushare industry: 电气设备
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=电气设备; equal-weight daily-return basket from peers: 300274.SZ, 600406.SH, 300014.SZ, 002028.SZ, 605117.SH, 600089.SH, 601727.SH, 002202.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -11.54% | 5.05% | -16.59% | 0.68 | 0.65 | strong_underperform_high_correlation |
| ChiNext Index / 创业板指 | 60d | -5.39% | 31.20% | -36.59% | 0.56 | 0.65 | strong_underperform |
| ChiNext Index / 创业板指 | 120d | 2.51% | 31.35% | -28.83% | 0.51 | 0.60 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | 58.55% | 110.22% | -51.67% | 0.60 | 0.76 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 20d | -11.54% | -5.34% | -6.20% | 0.79 | 0.79 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 电气设备 | 60d | -5.39% | 5.58% | -10.97% | 0.56 | 0.64 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 120d | 2.51% | 19.87% | -17.36% | 0.43 | 0.47 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 250d | 58.55% | 119.91% | -61.36% | 0.51 | 0.61 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-16 to 2026-07-01 |
| style_index_daily | ready | ChiNext Index / 创业板指; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.