# Relative strength and index linkage for 000933.SZ as of 2026-07-09

- Company: 神火股份
- Tushare industry: 铝
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铝; equal-weight daily-return basket from peers: 002379.SZ, 601600.SH, 000807.SZ, 002532.SZ, 600219.SH, 603115.SH, 600595.SH, 603876.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -18.67% | 1.24% | -19.90% | -0.03 | -0.06 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | -36.63% | 3.77% | -40.40% | 0.11 | 0.22 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | -29.00% | 4.98% | -33.98% | 0.24 | 0.48 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | 26.33% | 32.23% | -5.90% | 0.32 | 0.67 | modest_underperform |
| Tushare same-industry equal-weight basket / 铝 | 20d | -18.67% | -11.42% | -7.24% | 0.75 | 1.14 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 60d | -36.63% | -16.70% | -19.93% | 0.77 | 1.03 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 120d | -29.00% | -7.14% | -21.85% | 0.82 | 1.05 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铝 | 250d | 26.33% | 51.97% | -25.64% | 0.83 | 1.12 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-24 to 2026-07-09 |
| style_index_daily | ready | CSI 1000 / 中证1000; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.