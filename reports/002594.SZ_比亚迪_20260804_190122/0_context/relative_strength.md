# Relative strength and index linkage for 002594.SZ as of 2026-08-04

- Company: 比亚迪
- Tushare industry: 汽车整车
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=汽车整车; equal-weight daily-return basket from peers: 601633.SH, 600104.SH, 601127.SH, 000625.SZ, 600066.SH, 600418.SH, 601238.SH, 600733.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | 5.67% | -3.99% | 9.66% | 0.00 | 0.00 | modest_outperform_low_correlation |
| CSI 300 / 沪深300 | 60d | -9.25% | -7.09% | -2.16% | 0.19 | 0.26 | in_line_low_correlation |
| CSI 300 / 沪深300 | 120d | 4.71% | -0.11% | 4.82% | 0.16 | 0.25 | modest_outperform_low_correlation |
| CSI 300 / 沪深300 | 250d | -73.04% | 11.68% | -84.72% | 0.11 | 0.44 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 汽车整车 | 20d | 5.67% | 6.96% | -1.29% | 0.64 | 0.61 | in_line |
| Tushare same-industry equal-weight basket / 汽车整车 | 60d | -9.25% | -18.64% | 9.39% | 0.69 | 0.85 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 汽车整车 | 120d | 4.71% | -18.90% | 23.61% | 0.44 | 0.64 | strong_outperform |
| Tushare same-industry equal-weight basket / 汽车整车 | 250d | -73.04% | -20.42% | -52.62% | 0.18 | 0.69 | strong_underperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-07-21 to 2026-08-04 |
| style_index_daily | ready | CSI 300 / 沪深300; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.