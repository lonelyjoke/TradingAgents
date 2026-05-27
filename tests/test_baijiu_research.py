import pandas as pd

from tradingagents.dataflows import baijiu_research
from tradingagents.dataflows.baijiu_research import get_baijiu_context


def test_baijiu_context_triggers_for_curated_maotai_without_stock_basic(monkeypatch):
    monkeypatch.setattr(baijiu_research, "_fetch_stock_basic", lambda symbol: None)
    monkeypatch.setattr(
        baijiu_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            pd.DataFrame(),
            [
                (
                    "annual",
                    "公司销售飞天茅台和系列酒，持续关注经销商回款、合同负债、渠道库存和批价。",
                )
            ],
        ),
    )
    monkeypatch.setattr(
        baijiu_research,
        "_fetch_income_statement_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20251231", "20241231"],
                "total_revenue": [100.0, 95.0],
                "n_income_attr_p": [55.0, 50.0],
            }
        ),
    )
    monkeypatch.setattr(
        baijiu_research,
        "_fetch_balance_sheet_data",
        lambda *args, **kwargs: pd.DataFrame(
            {
                "end_date": ["20260331", "20251231", "20250331"],
                "contract_liab": [30.0, 80.0, 32.0],
                "inventories": [400.0, 390.0, 360.0],
            }
        ),
    )
    monkeypatch.setattr(
        baijiu_research,
        "_fetch_cashflow_data",
        lambda *args, **kwargs: pd.DataFrame(
            {"end_date": ["20251231"], "n_cashflow_act": [60.0], "c_fr_sale_sg": [110.0]}
        ),
    )
    monkeypatch.setattr(
        baijiu_research,
        "_fetch_fina_indicator",
        lambda *args, **kwargs: pd.DataFrame(
            {"end_date": ["20251231"], "roe": [30.0], "grossprofit_margin": [91.0]}
        ),
    )

    rendered = get_baijiu_context("600519.SH", "2026-05-27")

    assert "Status: triggered" in rendered
    assert "curated A-share baijiu ticker list" in rendered
    assert "Contract liabilities must be read with seasonality" in rendered
    assert "Required Peer Basket" in rendered
    assert "600519.SH" in rendered


def test_baijiu_context_not_applicable_for_non_baijiu(monkeypatch):
    monkeypatch.setattr(
        baijiu_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"name": "测试科技", "industry": "软件服务"}),
    )
    monkeypatch.setattr(
        baijiu_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (pd.DataFrame(), [("annual", "主营软件开发。")]),
    )

    rendered = get_baijiu_context("301396.SZ", "2026-05-27")

    assert "Status: not_applicable" in rendered
