"""General operating-model archetypes used by industry-specific research.

The seven public chapters stay stable across companies.  What changes is the
economic model underneath each material business unit.  This module provides
a small deterministic registry that gives the LLM the right revenue, profit,
cash, competition and valuation questions without pretending that a vendor
industry label is itself a business model.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class OperatingArchetypeProfile:
    profile_id: str
    name: str
    keywords: tuple[str, ...]
    revenue_equation: str
    profit_equation: str
    cash_equation: str
    mandatory_kpis: tuple[str, ...]
    competition_dimensions: tuple[str, ...]
    valuation_methods: tuple[str, ...]
    falsification_gates: tuple[str, ...]


OPERATING_ARCHETYPES: tuple[OperatingArchetypeProfile, ...] = (
    OperatingArchetypeProfile(
        "branded_consumer_channel",
        "branded consumer / distributor channel",
        ("consumer", "beverage", "food", "brand", "distributor", "retail terminal", "饮料", "食品", "品牌", "经销", "终端", "动销"),
        "effective outlets x sell-through per outlet x realized ASP x product mix",
        "category revenue x category gross margin - promotion - channel support - selling overhead",
        "operating profit + D&A - inventory/receivable build +/- distributor prepayments - capex",
        ("category volume and ASP", "outlet coverage and same-outlet productivity", "sell-in/sell-through/inventory", "repeat purchase and cannibalization", "promotion and selling-expense ROI"),
        ("consumption occasion", "price-pack architecture", "brand consideration", "channel profit", "shelf/cold-box control", "competitor promotion response"),
        ("PE with growth-quality cross-check", "DCF/FCF", "SOTP for unproven second curves"),
        ("core SKU share or repeat purchase deteriorates", "new products require persistently uneconomic promotion", "cash conversion decouples from earnings"),
    ),
    OperatingArchetypeProfile(
        "retail_chain",
        "retail / store network",
        ("retail", "store", "restaurant", "hotel", "pharmacy", "门店", "零售", "餐饮", "酒店", "药店", "同店"),
        "store count x same-store traffic x conversion x average ticket",
        "store gross profit - labor - rent - fulfillment - marketing - headquarters cost",
        "store EBITDA - working capital - maintenance/growth capex - lease cash obligations",
        ("net openings and closures", "same-store sales", "traffic/conversion/ticket", "store cohort payback", "inventory turns and shrink"),
        ("format and location", "price/value", "assortment", "supply chain", "member loyalty", "local density"),
        ("EV/EBITDA", "DCF", "PE after lease/accounting normalization"),
        ("mature-store economics weaken", "new-store payback extends", "closures or inventory losses rise"),
    ),
    OperatingArchetypeProfile(
        "platform_marketplace",
        "internet / marketplace platform",
        ("platform", "marketplace", "advertising", "payments", "互联网", "平台", "广告", "支付", "交易额", "gmv"),
        "active users/merchants x engagement x monetization or take rate",
        "revenue - traffic acquisition - incentives - fulfillment/payment loss - cloud/content cost",
        "operating profit + D&A/SBC - working capital - capex - strategic investment",
        ("MAU/DAU and engagement", "GMV or transactions", "take rate/ARPU", "retention and cohort contribution", "traffic acquisition and incentive intensity"),
        ("network effects", "multi-homing", "merchant/user switching", "distribution control", "regulation", "adjacent platform entry"),
        ("DCF", "SOTP", "EV/revenue or PE only with normalized margin"),
        ("engagement or retention falls", "monetization damages ecosystem health", "subsidies rise faster than contribution profit"),
    ),
    OperatingArchetypeProfile(
        "software_subscription",
        "software / subscription",
        ("software", "saas", "subscription", "cloud service", "软件", "订阅", "云服务", "续费", "席位"),
        "customers or seats x paid penetration x ARPU x retention",
        "subscription/license revenue - delivery/cloud/support cost - R&D - sales and marketing",
        "operating profit + non-cash charges - receivable/contract-asset build - capitalized development/capex",
        ("ARR and paid users/seats", "gross/net retention", "ARPU and attach rate", "CAC and payback", "gross margin and cloud cost"),
        ("switching cost", "workflow/data lock-in", "ecosystem", "implementation quality", "open-source/cloud substitutes", "customer budget"),
        ("DCF", "EV/ARR with retention/margin controls", "SOTP for services versus subscription"),
        ("renewal/churn worsens", "CAC payback extends", "AI or new modules fail to monetize"),
    ),
    OperatingArchetypeProfile(
        "project_order_delivery",
        "project / order / equipment delivery",
        ("project", "backlog", "order", "equipment", "acceptance", "工程", "项目", "订单", "合同负债", "验收", "装备"),
        "opening backlog + new orders - delivered/recognized orders = ending backlog",
        "recognized project revenue - BOM/labor/subcontract/warranty - R&D and selling overhead",
        "cash advances + collections - procurement/WIP - delivery/acceptance working capital - capex",
        ("new orders and backlog", "book-to-bill", "delivery/acceptance cadence", "project gross margin", "receivables/contract assets and collections"),
        ("technical qualification", "installed base/service", "price and delivery", "customer capex", "localization", "new entrants"),
        ("order-backed DCF", "EV/EBITDA", "SOTP by equipment/project category"),
        ("orders fail to convert", "acceptance or collection delays", "backlog margin deteriorates"),
    ),
    OperatingArchetypeProfile(
        "standard_manufacturing",
        "standardized manufacturing",
        ("manufacturing", "factory", "capacity", "utilization", "shipment", "制造", "工厂", "产能", "产量", "销量", "利用率"),
        "effective capacity x utilization x yield x saleable volume x realized ASP/mix",
        "volume x (realized ASP - material - conversion - freight - warranty) - period expense",
        "EBITDA - working-capital build - maintenance/growth capex - tax/interest",
        ("capacity/utilization/yield", "shipment and ASP/mix", "unit material/conversion cost", "inventory and receivables", "incremental ROIC"),
        ("cost curve", "quality/yield", "customer qualification", "scale", "capacity response", "substitution"),
        ("EV/EBITDA", "DCF/FCF", "PE/PB-ROE cross-check"),
        ("utilization or yield weakens", "price erosion outruns cost reduction", "expansion earns below cost of capital"),
    ),
    OperatingArchetypeProfile(
        "resource_commodity",
        "resource / commodity cycle",
        ("mining", "resource", "commodity", "reserve", "ore", "矿", "资源", "储量", "品位", "现货", "期货"),
        "equity output x realized product price plus by-product credits",
        "output x (realized price - cash cost/AISC) - sustaining overhead",
        "cash margin - sustaining/growth capex - tax/royalty/minority - working capital",
        ("reserves/grade/mine life", "equity output", "realized price/basis", "cash cost/AISC", "sustaining capex and leverage"),
        ("cost-curve position", "resource quality", "jurisdiction/license", "supply discipline", "substitution", "capital-cycle response"),
        ("NAV/SOTP", "normalized EV/EBITDA", "cycle-trough PB/PE"),
        ("cost curve moves above peers", "project ramp or reserve conversion fails", "balance sheet cannot survive trough"),
    ),
    OperatingArchetypeProfile(
        "technology_product",
        "technology product / semiconductor",
        ("semiconductor", "chip", "wafer", "design win", "electronics", "半导体", "芯片", "晶圆", "流片", "认证", "技术路线"),
        "qualified shipments x ASP by generation/customer/end market x product mix",
        "product gross profit - foundry/BOM/packaging - R&D - customer support and sales",
        "operating profit + D&A - inventory/receivables - tape-out/tool/capacity capex",
        ("design wins/qualification", "shipments and ASP/mix", "yield and supply cost", "customer/end-market concentration", "inventory and R&D conversion"),
        ("product performance", "ecosystem/IP", "qualification stickiness", "time-to-market", "route substitution", "customer self-design"),
        ("product-cycle DCF", "SOTP", "EV/EBITDA or PE with R&D/optionality separation"),
        ("qualification or product ramp slips", "ASP erosion outruns mix/yield", "inventory grows ahead of demand"),
    ),
    OperatingArchetypeProfile(
        "pharma_biotech",
        "pharma / biotech",
        ("pharma", "biotech", "drug", "clinical", "医药", "创新药", "临床", "管线", "适应症", "医保"),
        "commercial products: patients x penetration x net price; pipeline: probability-adjusted eligible population/value",
        "product gross profit - selling/medical affairs - R&D by program - milestone/royalty economics",
        "commercial cash contribution - R&D - milestone obligations - capex +/- working capital and financing",
        ("patient/volume and net price", "market share and competing labels", "clinical/regulatory milestones", "R&D spend by stage", "cash runway and dilution"),
        ("clinical differentiation", "label and reimbursement", "physician/patient switching", "competing pipeline timing", "manufacturing/IP", "BD alternatives"),
        ("risk-adjusted NPV", "SOTP", "DCF for commercial assets"),
        ("clinical/regulatory failure", "commercial uptake misses", "cash runway forces dilutive financing"),
    ),
    OperatingArchetypeProfile(
        "bank_spread_credit",
        "bank / spread and credit",
        ("bank", "loan", "deposit", "nim", "银行", "贷款", "存款", "净息差", "不良", "资本充足"),
        "earning assets x NIM + fee/other income",
        "net revenue - operating cost - credit cost/provisions - tax",
        "capital generation - RWA growth - dividend; cash-flow statement is not a manufacturing FCF proxy",
        ("earning assets and NIM", "deposit cost/mix", "NPL and provision coverage", "credit cost", "CET1/RWA and payout"),
        ("funding franchise", "customer/branch ecosystem", "loan pricing", "risk selection", "digital efficiency", "regulatory capital"),
        ("PB-ROE", "P/E", "dividend discount/residual income"),
        ("asset quality deteriorates", "capital constrains growth/payout", "funding cost prevents NIM stabilization"),
    ),
    OperatingArchetypeProfile(
        "insurance_value",
        "insurance / value and solvency",
        ("insurance", "nbv", "embedded value", "solvency", "保险", "新业务价值", "内含价值", "偿付能力", "综合成本率"),
        "life: APE x NBV margin; P&C: earned premium; plus investment income",
        "value of new business + in-force unwind + investment spread - claims/expenses",
        "capital generation - solvency capital consumption - dividend; separate life, P&C and investments",
        ("APE/NBV/NBV margin", "agent/bancassurance productivity", "EV/CSM", "investment yield/spread", "COR and solvency/payout"),
        ("distribution productivity", "product economics", "asset-liability management", "claims data", "capital strength", "peer product substitution"),
        ("P/EV", "SOTP", "dividend discount/residual income"),
        ("NBV quality weakens", "investment spread compresses", "COR or solvency deteriorates"),
    ),
    OperatingArchetypeProfile(
        "regulated_asset_reit",
        "regulated asset / utility / REIT",
        ("utility", "reit", "occupancy", "tariff", "power plant", "公用事业", "电价", "出租率", "租金", "特许经营"),
        "effective capacity/area x utilization/occupancy x regulated tariff/rent",
        "revenue - fuel/operating/maintenance/lease cost - depreciation - finance cost",
        "NOI/EBITDA - maintenance capex - interest/tax +/- working capital = distributable cash",
        ("capacity/area and utilization/occupancy", "tariff/rent and escalation", "maintenance capex", "leverage and refinancing", "distributable cash/payout"),
        ("asset location/quality", "license/concession", "regulatory return", "replacement cost", "tenant/customer concentration", "new supply"),
        ("DCF/DDM", "EV/EBITDA", "P/NAV or yield spread"),
        ("utilization/occupancy falls", "regulation blocks cost recovery", "maintenance/refinancing consumes distribution"),
    ),
)


def _normalized(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).lower()


def detect_operating_archetypes(
    symbol: str,
    text: str,
    *,
    segment_names: Iterable[str] = (),
    limit: int = 3,
) -> list[tuple[OperatingArchetypeProfile, int]]:
    """Return candidate profiles; candidates guide research and are not facts."""

    body = _normalized("\n".join([symbol, *segment_names, text]))
    scored: list[tuple[OperatingArchetypeProfile, int]] = []
    for profile in OPERATING_ARCHETYPES:
        score = sum(3 if len(keyword) >= 5 else 2 for keyword in profile.keywords if keyword.lower() in body)
        if score:
            scored.append((profile, score))
    scored.sort(key=lambda pair: (pair[1], pair[0].profile_id), reverse=True)
    return scored[: max(1, int(limit))]


def render_operating_archetype_context(
    symbol: str,
    text: str,
    *,
    segment_names: Iterable[str] = (),
) -> str:
    candidates = detect_operating_archetypes(symbol, text, segment_names=segment_names)
    if not candidates:
        return "\n".join(
            [
                "## General Operating-Model Router",
                "- No deterministic archetype candidate was strong enough. Keep each material business line qualitative until its customer, pricing, delivery, cost and cash cycle are identified.",
                "- Missing archetype evidence is partial research coverage, not a blocked report.",
            ]
        )
    lines = [
        "## General Operating-Model Router",
        "- These are deterministic candidates, not final classifications. Assign a primary and optional secondary profile to each material business unit; a diversified company may use multiple profiles.",
    ]
    for profile, score in candidates:
        lines.extend(
            [
                f"### Candidate: {profile.profile_id} ({profile.name}; score={score})",
                f"- Revenue equation: {profile.revenue_equation}",
                f"- Profit equation: {profile.profit_equation}",
                f"- Cash equation: {profile.cash_equation}",
                f"- Mandatory KPIs: {'; '.join(profile.mandatory_kpis)}",
                f"- Competition dimensions: {'; '.join(profile.competition_dimensions)}",
                f"- Valuation methods: {'; '.join(profile.valuation_methods)}",
                f"- Falsification gates: {'; '.join(profile.falsification_gates)}",
            ]
        )
    return "\n".join(lines)

