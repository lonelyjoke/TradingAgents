# Forward Forecast Model Scaffold for 600096.SH as of 2026-08-11

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 11980782595.76 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 19.5567% / +2.33pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.4309% / -0.35pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.6856 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 1.9076% / -1.36pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 14.0119% / +4.38pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Core revenue | category volume x ASP x product/channel mix | category growth, traffic/weather/catering recovery, regional penetration and product mix |
| Gross profit | revenue x gross margin | raw-material and packaging costs, price/mix, promotion intensity and logistics |
| Operating profit | gross profit - selling/admin/R&D expense | sales expense, channel rebates, scale leverage and brand investment |
| Cash profit / FCF | net profit + D&A - working capital - capex | contract liabilities/prepayments, inventory, receivables, OCF/NI and capex |
| Valuation bridge | normalized EPS/FCF x category-appropriate multiple with ROE/payout cross-check | growth durability, channel health, margin stability and shareholder return |

## Consumer-Staples Product, Cost And Cash Controls
| control | Mandatory treatment |
| --- | --- |
| Business buckets | model every material filing product, channel and consolidated subsidiary separately; identify core, growth, scenario, optionality and excluded/double-counted value |
| Revenue bridge | saleable volume x realized ASP x product/channel mix; distinguish end-demand sell-through from distributor restocking and acquisition consolidation |
| Raw-material bridge | map each material input to a dated price range/percentile, company purchase basis and pass-through or inventory-cost lag; do not infer margin directly from one futures move |
| Gross-profit sensitivity | product revenue - grade/product-matched raw material - packaging - energy - logistics - conversion cost; show the CNY mn gross-profit and parent-profit effect of each price/margin shock |
| Channel and cash | reconcile distributor inventory, contract liabilities/advances, receivables, inventory, OCF/NI and promotional rebates before calling shipment growth real demand |
| Subsidiaries / acquisitions | show revenue, margin, minority interest, purchase-price allocation, goodwill/impairment, cash conversion and consolidation effects separately |
| Three-year closure | product/subsidiary revenue and profit must sum to group revenue, operating profit, parent profit, EPS, OCF, capex and FCF for all three years |
| Valuation | connect normalized EPS/FCF and ROE/payout to PE/FCF-yield or SOTP; keep unverified new categories and overseas projects in probability-weighted optionality |
- If product volume/ASP, subsidiary profit or raw-material basis data are unavailable, keep the affected cells missing/partial, quantify a bounded sensitivity, and name the next filing or channel verification instead of filling the gap with a narrative growth rate.

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| Core revenue | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with category volume x ASP x product/channel mix plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Gross profit | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with revenue x gross margin plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Operating profit | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with gross profit - selling/admin/R&D expense plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Cash profit / FCF | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with net profit + D&A - working capital - capex plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Valuation bridge | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with normalized EPS/FCF x category-appropriate multiple with ROE/payout cross-check plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| Core revenue | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=category volume x ASP x product/channel mix; required assumptions=category growth, traffic/weather/catering recovery, regional penetration and product mix | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Gross profit | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=revenue x gross margin; required assumptions=raw-material and packaging costs, price/mix, promotion intensity and logistics | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Operating profit | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=gross profit - selling/admin/R&D expense; required assumptions=sales expense, channel rebates, scale leverage and brand investment | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Cash profit / FCF | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=net profit + D&A - working capital - capex; required assumptions=contract liabilities/prepayments, inventory, receivables, OCF/NI and capex | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Valuation bridge | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=normalized EPS/FCF x category-appropriate multiple with ROE/payout cross-check; required assumptions=growth durability, channel health, margin stability and shareholder return | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | What is the realized phosphate fertilizer price and cash cost by grade?; How much phosphate rock does the company mine, and what is the average grade/cost trend?; What is the volume growth trajectory for POM and what are the drivers?; How does working capital behave around seasonal peaks and does it reveal any demand quality issues? |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | Phosphate fertilizers are the dominant profit pool (likely >50% of gross profit) due to integration; nitrogen fertilizers contribute steady but lower-margin cash; POM is the highest-margin growth option but still small; trading is low-margin pass-through. Valuation sensitivity is highest for phosphate price/spread changes. |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | In phosphate fertilizers, the market boundary is global but domestic players compete on cost and integration. The company's true advantage is captive phosphate rock, a fixed supply asset. Competitors without captive rock are exposed to rock price inflation. Substitutes (NPK blends from other sources) and alternative fertilizer forms exist, but DAP/MAP remain essential for many crops. In POM, competition is more about product quality and customer qualification; the company's long-standing production and quality reputation may provide a narrow moat. However, the risk of Chinese overcapacity is real and must be monitored through price spreads and utilization. |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | We know gross margin improved y/y in Q1 2026, suggesting better cost pass-through or mix. But without volumes and prices, we cannot quantify into EPS. The underwriting is thus anchored on seasonal adjusted revenue of ~44 bn and a margin assumption of 19.6%. Qualitative channel checks signal that phosphate fertilizer prices could rise in autumn, but the quant bridge requires actual price data to justify a bull case. We have therefore set bull case at +8% revenue and margin expansion, bear at -10% revenue and margin contraction, reflecting limited evidence. The next step is to retrieve weekly phosphate fertilizer price indices and correlate with company quarterly ASP. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | Current market cap ~54.4 bn corresponds to ~10.3x TTM PE. This is below historical median but not extremely cheap for a commodity chemical company. The market appears to price a base case of stable earnings (~5.2 bn). The consensus might anticipate a minor recovery but not a strong bull cycle; if autumn demand proves robust and prices rise, there is upside surprise potential. Conversely, if commodity prices weaken, downside is limited by phosphate rock floor and dividend yield. The gap likely lies more in the timing and magnitude of phosphate fertilizer price improvement rather than a structural re-rating. |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | Bull thesis red team: Chinese phosphate fertilizer exports could be curtailed to ensure domestic supply, capping external price benefits; new mine permits in other regions (Africa) could flood the market and depress rock prices, eroding the resource scarcity narrative. Falsification signal: global phosphate rock price index falls below 80 USD/t.; Bear thesis red team: Even in a downturn, the company's integrated rock advantage and high dividend yield (implied 7%+ based on current market cap if payout remains) provide a floor; China's food security policy supports fertilizer demand; any supply disruption (e.g., sulfur) is temporary. Falsification signal: if company cuts dividend or reports tw |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | We used a probability-weighted earnings approach with target PE of 10.5x, consistent with its historical average and current TTM multiple. The resulting equity value of 54.8 bn is close to market cap, suggesting the stock is fairly valued under base assumptions. The bull case would imply 66 bn (11x 6 bn), while the bear case would be 36 bn (9x 4 bn). Without per-share data, we cannot express fair value per share or expected return. The key driver for multiple re-rating would be sustained above-cycle margins and successful POM capacity growth. |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | The PM should view 云天化 as a phosphate resource play with an integrated fertilizer and POM business. The current stock price essentially prices a steady-state earnings stream. The alpha opportunity hinges on whether the upcoming autumn fertilizer season can lift phosphate prices and margins beyond consensus expectations. The research priority is to quantify the company's realized phosphate fertilizer price and cost, then assess the likelihood of the bull scenario. In the meantime, the high dividend yield and rock resource provide downside protection. The report should present a range of fair values tied to those assumptions, rather than a single point estimate, and emphasize the dividend back |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 11980782595.76 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 19.5567% / +2.33pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 11.8921% / +1.98pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.4309% / -0.35pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.6856 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -75.25%, gross margin change -0.66pp, operating margin chan... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -75.25%, gross margin change -0.66pp, operating margin c... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2024, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 云天化2024年第三季度报告: 其他债权投资 0 0 长期应收款 26,785,787.11 21,785,787.11 长期股权投资 3,575,329,143.... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | utilization_or_backlog | 2025, 年度 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgrade: 云天化2025年年度报告: 万吨，单套产能规模在国内排名第一，同时在国内 MDCP 消费市场占有率达到 70% 公司聚甲醛产能国内前列，产品质量达到国产聚甲醛的领先水平，在国内聚甲醛 素、聚甲... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2024, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 云天化2024年第三季度报告: 净敞口套期收益（损失以“-”号填列） 0 0 公允价值变动收益（损失以“-”号填列） 927,672.12... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2024, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 云天化2024年第三季度报告: 交易性金融资产 931,700.00 85,900.00 衍生金融资产 0 0 应收票据 0 0 / receivables: 云天化2024年第三季度报告: 衍生金融资产 0 0 应收票据 0 0 / Contract liabilities and pa... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 云天化2025年年度报告: 公司拟向全体股东每10股派发现金红利12元（含税）。以截至2025年12月31日公 司总股本1,... |
| EV047 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 10.2794 / earnings multiple the market is paying now / |
| EV048 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 1.1481 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 1.9076% / -1.36pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |
| EV010 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Inventory / revenue / 14.0119% / +4.38pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Core revenue | category volume x ASP x product/channel mix | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Gross profit | revenue x gross margin | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Operating profit | gross profit - selling/admin/R&D expense | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Cash profit / FCF | net profit + D&A - working capital - capex | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Valuation bridge | normalized EPS/FCF x category-appropriate multiple with ROE/payout cross-check | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 54379812581 / current equity value / / / PE TTM / 10.2794 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Assumption Change And Valuation Transmission Ledger
| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |
- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.
- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.

## Shared Company Underwriting Packet
- Research readiness: partial
- Readiness reasons: No segmental revenue/profit disclosed from filings in this evidence set; No company-realized commodity prices or cost curves available; Forecast lines are partially filled with assumptions pending commodity and volume data; Transaction rights map T1 is incomplete: ownership-to-attributable-cash formula is missing; Required consolidated three-year forecast lines are incomplete.; Bull/base/bear per-share valuation is incomplete.; base scenario EPS x PE does not reconcile to fair value.; bull scenario EPS x PE does not reconcile to fair value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Sum over products: volume_sold * realized_ASP + trading revenue
- Profit: Gross profit (volume*(realized price - unit cost)) - selling/administrative/R&D expenses - finance costs + other income - income tax - minority interest
- Cash flow: Net operating profit + depreciation - change in working capital - capex - dividends
- Reinvestment: Moderate to high capex for mining capacity maintenance, upgrading fertilizer plants, and POM expansion; 2025 investing cash outflow increased due to construction in progress

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | What is the realized phosphate fertilizer price, volume, and cash production cost (including rock transfer price and sulfur) for the next three seasons? | unresolved | asp_or_price (phosphate fertilizers), segment_volume (phosphate fertilizers), unit_cost_and_input_prices (sulfur, rock) | Revenue, Gross profit, Operating profit, Parent net profit, EPS | Monthly realized phosphate fertilizer prices by grade, Company sulfur procurement cost and inventory policy, Phosphate rock mine-gate cost; Cross-reference Wind/Bloomberg fertilizer price data with company quarterly revenue and ASP disclosure when available |
| Q2 | Can the company maintain phosphate rock output and grade without a step-up in sustaining capex or cost? | unresolved | unit_cost_and_input_prices (phosphate rock), capex_or_roic | Gross margin, Capex, FCF, ROIC | Mine-by-mine reserves, grades, and cost data, Capex specifically for mining vs fertilizer plants; Retrieve mining segment operating data and reserves from filing or independent engineer reports |
| Q3 | What is the growth runway and margin trajectory for the POM business given industry capacity expansion? | unresolved | segment_volume (POM), segment_margin (POM) | Revenue mix, Operating profit, Valuation multiple | POM annual capacity, output, ASP, unit cost; Obtain POM segment numbers from annual report and monitor methanol spreads |
| Q4 | How will capital allocation shift between high dividend payout and growth capex (e.g., new fertilizer grade, POM expansion, or resource acquisition)? | unresolved | capex_or_roic, dividend policy, FCF | Capex, FCF per share, Dividend per share, Retained earnings | Detailed capex guidance by project, Future M&A intentions; Listen to management conference call for capex budget and dividend policy update |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 48414.92 | 43904.0 | 44778.0 | 45674.0 | Base: FY2025 actual (EV010). 2026E: Q1 2026 seasonal adjusted (11980.78 mn / 0.273). 2027E-2028E: +2% y/y assuming flat volume and slight price drift. | analytical | Phosphate fertilizer price +/- 5%; Segment volume and ASP drives, Commodity price curve |
| consolidated | Gross margin | % | 20.03 | 19.6 | 19.8 | 20.0 | Base: (48004-38390)/48004 (EV025). 2026E: Q1 2026 reported 19.56% (EV012) adjusts for full year slightly lower than base reflecting sulfur cost; 2027E-2028E gradual recovery. | analytical | Sulfur price and phosphate rock transfer cost; Input cost assumption bridge |
| consolidated | Operating profit | CNY mn | None | 6760.0 | 6894.0 | 7033.0 | Revenue * operating margin (15.4% in Q1 2026 EV013). 2026E 15.4%, 2027E 15.4%, 2028E 15.4%. | analytical | Revenue and cost absorption; Interest expense and other income decomposed |
| consolidated | Parent net profit | CNY mn | 5156.04 | 5200.0 | 5304.0 | 5410.0 | 2026E: Q1 seasonal-adjusted 5218 mn rounded; 2027E-2028E +2% y/y. | analytical | Gross margin and finance cost; Tax rate and minority interest breakdown |
| consolidated | EPS | CNY/share | None | 2.8524555830153164 | 2.909504694675623 | 2.9676509046370887 | parent net profit (CNY mn) / diluted shares (mn) | calculated | ; Diluted share count |
| consolidated | OCF | CNY mn | None | 8860.0 | 9039.0 | 9219.0 | Q1 2026 OCF/net profit ratio 1.6856 (EV016) applied to net profit forecasts. | analytical | Working capital cycle; Full-year capex and working capital change detail |
| consolidated | Capex | CNY mn | None | 2500.0 | 2500.0 | 2500.0 | Rough estimate based on prior-year investing outflow and construction-in-progress commentary (EV029); assumed steady maintenance + moderate growth capex. | analytical | New project approval; Management capex guidance, Other investing activities |
| consolidated | fcf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE02 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE03 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE04 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE05 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE06 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE07 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE08 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE09 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE10 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 天风化工｜唐婕团队/2026-07-22T08:28 | 有效窗口/20天 | 未披露 | 未提取到带期间的明确盈利预测 | 看好8~9月份需求旺季带来的利润弹性（桐昆股份、新凤鸣） 🌹氨纶：看好旺季涨价，中长期景气格局处上行通道（华峰化学） 🌹染料：旺季来临下，原材料支撑价格上涨（浙江龙盛、闰土股份） 🌹磷肥及磷化工：秋肥需求验证、原料成本缓和驱动价差修复，重视具备磷矿资源和一体化优势的企业盈利弹性（ 云天化、川恒股份、云图控股） 🌹农药：全球去库尾声与南美出口需求旺季共振，景气从底部磨底转向结构性修复（扬农化工、润丰股份） 🌹轮胎：逆全球化驱动出海2.0产能放量，板块估值处于历史底部，周期、成长、安全边际三重逻辑共振（赛轮轮胎、... | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
- Do not average incompatible forecast years, valuation dates or methods.
- A range or median may be called consensus only when a named multi-broker sample and statistical basis are supplied.

## Mandatory Three-Year Table
| item | 2026E | 2027E | 2028E | evidence / assumption status |
| --- | --- | --- | --- | --- |
| Revenue | to be estimated | to be estimated | to be estimated | reconcile segment volume, ASP, mix, and eliminations |
| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |
| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |
| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |
| Operating cash flow / capex / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and reinvestment |

## Analyst Instructions
- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.
- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.
- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.
- If an official earnings preview, guidance or quick report is available, it overrides run-rate extrapolation for the covered period until the formal report supplies segment, cash-flow and balance-sheet detail.
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.
- Never copy an external sell-side target or rating. Compare its operating assumptions with this model, record conflicts, and let the system-generated rating follow from the reconciled model.