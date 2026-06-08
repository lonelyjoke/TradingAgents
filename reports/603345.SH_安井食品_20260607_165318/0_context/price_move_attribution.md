# Price-move attribution context for 603345.SH as of 2026-06-07

- Status: ready
- Company: 安井食品
- Basket: 食品
- Attribution label: weak_trend_continuation
- Attribution reason: The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603345.SH | 安井食品 | 食品 | 86.68 | -0.2302 | -15.8447 | 2.7014 | -21.0708 | 0 | 2.1125 | 0.61 | 18.9083 | 1.7995 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | -1.2637 | 1.0335 |
| same_metal_equities | 食品 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -2.5214 | 2.2912 |
| mapped_commodity | mapped futures products | -1.1429 | 0.9127 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260605 | 4027.7362 | -0.7404 | -3.6416 | 0.5287 |
| CSI 300 | 20260605 | 4816.9199 | -1.7906 | -1.1288 | 5.0983 |
| CSI 500 | 20260605 | 8251.1407 | -1.2637 | -5.0957 | 4.7486 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Live hog futures | meat raw-material cost proxy | LH2607.DCE | 10235 | 20260605 | -2.57% | Verified by Tushare futures daily data. | -1.4918 | -8.7383 | 1.3244 |
| Soybean meal futures | feed and protein-chain cost proxy | M2607.DCE | 2749 | 20260605 | -2.14% | Verified by Tushare futures daily data. | -0.7939 | -2.7591 | 0.8862 |
| Corn futures | feed and starch/flour-chain cost proxy | C2607.DCE | 2323 | 20260605 | -1.69% | Verified by Tushare futures daily data. | 1 | -1.7759 | 0.5784 |
| Palm oil futures | edible-oil cost proxy for prepared dishes | P2606.DCE | 8967 | 20260605 | -6.09% | Verified by Tushare futures daily data. | -3.6635 | -5.1713 | 1.22 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 38.9 | -7.0268 | -3.45 | 18.6699 | -11.0857 | 19.7824 | 4.5665 | 1.02 | 27.4201 | 3.1518 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 8.94 | -4.6908 | -10.6893 | 9.4247 | -17.8309 | 7.4456 | 4.5488 | 0.97 | 37.4634 | 2.6762 |
| 002532.SZ | 天山铝业 | aluminum | 13.81 | -3.7631 | -17.1068 | -14.8057 | -29.8629 | 0 | 3.8321 | 0.94 | 10.6921 | 2.1185 |
| 600362.SH | 江西铜业 | copper | 44.36 | -3.6699 | -9.0238 | -2.8684 | -11.3863 | 6.696 | 3.6288 | 0.99 | 19.2121 | 1.8263 |
| 000807.SZ | 云铝股份 | aluminum | 27.64 | -3.3566 | -12.3096 | -5.0172 | -24.625 | 0.3861 | 3.6731 | 0.92 | 11.0429 | 2.6886 |
| 000878.SZ | 云南铜业 | copper | 17.32 | -3.2402 | -15.5122 | -8.9858 | -16.2476 | 3.5281 | 3.1686 | 0.86 | 29.6387 | 2.3505 |
| 000933.SZ | 神火股份 | aluminum | 27.8 | -3.0683 | -10.3226 | -12.4409 | -21.4911 | 0 | 3.3268 | 0.87 | 11.1911 | 2.4901 |
| 000630.SZ | 铜陵有色 | copper | 6.49 | -2.9895 | -2.6987 | 6.7434 | -8.3333 | 15.7439 | 4.2236 | 0.6 | 33.1583 | 2.3216 |
| 603993.SH | 洛阳钼业 | copper | 18.19 | -2.9349 | -9.9505 | 1.9048 | -13.3397 | 6.2358 | 3.857 | 0.86 | 16.1125 | 4.703 |
| 600595.SH | 中孚实业 | aluminum | 6.95 | -2.7972 | -11.802 | -3.7396 | -21.4689 | 2.1429 | 3.3503 | 0.75 | 12.6134 | 1.6163 |
| 600988.SH | 赤峰黄金 | precious_metals | 31.36 | -2.6993 | -29.3694 | -14.6434 | -33.7838 | 0 | 3.0401 | 0.78 | 16.6138 | 4.3562 |
| 603799.SH | 华友钴业 | nickel_cobalt | 49.96 | -2.6121 | -24.303 | -11.5909 | -26.7449 | 0 | 2.0731 | 1.12 | 12.8829 | 1.912 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.2 | -2.571 | -22.1622 | -8.7452 | -25.3112 | 0 | 1.955 | 0.97 | 23.0833 | 1.6839 |
| 000612.SZ | 焦作万方 | aluminum | 11.16 | -2.5328 | -15.6463 | -5.7432 | -19.1304 | 0 | 2.895 | 0.93 | 9.3666 | 1.8179 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 36.12 | -2.5101 | -23.8457 | -14.5897 | -26.6897 | 0 | 2.508 | 1.11 | 40.4701 | 2.0355 |
| 601899.SH | 紫金矿业 | copper | 29.63 | -2.3401 | -14.8563 | -8.323 | -16.9097 | 1.1671 | 2.6766 | 1.11 | 12.7717 | 3.9938 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.03 | -2.3301 | -22.0155 | -8.8768 | -25.3709 | 0 | 3.1858 | 0.81 | 71.675 | 2.209 |
| 600547.SH | 山东黄金 | precious_metals | 28.05 | -2.2989 | -23.1507 | -30.9963 | -33.9845 | 0 | 2.4046 | 0.88 | 25.0654 | 4.0403 |
| 601600.SH | 中国铝业 | aluminum | 10.68 | -2.0183 | -10.2521 | -9.721 | -16.5625 | 3.6122 | 4.0893 | 0.71 | 12.4947 | 2.2719 |
| 600219.SH | 南山铝业 | aluminum | 4.89 | -2.004 | -12.0504 | -19.9673 | -24.6533 | 0 | 3.3638 | 0.72 | 13.5882 | 1.1369 |
| 002460.SZ | 赣锋锂业 | lithium | 65.65 | -1.7068 | -22.5551 | 3.4836 | -28.2121 | 0 | 1.5918 | 1.3 | 36.1652 | 2.9628 |
| 002155.SZ | 湖南黄金 | precious_metals | 24.45 | -1.6888 | -19.8623 | -17.3986 | -23.7605 | 2.43 | 2.4418 | 0.85 | 21.8173 | 4.3855 |
| 000975.SZ | 山金国际 | precious_metals | 21.84 | -1.6659 | -25.2822 | -25.2055 | -31.4931 | 0 | 2.7798 | 0.88 | 16.4917 | 4.0898 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.26 | -1.632 | -22.6371 | -13.2767 | -28.2468 | 0.1486 | 2.2483 | 0.95 | 28.5686 | 1.4275 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260605 | H股公告（截至2026年5月31日止之股份发行人的证券变动月报表） | https://static.cninfo.com.cn/finalpage/2026-06-05/1225351345.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260605 | H股公告（截至2026年5月31日止之股份发行人的证券变动月报表） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-05/1225351345.PDF |
| weak_rumor | unclassified | web_search | Bing News | 周六, 06 6月 | 食品伙伴网（原食品伴侣网）—关注食品安全，探讨食品技术 ... | Web/search corroboration only; not filing or announcement grade. | https://www.foodmate.net/ |
| weak_rumor | unclassified | web_search | Bing News | 周六, 06 6月 | 中国食品新闻网 | Web/search corroboration only; not filing or announcement grade. | http://www.cfnews.com.cn/ |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 安井食品 大跌 原因: skipped low-signal result 安（汉字）_百度百科.
- web_search 安井食品 大跌 原因: skipped low-signal result 安 ān - 汉典.
- web_search 安井食品 大跌 原因: skipped low-signal result 安的意思,安的解释,安的拼音,安的部首,安的笔顺-汉语国学.
- web_search 安井食品 下跌 传闻: skipped low-signal result 安（汉字）_百度百科.
- web_search 安井食品 下跌 传闻: skipped low-signal result 安 ān - 汉典.
- web_search 安井食品 下跌 传闻: skipped low-signal result 安的意思,安的解释,安的拼音,安的部首,安的笔顺-汉语国学.
- web_search 食品 板块 大跌 原因: skipped low-signal result 食品_百度百科.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.