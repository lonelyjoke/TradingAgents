# Relative strength and index linkage for 603986.SH as of 2026-07-19

- Company: 兆易创新
- Tushare industry: 半导体
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 300 / 沪深300 and same-industry basket (12 peers). Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=半导体; equal-weight daily-return basket from peers: 688981.SH, 688256.SH, 688041.SH, 688347.SH, 002371.SZ, 688012.SH, 688802.SH, 688795.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -26.37% | -8.35% | -18.02% | 0.82 | 3.24 | strong_underperform_high_correlation |
| CSI 300 / 沪深300 | 60d | 59.41% | -4.80% | 64.21% | 0.74 | 3.15 | strong_outperform_high_correlation |
| CSI 300 / 沪深300 | 120d | 81.66% | -4.68% | 86.34% | 0.66 | 2.74 | strong_outperform_high_correlation |
| CSI 300 / 沪深300 | 250d | 283.37% | 14.22% | 269.15% | 0.66 | 2.74 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 20d | -26.37% | -6.98% | -19.39% | 0.74 | 1.13 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 60d | 59.41% | 38.10% | 21.31% | 0.69 | 0.95 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 120d | 81.66% | 49.09% | 32.57% | 0.69 | 1.03 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 半导体 | 250d | 283.37% | 221.70% | 61.67% | 0.68 | 0.97 | strong_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-07-04 to 2026-07-17 |
| style_index_daily | ready | CSI 300 / 沪深300; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.