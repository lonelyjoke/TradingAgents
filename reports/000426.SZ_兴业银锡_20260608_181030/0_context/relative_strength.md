# Relative strength and index linkage for 000426.SZ as of 2026-06-08

- Company: 兴业银锡
- Tushare industry: 铅锌
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 500 / 中证500 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=铅锌; equal-weight daily-return basket from peers: 000060.SZ, 000603.SZ, 000688.SZ, 000751.SZ, 000758.SZ, 600338.SH, 600497.SH, 600531.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| CSI 500 / 中证500 | 60d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| CSI 500 / 中证500 | 120d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| CSI 500 / 中证500 | 250d | N/A | N/A | N/A | N/A | N/A | insufficient_data |
| Tushare same-industry equal-weight basket / 铅锌 | 20d | -28.87% | -23.54% | -5.33% | 0.76 | 1.20 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铅锌 | 60d | -32.19% | -18.39% | -13.80% | 0.78 | 1.13 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铅锌 | 120d | 1.01% | 18.40% | -17.39% | 0.80 | 1.16 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 铅锌 | 250d | 159.51% | 75.16% | 84.35% | 0.79 | 1.19 | strong_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-26 to 2026-06-08 |
| style_index_daily | failed | CSI 500 / 中证500; 0 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.