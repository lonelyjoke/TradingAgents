# Relative strength and index linkage for 600323.SH as of 2026-06-22

- Company: 瀚蓝环境
- Tushare industry: 环境保护
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 1000 / 中证1000 (000852.SH) | 小市值股票用中证1000作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=环境保护; equal-weight daily-return basket from peers: 000967.SZ, 603568.SH, 002266.SZ, 603588.SH, 600388.SH, 300779.SZ, 301500.SZ, 300140.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 1000 / 中证1000 | 20d | -8.01% | 1.99% | -10.00% | -0.56 | -0.64 | modest_underperform_low_correlation |
| CSI 1000 / 中证1000 | 60d | -4.98% | 12.09% | -17.07% | -0.02 | -0.03 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 120d | -5.91% | 21.30% | -27.20% | 0.03 | 0.04 | strong_underperform_low_correlation |
| CSI 1000 / 中证1000 | 250d | 13.16% | 42.56% | -29.40% | 0.05 | 0.06 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 环境保护 | 20d | -8.01% | -5.28% | -2.72% | -0.43 | -0.57 | in_line_low_correlation |
| Tushare same-industry equal-weight basket / 环境保护 | 60d | -4.98% | -3.50% | -1.48% | 0.19 | 0.22 | in_line_low_correlation |
| Tushare same-industry equal-weight basket / 环境保护 | 120d | -5.91% | 21.84% | -27.74% | 0.20 | 0.22 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 环境保护 | 250d | 13.75% | 32.00% | -18.25% | 0.22 | 0.27 | strong_underperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 250 observations; 2025-06-09 to 2026-06-22 |
| style_index_daily | ready | CSI 1000 / 中证1000; 252 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.