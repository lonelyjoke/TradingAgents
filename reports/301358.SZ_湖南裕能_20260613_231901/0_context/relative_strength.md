# Relative strength and index linkage for 301358.SZ as of 2026-06-13

- Company: 湖南裕能
- Tushare industry: 电气设备
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus ChiNext Index / 创业板指 and same-industry basket (12 peers).
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=电气设备; equal-weight daily-return basket from peers: 300750.SZ, 300274.SZ, 600406.SH, 002028.SZ, 605117.SH, 300014.SZ, 600089.SH, 601727.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | -23.90% | -2.51% | -21.39% | 0.33 | 0.51 | strong_underperform |
| ChiNext Index / 创业板指 | 60d | -9.38% | 14.10% | -23.48% | 0.44 | 0.90 | strong_underperform |
| ChiNext Index / 创业板指 | 120d | 5.72% | 19.36% | -13.64% | 0.36 | 0.75 | strong_underperform |
| ChiNext Index / 创业板指 | 250d | 163.36% | 91.26% | 72.10% | 0.39 | 0.86 | strong_outperform |
| Tushare same-industry equal-weight basket / 电气设备 | 20d | -23.90% | -9.40% | -14.50% | 0.48 | 0.84 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 60d | -9.38% | -6.77% | -2.61% | 0.56 | 1.18 | in_line |
| Tushare same-industry equal-weight basket / 电气设备 | 120d | 5.72% | 20.04% | -14.32% | 0.46 | 0.92 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 250d | 163.36% | 96.87% | 66.48% | 0.50 | 1.04 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-05-29 to 2026-06-12 |
| style_index_daily | ready | ChiNext Index / 创业板指; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.