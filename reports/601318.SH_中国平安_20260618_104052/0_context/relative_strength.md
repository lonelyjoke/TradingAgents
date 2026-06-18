# Relative strength and index linkage for 601318.SH as of 2026-06-18

- Company: 中国平安
- Tushare industry: 保险
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is high, so part of the move is likely benchmark/sector beta rather than pure company alpha.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (4 peers) | Tushare stock_basic industry=保险; equal-weight daily-return basket from peers: 601628.SH, 601601.SH, 601319.SH, 601336.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -2.49% | 1.66% | -4.16% | 0.35 | 0.34 | modest_underperform |
| CSI 300 / 沪深300 | 60d | -12.97% | 7.60% | -20.56% | 0.63 | 0.80 | strong_underperform |
| CSI 300 / 沪深300 | 120d | -21.35% | 8.33% | -29.68% | 0.57 | 0.90 | strong_underperform |
| CSI 300 / 沪深300 | 250d | -1.22% | 27.29% | -28.51% | 0.49 | 0.79 | strong_underperform |
| Tushare same-industry equal-weight basket / 保险 | 20d | -2.49% | 0.73% | -3.23% | 0.60 | 0.46 | modest_underperform |
| Tushare same-industry equal-weight basket / 保险 | 60d | -12.97% | -15.73% | 2.76% | 0.83 | 0.71 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 保险 | 120d | -21.35% | -17.83% | -3.52% | 0.83 | 0.75 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 保险 | 250d | -1.22% | -4.61% | 3.39% | 0.83 | 0.75 | modest_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-03 to 2026-06-17 |
| style_index_daily | ready | CSI 300 / 沪深300; 254 observations |
| same_industry_basket | ready | 4 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.