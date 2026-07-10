# Price-move attribution context for 300750.SZ as of 2026-07-10

- Status: ready
- Company: 宁德时代
- Basket: 电气设备
- Attribution label: commodity_equity_divergence + cross_metal_underperformance + weak_trend_continuation
- Attribution reason: Mapped commodity futures did not move enough to explain the equity selloff. Target also underperformed the broader copper/precious/lithium/small-metal equity reference basket. The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300750.SZ | 宁德时代 | 电气设备 | 348.76 | -7.1212 | -8.7493 | -22.0822 | -24.1826 | 4.0166 | 3.0332 | 2.09 | 20.4313 | 4.5165 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | -1.7199 | -5.4013 |
| same_metal_equities | 电气设备 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | 1.262 | -8.3833 |
| mapped_commodity | mapped futures products | -0.928 | -6.1932 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260710 | 3996.1616 | -1.0015 | 0.2294 | -2.1766 |
| CSI 300 | 20260710 | 4780.7867 | -1.959 | 1.2361 | 0.2682 |
| CSI 500 | 20260710 | 8503.9705 | -1.7199 | 5.8263 | 2.8251 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lithium carbonate | raw material proxy | LC.GFE | 151600 | 20260710 | -26.06% | Verified by Tushare futures daily data. | -0.928 | -13.173 | 3.1968 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300750.SZ | 宁德时代 | 电气设备 | 348.76 | -7.1212 | -8.7493 | -22.0822 | -24.1826 | 4.0166 | 3.0332 | 2.09 | 20.4313 | 4.5165 |
| 300390.SZ | 天华新能 | lithium | 65.7 | -4.9204 | -30.1287 | -23.4355 | -42.7201 | 0 | 6.781 | 1.09 | 41.6816 | 4.4226 |
| 002460.SZ | 赣锋锂业 | lithium | 53.63 | -4.215 | -23.32 | -35.6646 | -41.3559 | 0 | 3.5651 | 0.99 | 29.5437 | 2.4203 |
| 002466.SZ | 天齐锂业 | lithium | 47.8 | -3.9968 | -21.6393 | -32.3999 | -41.5004 | 0 | 4.4647 | 1.11 | 36.6508 | 1.7667 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 9.51 | -2.8601 | 12.6777 | 5.7842 | -25.7031 | 19.2448 | 5.4336 | 0.87 | 39.8521 | 2.7884 |
| 000792.SZ | 盐湖股份 | lithium | 25.4 | -2.6447 | -16.4748 | -32.2486 | -37.1287 | 0 | 3.5141 | N/A | 13.0311 | 3.0072 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 36.45 | -2.2002 | 4.5611 | -4.1042 | -21.7811 | 9.7145 | 5.6376 | 0.83 | 25.6931 | 2.8946 |
| 002155.SZ | 湖南黄金 | precious_metals | 23.76 | -2.061 | 1.8431 | -23.057 | -24.2105 | 5.8926 | 4.7794 | 0.74 | 21.2016 | 4.2617 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 4.84 | -1.626 | 4.5356 | -15.8261 | -28.1899 | 7.8947 | 5.4469 | N/A | 68.9676 | 2.1162 |
| 603799.SH | 华友钴业 | nickel_cobalt | 41.51 | -1.6118 | -12.6657 | -36.626 | -39.1349 | 0 | 3.7446 | 0.88 | 10.6859 | 1.5561 |
| 002237.SZ | 恒邦股份 | precious_metals | 12.84 | -0.6961 | 4.4752 | -25.5652 | -30.5195 | 5.8968 | 4.7642 | 0.63 | 27.7843 | 1.3626 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 33.11 | -0.1809 | -5.1289 | -29.9408 | -32.7989 | 0 | 3.8257 | 0.64 | 37.0976 | 1.8482 |
| 601899.SH | 紫金矿业 | copper | 27.72 | 0.3621 | 1.427 | -22.2658 | -22.2658 | 10.0398 | 4.1652 | 0.84 | 11.9484 | 3.7364 |
| 002340.SZ | 格林美 | nickel_cobalt | 6.54 | 0.6154 | -8.2749 | -22.8774 | -32.1577 | 0 | 3.1439 | 0.8 | 20.9673 | 1.5293 |
| 000878.SZ | 云南铜业 | copper | 15.24 | 1.1952 | -5.2239 | -22.1655 | -26.3056 | 0.2663 | 4.0723 | 1.05 | 27.3554 | 2.0056 |
| 000630.SZ | 铜陵有色 | copper | 6.1 | 1.3289 | -5.4264 | -5.4264 | -23.0769 | 1.5177 | 4.5623 | N/A | 31.104 | 2.1821 |
| 600219.SH | 南山铝业 | aluminum | 4.08 | 1.7456 | -10.917 | -33.6585 | -33.6585 | 0.5013 | 2.7797 | 1.19 | 11.3374 | 0.9196 |
| 603993.SH | 洛阳钼业 | copper | 17.5 | 1.8034 | 0.7484 | -12.8486 | -19.1686 | 2.3824 | 5.0391 | 1 | 15.5013 | 4.2131 |
| 600489.SH | 中金黄金 | precious_metals | 20.34 | 1.9549 | -1.4535 | -25.3852 | -27.9235 | 11.0802 | 3.9889 | 0.77 | 15.7107 | 3.0062 |
| 000612.SZ | 焦作万方 | aluminum | 10.01 | 2.1429 | -5.3875 | -25.2427 | -26.8809 | 0 | 4.0688 | N/A | 8.4014 | 1.5486 |
| 600547.SH | 山东黄金 | precious_metals | 24.96 | 2.8007 | -7.384 | -33.9683 | -33.9683 | 5.5652 | 3.7483 | 0.87 | 22.3042 | 3.5952 |
| 601600.SH | 中国铝业 | aluminum | 8.35 | 3.0864 | -19.1675 | -31.2757 | -31.2757 | 0 | 3.4795 | 1.19 | 9.7671 | 1.7762 |
| 600595.SH | 中孚实业 | aluminum | 5.94 | 4.2105 | -10 | -31.7241 | -31.7241 | 2.8881 | 3.8983 | 1.94 | 10.7803 | 1.3274 |
| 000975.SZ | 山金国际 | precious_metals | 20.03 | 4.2144 | -2.3879 | -33.9815 | -33.9815 | 14.5411 | 4.585 | 0.93 | 15.125 | 3.4199 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260706 | H股公告（截至2026年6月30日止股份发行人的证券变动月报表） | https://static.cninfo.com.cn/finalpage/2026-07-06/1225412109.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260706 | H股公告（截至2026年6月30日止股份发行人的证券变动月报表） | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-07-06/1225412109.PDF |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 宁德时代 大跌 原因: skipped low-signal result Ford Transit cars for sale or order in Victoria.
- web_search 宁德时代 大跌 原因: skipped low-signal result Ford Transit Van cars for sale or order in Melbourne, Victor.
- web_search 宁德时代 大跌 原因: skipped low-signal result ford transit van for sale | Buy New and Used Cars in Victori.
- web_search 宁德时代 下跌 传闻: skipped low-signal result Delima 2.0.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result Is it possible to filter only ProductVisualSearch from speci.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result Request for Bing Search API V7 Access Approval.
- web_search 电气设备 板块 大跌 原因: skipped low-signal result Change search engine of Visual Studio 2019 - Stack Overflow.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.