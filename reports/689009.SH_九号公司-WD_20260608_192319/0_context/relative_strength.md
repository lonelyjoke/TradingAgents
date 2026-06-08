# Relative strength and index linkage for 689009.SH as of 2026-06-08

- Company: 九号公司-WD
- Tushare industry: 摩托车
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (11 peers) | Tushare stock_basic industry=摩托车; equal-weight daily-return basket from peers: 001696.SZ, 000913.SZ, 002105.SZ, 601777.SH, 603766.SH, 603787.SH, 603129.SH, 603529.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -12.50% | -8.86% | -3.64% | -0.09 | -0.10 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | -22.41% | -3.22% | -19.19% | 0.00 | 0.00 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | -38.19% | 11.49% | -49.68% | 0.17 | 0.22 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | -42.56% | 34.50% | -77.06% | 0.26 | 0.43 | strong_underperform |
| Tushare same-industry equal-weight basket / 摩托车 | 20d | -12.50% | -11.41% | -1.09% | 0.40 | 0.58 | in_line |
| Tushare same-industry equal-weight basket / 摩托车 | 60d | -22.41% | -14.02% | -8.39% | 0.07 | 0.09 | modest_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 摩托车 | 120d | -38.19% | -11.52% | -26.67% | 0.23 | 0.32 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 摩托车 | 250d | -42.56% | 7.54% | -50.10% | 0.32 | 0.48 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-26 to 2026-06-08 |
| style_index_daily | ready | CSI 1000 / 中证1000; 252 observations |
| same_industry_basket | ready | 11 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.