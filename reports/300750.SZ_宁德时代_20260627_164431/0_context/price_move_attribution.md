# Price-move attribution context for 300750.SZ as of 2026-06-27

- Status: ready
- Company: 宁德时代
- Basket: 电气设备
- Attribution label: commodity_equity_divergence + weak_trend_continuation
- Attribution reason: Mapped commodity futures did not move enough to explain the equity selloff. The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300750.SZ | 宁德时代 | 电气设备 | 381 | -5.2003 | -8.343 | -2.6323 | -17.1739 | 5.1544 | 2.704 | 1.15 | 22.3199 | 4.934 |

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
| SSE Composite | 20260626 | 4027.2648 | -2.2575 | -1.7413 | 0.8077 |
| CSI 300 | 20260626 | 4868.221 | -3.0255 | -0.9359 | 5.9332 |
| CSI 500 | 20260626 | 8703.565 | -2.623 | 1.6389 | 9.5456 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | raw material proxy | LC.GFE | 150220 | 20260626 | -15.90% | Verified by Tushare futures daily data. | -0.411 | -16.0125 | 3.0751 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300390.SZ | 天华新能 | lithium | 86.19 | -9.2546 | -0.2315 | 51.1575 | -24.8561 | 20.6402 | 5.2445 | 0.99 | 54.6809 | 5.8018 |
| 002466.SZ | 天齐锂业 | lithium | 58.92 | -8.849 | -8.4951 | 1.1155 | -27.8913 | 15.0178 | 4.0054 | 1.05 | 45.1771 | 2.1777 |
| 002460.SZ | 赣锋锂业 | lithium | 63.38 | -7.285 | -12.9396 | -22.7167 | -30.6944 | 8.9229 | 3.79 | 0.91 | 34.9147 | 2.8604 |
| 000630.SZ | 铜陵有色 | copper | 6.22 | -6.8862 | -7.8519 | 0.4847 | -21.5637 | 15.5709 | 5.2025 | 0.72 | 31.7159 | 2.2251 |
| 603799.SH | 华友钴业 | nickel_cobalt | 46.79 | -6.8114 | -16.297 | -23.4081 | -31.393 | 7.47 | 3.8715 | 0.84 | 12.0654 | 1.757 |
| 600362.SH | 江西铜业 | copper | 42.39 | -6.6916 | -2.4845 | -7.1209 | -22.7306 | 13.1789 | 5.9003 | 0.7 | 18.3589 | 1.7452 |
| 002340.SZ | 格林美 | nickel_cobalt | 6.69 | -6.1711 | -16.4794 | -16.6874 | -30.6017 | 4.0876 | 3.2782 | 0.96 | 21.4482 | 1.5644 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.65 | -5.5184 | 6.203 | 2.5408 | -16.1721 | 31.1404 | 5.1309 | 0.82 | 80.5097 | 2.4704 |
| 002155.SZ | 湖南黄金 | precious_metals | 24.24 | -5.4971 | -1.6234 | -24.4153 | -24.4153 | 11.6188 | 4.4416 | 0.73 | 21.6299 | 4.3478 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 34.78 | -5.4891 | -11.7707 | -19.2665 | -29.4094 | 7.6023 | 3.6738 | 0.86 | 38.9687 | 1.9414 |
| 000878.SZ | 云南铜业 | copper | 15.92 | -5.2381 | -10.158 | -15.9451 | -23.0174 | 5.2632 | 4.6676 | 0.66 | 28.576 | 2.0951 |
| 300750.SZ | 宁德时代 | 电气设备 | 381 | -5.2003 | -8.343 | -2.6323 | -17.1739 | 5.1544 | 2.704 | 1.15 | 22.3199 | 4.934 |
| 000807.SZ | 云铝股份 | aluminum | 22.48 | -4.7054 | -21.8631 | -35.328 | -38.6965 | 0 | 4.0134 | 0.86 | 8.9813 | 2.1867 |
| 600219.SH | 南山铝业 | aluminum | 4.09 | -4.662 | -21.0425 | -35.2848 | -35.9937 | 0 | 3.0034 | 0.98 | 11.3652 | 0.9218 |
| 000612.SZ | 焦作万方 | aluminum | 10.87 | -4.6491 | -8.0372 | -10.7553 | -21.2319 | 9.3001 | 4.4676 | 0.59 | 9.1232 | 1.6817 |
| 002532.SZ | 天山铝业 | aluminum | 11.08 | -4.6472 | -26.4276 | -40.8751 | -43.7278 | 0 | 3.8246 | 0.89 | 8.5784 | 1.6374 |
| 603993.SH | 洛阳钼业 | copper | 17.24 | -4.5932 | -8.2979 | -9.9269 | -20.3695 | 7.6236 | 5.55 | 0.68 | 15.271 | 4.1505 |
| 601600.SH | 中国铝业 | aluminum | 8.4 | -4.5455 | -25.6637 | -31.3164 | -34.375 | 0 | 4.1712 | 0.8 | 9.8256 | 1.7869 |
| 000792.SZ | 盐湖股份 | lithium | 28.91 | -4.3665 | -7.3397 | -22.3893 | -28.4406 | 7.5036 | 3.6216 | 0.73 | 14.8318 | 3.4227 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 42.58 | -4.1423 | 9.8272 | 27.2945 | -8.6266 | 30.7624 | 6.393 | 0.88 | 30.0141 | 3.3815 |
| 000975.SZ | 山金国际 | precious_metals | 17.31 | -4.0466 | -24.0789 | -45.7026 | -45.7026 | 0 | 3.5992 | 0.99 | 13.0711 | 2.9555 |
| 600595.SH | 中孚实业 | aluminum | 5.54 | -3.9861 | -21.6407 | -32.0245 | -37.4011 | 0 | 3.9154 | 0.76 | 10.0544 | 1.238 |
| 600547.SH | 山东黄金 | precious_metals | 23 | -3.8863 | -20.5801 | -45.8696 | -45.8696 | 0 | 3.2367 | 0.78 | 20.5527 | 3.3129 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.19 | -3.863 | -3.2282 | -15.5029 | -28.6255 | 12.3669 | 4.1753 | 0.74 | 28.5417 | 1.3998 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260625 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）在深圳证券交易所上市的公告 | https://static.cninfo.com.cn/finalpage/2026-06-25/1225387554.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260625 | 宁德时代新能源科技股份有限公司2026年面向专业投资者公开发行科技创新公司债券（第二期）在深圳证券交易所上市的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-25/1225387554.PDF |
| plausible | flow_or_sentiment | tushare_major_news | 新浪财经 | 2026-06-27 13:39:00 | 53家机构，“盯上”这家龙头公司 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| plausible | commodity_or_sector | tushare_major_news | 凤凰财经 | 2026-06-27 12:03:00 | 新能源赛道重大利好 2030年目标定了！机构扎堆盯上多只高成长潜力股 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| weak_rumor | commodity_or_sector | tushare_major_news | 新浪财经 | 2026-06-27 12:00:00 | 荣盛石化金塘新材料项目获重大技术突破、泉州金同旭能年产3万吨锂电新材料项目、恒申安科罗福州工厂投产运营 | Contains rumor/possibility wording; use only as a watch item. |  |
| weak_rumor | flow_or_sentiment | tushare_major_news | 新浪财经 | 2026-06-27 09:28:00 | 德方纳米定增29亿元扩产 欲破高端产能瓶颈 | Contains rumor/possibility wording; use only as a watch item. |  |
| weak_rumor | flow_or_sentiment | tushare_major_news | 新浪财经 | 2026-06-27 09:00:00 | 【月度前瞻】有色金属|碳酸锂：仓单注销月有压力，碳酸锂等待低多机会 | Contains rumor/possibility wording; use only as a watch item. |  |
| weak_rumor | macro_rate_fx | tushare_major_news | 同花顺 | 2026-06-27 08:23:39 | AI是“电老虎”？咨询巨头贝恩公司资深全球合伙人达沃斯论坛现场算账：全球电力需求增长中AI仅占约10% | Contains rumor/possibility wording; use only as a watch item. |  |
| weak_rumor | company_event | tushare_major_news | 同花顺 | 2026-06-27 08:13:13 | 全球出货量中国占85%！人形机器人加速“进厂打工”，价格却“打”下来了 | Contains rumor/possibility wording; use only as a watch item. |  |
| weak_rumor | company_event | tushare_major_news | 凤凰财经 | 2026-06-27 07:53:31 | 就在下周，超800亿元现金大红包在路上，17只滞涨股将大额派现 | Contains rumor/possibility wording; use only as a watch item. |  |
| plausible | commodity_or_sector | tushare_news_feed | sina | 2026-06-27 09:14:00 | 碳酸锂险些失守15万元／吨关口 拨开迷雾看宁德时代枧下窝锂矿：短期难复产 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| plausible | unclassified | tushare_news_feed | sina | 2026-06-27 08:36:00 | 首只新能源领域国家民企联合基金（宁德时代）启动 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| plausible | commodity_or_sector | tushare_news_feed | sina | 2026-06-26 21:00:00 | 国内期货夜盘开盘 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| plausible | company_event | tushare_news_feed | sina | 2026-06-26 20:47:00 | 宁德时代与中国节能签署深化战略合作协议 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| plausible | company_event | tushare_news_feed | eastmoney | 2026-06-26 19:37:00 | 湖南裕能：宁德时代减持触及1%整数倍 持股比例降至6.85% | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| weak_rumor | flow_or_sentiment | tushare_news_feed | sina | 2026-06-26 19:36:00 | 湖南裕能：宁德时代6月26日减持210.50万股 持股降至6.85% | Contains rumor/possibility wording; use only as a watch item. |  |
| plausible | company_event | tushare_news_feed | sina | 2026-06-26 19:19:00 | 宁德时代：成功发行10亿元5年期绿色科技创新债券 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| plausible | commodity_or_sector | tushare_news_feed | sina | 2026-06-26 17:52:00 | 机构：全球经济主要风险在于通胀持续和长期收益率不受控制上涨 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |

## News Probe Notes
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市（福建省辖地级市）_百度百科.
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市 - 维基百科，自由的百科全书.
- web_search 宁德时代 大跌 原因: skipped low-signal result 宁德市人民政府门户网站.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市（福建省辖地级市）_百度百科.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市 - 维基百科，自由的百科全书.
- web_search 宁德时代 下跌 传闻: skipped low-signal result 宁德市人民政府门户网站.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气工程（学科）_百度百科.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result “电气”中的“气”该如何理解？ - 知乎.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result 电气专业未来出路在哪？六大方向就业前景详解 - 知乎.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.