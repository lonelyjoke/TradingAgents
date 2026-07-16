# Relative strength and index linkage for 688981.SH as of 2026-07-15

- Company: 中芯国际
- Tushare industry: 半导体
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | STAR 50 / 科创50 (000688.SH) | 科创板股票优先用科创50作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=半导体; equal-weight daily-return basket from peers: 688256.SH, 688041.SH, 688347.SH, 002371.SZ, 603986.SH, 688802.SH, 688012.SH, 688820.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| STAR 50 / 科创50 | 20d | 23.35% | 14.95% | 8.39% | 0.88 | 1.12 | modest_outperform_high_correlation |
| STAR 50 / 科创50 | 60d | 54.93% | 42.91% | 12.03% | 0.82 | 1.23 | strong_outperform_high_correlation |
| STAR 50 / 科创50 | 120d | 26.11% | 32.93% | -6.82% | 0.82 | 1.15 | modest_underperform_high_correlation |
| STAR 50 / 科创50 | 250d | 82.59% | 100.29% | -17.70% | 0.84 | 1.24 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 20d | 23.35% | 19.24% | 4.10% | 0.87 | 0.91 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 60d | 54.93% | 73.87% | -18.94% | 0.83 | 0.95 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 120d | 26.11% | 81.81% | -55.70% | 0.83 | 0.90 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 250d | 83.44% | 285.80% | -202.36% | 0.81 | 0.91 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 247 observations; 2025-06-30 to 2026-07-14 |
| style_index_daily | ready | STAR 50 / 科创50; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.