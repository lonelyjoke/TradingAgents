# Price-move attribution context for 002714.SZ as of 2026-06-17

- Status: ready
- Company: 牧原股份
- Basket: 农业综合
- Attribution label: weak_trend_continuation
- Attribution reason: The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002714.SZ | 牧原股份 | 农业综合 | 34.66 | -1.1127 | -12.3419 | -19.8242 | -25.3661 | 2.6354 | 1.582 | 0.83 | 20.6875 | 2.3457 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 0.9654 | -2.0781 |
| same_metal_equities | 农业综合 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -0.4401 | -0.6726 |
| mapped_commodity | mapped futures products | -0.8342 | -0.2785 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260617 | 4108.0762 | 0.3955 | -1.3 | 4.7101 |
| CSI 300 | 20260617 | 4931.3861 | 0.9654 | 1.6634 | 9.7827 |
| CSI 500 | 20260617 | 8627.0862 | 1.3999 | -0.3376 | 11.2638 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Live hog futures | timely market-implied price signal | LH2607.DCE | 10105 | 20260617 | -10.38% | Verified by Tushare futures daily data. | -0.8342 | -6.6081 | 1.1558 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.11 | -2.8517 | -6.7518 | -5.7196 | -24.184 | 15.3509 | 4.5676 | 1.24 | 74.9524 | 2.2999 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.42 | -2.7523 | -11.5614 | -8.0545 | -23.029 | 11.3869 | 2.482 | 1.18 | 24.4619 | 1.7842 |
| 300390.SZ | 天华新能 | lithium | 91.75 | -1.7876 | -0.7572 | 46.4018 | -20.0087 | 18.6587 | 3.9169 | 0.77 | 59.2678 | 6.2885 |
| 600595.SH | 中孚实业 | aluminum | 6.24 | -1.7323 | -14.7541 | -17.351 | -29.4915 | 0 | 3.824 | 1.21 | 11.5244 | 1.419 |
| 000807.SZ | 云铝股份 | aluminum | 25 | -1.4972 | -17.9251 | -20.534 | -31.8244 | 0 | 3.7203 | 1.64 | 10.14 | 2.4688 |
| 000933.SZ | 神火股份 | aluminum | 24.55 | -1.4452 | -18.4385 | -22.7987 | -30.6693 | 0 | 3.3414 | 1.71 | 10.0277 | 2.083 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 38.19 | -1.3433 | -8.8762 | -10.2468 | -22.4883 | 13.1871 | 2.9691 | 1.07 | 43.372 | 2.1608 |
| 600219.SH | 南山铝业 | aluminum | 4.63 | -1.2793 | -10.9615 | -28.6595 | -28.6595 | 2.8509 | 3.5772 | 0.92 | 13.0325 | 1.0571 |
| 002532.SZ | 天山铝业 | aluminum | 12.55 | -1.2589 | -19.2926 | -29.216 | -36.2621 | 0 | 3.5473 | 1.5 | 9.8404 | 1.8783 |
| 002714.SZ | 牧原股份 | 农业综合 | 34.66 | -1.1127 | -12.3419 | -19.8242 | -25.3661 | 2.6354 | 1.582 | 0.83 | 20.6875 | 2.3457 |
| 601600.SH | 中国铝业 | aluminum | 9.97 | -0.993 | -9.3636 | -16.7084 | -22.1094 | 0.499 | 4.2946 | 1.46 | 11.7791 | 2.1421 |
| 000792.SZ | 盐湖股份 | lithium | 30.87 | -0.8989 | -6.056 | -20.9677 | -23.5891 | 10.7752 | 2.6797 | 0.86 | 15.981 | 3.6879 |
| 603799.SH | 华友钴业 | nickel_cobalt | 52.59 | -0.7736 | -9.4681 | -11.9833 | -22.8886 | 13.4418 | 3.0837 | 1.03 | 13.6668 | 1.9902 |
| 000612.SZ | 焦作万方 | aluminum | 10.97 | -0.544 | -10.3758 | -10.9578 | -20.5072 | 5.7526 | 3.6172 | 1.25 | 9.2575 | 1.7064 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 41.43 | -0.5043 | 13.6314 | 27.5554 | -5.3029 | 22.5787 | 5.5769 | 1.26 | 29.3515 | 3.3068 |
| 002155.SZ | 湖南黄金 | precious_metals | 26.5 | -0.3759 | 3.8808 | -12.8289 | -17.3683 | 15.7528 | 3.2035 | 1.54 | 23.7358 | 4.7711 |
| 002460.SZ | 赣锋锂业 | lithium | 71.32 | -0.1819 | -7.5807 | -11.0168 | -22.012 | 13.8464 | 2.663 | 0.8 | 39.3603 | 3.2246 |
| 000630.SZ | 铜陵有色 | copper | 7.56 | -0.1321 | 27.7027 | 27.7027 | -1.3055 | 30.9689 | 5.0742 | 1.3 | 38.5995 | 2.708 |
| 600547.SH | 山东黄金 | precious_metals | 28.26 | 0.0354 | -7.1921 | -30.548 | -33.4902 | 6.7649 | 2.8696 | 0.83 | 25.2441 | 4.0691 |
| 002466.SZ | 天齐锂业 | lithium | 64.04 | 0.0781 | -6.0446 | 11.8798 | -21.6253 | 13.8612 | 2.5437 | 0.93 | 49.0646 | 2.3651 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 10.1 | 0.2979 | 1.3039 | 25.6219 | -7.1691 | 22.6553 | 5.4224 | 1.61 | 42.1988 | 2.9526 |
| 601899.SH | 紫金矿业 | copper | 30.43 | 0.4622 | 0.1316 | -7.169 | -14.6663 | 10.8306 | 3.6259 | 0.75 | 13.0561 | 4.0828 |
| 000878.SZ | 云南铜业 | copper | 17.93 | 0.6173 | 0.3358 | -2.4483 | -13.2979 | 11.6541 | 3.9136 | 0.93 | 31.9865 | 2.3452 |
| 603993.SH | 洛阳钼业 | copper | 20.17 | 0.699 | 12.3051 | 15.72 | -3.9066 | 19.2972 | 4.9932 | 1.3 | 17.7424 | 4.8222 |

## Recent Company Event Check
No recent announcement rows found in the short event window.

## News & Rumor Probe
No matching news / rumor probe rows found.

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧（汉语文字）_百度百科.
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧的意思,牧的解释,牧的拼音,牧的部首,牧的笔顺-汉语国学.
- web_search 牧原股份 大跌 原因: skipped low-signal result 凉州牧_百度百科.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧（汉语文字）_百度百科.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧的意思,牧的解释,牧的拼音,牧的部首,牧的笔顺-汉语国学.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 凉州牧_百度百科.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 中国农业银行.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 农业（通过人工培育获得产品的产业）_百度百科.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 中国农业农村信息网.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.