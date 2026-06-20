# Relative strength and index linkage for 002714.SZ as of 2026-06-20

- Company: 牧原股份
- Tushare industry: 农业综合
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=农业综合; equal-weight daily-return basket from peers: 300498.SZ, 002157.SZ, 002299.SZ, 300761.SZ, 605296.SH, 600201.SH, 002458.SZ, 000061.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -14.84% | 3.01% | -17.85% | 0.08 | 0.07 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -31.99% | 11.77% | -43.76% | 0.29 | 0.39 | strong_underperform |
| CSI 500 / 中证500 | 120d | -31.45% | 23.88% | -55.33% | 0.20 | 0.26 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 250d | -21.48% | 49.39% | -70.87% | 0.24 | 0.33 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 20d | -14.84% | -7.39% | -7.45% | 0.64 | 0.75 | modest_underperform |
| Tushare same-industry equal-weight basket / 农业综合 | 60d | -31.99% | -17.93% | -14.06% | 0.70 | 0.89 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 120d | -31.45% | -10.47% | -20.98% | 0.67 | 0.88 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 250d | -21.48% | -0.81% | -20.67% | 0.67 | 0.95 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-05 to 2026-06-18 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.