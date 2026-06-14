# Relative strength and index linkage for 300285.SZ as of 2026-06-12

- Company: 国瓷材料
- Tushare industry: 陶瓷
- Verdict: relative_outperformer
- Buy-side read: The stock has delivered clear medium/long-window excess return versus ChiNext Index / 创业板指 and same-industry basket (4 peers). Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Treat price action as market confirmation, but still test whether the outperformance is company alpha or sector/theme beta before increasing valuation credit.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | ChiNext Index / 创业板指 (399006.SZ) | 创业板股票优先用创业板指作为风格基准。 |
| industry_proxy | same-industry basket (4 peers) | Tushare stock_basic industry=陶瓷; equal-weight daily-return basket from peers: 003012.SZ, 300234.SZ, 002918.SZ, 002162.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChiNext Index / 创业板指 | 20d | 43.33% | -2.51% | 45.85% | 0.69 | 2.57 | strong_outperform_high_correlation |
| ChiNext Index / 创业板指 | 60d | 50.66% | 14.10% | 36.56% | 0.56 | 1.48 | strong_outperform |
| ChiNext Index / 创业板指 | 120d | 139.09% | 19.36% | 119.73% | 0.55 | 1.64 | strong_outperform |
| ChiNext Index / 创业板指 | 250d | 244.95% | 91.26% | 153.69% | 0.52 | 1.20 | strong_outperform |
| Tushare same-industry equal-weight basket / 陶瓷 | 20d | 43.33% | -8.57% | 51.90% | 0.36 | 1.34 | strong_outperform |
| Tushare same-industry equal-weight basket / 陶瓷 | 60d | 50.66% | -4.28% | 54.93% | 0.31 | 0.76 | strong_outperform |
| Tushare same-industry equal-weight basket / 陶瓷 | 120d | 139.09% | -1.70% | 140.79% | 0.24 | 0.67 | strong_outperform_low_correlation |
| Tushare same-industry equal-weight basket / 陶瓷 | 250d | 244.95% | 24.42% | 220.53% | 0.24 | 0.60 | strong_outperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-05-28 to 2026-06-12 |
| style_index_daily | ready | ChiNext Index / 创业板指; 254 observations |
| same_industry_basket | ready | 4 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.