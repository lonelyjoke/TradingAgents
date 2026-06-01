# Dividend defensive verification context for 603605.SH as of 2026-06-01

Status: triggered
Defensive Dividend Rating: weak
- Company: 珀莱雅
- Industry: 日用化工
- Dividend stability: fail
- Dividend coverage: fail
- Industry durability: pass
- Valuation buffer: pass
- Dividend trap risk: high

## Routing Instruction
- Treat high dividend yield as a hypothesis, not proof. Verify profit durability, cash-flow coverage, and payout sustainability before calling it defensive.
- Explicitly test the dividend-trap path: profit decline, free-cash-flow pressure, capital constraints, or industry erosion that would shrink future dividends.
- Compare against the same-industry and cross-industry alternatives below because the user-entered ticker may not be the best defensive expression.

## Dividend And Valuation Snapshot
| metric | value | interpretation |
| --- | --- | --- |
| dv_ttm | 3.203 | Trailing dividend yield from daily_basic; high yield alone is not enough. |
| dividend_years | 0 | Count of recent end_dates with cash_div_tax records. |
| dividend_cv | N/A | Lower variation implies more predictable dividends. |
| recent_cut | False | A material recent cut is a dividend-trap warning. |

## Current Valuation Reference
| trade_date | close | pe_ttm | pb | dv_ttm | total_mv |
| --- | --- | --- | --- | --- | --- |
| 20260529 | 61.81 | 16.6029 | 3.8512 | 3.203 | 2447527.7054 |

## Annual Dividend History
No data returned.

## Profit And Cash-Flow Coverage
No data returned.

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
- stock_basic universe unavailable or missing ts_code.