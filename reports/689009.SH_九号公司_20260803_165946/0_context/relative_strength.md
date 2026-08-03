# Relative strength and index linkage for 689009.SH as of 2026-08-03

- Company: 九号公司
- Tushare industry: 摩托车
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=摩托车; equal-weight daily-return basket from peers: 603129.SH, 601777.SH, 603766.SH, 301345.SZ, 603529.SH, 001696.SZ, 000913.SZ, 300256.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | 12.15% | -17.93% | 30.07% | 0.21 | 0.25 | strong_outperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | 3.61% | -18.81% | 22.42% | 0.07 | 0.09 | strong_outperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | -18.79% | -15.08% | -3.71% | 0.09 | 0.11 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | -23.76% | 7.01% | -30.76% | 0.21 | 0.32 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 摩托车 | 20d | 12.15% | 2.58% | 9.57% | 0.53 | 0.96 | modest_outperform |
| Tushare same-industry equal-weight basket / 摩托车 | 60d | 3.61% | -10.32% | 13.92% | 0.41 | 0.77 | strong_outperform |
| Tushare same-industry equal-weight basket / 摩托车 | 120d | -18.79% | -10.83% | -7.96% | 0.29 | 0.48 | modest_underperform |
| Tushare same-industry equal-weight basket / 摩托车 | 250d | -23.94% | -4.01% | -19.93% | 0.33 | 0.56 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 251 observations; 2025-07-21 to 2026-07-31 |
| style_index_daily | ready | CSI 1000 / 中证1000; 251 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.