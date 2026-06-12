# Relative strength and index linkage for 002594.SZ as of 2026-06-12

- Company: 比亚迪
- Tushare industry: 汽车整车
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (11 peers) | Tushare stock_basic industry=汽车整车; equal-weight daily-return basket from peers: 601633.SH, 600104.SH, 601127.SH, 000625.SZ, 600418.SH, 600066.SH, 601238.SH, 600733.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -9.04% | -3.91% | -5.13% | 0.65 | 0.97 | modest_underperform |
| CSI 300 / 沪深300 | 60d | -9.90% | 1.14% | -11.04% | 0.28 | 0.46 | strong_underperform |
| CSI 300 / 沪深300 | 120d | -6.49% | 2.70% | -9.19% | 0.29 | 0.55 | modest_underperform |
| CSI 300 / 沪深300 | 250d | -74.51% | 22.97% | -97.48% | 0.14 | 0.66 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 汽车整车 | 20d | -9.04% | -15.85% | 6.80% | 0.62 | 1.11 | modest_outperform |
| Tushare same-industry equal-weight basket / 汽车整车 | 60d | -9.90% | -21.30% | 11.40% | 0.35 | 0.61 | strong_outperform |
| Tushare same-industry equal-weight basket / 汽车整车 | 120d | -6.49% | -24.01% | 17.53% | 0.28 | 0.51 | strong_outperform |
| Tushare same-industry equal-weight basket / 汽车整车 | 250d | -74.51% | -18.86% | -55.65% | 0.13 | 0.58 | strong_underperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-05-28 to 2026-06-11 |
| style_index_daily | ready | CSI 300 / 沪深300; 253 observations |
| same_industry_basket | ready | 11 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.