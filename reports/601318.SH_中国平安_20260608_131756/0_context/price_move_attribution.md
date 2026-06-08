# Price-move attribution context for 601318.SH as of 2026-06-08

- Status: ready
- Company: 中国平安
- Basket: 保险
- Attribution label: weak_trend_continuation
- Attribution reason: The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601318.SH | 中国平安 | 保险 | 53.48 | 0.4697 | -10.9557 | -10.4787 | -11.015 | 1.4484 | 1.1528 | 1.25 | 7.293 | 0.951 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | -1.2637 | 1.7334 |
| same_metal_equities | 保险 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -2.5101 | 2.9798 |
| mapped_commodity | mapped futures products | N/A | N/A |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260605 | 4027.7362 | -0.7404 | -3.6416 | 1.7863 |
| CSI 300 | 20260605 | 4816.9199 | -1.7906 | -1.1288 | 5.4719 |
| CSI 500 | 20260605 | 8251.1407 | -1.2637 | -5.0957 | 6.3286 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N/A | N/A | No mapped futures product | N/A | N/A | N/A | No commodity mapping; do not attribute the move to commodity prices without evidence. | N/A | N/A | N/A |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 38.9 | -7.0268 | -3.45 | 19.252 | -11.0857 | 19.7824 | 4.5665 | 1.02 | 27.4201 | 3.1518 |
| 002532.SZ | 天山铝业 | aluminum | 13.81 | -3.7631 | -17.1068 | -10.3829 | -29.8629 | 0 | 3.8321 | 0.94 | 10.6921 | 2.1185 |
| 000807.SZ | 云铝股份 | aluminum | 27.64 | -3.3566 | -12.3096 | -2.6075 | -24.625 | 0.3861 | 3.6731 | 0.92 | 11.0429 | 2.6886 |
| 000878.SZ | 云南铜业 | copper | 17.32 | -3.2402 | -15.5122 | -7.3797 | -16.2476 | 3.5281 | 3.1686 | 0.86 | 29.6387 | 2.3505 |
| 000933.SZ | 神火股份 | aluminum | 27.8 | -3.0683 | -10.3226 | -10.3515 | -21.4911 | 0 | 3.3268 | 0.87 | 11.1911 | 2.4901 |
| 000630.SZ | 铜陵有色 | copper | 6.49 | -2.9895 | -2.6987 | 8.8926 | -8.3333 | 15.7439 | 4.2236 | 0.6 | 33.1583 | 2.3216 |
| 603993.SH | 洛阳钼业 | copper | 18.19 | -2.9349 | -9.9505 | 3.6467 | -13.3397 | 6.2358 | 3.857 | 0.86 | 16.1125 | 4.703 |
| 600595.SH | 中孚实业 | aluminum | 6.95 | -2.7972 | -11.802 | -1.2784 | -21.4689 | 2.1429 | 3.3503 | 0.75 | 12.6134 | 1.6163 |
| 600988.SH | 赤峰黄金 | precious_metals | 31.36 | -2.6993 | -29.3694 | -14.6434 | -33.7838 | 0 | 3.0401 | 0.78 | 16.6138 | 4.3562 |
| 603799.SH | 华友钴业 | nickel_cobalt | 49.96 | -2.6121 | -24.303 | -12.9768 | -26.7449 | 0 | 2.0731 | 1.12 | 12.8829 | 1.912 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.2 | -2.571 | -22.1622 | -9.434 | -25.3112 | 0 | 1.955 | 0.97 | 23.0833 | 1.6839 |
| 000612.SZ | 焦作万方 | aluminum | 11.16 | -2.5328 | -15.6463 | -3.209 | -19.1304 | 0 | 2.895 | 0.93 | 9.3666 | 1.8179 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 36.12 | -2.5101 | -23.8457 | -14.5089 | -26.6897 | 0 | 2.508 | 1.11 | 40.4701 | 2.0355 |
| 601899.SH | 紫金矿业 | copper | 29.63 | -2.3401 | -14.8563 | -6.3823 | -16.9097 | 1.1671 | 2.6766 | 1.11 | 12.7717 | 3.9938 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.03 | -2.3301 | -22.0155 | -5.9813 | -25.3709 | 0 | 3.1858 | 0.81 | 71.675 | 2.209 |
| 600547.SH | 山东黄金 | precious_metals | 28.05 | -2.2989 | -23.1507 | -29.3273 | -33.9845 | 0 | 2.4046 | 0.88 | 25.0654 | 4.0403 |
| 601600.SH | 中国铝业 | aluminum | 10.68 | -2.0183 | -10.2521 | -7.3721 | -16.5625 | 3.6122 | 4.0893 | 0.71 | 12.4947 | 2.2719 |
| 600219.SH | 南山铝业 | aluminum | 4.89 | -2.004 | -12.0504 | -18.5 | -24.6533 | 0 | 3.3638 | 0.72 | 13.5882 | 1.1369 |
| 002460.SZ | 赣锋锂业 | lithium | 65.65 | -1.7068 | -22.5551 | -2.6398 | -28.2121 | 0 | 1.5918 | 1.3 | 36.1652 | 2.9628 |
| 002155.SZ | 湖南黄金 | precious_metals | 24.45 | -1.6888 | -19.8623 | -16.8367 | -23.7605 | 2.43 | 2.4418 | 0.85 | 21.8173 | 4.3855 |
| 000975.SZ | 山金国际 | precious_metals | 21.84 | -1.6659 | -25.2822 | -24.3767 | -31.4931 | 0 | 2.7798 | 0.88 | 16.4917 | 4.0898 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.26 | -1.632 | -22.6371 | -11.3636 | -28.2468 | 0.1486 | 2.2483 | 0.95 | 28.5686 | 1.4275 |
| 002466.SZ | 天齐锂业 | lithium | 59.06 | -0.6727 | -22.3406 | 17.8842 | -27.72 | 0 | 1.9671 | 1.22 | 45.2845 | 2.1829 |
| 000792.SZ | 盐湖股份 | lithium | 29.45 | 0.3407 | -22.6018 | -15.4222 | -27.104 | 0 | 1.764 | 1.21 | 15.0455 | 3.4867 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260602 | 中国平安H股公告 | https://static.cninfo.com.cn/finalpage/2026-06-02/1225343364.PDF |
| 20260602 | 中国平安2025年年度权益分派实施公告 | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342200.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260602 | 中国平安H股公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225343364.PDF |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260602 | 中国平安2025年年度权益分派实施公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-02/1225342200.PDF |
| weak_rumor | unclassified | web_search | Bing News | 周日, 07 6月 | 中国太平洋保险官网可购买车险、人寿保险、养老保险、意外 ... | Web/search corroboration only; not filing or announcement grade. | https://www.cpic.com.cn/ |
| weak_rumor | unclassified | web_search | Bing News | 周日, 07 6月 | PICC中国人民保险集团官网-车险-财产保险-意外险-健康保险 ... | Web/search corroboration only; not filing or announcement grade. | https://e.picc.com.cn/ |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 中国平安 大跌 原因: skipped low-signal result 中华人民共和国_百度百科.
- web_search 中国平安 大跌 原因: skipped low-signal result 中国政府网_中央人民政府门户网站.
- web_search 中国平安 大跌 原因: skipped low-signal result 中华人民共和国外交部.
- web_search 中国平安 下跌 传闻: skipped low-signal result 中华人民共和国_百度百科.
- web_search 中国平安 下跌 传闻: skipped low-signal result 中国政府网_中央人民政府门户网站.
- web_search 中国平安 下跌 传闻: skipped low-signal result 中华人民共和国外交部.
- web_search 保险 板块 大跌 原因: skipped low-signal result 保险（契约经济关系）_百度百科.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.