# Price-move attribution context for 300723.SZ as of 2026-08-08

- Status: ready
- Company: 一品红
- Basket: 化学制药
- Attribution label: mixed_or_unclassified
- Attribution reason: No single attribution bucket dominates; use the residual table and events for judgment.

## Target Move Snapshot
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300723.SZ | 一品红 | 化学制药 | 37.99 | 4.1964 | -4.4277 | -0.4976 | -13.4821 | 12.1501 | 3.8109 | 1.75 | 85.8022 | 8.8649 |

## Attribution Residual Table
| bucket | proxy | one_day_pct | target_minus_proxy |
| --- | --- | --- | --- |
| market | SSE/CSI median | 1.0175 | 3.1789 |
| same_metal_equities | 化学制药 | N/A | N/A |
| cross_metal_equities | all configured metal equity baskets | 2.2582 | 1.9382 |
| mapped_commodity | mapped futures products | N/A | N/A |

## Market Index Reference
| index | trade_date | close | one_day_pct | ret_20d_pct | ret_window_pct |
| --- | --- | --- | --- | --- | --- |
| SSE Composite | 20260807 | 3940.0371 | 1.0175 | -1.4045 | -5.3373 |
| CSI 300 | 20260807 | 4694.4365 | 0.9272 | -1.8062 | -3.2215 |
| CSI 500 | 20260807 | 7980.1245 | 1.9256 | -6.16 | -7.8114 |

## Mapped Commodity Reference
| product | role | exchange_proxy | latest_price | latest_date | window_change | status | one_day_pct | ret_20d_pct | realized_vol_20d_daily_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N/A | N/A | No mapped futures product | N/A | N/A | N/A | No commodity mapping; do not attribute the move to commodity prices without evidence. | N/A | N/A | N/A |

## Cross-Metal Equity Reference
| symbol | name | basket | close | one_day_pct | ret_20d_pct | ret_window_pct | drawdown_from_window_high_pct | pre_today_rebound_from_30d_low_pct | realized_vol_20d_daily_pct | volume_ratio | pe_ttm | pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000612.SZ | 焦作万方 | aluminum | 11.5 | 0.7005 | 14.8851 | -6.0458 | -7.9263 | 16.5306 | 2.7531 | 0.95 | 9.6519 | 1.7791 |
| 000792.SZ | 盐湖股份 | lithium | 28.8 | 0.9464 | 13.3858 | -12.3554 | -12.3554 | 16.5441 | 2.2858 | 1 | 14.7754 | 3.4097 |
| 002460.SZ | 赣锋锂业 | lithium | 52.82 | 1.1103 | -1.5103 | -31.5537 | -31.5537 | 13.2943 | 3.2276 | 0.98 | 29.0975 | 2.3838 |
| 600595.SH | 中孚实业 | aluminum | 6.63 | 1.2214 | 11.6162 | -9.4262 | -12.8778 | 18.231 | 3.6396 | 1.07 | 9.522 | 1.4523 |
| 600497.SH | 驰宏锌锗 | zinc_lead_tin | 10.45 | 1.2597 | 9.8843 | 4.8144 | -18.3594 | 21.8418 | 4.6103 | 1.16 | 43.7912 | 3.064 |
| 002340.SZ | 格林美 | nickel_cobalt | 6.84 | 1.3333 | 4.5872 | -18.4744 | -18.4744 | 7.1429 | 1.813 | 1.29 | 21.9291 | 1.5995 |
| 002466.SZ | 天齐锂业 | lithium | 47.87 | 1.4625 | 0.1464 | -29.7682 | -29.7682 | 11.563 | 3.8908 | 1.2 | 36.7045 | 1.7693 |
| 600547.SH | 山东黄金 | precious_metals | 30.48 | 1.7356 | 22.1154 | 0.0985 | -3.1151 | 30.2609 | 3.5477 | 0.98 | 27.2369 | 4.3903 |
| 000807.SZ | 云铝股份 | aluminum | 27.13 | 1.7629 | 17.1922 | -10.9324 | -14.3894 | 22.4621 | 3.2421 | 0.88 | 10.8391 | 2.639 |
| 000933.SZ | 神火股份 | aluminum | 26.83 | 1.8603 | 14.2188 | -10.8638 | -16.6511 | 24.775 | 3.1561 | 0.93 | 8.7676 | 2.18 |
| 601899.SH | 紫金矿业 | copper | 35.15 | 1.8841 | 26.8038 | 15.663 | 0 | 37.4502 | 2.9695 | 0.89 | 15.151 | 4.7379 |
| 600988.SH | 赤峰黄金 | precious_metals | 42.09 | 1.9128 | 28.1669 | 17.9652 | 0 | 60.0155 | 5.0774 | 1.05 | 22.2983 | 5.5979 |
| 300390.SZ | 天华新能 | lithium | 60.7 | 1.9483 | -7.6104 | -34.3429 | -38.5814 | 11.6445 | 4.272 | 1.09 | 38.5094 | 4.086 |
| 603993.SH | 洛阳钼业 | copper | 20.83 | 2.2582 | 19.0286 | 15.98 | -3.7875 | 20.8185 | 3.4969 | 1.07 | 18.451 | 5.0148 |
| 000751.SZ | 锌业股份 | zinc_lead_tin | 5.3 | 2.3166 | 9.5041 | -3.2847 | -14.791 | 22.1698 | 4.1457 | 1.79 | 75.5224 | 2.3174 |
| 601600.SH | 中国铝业 | aluminum | 9.85 | 2.4974 | 17.9641 | -10.4545 | -18.5277 | 18.642 | 3.4528 | 1.05 | 11.5217 | 2.0953 |
| 002155.SZ | 湖南黄金 | precious_metals | 25.78 | 2.505 | 8.5017 | 1.0584 | -11.5609 | 21.1464 | 3.6559 | 1.27 | 23.0041 | 4.624 |
| 002237.SZ | 恒邦股份 | precious_metals | 14.25 | 2.518 | 10.9813 | -0.766 | -8.183 | 13.8411 | 2.745 | 1.34 | 30.8354 | 1.5123 |
| 600219.SH | 南山铝业 | aluminum | 4.84 | 2.5424 | 18.6275 | -6.9231 | -14.7887 | 20.1018 | 3.6618 | 1.08 | 13.4493 | 1.0909 |
| 000960.SZ | 锡业股份 | zinc_lead_tin | 40.34 | 2.7771 | 10.6722 | 10.6418 | -13.4335 | 34.8797 | 5.2173 | 1.06 | 28.4351 | 3.2036 |
| 000975.SZ | 山金国际 | precious_metals | 26.35 | 3.4957 | 31.5527 | 11.4165 | 0 | 51.7282 | 4.0253 | 0.89 | 19.8973 | 4.4989 |
| 000878.SZ | 云南铜业 | copper | 17.22 | 3.7349 | 12.9921 | -3.6374 | -12.2771 | 16.328 | 3.2992 | 1.74 | 30.9095 | 2.2662 |
| 600489.SH | 中金黄金 | precious_metals | 26.1 | 3.9427 | 28.3186 | 11.9691 | 0 | 39.8107 | 3.8142 | 1.08 | 20.1597 | 3.8575 |
| 300723.SZ | 一品红 | 化学制药 | 37.99 | 4.1964 | -4.4277 | -0.4976 | -13.4821 | 12.1501 | 3.8109 | 1.75 | 85.8022 | 8.8649 |

## Recent Company Event Check
| ann_date | title | url |
| --- | --- | --- |
| 20260803 | 关于全资子公司参与第十二批国家药品集中采购拟中标的公告 | https://static.cninfo.com.cn/finalpage/2026-08-03/1225453066.PDF |

## News & Rumor Probe
| grade | topic | source_type | source | published | title | rationale | link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirmed | company_event | official_announcement | CNINFO/Tushare announcement | 20260803 | 关于全资子公司参与第十二批国家药品集中采购拟中标的公告 | Official announcement; hard evidence for event existence, not automatically the cause of the price move. | https://static.cninfo.com.cn/finalpage/2026-08-03/1225453066.PDF |

## News Probe Notes
- tushare_major_news: no matching rows or unavailable (Empty DataFrame
Columns: []
Index: []).
- tushare_news_feed: no matching rows or unavailable (Empty DataFrame
Columns: []
Index: []).
- web_search 一品红 大跌 原因: skipped low-signal result Лерканидипин - 33 отзыва и рейтинг покупателей | Мегаптека.р.
- web_search 一品红 大跌 原因: skipped low-signal result Лерканидипин-СЗ — 91 отзыв покупателей, рейтинг 4.9.
- web_search 一品红 大跌 原因: skipped low-signal result Лерканидипин - 10 отзывов, инструкция по применению.
- web_search 一品红 下跌 传闻: skipped low-signal result 知乎知学堂 - 知乎.
- web_search 一品红 下跌 传闻: skipped low-signal result 有没有大佬帮我解释一下AI infra到底是干啥的？ - 知乎.
- web_search 一品红 下跌 传闻: skipped low-signal result Je suis vs. J'ai - French Q & A | KwizIQ French.
- web_search 化学制药 板块 大跌 原因: skipped low-signal result 硕士专业目录_中国研究生招生信息网.
- web_search 化学制药 板块 大跌 原因: skipped low-signal result 中国研究生招生信息网.
- web_search 化学制药 板块 大跌 原因: skipped low-signal result 专业知识库 - 中国研究生招生信息网.

## Mispricing Decision Gate
- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.
- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.
- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.
- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.