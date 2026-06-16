# Price-move attribution context for 603345.SH as of 2026-06-15

- Status: ready
- Company: 安井食品
- Basket: 食品
- Attribution label: cross_metal_underperformance + weak_trend_continuation
- Attribution reason: Target also underperformed the broader copper/precious/lithium/small-metal equity reference basket. The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603345.SH | 安井食品 | 食品 | 88.85 | -1.4748 | -10.4786 | 1.6125 | -19.0949 | 4.0378 | 2.2417 | 1 | 19.3817 | 1.8445 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 2.3945 | -3.8693 |
| same_metal_equities | 食品 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | 4.3766 | -5.8514 |
| mapped_commodity | mapped futures products | -0.5757 | -0.8991 |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260615 | 4096.472 | 1.6113 | -0.8485 | 4.6694 |
| CSI 300 | 20260615 | 4891.713 | 2.3945 | 1.2039 | 8.6427 |
| CSI 500 | 20260615 | 8406.748 | 3.7076 | -1.7242 | 8.6478 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Live hog futures | meat raw-material cost proxy | LH2607.DCE | 10170 | 20260615 | -8.58% | Verified by Tushare futures daily data. | 0.1477 | -5.219 | 1.1686 |
| Soybean meal futures | feed and protein-chain cost proxy | M2607.DCE | 2764 | 20260615 | -2.61% | Verified by Tushare futures daily data. | -0.1806 | -1.4968 | 0.7745 |
| Corn futures | feed and starch/flour-chain cost proxy | C2607.DCE | 2322 | 20260615 | -3.01% | Verified by Tushare futures daily data. | -1.2335 | -1.3175 | 0.6085 |
| Palm oil futures | edible-oil cost proxy for prepared dishes | P2607.DCE | 8977 | 20260615 | -4.57% | Verified by Tushare futures daily data. | -0.9708 | -4.276 | 1.1109 |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000807.SZ | 云铝股份 | aluminum | 26.9 | -4.2705 | -7.2414 | -6.3696 | -26.643 | 5.4409 | 3.6855 | 2.03 | 10.7472 | 2.7168 |
| 000933.SZ | 神火股份 | aluminum | 26.44 | -3.1856 | -9.2656 | -13.3683 | -25.3318 | 4.0381 | 3.2211 | 1.63 | 10.6436 | 2.3683 |
| 600595.SH | 中孚实业 | aluminum | 6.72 | -2.6087 | -5.8824 | -5.8824 | -24.0678 | 6.8111 | 3.6854 | 1.37 | 12.1959 | 1.5628 |
| 603345.SH | 安井食品 | 食品 | 88.85 | -1.4748 | -10.4786 | 1.6125 | -19.0949 | 4.0378 | 2.2417 | 1 | 19.3817 | 1.8445 |
| 601600.SH | 中国铝业 | aluminum | 10.67 | -1.2037 | 1.4259 | -6.7308 | -16.6406 | 7.7844 | 4.1762 | 1.57 | 12.483 | 2.2697 |
| 002460.SZ | 赣锋锂业 | lithium | 71.32 | 0.2248 | -10.1537 | -10.4807 | -22.012 | 13.3843 | 2.8267 | 1.08 | 39.2887 | 3.2187 |
| 002532.SZ | 天山铝业 | aluminum | 13.52 | 0.6701 | -8.7719 | -16.129 | -31.3357 | 2.0517 | 3.4862 | 1.55 | 10.4675 | 2.074 |
| 000792.SZ | 盐湖股份 | lithium | 32.03 | 1.041 | -3.958 | -18.8086 | -20.7178 | 12.7312 | 2.7041 | 1.22 | 16.3636 | 3.7921 |
| 300390.SZ | 天华新能 | lithium | 97.12 | 1.0614 | 5.1424 | 51.7263 | -15.3269 | 22.0627 | 3.9957 | 1.1 | 58.9855 | 6.5376 |
| 000612.SZ | 焦作万方 | aluminum | 11.59 | 1.3998 | -1.5293 | -0.8554 | -16.0145 | 9.5877 | 3.5358 | 1.47 | 9.7275 | 1.888 |
| 600219.SH | 南山铝业 | aluminum | 4.81 | 1.6913 | -7.3218 | -18.4746 | -25.886 | 3.7281 | 3.583 | 1.23 | 13.3659 | 1.1183 |
| 002466.SZ | 天齐锂业 | lithium | 63.72 | 1.952 | -8.158 | 9.9379 | -22.0169 | 11.21 | 2.7455 | 1.18 | 48.8575 | 2.3552 |
| 002340.SZ | 格林美 | nickel_cobalt | 7.58 | 2.9891 | -9.4385 | -6.6502 | -21.3693 | 7.4453 | 2.4239 | 1.12 | 24.3016 | 1.7728 |
| 600547.SH | 山东黄金 | precious_metals | 28.66 | 3.1306 | -8.3173 | -25.7128 | -32.5488 | 5.0265 | 2.8739 | 1.33 | 25.6105 | 4.1281 |
| 300618.SZ | 寒锐钴业 | nickel_cobalt | 38.7 | 4.3127 | -8.424 | -10.4167 | -21.4532 | 8.4795 | 2.9702 | 1.55 | 43.3608 | 2.1809 |
| 603799.SH | 华友钴业 | nickel_cobalt | 52.45 | 4.4405 | -10.0497 | -12.4374 | -23.0938 | 7.4914 | 3.0829 | 1.28 | 13.5249 | 2.0073 |
| 002237.SZ | 恒邦股份 | precious_metals | 13.64 | 4.8424 | -8.21 | -6.8942 | -26.1905 | 6.552 | 2.9334 | 1.41 | 29.3873 | 1.4684 |
| 000975.SZ | 山金国际 | precious_metals | 22.15 | 4.9266 | -9.2213 | -21.5929 | -30.5207 | 4.2469 | 3.2 | 1.44 | 16.7258 | 4.1479 |
| 600489.SH | 中金黄金 | precious_metals | 22.58 | 4.9744 | -5.0862 | -11.5897 | -20.493 | 5.0293 | 3.1218 | 1.3 | 17.4408 | 3.3373 |
| 000878.SZ | 云南铜业 | copper | 18.23 | 5.5588 | -0.5998 | -1.2994 | -11.8472 | 8.208 | 3.9063 | 1.86 | 31.196 | 2.474 |
| 002155.SZ | 湖南黄金 | precious_metals | 25.65 | 5.8605 | -1.422 | -12.3077 | -20.0187 | 5.4395 | 3.115 | 1.75 | 22.8881 | 4.8623 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.39 | 5.8939 | -7.2289 | 1.1257 | -20.0297 | 11.6228 | 4.5907 | 2.48 | 76.8048 | 2.3671 |
| 600988.SH | 赤峰黄金 | precious_metals | 32.63 | 7.4416 | -10.9929 | -18.0151 | -31.1022 | 7.8097 | 4.1477 | 1.37 | 17.2866 | 4.5326 |
| 601899.SH | 紫金矿业 | copper | 31.31 | 7.6315 | 0.0319 | -3.5725 | -12.1985 | 6.4398 | 3.5931 | 1.62 | 13.4958 | 4.2203 |

## Recent Company Event Check
No recent announcement rows found in the short event window.

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| weak_rumor | unclassified | web_search | Bing News | 周日, 14 6月 | 食品伙伴网（原食品伴侣网）—关注食品安全，探讨食品技术 ... | Web/search corroboration only; not filing or announcement grade. | https://www.foodmate.net/ |
| weak_rumor | unclassified | web_search | Bing News | 周日, 14 6月 | Foodaily每日食品网_关注食品行业_了解食品资讯_聚焦食品 ... | Web/search corroboration only; not filing or announcement grade. | https://www.foodaily.com/ |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (major_news unavailable: major_news unavailable: configured_http_url: 请联系管理员添加此权限).
- tushare_news_feed: no matching rows or unavailable (news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限; news unavailable: news unavailable: configured_http_url: 请联系管理员添加此权限).
- web_search 安井食品 大跌 原因: skipped low-signal result 安（汉字）_百度百科.
- web_search 安井食品 大跌 原因: skipped low-signal result 安的意思,安的解释,安的拼音,安的部首,安的笔顺-汉语国学.
- web_search 安井食品 大跌 原因: skipped low-signal result 汉字“安”怎么解释? - 知乎.
- web_search 安井食品 下跌 传闻: skipped low-signal result 安（汉字）_百度百科.
- web_search 安井食品 下跌 传闻: skipped low-signal result 安的意思,安的解释,安的拼音,安的部首,安的笔顺-汉语国学.
- web_search 安井食品 下跌 传闻: skipped low-signal result 汉字“安”怎么解释? - 知乎.
- web_search 食品 板块 大跌 原因: skipped low-signal result 食品_百度百科.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.