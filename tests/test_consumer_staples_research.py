import pandas as pd

from tradingagents.dataflows import consumer_staples_research
from tradingagents.dataflows.consumer_staples_research import get_consumer_staples_context
from tradingagents.dataflows.data_coverage import classify_context_coverage


def test_consumer_staples_context_triggers_for_anjoy(monkeypatch):
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "安井食品", "industry": "食品"}),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            pd.DataFrame(),
            [("annual", "公司主营速冻鱼糜制品、速冻肉制品、速冻米面制品和预制菜肴。")],
        ),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_income_statement_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331", "20251231"],
                "total_revenue": [380.0, 1360.0],
                "n_income_attr_p": [5.2, 13.6],
            }
        ),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_balance_sheet_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331", "20251231"],
                "inventories": [62.0, 83.0],
                "accounts_receiv": [18.0, 21.0],
                "contract_liab": [14.0, 12.0],
                "money_cap": [50.0, 48.0],
                "total_liab": [90.0, 88.0],
                "total_assets": [450.0, 440.0],
            }
        ),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_cashflow_data",
        lambda *args, **kwargs: pd.DataFrame(
            {"end_date": ["20260331"], "n_cashflow_act": [9.6], "c_fr_sale_sg": [395.0]}
        ),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_fina_indicator",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331"],
                "grossprofit_margin": [25.0],
                "netprofit_margin": [9.5],
                "q_gr_yoy": [30.8],
            }
        ),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_macro_table",
        lambda curr_date: (
            pd.DataFrame({"macro_source": ["CPI"], "month": ["202605"], "nt_yoy": [0.2]}),
            [],
        ),
    )

    rendered = get_consumer_staples_context("603345.SH", "2026-06-05")

    assert "Status: triggered" in rendered
    assert "curated A-share consumer-staples ticker list" in rendered
    assert "Detected subsectors: frozen_prepared_food" in rendered
    assert "restaurant chain penetration" in rendered
    assert "inventory/revenue" in rendered
    assert "Spring Festival restocking" in rendered


def test_consumer_staples_context_not_applicable_for_non_consumer(monkeypatch):
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "测试科技", "industry": "软件服务"}),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (pd.DataFrame(), [("annual", "主营软件开发。")]),
    )

    rendered = get_consumer_staples_context("301396.SZ", "2026-06-05")

    assert "Status: not_applicable" in rendered


def test_consumer_staples_context_marks_missing_cashflow_gap(monkeypatch):
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "安井食品", "industry": "食品"}),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (pd.DataFrame(), []),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_income_statement_data",
        lambda *args, **kwargs: pd.DataFrame({"end_date": ["20260331"], "total_revenue": [380.0]}),
    )
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_balance_sheet_data",
        lambda *args, **kwargs: pd.DataFrame({"end_date": ["20260331"], "inventories": [62.0]}),
    )
    monkeypatch.setattr(consumer_staples_research, "_fetch_cashflow_data", lambda *args, **kwargs: pd.DataFrame())
    monkeypatch.setattr(
        consumer_staples_research,
        "_fetch_fina_indicator",
        lambda *args, **kwargs: pd.DataFrame({"end_date": ["20260331"], "grossprofit_margin": [25.0]}),
    )
    monkeypatch.setattr(consumer_staples_research, "_macro_table", lambda curr_date: (pd.DataFrame(), []))

    rendered = get_consumer_staples_context("603345.SH", "2026-06-05")

    assert "## Data Gaps" in rendered
    assert "cash flow: no rows returned" in rendered
    assert "do not make unsupported claims" in rendered


def test_data_coverage_marks_unmapped_shipping_not_applicable():
    coverage = classify_context_coverage(
        "shipping_cycle",
        "# Shipping cycle context\n\n- Note: No shipping mapping found. Add the ticker.",
    )

    assert coverage.status == "not_applicable"
