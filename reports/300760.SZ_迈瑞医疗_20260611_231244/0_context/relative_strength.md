# Relative strength and index linkage for 300760.SZ as of 2026-06-11

- Company: 迈瑞医疗
- Tushare industry: 医疗保健
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=医疗保健; equal-weight daily-return basket from peers: 688271.SH, 300015.SZ, 688301.SH, 300832.SZ, 300347.SZ, 300677.SZ, 002432.SZ, 688617.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -8.91% | -3.54% | -5.37% | -0.44 | -0.32 | modest_underperform_low_correlation |
| ChiNext Index / 创业板指 | 60d | -17.75% | 15.13% | -32.88% | 0.22 | 0.19 | strong_underperform_low_correlation |
| ChiNext Index / 创业板指 | 120d | -26.08% | 18.75% | -44.83% | 0.29 | 0.27 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | -34.97% | 91.21% | -126.19% | 0.33 | 0.29 | strong_underperform |
| Tushare same-industry equal-weight basket / 医疗保健 | 20d | -8.91% | -10.30% | 1.39% | 0.61 | 0.93 | in_line |
| Tushare same-industry equal-weight basket / 医疗保健 | 60d | -17.75% | -10.98% | -6.76% | 0.53 | 0.68 | modest_underperform |
| Tushare same-industry equal-weight basket / 医疗保健 | 120d | -26.08% | -2.00% | -24.09% | 0.60 | 0.72 | strong_underperform |
| Tushare same-industry equal-weight basket / 医疗保健 | 250d | -34.97% | 12.06% | -47.03% | 0.51 | 0.63 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-05-27 to 2026-06-11 |
| style_index_daily | ready | ChiNext Index / 创业板指; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.