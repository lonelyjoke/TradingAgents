import pandas as pd

from tradingagents.dataflows import commodity_research
from tradingagents.dataflows.commodity_research import (
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


def test_financial_institution_commodity_context_is_not_applicable(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "招商银行", "industry": "银行"}),
    )

    mapping = _infer_products("600036.SH")

    assert mapping["products"] == []
    assert "Not applicable" in mapping["spread_note"]
