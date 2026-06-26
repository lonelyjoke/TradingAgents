# Relative strength and index linkage for 601168.SH as of 2026-06-26

- Company: 西部矿业
- Tushare industry: 铜
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铜; equal-weight daily-return basket from peers: 601899.SH, 600362.SH, 000630.SZ, 002203.SZ, 000878.SZ, 603979.SH, 601212.SH, 688102.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -15.45% | 1.64% | -17.09% | 0.57 | 1.36 | strong_underperform |
| CSI 500 / 中证500 | 60d | 4.23% | 12.48% | -8.25% | 0.66 | 1.42 | modest_underperform_high_correlation |
| CSI 500 / 中证500 | 120d | 1.74% | 19.94% | -18.20% | 0.64 | 1.46 | strong_underperform |
| CSI 500 / 中证500 | 250d | 58.09% | 50.90% | 7.19% | 0.63 | 1.39 | modest_outperform |
| Tushare same-industry equal-weight basket / 铜 | 20d | -15.45% | -2.95% | -12.51% | 0.87 | 0.99 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 60d | 4.23% | 7.81% | -3.58% | 0.85 | 1.05 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 120d | 1.74% | 14.83% | -13.09% | 0.86 | 1.11 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铜 | 250d | 58.09% | 97.47% | -39.38% | 0.85 | 1.07 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-11 to 2026-06-26 |
| style_index_daily | ready | CSI 500 / 中证500; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.