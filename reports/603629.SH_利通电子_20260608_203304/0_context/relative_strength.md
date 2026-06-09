# Relative strength and index linkage for 603629.SH as of 2026-06-08

- Company: 利通电子
- Tushare industry: 元器件
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus CSI 1000 / 中证1000 and same-industry basket (12 peers). Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=元器件; equal-weight daily-return basket from peers: 000020.SZ, 000021.SZ, 000045.SZ, 000050.SZ, 000062.SZ, 000100.SZ, 000509.SZ, 000536.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -0.29% | -8.86% | 8.56% | 0.35 | 1.44 | modest_outperform |
| CSI 1000 / 中证1000 | 60d | 182.77% | -3.22% | 185.99% | 0.41 | 1.56 | strong_outperform |
| CSI 1000 / 中证1000 | 120d | 531.18% | 11.49% | 519.70% | 0.30 | 1.08 | strong_outperform |
| CSI 1000 / 中证1000 | 250d | 612.02% | 34.50% | 577.52% | 0.33 | 1.06 | strong_outperform |
| Tushare same-industry equal-weight basket / 元器件 | 20d | -0.29% | 9.21% | -9.50% | 0.12 | 0.29 | modest_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 60d | 182.77% | 12.43% | 170.34% | 0.17 | 0.48 | strong_outperform_low_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 120d | 531.18% | 21.59% | 509.60% | 0.14 | 0.38 | strong_outperform_low_correlation |
| Tushare same-industry equal-weight basket / 元器件 | 250d | 612.02% | 42.92% | 569.10% | 0.22 | 0.54 | strong_outperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 252 observations; 2025-05-26 to 2026-06-08 |
| style_index_daily | ready | CSI 1000 / 中证1000; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.