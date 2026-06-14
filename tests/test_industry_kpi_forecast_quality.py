from tradingagents.dataflows.data_coverage import build_data_coverage_context
from tradingagents.dataflows.forecast_model_research import build_forecast_model_context
from tradingagents.dataflows.industry_kpi_research import build_industry_kpi_context
from tradingagents.dataflows.prompt_compaction import compact_state_fields
from tradingagents.dataflows.quality_audit_research import build_quality_audit_context


def test_battery_industry_kpi_checklist_uses_sector_native_drivers():
    context = build_industry_kpi_context(
        "300750.SZ",
        "2026-06-11",
        filing_intelligence_context="公司披露动力电池、储能电池业务，产能和合同负债为核心跟踪项。",
        company_business_model_context="Segment Economics Pack: power battery revenue and storage battery gross margin.",
    )

    assert "battery / energy-storage chain" in context
    assert "NEV sales/penetration" in context
    assert "GWh" in context
    assert "contract liabilities" in context
    assert "verified, partial, or missing" in context


def test_lithium_industry_kpi_checklist_uses_metals_cycle_drivers():
    context = build_industry_kpi_context(
        "002460.SZ",
        "2026-06-11",
        filing_intelligence_context="赣锋锂业锂盐、锂矿和电池业务，锂价、库存、产能利用率影响利润。",
    )

    assert "lithium / metals cycle" in context
    assert "lithium carbonate/hydroxide price" in context
    assert "Cost Curve" in context
    assert "inventory" in context.lower()


def test_battery_material_kpi_checklist_uses_spread_drivers():
    context = build_industry_kpi_context(
        "301999.SZ",
        "2026-06-12",
        filing_intelligence_context="公司主营磷酸铁锂正极材料，碳酸锂成本、正极材料ASP、产能利用率和客户结构影响盈利。",
    )

    assert "lithium battery materials / cathode chain" in context
    assert "cathode ASP" in context
    assert "processing fee / spread" in context
    assert "customer mix" in context


def test_wind_equipment_kpi_checklist_preempts_broad_electrical_battery_route():
    context = build_industry_kpi_context(
        "301999.SZ",
        "2026-06-12",
        filing_intelligence_context="公司主营海上风电装备、塔筒、管桩和导管架，出口海工项目订单和合同负债影响收入。",
        company_business_model_context="Vendor industry: 电气设备。核心商业模式为项目订单交付回款型。",
    )

    assert "wind power / offshore foundation equipment" in context
    assert "offshore wind tenders" in context
    assert "contract liabilities" in context
    assert "lithium carbonate" not in context


def test_telecom_operator_kpi_checklist_uses_operator_drivers():
    context = build_industry_kpi_context(
        "601728.SH",
        "2026-06-12",
        filing_intelligence_context="中国电信为电信运营商，披露移动用户、宽带用户、天翼云、ARPU、资本开支和分红。",
        company_business_model_context="Vendor industry: 电信运营。传统通信现金牛与云AI第二曲线。",
    )

    assert "telecom operator / high-dividend SOE" in context
    assert "mobile subscribers" in context
    assert "mobile ARPU" in context
    assert "dividend yield" in context
    assert "lithium carbonate" not in context


def test_forecast_model_scaffold_requires_three_year_driver_bridge():
    context = build_forecast_model_context(
        "300750.SZ",
        "2026-06-11",
        earnings_model_context="Revenue grew; gross margin improved; net profit and EPS are thesis-critical.",
        company_business_model_context="动力电池和储能电池是主要收入和利润池。",
        industry_kpi_context="Required KPI Map: GWh shipments, ASP, utilization, contract liabilities.",
    )

    assert "Forward Forecast Model Scaffold" in context
    assert "GWh shipments x ASP" in context
    assert "2026E" in context
    assert "2027E" in context
    assert "2028E" in context
    assert "net profit/EPS" in context


def test_forecast_model_scaffold_uses_battery_material_bridge():
    context = build_forecast_model_context(
        "301999.SZ",
        "2026-06-12",
        company_business_model_context="公司主营磷酸铁锂正极材料，盈利取决于碳酸锂价格传导、加工费价差和产能利用率。",
        industry_kpi_context="Required KPI Map: cathode ASP, lithium carbonate, processing fee, capacity utilization.",
    )

    assert "Cathode / material revenue" in context
    assert "shipment volume x cathode ASP" in context
    assert "Manufacturing spread" in context


def test_forecast_model_scaffold_uses_wind_equipment_order_bridge():
    context = build_forecast_model_context(
        "301999.SZ",
        "2026-06-12",
        company_business_model_context="公司主营海上风电管桩、导管架和塔筒，盈利取决于海外订单、交付节奏、钢材成本、港口物流和汇率。",
        industry_kpi_context="Playbook: wind power / offshore foundation equipment. Required KPI Map: offshore wind tenders, contract liabilities, steel plate cost, utilization.",
    )

    assert "Wind-equipment revenue" in context
    assert "opening backlog + new orders - delivered orders" in context
    assert "steel plate cost" in context
    assert "Cathode / material revenue" not in context


def test_forecast_model_scaffold_uses_telecom_operator_bridge():
    context = build_forecast_model_context(
        "601728.SH",
        "2026-06-12",
        company_business_model_context="中国电信是电信运营商，核心变量包括移动用户、移动ARPU、宽带用户、天翼云、资本开支、经营现金流和分红。",
        industry_kpi_context="Playbook: telecom operator / high-dividend SOE. Required KPI Map: mobile subscribers, ARPU, cloud, capex, dividend.",
    )

    assert "Mobile service revenue" in context
    assert "mobile subscribers x mobile ARPU" in context
    assert "Enterprise / cloud / AI revenue" in context
    assert "dividend capacity" in context
    assert "Cathode / material revenue" not in context


def test_quality_audit_requires_formula_period_and_evidence_status():
    context = build_quality_audit_context(
        "300750.SZ",
        "2026-06-11",
        industry_cycle_context="# Industry Cycle Scan\n\n- Cycle verdict: bottom-right validation stage",
        company_business_model_context="# Company Business Model Primer\n\n## Segment Economics / Profit Pools\n动力电池",
        industry_kpi_context="# Industry KPI Checklist\n\n## Required KPI Map\n| Demand | evidence | driver |",
        forecast_model_context="# Forward Forecast Model Scaffold\n\n| item | 2026E | 2027E | 2028E |",
        peer_comparison_context="# Same-Industry Peer Comparison\n\n| peer | valuation |",
        price_earnings_decomposition_context="# Price-EPS-PE Decomposition\n\nready",
        earnings_model_context="# Earnings Model\n\nready",
        filing_intelligence_context="# Financial-Report Intelligence\n\nready",
    )

    assert "Sell-Side Depth And Key-Number Audit" in context
    assert "formula" in context
    assert "source period" in context
    assert "evidence status" in context
    assert "Weak or incomplete modules" in context


def test_new_contexts_are_compacted_and_covered():
    state = {
        "industry_kpi_context": "# Industry KPI Checklist\n\n## Required KPI Map\n" + "GWh ASP utilization\n" * 80,
        "forecast_model_context": "# Forward Forecast Model Scaffold\n\n## Mandatory Three-Year Table\n2026E 2027E 2028E\n",
        "quality_audit_context": "# Sell-Side Depth And Key-Number Audit\n\n## Key Number Audit Rules\nformula source period\n",
    }
    compacted = compact_state_fields(state, profile="portfolio")
    assert "industry_kpi_context" in compacted
    assert "forecast_model_context" in compacted
    assert "quality_audit_context" in compacted
    assert "Required KPI Map" in compacted["industry_kpi_context"]

    coverage = build_data_coverage_context(
        {
            "industry_kpi_checklist": state["industry_kpi_context"],
            "forecast_model_scaffold": state["forecast_model_context"],
            "sell_side_quality_audit": state["quality_audit_context"],
        }
    )
    assert "| industry_kpi_checklist | ready |" in coverage
    assert "| forecast_model_scaffold |" in coverage
    assert "| sell_side_quality_audit |" in coverage
