# Biopharma verification context for 002460.SZ as of 2026-06-11

- Status: triggered
- Company: 赣锋锂业
- Tushare industry: 小金属
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
| 2025年年度报告 | ...25 年年度报告全文 （包括能源、原材料及劳动力成本）、运输成本变动、汇率变动、商品库存 以及技术发展。2021 年锂产品价格上涨至历史新高后回落，2025 年上半年锂 产品价格探底后开始回升，如果未来锂产品价格波动，将对公司的业务、财 务状况及经营业绩产生重大影响。 应对措施：公司在产品端优化生产流程，技术升级和工艺优化降低生产 成本；在资源端优化锂矿运营，加快和推动低成本锂资源的建设和投产，进 一步优化公司锂资源的供应及成本结构；在研发端加大研发投入，开发高附 加值锂产品，提升市场竞争力，积极布局固态电池、锂回收等领域，抢占市 场先机；在财务端加强现金流管理，发行境内外债务融资工具优化债务结构， 拓宽融资渠道，降低融资成本，确保公司运营资金充足；通过展开商品期货 期权套期保值业务，有效对冲产品价格波动风险，降低对公司经营的不利影 响，充分利用套期保值的避险机制，增强财务稳健性，保障公司经营业务的 发展。公司通过产品端升级、资源端降本、研发端提升、财务端管控、商品 ... |

## Manager Treatment
- Separate commercialized products, label-expansion catalysts, clinical pipeline, BD economics, and cash runway before valuing the company.
- Commercial assets can enter base valuation only when sales/reimbursement/label evidence is present; clinical assets should use risk-adjusted NPV or scenario optionality.
- Do not treat Phase I/II, conference abstracts, or management pipeline wording as base-case earnings without trial quality, regulatory path, and competitive context.
- For CRO/CDMO/pharma-services names, analyze order visibility, customer funding, capacity utilization, geopolitical risk, and FCF; do not value them like drug-owner pipelines.
- Missing clinical-trial IDs, regulatory status, reimbursement/price data, or product sales is a research gap that caps conviction rather than a reason to invent numbers.