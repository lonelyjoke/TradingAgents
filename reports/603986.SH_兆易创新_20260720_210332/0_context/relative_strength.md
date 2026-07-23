# Relative strength and index linkage for 603986.SH as of 2026-07-20

- Company: 兆易创新
- Tushare industry: 半导体
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 300 / 沪深300 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=半导体; equal-weight daily-return basket from peers: 688981.SH, 688256.SH, 688041.SH, 688347.SH, 002371.SZ, 688802.SH, 688012.SH, 688795.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -37.32% | -9.12% | -28.20% | 0.73 | 2.81 | strong_underperform_high_correlation |
| CSI 300 / 沪深300 | 60d | 41.15% | -3.56% | 44.71% | 0.70 | 2.98 | strong_outperform_high_correlation |
| CSI 300 / 沪深300 | 120d | 54.14% | -2.82% | 56.96% | 0.65 | 2.67 | strong_outperform |
| CSI 300 / 沪深300 | 250d | 255.19% | 15.00% | 240.19% | 0.64 | 2.69 | strong_outperform |
| Tushare same-industry equal-weight basket / 半导体 | 20d | -37.32% | -10.58% | -26.74% | 0.73 | 1.08 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 60d | 41.15% | 38.99% | 2.16% | 0.70 | 0.97 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 120d | 54.14% | 44.67% | 9.47% | 0.70 | 1.02 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 250d | 255.19% | 212.55% | 42.64% | 0.68 | 0.97 | strong_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-07-07 to 2026-07-20 |
| style_index_daily | ready | CSI 300 / 沪深300; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.