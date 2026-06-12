# Relative strength and index linkage for 300750.SZ as of 2026-06-11

- Company: 宁德时代
- Tushare industry: 电气设备
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=电气设备; equal-weight daily-return basket from peers: 300274.SZ, 600406.SH, 002028.SZ, 605117.SH, 300014.SZ, 600089.SH, 601727.SH, 601012.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -10.49% | -3.54% | -6.95% | 0.42 | 0.37 | modest_underperform |
| ChiNext Index / 创业板指 | 60d | -3.73% | 15.13% | -18.86% | 0.53 | 0.62 | strong_underperform |
| ChiNext Index / 创业板指 | 120d | -1.39% | 18.75% | -20.14% | 0.48 | 0.58 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | 52.88% | 91.21% | -38.33% | 0.60 | 0.77 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 20d | -10.49% | -10.48% | -0.01% | 0.23 | 0.22 | in_line_low_correlation |
| Tushare same-industry equal-weight basket / 电气设备 | 60d | -3.73% | -7.18% | 3.45% | 0.46 | 0.53 | modest_outperform |
| Tushare same-industry equal-weight basket / 电气设备 | 120d | -1.39% | 23.30% | -24.69% | 0.37 | 0.39 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 250d | 52.88% | 107.41% | -54.53% | 0.49 | 0.59 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-05-27 to 2026-06-11 |
| style_index_daily | ready | ChiNext Index / 创业板指; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.