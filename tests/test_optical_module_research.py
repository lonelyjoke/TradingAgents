import pandas as pd

from tradingagents.dataflows import optical_module_research
from tradingagents.dataflows.data_coverage import classify_context_coverage
from tradingagents.dataflows.optical_module_research import get_optical_module_context


def test_optical_module_context_triggers_for_zhongji(monkeypatch):
    monkeypatch.setattr(
        optical_module_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "Zhongji Innolight", "industry": "optical communication"}),
    )
    monkeypatch.setattr(
        optical_module_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            pd.DataFrame(),
            [("annual", "The company sells high-speed optical module products for datacom and AI server demand.")],
        ),
    )
    monkeypatch.setattr(
        optical_module_research,
        "_fetch_income_statement_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331", "20251231"],
                "total_revenue": [720.0, 2400.0],
                "n_income_attr_p": [120.0, 390.0],
            }
        ),
    )
    monkeypatch.setattr(
        optical_module_research,
        "_fetch_balance_sheet_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331", "20251231"],
                "inventories": [180.0, 160.0],
                "accounts_receiv": [260.0, 220.0],
                "contract_liab": [12.0, 10.0],
                "money_cap": [500.0, 460.0],
                "total_liab": [700.0, 650.0],
                "total_assets": [2200.0, 2100.0],
            }
        ),
    )
    monkeypatch.setattr(
        optical_module_research,
        "_fetch_cashflow_data",
        lambda *args, **kwargs: pd.DataFrame(
            {"end_date": ["20260331"], "n_cashflow_act": [95.0], "c_fr_sale_sg": [680.0]}
        ),
    )
    monkeypatch.setattr(
        optical_module_research,
        "_fetch_fina_indicator",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331"],
                "grossprofit_margin": [34.0],
                "netprofit_margin": [18.0],
                "q_gr_yoy": [65.0],
            }
        ),
    )

    rendered = get_optical_module_context("300308.SZ", "2026-06-05")

    assert "Status: triggered" in rendered
    assert "curated A-share AI optical-module supply-chain ticker list" in rendered
    assert "high-speed optical module" in rendered
    assert "800G/1.6T" in rendered
    assert "inventories_to_revenue" in rendered
    assert "customer concentration" in rendered


def test_optical_module_context_not_applicable_for_unmapped_non_optical(monkeypatch):
    monkeypatch.setattr(
        optical_module_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "Generic Bank", "industry": "banking"}),
    )
    monkeypatch.setattr(
        optical_module_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (pd.DataFrame(), [("annual", "deposit loan wealth management")]),
    )

    rendered = get_optical_module_context("600000.SH", "2026-06-05")

    assert "Status: not_applicable" in rendered


def test_data_coverage_marks_optical_module_not_applicable():
    coverage = classify_context_coverage(
        "optical_module",
        "# AI optical-module context\n\n- Status: not_applicable\n- Reason: no curated optical-module mapping.",
    )

    assert coverage.status == "not_applicable"
