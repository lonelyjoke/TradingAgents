import pandas as pd

from tradingagents.dataflows import building_materials_research
from tradingagents.dataflows.building_materials_research import (
    get_building_materials_context,
)


def test_building_materials_context_skips_structured_battery_cell_company():
    rendered = get_building_materials_context("300750.SZ", "2026-06-27")

    assert "- Status: not_applicable" in rendered


def test_building_materials_context_triggers_for_curated_conch(monkeypatch):
    monkeypatch.setattr(building_materials_research, "_fetch_stock_basic", lambda symbol: None)
    monkeypatch.setattr(
        building_materials_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            pd.DataFrame(),
            [
                (
                    "annual",
                    "公司主营水泥、熟料和骨料业务，披露水泥熟料销量、单位成本、毛利率和区域需求。",
                )
            ],
        ),
    )
    monkeypatch.setattr(
        building_materials_research,
        "_fetch_income_statement_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331", "20251231"],
                "total_revenue": [170.0, 900.0],
                "n_income_attr_p": [13.0, 81.0],
            }
        ),
    )
    monkeypatch.setattr(
        building_materials_research,
        "_fetch_balance_sheet_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331", "20251231"],
                "accounts_receiv": [60.0, 55.0],
                "inventories": [75.0, 72.0],
                "contract_liab": [26.0, 29.0],
                "money_cap": [416.0, 500.0],
            }
        ),
    )
    monkeypatch.setattr(
        building_materials_research,
        "_fetch_cashflow_data",
        lambda *args, **kwargs: pd.DataFrame(
            {"end_date": ["20260331"], "n_cashflow_act": [3.3], "c_fr_sale_sg": [190.0]}
        ),
    )
    monkeypatch.setattr(
        building_materials_research,
        "_fetch_fina_indicator",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331"],
                "grossprofit_margin": [21.3],
                "roe": [1.0],
                "debt_to_assets": [20.0],
            }
        ),
    )

    rendered = get_building_materials_context("600585.SH", "2026-06-02")

    assert "Status: triggered" in rendered
    assert "curated A-share building-materials ticker list" in rendered
    assert "Detected subsectors: cement" in rendered
    assert "Low PB is a hypothesis" in rendered
    assert "Start with company filings" in rendered
    assert "industry stage as the second layer" in rendered
    assert "discipline layer" not in rendered
    assert "Operating Cycle Verdict" in rendered
    assert "600585.SH" in rendered


def test_building_materials_context_not_applicable_for_non_building_materials(monkeypatch):
    monkeypatch.setattr(
        building_materials_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "测试科技", "industry": "软件服务"}),
    )
    monkeypatch.setattr(
        building_materials_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (pd.DataFrame(), [("annual", "主营软件开发。")]),
    )

    rendered = get_building_materials_context("301396.SZ", "2026-06-02")

    assert "Status: not_applicable" in rendered


def test_demand_terms_alone_do_not_trigger_building_materials_context(monkeypatch):
    monkeypatch.setattr(
        building_materials_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "测试地产服务", "industry": "软件服务"}),
    )
    monkeypatch.setattr(
        building_materials_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            pd.DataFrame(),
            [("annual", "公司客户包含地产、基建、旧改和城中村项目，但主营软件开发。")],
        ),
    )

    rendered = get_building_materials_context("301396.SZ", "2026-06-02")

    assert "Status: not_applicable" in rendered


def test_building_materials_context_does_not_misroute_chemical_pipe_mentions(monkeypatch):
    monkeypatch.setattr(
        building_materials_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "万华化学", "industry": "化工原料"}),
    )
    monkeypatch.setattr(
        building_materials_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            pd.DataFrame(),
            [
                (
                    "annual",
                    "公司生产MDI、TDI与石化产品，部分材料用于保温板、涂料和管道应用，但主营业务并非建材生产销售。",
                )
            ],
        ),
    )

    rendered = get_building_materials_context("600309.SH", "2026-06-30")

    assert "Status: not_applicable" in rendered
