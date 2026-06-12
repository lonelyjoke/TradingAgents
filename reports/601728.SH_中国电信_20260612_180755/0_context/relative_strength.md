# Relative strength and index linkage for 601728.SH as of 2026-06-12

- Company: 中国电信
- Tushare industry: 电信运营
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows. Correlation is low in at least one key window, suggesting stock-specific forces may be more important than benchmark beta.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (4 peers) | Tushare stock_basic industry=电信运营; equal-weight daily-return basket from peers: 600941.SH, 601698.SH, 600050.SH, 300959.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -4.42% | -1.69% | -2.73% | -0.12 | -0.32 | in_line_low_correlation |
| CSI 300 / 沪深300 | 60d | -0.98% | 2.26% | -3.25% | 0.06 | 0.09 | modest_underperform_low_correlation |
| CSI 300 / 沪深300 | 120d | -11.03% | 4.04% | -15.07% | 0.08 | 0.13 | strong_underperform_low_correlation |
| CSI 300 / 沪深300 | 250d | -23.90% | 24.02% | -47.92% | 0.11 | 0.16 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 电信运营 | 20d | -4.42% | -2.64% | -1.78% | 0.40 | 0.65 | in_line |
| Tushare same-industry equal-weight basket / 电信运营 | 60d | -0.98% | 15.68% | -16.66% | 0.42 | 0.42 | strong_underperform |
| Tushare same-industry equal-weight basket / 电信运营 | 120d | -11.03% | 14.09% | -25.12% | 0.34 | 0.29 | strong_underperform |
| Tushare same-industry equal-weight basket / 电信运营 | 250d | -23.90% | 61.89% | -85.79% | 0.26 | 0.19 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 254 observations; 2025-05-28 to 2026-06-12 |
| style_index_daily | ready | CSI 300 / 沪深300; 254 observations |
| same_industry_basket | ready | 4 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.