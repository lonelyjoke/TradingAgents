import pandas as pd

from tradingagents.dataflows import insurance_research
from tradingagents.dataflows.insurance_research import get_insurance_context
from tradingagents.dataflows.filing_research import _select_industry_profile


def test_insurance_context_triggers_for_curated_insurer(monkeypatch):
    monkeypatch.setattr(
        insurance_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"ts_code": symbol, "name": "中国平安", "industry": "保险"}),
    )
    monkeypatch.setattr(
        insurance_research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"pe_ttm": 7.3, "pb": 0.95, "dv_ttm": 4.8}),
    )
    monkeypatch.setattr(
        insurance_research,
        "_fetch_fina_indicator",
        lambda symbol, curr_date: pd.DataFrame(
            [
                {
                    "end_date": "20251231",
                    "roe_annual": 13.9,
                    "roe": 2.5,
                    "netprofit_yoy": -7.4,
                    "debt_to_assets": 89.8,
                }
            ]
        ),
    )
    monkeypatch.setattr(
        insurance_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            [{"title": "中国平安2025年年度报告"}],
            [
                (
                    "中国平安2025年年度报告",
                    "寿险新业务价值增长，代理人产能提升。财产险综合成本率95.8%，"
                    "综合投资收益率保持稳健，偿付能力充足。",
                )
            ],
        ),
    )
    monkeypatch.setattr(
        insurance_research,
        "_fetch_stock_basic_universe",
        lambda: pd.DataFrame(
            [
                {"ts_code": "601318.SH", "name": "中国平安", "industry": "保险"},
                {"ts_code": "601601.SH", "name": "中国太保", "industry": "保险"},
            ]
        ),
    )

    rendered = get_insurance_context("601318.SH", "2026-06-04")

    assert "- Status: triggered" in rendered
    assert "Insurance-Native KPI Screen" in rendered
    assert "Required Insurance Valuation Bridge" in rendered
    assert "NBV" in rendered
    assert "P/EV" in rendered
    assert "COR" in rendered


def test_insurance_context_not_applicable_for_non_insurer(monkeypatch):
    monkeypatch.setattr(
        insurance_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series({"ts_code": symbol, "name": "测试科技", "industry": "软件服务"}),
    )

    rendered = get_insurance_context("300000.SZ", "2026-06-04")

    assert "- Status: not_applicable" in rendered
    assert "Do not force NBV" in rendered


def test_insurance_profile_wins_for_integrated_insurer_with_bank_subsidiary_text():
    reports = [
        (
            "2026年一季报",
            "平安银行不良贷款率1.05%，拨备覆盖率219.59%。"
            "公司新业务价值与内含价值持续改善，综合成本率保持稳定。",
        )
    ]

    assert _select_industry_profile("中国平安", "保险", reports) == "insurance"

