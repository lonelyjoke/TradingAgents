# Price-move attribution context for 300750.SZ as of 2026-06-28

- Status: ready
- Company: 宁德时代
- Basket: 电气设备
- Attribution label: commodity_equity_divergence + weak_trend_continuation
- Attribution reason: Mapped commodity futures did not move enough to explain the equity selloff. The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300750.SZ | 宁德时代 | 电气设备 | 381 | -5.2003 | -8.343 | -2.3052 | -17.1739 | 5.1544 | 2.704 | 1.15 | 22.3199 | 4.934 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | -2.623 | -2.5773 |
| same_metal_equities | 电气设备 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -4.6481 | -0.5522 |
| mapped_commodity | mapped futures products | -0.411 | -4.7893 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260626 | 4027.2648 | -2.2575 | -1.7413 | 1.5404 |
| CSI 300 | 20260626 | 4868.2205 | -3.0255 | -0.9359 | 6.6137 |
| CSI 500 | 20260626 | 8703.5652 | -2.623 | 1.6389 | 10.1908 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | raw material proxy | LC.GFE | 150220 | 20260626 | -18.31% | Verified by Tushare futures daily data. | -0.411 | -16.0125 | 3.0751 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300390.SZ | 天华新能 | lithium | 86.19 | -9.2546 | -0.2315 | 39.0161 | -24.8561 | 20.6402 | 5.2445 | 0.99 | 54.6809 | 5.8018 |
| 002466.SZ | 天齐锂业 | lithium | 58.92 | -8.849 | -8.4951 | 2.2029 | -27.8913 | 15.0178 | 4.0054 | 1.05 | 45.1771 | 2.1777 |
| 002460.SZ | 赣锋锂业 | lithium | 63.38 | -7.285 | -12.9396 | -21.7627 | -30.6944 | 8.9229 | 3.79 | 0.91 | 34.9147 | 2.8604 |
| 000630.SZ | 铜陵有色 | copper | 6.22 | -6.8862 | -7.8519 | 1.9672 | -21.5637 | 15.5709 | 5.2025 | 0.72 | 31.7159 | 2.2251 |
| 603799.SH | 华友钴业 | nickel_cobalt | 46.79 | -6.8114 | -16.297 | -21.3613 | -31.393 | 7.47 | 3.8715 | 0.84 | 12.0654 | 1.757 |
| 600362.SH | 江西铜业 | copper | 42.39 | -6.6916 | -2.4845 | -5.9046 | -22.7306 | 13.1789 | 5.9003 | 0.7 | 18.3589 | 1.7452 |
| 002340.SZ | 格林美 | nickel_cobalt | 6.69 | -6.1711 | -16.4794 | -15.7431 | -30.6017 | 4.0876 | 3.2782 | 0.96 | 21.4482 | 1.5644 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.65 | -5.5184 | 6.203 | 5.0186 | -16.1721 | 31.1404 | 5.1309 | 0.82 | 80.5097 | 2.4704 |
| 002155.SZ | 湖南黄金 | precious_metals | 24.24 | -5.4971 | -1.6234 | -21.882 | -22.6794 | 11.6188 | 4.4416 | 0.73 | 21.6299 | 4.3478 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 34.78 | -5.4891 | -11.7707 | -17.9136 | -29.4094 | 7.6023 | 3.6738 | 0.86 | 38.9687 | 1.9414 |
| 000878.SZ | 云南铜业 | copper | 15.92 | -5.2381 | -10.158 | -15.048 | -23.0174 | 5.2632 | 4.6676 | 0.66 | 28.576 | 2.0951 |
| 300750.SZ | 宁德时代 | 电气设备 | 381 | -5.2003 | -8.343 | -2.3052 | -17.1739 | 5.1544 | 2.704 | 1.15 | 22.3199 | 4.934 |
| 000807.SZ | 云铝股份 | aluminum | 22.48 | -4.7054 | -21.8631 | -36.7829 | -38.6965 | 0 | 4.0134 | 0.86 | 8.9813 | 2.1867 |
| 600219.SH | 南山铝业 | aluminum | 4.09 | -4.662 | -21.0425 | -35.2848 | -35.9937 | 0 | 3.0034 | 0.98 | 11.3652 | 0.9218 |
| 000612.SZ | 焦作万方 | aluminum | 10.87 | -4.6491 | -8.0372 | -13.1789 | -21.2319 | 9.3001 | 4.4676 | 0.59 | 9.1232 | 1.6817 |
| 002532.SZ | 天山铝业 | aluminum | 11.08 | -4.6472 | -26.4276 | -41.2825 | -43.7278 | 0 | 3.8246 | 0.89 | 8.5784 | 1.6374 |
| 603993.SH | 洛阳钼业 | copper | 17.24 | -4.5932 | -8.2979 | -9.8326 | -20.3695 | 7.6236 | 5.55 | 0.68 | 15.271 | 4.1505 |
| 601600.SH | 中国铝业 | aluminum | 8.4 | -4.5455 | -25.6637 | -34.2208 | -34.375 | 0 | 4.1712 | 0.8 | 9.8256 | 1.7869 |
| 000792.SZ | 盐湖股份 | lithium | 28.91 | -4.3665 | -7.3397 | -22.7005 | -28.4406 | 7.5036 | 3.6216 | 0.73 | 14.8318 | 3.4227 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 42.58 | -4.1423 | 9.8272 | 30.4534 | -8.6266 | 30.7624 | 6.393 | 0.88 | 30.0141 | 3.3815 |
| 000975.SZ | 山金国际 | precious_metals | 17.31 | -4.0466 | -24.0789 | -44.6434 | -44.6434 | 0 | 3.5992 | 0.99 | 13.0711 | 2.9555 |
| 600595.SH | 中孚实业 | aluminum | 5.54 | -3.9861 | -21.6407 | -33.8902 | -37.4011 | 0 | 3.9154 | 0.76 | 10.0544 | 1.238 |
| 600547.SH | 山东黄金 | precious_metals | 23 | -3.8863 | -20.5801 | -44.2694 | -44.2694 | 0 | 3.2367 | 0.78 | 20.5527 | 3.3129 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.19 | -3.863 | -3.2282 | -12.8798 | -28.6255 | 12.3669 | 4.1753 | 0.74 | 28.5417 | 1.3998 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260626 | 《期货和衍生品交易内部控制及风险管理制度》（2026年6月修订） | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392398.PDF |
| 20260626 | 关于制定及修订公司制度的公告 | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392396.PDF |
| 20260626 | 关于子公司开展期货和衍生品交易业务及可行性分析的公告 | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392394.PDF |
| 20260626 | 关于新增2026年度商品套期保值业务的公告 | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392393.PDF |
| 20260626 | 《董事、高级管理人员薪酬管理制度》（2026年6月制定） | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392397.PDF |
| 20260626 | 第四届董事会第十七次会议决议公告 | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392392.PDF |
| 20260626 | 关于2026年度第四期绿色科技创新债券发行完成的公告 | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392395.PDF |
| 20260625 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）在深圳证券交易所上市的公告 | https://static.cninfo.com.cn/finalpage/2026-06-25/1225387554.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | commodity_or_sector | official_announcement | CNINFO/Tushare announcement | 20260626 | 《期货和衍生品交易内部控制及风险管理制度》（2026年6月修订） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392398.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260626 | 关于制定及修订公司制度的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392396.PDF |
| confirmed | commodity_or_sector | official_announcement | CNINFO/Tushare announcement | 20260626 | 关于子公司开展期货和衍生品交易业务及可行性分析的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392394.PDF |
| confirmed | commodity_or_sector | official_announcement | CNINFO/Tushare announcement | 20260626 | 关于新增2026年度商品套期保值业务的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392393.PDF |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260626 | 《董事、高级管理人员薪酬管理制度》（2026年6月制定） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392397.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260626 | 第四届董事会第十七次会议决议公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392392.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260626 | 关于2026年度第四期绿色科技创新债券发行完成的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-26/1225392395.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260625 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）在深圳证券交易所上市的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-25/1225387554.PDF |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市（福建省辖地级市）_百度百科.
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市人民政府门户网站.
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市 - 维基百科，自由的百科全书.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市（福建省辖地级市）_百度百科.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市人民政府门户网站.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市 - 维基百科，自由的百科全书.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气工程（学科）_百度百科.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result “电气”中的“气”该如何理解？ - 知乎.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气专业未来出路在哪？六大方向就业前景详解 - 知乎.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.