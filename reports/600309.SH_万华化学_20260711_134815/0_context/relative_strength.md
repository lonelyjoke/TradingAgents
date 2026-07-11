# Relative strength and index linkage for 600309.SH as of 2026-07-11

- Company: 万华化学
- Tushare industry: 化工原料
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=化工原料; equal-weight daily-return basket from peers: 600989.SH, 600160.SH, 002709.SZ, 300054.SZ, 600378.SH, 002648.SZ, 688585.SH, 688548.SH |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | 2.32% | 1.24% | 1.09% | 0.35 | 0.65 | in_line |
| CSI 300 / 沪深300 | 60d | -25.48% | 2.90% | -28.37% | 0.30 | 0.53 | strong_underperform |
| CSI 300 / 沪深300 | 120d | -13.78% | 0.91% | -14.69% | 0.36 | 0.77 | strong_underperform |
| CSI 300 / 沪深300 | 250d | 26.63% | 21.46% | 5.17% | 0.41 | 0.90 | modest_outperform |
| Tushare same-industry equal-weight basket / 化工原料 | 20d | 2.32% | 1.26% | 1.06% | 0.15 | 0.14 | in_line_low_correlation |
| Tushare same-industry equal-weight basket / 化工原料 | 60d | -25.48% | 23.32% | -48.80% | 0.20 | 0.18 | strong_underperform_low_correlation |
| Tushare same-industry equal-weight basket / 化工原料 | 120d | -13.78% | 44.56% | -58.34% | 0.34 | 0.39 | strong_underperform |
| Tushare same-industry equal-weight basket / 化工原料 | 250d | 26.63% | 205.52% | -178.89% | 0.39 | 0.45 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-26 to 2026-07-10 |
| style_index_daily | ready | CSI 300 / 沪深300; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.