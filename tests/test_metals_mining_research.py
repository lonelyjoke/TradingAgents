import pandas as pd

from tradingagents.dataflows import metals_mining_research
from tradingagents.dataflows.metals_mining_research import get_metals_mining_context


def test_metals_mining_context_skips_structured_battery_cell_company():
    rendered = get_metals_mining_context("300750.SZ", "2026-06-27")

    assert "- Status: not_applicable" in rendered


def test_metals_mining_context_triggers_for_curated_gold_miner(monkeypatch):
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": "\u5c71\u4e1c\u9ec4\u91d1",
                "industry": "\u9ec4\u91d1",
            }
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"pe_ttm": 18.0, "pb": 2.1, "dv_ttm": 1.2}),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_fina_indicator",
        lambda symbol, curr_date: pd.DataFrame(
            [
                {
                    "end_date": "20251231",
                    "roe_annual": 12.5,
                    "grossprofit_margin": 22.0,
                    "netprofit_yoy": 35.0,
                    "debt_to_assets": 58.0,
                    "ocf_yoy": 18.0,
                }
            ]
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            [{"title": "\u5c71\u4e1c\u9ec4\u91d12025\u5e74\u5e74\u62a5"}],
            [
                (
                    "\u5c71\u4e1c\u9ec4\u91d12025\u5e74\u5e74\u62a5",
                    "\u516c\u53f8\u9ec4\u91d1\u77ff\u5c71\u4ea7\u91cf\u589e\u957f\uff0c"
                    "\u8d44\u6e90\u50a8\u91cf\u3001\u77ff\u77f3\u54c1\u4f4d\u3001\u6743\u76ca\u4ea7\u91cf\u548c\u5355\u4f4d\u6210\u672c\u662f\u6838\u5fc3\u53d8\u91cf\uff0c"
                    "\u540c\u65f6\u5173\u6ce8\u5957\u671f\u4fdd\u503c\u548c\u5728\u5efa\u5de5\u7a0b\u8fbe\u4ea7\u3002",
                )
            ],
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_stock_basic_universe",
        lambda: pd.DataFrame(
            [
                {"ts_code": "600547.SH", "name": "\u5c71\u4e1c\u9ec4\u91d1", "industry": "\u9ec4\u91d1"},
                {"ts_code": "600489.SH", "name": "\u4e2d\u91d1\u9ec4\u91d1", "industry": "\u9ec4\u91d1"},
            ]
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "get_commodity_context",
        lambda symbol, curr_date, look_back_days=90: (
            "# Commodity and product price context\n\n"
            "## Metal Price Source Audit\n"
            "| metal | domestic_price_chain | overseas_cross_check |\n"
            "| --- | --- | --- |\n"
            "| Gold | Tushare fut_daily -> SHFE AU contracts | COMEX GC futures; LBMA gold benchmark |"
        ),
    )

    rendered = get_metals_mining_context("600547.SH", "2026-06-04")

    assert "- Status: triggered" in rendered
    assert "Metal Price Source Chain Audit" in rendered
    assert "Tushare fut_daily -> SHFE AU contracts" in rendered
    assert "COMEX GC futures" in rendered
    assert "Required Metals Valuation Bridge" in rendered
    assert "AISC" in rendered
    assert "NAV/SOTP" in rendered


def test_chalco_context_adds_nonferrous_cycle_rating_gate(monkeypatch):
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": "\u4e2d\u56fd\u94dd\u4e1a",
                "industry": "\u94dd",
            }
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"pe_ttm": 9.0, "pb": 2.3, "dv_ttm": 3.0}),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_fina_indicator",
        lambda symbol, curr_date: pd.DataFrame(
            [
                {
                    "end_date": "20260331",
                    "roe_annual": 18.0,
                    "grossprofit_margin": 20.0,
                    "netprofit_yoy": 45.0,
                    "debt_to_assets": 50.0,
                    "ocf_yoy": 80.0,
                }
            ]
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            [{"title": "\u4e2d\u56fd\u94dd\u4e1a2025\u5e74\u5e74\u62a5"}],
            [
                (
                    "\u4e2d\u56fd\u94dd\u4e1a2025\u5e74\u5e74\u62a5",
                    "\u516c\u53f8\u4e3b\u8981\u4ece\u4e8b\u94dd\u3001\u6c27\u5316\u94dd\u548c\u51b6\u70bc\u4e1a\u52a1\uff0c"
                    "\u5173\u6ce8\u94dd\u4ef7\u3001\u7535\u4ef7\u3001\u6c27\u5316\u94dd\u6210\u672c\u4e0e\u73b0\u91d1\u6d41\u3002",
                )
            ],
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_stock_basic_universe",
        lambda: pd.DataFrame(
            [
                {"ts_code": "601600.SH", "name": "\u4e2d\u56fd\u94dd\u4e1a", "industry": "\u94dd"},
                {"ts_code": "000807.SZ", "name": "\u4e91\u94dd\u80a1\u4efd", "industry": "\u94dd"},
            ]
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "get_commodity_context",
        lambda symbol, curr_date, look_back_days=90: (
            "# Commodity and product price context\n\n"
            "## Metal Price Source Audit\n"
            "| metal | domestic_price_chain | overseas_cross_check |\n"
            "| --- | --- | --- |\n"
            "| Aluminum | Tushare fut_daily -> SHFE AL contracts | LME aluminum futures |"
        ),
    )

    rendered = get_metals_mining_context("601600.SH", "2026-06-04")

    assert "Nonferrous Cycle Rating Gate" in rendered
    assert "Industry Cycle View" in rendered
    assert "Company Expression View" in rendered
    assert "Valuation/Odds View" in rendered
    assert "Tactical Attribution View" in rendered
    assert "Aluminum Demand Bridge" in rendered
    assert "Grid, PV, EV, lightweighting" in rendered
    assert "low PE / high PB" in rendered
    assert "Underweight/Sell" in rendered


def test_metals_mining_context_not_applicable_for_non_miner(monkeypatch):
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": "\u6d4b\u8bd5\u8f6f\u4ef6",
                "industry": "\u8f6f\u4ef6\u670d\u52a1",
            }
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: ([], []),
    )
    monkeypatch.setattr(metals_mining_research, "_inferred_metals", lambda symbol: ())

    rendered = get_metals_mining_context("300000.SZ", "2026-06-04")

    assert "- Status: not_applicable" in rendered
    assert "Do not force reserve" in rendered


def test_metals_mining_context_not_applicable_for_optical_module_resource_wording(monkeypatch):
    monkeypatch.setattr(
        metals_mining_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": "\u4e2d\u9645\u65ed\u521b",
                "industry": "\u901a\u4fe1\u8bbe\u5907",
            }
        ),
    )
    monkeypatch.setattr(
        metals_mining_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            [],
            [
                (
                    "2025 annual report",
                    "\u516c\u53f8\u56f4\u7ed5AI\u6570\u636e\u4e2d\u5fc3\u3001\u5ba2\u6237\u8d44\u6e90\u3001"
                    "\u4f9b\u5e94\u94fe\u8d44\u6e90\u4e0e\u539f\u6750\u6599\u4fdd\u969c\u5c55\u5f00\u7ecf\u8425\uff0c"
                    "\u4e3b\u8981\u4ea7\u54c1\u4e3a\u9ad8\u901f\u5149\u6a21\u5757\u3002",
                )
            ],
        ),
    )
    monkeypatch.setattr(metals_mining_research, "_inferred_metals", lambda symbol: ())

    rendered = get_metals_mining_context("300308.SZ", "2026-06-05")

    assert "- Status: not_applicable" in rendered
    assert "Do not force reserve" in rendered
