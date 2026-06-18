# Price-move attribution context for 300750.SZ as of 2026-06-16

- Status: ready
- Company: 宁德时代
- Basket: 电气设备
- Attribution label: mixed_or_unclassified
- Attribution reason: No single attribution bucket dominates; use the residual table and events for judgment.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300750.SZ | 宁德时代 | 电气设备 | 403.53 | 1.364 | -3.4432 | -2.293 | -12.2761 | 4.1601 | 2.117 | 1.1273 | 23.6397 | 5.2258 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | -0.1118 | 1.4758 |
| same_metal_equities | 电气设备 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -2.1205 | 3.4845 |
| mapped_commodity | mapped futures products | -2.5568 | 3.9208 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260616 | 4091.892 | -0.1118 | -1.8622 | 4.2975 |
| CSI 300 | 20260616 | 4884.232 | -0.1529 | 0.646 | 8.733 |
| CSI 500 | 20260616 | 8507.98 | 1.2042 | -1.3904 | 9.7277 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | raw material proxy | LC.GFE | 169980 | 20260616 | -4.27% | Verified by Tushare futures daily data. | -2.5568 | -7.82 | 2.5742 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002532.SZ | 天山铝业 | aluminum | 12.71 | -5.9911 | -16.6557 | -28.3136 | -35.4495 | 2.7356 | 3.608 | 1.4968 | 9.8404 | 1.8783 |
| 000933.SZ | 神火股份 | aluminum | 24.91 | -5.7867 | -16.3252 | -21.6667 | -29.6526 | 0.7238 | 3.3706 | 1.7071 | 10.0277 | 2.083 |
| 000807.SZ | 云铝股份 | aluminum | 25.38 | -5.6506 | -15.4282 | -19.3261 | -30.7881 | 0.9381 | 3.7559 | 1.6432 | 10.14 | 2.4688 |
| 601600.SH | 中国铝业 | aluminum | 10.07 | -5.6232 | -5.8879 | -15.873 | -21.3281 | 6.487 | 4.3507 | 1.4602 | 11.7791 | 2.1421 |
| 600595.SH | 中孚实业 | aluminum | 6.35 | -5.506 | -12.7747 | -15.894 | -28.2486 | 4.0248 | 3.8264 | 1.2126 | 11.5244 | 1.419 |
| 000612.SZ | 焦作万方 | aluminum | 11.03 | -4.8318 | -7.9299 | -10.4708 | -20.0725 | 11.1218 | 3.6655 | 1.2475 | 9.2575 | 1.7064 |
| 603993.SH | 洛阳钼业 | copper | 20.03 | -4.2543 | 10.176 | 14.9168 | -4.5736 | 24.598 | 5.0114 | 1.3031 | 17.7424 | 4.8222 |
| 300390.SZ | 天华新能 | lithium | 93.42 | -3.8097 | 5.1909 | 49.0665 | -18.5527 | 23.3583 | 3.9932 | 0.7698 | 59.2678 | 6.2885 |
| 601899.SH | 紫金矿业 | copper | 30.29 | -3.2577 | -2.792 | -7.5961 | -15.0589 | 14.5628 | 3.6682 | 0.7455 | 13.0561 | 4.0828 |
| 000792.SZ | 盐湖股份 | lithium | 31.15 | -2.7474 | -3.8877 | -20.2509 | -22.896 | 13.9047 | 2.7005 | 0.8604 | 15.981 | 3.6879 |
| 600219.SH | 南山铝业 | aluminum | 4.69 | -2.4948 | -11.1742 | -27.735 | -27.735 | 5.4825 | 3.5802 | 0.9179 | 13.0325 | 1.0571 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.26 | -2.4119 | -5.9034 | -2.952 | -21.9585 | 18.2018 | 4.5454 | 1.2392 | 74.9524 | 2.2999 |
| 000975.SZ | 山金国际 | precious_metals | 21.65 | -2.2573 | -9.9043 | -27.5193 | -32.0891 | 9.3827 | 3.2174 | 0.8985 | 16.3483 | 3.6965 |
| 000878.SZ | 云南铜业 | copper | 17.82 | -2.249 | -0.8899 | -3.0468 | -13.8298 | 14.2231 | 3.9146 | 0.9288 | 31.9865 | 2.3452 |
| 600988.SH | 赤峰黄金 | precious_metals | 31.98 | -1.992 | -11.8036 | -25.524 | -32.4747 | 15.8324 | 4.1593 | 0.6146 | 16.9423 | 4.2533 |
| 600362.SH | 江西铜业 | copper | 46.5 | -1.8159 | 5.3944 | 6.2129 | -7.1115 | 17.987 | 4.7387 | 1.288 | 20.1389 | 1.9144 |
| 600547.SH | 山东黄金 | precious_metals | 28.25 | -1.4306 | -8.4279 | -30.5726 | -33.5138 | 8.3144 | 2.876 | 0.8305 | 25.2441 | 4.0691 |
| 000630.SZ | 铜陵有色 | copper | 7.57 | -1.1749 | 25.7475 | 27.8716 | -1.1749 | 32.526 | 5.1091 | 1.301 | 38.5995 | 2.708 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 10.07 | -0.4941 | 1.4099 | 25.2488 | -7.4449 | 23.2643 | 5.4225 | 1.6149 | 42.1988 | 2.9526 |
| 600489.SH | 中金黄金 | precious_metals | 22.52 | -0.2657 | -4.4953 | -15.8131 | -20.7042 | 10.2539 | 3.1179 | 0.7435 | 17.3945 | 3.3284 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 38.71 | 0.0258 | -7.3036 | -9.0247 | -21.4329 | 13.1579 | 2.9656 | 1.0671 | 43.372 | 2.1608 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.65 | 0.0733 | -6.5708 | -8.9393 | -26.1364 | 11.7117 | 2.9188 | 0.9099 | 29.5371 | 1.4486 |
| 002460.SZ | 赣锋锂业 | lithium | 71.45 | 0.1823 | -6.0734 | -10.8546 | -21.8699 | 13.6393 | 2.6934 | 0.8045 | 39.3603 | 3.2246 |
| 002466.SZ | 天齐锂业 | lithium | 63.99 | 0.4237 | -3.8901 | 11.7925 | -21.6865 | 13.3808 | 2.6116 | 0.9256 | 49.0646 | 2.3651 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260616 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）发行公告 | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373026.PDF |
| 20260616 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）募集说明书 | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373024.PDF |
| 20260616 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行公司债券更名公告 | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373022.PDF |
| 20260616 | 宁德时代新能源科技股份有限公司主体长期信用评级报告 | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373020.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260616 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）发行公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373026.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260616 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）募集说明书 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373024.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260616 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行公司债券更名公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373022.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260616 | 宁德时代新能源科技股份有限公司主体长期信用评级报告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-16/1225373020.PDF |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市（福建省辖地级市）_百度百科.
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市人民政府门户网站.
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德旅游必去十大景点，福建宁德值得推荐的10个景点 ....
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市（福建省辖地级市）_百度百科.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市人民政府门户网站.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德旅游必去十大景点，福建宁德值得推荐的10个景点 ....
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气工程（学科）_百度百科.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result “电气”中的“气”该如何理解？ - 知乎.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气工程 - 维基百科，自由的百科全书.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.