# Price-move attribution context for 002714.SZ as of 2026-06-24

- Status: ready
- Company: 牧原股份
- Basket: 农业综合
- Attribution label: cross_metal_underperformance + weak_trend_continuation
- Attribution reason: Target also underperformed the broader copper/precious/lithium/small-metal equity reference basket. The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002714.SZ | 牧原股份 | 农业综合 | 32.53 | -1.4839 | -15.9649 | -25.1323 | -29.9526 | 0 | 1.7247 | N/A | 19.2001 | 2.177 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 0.4804 | -1.9643 |
| same_metal_equities | 农业综合 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | 0.9735 | -2.4574 |
| mapped_commodity | mapped futures products | 0.4573 | -1.9412 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260624 | 4110.8134 | 0.1111 | -0.8337 | 5.672 |
| CSI 300 | 20260624 | 4943.0197 | 0.4804 | -0.0976 | 11.3138 |
| CSI 500 | 20260624 | 8842.9378 | 1.7764 | 2.1287 | 16.7984 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Live hog futures | timely market-implied price signal | LH2607.DCE | 9885 | 20260624 | -11.86% | Verified by Tushare futures daily data. | 0.4573 | -8.2599 | 0.9125 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600362.SH | 江西铜业 | copper | 47.33 | -4.1321 | 1.6975 | 10.4809 | -13.7258 | 22.9945 | 5.7521 | N/A | 20.4984 | 1.9485 |
| 000630.SZ | 铜陵有色 | copper | 6.94 | -2.8011 | 1.6105 | 19.244 | -12.4842 | 23.5294 | 5.1452 | N/A | 35.3872 | 2.4826 |
| 603993.SH | 洛阳钼业 | copper | 18.98 | -2.6167 | -6.9152 | 7.8409 | -12.3326 | 16.081 | 5.5092 | N/A | 16.8123 | 4.5694 |
| 600219.SH | 南山铝业 | aluminum | 4.38 | -1.573 | -22.8873 | -28.0788 | -31.4554 | 0 | 3.1193 | N/A | 12.171 | 0.9872 |
| 002714.SZ | 牧原股份 | 农业综合 | 32.53 | -1.4839 | -15.9649 | -25.1323 | -29.9526 | 0 | 1.7247 | N/A | 19.2001 | 2.177 |
| 000878.SZ | 云南铜业 | copper | 17.45 | -1.3009 | -6.3841 | -1.021 | -15.619 | 10.7769 | 4.5692 | N/A | 31.3223 | 2.2965 |
| 600489.SH | 中金黄金 | precious_metals | 19.88 | -0.7489 | -19.3836 | -24.2667 | -30 | 0 | 3.6365 | N/A | 15.3553 | 2.9382 |
| 002155.SZ | 湖南黄金 | precious_metals | 26.06 | -0.686 | 0.0768 | -10.6003 | -18.7403 | 14.1862 | 4.3709 | N/A | 23.254 | 4.6742 |
| 600547.SH | 山东黄金 | precious_metals | 24.76 | -0.4023 | -21.2969 | -37.6322 | -41.7275 | 0 | 3.2868 | N/A | 22.1255 | 3.5664 |
| 601899.SH | 紫金矿业 | copper | 27.65 | -0.3604 | -15.9574 | -14.6868 | -22.4621 | 1.5368 | 3.9041 | N/A | 11.9182 | 3.727 |
| 000975.SZ | 山金国际 | precious_metals | 19.12 | -0.1567 | -24.6354 | -34.8552 | -40.0251 | 0 | 3.6343 | N/A | 14.4378 | 3.2645 |
| 601600.SH | 中国铝业 | aluminum | 9.09 | 0 | -24.8139 | -20.1932 | -28.9844 | 0 | 4.1538 | N/A | 10.6327 | 1.9336 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.38 | 0 | -10.6538 | -4.2802 | -23.444 | 7.7372 | 2.9765 | N/A | 23.6604 | 1.7257 |
| 600988.SH | 赤峰黄金 | precious_metals | 28.19 | 0.7505 | -26.1462 | -35.4772 | -40.4772 | 0 | 4.4534 | N/A | 14.9344 | 3.7492 |
| 002532.SZ | 天山铝业 | aluminum | 11.89 | 0.7627 | -27.8081 | -34.885 | -39.614 | 0 | 3.877 | N/A | 9.2055 | 1.7571 |
| 600595.SH | 中孚实业 | aluminum | 5.98 | 1.1844 | -21.4192 | -23.2349 | -32.4294 | 0 | 3.9122 | N/A | 10.8529 | 1.3363 |
| 002237.SZ | 恒邦股份 | precious_metals | 14.16 | 1.2876 | -2.5465 | -3.4106 | -23.3766 | 14.4963 | 4.2034 | N/A | 30.6406 | 1.5027 |
| 000933.SZ | 神火股份 | aluminum | 23.3 | 1.3484 | -27.6173 | -27.142 | -34.1994 | 0 | 3.652 | N/A | 9.3796 | 1.9484 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 38.6 | 1.9276 | -8.4657 | -5.8307 | -21.6562 | 10.731 | 3.4816 | N/A | 43.2488 | 2.1546 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 6.16 | 2.1559 | 11.1913 | 18.0077 | -8.6053 | 32.2368 | 5.0677 | N/A | 87.7769 | 2.6934 |
| 603799.SH | 华友钴业 | nickel_cobalt | 52.33 | 2.5877 | -9.9312 | -9.5888 | -23.2698 | 9.1824 | 3.5758 | N/A | 13.494 | 1.9651 |
| 000807.SZ | 云铝股份 | aluminum | 24.64 | 2.967 | -22.2468 | -25.2427 | -32.8061 | 0 | 4.0498 | N/A | 9.8443 | 2.3968 |
| 000612.SZ | 焦作万方 | aluminum | 12 | 3.9861 | -3.9231 | 4.0763 | -13.0435 | 10.6424 | 4.2893 | N/A | 10.0716 | 1.8565 |
| 002460.SZ | 赣锋锂业 | lithium | 71.62 | 5.3235 | -4.5067 | -9.2958 | -21.684 | 8.3493 | 3.3391 | N/A | 39.454 | 3.2322 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260624 | 北京市康达律师事务所关于牧原食品集团股份有限公司2026年第二次临时股东会的法律意见书 | https://static.cninfo.com.cn/finalpage/2026-06-24/1225383964.PDF |
| 20260624 | 2026年第二次临时股东会决议公告 | https://static.cninfo.com.cn/finalpage/2026-06-24/1225383963.PDF |
| 20260618 | H股公告（变更公司名称） | https://static.cninfo.com.cn/finalpage/2026-06-18/1225376823.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260624 | 北京市康达律师事务所关于牧原食品集团股份有限公司2026年第二次临时股东会的法律意见书 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-24/1225383964.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260624 | 2026年第二次临时股东会决议公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-24/1225383963.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260618 | H股公告（变更公司名称） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-18/1225376823.PDF |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧（汉语文字）_百度百科.
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧的意思,牧的解释,牧的拼音,牧的部首,牧的笔顺-汉语国学.
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧字_百度百科.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧（汉语文字）_百度百科.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧的意思,牧的解释,牧的拼音,牧的部首,牧的笔顺-汉语国学.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧字_百度百科.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 中国农业银行.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 农业（通过人工培育获得产品的产业）_百度百科.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 中国农业农村信息网.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.