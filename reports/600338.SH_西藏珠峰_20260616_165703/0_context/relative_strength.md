# Relative strength and index linkage for 600338.SH as of 2026-06-16

- Company: 西藏珠峰
- Tushare industry: 铅锌
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 1000 / 中证1000 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铅锌; equal-weight daily-return basket from peers: 000426.SZ, 600497.SH, 000688.SZ, 000060.SZ, 600961.SH, 601020.SH, 000603.SZ, 603132.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -9.21% | -1.84% | -7.37% | 0.58 | 0.83 | modest_underperform |
| CSI 1000 / 中证1000 | 60d | 9.18% | 6.79% | 2.39% | 0.48 | 1.19 | in_line |
| CSI 1000 / 中证1000 | 120d | 35.51% | 17.30% | 18.21% | 0.54 | 1.38 | strong_outperform |
| CSI 1000 / 中证1000 | 250d | 85.04% | 40.20% | 44.84% | 0.53 | 1.37 | strong_outperform |
| Tushare same-industry equal-weight basket / 铅锌 | 20d | -9.21% | -3.15% | -6.06% | 0.79 | 0.62 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铅锌 | 60d | 9.18% | 1.42% | 7.76% | 0.61 | 0.88 | modest_outperform |
| Tushare same-industry equal-weight basket / 铅锌 | 120d | 35.51% | 31.00% | 4.52% | 0.68 | 0.83 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 铅锌 | 250d | 85.04% | 101.42% | -16.38% | 0.68 | 0.86 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-03 to 2026-06-16 |
| style_index_daily | ready | CSI 1000 / 中证1000; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.