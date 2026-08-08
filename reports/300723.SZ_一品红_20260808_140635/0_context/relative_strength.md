# Relative strength and index linkage for 300723.SZ as of 2026-08-08

- Company: 一品红
- Tushare industry: 化学制药
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=化学制药; equal-weight daily-return basket from peers: 603259.SH, 600276.SH, 688506.SH, 002001.SZ, 300759.SZ, 002653.SZ, 002422.SZ, 600196.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -4.43% | -7.28% | 2.85% | 0.72 | 0.71 | in_line_high_correlation |
| ChiNext Index / 创业板指 | 60d | -5.21% | -9.82% | 4.61% | 0.23 | 0.35 | modest_outperform_low_correlation |
| ChiNext Index / 创业板指 | 120d | 12.06% | 9.29% | 2.78% | 0.27 | 0.43 | in_line |
| ChiNext Index / 创业板指 | 250d | -49.28% | 50.81% | -100.09% | 0.22 | 0.42 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 化学制药 | 20d | -4.43% | 5.86% | -10.29% | 0.76 | 0.91 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 化学制药 | 60d | -5.21% | 21.70% | -26.91% | 0.72 | 1.21 | strong_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 化学制药 | 120d | 12.06% | 18.97% | -6.90% | 0.72 | 1.25 | modest_underperform_high_correlation |
| Tushare same-industry equal-weight basket / 化学制药 | 250d | -49.28% | 14.76% | -64.04% | 0.62 | 1.32 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-07-24 to 2026-08-07 |
| style_index_daily | ready | ChiNext Index / 创业板指; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.