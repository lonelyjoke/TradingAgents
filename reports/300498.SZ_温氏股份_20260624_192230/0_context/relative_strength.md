# Relative strength and index linkage for 300498.SZ as of 2026-06-24

- Company: 温氏股份
- Tushare industry: 农业综合
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=农业综合; equal-weight daily-return basket from peers: 002714.SZ, 002157.SZ, 002299.SZ, 300761.SZ, 600201.SH, 605296.SH, 002458.SZ, 000061.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -15.06% | 5.15% | -20.21% | -0.19 | -0.13 | strong_underperform_low_correlation |
| ChiNext Index / 创业板指 | 60d | -30.03% | 28.17% | -58.20% | 0.07 | 0.05 | strong_underperform_low_correlation |
| ChiNext Index / 创业板指 | 120d | -30.85% | 36.17% | -67.02% | 0.07 | 0.06 | strong_underperform_low_correlation |
| ChiNext Index / 创业板指 | 250d | -33.84% | 105.67% | -139.50% | 0.10 | 0.08 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 20d | -15.06% | -6.66% | -8.40% | 0.71 | 0.84 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 60d | -30.03% | -15.40% | -14.63% | 0.70 | 0.79 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 120d | -30.85% | -12.53% | -18.32% | 0.67 | 0.69 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 农业综合 | 250d | -33.84% | -0.49% | -33.35% | 0.69 | 0.77 | strong_underperform_high_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-06-09 to 2026-06-24 |
| style_index_daily | ready | ChiNext Index / 创业板指; 254 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.