# Dividend defensive verification context for 600660.SH as of 2026-06-16

Status: triggered
Defensive Dividend Rating: strong
- Company: 福耀玻璃
- Industry: 汽车配件
- Dividend stability: watch
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: pass
- Dividend trap risk: low

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 4.1461 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0683 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260616 | 50.65 | 14.6967 | 3.3771 | 4.1461 | 13218350.8275 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 3.6 | 3 |
| 20250630 | 2.7 | 3 |
| 20241231 | 5.4 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 3.9 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 45787435563 | 9312304150 | 12055090552 | 6164082209 | 7314773596 | 5891008343 | 0.7855 |
| 20241231 | 39251657267 | 7497976123 | 8562187329 | 5480872166 | 3713615661 | 3081315163 | 0.4953 |
| 20231231 | 33160996641 | 5629256054 | 7624580890 | 4474711099 | 3596607894 | 3149869791 | 0.6389 |
| 20221231 | 28098754166 | 4755595541 | 5893041655 | 3130253387 | 2907622437 | 2762788268 | 0.6114 |
| 20211231 | 23603063361 | 3146167091 | 5677009641 | 2328511864 | 2277802231 | 3348497777 | 0.724 |

## Same-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603049.SH | 中策橡胶 | 汽车配件 | 4145061.744 | 9.8328 | 1.6219 | 2.7426 | 4.8428 | 2.6161 | 5.9108 | 52.4985 | 75 |
| 600660.SH | 福耀玻璃 | 汽车配件 | 13218350.8275 | 14.6967 | 3.3771 | 4.1461 | 4.4631 | 2.5744 | -15.6769 | 46.6335 | 73 |
| 601058.SH | 赛轮轮胎 | 汽车配件 | 4047651.4693 | 11.433 | 1.8057 | 2.6807 | 4.7983 | 2.7971 | 1.7166 | 51.2359 | 68 |
| 000338.SZ | 潍柴动力 | 汽车配件 | 24349288.4706 | 21.5377 | 2.5532 | 2.5164 | 3.2727 | 1.3243 | 13.8311 | 64.157 | 64.5 |
| 600741.SH | 华域汽车 | 汽车配件 | 5198841.876 | 7.2471 | 0.7633 | 4.8514 | 1.8394 | 0.8823 | -2.6273 | 62.1208 | 60.5 |
| 601689.SH | 拓普集团 | 汽车配件 | 10553875.5988 | 38.164 | 4.2922 | 0.8068 | 2.2668 | 1.6405 | -2.4171 | 40.7749 | 48.5 |
| 002920.SZ | 德赛西威 | 汽车配件 | 5289520.8259 | 22.6743 | 3.4893 | 1.4036 | 3.0185 | 1.8864 | -20.7404 | 49.3564 | 48.5 |
| 002126.SZ | 银轮股份 | 汽车配件 | 4277217.6111 | 44.6042 | 5.7177 | 0.2347 | 2.8707 | 1.3421 | 0.793 | 62.5238 | 31.5 |
| 000559.SZ | 万向钱潮 | 汽车配件 | 4571879.2336 | 46.2211 | 5.2079 | 1.4503 | 2.8197 | 1.2475 | -15.8382 | 64.5321 | 30.5 |
| 301656.SZ | 联合动力 | 汽车配件 | 4658079.9733 | 54.5464 | 4.8286 | 0.222 | 0.5044 | 0.0589 | -85.1996 | 60.9801 | 20 |

## Cross-Industry Defensive Alternatives
| ts_code | name | industry | total_mv | pe_ttm | pb | dv_ttm | roe | roa | netprofit_yoy | debt_to_assets | defensive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 601857.SH | 中国石油 | 石油开采 | 182105872.911 | 11.5123 | 1.121 | 4.7236 | 3.0108 | 2.4513 | 1.8588 | 39.5841 | 65.6 |
| 600938.SH | 中国海油 | 石油开采 | 148626166.158 | 11.9222 | 1.7755 | 4.0652 | 4.7741 | 4.6076 | 7.059 | 27.0925 | 64.4 |
| 600036.SH | 招商银行 | 银行 | 97272944.4792 | 6.4527 | 0.859 | 7.8118 | 2.9627 | N/A | 1.518 | 90.4294 | 63.8 |
| 600519.SH | 贵州茅台 | 白酒 | 156968996.2672 | 18.9771 | 5.7945 | 4.12 | 10.5687 | 11.9998 | 1.4714 | 12.1227 | 57.5 |
| 600028.SH | 中国石化 | 石油加工 | 60099980.5574 | 16.9053 | 0.7214 | 4.5914 | 2.0447 | 1.2593 | 28.2117 | 55.8931 | 57.5 |
| 601318.SH | 中国平安 | 保险 | 95952394.958 | 7.2262 | 0.9423 | 5.0953 | 2.479 | N/A | -7.3808 | 89.8779 | 55.9 |
| 601088.SH | 中国神华 | 煤炭开采 | 92223474.6436 | 17.8842 | 1.9177 | 6.8622 | 2.3971 | 2.3774 | -10.7289 | 29.0313 | 55.6 |
| 600941.SH | 中国移动 | 电信运营 | 201596878.2252 | 14.8445 | 1.4169 | 5.0583 | 2.084 | 1.759 | -4.2082 | 33.7319 | 54.7 |
| 600900.SH | 长江电力 | 水力发电 | 66529083.9263 | 18.4378 | 2.9192 | 3.4682 | 3.01 | 1.8364 | 30.5016 | 57.3271 | 50.6 |
| 601398.SH | 工商银行 | 银行 | 264453442.7682 | 7.1215 | 0.6707 | 4.1819 | 2.0286 | N/A | 3.3093 | 92.1901 | 50.6 |

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- No retrieval errors recorded.