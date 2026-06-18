# Price-move attribution context for 601318.SH as of 2026-06-18

- Status: ready
- Company: 中国平安
- Basket: 保险
- Attribution label: mixed_or_unclassified
- Attribution reason: No single attribution bucket dominates; use the residual table and events for judgment.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601318.SH | 中国平安 | 保险 | 52.76 | -0.434 | -2.4949 | -6.3377 | -12.213 | 0.991 | 1.2386 | 0.73 | 7.1948 | 0.9382 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 0.9654 | -1.3994 |
| same_metal_equities | 保险 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -0.4401 | 0.0061 |
| mapped_commodity | mapped futures products | N/A | N/A |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260617 | 4108.0762 | 0.3955 | -1.3 | 4.7101 |
| CSI 300 | 20260617 | 4931.3861 | 0.9654 | 1.6634 | 9.7827 |
| CSI 500 | 20260617 | 8627.0862 | 1.3999 | -0.3376 | 11.2638 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N/A | N/A | No mapped futures product | N/A | N/A | N/A | No commodity mapping; do not attribute the move to commodity prices without evidence. | N/A | N/A | N/A |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.11 | -2.8517 | -6.7518 | -5.7196 | -24.184 | 15.3509 | 4.5676 | 0.79 | 72.815 | 2.2343 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.42 | -2.7523 | -11.5614 | -8.0545 | -23.029 | 11.3869 | 2.482 | 1.09 | 23.7886 | 1.7351 |
| 300390.SZ | 天华新能 | lithium | 91.75 | -1.7876 | -0.7572 | 46.4018 | -20.0087 | 18.6587 | 3.9169 | 0.75 | 58.2083 | 6.1761 |
| 600595.SH | 中孚实业 | aluminum | 6.24 | -1.7323 | -14.7541 | -17.351 | -29.4915 | 0 | 3.824 | 0.95 | 11.3248 | 1.3944 |
| 000807.SZ | 云铝股份 | aluminum | 25 | -1.4972 | -17.9251 | -20.534 | -31.8244 | 0 | 3.7203 | 0.98 | 9.9881 | 2.4318 |
| 000933.SZ | 神火股份 | aluminum | 24.55 | -1.4452 | -18.4385 | -22.7987 | -30.6693 | 0 | 3.3414 | 0.66 | 9.8828 | 2.0529 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 38.19 | -1.3433 | -8.8762 | -10.2468 | -22.4883 | 13.1871 | 2.9691 | 0.72 | 42.7894 | 2.1317 |
| 600219.SH | 南山铝业 | aluminum | 4.63 | -1.2793 | -10.9615 | -28.6595 | -28.6595 | 2.8509 | 3.5772 | 0.73 | 12.8657 | 1.0436 |
| 002532.SZ | 天山铝业 | aluminum | 12.55 | -1.2589 | -19.2926 | -29.216 | -36.2621 | 0 | 3.5473 | 0.73 | 9.7165 | 1.8547 |
| 601600.SH | 中国铝业 | aluminum | 9.97 | -0.993 | -9.3636 | -16.7084 | -22.1094 | 0.499 | 4.2946 | 0.73 | 11.6621 | 2.1208 |
| 000792.SZ | 盐湖股份 | lithium | 30.87 | -0.8989 | -6.056 | -20.9677 | -23.5891 | 10.7752 | 2.6797 | 0.62 | 15.8374 | 3.6548 |
| 603799.SH | 华友钴业 | nickel_cobalt | 52.59 | -0.7736 | -9.4681 | -11.9833 | -22.8886 | 13.4418 | 3.0837 | 0.7 | 13.561 | 1.9748 |
| 000612.SZ | 焦作万方 | aluminum | 10.97 | -0.544 | -10.3758 | -10.9578 | -20.5072 | 5.7526 | 3.6172 | 0.78 | 9.2071 | 1.6971 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 41.43 | -0.5043 | 13.6314 | 27.5554 | -5.3029 | 22.5787 | 5.5769 | 0.84 | 29.2034 | 3.2901 |
| 601318.SH | 中国平安 | 保险 | 52.76 | -0.434 | -2.4949 | -6.3377 | -12.213 | 0.991 | 1.2386 | 0.73 | 7.1948 | 0.9382 |
| 002155.SZ | 湖南黄金 | precious_metals | 26.5 | -0.3759 | 3.8808 | -12.8289 | -17.3683 | 15.7528 | 3.2035 | 0.92 | 23.6466 | 4.7532 |
| 002460.SZ | 赣锋锂业 | lithium | 71.32 | -0.1819 | -7.5807 | -11.0168 | -22.012 | 13.8464 | 2.663 | 0.76 | 39.2887 | 3.2187 |
| 000630.SZ | 铜陵有色 | copper | 7.56 | -0.1321 | 27.7027 | 27.7027 | -1.3055 | 30.9689 | 5.0742 | 0.84 | 38.5486 | 2.7044 |
| 600547.SH | 山东黄金 | precious_metals | 28.26 | 0.0354 | -7.1921 | -30.548 | -33.4902 | 6.7649 | 2.8696 | 0.58 | 25.2531 | 4.0705 |
| 002466.SZ | 天齐锂业 | lithium | 64.04 | 0.0781 | -6.0446 | 11.8798 | -21.6253 | 13.8612 | 2.5437 | 0.81 | 49.1029 | 2.367 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 10.1 | 0.2979 | 1.3039 | 25.6219 | -7.1691 | 22.6553 | 5.4224 | 1.15 | 42.3245 | 2.9614 |
| 601899.SH | 紫金矿业 | copper | 30.43 | 0.4622 | 0.1316 | -7.169 | -14.6663 | 10.8306 | 3.6259 | 0.56 | 13.1165 | 4.1017 |
| 000878.SZ | 云南铜业 | copper | 17.93 | 0.6173 | 0.3358 | -2.4483 | -13.2979 | 11.6541 | 3.9136 | 0.65 | 32.1839 | 2.3596 |
| 603993.SH | 洛阳钼业 | copper | 20.17 | 0.699 | 12.3051 | 15.72 | -3.9066 | 19.2972 | 4.9932 | 0.8 | 17.8664 | 4.8559 |

## Recent Company Event Check
No recent announcement rows found in the short event window.

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| weak_rumor | unclassified | web_search | Bing News | 周三, 17 6月 | 中国太平洋保险官网可购买车险、人寿保险、养老保险、意外 ... | Web/search corroboration only; not filing or announcement grade. | https://www.cpic.com.cn/ |
| weak_rumor | unclassified | web_search | Bing News | 周二, 16 6月 | PICC中国人民保险集团官网-车险-财产保险-意外险-健康保险 ... | Web/search corroboration only; not filing or announcement grade. | https://e.picc.com.cn/ |
| weak_rumor | company_event | web_search | Bing News | 周三, 17 6月 | 平安集团官网_保险·车险·健康险·信用卡·投资理财一站式服务 | Contains rumor/possibility wording; use only as a watch item. | https://www.pingan.com/ |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 中国平安 大跌 原因: skipped low-signal result Plumeria - Wikipedia.
- web_search 中国平安 大跌 原因: skipped low-signal result Growing Plumeria: A Complete Care Guide - The Spruce.
- web_search 中国平安 大跌 原因: skipped low-signal result Plumeria Trees: Planting, Growing, and Pruning Plumerias.
- web_search 中国平安 下跌 传闻: skipped low-signal result Premier League Football News, Fixtures, Scores & Results.
- web_search 中国平安 下跌 传闻: skipped low-signal result Premier League Top Scorers 2026/27, Player Stats & Club Stat.
- web_search 中国平安 下跌 传闻: skipped low-signal result Premier League Table, Standings & Form Guide.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.