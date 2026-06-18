# Relative strength and index linkage for 002714.SZ as of 2026-06-17

- Company: 牧原股份
- Tushare industry: 农业综合
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=农业综合; equal-weight daily-return basket from peers: 300498.SZ, 002157.SZ, 002299.SZ, 300761.SZ, 600201.SH, 605296.SH, 000061.SZ, 002458.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -12.34% | 1.66% | -14.01% | 0.17 | 0.21 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 60d | -28.98% | 7.60% | -36.57% | 0.38 | 0.72 | strong_underperform |
| CSI 300 / 沪深300 | 120d | -29.62% | 8.33% | -37.96% | 0.30 | 0.58 | strong_underperform |
| CSI 300 / 沪深300 | 250d | -15.75% | 27.29% | -43.05% | 0.30 | 0.60 | strong_underperform |
| Tushare same-industry equal-weight basket / 农业综合 | 20d | -12.34% | -8.10% | -4.24% | 0.57 | 0.62 | modest_underperform |
| Tushare same-industry equal-weight basket / 农业综合 | 60d | -28.98% | -17.89% | -11.08% | 0.68 | 0.87 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 120d | -29.62% | -9.48% | -20.15% | 0.67 | 0.87 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 250d | -15.75% | 2.17% | -17.92% | 0.67 | 0.96 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-03 to 2026-06-17 |
| style_index_daily | ready | CSI 300 / 沪深300; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.