# Relative strength and index linkage for 600415.SH as of 2026-06-06

- Company: 小商品城
- Tushare industry: 商品城
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 500 / 中证500 (000905.SH) | 中等市值股票用中证500作为风格基准。 |
| industry_proxy | same-industry basket (3 peers) | Tushare stock_basic industry=商品城; equal-weight daily-return basket from peers: 000058.SZ, 600790.SH, 002344.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 500 / 中证500 | 20d | -9.01% | -5.10% | -3.92% | 0.07 | 0.13 | modest_underperform_low_correlation |
| CSI 500 / 中证500 | 60d | -15.76% | -0.34% | -15.42% | 0.37 | 0.60 | strong_underperform |
| CSI 500 / 中证500 | 120d | -26.83% | 17.93% | -44.76% | 0.31 | 0.46 | strong_underperform |
| CSI 500 / 中证500 | 250d | -30.53% | 45.54% | -76.07% | 0.27 | 0.53 | strong_underperform |
| Tushare same-industry equal-weight basket / 商品城 | 20d | -9.01% | -14.84% | 5.83% | 0.37 | 0.52 | modest_outperform |
| Tushare same-industry equal-weight basket / 商品城 | 60d | -15.76% | -10.62% | -5.14% | 0.49 | 0.70 | modest_underperform |
| Tushare same-industry equal-weight basket / 商品城 | 120d | -26.83% | -13.13% | -13.70% | 0.44 | 0.62 | strong_underperform |
| Tushare same-industry equal-weight basket / 商品城 | 250d | -30.53% | -3.97% | -26.56% | 0.24 | 0.43 | strong_underperform_low_correlation |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-05-22 to 2026-06-05 |
| style_index_daily | ready | CSI 500 / 中证500; 253 observations |
| same_industry_basket | ready | 3 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.