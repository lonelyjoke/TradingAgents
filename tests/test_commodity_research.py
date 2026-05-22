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

    assert {"Live hog", "Piglet", "Feed", "Hog-grain ratio"} <= product_names


def test_financial_institution_commodity_context_is_not_applicable(monkeypatch):
    monkeypatch.setattr(
        commodity_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "招商银行", "industry": "银行"}),
    )

    mapping = _infer_products("600036.SH")

    assert mapping["products"] == []
    assert "Not applicable" in mapping["spread_note"]
