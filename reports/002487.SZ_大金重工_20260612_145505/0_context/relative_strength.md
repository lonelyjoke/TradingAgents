# Relative strength and index linkage for 002487.SZ as of 2026-06-12

- Company: 大金重工
- Tushare industry: 电气设备
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 1000 / 中证1000 and same-industry basket (12 peers). Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=电气设备; equal-weight daily-return basket from peers: 300750.SZ, 300274.SZ, 600406.SH, 002028.SZ, 605117.SH, 300014.SZ, 600089.SH, 601727.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -27.59% | -7.05% | -20.53% | 0.57 | 0.96 | strong_underperform |
| CSI 1000 / 中证1000 | 60d | -27.49% | -0.67% | -26.82% | 0.27 | 0.50 | strong_underperform |
| CSI 1000 / 中证1000 | 120d | 2.52% | 10.55% | -8.03% | 0.22 | 0.47 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | 113.43% | 35.39% | 78.04% | 0.24 | 0.56 | strong_outperform_low_correlation |
| Tushare same-industry equal-weight basket / 电气设备 | 20d | -27.59% | -11.80% | -15.79% | 0.63 | 0.96 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 60d | -27.49% | -8.99% | -18.50% | 0.38 | 0.61 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 120d | 2.52% | 16.87% | -14.35% | 0.32 | 0.57 | strong_underperform |
| Tushare same-industry equal-weight basket / 电气设备 | 250d | 113.43% | 93.03% | 20.41% | 0.36 | 0.59 | strong_outperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-05-28 to 2026-06-11 |
| style_index_daily | ready | CSI 1000 / 中证1000; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.