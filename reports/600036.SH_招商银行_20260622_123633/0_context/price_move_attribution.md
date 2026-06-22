# Price-move attribution context for 600036.SH as of 2026-06-22

- Status: ready
- Company: 招商银行
- Basket: 银行
- Attribution label: mixed_or_unclassified
- Attribution reason: No single attribution bucket dominates; use the residual table and events for judgment.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 600036.SH | 招商银行 | 银行 | 37.26 | -2.5373 | 0.2961 | -5.4315 | -6.6399 | 3.4921 | 1.1476 | 1.21 | 6.2336 | 0.8298 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 0.2071 | -2.7444 |
| same_metal_equities | 银行 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | -2.2958 | -0.2415 |
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
| 000792.SZ | 盐湖股份 | lithium | 29.75 | -3.6281 | -7.8377 | -17.931 | -26.3614 | 9.7795 | 2.7651 | 0.95 | 15.2628 | 3.5222 |
| 600489.SH | 中金黄金 | precious_metals | 21.92 | -3.4361 | -3.7752 | -17.8411 | -22.8169 | 10.8398 | 3.17 | 0.93 | 16.931 | 3.2397 |
| 000807.SZ | 云铝股份 | aluminum | 24.17 | -3.32 | -19.4065 | -24.4451 | -34.0878 | 0 | 3.7571 | 1.13 | 9.6565 | 2.3511 |
| 300390.SZ | 天华新能 | lithium | 89 | -2.9973 | 0.3269 | 53.0525 | -22.4063 | 16.5375 | 3.8661 | 0.8 | 56.4636 | 5.991 |
| 600595.SH | 中孚实业 | aluminum | 6.06 | -2.8846 | -14.5275 | -17.663 | -31.5254 | 0 | 3.8159 | 1.03 | 10.9981 | 1.3542 |
| 600036.SH | 招商银行 | 银行 | 37.26 | -2.5373 | 0.2961 | -5.4315 | -6.6399 | 3.4921 | 1.1476 | 1.21 | 6.2336 | 0.8298 |
| 601899.SH | 紫金矿业 | copper | 29.69 | -2.4318 | -1.0003 | -9.7843 | -16.7414 | 11.3428 | 3.6568 | 0.94 | 12.7975 | 4.0019 |
| 600219.SH | 南山铝业 | aluminum | 4.53 | -2.1598 | -10.297 | -23.7374 | -29.108 | 1.5351 | 3.5556 | 0.95 | 12.5879 | 1.021 |
| 603799.SH | 华友钴业 | nickel_cobalt | 52.1 | -0.9317 | -7.7223 | -9.2651 | -23.607 | 12.5642 | 3.0364 | 0.85 | 13.4347 | 1.9564 |
| 603993.SH | 洛阳钼业 | copper | 20.04 | -0.6445 | 13.6054 | 14.3836 | -4.526 | 20.131 | 4.9699 | 0.98 | 17.7512 | 4.8246 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 38.23 | 0.1047 | -8.123 | -5.6049 | -22.4071 | 11.6667 | 2.9704 | 0.76 | 42.8342 | 2.134 |
| 000612.SZ | 焦作万方 | aluminum | 11.03 | 0.5469 | -6.9198 | -3.0756 | -20.0725 | 5.1774 | 3.5664 | 0.82 | 9.2575 | 1.7064 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.15 | 0.7828 | N/A | 0 | 0 | 0 | N/A | 0.87 | 73.3849 | 2.2518 |
| 000630.SZ | 铜陵有色 | copper | 7.65 | 1.1905 | 32.3529 | 33.0435 | -0.1305 | 30.7958 | 4.9989 | 1.16 | 39.0075 | 2.7366 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 10.28 | 1.7822 | 11.2554 | 33.5065 | -5.5147 | 23.0207 | 5.1318 | 1.12 | 43.0788 | 3.0141 |
| 000878.SZ | 云南铜业 | copper | 18.66 | 4.0714 | 7.9237 | 7.2414 | -9.7679 | 12.3434 | 3.9274 | 1.47 | 33.4943 | 2.4557 |
| 600362.SH | 江西铜业 | copper | 53.31 | 10.0083 | 22.6081 | 25.5535 | 0 | 20.7275 | 5.1629 | 1.66 | 23.0883 | 2.1947 |
| 000933.SZ | 000933.SZ | aluminum | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 000960.SZ | 000960.SZ | zinc_lead_tin | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 000975.SZ | 000975.SZ | precious_metals | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260617 | 招商银行股份有限公司关于无固定期限资本债券发行完毕的公告 | https://static.cninfo.com.cn/finalpage/2026-06-17/1225373720.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260617 | 招商银行股份有限公司关于无固定期限资本债券发行完毕的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-06-17/1225373720.PDF |
| weak_rumor | macro_rate_fx | web_search | Bing News | 周日, 21 6月 | 一网通主页 -- 招商银行官方网站 | Web/search corroboration only; not filing or announcement grade. | https://cmbchina.com/ |
| weak_rumor | unclassified | web_search | Bing News | 周日, 21 6月 | 招商银行企业银行U-BANK | Contains rumor/possibility wording; use only as a watch item. | https://u.ebank.cmbchina.com/CmbBank_FB/UI/Login/FBPOPLogin.aspx |
| weak_rumor | company_event | web_search | Bing News | 周日, 21 6月 | 重要公告 -- 招商银行官方网站 | Web/search corroboration only; not filing or announcement grade. | https://www.cmbchina.cn/main/default.aspx |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 银行 板块 大跌 原因: skipped low-signal result Sign in to Gmail.
- web_search 银行 板块 大跌 原因: skipped low-signal result Sign in to Gmail.
- web_search 银行 板块 大跌 原因: skipped low-signal result Gmail にログインする.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.