from pathlib import Path

import pandas as pd

from tradingagents.dataflows import insurance_research
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


def test_copper_miner_kpi_checklist_uses_nonferrous_mining_drivers():
    context = build_industry_kpi_context(
        "601168.SH",
        "2026-06-16",
        filing_intelligence_context="西部矿业主营铜、锌、铅等有色金属采选冶，矿山储量、品位、权益产量和冶炼加工费影响利润。",
        company_business_model_context="Business model: multi-metal mining, beneficiation, smelting, and trading platform.",
    )

    assert "nonferrous metals / copper-mining-smelting" in context
    assert "reserve/resource tonnage" in context
    assert "TC/RC" in context
    assert "Segment/SOTP" in context
    assert "new-project NAV split" in context
    assert "battery / energy-storage chain" not in context


def test_aluminum_kpi_checklist_uses_nonferrous_chain_even_with_battery_downstream_mentions():
    context = build_industry_kpi_context(
        "601600.SH",
        "2026-06-16",
        filing_intelligence_context=(
            "中国铝业主营氧化铝、电解铝和贸易，铝价、氧化铝、电力成本、"
            "产能利用率影响利润。动力电池只是铝需求下游之一。"
        ),
        commodity_context="# Commodity\n\n| Aluminum | main product |\n| Alumina | cost/spread driver |",
        metals_mining_context="# Metals-mining verification context\n\n- Status: triggered\n- Metals covered: Aluminum",
    )

    assert "nonferrous metals / aluminum chain" in context
    assert "alumina price" in context
    assert "power tariff" in context
    assert "LME-SHFE spread" in context
    assert "battery / energy-storage chain" not in context


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


def test_muyuan_kpi_checklist_uses_hog_cycle_even_with_battery_noise():
    context = build_industry_kpi_context(
        "002714.SZ",
        "2026-06-18",
        company_business_model_context="Legacy report had battery and energy-storage noise, but the company sells commodity hogs.",
        commodity_context="DCE LH2611.DCE close=12815; company complete cost is thesis-critical.",
        investor_interaction_context="Management discussed live hog ASP, output, complete cost, and breeding-sow supply.",
    )

    assert "hog breeding / live-hog cycle" in context
    assert "company monthly commodity-hog ASP" in context
    assert "breeding-sow supply" in context
    assert "hog-price sensitivity" in context
    assert "battery / energy-storage chain" not in context


def test_ping_an_kpi_checklist_uses_insurance_not_metals_or_hog():
    context = build_industry_kpi_context(
        "601318.SH",
        "2026-06-18",
        insurance_context="# Insurance verification context\n\n- Status: triggered\n- Company: Ping An",
        company_business_model_context="Integrated insurer with life, P&C, bank and asset-management subsidiaries.",
        filing_intelligence_context="NBV, embedded value, solvency, COR, investment yield and dividend capacity drive the thesis.",
    )

    assert "insurance / integrated financial services" in context
    assert "new business value" in context
    assert "P&C Underwriting" in context
    assert "nonferrous metals" not in context
    assert "hog breeding" not in context


def test_not_applicable_insurance_context_does_not_route_generic_stock_to_insurance():
    insurance_context = (
        "# Insurance verification context\n\n"
        "- Status: not_applicable\n"
        "- Analyst Instructions: Do not force NBV, EV, solvency, or COR analysis."
    )
    kpi = build_industry_kpi_context(
        "600519.SH",
        "2026-06-18",
        insurance_context=insurance_context,
        filing_intelligence_context="Revenue, gross margin, contract liabilities and cash conversion are relevant.",
    )
    forecast = build_forecast_model_context(
        "600519.SH",
        "2026-06-18",
        insurance_context=insurance_context,
        industry_kpi_context=kpi,
    )

    assert "insurance / integrated financial services" not in kpi
    assert "Life NBV" not in forecast
    assert "P&C underwriting profit" not in forecast


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


def test_muyuan_forecast_scaffold_requires_hog_price_sensitivity():
    context = build_forecast_model_context(
        "002714.SZ",
        "2026-06-18",
        earnings_model_context="Market cap and valuation need an implied hog price bridge.",
        company_business_model_context="Muyuan output, average sale weight, live hog ASP, and complete cost drive earnings.",
        industry_kpi_context="Playbook: hog breeding / live-hog cycle. Required KPI Map: hog ASP, complete cost, sales kilograms, breeding-sow inventory.",
    )
    lower = context.lower()

    assert "hog sales kilograms" in lower
    assert "realized hog asp - complete hog-breeding cost" in lower
    assert "hog-breeding sensitivity requirement" in lower
    assert "reverse-engineer the hog asp implied by current market cap" in lower
    assert "GWh shipments x ASP" not in context


def test_ping_an_forecast_scaffold_uses_insurance_bridge_not_hog():
    context = build_forecast_model_context(
        "601318.SH",
        "2026-06-18",
        insurance_context="# Insurance verification context\n\n- Status: triggered\n- Company: Ping An",
        earnings_model_context="Net profit, OPAT, dividend capacity and ROE need an insurance-native bridge.",
        industry_kpi_context="Playbook: insurance / integrated financial services. Required KPI Map: NBV, EV, COR, solvency.",
    )
    lower = context.lower()

    assert "life nbv" in lower
    assert "new premium x nbv margin" in lower
    assert "p&c underwriting profit" in lower
    assert "investment assets x" in lower
    assert "hog-breeding sensitivity requirement" not in lower
    assert "hog sales kilograms" not in lower


def test_insurance_context_handles_dataframe_report_list(monkeypatch):
    monkeypatch.setattr(
        insurance_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {"ts_code": symbol, "name": "Ping An", "industry": "Insurance"}
        ),
    )
    monkeypatch.setattr(
        insurance_research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"pe_ttm": 7.2, "pb": 0.9, "dv_ttm": 5.1}),
    )
    monkeypatch.setattr(
        insurance_research,
        "_fetch_fina_indicator",
        lambda symbol, curr_date: pd.DataFrame(
            [
                {
                    "end_date": "20260331",
                    "roe_annual": 11.0,
                    "roe": 2.6,
                    "netprofit_yoy": -7.4,
                    "debt_to_assets": 90.0,
                }
            ]
        ),
    )
    monkeypatch.setattr(
        insurance_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            pd.DataFrame([{"title": "Ping An 2025 annual report"}]),
            [("Ping An 2025 annual report", "NBV embedded value solvency COR investment yield")],
        ),
    )
    monkeypatch.setattr(
        insurance_research,
        "_fetch_stock_basic_universe",
        lambda: pd.DataFrame(
            [
                {"ts_code": "601318.SH", "name": "Ping An", "industry": "Insurance"},
                {"ts_code": "601601.SH", "name": "CPIC", "industry": "Insurance"},
            ]
        ),
    )

    context = insurance_research.get_insurance_context("601318.SH", "2026-06-18")

    assert "- Status: triggered" in context
    assert "- Reports considered: Ping An 2025 annual report" in context
    assert "Insurance-Native KPI Screen" in context
    assert "P/EV, NBV multiple, PB/ROE, dividend yield, and SOTP" in context
    assert "Q1 net profit, non-recurring profit, or operating cash flow deterioration is a warning signal" in context
    assert "relative Underweight/watch" in context


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


def test_forecast_model_scaffold_uses_metals_mining_bridge():
    context = build_forecast_model_context(
        "601168.SH",
        "2026-06-16",
        company_business_model_context="公司主营铜、锌、铅等有色金属采选冶，盈利取决于权益产量、储量品位、冶炼加工费和现金成本。",
        industry_kpi_context="Playbook: nonferrous metals / mining. Required KPI Map: reserve/resource tonnage, AISC, TC/RC, NAV/SOTP.",
    )

    assert "Mining revenue" in context
    assert "equity copper/by-product output x realized selling price" in context
    assert "Smelting / refining spread" in context
    assert "NAV / SOTP value" in context
    assert "Cathode / material revenue" not in context


def test_forecast_model_scaffold_uses_aluminum_spread_bridge():
    context = build_forecast_model_context(
        "601600.SH",
        "2026-06-16",
        company_business_model_context="中国铝业是氧化铝和电解铝一体化平台，动力电池只是下游需求之一。",
        industry_kpi_context="Playbook: nonferrous metals / aluminum chain. Required KPI Map: alumina price, power tariff, LME-SHFE spread.",
        metals_mining_context="# Metals-mining verification context\n\n- Status: triggered\n- Metals covered: Aluminum",
    )

    assert "Primary aluminum revenue" in context
    assert "primary aluminum output x realized aluminum price" in context
    assert "Alumina / upstream spread" in context
    assert "Smelting margin" in context
    assert "power tariff/self-generation" in context
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


def test_quality_audit_catches_report_specific_number_and_attribution_errors():
    context = build_quality_audit_context(
        "601318.SH",
        "2026-06-18",
        industry_cycle_context="# Industry Cycle Scan\n\n- Cycle verdict: bottom-testing",
        company_business_model_context="# Company Business Model Primer\n\nintegrated insurer",
        industry_kpi_context="# Industry KPI Checklist\n\ninsurance KPI ready",
        forecast_model_context="# Forward Forecast Model Scaffold\n\ninsurance forecast ready",
        peer_comparison_context="# Same-Industry Peer Comparison\n\ninsurance peer screen ready",
        price_earnings_decomposition_context="# Price-EPS-PE Decomposition\n\nready",
        earnings_model_context="# Earnings Model\n\nready",
        filing_intelligence_context="# Financial-Report Intelligence\n\nready",
    )

    assert "Do not confuse dividend yield with DPS" in context
    assert "percentage as DPS" in context
    assert "yuan/ten-thousand-yuan/100-million-yuan conversion error" in context
    assert "PE/PB/ROE/dividend yield/one-quarter profit growth" in context
    assert "not enough to prove a peer is a superior substitute" in context
    assert "do not infer institutional rotation" in context
    assert "trading volume alone" in context


def test_quality_audit_flags_metals_template_mismatch_and_missing_aluminum_spread():
    context = build_quality_audit_context(
        "601600.SH",
        "2026-06-16",
        industry_cycle_context="# Industry Cycle Scan\n\n- Cycle verdict: bottom-testing",
        company_business_model_context="# Company Business Model Primer\n\nintegrated aluminum and alumina producer",
        industry_kpi_context="# Industry KPI Checklist\n\n- Playbook: battery / energy-storage chain\ncathode ASP",
        forecast_model_context="# Forward Forecast Model Scaffold\n\n| Cathode / material revenue | shipment volume x cathode ASP |",
        peer_comparison_context="# Peer\n\nready",
        price_earnings_decomposition_context="# PE/PB\n\nready",
        earnings_model_context="# Earnings\n\nready",
        filing_intelligence_context="# Filing\n\nready",
        metals_mining_context="# Metals-mining verification context\n\n- Status: triggered\n- Metals covered: Aluminum",
        commodity_context=(
            "# Commodity\n\n"
            "| product | data_type | latest_price | evidence_status |\n"
            "| Aluminum | Tushare futures proxy | 23830 | Verified by Tushare futures daily data. |\n"
            "| Power cost | unavailable key driver | N/A | Missing; neutral for direction, confidence cap only. |"
        ),
    )

    assert "Metals/mining KPI routing | partial" in context
    assert "Metals/mining forecast bridge | partial" in context
    assert "Aluminum spread driver coverage | partial" in context
    assert "neutral for direction" in context
    assert "Underweight/Sell needs independent verified evidence" in context
    assert "do not permit strong Buy/Sell language" in context


def test_global_instructions_force_hog_breeding_valuation_bridge():
    agent_utils_source = Path("tradingagents/agents/utils/agent_utils.py").read_text(encoding="utf-8")

    assert "For hog breeders" in agent_utils_source
    assert "sales kilograms = hog output x" in agent_utils_source
    assert "average sale weight" in agent_utils_source
    assert "hog-price sensitivity table" in agent_utils_source
    assert "reverse-engineer the hog-price center" in agent_utils_source
    assert "current" in agent_utils_source
    assert "market cap" in agent_utils_source


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
