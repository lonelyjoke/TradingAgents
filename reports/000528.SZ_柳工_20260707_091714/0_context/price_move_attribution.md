# Price-move attribution context for 000528.SZ as of 2026-07-07

- Status: ready
- Company: 柳工
- Basket: 工程机械
- Attribution label: mixed_or_unclassified
- Attribution reason: No single attribution bucket dominates; use the residual table and events for judgment.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000528.SZ | 柳工 | 工程机械 | 8.27 | 1.348 | -3.0481 | -13.7643 | -18.1188 | 8.0795 | 2.2706 | 0.85 | 10.8137 | 0.8855 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | -0.0595 | 1.4075 |
| same_metal_equities | 工程机械 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | 0.0739 | 1.2741 |
| mapped_commodity | mapped futures products | N/A | N/A |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260706 | 4041.2382 | -0.0595 | 0.3352 | -1.0017 |
| CSI 300 | 20260706 | 4841.998 | -0.0036 | 0.5206 | 1.7773 |
| CSI 500 | 20260706 | 8651.1339 | -1.0763 | 4.8477 | 4.356 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N/A | N/A | No mapped futures product | N/A | N/A | N/A | No commodity mapping; do not attribute the move to commodity prices without evidence. | N/A | N/A | N/A |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002155.SZ | 湖南黄金 | precious_metals | 24.22 | -6.5947 | -0.9407 | -20.3027 | -22.7432 | 12.8372 | 4.7359 | 1.38 | 21.6121 | 4.3442 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.28 | -6.2167 | 4.9702 | -10.3565 | -21.6617 | 23.4649 | 5.6794 | 0.74 | 75.2374 | 2.3086 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.3 | -3.1318 | 0.3017 | -21.3483 | -28.0303 | 12.4488 | 4.8618 | 0.92 | 28.7797 | 1.4115 |
| 600362.SH | 江西铜业 | copper | 41.94 | -3.0961 | -5.4554 | -10.1157 | -23.5509 | 7.8226 | 5.5537 | 0.99 | 18.164 | 1.7266 |
| 000630.SZ | 铜陵有色 | copper | 6.3 | -2.6275 | -2.9276 | -3.3742 | -20.5549 | 9.1062 | 5.0795 | 0.95 | 32.1238 | 2.2537 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 10.75 | -1.8265 | 20.2461 | 17.1024 | -16.0156 | 33.3739 | 5.405 | 0.74 | 45.0483 | 3.1519 |
| 300390.SZ | 天华新能 | lithium | 91.1 | -1.4922 | 13.1677 | 5.1842 | -20.5754 | 17.4648 | 5.3205 | 0.79 | 57.7959 | 6.1323 |
| 000878.SZ | 云南铜业 | copper | 15.98 | -1.175 | -7.7367 | -19.0066 | -22.7273 | 2.1478 | 4.3516 | 0.82 | 28.6837 | 2.103 |
| 603993.SH | 洛阳钼业 | copper | 18.31 | -1.1339 | 0.6597 | -9.5356 | -15.4273 | 10.3038 | 5.2783 | 0.93 | 16.2188 | 4.4081 |
| 600547.SH | 山东黄金 | precious_metals | 25.8 | -1.0736 | -8.0214 | -32.319 | -32.319 | 13.3913 | 3.9104 | 1.27 | 23.0548 | 3.7162 |
| 000792.SZ | 盐湖股份 | lithium | 29.25 | -0.544 | -0.6791 | -22.0208 | -27.599 | 4.5875 | 3.6806 | 0.98 | 15.0062 | 3.463 |
| 002460.SZ | 赣锋锂业 | lithium | 62.83 | -0.2223 | -4.2955 | -24.0358 | -31.2958 | 0.3346 | 3.8117 | 1.17 | 34.6118 | 2.8355 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 40.41 | -0.1729 | 3.8817 | 7.6165 | -13.2833 | 19.164 | 5.8097 | 0.76 | 28.4845 | 3.2091 |
| 603799.SH | 华友钴业 | nickel_cobalt | 46.91 | 0.3208 | -6.1049 | -28.6865 | -31.217 | 0.0856 | 3.8156 | 1.09 | 12.076 | 1.7586 |
| 600595.SH | 中孚实业 | aluminum | 5.93 | 0.3384 | -14.6763 | -30.5621 | -31.8391 | 6.6787 | 3.9995 | 0.94 | 10.7622 | 1.3251 |
| 002466.SZ | 天齐锂业 | lithium | 58.91 | 0.4262 | -0.254 | -11.8378 | -27.9036 | 4.3772 | 4.1124 | 0.88 | 45.1695 | 2.1774 |
| 600219.SH | 南山铝业 | aluminum | 4.19 | 0.4796 | -14.3149 | -32.5282 | -32.5282 | 4.5113 | 2.984 | 0.86 | 11.6431 | 0.9444 |
| 600988.SH | 赤峰黄金 | precious_metals | 31.6 | 1.1848 | 0.7653 | -28.5714 | -28.8288 | 20.9996 | 5.4896 | 2.77 | 16.7409 | 4.2027 |
| 600489.SH | 中金黄金 | precious_metals | 20.6 | 1.2783 | -7.2072 | -23.8447 | -27.0021 | 13.2517 | 4.1756 | 1.28 | 15.9115 | 3.0446 |
| 000528.SZ | 柳工 | 工程机械 | 8.27 | 1.348 | -3.0481 | -13.7643 | -18.1188 | 8.0795 | 2.2706 | 0.85 | 10.8137 | 0.8855 |
| 601899.SH | 紫金矿业 | copper | 28.28 | 1.6535 | -4.5562 | -18.7823 | -20.6955 | 10.8367 | 4.3656 | 0.92 | 12.1898 | 3.8119 |
| 601600.SH | 中国铝业 | aluminum | 8.48 | 1.8007 | -20.5993 | -31.1129 | -31.1129 | 1.9584 | 3.6545 | 1.1 | 9.9192 | 1.8039 |
| 000975.SZ | 山金国际 | precious_metals | 20.21 | 1.8649 | N/A | 0 | 0 | 0 | N/A | 2.14 | 15.2609 | 3.4506 |
| 000807.SZ | 云铝股份 | aluminum | 22.88 | 2.0517 | -17.2214 | -34.889 | -34.889 | 2.9858 | 3.8754 | 1.18 | 9.1411 | 2.2256 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260704 | 关于全资子公司中恒国际租赁有限公司3号第1期绿色资产支持专项计划发行完成的公告 | https://static.cninfo.com.cn/finalpage/2026-07-04/1225409037.PDF |
| 20260703 | 关于2026年第二季度可转换公司债券转股情况的公告 | https://static.cninfo.com.cn/finalpage/2026-07-03/1225404889.PDF |
| 20260701 | 关于修订《公司章程》的公告 | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400891.PDF |
| 20260701 | 关于公司调整财务负责人暨新聘副总裁的公告 | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400890.PDF |
| 20260701 | 关于召开2026年第三次临时股东会的通知 | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400889.PDF |
| 20260701 | 第十届董事会第十四次（临时）会议决议公告 | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400888.PDF |
| 20260701 | 关于回购股份并注销的公告 | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400887.PDF |
| 20260630 | 华泰联合证券有限责任公司关于广西柳工机械股份有限公司向不特定对象发行可转换公司债券受托管理事务报告（2025年度） | https://static.cninfo.com.cn/finalpage/2026-06-30/1225394802.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260704 | 关于全资子公司中恒国际租赁有限公司3号第1期绿色资产支持专项计划发行完成的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-04/1225409037.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260703 | 关于2026年第二季度可转换公司债券转股情况的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-03/1225404889.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260701 | 关于修订《公司章程》的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400891.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260701 | 关于公司调整财务负责人暨新聘副总裁的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400890.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260701 | 关于召开2026年第三次临时股东会的通知 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400889.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260701 | 第十届董事会第十四次（临时）会议决议公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400888.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260701 | 关于回购股份并注销的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-01/1225400887.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260630 | 华泰联合证券有限责任公司关于广西柳工机械股份有限公司向不特定对象发行可转换公司债券受托管理事务报告（2025年度） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-30/1225394802.PDF |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 柳工 大跌 原因: skipped low-signal result 柳（汉语文字）_百度百科.
- web_search 柳工 大跌 原因: skipped low-signal result 柳的意思,柳的解释,柳的拼音,柳的部首,柳的笔顺-汉语国学.
- web_search 柳工 大跌 原因: skipped low-signal result 柳树（金虎尾目杨柳科下的一属植物）_百度百科.
- web_search 柳工 下跌 传闻: skipped low-signal result 柳（汉语文字）_百度百科.
- web_search 柳工 下跌 传闻: skipped low-signal result 柳的意思,柳的解释,柳的拼音,柳的部首,柳的笔顺-汉语国学.
- web_search 柳工 下跌 传闻: skipped low-signal result 柳树（金虎尾目杨柳科下的一属植物）_百度百科.
- web_search 工程机械 板块 大跌 原因: skipped low-signal result 工程（汉语词语）_百度百科.
- web_search 工程机械 板块 大跌 原因: skipped low-signal result 什么是工程，什么又是工程思想？ - 知乎.
- web_search 工程机械 板块 大跌 原因: skipped low-signal result 中国工程科学 - CAE.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.