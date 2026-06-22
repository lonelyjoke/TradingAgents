# Forward Forecast Model Scaffold for 600036.SH as of 2026-06-22

- Purpose: prevent valuation from being a loose multiple paragraph. The public report should show how operating drivers become revenue, profit, EPS, and cash flow.

## Evidence Base Already Present
- # Company Business Model Primer for 600036.SH as of 2026-06-22
- - Purpose: make the reader understand how the company earns money before valuation or cycle language.
- - / project_delivery / 项目订单 / 交付回款型 / quantified disclosure / 徐工集团工程机械股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流量净额 153.12% 报告期内加强应收账款管理并规范采购及运营支出 投资活动产生的现金流量净额 -38.29% 报告期内保证金金额变动影响 筹资活动产生的现金流量净额 49.07% 报告期内收到员工股权激励认股款 二、股东信息 （一） 普通股股东总数和表决权恢复的...
- - / core_revenue_engine / quarterly / 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 / Defines what actually drives the income statement. /
- ## Segment Economics / Profit Pools
- ## Segment Valuation / Evidence Gates
- - / business_bucket / report_type / filing_evidence / valuation_anchor / analyst_use / verification_need /
- - / core_revenue_engine / quarterly / 西部矿业股份有限公司2026 年第一季度报告 [local disclosure cache]: 2026 年 1-3 月，公司实现营业收入 187.24 亿元，较上年同期增加 13.19%，实现利润总额 28.92 / Anchor the first valuation block on the mature revenue engine: normalized earnings, FCF yield, EV/EBITDA, PE, ...
- - / emerging_or_second_curve / filing / 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 经营活动产生的现金流 报告期内，主要系销售回款增 2,116,658,463.16 423,857,775.27 399.38% 量净额 加及出口退税增加所致。 / Treat as SOTP/scenario value when stage is planned; include in base-case valuation...
- - / geography_or_export_lane / quarterly / 胜宏科技（惠州）股份有限公司 2026 年第一季度报告 [local disclosure cache]: 量净额 加及出口退税增加所致。 / Use as a growth/margin modifier for the core business; only value separately when regional revenue, margin, and regulatory risk are disclosed. /...

## Driver Bridge
| Forecast line | Formula / bridge | Required assumptions |
| --- | --- | --- |
| Mining revenue | equity output by metal x realized selling price | reserve grade, recovery rate, mine life, ramp schedule, realized price versus SHFE/LME/COMEX proxy |
| Smelting / refining spread | processed volume x TC/RC or processing margin | concentrate supply, treatment/refining charges, utilization, power and energy cost |
| Trading / pass-through revenue | traded volume x thin gross spread | inventory exposure, customer credit, working-capital intensity; do not value like scarce resources |
| Gross profit | mining gross profit + smelting spread + by-product credits - unit cash/AISC cost | cash cost, AISC/unit cost, sustaining capex, FX, energy/labor, product mix |
| NAV / SOTP value | mine-by-mine NAV + smelting/trading earnings value + project optionality | capex, construction-in-progress, commissioning, permitting, jurisdiction risk, discount/haircut |
| net profit/EPS / FCF | operating profit - tax/minority/finance cost + working-capital/capex bridge | minority interest, debt maturity, OCF/NI, hedging/derivatives, inventory marks |

## Mandatory Three-Year Table
| item | 2026E | 2027E | 2028E | evidence / assumption status |
| --- | --- | --- | --- | --- |
| Revenue | to be estimated | to be estimated | to be estimated | tie to segment volume, ASP, and mix |
| Gross margin | to be estimated | to be estimated | to be estimated | tie to price/spread, cost, utilization, and mix |
| Operating expense ratio | to be estimated | to be estimated | to be estimated | tie to R&D, sales, admin, and scale leverage |
| Net profit / EPS | to be estimated | to be estimated | to be estimated | tie to tax, minority, non-recurring, and share count |
| Operating cash flow / FCF | to be estimated | to be estimated | to be estimated | tie to working capital and capex |

## Analyst Instructions
- A Buy/Overweight call should identify which two or three assumptions drive most of the upside.
- Do not cite target price, safety price, or re-rating multiple without showing the earnings/cash-flow bridge behind it.
- If only a run-rate quarter is available, label it as run-rate or stress/base scenario, not as a full forecast.
- Knowledge Planet can supply private/proxy assumptions, but each assumption must be tagged and reconciled with filings, public prices, Tushare data, or a verification calendar before it changes valuation.