# Dividend defensive verification context for 603345.SH as of 2026-06-05

Status: triggered
Defensive Dividend Rating: medium
- Company: 安井食品
- Industry: 食品
- Dividend stability: fail
- Dividend coverage: pass
- Industry durability: pass
- Valuation buffer: watch
- Dividend trap risk: medium

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 2.5863 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 0 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | N/A | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260602 | 93.97 | 20.4986 | 1.9508 | 2.5863 | 3131916.094 |

## Annual Dividend History
No data returned.

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p | n_cashflow_act | c_pay_acq_const_fiolta | c_pay_dist_dpcp_int_exp | free_cash_flow_proxy | cash_distribution_to_profit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20251231 | 16192613033.59 | 1359237139.62 | 2316722978.59 | 873464939.66 | 1064864073.2 | 1443258038.93 | 0.7834 |
| 20241231 | 15126651674.36 | 1484831242.06 | 2103844668.23 | 901279791.42 | 929784589.68 | 1202564876.81 | 0.6262 |
| 20231231 | 14045234826.03 | 1478066338.58 | 1955654340.14 | 1444458112.92 | 568996953.26 | 511196227.22 | 0.385 |
| 20221231 | 12182663119.36 | 1101029966.93 | 1407225497.62 | 1073070703.18 | 219286412.48 | 334154794.44 | 0.1992 |
| 20211231 | 9272201669.79 | 682296084.71 | 538203778.55 | 911896509.6 | 195406903.78 | -373692731.05 | 0.2864 |

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