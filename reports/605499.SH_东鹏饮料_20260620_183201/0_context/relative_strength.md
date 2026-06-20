# Relative strength and index linkage for 605499.SH as of 2026-06-20

- Company: 东鹏饮料
- Tushare industry: 软饮料
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (8 peers) | Tushare stock_basic industry=软饮料; equal-weight daily-return basket from peers: 603156.SH, 605198.SH, 000848.SZ, 600962.SH, 300997.SZ, 600189.SH, 603711.SH, 600300.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -18.09% | 3.01% | -21.10% | -0.34 | -0.50 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -47.13% | 11.77% | -58.89% | 0.19 | 0.44 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 120d | -54.34% | 23.88% | -78.22% | 0.12 | 0.25 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 250d | -63.89% | 49.39% | -113.28% | 0.11 | 0.20 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 软饮料 | 20d | -18.09% | -1.30% | -16.79% | 0.14 | 0.22 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 软饮料 | 60d | -47.13% | 15.75% | -62.87% | 0.06 | 0.13 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 软饮料 | 120d | -54.34% | 11.22% | -65.56% | 0.06 | 0.13 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 软饮料 | 250d | -63.89% | 20.27% | -84.16% | 0.12 | 0.21 | strong_underperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-05 to 2026-06-18 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 8 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.