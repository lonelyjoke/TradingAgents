# Forward Forecast Model Scaffold for 600426.SH as of 2026-08-02

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 8343592884.31 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 22.2802% / +5.93pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.9018% / +0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.7977 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 0.3245% / -0.20pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 4.9801% / +0.04pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 化肥产品 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| 化肥产品 | period=annual filing; revenue=7305674635.46 filing table unit not explicit in extracted row; revenue_weight=100.0%; growth=0.12%; gross_margin=32.3% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 化肥产品 | revenue_weight=100.0%; growth=0.12%; gross_margin=32.3%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | What are the revenue and profit splits by product? The filing only gave fertilizer segment; we need the other three material segments (new energy/new materials, organic amines, acetic acid) to assess profit pool quality and growth drivers.; How much capex is growth vs maintenance? The Q1 2026 balance sheet shows net fixed assets ~33 bn; without capex details, FCF projections are rough.; What is the cost curve position in caprolactam and adipic acid? This determines how much margin expansion is sustainable as industry utilization rises.; What is the sensitivity to coal prices? Need consumption per tonne and realized coal price to build a cash-cost model. |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | Based on 2025 reported data, 化肥 contributed only 23.6% of total revenue with a 32.3% gross margin, implying significant other segments. The qualitative descriptions indicate 新能源新材料 (caprolactam, adipic acid, nylon 6) is the largest and most cyclical, likely contributing >40% of revenue. 有机胺 likely has high margins and stable profits, but small scale. 醋酸及衍生品 is a swing factor. Prioritize modeling 新能源新材料 with a volume x spread approach, then 化肥 as a stable base, and treat 有机胺/醋酸 as margin enhancers. Valuation depends critically on caprolactam/adipic acid spreads. |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | In 化肥, HLS competes with other coal-based urea producers on cost but is protected by transport advantages and some policy favoritism. In 新能源新材料, the landscape is more competitive with large players also expanding. However, coal-based routes provide HLS a structural cost edge over naphtha-based peers globally. Substitution risk exists from bio-based chemicals and alternative materials, but is currently distant. New entrants are limited by policy, but existing competitors could still add capacity, intensifying price wars. The company's relative position is strong due to scale, integration, and project execution track record. |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | Management claims of '6-10 bn profit uplift from Dezhou upgrade' (KPE01) and '底部利润 30e 增厚至 50e以上' are unverifiable without cost breakdowns. We partially quantified bull scenario by assuming high margin new products. The Jingzhou project revenue of ~5 bn is a placeholder; actual contribution could be modeled once product volumes and margins are disclosed. Coal cost sensitivity is not quantified because we lack unit consumption; we must retrieve technical coefficients before building a deterministic bottom-up model. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | The market price of CNY 21.55 implies a P/E of ~16x on 2025 earnings, or ~12.5x on 2026E base case. This is above the 5-year median but still below the 73rd percentile PE. It appears the market is pricing in some recovery but not a full bull case. Private channel checks (KPEs) are much more bullish, projecting trough profit of CNY 3-3.5 bn rising to >5 bn, which would imply 2026E EPS ~1.8-2.0 CNY and a fair value of 23-26 CNY. The gap is mainly about the speed and magnitude of the margin recovery in caprolactam/adipic acid and the success of Jingzhou. Our model's base case EPS is lower because we assume only modest 100 bp gross margin improvement. The market may be pricing a 'scenario' close |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | Red team against bull thesis: The industry is still in overcapacity; any capacity discipline can break quickly. HLS's growth plan (TDI, oxalic acid) could destroy value if demand for these products is weaker than expected. Coal cost may surge if China's industrial activity rebounds. The stock at 16x P/E is not cheap for a cyclical with heavy capex risk. The bull case relies on oil staying high, which is geopolitically uncertain.; Red team against bear thesis: Even in a bear case, HLS has shown it can generate positive FCF and maintain gross margins >20%. Its asset base is irreplaceable; new entrants are effectively banned. The fertilizer business provides a floor. Any recovery in global manu |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | We used a probability-weighted PE approach with three scenarios. The base case uses 12.5x 2026E EPS, which is a 20% discount to the current TTM PE, reflecting that the market may be too optimistic about the speed of recovery. Bull case 14x 2028E EPS reflects durable earnings power if new projects execute well. Bear case 10x trough EPS. The weighted fair value of 19.82 is below current price, indicating the stock may be slightly overvalued based on our conservative estimates. However, if one believes the bull scenario probability is higher (say 40%), fair value would rise to ~21 CNY, close to current price. Key sensitivity: +1% in long-term growth rate or +0.5x multiple changes value by ~1.5  |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | Huaren Hengsheng is a high-quality chemical conglomerate with a cost advantage that should widen in the coming years as new capacities ramp and oil prices stay elevated. However, the market already awards a premium multiple to this recovery story. Our model suggests current price of CNY 21.55 implies a successful execution of Jingzhou and sustained margin improvement; there is limited margin of safety. Investors should watch for detailed segment revenue and margin data in the upcoming semi-annual report to validate the bull thesis. A conservative entry point would be closer to probability-weighted fair value of ~CNY 19.8, while a more aggressive view would require confidence in the bull case |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE02 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | model conflict result and accepted/rejected reason |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 8343592884.31 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 22.2802% / +5.93pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 13.3826% / +4.29pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.9018% / +0.21pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.7977 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 华鲁恒升2026年一季度报告: 1,112,802,620.71 703,113,957.51 58.27 经常性损益的净利润 经营活动产生的现金流量净额 890,668,396.41 930,375,592.80... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 华鲁恒升2026年一季度报告: 1,112,802,620.71 703,113,957.51 58.27 经常性损益的净利润 经营活动产生的现金流量净额 890,668,396.41 930,375,592... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 华鲁恒升2026年一季度报告: 其他非流动金融资产 投资性房地产 固定资产 32,889,707,075.45 32,993,654,001.92 / constr... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | asp_or_price | 2025, 年度 | / mdna_text_change / Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. / risk_language_upgrade: 华鲁恒升2025年年度报告: 二、报告期内公司所处行业情况 2025 年，全球经济增长放缓，行业内卷和结构性产能过剩与需求偏弱的矛盾依然存在，化工 市场景气度较低，化工产品价格低谷震荡，企业盈... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 华鲁恒升2026年一季度报告: 净敞口套期收益（损失以“-”号填列） 公允价值变动收益（损失以“-”号填列） 9,246.58 信用减值损... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 华鲁恒升2026年一季度报告: 交易性金融资产 50,009,246.58 衍生金融资产 应收票据 36,455,065.71 18,372,770.00 / receivables: 华鲁恒升2026年一季度报告: 衍生金融资产 应收票据 36,455,065.71 18,372,770... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 华鲁恒升2025年年度报告: 数为基数，向全体股东每10股派发现金红利2.50元（含税），以资本公积每10股转增3.00股；... |
| EV045 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 15.9081 / earnings multiple the market is paying now / |
| EV046 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 1.8789 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 0.3245% / -0.20pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |
| EV010 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Inventory / revenue / 4.9801% / +0.04pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 化肥产品 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=7305674635.46 (filing table unit not explicit in extracted row); revenue weight=100.0%; growth=0.12%; gross margin=32.3%; margin change=2.4pp; source=filing_intelligence; mode=deterministic_filing_row |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 59261271650 / current equity value / / / PE TTM / 15.9081 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: Only the 化肥 segment has reported revenue, cost, and gross margin from the 2025 annual report; other material segments (新能源新材料, 有机胺, 醋酸及衍生品) lack quantitative segment data in the supplied evidence.; Product-level capacity, utilization, ASP, and unit cost evidence is absent for all segments, limiting the operating model to consolidated volume/price/cost assumptions.; Cash flow and balance sheet items (capex, OCF, FCF) were extracted only from Q1 2026 data; full-year 2025 cash flow statements are referenced but not fully reproduced in the evidence payload.; No analyst consensus or broker estimates are supplied; the model relies entirely on reported financials and private channel checks that remain unverified.; Material segment three-year driver lines are missing: 化肥产品; Parent-profit/EPS/share-count conflict corrected for year_1_value.; Parent-profit/EPS/share-count conflict corrected for year_2_value.; Parent-profit/EPS/share-count conflict corrected for year_3_value.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Σ (segment_product_volume x realized_ASP_x_mix) + by-product and energy sales (electricity/steam)
- Profit: Revenue - coal/feedstock cost - energy and freight - conversion labor/overhead - depreciation - period expenses (selling, G&A, R&D, finance). Operating leverage is high due to fixed asset intensity.
- Cash flow: Operating profit + depreciation - change in working capital (receivables, inventory, payables) - capex (sustaining + growth) - tax - interest +/- financing
- Reinvestment: Highly asset-intensive: gross PP&E was CNY ~33 bn at end-Q1 2026. Ongoing growth capex in Jingzhou new-material base and Debang upgrading projects; maintenance capex is significant.

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| UQ1 | What are the actual 2025 revenue, volume, and gross profit contributions of 新能源新材料, 有机胺, and 醋酸及衍生品 segments? | Unresolved: only 化肥 product data was extracted from filing; other segments are unquantified. | segment revenue mix, segment gross margin, consolidated revenue growth | Revenue, Gross profit, EPS | Full product revenue/cost table from 2025 annual report; Retrieve 2025 annual report, extract '主营业务分产品情况' table with all product line revenues, costs, growth rates, gross margins. |
| UQ2 | What are the expected capex outlays for 2026-2028, and how much is growth vs. maintenance? | Unresolved: no capex guidance disclosed; Q1 2026 cash flow shows 1.11 bn OCF but capex not separated. | capex, FCF, net debt | Capital expenditures, Free cash flow, Interest expense, EPS | Capex guidance from management or filings; Review 2025 annual report disclosures on capital commitments, budget for 2026, and '在建工程' details; check investor presentation slides. |
| UQ3 | What is the company's realized coal cost structure and its sensitivity to thermal/anthracite coal price changes? | Unresolved: no coal grade, sourcing mix, or unit consumption data available. | unit coal cost, gross margin, operating profit | Cost of goods sold, Gross profit, EPS | Coal procurement price (CNY/t) and consumption intensity (t/t product); Obtain provincial anthracite/thermal coal price indices and match with company's sourcing region; check annual report for any coal cost commentary. |
| UQ4 | What is the trajectory of caprolactam and adipic acid spreads, and how do Jingzhou new capacities affect volume mix by 2028? | Partially known: prices have recovered from 2025 lows (KPE02), but absolute spread and company's cost position are unknown. | segment volume growth, segment gross margin, revenue | Revenue, Gross profit, EPS | Detailed product-wise volume/price/margin projections; Track weekly product prices and compare with company's reported quarterly gross margin to infer spread; monitor Jingzhou ramp-up announcements. |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 30968.88 | 34066.0 | 36791.0 | 39326.0 | Base revenue grown at 10% YoY (2026E), 8% (2027E), 7% (2028E) reflecting new capacity ramp and modest price recovery | estimated | ±1% revenue growth changes 2026E revenue by ~309 mn; segment-level volume and ASP forecast |
| consolidated | Gross margin | % | 22.28 | 23.5 | 24.0 | 24.0 | Assume 122 bp improvement in 2026E from cost absorption and better product mix, stabilizing thereafter | estimated | ±1 pp gross margin changes 2026E gross profit by ~341 mn; Product-level margins |
| consolidated | Operating profit | CNY mn | 3315.49 | 4010.0 | 4450.0 | 4750.0 | Revenue x operating margin (11.77% in 2026E) – calculated as 34066 x (23.5% GM - ~5.5% SG&A - ~3.0% R&D - ~1.5% finance cost net) = ~11.77% op margin | calculated | ±0.5 pp operating margin changes 2026E operating profit by ~170 mn; detailed expense breakdown forecast |
| consolidated | Parent net profit | CNY mn | 3315.49 | 3694.0 | 4100.0 | 4370.0 | Operating profit - interest (net) - income tax (~15% effective) – minority interest negligible | estimated | ±100 mn net profit moves EPS by ~0.036 CNY; interest expense forecast, tax holidays |
| consolidated | EPS | CNY/share | 1.57 | 1.7462907315830731 | 1.9382219814538713 | 2.0658609899886384 | parent net profit (CNY mn) / diluted shares (mn) | calculated | ±0.10 CNY = ±275 mn parent profit;  |
| consolidated | OCF | CNY mn | None | 3800.0 | 4200.0 | 4500.0 | Roughly 1.0x net profit plus depreciation (estimated at 2,400 mn) minus working capital build | estimated | Not directly driving EPS; FY2025 OCF actual |
| consolidated | Capex | CNY mn | None | -3200.0 | -2900.0 | -2500.0 | Assumed based on Q1 2026 capex run-rate and project timeline; high growth phase | estimated | Higher capex reduces FCF and may require financing; FY2025 capex actual, capex budget |
| consolidated | FCF | CNY mn | None | 600.0 | 1300.0 | 2000.0 | OCF - capex (negative capex added) | calculated | FCF generation capacity determines dividend and reinvestment potential; capex split, working capital |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE02 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE03 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE04 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE05 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE06 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE07 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE08 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE09 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until 产品报价、毛利率、竞品价格、下游接受度、行业价格指数 | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-17T08:17 | 有效窗口/16天 | 未披露 | 德州追求提质增效，计划更换第一平台、二平台的气化炉和净化装置，预计实现约6-10亿利润提升空间，表内增量显著，测算底部利润30e增厚至50e以上，当前底部估值仅11X | 德州追求提质增效，计划更换第一平台、二平台的气化炉和净化装置，预计实现约6-10亿利润提升空间，表内增量显著，测算底部利润30e增厚至50e以上，当前底部估值仅11X | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-07T08:15 | 有效窗口/26天 | 未披露 | 未提取到带期间的明确盈利预测 | 目前龙头万华化学和华鲁恒升的PE约为12倍，PB仅有2.1倍和1.6倍，PB位于2020年以来10%和13%的分位数（按照7月6日收盘价测算） | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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