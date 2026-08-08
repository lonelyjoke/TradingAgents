# Financial-report intelligence for 300723.SZ as of 2026-08-08

- Company: 一品红
- Vendor industry: 化学制药
- Reading profile: banking
- Research hygiene: industry-specific playbooks are conservative by design; if identity is ambiguous, generic questions are safer than a wrong template.
- Financial-report look-back: 900 days
- Extraction status: Financial-report text extraction succeeded.

## Financial Reports Considered
- : 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]

## Financial Report Text Acquisition Audit
| stage | status | detail |
| --- | --- | --- |
| runtime_dependency | ready | pdftotext is available for PDF text extraction. |
| announcement_lookup | ready | Found 4 candidate financial-report announcement(s) from primary and CNINFO sources. |
| pdf_text_extraction | failed | 2025年年度报告: PDF downloaded but no readable text was extracted from c94be0ac8fa58e7f93add8974c086f8d92dd6c9d.pdf. |
| pdf_text_extraction | failed | 2026年一季度报告: PDF downloaded but no readable text was extracted from 42dbbb56973b60fcfd419ec3edf8b51581811ba9.pdf. |
| pdf_text_extraction | failed | 2025年三季度报告: PDF downloaded but no readable text was extracted from 935e1ef7acdebbff37a9e418559e8281bf254cec.pdf. |
| pdf_text_extraction | failed | 2025年半年度报告: PDF downloaded but no readable text was extracted from 9513256898ec38f3b386d31de1b832c746dd7402.pdf. |
| local_text_cache | ready | Recovered 1 supplemental cached report text(s). |
| final_text_bundle | ready | Prepared 1 readable report text(s) for filing intelligence. |

## Filing Reading Coverage Audit
| coverage_grade | report_types_seen | missing_report_types | answered_questions | core_pack_status | confidence_read |
| --- | --- | --- | --- | --- | --- |
| weak | quarterly | annual/semiannual | 2/5 | thin | Readable text exists but the pack is too thin for a full buy-side read; avoid strong claims about business model, second curve, or execution trend. |

## Internal Filing Quality Modules
| module | purpose | filing_evidence | analyst_use | missing_or_next_check |
| --- | --- | --- | --- | --- |
| accounting_reconciliation | Check signs, units, periods, and cross-statement consistency before a number enters the PM memo. | {'lens': 'retail_wealth_engine', 'report_type': 'quarterly', 'evidence_strength': 'explicit disclosure', 'filing_evidence': '一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：应付利息 应付股利 应付手续费及佣金', 'why_it_matters': 'Retail AUM matters only when it convert... | Use as the report's source-of-truth layer; flag conflicting cash-flow, profit, leverage, or period claims instead of averaging narratives. | If debate numbers conflict, cite the exact filing period and reconcile revenue, profit, OCF, working capital, and leverage before rating impact. |
| segment_economics_depth | Decide whether each business line has enough disclosed scale, growth, margin, cash quality, and valuation treatment. | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 子公司 Sobi US Holding Corp.（以下简称：Sobi 美国）签署并购协议，Sobi 美国拟以 9.5 亿美元首付款（折合人民币约 | Core segments can support base-case value; thin or header-only second curves stay in SOTP/scenario value. | Require revenue, cost/gross margin, profit or cash-quality evidence by product, channel, geography, or business bucket. |
| footnote_radar | Surface decision-relevant notes that can hide risk or change confidence. | impairment_policy: 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | impairment_policy: 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Use footnotes as valuation modifiers for customer concentration, related parties, guarantees, litigation, impairment, and capitalization choices. | If note evidence is thin, avoid claiming footnote cleanliness; keep guarantees, litigation, impairment assumptions, and related parties on the checklist. |
| cash_flow_quality_decomposition | Separate accounting profit from cash conversion, working-capital drag, and demand visibility. | Not enough direct filing evidence found in the readable report pack. | Upgrade growth only when revenue, margin, OCF, receivables, inventory, and contract liabilities point in the same direction. | Next filing should confirm OCF/net profit, collections, inventory turns, and whether contract liabilities convert at acceptable margin. |
| capex_cip_return_bridge | Test whether capex, construction-in-progress, or investment assets are building returns or just absorbing capital. | Not enough direct filing evidence found in the readable report pack. | Put projects with unclear utilization, payback, or ROIC in scenario value; require demand and margin evidence before base-case valuation credit. | Track commissioning, utilization or occupancy, capex-to-revenue, payback/ROIC, impairment, and disposal gains or losses. |
| mdna_text_change | Read management wording changes, proof-backed claims, risk-language upgrades, and abnormal silence across reports. | risk_language_upgrade: 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | risk_language_upgrade: 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值... | Use text changes to decide whether management is proving, softening, or avoiding a theme; do not let soft wording replace hard evidence. | Compare the next quarterly MD&A against annual/semiannual promises, especially on strategy, project ramp, risks, and cash conversion. |
| non_recurring_profit_quality | Distinguish core operating profit from investment income, fair-value moves, subsidies, asset disposals, impairment, and other one-off items. | Not enough direct filing evidence found in the readable report pack. | Use this to prevent headline EPS from receiving a core multiple when profit quality depends on non-operating or non-recurring items. | Require a bridge from gross profit/operating profit to net profit, and isolate investment income, fair-value gains, subsidies, disposals, and impairments. |
| balance_sheet_forward_signals | Read balance-sheet leads before income-statement confirmation. | Not enough direct filing evidence found in the readable report pack. | Contract liabilities and payables can signal demand/funding; receivables, inventory, prepayments, debt, and CIP can signal execution burden. | Track whether leading assets/liabilities convert into revenue, margin, and cash rather than reversals, impairments, or financing drag. |
| shareholder_return_authenticity | Test whether dividends, buybacks, and capital returns are funded by durable profit and cash rather than leverage or asset sales. | Not enough direct filing evidence found in the readable report pack. | Treat shareholder yield as quality only when payout, FCF/OCF coverage, leverage, capex needs, and dilution risk line up. | Verify dividend payout, buyback execution/cancellation, FCF coverage, leverage movement, and whether capital needs crowd out future returns. |
| disclosure_quality_score | Grade whether filing disclosure is rich enough for a buy-side thesis or only a watchlist view. | Coverage grade weak; reports seen quarterly; answered 2/5; core pack thin. Readable text exists but the pack is too thin for a full buy-side read; avoid strong claims about business model, second curve, or execution trend. | High disclosure quality raises conviction; weak or partial coverage should cap sizing and push more assumptions into verification. | Improve confidence by retrieving missing annual/semiannual/quarterly text and answering unanswered thesis-critical filing questions. |

## Company-Specific Business Archetype
| archetype_id | archetype_name | evidence_strength | evidence_basis | underwriting_focus |
| --- | --- | --- | --- | --- |
| regulated_pipeline | 监管审批 / 产品管线型 | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报... | 验证管线阶段、获批概率、商业化能力、医保/集采价格压力和研发现金消耗。 |
| product_manufacturer | 产品制造 / 产能出货型 | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报... | 拆解量价成本、产品结构、产能利用率、库存、原材料和资本开支回报。 |
| resource_cycle | 资源周期 / 商品价格型 | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报... | 验证商品价格敏感性、产量、成本曲线、资源储量、扩产资本开支和现金分配。 |

## Growth Sustainability & Ramp Conditions
| growth_source | sustainability_read | evidence_strength | evidence_basis | ramp_conditions | falsification_signals | pm_use |
| --- | --- | --- | --- | --- | --- | --- |
| core_revenue_and_profit_engine | growth durability is not proven by the current readable filings; treat it as a verification item. | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | Revenue and profit can keep expanding only if the disclosed core engine keeps volume/price/utilization/customer growth while margins and cash conversion do not deteriorate. | Revenue growth decouples from gross margin, operating cash flow, receivables, inventory, contract liabilities, utilization, or disclosed customer/order evidence. | Use as the first growth paragraph in the PM memo: what has to remain true for consolidated revenue and profit growth to be sustainable. |
| segment_mix_and_profit_pool | segment mix can support growth only if higher-growth buckets are material and do not dilute margin or cash quality. | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | Track segment revenue scale, growth rate, margin/profit contribution, cash conversion, and valuation treatment separately instead of relying on consolidated growth. | High-growth segments remain too small, undisclosed, margin-dilutive, capital-intensive, or valued like the best segment without proof. | Use this as the bridge between Business Segment Breakdown and valuation/SOTP evidence gates. |
| archetype_ramp_regulated_pipeline | the primary business archetype sets the company-specific ramp variables; growth is only durable when those variables improve together. | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报告期，公司医药制造业务实现营业收入 38... | 验证管线阶段、获批概率、商业化能力、医保/集采价格压力和研发现金消耗。 | The next evidence pack fails on the archetype's own value drivers, even if headline revenue still grows. | Use as the company-specific final check before the bull/bear debate and PM rating. |

## Pre-Debate Underwriting Questions
| question_id | theme | underwriting_question | preliminary_answer | evidence_strength | evidence_basis | bull_debate_use | bear_debate_use | pm_integration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pre_debate_business_model | business_model | 一品红到底靠什么赚钱，收入、利润和资产之间如何形成经营闭环？ | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | Use disclosed core engine and segment mix to prove the thesis is tied to real economics, not a slogan. | Attack any rating that relies on an undefined or over-blended business model. | Put a concise business-model explanation before valuation and avoid using one blended multiple if segments differ. |
| pre_debate_moat | moat | 这家公司的护城河来自哪里，它能否保护价格、份额、租金、毛利率或客户粘性？ | No direct moat section or industry-specific moat evidence was found; treat moat as unproven until corroborated. | unanswered | No direct filing evidence found. | Support durable valuation only when filings show customer stickiness, network effect, cost advantage, brand, license, technology, or location advantage. | Challenge generic competitive-advantage language when it lacks numbers or transmission into returns. | Use this question to decide business quality and deserved valuation premium/discount. |
| pre_debate_archetype_regulated_pipeline | company_archetype | 核心价值来自已商业化产品，还是监管审批/临床管线的可选项？医保、集采、注册和商业化节奏如何改变利润曲线？ | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69... | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报... | 当管线进入商业化且价格/放量路径清晰时，可支持成长估值。 | 若审批、价格或商业化不确定性高，应把管线放在情景估值而非基准估值。 | PM报告应区分存量利润和管线期权。 |
| pre_debate_archetype_product_manufacturer | company_archetype | 这家公司增长来自价格、销量、产能利用率、产品结构还是成本下降？扩产、库存和原材料波动会怎样影响毛利率和现金流？ | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69... | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报... | 当产能利用率提升、产品结构升级、成本下降或订单支撑出货时，可支持盈利弹性。 | 若扩产先行、库存累积、原材料扰动或毛利率承压，应质疑增长质量。 | PM报告应围绕量价利和现金转换，而不是只引用收入增速。 |
| pre_debate_growth_driver | growth_driver | 未来增长主要来自价格、销量/客流、利用率/出租率、产能、客户、区域扩张，还是产品/服务结构升级？ | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 12 一品红药业集团股份有限公司 2026 年第一季度报告 客户存款和同业存放款项净增加额 | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 12 一品红药业集团股份有限公司 2026 年第一季度报告 客户存款和同业存放款项净增加额 | Use this to show which value driver can still beat market expectations. | Use this to expose where growth depends on unverified volume, price, utilization, or mix assumptions. | Tie valuation and rating to 3-6 named value drivers rather than generic growth. |
| pre_debate_second_curve | second_curve | 是否存在第二增长曲线？它已经变成收入、利润、订单、客户或现金流，还是仍停留在战略叙事？ | No monetized second-curve evidence was found; keep optionality out of base valuation unless other contexts prove it. | unanswered | No direct filing evidence found. | Promote second curves only when filings show monetization, contracted demand, users, capacity, customers, or cash conversion. | Challenge concept-only optionality, especially when capex or working capital rises before revenue proof. | Classify each second curve as core valuation, scenario/SOTP value, watch item, or narrative only. |
| pre_debate_cash_quality | cash_quality | 利润和收入能否转化为现金？应收、存货、预付款、合同负债或资本开支是否改变了增长质量？ | No direct cash-quality answer was found; structured statements may still be needed before conviction rises. | unanswered | No direct filing evidence found. | Use cash conversion and disciplined working capital to validate earnings quality. | Use working-capital absorption, weak OCF, or capex-before-proof to attack reported growth. | Let cash quality affect conviction, sizing, and safety-price work. |
| pre_debate_segment_valuation | valuation | 不同业务、地区、渠道或第二曲线应如何分开估值，而不是简单套一个合并PE/PB？ | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | Give premium credit only to segments with proven growth, margin, cash conversion, or scarcity. | Attack over-blending when low-quality or unproven businesses are valued like the best segment. | Use split valuation when segment evidence exists; otherwise state why a blended multiple is only a rough cross-check. |
| pre_debate_key_risks | risk | 哪些风险会真正改变股权价值，而不只是年报里的常规风险披露？ | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Use absence of material negative notes cautiously; it is not proof of safety unless coverage is strong. | Prioritize risks with direct financial transmission: impairment, litigation, guarantees, customer concentration, margin pressure, leverage, or policy exposure. | Put only decision-relevant risks into verification/falsification and avoid padding with boilerplate. |

## Selected Filing Question Playbook
| question_id | category | question | preferred_reports |
| --- | --- | --- | --- |
| bank_asset_quality | asset_quality | 不良率、关注类贷款、拨备覆盖和逾期迁徙是否在改善？ | quarterly/semiannual/annual |
| bank_nim | profitability | 净息差压力是否缓解，还是利润靠规模硬撑？ | quarterly/semiannual/annual |
| bank_fees | mix | 中收、零售、财富管理能否抵消传统息差压力？ | semiannual/annual |
| bank_capital | capital | 资本充足率、核心一级资本和风险加权资产是否支持扩表与分红？ | quarterly/semiannual/annual |
| bank_retail_book | loan_deposit_mix | 零售贷款、客户存款和财富管理规模是否仍支撑零售银行护城河？ | quarterly/semiannual/annual |

## Business Model Map
| lens | report_type | filing_evidence | why_it_matters |
| --- | --- | --- | --- |
| core_revenue_engine | quarterly | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | Defines what actually drives the income statement. |
| customer_and_channel | quarterly | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 子公司 Sobi US Holding Corp.（以下简称：Sobi 美国）签署并购协议，Sobi 美国拟以 9.5 亿美元首付款（折合人民币约 | Reveals demand source, concentration, and market validation. |
| reinvestment_engine | quarterly | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 2.报告期，公司自主研发投入 3,950.82 万元（含 AR882 Ⅲ期临床费用资本化金额 146.22 万元），占营业收入的 | Shows how today's cash is being converted into tomorrow's earnings power. |

## Segment Economics Pack
No filing-derived evidence snippets found.

## Business Segment Valuation Map
| business_bucket | report_type | filing_evidence | valuation_anchor | analyst_use | verification_need |
| --- | --- | --- | --- | --- | --- |
| core_revenue_engine | quarterly | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | Anchor the first valuation block on the mature revenue engine: normalized earnings, FCF yield, EV/EBITDA, PE, or peer-relative multiples depending on business model. | Use this as the company introduction before discussing optionality; every later segment should be compared with this core engine. | Confirm the core engine's revenue scale, margin, cash conversion, reinvestment need, and peer multiple range. |
| channel_mix | quarterly | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 子公司 Sobi US Holding Corp.（以下简称：Sobi 美国）签署并购协议，Sobi 美国拟以 9.5 亿美元首付款（折合人民币约 | Use as a sales-efficiency and working-capital modifier; do not value as a separate business unless channel economics are disclosed. | Use this to decide whether the company needs a split valuation rather than one blended multiple. | Check direct/dealer/platform split, take rate or gross margin, receivables, inventory burden, and customer acquisition cost. |

## Growth Vector Map
No filing-derived evidence snippets found.

## Deep Reading Excerpts
| report_type | section | excerpt | reading_purpose |
| --- | --- | --- | --- |
| quarterly | 主要会计数据和财务指标发生变动的情况及原因 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 司高质量发展。 2.报告期，公司自主研发投入 3,950.82 万元（含 AR88... | Check short-cycle proof or disproof. |
| quarterly | 经营活动产生的现金流量净额 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 18,712,971.40 38,342,797.32 二、投资活动产生的现金流量： 收回投资收到的现金 1,092,294,663.13 402,378,716.27 取得投资收益收到的现金 482,446,128.29 845,946.68 处置固定资产、无形资产和其他长 0.00 143,860.00 期资产收回的现金净额 处置子公司及其他营业单位收到的 | Check cash conversion. |

## Paragraph Reading Pack
| lens | report_type | section | reading_question | paragraph_excerpt | why_it_matters |
| --- | --- | --- | --- | --- | --- |
| short_cycle_execution | quarterly | 主要会计数据和财务指标发生变动的情况及原因 | Did the last quarter confirm or weaken the thesis? | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 司高质量发展。 2.报告期，公司自主研发投入 3,950.82 万元（含 AR882 Ⅲ期临床费用资本化金额 146.22 万元），占营业收入的 10.25%。2025 年 12 月，公司参股公司美国 Arthrosi 与瑞典 Swedish Orphan Biovitrum AB... | Turns quarterly reports into proof tests rather than headline snapshots. |

## Industry Reading Pack
No filing-derived evidence snippets found.

## Banking KPI Pack
| lens | report_type | evidence_strength | filing_evidence | why_it_matters | bear_check |
| --- | --- | --- | --- | --- | --- |
| retail_wealth_engine | quarterly | explicit disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 其中：应付利息 应付股利 应付手续费及佣金 | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| retail_wealth_engine | quarterly | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 已赚保费 手续费及佣金收入 二、营业总成本 395,749,176.13 396,925,091.87 | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| retail_wealth_engine | quarterly | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 手续费及佣金收入 二、营业总成本 395,749,176.13 396,925,091.87 | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| retail_wealth_engine | quarterly | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 手续费及佣金收入 二、营业总成本 395,749,176.13 396,925,091.87 其中：营业成本 130,761,559.02 146,832,079.62 | Retail AUM matters only when it converts into durable fee income and deposit stickiness. | Challenge AUM-led bulls if fees lag because of product mix or fee-rate compression. |
| loan_deposit_mix | quarterly | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 12 一品红药业集团股份有限公司 2026 年第一季度报告 客户存款和同业存放款项净增加额 | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |
| loan_deposit_mix | quarterly | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一品红药业集团股份有限公司 2026 年第一季度报告 客户存款和同业存放款项净增加额 | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |
| loan_deposit_mix | quarterly | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 一品红药业集团股份有限公司 2026 年第一季度报告 客户存款和同业存放款项净增加额 向中央银行借款净增加额 | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |
| loan_deposit_mix | quarterly | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动现金流入小计 353,301,172.61 335,042,257.61 购买商品、接受劳务支付的现金 135,572,760.43 43,057,007.27 客户贷款及垫款净增加额 | Loan/deposit mix explains whether franchise quality is improving or merely expanding the balance sheet. | Stress weak retail credit, mortgage, credit-card, or consumer-finance data when the thesis depends on retail banking. |

## Structured Balance-Sheet History
| end_date | ann_date | contract_liab | adv_receipts | contract_plus_adv | qoq_change | yoy_change | inventories | receivables | money_cap | liab_to_assets | analyst_read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260331 | 20260424 | 0.23亿元 | N/A | 0.23亿元 | -0.14亿元 (-38.4%) | -0.18亿元 (-43.8%) | 2.21亿元 | 2.87亿元 | 13.70亿元 | 58.0% | forward demand/liability signal available; inventory signal available; receivable signal available |
| 20251231 | 20260424 | 0.37亿元 | N/A | 0.37亿元 | +0.08亿元 (+26.1%) | -0.02亿元 (-5.8%) | 2.16亿元 | 2.05亿元 | 5.15亿元 | 65.2% | forward demand/liability signal available; inventory signal available; receivable signal available |
| 20250930 | 20251030 | 0.29亿元 | N/A | 0.29亿元 | +0.04亿元 (+16.4%) | -0.11亿元 (-27.4%) | 2.75亿元 | 3.82亿元 | 5.89亿元 | 60.3% | forward demand/liability signal available; inventory signal available; receivable signal available |
| 20250630 | 20250822 | 0.25亿元 | N/A | 0.25亿元 | -0.15亿元 (-37.7%) | -0.07亿元 (-22.2%) | 3.01亿元 | 4.13亿元 | 6.64亿元 | 62.5% | forward demand/liability signal available; inventory signal available; receivable signal available |
| 20250331 | 20250425 | 0.40亿元 | N/A | 0.40亿元 | +0.01亿元 (+3.2%) | N/A | 2.71亿元 | 4.61亿元 | 7.99亿元 | 62.1% | forward demand/liability signal available; inventory signal available; receivable signal available |
| 20241231 | 20250425 | 0.39亿元 | N/A | 0.39亿元 | -0.01亿元 (-2.9%) | N/A | 2.87亿元 | 3.49亿元 | 4.69亿元 | 56.0% | forward demand/liability signal available; inventory signal available; receivable signal available |
| 20240930 | 20241030 | 0.40亿元 | N/A | 0.40亿元 | +0.08亿元 (+24.7%) | N/A | 2.70亿元 | 3.82亿元 | 6.58亿元 | 51.1% | forward demand/liability signal available; inventory signal available; receivable signal available |
| 20240630 | 20240829 | 0.32亿元 | N/A | 0.32亿元 | N/A | N/A | 3.56亿元 | 2.89亿元 | 4.42亿元 | 43.7% | forward demand/liability signal available; inventory signal available; receivable signal available |

## Statement Table Reading Pack
No filing-derived evidence snippets found.

## Filing Note Reading Pack
| note_type | importance | note_evidence | why_it_matters | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- |
| impairment_policy | supporting | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Provisioning language explains whether accounting conservatism is strengthening or weakening. | Use conservative provisioning only when it lowers future surprise risk. | Use aggressive assumptions or rising provisions to challenge earnings quality. |
| impairment_policy | supporting | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Provisioning language explains whether accounting conservatism is strengthening or weakening. | Use conservative provisioning only when it lowers future surprise risk. | Use aggressive assumptions or rising provisions to challenge earnings quality. |
| capitalized_development | supporting | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 司高质量发展。 2.报告期，公司自主研发投入 3,950.82 万元（含 AR882 Ⅲ期临床费用资本化金额 146.22 万元... | Capitalized development can shift current profit at the cost of later amortization risk. | Use with commercialization evidence to support platform investment. | Challenge profit quality if capitalization rises ahead of monetization. |
| capitalized_development | supporting | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 司高质量发展。 2.报告期，公司自主研发投入 3,950.82 万元（含 AR882 Ⅲ期临床费用资本化金额 146.22 万元），占营业收入的 | Capitalized development can shift current profit at the cost of later amortization risk. | Use with commercialization evidence to support platform investment. | Challenge profit quality if capitalization rises ahead of monetization. |

## Financial Relationship Reading Pack
No filing-derived evidence snippets found.

## Filing Textual Signals
| signal_type | report_type | wording_stage | textual_evidence | investment_read | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| risk_language_upgrade | quarterly | risk-language | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| risk_language_upgrade | quarterly | risk-language | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| management_claim_with_evidence | quarterly | proof-backed | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 应交税费 28,946,943.23 7,596,401.58 281.06% 增加所致。 主要是报告期按合同正常支付购买 | Management language has a harder evidence bridge; debate materiality and economics rather than existence. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| management_claim_with_evidence | quarterly | proof-backed | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 增加所致。 主要是报告期按合同正常支付购买 其他应付款 339,998,784.99 260,665,090.71 30.44% 非流动资产待付款造成余额增加所 | Management language has a harder evidence bridge; debate materiality and economics rather than existence. | Use only after linking wording to disclosed orders, customers, revenue, capacity, or cash conversion. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |

## Filing Insight Distillation Layer
| insight_type | analyst_question | distilled_read | evidence_basis | debate_use | what_would_change_mind |
| --- | --- | --- | --- | --- | --- |
| core_business_engine | What actually drives this company's revenue and profit pool? | Start the memo from the operating engine disclosed in filings, not from market labels, hot themes, or valuation screens. | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 | Forces bulls and bears to debate the real business before discussing optionality. | A segment disclosure or order/customer evidence showing a different profit engine has become material. |
| textual_filing_signal | What is management language trying to prove, soften, or avoid? | Risk wording deserves explicit bearish debate if it has become more concrete or financially relevant. | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Use wording as a debate input: hard wording must still clear materiality; soft wording needs proof; risk wording can cap valuation. | Challenge vague, unquantified, repetitive, or risk-upgraded language before it enters valuation. |
| core_debate_item | Which filing-derived point must enter the bull/bear debate? | Direct filing answer for mix. | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 支出 其他符合非经常性损益定义的损益项 327,030.00 主要是个税手续费返还。 | Do not leave this as background context; make it one of the main debate pillars. | Question whether fee income is cyclical or shrinking. |
| filing_read_confidence_gap | Can we trust a strong conclusion from the available filings? | Readable text exists but the pack is too thin for a full buy-side read; avoid strong claims about business model, second curve, or execution trend. | Coverage: weak; reports seen: quarterly | Cap conviction and explicitly name missing report types or unanswered thesis-critical questions. | Retrieve annual/semiannual/quarterly text and answer the core playbook with quantified evidence. |

## Core Discussion Promotion Queue
| topic | priority | evidence_basis | why_it_matters | valuation_treatment | verification_need |
| --- | --- | --- | --- | --- | --- |
| bank_fees | core | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 支出 其他符合非经常性损益定义的损益项 327,030.00 主要是个税手续费返还。 | Direct filing answer for mix. | core debate candidate | Question whether fee income is cyclical or shrinking. |
| capitalized_development | supporting | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 司高质量发展。 2.报告期，公司自主研发投入 3,950.82 万元（含 AR882 Ⅲ期临床费用资本化金额 146.22 万元... | Capitalized development can shift current profit at the cost of later amortization risk. | risk/governance modifier | Challenge profit quality if capitalization rises ahead of monetization. |
| impairment_policy | supporting | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 非流动性资产处置损益（包括已计提 582,219,801.27 主要是转让 Arthrosi 股权所致。 资产减值准备的冲销部分） | Provisioning language explains whether accounting conservatism is strengthening or weakening. | risk/governance modifier | Use aggressive assumptions or rising provisions to challenge earnings quality. |

## Unanswered Filing Questions
| question_id | category | question | why_it_matters |
| --- | --- | --- | --- |
| bank_asset_quality | asset_quality | 不良率、关注类贷款、拨备覆盖和逾期迁徙是否在改善？ | Still unresolved in the latest readable filings; Challenge hidden deterioration before it hits profits. |
| bank_nim | profitability | 净息差压力是否缓解，还是利润靠规模硬撑？ | Still unresolved in the latest readable filings; Attack profitability if volume masks spread compression. |
| bank_capital | capital | 资本充足率、核心一级资本和风险加权资产是否支持扩表与分红？ | Still unresolved in the latest readable filings; Challenge expansion or dividend claims if RWA growth consumes capital. |

## Question-Driven Filing Answers
| question_id | report_type | question | evidence_strength | filing_answer | bull_use | bear_use |
| --- | --- | --- | --- | --- | --- | --- |
| bank_fees | quarterly | 中收、零售、财富管理能否抵消传统息差压力？ | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 支出 其他符合非经常性损益定义的损益项 327,030.00 主要是个税手续费返还。 | Support business diversification. | Question whether fee income is cyclical or shrinking. |
| bank_retail_book | quarterly | 零售贷款、客户存款和财富管理规模是否仍支撑零售银行护城河？ | quantified disclosure | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 12 一品红药业集团股份有限公司 2026 年第一季度报告 客户存款和同业存放款项净增加额 | Support the retail-bank moat when deposit and AUM growth remain healthy. | Challenge the moat if retail loan demand or deposit quality deteriorates. |

## Material Filing Findings
No filing-derived evidence snippets found.

## Report-to-Report Bridge
| topic | long_cycle_evidence | checkpoint_evidence | bridge_status | bridge_read | analyst_read |
| --- | --- | --- | --- | --- | --- |
| orders_and_visibility |  | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 合同负债 22,508,895.44 36,569,663.95 | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Does the short-cycle report confirm the demand visibility described in long-cycle filings? |
| pricing_and_margin |  | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 营业成本 130,761,559.02 146,832,079.62 -10.94% | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Does the latest checkpoint validate or weaken the prior margin story? |
| cash_conversion |  | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 预付款项 12,794,877.52 9,999,713.42 27.95% | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Do newer filings show profits turning into cash? |
| capital_intensity |  | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 在建工程 12,218,333.66 8,087,436.13 | short-cycle-signal-without-long-cycle-anchor | new-short-cycle-signal | Is reinvestment translating into visible operating progress? |

## Company-Specific Watch Questions
| question_id | question | times_seen | last_seen | last_report_type |
| --- | --- | --- | --- | --- |
| bank_fees | 中收、零售、财富管理能否抵消传统息差压力？ | 1 | 2026-08-08 | quarterly |
| bank_retail_book | 零售贷款、客户存款和财富管理规模是否仍支撑零售银行护城河？ | 1 | 2026-08-08 | quarterly |

## Filing-Derived Operating Evidence
| category | signal | filing_evidence | bull_use | bear_use |
| --- | --- | --- | --- | --- |
| bank_retail_wealth | 手续费 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 327,030.00 主要是个税手续费返还。 | Use wealth-management monetization and retail franchise scale to support fee resilience. | Test whether AUM growth is translating into fee income or being offset by fee-rate compression. |
| bank_retail_wealth | 手续费 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 个税扣缴手续费返还 327,030.00 | Use wealth-management monetization and retail franchise scale to support fee resilience. | Test whether AUM growth is translating into fee income or being offset by fee-rate compression. |
| bank_retail_wealth | 手续费 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 含手续费）回购 316.22 万股，占公司总股本的 0.70%。 | Use wealth-management monetization and retail franchise scale to support fee resilience. | Test whether AUM growth is translating into fee income or being offset by fee-rate compression. |
| bank_balance_sheet_mix | 客户存款 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 客户存款和同业存放款项净增加额 | Use loan/deposit mix to connect franchise quality to NIM and asset-quality outcomes. | Challenge retail-bank quality if weak mortgage, credit-card, or consumer-loan data undermine the core engine. |
| bank_balance_sheet_mix | 客户贷款 | 一品红药业集团股份有限公司 2026 年第一季度报告 [local disclosure cache]: 客户贷款及垫款净增加额 | Use loan/deposit mix to connect franchise quality to NIM and asset-quality outcomes. | Challenge retail-bank quality if weak mortgage, credit-card, or consumer-loan data undermine the core engine. |

## Analyst Instructions
- Start with the filing reading coverage audit. If coverage is partial, weak, or failed, explicitly downgrade confidence before using any filing-derived thesis.
- Use the Internal Filing Quality Modules as a ten-part filing-only review: accounting reconciliation, segment economics, footnote radar, cash-flow quality, capex/CIP return bridge, MD&A text change, non-recurring profit quality, balance-sheet forward signals, shareholder-return authenticity, and disclosure quality. The final PM memo should integrate these into PM Summary, Investment Thesis, Valuation, Risk, and Verification rather than dumping a checklist.
- Use the Growth Sustainability & Ramp Conditions table before assigning upside or downside. For each company, explain whether revenue and profit growth are sustainable, what must happen for growth to keep ramping, which evidence is already verified, and what would falsify the growth thesis.
- Use the Pre-Debate Underwriting Questions before the bull/bear debate. These are the company-specific buy-side questions that should frame the debate: business model, moat, growth driver, second curve, cash quality, segment valuation, and decision-relevant risks. Bulls and bears should answer or attack these questions directly rather than debating generic sector slogans.
- Use Structured Balance-Sheet History as the second-layer financial-statement proof for contract liabilities/advance receipts, inventory, receivables, cash, and leverage. If this table is ready, do not call contract liabilities or working-capital history missing merely because the PDF narrative excerpt did not mention it.
- Read quarterly reports for confirmation or reversal of short-cycle signals; read half-year reports for trend formation and segment mix; read annual reports for business model, capital allocation, and long-cycle risk.
- Start with the business model map, then use the growth vector map to separate mature engines from emerging second curves.
- For multi-product or multi-region companies, read the Segment Economics Pack before the bull/bear debate. Do not collapse a company into headline revenue or profit when annual/half-year filings disclose product, geography, channel, revenue, cost, gross margin, or growth-rate splits.
- Use the Business Segment Valuation Map to build a split valuation before applying a blended multiple. Value mature/core businesses on normalized earnings, FCF, EV/EBITDA, PE, or peer-relative multiples; value emerging or second-curve businesses with SOTP/scenario treatment until segment revenue, margin, capex/utilization, customers, and cash conversion are proven.
- For unfamiliar companies, first explain the main business from filings, then split the investment case into disclosed business buckets. Do not discuss new businesses as free optionality unless the map shows filing-backed monetization or a clear verification path.
- Use the deep-reading excerpts as source text, not decorative context: annual-report excerpts define the company, semiannual excerpts test trend formation, and quarterly excerpts test short-cycle execution.
- Use the paragraph reading pack for genuine report reading: answer the paragraph-level question first, then decide whether the business model, second curve, moat, trend, or cash-conversion thesis changed.
- Use the industry reading pack as the specialist layer: the same filing should be read through the value drivers that matter for that business model, then linked to the external inputs named in `connect_to` before forming a conclusion.
- Use the statement table reading pack for the hard-accounting layer: contract liabilities, receivables, inventory, prepayments, capex, investment assets, operating cash flow, and impairment rows often decide whether the narrative survives contact with the numbers.
- Use the filing note reading pack for footnote discipline: customer concentration, related parties, guarantees, litigation, impairment assumptions, and capitalization policies often reveal risks that the headline statements hide.
- Use the financial relationship reading pack to connect the statements rather than reading metrics in isolation. Revenue growth only deserves praise if margin, cash conversion, and balance-sheet demands make sense together.
- Use the filing textual signals layer to read management wording strength, risk-language upgrades, abnormal silence, and strategic promises. Hard wording still needs materiality; soft wording belongs in scenarios/watchlist; risk wording can cap valuation. Keep a concise textual-signal module in the manager report when it changes the thesis.
- Use the filing insight distillation layer before writing the final thesis. It converts raw filing snippets into buy-side questions: core engine, second curve, quality of growth, monetization gap, capital allocation, and tail risk. The manager report should read like a company memo, not a list of disconnected data points.
- Start from the selected question playbook, then answer only with evidence actually found in filings.
- For banks, start from the Banking KPI Pack and the banking playbook. Do not use contract liabilities, inventory, gross margin, capex, or generic OCF conversion as core bank-quality evidence unless a bank-specific disclosure explicitly makes them decision-relevant.
- For banks, preserve the exact spread terminology from filings: `净利息收益率`, `净息差`, and `净利差` are not interchangeable. If the filing only supports 净利差 1.77% and 净利息收益率 1.83%, do not invent or substitute a 1.40%/1.50% NIM number. Treat NIM stabilization as conditional until the next filing confirms spread, loan yield, and deposit-cost movement together.
- Use the core discussion promotion queue as the bridge from reading to investing: core items should enter bull/bear debate, supporting items should reinforce or challenge a thesis, scenario items belong in upside/downside cases, and watch items stay out of base-case valuation until upgraded.
- Treat unanswered filing questions as neutral non-evidence and explicit retrieval tasks. State what disclosure would close each gap; do not mechanically reduce or raise the rating or conviction tier.
- Promote materially decision-relevant findings such as signed long-term agreements, named customers, take-or-pay/offtake signals, capacity-to-demand bridges, and commercialization milestones into the core debate rather than leaving them buried as generic snippets.
- Use the report-to-report bridge to ask whether annual/semiannual narratives are being confirmed, weakened, or still waiting for quarterly proof.
- Treat annual reports, half-year reports, and quarterly reports as a linked evidence chain: annual reports define the long-cycle thesis, half-year reports test trend formation, and quarterly reports confirm, weaken, or leave unresolved the latest checkpoint.
- Treat quantified disclosures as stronger than explicit but unquantified statements, and both as stronger than management narrative.
- Use company-specific watch questions to maintain continuity across runs: the system should remember what has repeatedly mattered for this company.
- Bulls should use this layer to support visibility, monetization, moat, and inflection; bears should use it to test margin quality, working capital, capital intensity, governance, and tail risk.