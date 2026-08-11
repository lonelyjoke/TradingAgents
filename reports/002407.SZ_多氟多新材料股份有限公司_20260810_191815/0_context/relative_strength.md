# Relative strength and index linkage for 002407.SZ as of 2026-08-10

- Company: 多氟多
- Tushare industry: 化工原料
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 1000 / 中证1000 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=化工原料; equal-weight daily-return basket from peers: 600309.SH, 600989.SH, 600160.SH, 002648.SZ, 002709.SZ, 300054.SZ, 688585.SH, 600378.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -11.09% | -6.33% | -4.77% | 0.65 | 1.33 | modest_underperform |
| CSI 1000 / 中证1000 | 60d | 10.23% | -12.52% | 22.75% | 0.45 | 1.17 | strong_outperform |
| CSI 1000 / 中证1000 | 120d | 30.31% | -4.82% | 35.13% | 0.42 | 1.03 | strong_outperform |
| CSI 1000 / 中证1000 | 250d | 181.73% | 14.11% | 167.62% | 0.37 | 1.05 | strong_outperform |
| Tushare same-industry equal-weight basket / 化工原料 | 20d | -11.09% | -0.12% | -10.98% | 0.74 | 1.37 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 化工原料 | 60d | 10.23% | 6.83% | 3.40% | 0.68 | 1.37 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 化工原料 | 120d | 30.31% | 34.95% | -4.64% | 0.68 | 1.39 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 化工原料 | 250d | 183.26% | 115.20% | 68.06% | 0.60 | 1.30 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-07-28 to 2026-08-07 |
| style_index_daily | ready | CSI 1000 / 中证1000; 251 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.