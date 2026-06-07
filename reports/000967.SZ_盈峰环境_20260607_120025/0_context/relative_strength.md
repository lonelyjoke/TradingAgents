# Relative strength and index linkage for 000967.SZ as of 2026-06-07

- Company: 盈峰环境
- Tushare industry: 环境保护
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 1000 / 中证1000 and same-industry basket unavailable.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket unavailable | Tushare stock_basic industry=环境保护; equal-weight daily-return basket from peers: N/A |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -34.97% | -4.58% | -30.39% | 0.68 | 2.40 | strong_underperform_high_correlation |
| CSI 1000 / 中证1000 | 60d | 23.98% | 1.67% | 22.31% | 0.53 | 1.64 | strong_outperform |
| CSI 1000 / 中证1000 | 120d | 61.09% | 15.08% | 46.02% | 0.47 | 1.21 | strong_outperform |
| CSI 1000 / 中证1000 | 250d | 48.67% | 38.35% | 10.32% | 0.43 | 1.03 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-23 to 2026-06-05 |
| style_index_daily | ready | CSI 1000 / 中证1000; 252 observations |
| same_industry_basket | partial | 0 peers used; notes: No same-industry peer symbols available for basket proxy. |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.