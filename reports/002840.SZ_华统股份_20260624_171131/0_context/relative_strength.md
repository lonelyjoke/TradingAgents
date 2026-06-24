# Relative strength and index linkage for 002840.SZ as of 2026-06-24

- Company: 华统股份
- Tushare industry: 食品
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=食品; equal-weight daily-return basket from peers: 603288.SH, 300999.SZ, 000895.SZ, 300765.SZ, 300972.SZ, 600298.SH, 603345.SH, 600186.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -21.67% | 1.22% | -22.89% | 0.02 | 0.03 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | -31.39% | 13.45% | -44.84% | 0.04 | 0.09 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | -23.53% | 19.97% | -43.50% | 0.00 | 0.01 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | -30.36% | 42.01% | -72.37% | 0.07 | 0.11 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 食品 | 20d | -21.67% | -6.29% | -15.38% | 0.07 | 0.12 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 食品 | 60d | -31.39% | -2.65% | -28.74% | 0.24 | 0.76 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 食品 | 120d | -23.53% | -4.35% | -19.18% | 0.18 | 0.44 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 食品 | 250d | -30.36% | 0.15% | -30.51% | 0.20 | 0.41 | strong_underperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-09 to 2026-06-24 |
| style_index_daily | ready | CSI 1000 / 中证1000; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.