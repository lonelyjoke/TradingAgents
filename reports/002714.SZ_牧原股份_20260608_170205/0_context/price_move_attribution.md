# Price-move attribution context for 002714.SZ as of 2026-06-08

- Status: ready
- Company: 牧原股份
- Basket: 农业综合
- Attribution label: weak_trend_continuation
- Attribution reason: The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002714.SZ | 牧原股份 | 农业综合 | 34.15 | -2.5956 | -22.9468 | -30.9403 | -30.9403 | 0 | 1.6859 | N/A | 20.1563 | 2.3518 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | -2.1442 | -0.4514 |
| same_metal_equities | 农业综合 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -6.1574 | 3.5618 |
| mapped_commodity | mapped futures products | -1.0747 | -1.5209 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260608 | 3959.3378 | -1.6982 | -6.2883 | 0.0577 |
| CSI 300 | 20260608 | 4713.6358 | -2.1442 | -4.8104 | 3.2104 |
| CSI 500 | 20260608 | 7963.4529 | -3.4866 | -9.9131 | 2.6213 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Live hog futures | timely market-implied price signal | LH2607.DCE | 10235 | 20260605 | -2.97% | Verified by Tushare futures daily data. | -1.0747 | -9.8798 | 1.3229 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 35.01 | -10 | -15.2505 | 7.3268 | -19.9771 | 11.3656 | 5.0263 | N/A | 24.6781 | 2.8366 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 4.57 | -9.1451 | -29.1473 | -14.5794 | -32.1958 | 0 | 3.6316 | N/A | 65.1202 | 2.007 |
| 000630.SZ | 铜陵有色 | copper | 5.93 | -7.9193 | -13.8081 | -0.5034 | -16.2429 | 12.2837 | 4.5612 | N/A | 30.2972 | 2.1599 |
| 600362.SH | 江西铜业 | copper | 40.87 | -7.8674 | N/A | 0 | 0 | 0 | N/A | N/A | 17.7006 | 1.6826 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 8.24 | -7.83 | -19.2948 | 1.7284 | -24.2647 | 2.4055 | 4.793 | N/A | 34.5301 | 2.4666 |
| 000878.SZ | 云南铜业 | copper | 15.97 | -7.7945 | -21.5619 | -14.5989 | -22.7756 | 0.1735 | 3.5338 | N/A | 27.3286 | 2.1673 |
| 603993.SH | 洛阳钼业 | copper | 16.89 | -7.1468 | -15.5922 | -3.7607 | -19.5331 | 3.1179 | 4.1378 | N/A | 14.961 | 4.3669 |
| 000975.SZ | 山金国际 | precious_metals | 20.3 | -7.0513 | -27.7323 | -29.7091 | -36.3237 | 0 | 3.0083 | N/A | 15.3289 | 3.8014 |
| 600988.SH | 赤峰黄金 | precious_metals | 29.2 | -6.8878 | -30.5423 | -20.5226 | -38.3446 | 0 | 3.1571 | N/A | 15.4695 | 4.0562 |
| 000612.SZ | 焦作万方 | aluminum | 10.43 | -6.5412 | -20.5636 | -9.5403 | -24.4203 | 0 | 3.166 | N/A | 8.7539 | 1.699 |
| 603799.SH | 华友钴业 | nickel_cobalt | 46.72 | -6.4852 | -27.9457 | -18.6204 | -31.4956 | 0 | 2.369 | N/A | 12.0474 | 1.788 |
| 600595.SH | 中孚实业 | aluminum | 6.5 | -6.4748 | -15.8031 | -7.6705 | -26.5537 | 0 | 3.5908 | N/A | 11.7967 | 1.5116 |
| 600489.SH | 中金黄金 | precious_metals | 20.77 | -6.4414 | -23.2163 | -20.3604 | -26.8662 | 0 | 2.869 | N/A | 16.0428 | 3.0697 |
| 601600.SH | 中国铝业 | aluminum | 10.02 | -6.1798 | -14.9406 | -13.0963 | -21.7188 | 1.5209 | 4.2846 | N/A | 11.7225 | 2.1315 |
| 600219.SH | 南山铝业 | aluminum | 4.59 | -6.135 | -16.9982 | -23.5 | -29.2758 | 0 | 3.5851 | N/A | 12.7546 | 1.0672 |
| 002155.SZ | 湖南黄金 | precious_metals | 23.03 | -5.8078 | -22.7958 | -21.6667 | -28.1883 | 0.7002 | 2.653 | N/A | 20.5502 | 4.1308 |
| 600547.SH | 山东黄金 | precious_metals | 26.46 | -5.6684 | -25.212 | -33.3333 | -37.7265 | 0 | 2.5709 | N/A | 23.6446 | 3.8113 |
| 601899.SH | 紫金矿业 | copper | 28.05 | -5.3324 | -18.15 | -11.3744 | -21.3404 | 0 | 2.8623 | N/A | 12.0906 | 3.7809 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 34.2 | -5.3156 | -27.7261 | -19.0533 | -30.5866 | 0 | 2.6455 | N/A | 38.3189 | 1.9273 |
| 002237.SZ | 恒邦股份 | precious_metals | 12.6 | -4.9774 | -25.7951 | -15.7754 | -31.8182 | 0 | 2.3953 | N/A | 27.1467 | 1.3565 |
| 002340.SZ | 格林美 | nickel_cobalt | 6.85 | -4.8611 | -24.4763 | -13.8365 | -28.9419 | 0 | 2.1137 | N/A | 21.9612 | 1.602 |
| 002466.SZ | 天齐锂业 | lithium | 56.2 | -4.8425 | -27.362 | 12.1756 | -31.2202 | 0 | 1.9936 | N/A | 43.0916 | 2.0772 |
| 002532.SZ | 天山铝业 | aluminum | 13.16 | -4.7067 | -20.1941 | -14.6009 | -33.164 | 0 | 3.9275 | N/A | 10.1888 | 2.0188 |
| 000792.SZ | 盐湖股份 | lithium | 28.12 | -4.5161 | -25.0932 | -19.2418 | -30.396 | 0.3407 | 1.9088 | N/A | 14.366 | 3.3292 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260606 | 2026年5月份销售简报 | https://static.cninfo.com.cn/finalpage/2026-06-06/1225354982.PDF |
| 20260605 | H股公告（证券变动月报表） | https://static.cninfo.com.cn/finalpage/2026-06-05/1225352213.PDF |
| 20260602 | 章程修正案 | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342412.PDF |
| 20260602 | 公司章程（2026年6月） | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342411.PDF |
| 20260602 | 关于董事长辞任、选举董事长等事项的公告 | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342410.PDF |
| 20260602 | 关于聘任公司终身荣誉董事长暨关联交易的公告 | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342409.PDF |
| 20260602 | 关于召开2026年第二次临时股东会的通知 | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342408.PDF |
| 20260602 | 第五届董事会独立董事专门会议第五次会议决议 | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342407.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260606 | 2026年5月份销售简报 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-06/1225354982.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260605 | H股公告（证券变动月报表） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-05/1225352213.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260602 | 章程修正案 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342412.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260602 | 公司章程（2026年6月） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342411.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260602 | 关于董事长辞任、选举董事长等事项的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342410.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260602 | 关于聘任公司终身荣誉董事长暨关联交易的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342409.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260602 | 关于召开2026年第二次临时股东会的通知 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342408.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260602 | 第五届董事会独立董事专门会议第五次会议决议 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342407.PDF |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧（汉语文字）_百度百科.
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧的意思,牧的解释,牧的拼音,牧的部首,牧的笔顺-汉语国学.
- web_search 牧原股份 大跌 原因: skipped low-signal result 牧_牧怎么读_牧的意思 - 汉语字典.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧（汉语文字）_百度百科.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧的意思,牧的解释,牧的拼音,牧的部首,牧的笔顺-汉语国学.
- web_search 牧原股份 下跌 传闻: skipped low-signal result 牧_牧怎么读_牧的意思 - 汉语字典.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 中国农业银行.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 农业（通过人工培育获得产品的产业）_百度百科.
- web_search 农业综合 板块 大跌 原因: skipped low-signal result 国务院关于印发《加快农业农村现代化“十五五”规划》的通知 ....

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.