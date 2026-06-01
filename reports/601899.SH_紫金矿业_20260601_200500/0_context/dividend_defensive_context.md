# Dividend defensive verification context for 601899.SH as of 2026-06-01

Status: triggered
Defensive Dividend Rating: medium
- Company: 紫金矿业
- Industry: 铜
- Dividend stability: watch
- Dividend coverage: watch
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
| dv_ttm | N/A | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 25 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | 1.0233 | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| N/A | N/A | N/A | N/A | N/A | N/A |

## Annual Dividend History
| end_date | cash_div_tax_sum | events |
| --- | --- | --- |
| 20251231 | 0.38 | 1 |
| 20250630 | 0.44 | 2 |
| 20241231 | 0.84 | 3 |
| 20240630 | 0.2 | 2 |
| 20231231 | 0.6 | 3 |
| 20230630 | 0.15 | 3 |

## Profit And Cash-Flow Coverage
| end_date | total_revenue | n_income_attr_p |
| --- | --- | --- |
| 20251231 | 349079082852 | 51777327785 |
| 20241231 | 303639957153 | 32050602437 |
| 20231231 | 293403242878 | 21119419571 |
| 20221231 | 270328998459 | 20042045977 |
| 20211231 | 225102488592 | 15672870591 |

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