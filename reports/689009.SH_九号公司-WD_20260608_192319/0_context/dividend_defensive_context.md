# Dividend defensive verification context for 689009.SH as of 2026-06-08

Status: triggered
Defensive Dividend Rating: strong
- Company: 九号公司-WD
- Industry: 摩托车
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
| dv_ttm | 4.0747 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 7 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.1137 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260608 | 36.95 | 17.9487 | 3.6444 | 4.0747 | 2701941.1114 |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 12.514 | 1 |
| 20250630 | 12.6673 | 3 |
| 20241231 | 13.572 | 3 |
| 20240630 | 0 | 1 |
| 20231231 | 0.8505 | 3 |
| 20230630 | 0 | 1 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 21277876666.95 | 1758171535.84 | 4444116067.49 | 1221181361.89 | 1104050264.95 | 3222934705.6 | 0.628 |
| 20241231 | 14195808623.28 | 1084126917.88 | 3353676329.25 | 546380055.82 | 199875599.15 | 2807296273.43 | 0.1844 |
| 20231231 | 10222083359.99 | 597994833.29 | 2319465051.8 | 826695461.17 | N/A | 1492769590.63 | N/A |
| 20221231 | 10124318048.95 | 450553095.67 | 1589096254.56 | 433201319.27 | 653179.04 | 1155894935.29 | 0.0014 |
| 20211231 | 9146053585.08 | 410598753.65 | -161451665.8 | 266351997.62 | 3958412.35 | -427803663.42 | 0.0096 |

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