# Relative strength and index linkage for 600309.SH as of 2026-06-30

- Company: 万华化学
- Tushare industry: 化工原料
- Verdict: relative_laggard
- Buy-side read: The stock has lagged its style or industry proxy over medium/long windows.
- PM use: Use this as a warning or contrarian screen: if fundamentals are improving, ask why the market disagrees; if fundamentals are weak, avoid averaging down too early.

## Benchmark Selection
| benchmark_type | benchmark | selection_basis |
| --- | --- | --- |
| style_or_broad_index | CSI 300 / 沪深300 (000300.SH) | 大市值股票用沪深300作为风格基准。 |
| industry_proxy | same-industry basket (12 peers) | Tushare stock_basic industry=化工原料; equal-weight daily-return basket from peers: 600989.SH, 600160.SH, 002709.SZ, 300054.SZ, 600378.SH, 002648.SZ, 601208.SH, 300037.SZ |

## Relative Strength Window Table
| benchmark | window | stock_return | benchmark_return | excess_return | correlation | beta | relative_read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSI 300 / 沪深300 | 20d | -9.81% | 2.79% | -12.60% | 0.49 | 0.99 | strong_underperform |
| CSI 300 / 沪深300 | 60d | -13.90% | 11.90% | -25.79% | 0.36 | 0.72 | strong_underperform |
| CSI 300 / 沪深300 | 120d | -10.82% | 7.26% | -18.08% | 0.42 | 0.98 | strong_underperform |
| CSI 300 / 沪深300 | 250d | 26.78% | 28.50% | -1.72% | 0.44 | 0.99 | in_line |
| Tushare same-industry equal-weight basket / 化工原料 | 20d | -9.81% | 32.23% | -42.04% | 0.25 | 0.31 | strong_underperform |
| Tushare same-industry equal-weight basket / 化工原料 | 60d | -13.90% | 56.49% | -70.39% | 0.31 | 0.34 | strong_underperform |
| Tushare same-industry equal-weight basket / 化工原料 | 120d | -10.82% | 86.15% | -96.97% | 0.38 | 0.49 | strong_underperform |
| Tushare same-industry equal-weight basket / 化工原料 | 250d | 26.78% | 278.97% | -252.19% | 0.42 | 0.51 | strong_underperform |

## Data Coverage
| item | status | detail |
| --- | --- | --- |
| stock_daily | ready | 253 observations; 2025-06-16 to 2026-06-30 |
| style_index_daily | ready | CSI 300 / 沪深300; 253 observations |
| same_industry_basket | ready | 12 peers used; notes: none |

## Analyst Instructions
- Use this module as market validation and position-timing evidence, not as a replacement for fundamentals.
- High excess return plus high correlation usually means benchmark/sector beta is important; require company evidence before calling it alpha.
- Strong relative performance with low correlation can indicate stock-specific capital preference, hidden catalysts, or crowding; verify against filings, news, peers, and expectations.
- Persistent underperformance versus the industry proxy is a warning when fundamentals are weak, but can be a contrarian setup if valuation and operating evidence are improving.
- PM reports should include a standalone `相对走势与指数联动` module when this context is ready: trend versus benchmark, correlation/Beta, stronger/weaker verdict, and what it means for sizing, entry timing, and thesis validation.