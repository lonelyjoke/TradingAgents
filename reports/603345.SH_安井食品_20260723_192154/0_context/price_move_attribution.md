# Price-move attribution context for 603345.SH as of 2026-07-23

- Status: ready
- Company: 安井食品
- Basket: 食品
- Attribution label: cross_metal_underperformance
- Attribution reason: Target also underperformed the broader copper/precious/lithium/small-metal equity reference basket.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603345.SH | 安井食品 | 食品 | 87.12 | -0.6613 | 5.1539 | -20.4093 | -20.4093 | 11.1393 | 2.7842 | 0.56 | 19.0043 | 1.8086 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 0.228 | -0.8893 |
| same_metal_equities | 食品 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | 3.7249 | -4.3862 |
| mapped_commodity | mapped futures products | 0.6302 | -1.2915 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260723 | 3876.7774 | 0.252 | -5.6932 | -6.8121 |
| CSI 300 | 20260723 | 4728.0018 | 0.228 | -4.3499 | -3.057 |
| CSI 500 | 20260723 | 7734.31 | -0.2238 | -12.5369 | -9.9451 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Live hog futures | meat raw-material cost proxy | LH2607.DCE | 10000 | 20260723 | -6.59% | Verified by Tushare futures daily data. | 0 | 1.626 | 2.6978 |
| Soybean meal futures | feed and protein-chain cost proxy | M2608.DCE | 3153 | 20260723 | 5.91% | Verified by Tushare futures daily data. | 0.8637 | 8.0535 | 0.7569 |
| Corn futures | feed and starch/flour-chain cost proxy | C2609.DCE | 2278 | 20260723 | -2.65% | Verified by Tushare futures daily data. | 0.3967 | -2.1057 | 0.5218 |
| Palm oil futures | edible-oil cost proxy for prepared dishes | P2608.DCE | 9332 | 20260723 | -2.72% | Verified by Tushare futures daily data. | 2.7753 | 1.1928 | 1.1412 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603345.SH | 安井食品 | 食品 | 87.12 | -0.6613 | 5.1539 | -20.4093 | -20.4093 | 11.1393 | 2.7842 | 0.56 | 19.0043 | 1.8086 |
| 600547.SH | 山东黄金 | precious_metals | 27.42 | 0.073 | 14.5842 | -23.0856 | -24.8767 | 19.1304 | 3.7388 | 1.2 | 24.5024 | 3.9495 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.24 | 0.9146 | -3.4985 | -22.346 | -22.7538 | 7.4529 | 3.4963 | 1.03 | 28.6499 | 1.4051 |
| 000975.SZ | 山金国际 | precious_metals | 22.81 | 1.2877 | 26.4412 | -17.2951 | -21.9637 | 34.2074 | 4.4868 | 1.97 | 17.2242 | 3.8945 |
| 002155.SZ | 湖南黄金 | precious_metals | 23.34 | 1.4342 | -9.0058 | -22.8685 | -23.5005 | 10.8382 | 4.1225 | 1.14 | 20.8268 | 4.1864 |
| 600489.SH | 中金黄金 | precious_metals | 22.45 | 1.5378 | 18.846 | -16.9749 | -20.4465 | 23.1069 | 3.5888 | 1.06 | 17.3404 | 3.318 |
| 600988.SH | 赤峰黄金 | precious_metals | 38.83 | 1.596 | 45.8678 | -5.5461 | -12.545 | 48.0821 | 5.2318 | 1.36 | 20.5712 | 5.1643 |
| 603993.SH | 洛阳钼业 | copper | 20.03 | 2.1418 | 10.8467 | 2.8234 | -7.4827 | 16.7957 | 3.4812 | 1.19 | 17.7424 | 4.8222 |
| 000878.SZ | 云南铜业 | copper | 16 | 2.2364 | -4.7619 | -19.96 | -22.6306 | 9.6706 | 3.2322 | 1.2 | 28.7196 | 2.1056 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 9.4 | 2.5082 | -23.6393 | 0.4274 | -26.5625 | 11.6931 | 4.7537 | 0.8 | 39.3911 | 2.7561 |
| 601899.SH | 紫金矿业 | copper | 33.06 | 2.6708 | 27.5463 | -3.3616 | -5 | 28.2869 | 3.0891 | 1.29 | 14.2501 | 4.4562 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 32.83 | 2.9154 | -26.0919 | -14.6386 | -29.5494 | 9.622 | 4.6121 | 0.89 | 23.1414 | 2.6072 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 33.65 | 3.0944 | -8.5598 | -31.7029 | -31.7029 | 4.1481 | 3.3111 | 1.28 | 37.7026 | 1.8783 |
| 000630.SZ | 铜陵有色 | copper | 6.3 | 3.2787 | -5.6886 | -3.0769 | -20.5549 | 6.087 | 3.2052 | 1.45 | 32.1238 | 2.2537 |
| 601600.SH | 中国铝业 | aluminum | 9.78 | 3.7116 | 11.1364 | -19.4399 | -19.4399 | 16.4198 | 3.7525 | 1.21 | 11.4398 | 2.0804 |
| 002340.SZ | 格林美 | nickel_cobalt | 6.66 | 3.7383 | -6.5919 | -28.7701 | -28.7701 | 1.9048 | 2.3916 | 1.31 | 21.3521 | 1.5574 |
| 000612.SZ | 焦作万方 | aluminum | 11.04 | 3.7594 | -3.1579 | -19.3572 | -19.3572 | 8.5714 | 2.7629 | 1.27 | 9.2658 | 1.708 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 4.53 | 4.1379 | -24.2475 | -28.6614 | -29.7674 | 2.5943 | 4.4759 | 1.25 | 64.5503 | 1.9807 |
| 603799.SH | 华友钴业 | nickel_cobalt | 41.55 | 4.397 | -17.2476 | -38.8701 | -39.0762 | 9.9144 | 3.8914 | 1.25 | 10.6962 | 1.5576 |
| 600362.SH | 江西铜业 | copper | 45.06 | 4.669 | -0.8144 | -3.9847 | -17.8637 | 11.4707 | 4.7984 | 1.44 | 19.5152 | 1.8551 |
| 000792.SZ | 盐湖股份 | lithium | 27.58 | 4.9467 | -8.7661 | -31.7327 | -31.7327 | 7.3529 | 3.0449 | 1.27 | 14.1495 | 3.2653 |
| 000933.SZ | 神火股份 | aluminum | 26.26 | 5.04 | 18.1818 | -19.6696 | -19.6696 | 18.4273 | 3.9727 | 1.16 | 10.5712 | 2.1959 |
| 000807.SZ | 云铝股份 | aluminum | 26.87 | 5.043 | 13.9042 | -17.7281 | -17.7281 | 17.5011 | 3.6063 | 1.21 | 10.7352 | 2.6137 |
| 002466.SZ | 天齐锂业 | lithium | 46.38 | 5.6011 | -28.2488 | -43.2383 | -43.2383 | 3.8543 | 4.7954 | 1.09 | 35.562 | 1.7143 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260722 | 安井食品关于全资子公司变更注册地址并换发营业执照的公告 | http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603345&announcementId=1225434562&orgId=9900028960&announcementTime=2026-07-22 |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260722 | 安井食品关于全资子公司变更注册地址并换发营业执照的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603345&announcementId=1225434562&orgId=9900028960&announcementTime=2026-07-22 |
| plausible | unclassified | tushare_major_news | 新浪财经 | 2026-07-22 20:50:00 | 洽洽食品上半年净利润预增近两倍？ 创始人之女陈奇这回证明了自己 | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| plausible | company_event | tushare_news_feed | sina | 20260716 |  | News topic is directionally relevant; reconcile with residual table before treating it as a cause. |  |
| weak_rumor | unclassified | web_search | Bing News | 周四, 23 7月 | 食品伙伴网（原食品伴侣网）—关注食品安全，探讨食品技术 ... | Web/search corroboration only; not filing or announcement grade. | https://www.foodmate.net/ |
| weak_rumor | unclassified | web_search | Bing News | 周二, 21 7月 | 食品标准_食品伙伴网下载中心 | Web/search corroboration only; not filing or announcement grade. | http://down.foodmate.net/standard/index.html |

## News Probe Notes
- web_search 安井食品 大跌 原因: skipped low-signal result 0xk1h0/ChatGPT_DAN: ChatGPT DAN, Jailbreaks prompt - GitHub.
- web_search 安井食品 大跌 原因: skipped low-signal result Download GitHub Desktop.
- web_search 安井食品 大跌 原因: skipped low-signal result Orangetheory Fitness - Reddit.
- web_search 安井食品 下跌 传闻: skipped low-signal result XNXX Adult Forum.
- web_search 安井食品 下跌 传闻: skipped low-signal result c# - Format a Social Security Number (SSN) as XXX-XX-XXXX fr.
- web_search 安井食品 下跌 传闻: skipped low-signal result Pic & Movie Post - XNXX Adult Forum.
- web_search 食品 板块 大跌 原因: skipped low-signal result 食品_百度百科.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.