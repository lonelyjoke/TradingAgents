# Forward Forecast Model Scaffold for 300136.SZ as of 2026-08-21

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 1992215856.05 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 21.7664% / +2.30pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 2.1465% / +1.54pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 0.7722 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 31.6136% / +7.76pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 19.1263% / -1.60pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Equipment revenue | opening backlog + new orders - undelivered backlog; recognized on shipment/acceptance by tool category | customer fab capex, tool demand, installation and acceptance cycle |
| Service / spare-parts revenue | installed base x service attach rate x service ASP | installed base, warranty period, consumables/spares and customer utilization |
| Gross profit | equipment revenue x tool gross margin + service revenue x service margin | product mix, localization, BOM cost, warranty, yield and learning curve |
| Operating profit | gross profit - R&D - selling/admin - credit impairment | R&D platform investment, demo tools, customer support and scale leverage |
| Parent net profit / EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | advances, inventory, receivables, acceptance timing, capex and share count |
| Valuation bridge | order-backed DCF/EV-EBITDA + SOTP for tool categories, cross-checked with PE only after backlog conversion | backlog quality, domestic substitution rate, customer capex cycle and ROIC |

## Semiconductor Forecast And Valuation Controls
- Semiconductor profile: semiconductor equipment / wafer-fab tools. Use this profile before consumer, generic technology, telecom, metals, or battery templates.
| control | Mandatory treatment |
| --- | --- |
| Business buckets | split mature/core products from product-cycle, technology-node, customer, or tool-category optionality; do not bury optionality inside the base multiple |
| Operating bridge | start from sector-native volume x ASP x mix, then explicitly bridge gross margin, R&D, working capital, capex and share count |
| Foundry / manufacturing | use wafer capacity, utilization, wafer ASP, node mix, yield, depreciation, capex, construction-in-progress transfer, and equipment access |
| Chip design | use shipments, ASP, design wins, tape-out/mass-production milestones, customer concentration, foundry/package cost, inventory and R&D/IP moat |
| Semiconductor equipment | use new orders, backlog, delivery/acceptance, tool-category mix, localization rate, installed base/service, inventory, advances and receivables |
| Valuation triangulation | PE is only one cross-check. Also show EV/EBITDA, DCF/FCF, ROIC/PB or SOTP/NAV depending on asset intensity and disclosure |
| Optionality discipline | AI, advanced node, localization or strategic-scarcity value must have explicit probability, payoff, verification gate and overlap key; unverified optionality cannot enter base value |
| Market-implied check | reverse current market cap into required revenue, gross margin, net profit, ROIC, backlog conversion or node/product contribution; compare with the model |
- A semiconductor Buy/Underweight call is incomplete if it relies only on static PE/PB or valuation percentiles without the operating bridge above.

## Business-Line Qualitative And Quantitative Underwriting Agenda
- Start with the company's financial-report revenue composition. Prioritize high-revenue-weight or thesis-critical segments; do not impose a fixed industry checklist when the filing discloses different economics.
- For each selected segment, use the LLM to form company-specific questions from that segment's product, customer, procurement decision, substitutes, true peers, pricing mechanism, cost stack, delivery cycle and cash-collection pattern.
| business line selected from filing revenue mix | disclosed financial anchor | qualitative baseline required even when data are missing | quantitative upgrade when evidence exists |
| --- | --- | --- | --- |
| Equipment revenue | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with opening backlog + new orders - undelivered backlog; recognized on shipment/acceptance by tool category plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Service / spare-parts revenue | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with installed base x service attach rate x service ASP plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Gross profit | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with equipment revenue x tool gross margin + service revenue x service margin plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Operating profit | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with gross profit - R&D - selling/admin - credit impairment plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
| Parent net profit / EPS / FCF | no structured filing segment extracted; industry-driver fallback | Ask the LLM to infer the relevant business-specific questions from the available company description, industry context and peer evidence, then state that the revenue-mix source is missing. | Quantify with operating profit - tax/minority + working-capital/capex bridge plus margin/profit/cash/valuation contribution only when evidence exists; otherwise keep the answer qualitative and add a retrieval task for filing segment revenue mix. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| Equipment revenue | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=opening backlog + new orders - undelivered backlog; recognized on shipment/acceptance by tool category; required assumptions=customer fab capex, tool demand, installation and acceptance cycle | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Service / spare-parts revenue | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=installed base x service attach rate x service ASP; required assumptions=installed base, warranty period, consumables/spares and customer utilization | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Gross profit | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=equipment revenue x tool gross margin + service revenue x service margin; required assumptions=product mix, localization, BOM cost, warranty, yield and learning curve | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Operating profit | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=gross profit - R&D - selling/admin - credit impairment; required assumptions=R&D platform investment, demo tools, customer support and scale leverage | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
| Parent net profit / EPS / FCF | filing segment mix missing; use as fallback driver only | Demand/competition/profitability/cash-flow questions must be generated from company and peer context; driver formula=operating profit - tax/minority + working-capital/capex bridge; required assumptions=advances, inventory, receivables, acceptance timing, capex and share count | Do not claim a profit-pool ranking until segment revenue/margin/cash evidence is retrieved; use expectation gap and valuation transmission only as bounded scenarios |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | Which disclosed product line contributes revenue and gross profit, and how much is consumer electronics vs MLCC vs satellite?; Does MLCC qualification evidence align with audit-proof orders: customer code, volume, ASP, capacity, yield?; Do commercial aerospace catalysts produce company-specific backlog or only peer-list exposure?; Is the Q1 2026 gross margin improvement mix-driven or driven by FX/one-off? |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | The incumbent consumer RF/mobile components likely dominate consolidated revenue and cash generation, but the market is paying for MLCC and satellite optionality. Therefore disclosure priority should be: 1) disclosure of segment revenue/margin; 2) MLCC capacity and customer verification; 3) satellite order evidence; 4) capex/FCF. Without these, the core profit pool remains unreported and the new-business contribution is not independently observable. |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | The true economic boundaries are product-and-customer specific, not the broad '元器件' industry label. Consumer RF/modules compete with international component makers and potentially customer in-sourcing; MLCC competes with Murata and domestic ceramic specialists on qualification, yield, and ASP; satellite ground-terminal components are a separate customer-qualification domain where broker lists are not evidence of orders. The company is positioned as a diversified precision-component supplier but has not supplied share or segment-margin data that would allow competitive position to be quantified. |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | Filing language supports a diversified high-R&D manufacturing model and global customer access, but exact product revenue, volume, price, unit cost, capacity, and cash conversion are missing. Therefore the qualitative story can inform scenario direction but cannot be mechanically converted into segment EPS or FCF. Required retrievals are: segment revenue and gross margin, MLCC capacity/utilization/yield, satellite backlog, capex, and the acquisition target's financials. |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | The market is pricing the shares at roughly 78x TTM PE and 6.3x PS, with PE/PB/PS percentiles near 87%. That suggests the current price already prices substantial recovery or new-business success. The underwriting model's base probability-weighted value is close to the current price, implying the market may already be embedding MLCC/satellite optionality. The gap is less about whether the story is real and more about magnitude and timing: the valuation requires delivery of new-business earnings, not just verification headlines. |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | Bull case is vulnerable to MLCC certification taking multiple customer cycles while international incumbents protect share; falsification signal is no audited MLCC revenue or a customer verification delay.; Bull case assumes commercial aerospace catalysts convert to company orders, but the company has not disclosed satellite order value; falsification signal is no company-attributable satellite revenue in upcoming reports.; Bear case is vulnerable to Q1 2026 being seasonally weak and not reflective of H2 recovery; falsification signal is gross margin staying above 21.77% and OCF/NP holding near 0.77 while H2 revenue rebounds.; Bear case may understate export/FX tailwind and AI-driven content |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | The valuation is a normalized PE bridge on 2027E scenario parent profit. Bull/base/bear are alternative earnings paths with probabilities 30/50/20. The base 85x multiple reflects the current high-valuation regime and optionality; it is not a raw historical average. Without segment-level revenue or FCF, DCF or SOTP is not reliable. The fair value is therefore partial and should be re-run once segment revenue, MLCC capacity, and capex are known. |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | The PM memo should state plainly that Xinwei is a diversified precision-component maker with a stable core and two high-valuation options: high-end MLCC import substitution and commercial satellite ground terminals. It should explain that Q1 2026 improved margin is a useful but segment-ambiguous signal, that the market already prices a large part of the optionality, and that investment debate centers on verification of MLCC orders and company-specific satellite revenue rather than on industry themes. The packet should avoid exposing the evidence ledger and instead present a three-scenario earnings bridge with explicit missing items to be closed. |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE06 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 1992215856.05 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 21.7664% / +2.30pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 5.2649% / +0.82pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 2.1465% / +1.54pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 0.7722 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV026 | financial_report_intelligence | primary_or_structured_filing | reported | scenario_probability | unspecified | / strong / annual/quarterly/semiannual / none / 9/9 / ready / Annual base text and quarterly checkpoint are both present, with broad question coverage; filing read is suitable for thesis formation. / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.64%, gross margin change -1.02pp, operating margin chan... |
| EV031 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 20251231, 20260331 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / visibility_not_yet_profitability: 20251231->20260331: revenue growth -77.64%, gross margin change -1.02pp, operating margin c... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 2026年一季度报告: 其他债权投资 长期应收款 长期股权投资 524,156,667.99 529,536,158.22 / long_term_equity_i... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 2026年一季度报告: 收益 价值变动产生的损益 主要是报告期按照预期信用损失 信用减值损失 2,931,818.32 1,150,359... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 2026年一季度报告: （%） 主要是报告期客户支付的票据增 应收票据 28,089,116.10 15,273,438.94 83.91% / receivables: 2026年一季度报告: 主要是报告期客户支付的票据增 应收票据 28,089,116.10 15,273,438.94... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | revenue | 2025, 年度 | / shareholder_return_authenticity / Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. / generic_capital_allocation: 2025年年度报告: 股东的净利润达到 70,868.63 万元，同比增长 7.12%；扣除股份支付影响后的净利润达到 73... |
| EV036 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 9/9; core pack ready. Annual base text and quarterly chec... |
| EV045 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 78.3695 / earnings multiple the market is paying now / |
| EV046 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 6.2983 / sales multiple the market is paying now / |
| EV009 | earnings_model | primary_or_structured_filing | calculated | revenue | 20260331, 20250331 | / Receivables / revenue / 31.6136% / +7.76pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| Equipment revenue | opening backlog + new orders - undelivered backlog; recognized on shipment/acceptance by tool category | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Service / spare-parts revenue | installed base x service attach rate x service ASP | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Gross profit | equipment revenue x tool gross margin + service revenue x service margin | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Operating profit | gross profit - R&D - selling/admin - credit impairment | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Parent net profit / EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
| Valuation bridge | order-backed DCF/EV-EBITDA + SOTP for tool categories, cross-checked with PE only after backlog conversion | to be estimated | to be estimated | to be estimated | link EV ids; reported / calculated / estimated / proxy / missing |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 57686442198 / current equity value / / / PE TTM / 78.3695 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
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
- Readiness reasons: Filing text confirms product lines and FY2025/Q12026 consolidated financials, but no authoritative segment revenue/margin split is supplied.; Cash-flow detail and capex are missing, so FCF cannot be fully bridged.; The 2026-07-14 acquisition/capital-increase intention agreement is material but lacks consideration, ownership, and consolidation terms.; Most KPE items are unverified private/broker clues and are held at watch_unchanged without quantitative model changes.; Derived share count is based on top-10 holder ratio, not a primary total_share field.; Required consolidated three-year forecast lines are incomplete.; Valuation has not closed from mutually exclusive buckets to per-share fair value.; volume_price_cost driver chain is incomplete; missing: volume
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: Σ(有效产能 × 利用率 × 良率 × 可售出货量 × 实际ASP/产品结构)；分产品未披露；FY2025合并营收8,909.78百万CNY。
- Profit: Σ(出货量 × (ASP - 材料 - 制造成本 - 运费 - 质保)) - 研发/销售/管理费用；产品结构升级淘汰低毛利产品；Q12026合并毛利率21.77%。
- Cash flow: EBITDA - 营运资金变动 - 维护/扩张资本开支 - 税息；Q12026 OCF/净利润=0.7722；全年Capex/FCF缺少证据。
- Reinvestment: 高研发、全球5个主要生产基地和11个研发中心；持续投入高端连接器、散热材料、被动元件和卫星通信；资本开支与回报率尚未量化。

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 2026-07-14披露的《股权收购及增资意向协议》针对信维电科的交易结构、总对价、上市公司自有资金/股份支付、标的财务数据、并表时点和少数股东损益是什么？ | unresolved | transaction_attributable_consideration, ownership_after_pct, consolidation_scope, minority_interest, cash_received | parent_net_profit, goodwill, minority_interest, FCF | transaction consideration, ownership before/after, target financials, closing timeline; 获取股权收购及增资意向协议正式方案与审计报告 |
| Q2 | 高端MLCC北美大客户验证能否转化为合格供应商编码、爬坡订单和可视化收入；当前产能/良率/ASP/单位成本如何支撑毛利率？ | unresolved | MLCC revenue, MLCC capacity_utilization, MLCC ASP, MLCC gross_margin, customer_qualification_status | revenue, gross_margin, parent_net_profit, EPS | passive component revenue, qualified SKU list, capacity, yield, ASP, unit cost; 检索定期报告/公告中的MLCC收入、客户验证里程碑、产能和单位成本 |
| Q3 | 商业卫星通信/地面终端业务是否已形成实际订单、交付和可归属收入；朱雀三号回收成功后，公司能否获得增量订单而非仅是主题映射？ | unresolved | satellite_revenue, satellite_backlog, satellite_ASP, satellite_margin | revenue, gross_margin, parent_net_profit, valuation_multiple | satellite/ground terminal revenue, backlog, order conversion, margin; 获取公告/年报中商业卫星通信业务收入、订单与客户名称 |
| Q4 | 公司海外收入占比高、美元结算且存在北美客户供应链监管传闻；实际区域收入占比、客户集中度、关税与供应链合规整改对交付和毛利率的影响是什么？ | unresolved | overseas_revenue_pct, top_customer_share, USD_CNY, export_volume | revenue, gross_margin, finance_expense, receivables | geographic revenue split, customer concentration, FX hedge ratio, tariff exposure; 获取区域收入结构和前五大客户数据 |
| Q5 | Q12026合并毛利率+2.30pp YoY的改善来自哪个产品/客户；高附加值连接器、散热材料、不锈钢电池壳能否持续提升产品结构并支撑经营利润率？ | unresolved | product_mix, segment_gross_margin, R&D_expense_ratio, operating_leverage | gross_margin, operating_margin, parent_net_profit, EPS | segment gross margin, new product revenue, R&D project economics; 获取分产品毛利、新品收入与研发资本化/费用化详情 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | Revenue | CNY mn | 8909.78 | 9153.62 | 9611.3 | 10091.87 | 2026E = Q12026 revenue / implied seasonality share (Q1 seasonal-adjusted 9153.62); 2027E/2028E = +5% p.a. analyst estimate | analyst_estimate_base | consumer electronics demand, MLCC/satellite ramp, FX; segment revenue split, volume/ASP detail |
| consolidated | Gross margin | % | 21.7664 | 22.0 | 22.4 | 22.8 | Q1 2026 reported + product-mix improvement assumption | analyst_estimate_base | product mix, input costs, FX; segment gross margin, unit cost |
| consolidated | Operating margin | % | 6.2048 | 6.4 | 7.0 | 7.3 | Q1 2026 + modest mix/scale leverage; R&D drag not fully quantified | analyst_estimate_base | R&D spend, selling expense, mix; segment operating expense, R&D capitalization |
| consolidated | Net margin | % | 5.2649 | 6.0 | 6.6 | 7.0 | Revenue x net margin = parent net profit; base case gradual recovery above Q1 seasonal low | analyst_estimate_base | finance expense, tax, minority interest; finance expense forecast, minority interest forecast, tax rate |
| consolidated | Parent net profit | CNY mn | 708.69 | 549.2 | 634.35 | 706.43 | Revenue x net margin: 9153.62*6.0%, 9611.30*6.6%, 10091.87*7.0% | analyst_estimate_base | segment gross margin, MLCC/satellite ramp, transaction consolidation; segment profit, transaction target profit |
| consolidated | EPS | CNY/share | 0.732 | 0.5676083105907893 | 0.6556124031741937 | 0.7301084101432106 | parent net profit (CNY mn) / diluted shares (mn) | calculated | share count, parent profit, share-based payment; diluted share count from primary total_share source |
| consolidated | OCF | CNY mn | None | 424.2 | 507.5 | 600.5 | Parent net profit x assumed OCF/NP ratio; 2026 77.22% Q1 ratio, 2027 80%, 2028 85% | analyst_estimate_base | working capital, receivables, inventory; reported FY2025/2026 OCF, working-capital schedule |
| consolidated | Capex | CNY mn | None | None | None | None | Not derivable from supplied evidence; cash paid to acquire/construct long-term assets not supplied | missing | MLCC and satellite capacity expansion; c_pay_acq_const_fiolta, capex schedule |
| consolidated | FCF | CNY mn | None | None | None | None | OCF - Capex; blocked by missing Capex | missing | capex intensity, OCF quality; Capex, reported FCF |
| consolidated | operating_profit |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | consolidated/unmapped | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE02 | consolidated/unmapped | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE03 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE04 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE05 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE06 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE07 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE08 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE09 | consolidated/unmapped | capex_or_roic | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE10 | consolidated/unmapped | segment_volume | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE11 | consolidated/unmapped | asp_or_price | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE12 | consolidated/unmapped | utilization_or_backlog | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-08-10T14:31 | 有效窗口/11天 | 未披露 | 未提取到带期间的明确盈利预测 | https://images.zsxq.com/FrsZYT1FicK0dPbgmurq5PeVvaV1?imageMogr2/auto-orient/quality/100!/ignore-error/1&e=1790783999&s=yvjvjtjmyvyvtt&token=q6iZ0sQtf9U7s1qz0r4yMawNq3-u2w6lbnai6y2J:GjNBJqjhv8St04uzK4abm5xgPaw= | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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