# Dividend defensive verification context for 002475.SZ as of 2026-06-07

Status: not_applicable
Defensive Dividend Rating: not_applicable
- Company: 立讯精密
- Industry: 元器件
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
| dv_ttm | 0.5213 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.1635 | Lower variation implies more predictable dividends. |
| recent_cut | True | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260605 | 68.77 | 29.1044 | 5.6719 | 0.5213 | 50105727.1455 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.28 | 2 |
| 20250930 | 0.4799 | 3 |
| 20250630 | 0 | 1 |
| 20241231 | 0.5999 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.8989 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 332344443143.39 | 16599769785.64 | 17325329533.97 | 17904337668.17 | 3464040516.48 | -579008134.2 | 0.2087 |
| 20241231 | 268794737612.58 | 13365651026.16 | 27116908208.53 | 12110699704.87 | 3717457760.53 | 15006208503.66 | 0.2781 |
| 20231231 | 231905459829.83 | 10952656702.16 | 27605060411.16 | 11387449010.98 | 2530927017.73 | 16217611400.18 | 0.2311 |
| 20221231 | 214028394291.44 | 9163104849.54 | 12727610319.34 | 13584140261.73 | 1796754390.9 | -856529942.39 | 0.1961 |
| 20211231 | 153946097790.4 | 7070520386.57 | 7284766917 | 12567222230.86 | 1399755112.12 | -5282455313.86 | 0.198 |

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
- stock_basic universe unavailable: stock_basic unavailable: configured_http_url: ip超限，请不到在多个ip同时使用