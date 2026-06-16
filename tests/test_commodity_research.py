import pandas as pd

from tradingagents.dataflows import commodity_research
from tradingagents.dataflows.commodity_research import (
    METAL_FUTURES_SOURCE_REGISTRY,
    _infer_products,
    _moa_monthly_archive_urls,
)


def test_moa_monthly_archive_urls_roll_back_across_year_boundary():
    urls = _moa_monthly_archive_urls("2026-01-15", months_back=2)

    assert urls == [
        "https://www.moa.gov.cn/ztzl/szcpxx/jdsj/2026/202601/",
        "https://www.moa.gov.cn/ztzl/szcpxx/jdsj/2025/202512/",
    ]


def test_muyuan_commodity_mapping_includes_hog_cycle_signals():
    mapping = _infer_products("002714.SZ")
    product_names = {product["name"] for product in mapping["products"]}

    assert {
        "Breeding sow inventory",
        "Live hog",
        "Live hog futures",
        "Piglet",
        "Feed",
        "Hog-grain ratio",
    } <= product_names


def test_livestock_context_declares_source_priority(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_livestock_sales_announcements",
        lambda symbol, curr_date, look_back_days: {
            "product": "Company monthly hog sales brief",
            "role": "ticker-specific realized volume/price evidence",
            "data_type": "company announcement",
            "latest_contract_or_source": "mock",
            "latest_price": "Not parsed",
            "latest_date": "20260501",
            "change_over_window": "Not computed",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Fetched stable company announcement titles.",
            "evidence": "mock sales brief",
        },
    )
    monkeypatch.setattr(
        commodity_research,
        "_fetch_moa_livestock_market",
        lambda product, curr_date: {
            "product": product["name"],
            "role": product.get("role", ""),
            "data_type": "official livestock market evidence",
            "latest_contract_or_source": "mock",
            "latest_price": "See official source",
            "latest_date": "See official source",
            "change_over_window": "Not computed",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Fetched official MOA livestock archive page.",
            "evidence": "mock official evidence",
        },
    )
    monkeypatch.setattr(
        commodity_research,
        "_fetch_futures_product",
        lambda product, curr_date, look_back_days: {
            "product": product["name"],
            "role": product.get("role", ""),
            "data_type": "Tushare futures proxy",
            "latest_contract_or_source": "LH_mock.DCE",
            "latest_price": "10000",
            "latest_date": "20260528",
            "change_over_window": "N/A",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Verified by Tushare futures daily data.",
            "evidence": "mock futures evidence",
        },
    )

    context = commodity_research.get_commodity_context("002714.SZ", "2026-05-28")

    assert "## Source Priority" in context
    assert "stable hard evidence" in context
    assert "DCE live-hog futures" in context
    assert "current-month breeding-sow inventory" in context


def test_resource_commodity_context_does_not_use_livestock_template(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_futures_product",
        lambda product, curr_date, look_back_days: {
            "product": product["name"],
            "role": product.get("role", ""),
            "data_type": "Tushare futures proxy",
            "latest_contract_or_source": f"{product['prefix']}.SHF",
            "latest_price": "100",
            "latest_date": "20260601",
            "change_over_window": "N/A",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Verified by Tushare futures daily data.",
            "evidence": "mock resource futures evidence",
        },
    )

    context = commodity_research.get_commodity_context("601899.SH", "2026-06-01")

    assert "exchange market proxy" in context
    assert "Copper" in context
    assert "Gold" in context
    assert "DCE live-hog futures" not in context
    assert "breeding-sow inventory" not in context
    assert "## Metal Price Source Audit" in context
    assert "COMEX HG futures" in context
    assert "COMEX GC futures" in context


def test_metal_price_registry_covers_core_domestic_and_overseas_links():
    expected = {
        "Gold": ("SHFE", "AU", "COMEX GC futures"),
        "Silver": ("SHFE", "AG", "COMEX SI futures"),
        "Copper": ("SHFE", "CU", "COMEX HG futures"),
        "Aluminum": ("SHFE", "AL", "LME aluminum"),
        "Alumina": ("SHFE", "AO", "domestic alumina spot"),
        "Zinc": ("SHFE", "ZN", "LME zinc"),
        "Lead": ("SHFE", "PB", "LME lead"),
        "Nickel": ("SHFE", "NI", "LME nickel"),
        "Tin": ("SHFE", "SN", "LME tin"),
        "Lithium carbonate": ("GFEX", "LC", "Fastmarkets"),
        "Industrial silicon": ("GFEX", "SI", "SMM"),
    }

    for metal, (exchange, prefix, overseas) in expected.items():
        source = METAL_FUTURES_SOURCE_REGISTRY[metal]
        assert source["domestic_exchange"] == exchange
        assert source["tushare_prefix"] == prefix
        assert overseas in source["overseas_cross_checks"]


def test_gold_company_mapping_uses_shfe_gold_proxy():
    mapping = _infer_products("600547.SH")
    product = mapping["products"][0]

    assert product["name"] == "Gold"
    assert product["prefix"] == "AU"
    assert product["exchange"] == "SHFE"


def test_chalco_mapping_fetches_alumina_and_marks_unavailable_costs_neutral(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_futures_product",
        lambda product, curr_date, look_back_days: {
            "product": product["name"],
            "role": product.get("role", ""),
            "data_type": "Tushare futures proxy",
            "latest_contract_or_source": f"{product['prefix']}.SHF",
            "latest_price": "100",
            "latest_date": "20260616",
            "change_over_window": "N/A",
            "inventory_or_receipt": "N/A",
            "evidence_status": "Verified by Tushare futures daily data.",
            "evidence": "mock futures evidence",
        },
    )

    mapping = _infer_products("601600.SH")
    context = commodity_research.get_commodity_context("601600.SH", "2026-06-16")
    product_names = {product["name"] for product in mapping["products"]}

    assert {"Aluminum", "Alumina", "Power cost", "Carbon anode cost"} <= product_names
    assert "Alumina" in context
    assert "AO.SHF" in context
    assert "Power cost" in context
    assert "Carbon anode cost" in context
    assert "Missing; neutral for direction, confidence cap only." in context
    assert "cannot prove margin deterioration" in context


def test_hunan_yuneng_uses_lithium_carbonate_cost_proxy():
    mapping = _infer_products("301358.SZ")
    product = mapping["products"][0]

    assert mapping["name"] == "Hunan Yuneng"
    assert product["name"] == "Lithium carbonate"
    assert product["role"] == "LFP cathode raw-material cost proxy"
    assert "not the realized cathode selling price" in mapping["spread_note"]


def test_unmapped_cathode_company_infers_lithium_cost_proxy_from_filings(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"ts_code": symbol, "name": "测试材料", "industry": "电气设备"}),
    )

    def fake_load_reports(symbol, curr_date, look_back_days):
        return [], [("年报", "公司主营磷酸铁锂正极材料，碳酸锂成本和正极材料售价影响毛利率。")]

    monkeypatch.setattr("tradingagents.dataflows.filing_research._load_financial_report_texts", fake_load_reports)

    mapping = _infer_products("301999.SZ", "2026-06-12")
    product = mapping["products"][0]

    assert product["name"] == "Lithium carbonate"
    assert product["role"] == "lithium-battery-material raw-material cost proxy"
    assert "stock name/industry and recent filing text" in mapping["spread_note"]


def test_unmapped_wind_equipment_uses_steel_proxy_not_incidental_precious_metal(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"ts_code": symbol, "name": "测试重工", "industry": "电气设备"}),
    )

    def fake_load_reports(symbol, curr_date, look_back_days):
        return [], [("年报", "公司主营海上风电装备、塔筒、管桩和导管架，钢材成本、港口物流和汇率影响项目毛利。")]

    monkeypatch.setattr("tradingagents.dataflows.filing_research._load_financial_report_texts", fake_load_reports)

    mapping = _infer_products("301997.SZ", "2026-06-12")
    product_names = {product["name"] for product in mapping["products"]}

    assert "Rebar" in product_names
    assert "Silver" not in product_names
    assert "Lithium carbonate" not in product_names


def test_telecom_operator_commodity_context_is_not_applicable(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"ts_code": symbol, "name": "中国电信", "industry": "电信运营"}),
    )

    mapping = _infer_products("601728.SH", "2026-06-12")

    assert mapping["products"] == []
    assert "Not applicable: telecom operators" in mapping["spread_note"]


def test_xingye_silver_tin_mapping_covers_core_metals():
    mapping = _infer_products("000426.SZ")
    product_names = {product["name"] for product in mapping["products"]}

    assert {"Silver", "Tin", "Lead", "Zinc"} <= product_names
    assert "silver, tin, lead, and zinc futures" in mapping["spread_note"]


def test_live_hog_futures_prefers_near_month_with_main_reference(monkeypatch):
    board = pd.DataFrame(
        [
            {"ts_code": "LH2607.DCE", "trade_date": "20260528", "close": 11900, "oi": 1000, "vol": 500},
            {"ts_code": "LH2609.DCE", "trade_date": "20260528", "close": 12130, "oi": 5000, "vol": 2000},
        ]
    )

    monkeypatch.setattr(commodity_research, "_latest_futures_trade_date", lambda curr_date, exchange: board)
    monkeypatch.setattr(
        commodity_research,
        "_query_futures_history",
        lambda ts_code, exchange, start, end: pd.DataFrame(
            [
                {"ts_code": ts_code, "trade_date": "20260501", "close": 11800, "vol": 1, "oi": 1},
                {"ts_code": ts_code, "trade_date": "20260528", "close": 11900, "vol": 1, "oi": 1},
            ]
        ),
    )
    monkeypatch.setattr(commodity_research, "_fetch_futures_receipt", lambda ts_code, exchange, trade_date: "N/A")

    result = commodity_research._fetch_futures_product(
        {
            "name": "Live hog futures",
            "type": "futures",
            "role": "timely market-implied price signal",
            "prefix": "LH",
            "exchange": "DCE",
            "selection": "near_month_with_main_reference",
        },
        "2026-05-28",
        90,
    )

    assert result["latest_contract_or_source"] == "LH2607.DCE"
    assert result["latest_price"] == "11900"
    assert "main_contract=LH2609.DCE" in result["evidence"]


def test_single_letter_futures_prefix_matches_exact_root(monkeypatch):
    board = pd.DataFrame(
        [
            {"ts_code": "CU2607.SHF", "trade_date": "20260605", "close": 81000, "oi": 9000, "vol": 5000},
            {"ts_code": "C2607.DCE", "trade_date": "20260605", "close": 2450, "oi": 1000, "vol": 600},
            {"ts_code": "C2609.DCE", "trade_date": "20260605", "close": 2480, "oi": 5000, "vol": 2000},
            {"ts_code": "PP2607.DCE", "trade_date": "20260605", "close": 7600, "oi": 7000, "vol": 3000},
            {"ts_code": "P2607.DCE", "trade_date": "20260605", "close": 8200, "oi": 800, "vol": 400},
        ]
    )
    queried = []

    monkeypatch.setattr(commodity_research, "_latest_futures_trade_date", lambda curr_date, exchange: board)

    def fake_history(ts_code, exchange, start, end):
        queried.append(ts_code)
        return pd.DataFrame(
            [
                {"ts_code": ts_code, "trade_date": "20260501", "close": 2400, "vol": 1, "oi": 1},
                {"ts_code": ts_code, "trade_date": "20260605", "close": 2450, "vol": 1, "oi": 1},
            ]
        )

    monkeypatch.setattr(commodity_research, "_query_futures_history", fake_history)
    monkeypatch.setattr(commodity_research, "_fetch_futures_receipt", lambda ts_code, exchange, trade_date: "N/A")

    corn = commodity_research._fetch_futures_product(
        {
            "name": "Corn futures",
            "type": "futures",
            "role": "cost proxy",
            "prefix": "C",
            "exchange": "DCE",
            "selection": "near_month_with_main_reference",
        },
        "2026-06-05",
        90,
    )
    palm = commodity_research._fetch_futures_product(
        {
            "name": "Palm oil futures",
            "type": "futures",
            "role": "cost proxy",
            "prefix": "P",
            "exchange": "DCE",
            "selection": "near_month_with_main_reference",
        },
        "2026-06-05",
        90,
    )

    assert corn["latest_contract_or_source"] == "C2607.DCE"
    assert palm["latest_contract_or_source"] == "P2607.DCE"
    assert queried == ["C2607.DCE", "P2607.DCE"]
    assert "CU2607.SHF" not in corn["evidence"]
    assert "PP2607.DCE" not in palm["evidence"]


def test_financial_institution_commodity_context_is_not_applicable(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "招商银行", "industry": "银行"}),
    )

    mapping = _infer_products("600036.SH")

    assert mapping["products"] == []
    assert "Not applicable" in mapping["spread_note"]
