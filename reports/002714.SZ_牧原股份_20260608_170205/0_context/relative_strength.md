# Relative strength and index linkage for 002714.SZ as of 2026-06-08

- Company: 牧原股份
- Tushare industry: 农业综合
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=农业综合; equal-weight daily-return basket from peers: 000019.SZ, 000048.SZ, 000061.SZ, 000735.SZ, 000930.SZ, 600127.SH, 600195.SH, 600201.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -22.95% | -9.91% | -13.03% | -0.34 | -0.37 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -29.34% | -5.31% | -24.03% | 0.24 | 0.33 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 120d | -30.25% | 13.56% | -43.81% | 0.21 | 0.27 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 250d | -11.96% | 40.89% | -52.85% | 0.24 | 0.34 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 20d | -22.95% | -15.30% | -7.65% | 0.35 | 0.45 | modest_underperform |
| Tushare same-industry equal-weight basket / 农业综合 | 60d | -29.34% | -23.45% | -5.89% | 0.47 | 0.62 | modest_underperform |
| Tushare same-industry equal-weight basket / 农业综合 | 120d | -30.25% | -16.15% | -14.10% | 0.46 | 0.60 | strong_underperform |
| Tushare same-industry equal-weight basket / 农业综合 | 250d | -11.96% | -3.09% | -8.87% | 0.43 | 0.64 | modest_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-26 to 2026-06-08 |
| style_index_daily | ready | CSI 500 / 中证500; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.