# Biopharma verification context for 300723.SZ as of 2026-08-08

- Status: triggered
- Company: 一品红
- Tushare industry: 化学制药
- Business model: CRO/CDMO pharma-services company
- Trigger reason: company name / Tushare industry / filing text contains biopharma terms

## Company Watchlist
- approved products and commercial ramp
- late-stage pipeline and label expansion
- regulatory review and reimbursement milestones
- R&D spend, cash runway, and dilution risk

## Source Priority And Data Acquisition
| data_bucket | source | use | valuation_treatment |
| --- | --- | --- | --- |
| Company filings / IR | annual/interim reports, exchange announcements, investor presentations, official pipeline pages | segment revenue, R&D spend, cash runway, product sales, disclosed milestones, management wording | filing-grade base evidence; still separate disclosed fact from forward assumption |
| Clinical trials | ClinicalTrials.gov, CDE trial registration, company trial registry when official | NCT/registration ID, phase, enrollment, status, primary completion, endpoint, comparator | pipeline risk-adjusted NPV input; Phase I/II normally optionality, not base earnings |
| Regulatory | CDE/NMPA, FDA, EMA, labels, review decisions, approved indications | NDA/BLA/MAA acceptance, approval, label breadth, safety warnings, review timing | official catalyst evidence; do not treat media speculation as approval proof |
| Reimbursement / pricing | 医保目录/NRDL, national and provincial procurement, official tender/platform prices | access, negotiated price, volume trade-off, margin pressure, competitive intensity | commercial ramp and margin input; missing price data remains a neutral retrieval task |
| Clinical readouts | ASCO/ESMO/ASH/AACR abstracts, peer-reviewed papers, conference presentations | ORR, PFS, OS, DOR, AE/SAE, discontinuation, subgroup, line of therapy | evidence quality depends on trial design, maturity, sample size, and comparator |
| CRO/CDMO demand | company filings, customer concentration disclosure, order/backlog commentary, capex/utilization evidence | customer funding cycle, backlog visibility, project conversion, geopolitical restrictions | service-cycle and FCF evidence; do not value like a drug-owner pipeline |

## Asset / Evidence Gate
| bucket | must_verify | source | valuation_rule |
| --- | --- | --- | --- |
| Drug discovery / CRO | customer demand, new project flow, pricing, cancellation, client concentration | filings, IR, customer funding trend, official order/backlog commentary | service revenue/FCF multiple; no pipeline rNPV unless the company owns the asset economics |
| CDMO capacity | capacity utilization, ramp schedule, capex returns, large-project conversion | filings, capex/CIP, segment margin, management commentary | cycle and utilization sensitivity; capex without utilization is not growth proof |
| Geopolitical risk | affected revenue/customer mix, legal status, mitigation plan, order behavior | official filings, risk disclosures, customer/geography segment data | scenario haircut to revenue visibility, multiple, and cash-flow durability |

## Filing Text Evidence Snippets
| report | snippet |
| --- | --- |
| 2026年一季度报告 | ...解释性公告第 1 号——非经常性损益》中列举的非经常性损益项目界定为 经常性损益的项目的情形。 （三） 主要会计数据和财务指标发生变动的情况及原因 适用 □不适用 2026 年第一季度，公司实现营业收入 38,546.83 万元，同比增长 2.26%；实现归属于上市公司股东的净利润 59,437.57 万元，同比增加 950.35%；实现归属于上市公司股东扣非后净利润-269.32 万元，同比下降 117.73%。 1. 报告期，公司医药制造业务实现营业收入 38,015.01 万元，同比增加 1.69%。公司持续通过营销体系优化，推动公 司高质量发展。 2.报告期，公司自主研发投入 3,950.82 万元（含 AR882 Ⅲ期临床费用资本化金额 146.22 万元），占营业收入的 10.25%。2025 年 12 月，公司参股公司美国 Arthrosi 与瑞典 Swedish Orphan Biovitrum AB （pub1）（SOBI.ST）下属全资 子公司 ... |
| 2025年年度报告 | ...、完整。 所有董事均已出席了审议本报告的董事会会议。 1、报告期，公司实现销售收入 93,227.05 万元，同比下降 35.72%，影 响了公司经营业绩达成。 2、报告期，2025 年度非经常性损益对净利润的影响金额为 4,174.87 万 元；主要是计入当期损益的政府补助 6,686.94 万元，公司持有金融资产和金 融负债产生的公允价值变动损益以及处置金融资产和金融负债产生的损益- 3,015.33 万元及其他综合因素所致。 1.药品研发风险。医药行业研发具有高技术、高投入、高风险、长周期 特点，药品研发存在许多不确定性风险。面对上述风险，公司通过自主研发、 合作研发等多种创新机制，不断提升创新药研发能力，并建立产学研联合体， 实现研发、生产良性循环。同时紧跟产品技术、政策法规及市场环境的动态 变化，培养高效研发团队，持续在儿童药和慢病药领域产品管线丰富上取得 新突破。但是公司药品研发能否成功仍可能存在不及预期的风险。 2 一品红药业集团股份有限公司 2025 ... |
| 2025年半年度报告 | ... 月 1 一品红药业集团股份有限公司 2025 年半年度报告全文 第一节 重要提示、目录和释义 公司董事会、监事会及董事、监事、高级管理人员保证半年度报告内容 的真实、准确、完整，不存在虚假记载、误导性陈述或者重大遗漏，并承担 个别和连带的法律责任。 公司负责人李捍雄、主管会计工作负责人张辉星及会计机构负责人(会计 主管人员)张辉星声明：保证本半年度报告中财务报告的真实、准确、完整。 所有董事均已出席了审议本次半年报的董事会会议。 1.药品研发风险。医药行业研发具有高技术、高投入、高风险、长周期 特点，其中临床前研究、临床研究到产品注册各个阶段充满挑战，存在研发 产品获批不确定性风险。面对上述风险，公司通过自主研发、合作研发等多 种创新机制，不断提升创新药研发能力，并建立产学研联合体，实现研发、 生产良性循环。同时紧跟治疗领域、政策法规及竞争环境的动态变化，培养 高效研发团队，持续在儿童药和慢病药领域产品管线丰富上取得新突破。但 是公司药品研发能否成功仍可能存在不及预... |

## Manager Treatment
- Separate commercialized products, label-expansion catalysts, clinical pipeline, BD economics, and cash runway before valuing the company.
- Commercial assets can enter base valuation only when sales/reimbursement/label evidence is present; clinical assets should use risk-adjusted NPV or scenario optionality.
- Do not treat Phase I/II, conference abstracts, or management pipeline wording as base-case earnings without trial quality, regulatory path, and competitive context.
- For CRO/CDMO/pharma-services names, analyze order visibility, customer funding, capacity utilization, geopolitical risk, and FCF; do not value them like drug-owner pipelines.
- Missing clinical-trial IDs, regulatory status, reimbursement/price data, or product sales is a neutral research gap. Do not invent numbers or mechanically alter the rating.