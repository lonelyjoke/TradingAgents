# Dividend defensive verification context for 002714.SZ as of 2026-06-08

Status: not_applicable
Defensive Dividend Rating: not_applicable
- Company: 牧原股份
- Industry: 农业综合
- Dividend stability: not_applicable
- Dividend coverage: not_applicable
- Industry durability: not_applicable
- Valuation buffer: not_applicable
- Dividend trap risk: not_applicable

## Routing Instruction
- This layer did not find enough dividend/defensive evidence to treat the target as a defensive dividend asset.
- Do not force a high-dividend or cash-cow thesis unless another supplied context provides direct evidence.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | N/A | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 22 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.3213 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260608 | 34.15 | 20.1563 | 2.3518 | N/A | 19714781.3707 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 1.281 | 3 |
| 20250630 | 1.8595 | 2 |
| 20241231 | 1.7183 | 3 |
| 20240930 | 2.4968 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0 | 2 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 144144965371.68 | 15486891254.04 | 30056186914.47 | 9528929651.93 | 10344664907.19 | 20527257262.54 | 0.668 |
| 20241231 | 137946892076.87 | 17881260485.27 | 37543066214.49 | 12380725812 | 8255880276.03 | 25162340402.49 | 0.4617 |
| 20231231 | 110860727714.4 | -4263280820.31 | 9892816863.72 | 17015725403.56 | 7747123200.88 | -7122908539.84 | 1.8172 |
| 20221231 | 124826212177.74 | 13266156512.39 | 23010550801.93 | 15738918946.02 | 4190777891.87 | 7271631855.91 | 0.3159 |
| 20211231 | 78889870566.4 | 6903777691.92 | 16295026813.82 | 35852334356.78 | 8966972376.87 | -19557307542.96 | 1.2989 |

## Same-Industry Defensive Alternatives
No data returned.

## Cross-Industry Defensive Alternatives
No data returned.

## Analyst Instructions
- Output a verdict: true defensive dividend candidate, dividend-trap risk, better substituted by peers, or not applicable.
- For banks, prioritize capital adequacy, NPL/provision risk, NIM pressure, and payout constraints; do not use industrial FCF rules mechanically.
- For consumer/blue-chip cash cows, require stable margins, cash conversion, brand/channel durability, and moderate reinvestment needs.
- Use the peer tables to name at least one better-quality or better-yield alternative when the evidence supports it; otherwise say no sampled peer clearly improves the setup.
- For portfolio construction, separate core defensive yield, quality growth with lower yield, and higher-yield but higher-risk substitutes.

## Coverage Notes
- peer tables need daily_basic market snapshot.