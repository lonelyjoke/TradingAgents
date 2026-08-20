# Relative strength and index linkage for 688041.SH as of 2026-08-20

- Company: 海光信息
- Tushare industry: 半导体
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | STAR 50 / 科创50 (000688.SH) | 科创板股票优先用科创50作为风格基准。 |
| industry_proxy | same-industry basket (11 peers) | Tushare stock_basic industry=半导体; equal-weight daily-return basket from peers: 688981.SH, 688256.SH, 002371.SZ, 688347.SH, 688012.SH, 688802.SH, 603986.SH, 688795.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| STAR 50 / 科创50 | 20d | -21.67% | -10.35% | -11.32% | 0.91 | 0.92 | strong_underperform_high_correlation |
| STAR 50 / 科创50 | 60d | -23.87% | -10.72% | -13.15% | 0.86 | 0.95 | strong_underperform_high_correlation |
| STAR 50 / 科创50 | 120d | 5.38% | 13.18% | -7.80% | 0.82 | 1.05 | modest_underperform_high_correlation |
| STAR 50 / 科创50 | 250d | 90.13% | 57.58% | 32.55% | 0.78 | 1.24 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 20d | -21.05% | -12.01% | -9.03% | 0.92 | 0.76 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 60d | -22.24% | -11.13% | -11.11% | 0.84 | 0.74 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 120d | -2.52% | 36.23% | -38.75% | 0.78 | 0.79 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 250d | 80.97% | 150.54% | -69.58% | 0.72 | 0.88 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-08-05 to 2026-08-20 |
| style_index_daily | ready | STAR 50 / 科创50; 253 observations |
| same_industry_basket | ready | 11 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.