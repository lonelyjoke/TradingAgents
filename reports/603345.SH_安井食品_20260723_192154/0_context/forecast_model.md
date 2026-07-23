# Forward Forecast Model Scaffold for 603345.SH as of 2026-07-23

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- / snapshot / period / end_date / revenue / net_profit_parent / annualized_revenue / annualized_net_profit_parent / seasonality_adjusted_revenue / seasonality_adjusted_net_profit_parent / seasonality_method /
- / Revenue base / 4710170515.87 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix /
- / Gross margin / 24.9871% / +1.66pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit /
- / Finance-expense ratio / 0.2985% / +0.43pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief /
- / OCF / net profit / 1.8527 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization /
- / Receivables / revenue / 3.124% / +0.02pp / YoY: 20260331 vs 20250331 / tests working-capital drag; interim periods use annualized revenue /
- / Inventory / revenue / 16.1335% / -3.32pp / YoY: 20260331 vs 20250331 / tests inventory build and demand quality; interim periods use annualized revenue /
- - Working-capital stock ratios use annualized revenue for interim periods so Q1/H1/Q3 snapshots remain comparable with FY.
- - Build every forward case through revenue = volume × price × mix, then flow it through gross margin, operating margin, finance cost, and cash conversion.
- - Tie every catalyst to one modeled lever: order growth, ASP, utilization, product mix, gross margin, working capital, capex, or financing cost.

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| 食品制造与农产品 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 安井主业（速冻食品） revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 新宏业 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 新柳伍 revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| 鼎味泰（并表） revenue | segment revenue = volume/units x ASP/price/mix or reported segment run-rate | start from filing revenue weight, growth, margin and segment-specific demand/pricing evidence |
| Gross profit | sum(segment revenue x segment gross margin) | segment margin, mix, cost curve, utilization and pass-through |
| Operating profit | gross profit - R&D - SG&A - finance/impairment | scale leverage, investment phase and credit quality |
| net profit/EPS / FCF | operating profit - tax/minority + working-capital/capex bridge | cash conversion, reinvestment cycle and share count |

## Semiconductor Forecast And Valuation Controls
- Semiconductor profile: fabless / chip design. Use this profile before consumer, generic technology, telecom, metals, or battery templates.
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
| 食品制造与农产品 | period=annual filing; revenue=16176975631.6 filing table unit not explicit in extracted row; revenue_weight=100.0%; growth=7.11%; gross_margin=21.53% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 安井主业（速冻食品） | period=2026Q1; revenue=None; revenue_weight=None%; growth=None%; gross_margin=24.9871% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 新宏业 | period=估计2026Q2; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 新柳伍 | period=估计2026Q2; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
| 鼎味泰（并表） | period=估计2026Q2; revenue=None; revenue_weight=None%; growth=None%; gross_margin=None% | Ask what this business sells, who buys, why customers choose/switch, who the true substitutes and peers are, how pricing and delivery work, where the cost and cash-cycle risks sit, and what segment-specific question decides the investment case. | Use reported/calculated revenue, volume, ASP/price, margin, profit, backlog/utilization, market share, cash conversion and valuation contribution where available; otherwise label the missing metric and keep the answer qualitative. |
- Every material segment selected from the filing revenue mix must receive a qualitative answer even when source data do not disclose the ideal volume, ASP, margin or share series.
- Quantitative claims require reported, calculated or verified evidence, or an explicit analyst_estimate label with sensitivity and verification gate.
- The public PM report must synthesize these answers as investor-facing sell-side analysis; keep the agenda itself, missing-data ledger and raw checks in internal workbench fields.

## Sell-Side Depth Chain: Revenue Mix To Falsification
- Required analytical chain: financial-report revenue mix -> profit-pool priority -> segment question tree -> qualitative/quantitative answer -> expectation gap -> valuation transmission -> falsification gate.
- Revenue weight is only the starting point. Prioritize segments by revenue weight, gross margin, growth, cash conversion, capex intensity, competitive erosion risk and valuation sensitivity.
| segment / business line | profit-pool priority basis | segment-specific question tree | expectation gap / valuation / falsification linkage |
| --- | --- | --- | --- |
| 食品制造与农产品 | revenue_weight=100.0%; growth=7.11%; gross_margin=21.53%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 安井主业（速冻食品） | revenue_weight=None%; growth=None%; gross_margin=24.9871%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 新宏业 | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 新柳伍 | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
| 鼎味泰（并表） | revenue_weight=None%; growth=None%; gross_margin=None%; add cash conversion, capex intensity and valuation sensitivity if disclosed | Demand: volume, penetration, customer budget or cycle driver; Competition: true peers, substitutes, customer switching or self-supply; Profitability: ASP/price, cost curve, utilization, mix and operating leverage; Cash flow: inventory, receivables, prepayments, capex and collection cycle | State what the market appears to price for this segment, which assumption differs in the model, how the delta changes revenue/profit/FCF/multiple, and which future KPI would confirm or falsify it |
- A public thesis is incomplete unless it names the one or two segment assumptions that matter most for market expectation and valuation.
- A positive thesis must include the strongest bear mechanism; a negative thesis must include the strongest upside mechanism. Tie each to a dated KPI or disclosure gate.
- The final PM memo should not reproduce this table. It should convert the chain into connected sell-side prose in the business, thesis, forecast, valuation and catalyst/risk sections.

## LLM Analysis Intervention Map
| LLM node | required contribution | current packet output / fallback task |
| --- | --- | --- |
| 1. Business question tree | Use LLM judgment to turn filing segments into company-specific demand, competition, profitability and cash-flow questions. | Q1：安井主业量增是否可持续？餐饮端实质性恢复程度如何？; Q2：子公司小龙虾/鱼糜能否稳定盈利，避免利润拖累？; Q3：清真/出口项目能否成为有意义的第二增长曲线？; Q4：在资本开支下降后，自由现金流是否能支撑持续高额分红？ |
| 2. Profit-pool priority | Use LLM judgment to decide which units matter beyond revenue weight, considering margin, growth, cash, capex, erosion risk and valuation sensitivity. | 绝对核心：安井品牌速冻主业贡献集团毛利的90%+，是质优现金牛，即使利润增速10%，体量也足以提供17-18亿经调整利润；子公司体量小但利润弹性大，可贡献2-3亿元净利润或大幅拖累；新业务尚属于期权阶段，利润贡献几乎为零。因此研究资源优先聚焦主业量、价、成本三大变量。 |
| 3. Competition and substitution | Use LLM judgment to reason about true peers, customer switching, supplier diversification, self-supply, substitutes and technology/regulatory change. | 安井在速冻火锅料赛道领先地位明显，真正竞争对手是海欣食品（品牌较弱）、三全食品（传统面米为主，火锅料存在竞争）以及区域小厂。主要威胁来自：1）大型餐饮企业自建中央厨房，替代外采；2）新的资本扶持的预制菜品牌（如味知香、千味央厨）以差异化产品切入B端，抢夺份额；3）便利店鲜食/短保食品对速冻替代，但影响有限。公司应对之道在于快速推新、强化经销商忠诚度和扩大品类边界。 |
| 4. Qualitative-to-quantitative bridge | Use LLM judgment to keep analysis alive when ideal data are absent, while clearly stating what can and cannot be quantified. | Q2新宏业、新柳伍等子公司数据极缺，仅从渠道反馈得知新宏业双位数增长、新柳伍利润承压，但无法量化影响。需通过获取子公司报表或准实缴数据，才能从定性转为定量预测。另一关键缺口是原材料成本对毛利率的量化弹性，需获取公司内部成本结构管理报表。 |
| 5. Expectation gap | Use LLM judgment to infer what the market or consensus appears to price and whether the model differs by variable, magnitude or timing. | 市场当前给予TTM PE 19x，隐含了: 当前利润TTM 15.3亿且预期未来一年持续增长10-15%。若公司达成2026E 16.8亿利润，远期PE约17.3x（在市值不变情况下），但若增长不达12%，估值将面临收缩。潜在的预期差在于市场可能低估了成本红利和运营杠杆带来的利润率提升，同时可能对清真/出口等增量信心不足，并未给予期权价值。若二季报主业增速超15%且毛利率保持在24%以上，将触发向上重估。 |
| 6. Red-team counterargument | Use LLM judgment as a skeptical analyst to challenge the core thesis and define falsification signals. | 熊案强化版：如果餐饮下半年失速，同时小龙虾/鱼糜因气候或消费降级严重亏损，公司可能面临主业增速降至5%，毛利率跌破20%的局面，年利润仅11-12亿。届时PE将跌至12-15x，对应市值缩至150-180亿。此外，公司商誉高达X亿（需查年报），若子公司业绩连续低于预期，计提减值将一次性侵蚀利润。; 牛案的反驳点：即使公司主业坚韧，市场也许因宏观通缩和国家取消补贴担忧，给予消费股系统性折价，即使业绩达成20亿利润，也只能获得15x低估值，股价几乎无上涨空间。加之公司历史上较少回购和积极回报，资金流动偏弱，可能长期被低估。 |
| 7. Valuation explanation | Use LLM judgment to explain valuation method, multiple/risk-premium logic and business-variable sensitivity; code owns arithmetic. | 基础桶采用2026E PE 19x，与当前TTM市盈率基本持平，体现了市场对消费必需品稳定的估值中枢。期权桶采用概率加权估算新业务可能带来的价值，按20%成功率给予60亿增量，折现后计入每股。该方法依赖盈利预测准确性，风险在于假设的永久增长率和权益成本未被明确，但通过场景概率减轻了部分不确定性。当前估值无法与价格比较，缺少股价和股本。 |
| 8. Final editorial synthesis | Use LLM judgment to convert the workbench into readable investor-facing sell-side prose without exposing raw ledgers. | 安井食品作为中国速冻调理食品的龙头企业，当前仍处在品类扩张和渠道下沉的成长中场。2026年主业在弱需求中继续保持双位数增长，叠加原材料成本下降，利润弹性正在释放。主要风险在于消费大盘能否止跌回升、子公司盈利能否稳定。PM需要关注即将披露的半年报是否验证量利齐升，并密切跟踪餐饮社零与原材料价格。当前市场估值并未给予过高期待，为左侧布局业绩确定性提供了可能性，但需忍受消费板块风格压制的短期波动。 |
- These are analysis-layer judgments, not permission to invent facts. Numeric claims still require reported/calculated/verified evidence or explicitly labeled analyst estimates.
- The final PM memo should absorb these judgments into the owning sections and not publish this intervention map as a reader-facing table.

## Alternative-Intelligence Assumption Bridge
| evidence_id | affected model variable | permitted use | verification gate | required audited outcome |
| --- | --- | --- | --- | --- |
| KPE01 | segment gross margin | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE02 | working hypothesis / verification calendar | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE03 | segment gross margin | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE04 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE05 | market share / segment volume | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | numeric assumption delta or explicit rejection |
| KPE06 | valuation multiple / risk premium | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE07 | realized ASP / price pass-through | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
| KPE08 | segment volume / utilization / backlog | private/proxy prior; quantify delta or reject, never use as a hard fact | cross-check with filings/Tushare/price-volume/announcements before hard use | scenario probability before->after or watch/reject |
- The downstream model must state an explicit numeric assumption delta, scenario-probability delta, or rejection reason for every listed KPE item.

## Model-Ready Evidence Ledger
| evidence_id | source | tier | status | model variable | source period | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| EV003 | earnings_model | primary_or_structured_filing | reported | revenue | 20260331, 20250331 | / Revenue base / 4710170515.87 / N/A / YoY: 20260331 vs 20250331 / top-line starting point for volume × price × mix / |
| EV004 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Gross margin / 24.9871% / +1.66pp / YoY: 20260331 vs 20250331 / main bridge from demand to gross profit / |
| EV006 | earnings_model | primary_or_structured_filing | reported | segment_margin | 20260331, 20250331 | / Net margin / 11.9562% / +1.00pp / YoY: 20260331 vs 20250331 / captures final earnings conversion / |
| EV007 | earnings_model | primary_or_structured_filing | reported | operating_expense | 20260331, 20250331 | / Finance-expense ratio / 0.2985% / +0.43pp / YoY: 20260331 vs 20250331 / captures leverage drag or relief / |
| EV008 | earnings_model | primary_or_structured_filing | reported | profit_or_eps | 20260331, 20250331 | / OCF / net profit / 1.8527 / N/A / YoY: 20260331 vs 20250331 / tests earnings quality and cash realization / |
| EV029 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / accounting_reconciliation / Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. / operating_cash_flow: 安井食品2026年第一季度报告: 524,970,309.80 343,034,225.89 53.04 经常性损益的净利润 经营活动产生的现金流量净额 1,043,368,202.31 673,201,949.8... |
| EV032 | industry_kpi | secondary_or_derived_research | reported | profit_or_eps | 2026, 季度 | / cash_flow_quality_decomposition / Separate accounting profit from cash conversion, working-capital drag, and demand visibility. / operating_cash_flow: 安井食品2026年第一季度报告: 524,970,309.80 343,034,225.89 53.04 经常性损益的净利润 经营活动产生的现金流量净额 1,043,368,202.31 673,201,94... |
| EV033 | industry_kpi | secondary_or_derived_research | reported | capex_or_roic | 2026, 季度 | / capex_cip_return_bridge / Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. / long_term_equity_investments: 安井食品2026年第一季度报告: 其他债权投资 长期应收款 长期股权投资 16,119,940.24 15,568,064.29 / long_term_equit... |
| EV034 | industry_kpi | secondary_or_derived_research | reported | segment_margin | 2026, 季度 | / non_recurring_profit_quality / Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. / impairment: 安井食品2026年第一季度报告: 净敞口套期收益（损失以“-”号填列） 公允价值变动收益（损失以“-”号填列） 9,350,781.12 ... |
| EV035 | industry_kpi | secondary_or_derived_research | reported | balance_sheet | 2026, 季度 | / balance_sheet_forward_signals / Read balance-sheet leads before income-statement confirmation. / receivables: 安井食品2026年第一季度报告: 交易性金融资产 3,613,546,171.26 3,639,173,341.26 衍生金融资产 应收票据 3,289,265.59 1,967,358.95 / receivables: 安井食品2026年第一季度报告: 衍生金融资产 应收票据 3,28... |
| EV037 | industry_kpi | secondary_or_derived_research | reported | segment_margin | unspecified | / disclosure_quality_score / Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. / Coverage grade strong; reports seen annual/quarterly/semiannual; answered 7/9; core pack ready. Annual base text and quarterly chec... |
| EV043 | company_events | research_context | reported | profit_or_eps | 2026-07-22, 半年 | / 2026-07-22 20:50:00 / 新浪财经 / 洽洽食品上半年净利润预增近两倍？ 创始人之女陈奇这回证明了自己 / N/A / |
| EV045 | company_events | research_context | reported | utilization_or_backlog | 20260720, 2028 | / 20260720 / 国内联播快讯 / 央视网消息（新闻联播）：水利部启动水文现代化建设三年行动水利部日前启动水文现代化建设三年行动，提出到2028年，推动国家水文站网体系进一步优化，雨水情监测立体感知能力进一步提升，水文新质生产力加速发展，水文行业管理能力明显提升。国务院食安办部署加强暑期、汛期食品安全工作国务院食安办印发通知，要求各地食安办切实加强暑期、汛期食品安全工作，对向灾区集中调拨、捐赠、销售的食品以及灾区企业生产销售的食品，视情加大监督抽检力度，发现不合格食品依法下架、召回、销毁。我国将开展村镇微能 |
| EV046 | company_events | research_context | reported | asp_or_price | 20260715, 2030 | / 20260715 / 国内联播快讯 / 央视网消息（新闻联播）：“十五五”时期支持建设200个左右“无废城市”《固体废物污染防治“十五五”规划》日前出台，明确提出：将支持200个左右城市开展“无废城市”建设。到2030年，重点领域固体废物专项整治取得明显成效，固体废物历史堆存量得到有效管控，固体废物综合治理能力和水平显著提升。前六个月全社会用电量同比增长5.3%国家能源局今天（7月15日）发布数据显示，1—6月，全社会用电量累计50999亿千瓦时，同比增长5.3%。其中，充换电服务业、互联网数据服务用电量增速较 |
| EV051 | market_expectation | structured_market_data | reported | valuation | TTM | / PE TTM / 19.0043 / earnings multiple the market is paying now / |
| EV052 | market_expectation | structured_market_data | reported | revenue | TTM | / PS TTM / 1.6781 / sales multiple the market is paying now / |

## Segment / Business-Bucket Three-Year Operating Matrix
| business bucket / driver | formula | 2026E | 2027E | 2028E | evidence ids / assumption status |
| --- | --- | --- | --- | --- | --- |
| 食品制造与农产品 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=annual filing; reported revenue=16176975631.6 (filing table unit not explicit in extracted row); revenue weight=100.0%; growth=7.11%; gross margin=21.53%; margin change=-1.7pp; source=filing_intelligence; mode=deterministic_filing_row |
| 安井主业（速冻食品） | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=2026Q1; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=24.9871%; margin change=1.66pp; source=earnings_model; mode=llm_semantic |
| 新宏业 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=估计2026Q2; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| 新柳伍 | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=估计2026Q2; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
| 鼎味泰（并表） | segment revenue = volume/units x ASP/mix | to be estimated | to be estimated | to be estimated | base period=估计2026Q2; reported revenue=None (); revenue weight=None%; growth=None%; gross margin=None%; margin change=Nonepp; source=knowledge_planet; mode=llm_semantic |
- Consolidated revenue, profit, and cash flow must reconcile to the sum of business buckets; do not model only the fastest-growing segment.

## Consensus And Market-Implied Expectation Gap
| comparison layer | supplied evidence | required model treatment |
| --- | --- | --- |
| Current market-implied expectation | / Market cap (CNY) / 29036128968 / current equity value / / / PE TTM / 19.0043 / earnings multiple the market is paying now / | reverse current price into earnings, growth, margin, ROE/FCF or asset-value assumptions |
| External sell-side / consensus proxy | missing; no company-specific external forecast supplied | label broker/date/count; use range or median only when the source is company-specific |
| TradingAgents model | missing until downstream analyst fills the operating matrix | compare our driver assumptions line by line with market and external expectations |
- A claimed expectation gap is invalid unless it identifies the exact differing variable, period, magnitude, evidence grade, and next event that can close the gap.
- An industry report mentioning the company is not company consensus. Keep it as a sector prior unless it supplies company-specific forecasts.

## Official Earnings Guidance Override
| supplied official evidence | required model treatment |
| --- | --- |
| / 2026-07-22 20:50:00 / 新浪财经 / 洽洽食品上半年净利润预增近两倍？ 创始人之女陈奇这回证明了自己 / N/A / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| / 2026-07-22 20:50:00 / 新浪财经 / 洽洽食品上半年净利润预增近两倍？ 创始人之女陈奇这回证明了自己 / N/A / | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
| - Treat official earnings guidance, performance previews, and quick reports as harder evidence than run-rate extrapolation; reconcile stated H1/Q1/Q2/EPS ranges before writing forecast, valuation, rating, or next-verification language. | hard public evidence for the covered period; reconcile Q1, implied Q2, H1, H2, full-year parent profit/EPS, and mark unaudited/preliminary status where applicable |
- If official guidance conflicts with the prior run-rate or sell-side/proxy assumption, update the forecast or state the exact reason it cannot be used. Do not ignore the guidance.
- After guidance is available, the next verification point is the formal report's segment mix, cost bridge, cash conversion and balance-sheet quality, not whether the guided profit strength exists.

## Assumption Change And Valuation Transmission Ledger
| evidence_id | model variable | old assumption | new assumption | earnings/FCF formula impact | bull/base/bear probability before -> after | valuation impact | disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| required per promoted clue | required | numeric or explicit missing | numeric or unchanged | show affected forecast line and delta | probabilities must sum to 100% before and after | target/SOTP/multiple delta or none | accepted / watch / rejected with reason |
- Recalculate revenue, profit/EPS, FCF, scenario values, and probability-weighted value after any accepted assumption change; narrative-only changes are invalid.
- Private/proxy evidence may change probability or timing before it changes a base-case number, but the before/after values and public verification gate are mandatory.

## Shared Company Underwriting Packet
- Research readiness: partial
- Readiness reasons: 缺少稀释后总股本数据，无法计算 EPS 及每股公允价值，所有 per-share 指标留空; 缺乏分产品线/子公司拆分收入与利润的权威数据，新宏业、新柳伍、鼎味泰的贡献无法量化建模，仅能做定性分析; 缺少2025年完整现金流量表及资本支出明细，OCF/capex 仅基于2026Q1 年化推导，缺乏全年实际数验证; 原材料成本传导机制未建模，生猪、豆粕、玉米、棕榈油等价格变化尚未定量纳入利润预测; One or more filing-reported segments required deterministic restoration.; Required consolidated three-year forecast lines are incomplete.; Material segment three-year driver lines are missing: 安井主业（速冻食品）, 新宏业, 新柳伍, 食品制造与农产品, 鼎味泰（并表）; Bull/base/bear per-share valuation is incomplete.
- Forecast years: 2026E, 2027E, 2028E
- This is the common model. Analysts must propose explicit changes to these rows instead of creating separate narrative forecasts.

### Company Operating Equations
- Revenue: 营收 = 出货量(万吨) × 平均出厂价(元/吨)，其中量由产能、利用率和渠道覆盖决定，价受产品结构(高毛利菜肴占比)、竞品定价和原材料成本传导影响
- Profit: 毛利 = 营收 - 主要原材料(肉类、鱼糜、大豆蛋白、油脂、面粉等) - 包材 - 制造费用；营业利润 = 毛利 - 销售费用(渠道佣金/促销) - 管理费用 - 研发费用；归母净利润 = 营业利润 - 财务费用 - 所得税 - 少数股东损益
- Cash flow: 经营性现金流 = 净利润 + 折旧摊销 - 营运资金变动(存货/应收/应付)，自由现金流 = 经营性现金流 - 资本开支(产能新建/设备更新)
- Reinvestment: 中等资本密集，年资本开支约为营收的5-8%，主要用于新建工厂(如安斋项目、华中/西北产能)和生产线智能化改造，坚持高比例现金分红，维持低有息负债

### Company-Specific Underwriting Questions
| id | question | current answer | decisive variables | affected financial lines | missing evidence / next verification |
| --- | --- | --- | --- | --- | --- |
| Q1 | 安井品牌主业2026年全年出货量增速能否持续12%以上，且毛利率稳定在23%以上？ | unresolved | 主营业务收入增速, 毛利率, 销售费用率 | revenue, gross_margin, parent_net_profit | 6-7月每月出货量及终端动销实际数据, 最新的原材料采购订单价和库存成本重估结果, 各子品类具体量价拆分和利润贡献; 2026年8月半年报详细收入拆分、毛利率分析及经销商数量变动 |
| Q2 | 子公司新宏业、新柳伍、鼎味泰在2026-2027年能否实现可持续盈利，而非周期性拖累？ | unresolved | 子公司合并营业收入, 子公司合并净利润, 少数股东损益 | revenue, parent_net_profit | 各子公司最近三期报表数据, 新宏业小龙虾原材料成本和售价季节性曲线, 鼎味泰并表时点、收购溢价比率和业绩承诺; 2026半年报和年报中有关子公司业绩的披露，或管理层业绩会给予明确指引 |
| Q3 | 公司的清真（安斋）及出口东南亚项目能否在2027年前形成5%以上的收入增量？ | unresolved | 新品类收入, 新市场收入, 新业务盈亏 | revenue, parent_net_profit | 安斋项目的营收目标和投资回收期, 东南亚出口的订单、物流解决方案和经销商协议; 2026年中报是否单独披露清真产品或出口收入，以及下一个投资者互动平台是否有更具体的经营数据 |
| Q4 | 自由现金流能否在2026-2027年实现20亿以上，并支持持续的高比例分红？ | unresolved | 经营性现金流, 资本开支, 自由现金流 | free_cash_flow, dividend_per_share | 2025年全年OCF和capex的具体数额, 2026-2028年资本开支计划, 分红政策是否稳定且无回购抵消; 2026半年报的现金流量表全文及管理层对后续资本开支的指引 |
| Q5 | 安井食品合理的长期PE估值中枢应是15x、20x还是25x？ | unresolved | PE_multiple, earnings_growth, ROE | valuation | 可比公司的PE中枢和财务比率全面对比, 机构投资者对安井的估值方法论; 机构一致预期（如有）的更新数据，以及食品饮料行业比较的估值框架研究 |

### Shared Three-Year Model Lines
| segment | metric | unit | base | 2026E | 2027E | 2028E | formula | status | sensitivity / missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consolidated | 营业收入 | CNY mn | 16192.6 | 18240.0 | 20040.0 | 21840.0 | 基年实际 x (1+增速)，2026E+12.6%, 2027E+9.9%, 2028E+9.0% | model_assumption, based on channel checks and industry recovery trajectory | 每下降1%收入增速，净利润下降约1.2%; 下半年具体订单和经销商备货数据, 餐饮端整体复苏速度的实际量化 |
| consolidated | 毛利率 | % | 21.53 | 23.2 | 23.5 | 23.8 | 原材料成本小幅回落叠加产品结构升级，毛利率逐步提升，2026E+1.67pp, 2027E+0.3pp, 2028E +0.3pp | model_assumption, supported by Q1 2026 gross margin of 24.99% and commodity price trends | 毛利率每变动0.5个百分点，对净利润的影响约4-5%; 各原材料在成本中精确占比及套保策略, 公司实际采购价格与期货基准的差异（basis） |
| consolidated | 营业利润 | CNY mn | None | 2050.0 | 2350.0 | 2650.0 | 粗略估计为营收的11-12%，随毛利率提升和费用率优化改善 | model_assumption, pending verification from operating margin derived from 2026Q1 (15.49%) | 费用率变化导致营业利润波动较大; 2025年实际营业利润, 明细销售/管理费用预算 |
| consolidated | 归母净利润 | CNY mn | 1359.24 | 1680.0 | 1920.0 | 2160.0 | 净利润增速快于收入，2026E+23.6%, 2027E+14.3%, 2028E+12.5% | model_assumption, reflects operating leverage and moderate cost tailwinds | 归母净利润是估值的基础，每相差1亿利润，按20x PE影响20亿市值; 少数股东损益预测, 财务费用及税率实精准假设 |
| consolidated | 基本每股收益 (EPS) | CNY/share | None | 5.040671437598174 | 5.760767357255056 | 6.480863276911938 | parent net profit (CNY mn) / diluted shares (mn) | calculated | ; 稀释后总股本，无法由其他数据可靠推导 |
| consolidated | 经营活动现金流量净额 (OCF) | CNY mn | None | 2100.0 | 2400.0 | 2700.0 | 按净利润的1.25x估算, 基于2026Q1 OCF/净利=1.85x适度下调 | model_assumption, partially supported by Q1 2026 cash conversion | OCF低于预期则FCF无法支撑高分红; 2025年全年经营现金流量, 预收/应付/存货的预计变动 |
| consolidated | 资本开支 (capex) | CNY mn | None | 900.0 | 850.0 | 800.0 | 假设为营收的5%左右，略下降，进入产能释放期 | model_assumption, no filing-backed capex data available | 若 capex 超预期达营收7%+，将严重侵蚀FCF; 2025年资本开支的具体数额及2026-2028预算, 在建工程未来节奏 |
| consolidated | 自由现金流 (FCF) | CNY mn | None | 1200.0 | 1550.0 | 1900.0 | OCF minus capex | derived from OCF and capex assumptions | FCF是回本周期计算基础，差额影响估值15-25%; 同上，OCF和capex不确定导致FCF偏差大 |
| consolidated | ocf |  | None | None | None | None | missing; downstream analyst must complete | missing | ; required consolidated forecast line omitted |

## Structured KPE Physical And Financial Quantification
| evidence_id | segment | variable | assumption delta | revenue delta CNY mn | parent-profit delta CNY mn | EPS delta | FCF delta CNY mn | probability treatment | status | audited outcome | missing inputs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KPE01 | 安井主业（速冻食品） | revenue_growth | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 6月社零及公司中报 | 渠道反馈的准确基数, 同比基数调整 |
| KPE01 | 新宏业 | revenue_growth | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 子公司财务数据披露或渠道复核 | 新宏业收入利润绝对数 |
| KPE01 | 新柳伍 | profit_margin | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 子公司利润表或渠道细节 | 承压原因量化项 |
| KPE03 | 安井主业（速冻食品） | revenue_growth | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 中报验证 | none |
| KPE04 | consolidated | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 行业数据验证 | none |
| KPE05 | consolidated | free_cash_flow | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 公司现金流报告 | 具体回本年限数值 |
| KPE08 | 安井主业（速冻食品） | revenue_growth | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 6月行业数据 | none |
| KPE10 | 安井主业（速冻食品） | revenue_growth | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 公司中报 | none |
| KPE11 | 安井主业（速冻食品） | revenue_growth | None % | None | None | None | None | bull None->None; base None->None; bear None->None | unquantified | unchanged/watch: no model assumption or scenario probability change until 渠道复核 | none |
| KPE12 | consolidated | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | unverified | unchanged/watch: no model assumption or scenario probability change until 行业数据验证 | none |
| KPE02 | 安井主业（速冻食品） | unmapped | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
| KPE06 | consolidated/unmapped | valuation | None  | None | None | None | None | bull None->None; base None->None; bear None->None | watch_no_model_change | unchanged/watch: no model assumption, scenario probability, valuation, rating, or sizing change until cross-check with filings/Tushare/price-volume/announcements before hard use | baseline and revised operating assumption, unit and financial transmission inputs |
- Only grounded and deterministically quantified rows may change a base-case forecast. Missing or unverified rows remain probability/watch inputs until the listed baselines or unit economics are supplied.

## Sell-Side Forecast, Valuation And Revision Observations
| id | institution/date | freshness | rating | forecast facts | valuation facts | normalized points | revision signal | model treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KSI01 | 机构未识别/2026-07-07 | 有效窗口/16天 | 未披露 | 26Q2新宏业收入净利润双位数以上，新柳伍收入正增长净利润承压，叠加鼎味泰并表额外贡献 / 预计26Q2报表收入增速接近15% / 26Q2新宏业收入净利润双位数以上，新柳伍收入正增长净利润承压，叠加鼎味泰并表额外贡献 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 较前次口径发生变化；尚无可同口径比较的标准化数值 | single observation; compare period/variable/magnitude with the independent model |
| KSI02 | 机构未识别/2026-07-06T09:22 | 有效窗口/17天 | 未披露 | 安井食品：坚定持有！6月收入双位数增长、环比提速，淡季增速好于同期，龙头优势持续巩固 | 未提取到目标价/估值方法与倍数 | 无可标准化数值 | 窗口内首次识别，暂无同机构前序可比 | single observation; compare period/variable/magnitude with the independent model |
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