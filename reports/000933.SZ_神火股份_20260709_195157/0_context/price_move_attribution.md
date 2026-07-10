# Price-move attribution context for 000933.SZ as of 2026-07-09

- Status: ready
- Company: 神火股份
- Basket: aluminum
- Attribution label: weak_trend_continuation
- Attribution reason: The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000933.SZ | 神火股份 | aluminum | 21.35 | -2.4669 | -18.6667 | -36.6281 | -36.6281 | 3.6949 | 3.6084 | 0.81 | 8.5946 | 1.7853 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 2.5398 | -5.0067 |
| same_metal_equities | aluminum | -1.4523 | -1.0146 |
| cross_metal_equities | all configured metal equity baskets | -0.4963 | -1.9706 |
| mapped_commodity | mapped futures products | -0.065 | -2.4019 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260709 | 4036.5879 | 1.6548 | 1.0859 | -1.1156 |
| CSI 300 | 20260709 | 4876.3125 | 2.5398 | 2.6896 | 2.4986 |
| CSI 500 | 20260709 | 8652.787 | 3.1319 | 7.3032 | 4.3759 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Aluminum | industry proxy | AL.SHF | 23060 | 20260709 | -5.97% | Verified by Tushare futures daily data. | -0.065 | -3.5348 | 1.174 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300390.SZ | 天华新能 | lithium | 69.1 | -14.7124 | -21.1187 | -20.2171 | -39.7559 | 2.9087 | 7.0106 | 1.64 | 43.8386 | 4.6514 |
| 002466.SZ | 天齐锂业 | lithium | 49.79 | -6.5328 | -16.2912 | -25.4864 | -39.065 | 0 | 4.4824 | 1.79 | 38.1767 | 1.8403 |
| 002532.SZ | 天山铝业 | aluminum | 10.67 | -3.6134 | -20.3137 | -43.5151 | -43.5151 | 3.1687 | 3.575 | 1.2 | 8.261 | 1.5768 |
| 000612.SZ | 焦作万方 | aluminum | 9.8 | -2.7778 | -7.109 | -27.2997 | -28.4149 | 0 | 4.0336 | 1.27 | 8.2251 | 1.5161 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 33.17 | -2.4985 | -4.1052 | -27.907 | -32.6771 | 0 | 3.8334 | 0.92 | 37.1648 | 1.8515 |
| 000933.SZ | 神火股份 | aluminum | 21.35 | -2.4669 | -18.6667 | -36.6281 | -36.6281 | 3.6949 | 3.6084 | 0.81 | 8.5946 | 1.7853 |
| 002340.SZ | 格林美 | nickel_cobalt | 6.5 | -2.4024 | -7.4074 | -23.1678 | -32.5726 | 1.2158 | 3.167 | 0.88 | 20.8391 | 1.52 |
| 603993.SH | 洛阳钼业 | copper | 17.19 | -1.9395 | 2.3824 | -15.0692 | -20.6005 | 4.4074 | 5.0809 | 1.03 | 15.2267 | 4.1385 |
| 000807.SZ | 云铝股份 | aluminum | 21.89 | -1.9265 | -17.8612 | -37.7063 | -37.7063 | 2.5264 | 3.8591 | 1.01 | 8.7456 | 2.1293 |
| 000792.SZ | 盐湖股份 | lithium | 26.09 | -1.6585 | -10.1275 | -30.4452 | -35.4208 | 0 | 3.6984 | 1.1 | 13.3851 | 3.0889 |
| 000975.SZ | 山金国际 | precious_metals | 19.22 | -1.1825 | -5.0864 | -36.7139 | -36.7139 | 15.9118 | 4.4892 | 0.73 | 14.5133 | 3.2816 |
| 603799.SH | 华友钴业 | nickel_cobalt | 42.19 | -1.1481 | -10.5196 | -35.862 | -38.1378 | 0 | 3.7495 | 1.38 | 10.8609 | 1.5816 |
| 601600.SH | 中国铝业 | aluminum | 8.1 | -0.978 | -19.802 | -34.1998 | -34.1998 | 0.1224 | 3.4339 | 1.02 | 9.4747 | 1.723 |
| 600547.SH | 山东黄 | precious_metals | 24.28 | -0.7765 | -8.7561 | -36.3064 | -36.3064 | 7.1739 | 3.6968 | 0.7 | 21.6966 | 3.4972 |
| 600219.SH | 南山铝业 | aluminum | 4.01 | -0.4963 | -12.0614 | -35.4267 | -35.4267 | 1.0025 | 2.7382 | 0.98 | 11.1429 | 0.9038 |
| 000630.SZ | 铜陵有色 | copper | 6.02 | -0.3311 | -5.1969 | -7.6687 | -24.0858 | 1.855 | 4.5669 | 0.96 | 30.6961 | 2.1535 |
| 002460.SZ | 赣锋锂业 | lithium | 55.99 | -0.3205 | -17.1746 | -32.3056 | -38.7753 | 0 | 3.6423 | 1.42 | 30.8437 | 2.5268 |
| 600988.SH | 赤峰黄金 | precious_metals | 31.35 | 0.0958 | 11.2886 | -29.1365 | -29.3919 | 21.3483 | 5.2445 | 0.8 | 16.6085 | 4.1695 |
| 000878.SZ | 云南铜业 | copper | 15.06 | 0.2663 | -5.6391 | -23.6695 | -27.176 | 0 | 4.0655 | 1.14 | 27.0323 | 1.9819 |
| 600595.SH | 中孚实业 | aluminum | 5.7 | 0.3521 | -13.8973 | -33.2553 | -34.4828 | 2.5271 | 3.7416 | 1.33 | 10.3448 | 1.2737 |
| 600489.SH | 中金黄金 | precious_metals | 19.95 | 0.3521 | -2.5879 | -26.2477 | -29.3055 | 10.6904 | 3.9673 | 0.65 | 15.4094 | 2.9485 |
| 002237.SZ | 恒邦股份 | precious_metals | 12.93 | 0.7009 | 5.8968 | -23.5364 | -30.0325 | 5.1597 | 4.7586 | 0.51 | 27.9791 | 1.3722 |
| 601899.SH | 紫金矿业 | copper | 27.62 | 0.9503 | -0.2888 | -20.6778 | -22.5463 | 9.004 | 4.178 | 0.68 | 11.9053 | 3.7229 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 4.92 | 1.6529 | 7.8947 | -16.4686 | -27.003 | 6.1404 | 5.4321 | 0.64 | 70.1076 | 2.1512 |

## Recent Company Event Check
No recent announcement rows found in the short event window.

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| weak_rumor | commodity_or_sector | web_search | Bing News | 周三, 08 7月 | 铝业行情-今日铝价,铝锭价格,有色宝长江,上海期货,南海有 ... | Web/search corroboration only; not filing or announcement grade. | https://market.cnal.com/ |
| weak_rumor | commodity_or_sector | web_search | Bing News | 周三, 08 7月 | 铝：从贵族金属到工业基石 - 知乎 | Web/search corroboration only; not filing or announcement grade. | https://zhuanlan.zhihu.com/p/1903387727019374018 |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 神火股份 大跌 原因: skipped low-signal result 神（汉语文字）_百度百科.
- web_search 神火股份 大跌 原因: skipped low-signal result 神的意思,神的解释,神的拼音,神的部首,神的笔顺-汉语国学.
- web_search 神火股份 大跌 原因: skipped low-signal result 神（宗教及神话概念）_百度百科.
- web_search 神火股份 下跌 传闻: skipped low-signal result 神（汉语文字）_百度百科.
- web_search 神火股份 下跌 传闻: skipped low-signal result 神的意思,神的解释,神的拼音,神的部首,神的笔顺-汉语国学.
- web_search 神火股份 下跌 传闻: skipped low-signal result 神（宗教及神话概念）_百度百科.
- web_search 铝 板块 大跌 原因: skipped low-signal result 铝（金属元素）_百度百科.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.