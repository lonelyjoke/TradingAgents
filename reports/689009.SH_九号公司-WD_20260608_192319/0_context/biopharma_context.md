# Biopharma verification context for 689009.SH as of 2026-06-08

- Status: triggered
- Company: 九号公司-WD
- Tushare industry: 摩托车
- Business model: innovative-drug company
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
| Reimbursement / pricing | 医保目录/NRDL, national and provincial procurement, official tender/platform prices | access, negotiated price, volume trade-off, margin pressure, competitive intensity | commercial ramp and margin input; missing price data caps conviction |
| Clinical readouts | ASCO/ESMO/ASH/AACR abstracts, peer-reviewed papers, conference presentations | ORR, PFS, OS, DOR, AE/SAE, discontinuation, subgroup, line of therapy | evidence quality depends on trial design, maturity, sample size, and comparator |

## Asset / Evidence Gate
| bucket | must_verify | source | valuation_rule |
| --- | --- | --- | --- |
| Approved commercial assets | approved indication, label breadth, sales ramp, reimbursement, gross margin, competition | filings, CDE/NMPA/FDA/EMA labels, NRDL/procurement, product sales disclosure | base valuation can use revenue/profit contribution when sales evidence exists |
| Label expansion / late-stage trials | phase, endpoint, comparator, enrollment, primary completion, regulatory path | ClinicalTrials.gov/CDE, official pipeline, conference abstract | risk-adjusted NPV; catalyst timing is a watch item until official |
| Early pipeline | mechanism, differentiation, safety signal, sample size, competitive landscape | trial registry, abstracts, company R&D disclosure | scenario optionality; do not let Phase I/II drive base-case valuation |
| BD / licensing | upfront/milestone/royalty terms, territory, economics retained, partner quality | official announcement and filing treatment | SOTP/rNPV only for retained economics; avoid double-counting product sales and royalties |

## Filing Text Evidence Snippets
| report | snippet |
| --- | --- |
| 九号有限公司2026年第一季度报告 | ...净利润 经营活动产生的现金流量净额 -476,552,990.04 1,567,547,615.43 -130.40 基本每股收益（元/股） 2.83 6.36 -55.50 基本每份存托凭证收益（元/份） 0.28 0.64 -55.50 稀释每股收益（元/股） 2.66 5.62 -52.67 稀释每份存托凭证收益（元/份） 0.27 0.56 -52.67 加权平均净资产收益率（%） 2.79 7.12 减少 4.33 个百分点 研发投入合计 371,103,561.06 253,036,196.48 46.66 1/12 九号有限公司2026 年第一季度报告 研发投入占营业收入的比例（%） 6.32 4.95 增加 1.37 个百分点 本报告期末比上年度 本报告期末 上年度末 末增减变动幅度(%) 总资产 20,655,466,166.78 21,519,835,957.95 -4.02 归属于上市公司股东的所有者权益 7,403,707,144.97 7,1... |
| 九号有限公司2025年第三季度报告 | ...2.51 84.45 稀释每股收益（元/股） 7.20 52.28 23.69 93.43 稀释每份存托凭证（元/份） 0.72 52.28 2.37 93.43 增加 0.50 增加 5.98 加权平均净资产收益率（%） 7.15 23.12 个百分点 个百分点 1/12 九号有限公司2025 年第三季度报告 本报告期比 年初至报告 上年同期增 期末比上年 项目 本报告期 年初至报告期末 减变动幅度 同期增减变 (%) 动幅度(%) 研发投入合计 349,236,118.05 75.85 871,644,924.42 59.06 研发投入占营业收入的比 增加 0.56 减少 0.29 5.25 4.74 例（%） 个百分点 个百分点 本报告期末 比上年度末 本报告期末 上年度末 增减变动幅 度(%) 总资产 20,615,596,975.34 15,677,918,996.62 31.49 归属于上市公司股东的所 7,119,734,553.72 6,156,282... |

## Manager Treatment
- Separate commercialized products, label-expansion catalysts, clinical pipeline, BD economics, and cash runway before valuing the company.
- Commercial assets can enter base valuation only when sales/reimbursement/label evidence is present; clinical assets should use risk-adjusted NPV or scenario optionality.
- Do not treat Phase I/II, conference abstracts, or management pipeline wording as base-case earnings without trial quality, regulatory path, and competitive context.
- For CRO/CDMO/pharma-services names, analyze order visibility, customer funding, capacity utilization, geopolitical risk, and FCF; do not value them like drug-owner pipelines.
- Missing clinical-trial IDs, regulatory status, reimbursement/price data, or product sales is a research gap that caps conviction rather than a reason to invent numbers.