# Relative strength and index linkage for 600809.SH as of 2026-07-14

- Company: 山西汾酒
- Tushare industry: 白酒
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=白酒; equal-weight daily-return basket from peers: 600519.SH, 000858.SZ, 000568.SZ, 002304.SZ, 000596.SZ, 603369.SH, 603198.SH, 600779.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -7.58% | 0.39% | -7.97% | 0.09 | 0.09 | modest_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -21.21% | 0.61% | -21.83% | 0.01 | 0.01 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 120d | -37.94% | 1.01% | -38.95% | 0.06 | 0.06 | strong_underperform_low_correlation |
| CSI 500 / 中证500 | 250d | -37.19% | 37.13% | -74.31% | 0.14 | 0.17 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 白酒 | 20d | -7.58% | -7.40% | -0.18% | 0.86 | 1.09 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 白酒 | 60d | -21.21% | -20.01% | -1.21% | 0.80 | 0.87 | in_line_high_correlation |
| Tushare same-industry equal-weight basket / 白酒 | 120d | -37.94% | -32.44% | -5.50% | 0.85 | 0.90 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 白酒 | 250d | -37.19% | -31.45% | -5.73% | 0.85 | 0.95 | modest_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-06-30 to 2026-07-13 |
| style_index_daily | ready | CSI 500 / 中证500; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.