# Price-move attribution context for 601166.SH as of 2026-06-22

- Status: ready
- Company: 兴业银行
- Basket: 银行
- Attribution label: mixed_or_unclassified
- Attribution reason: No single attribution bucket dominates; use the residual table and events for judgment.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601166.SH | 兴业银行 | 银行 | 17.32 | -2.9148 | -0.2879 | -7.3301 | -8.3113 | 2.9429 | 1.4477 | 1.12 | 4.7293 | 0.4416 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 0.2071 | -3.1219 |
| same_metal_equities | 银行 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -2.2958 | -0.619 |
| mapped_commodity | mapped futures products | N/A | N/A |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260618 | 4090.4813 | -0.4283 | 0.3239 | 5.4221 |
| CSI 300 | 20260618 | 4941.5986 | 0.2071 | 3.3138 | 11.2775 |
| CSI 500 | 20260618 | 8673.0899 | 0.5332 | 3.0078 | 15.105 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N/A | N/A | No mapped futures product | N/A | N/A | N/A | No commodity mapping; do not attribute the move to commodity prices without evidence. | N/A | N/A | N/A |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601600.SH | 中国铝业 | aluminum | 9.38 | -5.9178 | -13.4686 | -16.3247 | -26.7188 | 0 | 4.4647 | 1.31 | 10.972 | 1.9953 |
| 600988.SH | 赤峰黄金 | precious_metals | 30.59 | -5.8769 | -11.3333 | -32.3978 | -35.4096 | 15.371 | 4.3108 | 1 | 16.2059 | 4.0684 |
| 600547.SH | 山东黄金 | precious_metals | 26.91 | -4.7771 | -9.0878 | -33.043 | -36.6675 | 6.8027 | 2.9909 | 1.03 | 24.0467 | 3.8761 |
| 002532.SZ | 天山铝业 | aluminum | 12.05 | -3.9841 | -21.7532 | -30.3065 | -38.8014 | 0 | 3.6092 | 0.8 | 9.3294 | 1.7808 |
| 000975.SZ | 山金国际 | precious_metals | 21.07 | -3.702 | -9.8417 | -29.7667 | -33.9084 | 8.0494 | 3.3066 | 0.89 | 15.9103 | 3.5974 |
| 000792.SZ | 盐湖股份 | lithium | 29.75 | -3.6281 | -7.8377 | -17.931 | -26.3614 | 9.7795 | 2.7651 | 0.95 | 15.2628 | 3.5222 |
| 600489.SH | 中金黄金 | precious_metals | 21.92 | -3.4361 | -3.7752 | -17.8411 | -22.8169 | 10.8398 | 3.17 | 0.93 | 16.931 | 3.2397 |
| 000807.SZ | 云铝股份 | aluminum | 24.17 | -3.32 | -19.4065 | -24.4451 | -34.0878 | 0 | 3.7571 | 1.13 | 9.6565 | 2.3511 |
| 000933.SZ | 神火股份 | aluminum | 23.74 | -3.2994 | -21.2342 | -22.8218 | -32.9568 | 0 | 3.3703 | 1.05 | 9.5567 | 1.9852 |
| 300390.SZ | 天华新能 | lithium | 89 | -2.9973 | 0.3269 | 53.0525 | -22.4063 | 16.5375 | 3.8661 | 0.8 | 56.4636 | 5.991 |
| 601166.SH | 兴业银行 | 银行 | 17.32 | -2.9148 | -0.2879 | -7.3301 | -8.3113 | 2.9429 | 1.4477 | 1.12 | 4.7293 | 0.4416 |
| 002466.SZ | 天齐锂业 | lithium | 62.18 | -2.9044 | -5.4728 | 12.1573 | -23.9016 | 13.9502 | 2.5078 | 0.86 | 47.6767 | 2.2982 |
| 600595.SH | 中孚实业 | aluminum | 6.06 | -2.8846 | -14.5275 | -17.663 | -31.5254 | 0 | 3.8159 | 1.03 | 10.9981 | 1.3542 |
| 002460.SZ | 赣锋锂业 | lithium | 69.36 | -2.7482 | -7.9251 | -13.0282 | -24.1553 | 13.6393 | 2.6787 | 0.84 | 38.209 | 3.1302 |
| 601899.SH | 紫金矿业 | copper | 29.69 | -2.4318 | -1.0003 | -9.7843 | -16.7414 | 11.3428 | 3.6568 | 0.94 | 12.7975 | 4.0019 |
| 600219.SH | 南山铝业 | aluminum | 4.53 | -2.1598 | -10.297 | -23.7374 | -29.108 | 1.5351 | 3.5556 | 0.95 | 12.5879 | 1.021 |
| 603799.SH | 华友钴业 | nickel_cobalt | 52.1 | -0.9317 | -7.7223 | -9.2651 | -23.607 | 12.5642 | 3.0364 | 0.85 | 13.4347 | 1.9564 |
| 603993.SH | 洛阳钼业 | copper | 20.04 | -0.6445 | 13.6054 | 14.3836 | -4.526 | 20.131 | 4.9699 | 0.98 | 17.7512 | 4.8246 |
| 002237.SZ | 恒邦股份 | precious_metals | 14.43 | -0.5513 | 3.8129 | 0 | -21.9156 | 18.837 | 3.157 | 1.21 | 31.2249 | 1.5314 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.42 | 0 | -8.0545 | -2.6247 | -23.029 | 8.3212 | 2.3645 | 1.25 | 23.7886 | 1.7351 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 38.23 | 0.1047 | -8.123 | -5.6049 | -22.4071 | 11.6667 | 2.9704 | 0.76 | 42.8342 | 2.134 |
| 000612.SZ | 焦作万方 | aluminum | 11.03 | 0.5469 | -6.9198 | -3.0756 | -20.0725 | 5.1774 | 3.5664 | 0.82 | 9.2575 | 1.7064 |
| 002155.SZ | 湖南黄金 | precious_metals | 26.66 | 0.6038 | 7.9789 | -8.2272 | -16.8693 | 15.3177 | 3.0989 | 0.95 | 23.7894 | 4.7819 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 41.74 | 0.7483 | 15.0179 | 37.8013 | -4.5943 | 21.9606 | 5.5691 | 0.97 | 29.422 | 3.3147 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260618 | 兴业银行股份有限公司公开发行A股可转换公司债券受托管理事务报告（2025年度） | https://static.cninfo.com.cn/finalpage/2026-06-18/1225375059.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | unclassified | official_announcement | CNINFO/Tushare announcement | 20260618 | 兴业银行股份有限公司公开发行A股可转换公司债券受托管理事务报告（2025年度） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-18/1225375059.PDF |
| weak_rumor | commodity_or_sector | web_search | Bing News | 周日, 21 6月 | 首页 -- 兴业银行官方网站 | Web/search corroboration only; not filing or announcement grade. | https://www.cib.com.cn/ |
| weak_rumor | unclassified | web_search | Bing News | 周日, 21 6月 | 企业金融 -- 兴业银行官方网站 | Web/search corroboration only; not filing or announcement grade. | https://www.cib.com.cn/cn/corporate/ |
| weak_rumor | flow_or_sentiment | web_search | Bing News | 周日, 21 6月 | 中国银行网站_全球门户首页 | Web/search corroboration only; not filing or announcement grade. | https://www.boc.cn/ |
| weak_rumor | unclassified | web_search | Bing News | 周日, 21 6月 | 中国农业银行 | Web/search corroboration only; not filing or announcement grade. | https://www.abchina.com/cn/ |
| weak_rumor | company_event | web_search | Bing News | 周日, 21 6月 | 中国工商银行中国网站 | Web/search corroboration only; not filing or announcement grade. | https://www.icbc.com.cn/ |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 兴业银行 大跌 原因: skipped low-signal result 兴业银行股份有限公司_百度百科.
- web_search 兴业银行 下跌 传闻: skipped low-signal result 兴业银行股份有限公司_百度百科.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.