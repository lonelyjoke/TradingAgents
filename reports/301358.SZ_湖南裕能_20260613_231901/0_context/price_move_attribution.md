# Price-move attribution context for 301358.SZ as of 2026-06-13

- Status: ready
- Company: 湖南裕能
- Basket: 电气设备
- Attribution label: commodity_equity_divergence + weak_trend_continuation
- Attribution reason: Mapped commodity futures did not move enough to explain the equity selloff. The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 301358.SZ | 湖南裕能 | 电气设备 | 72.66 | 5.5031 | -23.9003 | -5.9661 | -33.8854 | 1.205 | 3.4019 | 1.4 | 24.1351 | 3.2702 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 1.1161 | 4.387 |
| same_metal_equities | 电气设备 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | 4.5477 | 0.9554 |
| mapped_commodity | mapped futures products | 0.4009 | 5.1022 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260612 | 4031.513 | 1.1161 | -2.5119 | 2.5351 |
| CSI 300 | 20260612 | 4777.321 | 1.1627 | -1.693 | 5.2861 |
| CSI 500 | 20260612 | 8106.203 | 0.8764 | -5.0389 | 4.3583 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | LFP cathode raw-material cost proxy | LC.GFE | 175300 | 20260612 | 5.07% | Verified by Tushare futures daily data. | 0.4009 | -7.1504 | 2.7075 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002532.SZ | 天山铝业 | aluminum | 13.43 | 0.1491 | -12.394 | -14.9462 | -31.7928 | 1.8997 | 3.5359 | 2.51 | 10.3979 | 2.0602 |
| 002460.SZ | 赣锋锂业 | lithium | 71.16 | 1.7444 | -8.8394 | 0.7504 | -22.187 | 11.4404 | 2.8651 | 1.21 | 39.2006 | 3.2115 |
| 000933.SZ | 神火股份 | aluminum | 27.31 | 2.0172 | -9.1786 | -7.4551 | -22.8749 | 1.981 | 3.217 | 1.48 | 10.9938 | 2.4463 |
| 300390.SZ | 天华新能 | lithium | 96.1 | 2.2014 | 2.6161 | 73.1532 | -16.2162 | 19.4335 | 4.009 | 1.34 | 58.366 | 6.4689 |
| 002466.SZ | 天齐锂业 | lithium | 62.5 | 2.459 | -9.5645 | 16.9098 | -23.51 | 8.5409 | 2.6972 | 1.41 | 47.9221 | 2.3101 |
| 000975.SZ | 山金国际 | precious_metals | 21.11 | 2.8752 | -15.8629 | -23.0405 | -33.7829 | 1.3333 | 2.9758 | 1.33 | 15.9405 | 3.9531 |
| 600547.SH | 山东黄金 | precious_metals | 27.79 | 3.1169 | -12.884 | -29.7523 | -34.5964 | 1.8519 | 2.77 | 1.58 | 24.8331 | 4.0028 |
| 000807.SZ | 云铝股份 | aluminum | 28.1 | 3.195 | -5.5462 | -1.0912 | -23.3706 | 2.1764 | 3.6065 | 1.52 | 11.2267 | 2.838 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.36 | 3.2258 | -13.0024 | -7.5377 | -23.6515 | 4.0876 | 2.2853 | 1.46 | 23.5963 | 1.7213 |
| 600219.SH | 南山铝业 | aluminum | 4.73 | 3.2751 | -9.387 | -21.9472 | -27.1186 | 0.4386 | 3.5517 | 1.51 | 13.1436 | 1.0997 |
| 002155.SZ | 湖南黄金 | precious_metals | 24.23 | 3.8577 | -7.9407 | -16.2461 | -24.4465 | 1.5231 | 2.7957 | 1.75 | 21.621 | 4.5932 |
| 600489.SH | 中金黄金 | precious_metals | 21.51 | 4.2151 | -11.6995 | -15.7132 | -24.2606 | 0.7812 | 2.9028 | 1.5 | 16.6144 | 3.1791 |
| 000792.SZ | 盐湖股份 | lithium | 31.7 | 4.242 | -6.4621 | -13.7884 | -21.5347 | 8.1437 | 2.7063 | 1.59 | 16.195 | 3.7531 |
| 600595.SH | 中孚实业 | aluminum | 6.9 | 4.5455 | -5.4795 | -2.8169 | -22.0339 | 2.1672 | 3.6725 | 1.61 | 12.5226 | 1.6047 |
| 601600.SH | 中国铝业 | aluminum | 10.8 | 4.5499 | -1.1894 | -6.1685 | -15.625 | 3.0938 | 4.2579 | 1.64 | 12.635 | 2.2974 |
| 301358.SZ | 湖南裕能 | 电气设备 | 72.66 | 5.5031 | -23.9003 | -5.9661 | -33.8854 | 1.205 | 3.4019 | 1.4 | 24.1351 | 3.2702 |
| 603799.SH | 华友钴业 | nickel_cobalt | 50.22 | 5.6596 | -14.3734 | -14.939 | -26.3636 | 1.7337 | 2.857 | 1.88 | 12.9499 | 1.9219 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.01 | 5.8584 | -14.5765 | -10.3377 | -29.5996 | 0.6552 | 2.6918 | 1.52 | 28.03 | 1.4006 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 37.1 | 6.3037 | -11.6667 | -11.3077 | -24.7006 | 2.0468 | 2.77 | 2.03 | 41.5681 | 2.0907 |
| 601899.SH | 紫金矿业 | copper | 29.09 | 6.4398 | -8.6369 | -12.485 | -18.424 | 0 | 3.135 | 1.67 | 12.5389 | 3.921 |
| 600362.SH | 江西铜业 | copper | 43.05 | 7.2496 | -7.1598 | -3.7774 | -14.0032 | 0 | 4.2091 | 1.77 | 18.6447 | 1.7723 |
| 000878.SZ | 云南铜业 | copper | 17.27 | 7.4005 | -6.497 | -7.3001 | -16.4894 | 0.7519 | 3.6856 | 2.19 | 29.5532 | 2.3437 |
| 600988.SH | 赤峰黄金 | precious_metals | 30.37 | 7.4664 | -19.3146 | -20.767 | -35.8742 | 0.3195 | 3.7218 | 1.92 | 16.0893 | 4.2187 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 37.65 | 8.0034 | 3.0942 | 17.5094 | -13.9429 | 2.62 | 5.2531 | 1.54 | 26.539 | 3.0505 |

## Recent Company Event Check
No recent announcement rows found in the short event window.

## News & Rumor Probe
No matching news / rumor probe rows found.

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 湖南裕能 大跌 原因: skipped low-signal result 湖南省_百度百科.
- web_search 湖南裕能 大跌 原因: skipped low-signal result 欢迎光临湖南省人民政府门户网站.
- web_search 湖南裕能 大跌 原因: skipped low-signal result 欢迎光临湖南省人民政府门户网站.
- web_search 湖南裕能 下跌 传闻: skipped low-signal result 湖南省_百度百科.
- web_search 湖南裕能 下跌 传闻: skipped low-signal result 欢迎光临湖南省人民政府门户网站.
- web_search 湖南裕能 下跌 传闻: skipped low-signal result 欢迎光临湖南省人民政府门户网站.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气工程（学科）_百度百科.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result “电气”中的“气”该如何理解？ - 知乎.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气工程 - 维基百科，自由的百科全书.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.