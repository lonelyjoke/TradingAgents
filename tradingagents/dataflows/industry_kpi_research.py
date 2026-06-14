"""Derived industry-specific KPI checklist context.

This module turns already-fetched report/industry contexts into an evidence
checklist. It does not fetch or invent data; missing rows remain research gaps.
"""

from __future__ import annotations

import re
from typing import Mapping

from .industry_identity import is_telecom_operator_text


def _compact_line(line: str, *, max_len: int = 260) -> str:
    line = re.sub(r"\s+", " ", (line or "").strip())
    if len(line) > max_len:
        return line[: max_len - 3] + "..."
    return line


def _matching_lines(text: str, patterns: tuple[str, ...], *, limit: int = 6) -> list[str]:
    rows: list[str] = []
    compiled = [re.compile(pattern, re.I) for pattern in patterns]
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("| ---"):
            continue
        if any(pattern.search(line) for pattern in compiled):
            rows.append(_compact_line(line).replace("|", "/"))
        if len(rows) >= limit:
            break
    return rows


def _detect_playbook(symbol: str, combined_text: str) -> tuple[str, list[tuple[str, str, str]]]:
    lower = f"{symbol}\n{combined_text}".lower()
    if is_telecom_operator_text(symbol, combined_text):
        return (
            "telecom operator / high-dividend SOE",
            [
                ("Mobile", "mobile subscribers, 5G penetration, mobile ARPU, DOU, churn, package mix", "service revenue and margin durability"),
                ("Broadband/Home", "broadband subscribers, household ARPU, gigabit penetration, smart-home attach", "cash-cow stability"),
                ("Enterprise/Cloud", "IDC, cloud revenue, cloud gross margin, AI/industry-digital revenue, contract liabilities", "second-curve growth and margin mix"),
                ("Capex", "5G/cloud/AI capex, depreciation, network utilization, capex-to-revenue", "FCF and ROIC"),
                ("Cash/Dividend", "OCF, FCF after capex, payout ratio, net cash/debt, dividend yield", "defensive yield and downside protection"),
                ("Peer Allocation", "China Mobile / China Unicom comparison, ARPU, ROE, FCF, dividend, cloud growth", "relative allocation"),
            ],
        )
    wind_hits = sum(
        token in combined_text
        for token in ("风电", "海上风电", "海风", "塔筒", "管桩", "导管架", "海工", "风电装备", "风机")
    ) + sum(token in lower for token in ("wind power", "offshore wind", "monopile", "jacket foundation", "tower"))
    battery_material_hits = sum(
        token in combined_text
        for token in ("正极材料", "磷酸铁锂", "三元材料", "前驱体", "锂电材料", "电池材料")
    ) + sum(token in lower for token in ("cathode", "precursor", "lfp"))
    battery_hits = sum(
        token in combined_text
        for token in ("动力电池", "储能电池", "锂离子电池", "电芯")
    ) + sum(token in lower for token in ("300750", "battery cell", "power battery"))
    if wind_hits >= 2 and battery_material_hits == 0 and battery_hits == 0:
        return (
            "wind power / offshore foundation equipment",
            [
                ("Demand", "offshore wind tenders, project approvals, grid-connection schedule, overseas capex cycle", "order intake and delivery volume"),
                ("Backlog", "new orders, order backlog, contract liabilities, order-to-revenue ratio", "revenue visibility"),
                ("Price", "tower/monopile/jacket ASP, project mix, export pricing, FX clauses", "revenue and gross margin"),
                ("Cost", "steel plate, welding/processing, logistics, port cost, FX, warranty", "project gross margin"),
                ("Capacity", "base capacity, dock/port resources, utilization, capex and depreciation", "operating leverage"),
                ("Cash", "prepayments, receivables, inventory, OCF/NI, capex, debt maturity", "cash conversion and balance-sheet risk"),
            ],
        )
    if any(
        token in combined_text
        for token in ("正极材料", "磷酸铁锂", "三元材料", "前驱体", "锂电材料", "电池材料")
    ) or any(token in lower for token in ("cathode", "precursor", "lfp")):
        return (
            "lithium battery materials / cathode chain",
            [
                ("Demand", "LFP / ternary cathode output, downstream battery installation, ESS demand, customer order cadence", "shipment volume"),
                ("Price", "cathode ASP, lithium carbonate pass-through, processing fee / spread, contract pricing clauses", "revenue and gross margin"),
                ("Cost", "lithium carbonate, iron phosphate / precursor, energy, depreciation, inventory-cost lag", "unit margin"),
                ("Capacity", "effective capacity, utilization, new-line ramp, maintenance shutdowns", "operating leverage"),
                ("Customers", "CATL/BYD/major customer mix, concentration, credit terms, contract liabilities", "visibility and bargaining power"),
                ("Cash", "receivables, notes, inventory, OCF/NI, credit impairment", "earnings quality"),
            ],
        )
    if (
        "300750" in lower
        or "动力电池" in combined_text
        or "储能电池" in combined_text
        or "锂离子电池" in combined_text
        or "battery" in lower
    ):
        return (
            "battery / energy-storage chain",
            [
                ("Demand", "NEV sales/penetration, power-battery installation GWh, storage tenders/shipments GWh", "volume and mix"),
                ("Share", "domestic/global battery-install share, key customer mix, overseas certification", "competitive position"),
                ("Price", "battery ASP, lithium/material pass-through, pricing clauses", "revenue and gross margin"),
                ("Cost", "lithium carbonate, cathode/anode/electrolyte, manufacturing yield, warranty", "unit margin"),
                ("Capacity", "effective capacity, utilization, new bases, capex and depreciation", "operating leverage"),
                ("Backlog", "contract liabilities, orders, storage pipeline, customer concentration", "visibility"),
            ],
        )
    if any(token in lower for token in ["002460", "赣锋", "锂", "lithium", "metals", "mining"]):
        return (
            "lithium / metals cycle",
            [
                ("Price", "lithium carbonate/hydroxide price, futures curve, realized ASP", "revenue and inventory gains/losses"),
                ("Spread", "ore/salt-lake/brine cost, processing spread, by-product credits", "cash margin"),
                ("Inventory", "industry and company inventory, downstream restocking/destocking", "cycle stage"),
                ("Output", "equity resource output, conversion capacity, ramp schedule", "volume"),
                ("Demand", "battery installation, ESS, cathode output, export/import", "end demand"),
                ("Cost Curve", "peer cost curve, project grade, AISC/cash cost, impairment risk", "moat and downside"),
            ],
        )
    if any(token in combined_text for token in ["白酒", "经销商", "批价", "动销"]):
        return (
            "baijiu / consumer channel",
            [
                ("Price", "wholesale price, retail price, promotion intensity", "brand power"),
                ("Channel", "channel inventory, distributor payment, contract liabilities", "cycle pressure"),
                ("Demand", "banquet/business demand, sell-through, regional traffic", "volume"),
                ("Mix", "high-end/sub-high-end mix, product upgrade/downgrade", "margin"),
                ("Cash", "receivables, advance receipts, cash conversion", "quality"),
            ],
        )
    if any(token in combined_text for token in ["水泥", "熟料", "防水", "玻璃", "建材"]):
        return (
            "building materials",
            [
                ("Demand", "property completion, infrastructure, regional construction starts", "volume"),
                ("Price", "cement/clinker/glass/waterproof ASP and regional spread", "revenue"),
                ("Capacity", "kiln utilization, capacity discipline, inventory days", "cycle stage"),
                ("Cost", "coal, soda ash, asphalt, energy and logistics", "gross margin"),
                ("Cash", "receivables, bills, credit impairment, operating cash flow", "balance-sheet quality"),
            ],
        )
    return (
        "generic company / sector",
        [
            ("Demand", "end-market volume, order/backlog, customer budget, channel sell-through", "revenue"),
            ("Price", "ASP, discount, mix, contract terms", "margin"),
            ("Cost", "raw material, labor, depreciation, logistics, warranty", "unit economics"),
            ("Capacity", "utilization, capex, bottleneck, operating leverage", "profit elasticity"),
            ("Competition", "market share, peer price behavior, substitution", "moat"),
            ("Cash", "working capital, receivables, inventory, free cash flow", "earnings quality"),
        ],
    )


def build_industry_kpi_context(
    symbol: str,
    curr_date: str,
    *,
    filing_intelligence_context: str = "",
    industry_cycle_context: str = "",
    company_business_model_context: str = "",
    commodity_context: str = "",
    peer_comparison_context: str = "",
    investor_interaction_context: str = "",
    policy_planning_context: str = "",
    web_fact_check_context: str = "",
) -> str:
    combined = "\n".join(
        [
            filing_intelligence_context,
            industry_cycle_context,
            company_business_model_context,
            commodity_context,
            peer_comparison_context,
            investor_interaction_context,
            policy_planning_context,
            web_fact_check_context,
        ]
    )
    playbook, kpis = _detect_playbook(symbol, combined)
    evidence = _matching_lines(
        combined,
        (
            r"revenue|profit|gross margin|ASP|price|latest_price|change_over_window",
            r"capacity|utilization|shipment|installation|GWh|market share|share",
            r"contract liabilit|backlog|order|inventory|cash flow|capex",
            r"锂|电池|储能|装机|份额|产能|利用率|合同负债|库存|价格|毛利|现金流",
            r"ARPU|subscriber|broadband|cloud|IDC|capex|dividend|payout|用户|宽带|天翼云|智算|资本开支|分红|派息",
        ),
        limit=10,
    )
    missing_rows = [
        f"- {name}: verify {metric}; explain impact on {driver}."
        for name, metric, driver in kpis
    ]
    return "\n".join(
        [
            f"# Industry KPI Checklist for {symbol} as of {curr_date}",
            "",
            f"- Playbook: {playbook}",
            "- Purpose: force the report to verify sector-native operating data before drawing cycle, moat, or valuation conclusions.",
            "",
            "## Required KPI Map",
            "| KPI layer | Required public evidence | Financial driver |",
            "| --- | --- | --- |",
            *[f"| {name} | {metric} | {driver} |" for name, metric, driver in kpis],
            "",
            "## Evidence Already Present",
            *([f"- {line}" for line in evidence] if evidence else ["- No compact KPI evidence was extracted from existing contexts."]),
            "",
            "## Missing / High-Priority Public Data",
            *missing_rows,
            "",
            "## Analyst Instructions",
            "- Do not let a generic sector label replace the KPI map. State which KPI layers are verified, partial, or missing.",
            "- If the report uses cycle language, connect it to at least demand, price/spread, inventory/backlog, and capacity/utilization evidence.",
            "- If a thesis-critical KPI is missing, cap conviction or move the item to the verification calendar instead of converting it into a hard trigger.",
        ]
    )


def get_industry_kpi_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, str] | None = None,
) -> str:
    supplied = dict(contexts or {})
    return build_industry_kpi_context(
        ticker,
        curr_date,
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        industry_cycle_context=supplied.get("industry_cycle_context", ""),
        company_business_model_context=supplied.get("company_business_model_context", ""),
        commodity_context=supplied.get("commodity_context", ""),
        peer_comparison_context=supplied.get("peer_comparison_context", ""),
        investor_interaction_context=supplied.get("investor_interaction_context", ""),
        policy_planning_context=supplied.get("policy_planning_context", ""),
        web_fact_check_context=supplied.get("web_fact_check_context", ""),
    )
