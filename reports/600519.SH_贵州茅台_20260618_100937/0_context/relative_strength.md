# Relative strength and index linkage for 600519.SH as of 2026-06-18

- Company: 贵州茅台
- Tushare industry: 白酒
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=白酒; equal-weight daily-return basket from peers: 000858.SZ, 600809.SH, 000568.SZ, 002304.SZ, 000596.SZ, 603369.SH, 603198.SH, 600779.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -5.70% | 1.66% | -7.37% | -0.29 | -0.35 | modest_underperform_low_correlation |
| CSI 300 / 沪深300 | 60d | -14.65% | 7.60% | -22.25% | 0.02 | 0.02 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 120d | -13.04% | 8.33% | -21.38% | 0.15 | 0.22 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 250d | -17.68% | 27.29% | -44.98% | 0.22 | 0.29 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 白酒 | 20d | -5.70% | -8.86% | 3.16% | 0.75 | 0.56 | modest_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 白酒 | 60d | -14.65% | -18.08% | 3.42% | 0.61 | 0.48 | modest_outperform |
| Tushare same-industry equal-weight basket / 白酒 | 120d | -13.04% | -30.88% | 17.84% | 0.71 | 0.62 | strong_outperform_high_correlation |
| Tushare same-industry equal-weight basket / 白酒 | 250d | -17.68% | -31.98% | 14.29% | 0.71 | 0.55 | strong_outperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-03 to 2026-06-17 |
| style_index_daily | ready | CSI 300 / 沪深300; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.