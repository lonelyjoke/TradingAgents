import pandas as pd

from tradingagents.dataflows import dividend_defensive_research as ddr
from tradingagents.dataflows.data_coverage import classify_context_coverage


def _base_mocks(monkeypatch, *, basic=None, daily=None, dividends=None, income=None, cashflow=None):
    monkeypatch.setattr(
        ddr,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(basic or {"name": "TestCo", "industry": "software"}),
    )
    monkeypatch.setattr(
        ddr,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series(daily or {"trade_date": "20260525", "dv_ttm": 0.4, "pe_ttm": 30, "pb": 4, "total_mv": 10000}),
    )
    monkeypatch.setattr(ddr, "_fetch_dividends", lambda symbol, curr_date, years: dividends if dividends is not None else pd.DataFrame())
    monkeypatch.setattr(ddr, "_fetch_income_statement_data", lambda symbol, curr_date, freq="annual", limit=6: income if income is not None else pd.DataFrame())
    monkeypatch.setattr(ddr, "_fetch_cashflow_data", lambda symbol, curr_date, freq="annual", limit=6: cashflow if cashflow is not None else pd.DataFrame())
    monkeypatch.setattr(ddr, "_fetch_fina_indicator", lambda symbol, curr_date: pd.DataFrame())
    monkeypatch.setattr(ddr, "_peer_tables", lambda symbol, basic, curr_date, trade_date, peer_limit: (pd.DataFrame(), pd.DataFrame(), []))


def test_dividend_defensive_context_stays_dormant_without_dividend_or_defensive_profile(monkeypatch):
    _base_mocks(monkeypatch)

    context = ddr.get_dividend_defensive_context("300000.SZ", "2026-05-26")

    assert "Status: not_applicable" in context
    assert "Do not force a high-dividend" in context
    assert classify_context_coverage("dividend_defensive", context).status == "not_applicable"


def test_dividend_defensive_context_triggers_for_stable_cash_cow(monkeypatch):
    dividends = pd.DataFrame(
        [
            {"ann_date": "20260401", "end_date": "20251231", "cash_div_tax": 1.2},
            {"ann_date": "20250401", "end_date": "20241231", "cash_div_tax": 1.1},
            {"ann_date": "20240401", "end_date": "20231231", "cash_div_tax": 1.0},
            {"ann_date": "20230401", "end_date": "20221231", "cash_div_tax": 1.0},
        ]
    )
    income = pd.DataFrame(
        [
            {"end_date": "20251231", "total_revenue": 1200, "n_income_attr_p": 160},
            {"end_date": "20241231", "total_revenue": 1150, "n_income_attr_p": 150},
            {"end_date": "20231231", "total_revenue": 1100, "n_income_attr_p": 145},
            {"end_date": "20221231", "total_revenue": 1000, "n_income_attr_p": 130},
        ]
    )
    cashflow = pd.DataFrame(
        [
            {"end_date": "20251231", "n_cashflow_act": 210, "c_pay_acq_const_fiolta": 35, "c_pay_dist_dpcp_int_exp": 70},
            {"end_date": "20241231", "n_cashflow_act": 205, "c_pay_acq_const_fiolta": 30, "c_pay_dist_dpcp_int_exp": 68},
        ]
    )
    _base_mocks(
        monkeypatch,
        basic={"name": "CashCow", "industry": "\u5bb6\u7535"},
        daily={"trade_date": "20260525", "dv_ttm": 3.6, "pe_ttm": 12, "pb": 2, "total_mv": 50000},
        dividends=dividends,
        income=income,
        cashflow=cashflow,
    )

    context = ddr.get_dividend_defensive_context("000001.SZ", "2026-05-26")

    assert "Status: triggered" in context
    assert "Defensive Dividend Rating: strong" in context
    assert "Dividend trap risk: low" in context


def test_dividend_defensive_context_triggers_for_telecom_operator(monkeypatch):
    _base_mocks(
        monkeypatch,
        basic={"name": "\u4e2d\u56fd\u7535\u4fe1", "industry": "\u7535\u4fe1\u8fd0\u8425"},
        daily={"trade_date": "20260525", "dv_ttm": 3.1, "dv_ratio": 60, "pe_ttm": 17, "pb": 1.2, "total_mv": 600000},
        income=pd.DataFrame([{"end_date": "20251231", "total_revenue": 500, "n_income_attr_p": 30}]),
        cashflow=pd.DataFrame(
            [{"end_date": "20251231", "n_cashflow_act": 90, "c_pay_acq_const_fiolta": 40, "c_pay_dist_dpcp_int_exp": 18}]
        ),
    )

    context = ddr.get_dividend_defensive_context("601728.SH", "2026-05-26")

    assert "Status: triggered" in context
    assert "Dividend defensive verification context" in context


def test_dividend_defensive_context_flags_trap_risk_on_cut_and_weak_coverage(monkeypatch):
    dividends = pd.DataFrame(
        [
            {"ann_date": "20260401", "end_date": "20251231", "cash_div_tax": 0.3},
            {"ann_date": "20250401", "end_date": "20241231", "cash_div_tax": 1.0},
            {"ann_date": "20240401", "end_date": "20231231", "cash_div_tax": 1.1},
        ]
    )
    income = pd.DataFrame([{"end_date": "20251231", "total_revenue": 800, "n_income_attr_p": -20}])
    cashflow = pd.DataFrame([{"end_date": "20251231", "n_cashflow_act": -50, "c_pay_acq_const_fiolta": 20, "c_pay_dist_dpcp_int_exp": 80}])
    _base_mocks(
        monkeypatch,
        daily={"trade_date": "20260525", "dv_ttm": 5.2, "pe_ttm": 8, "pb": 1.2, "total_mv": 12000},
        dividends=dividends,
        income=income,
        cashflow=cashflow,
    )

    context = ddr.get_dividend_defensive_context("300000.SZ", "2026-05-26")

    assert "Status: triggered" in context
    assert "Dividend trap risk: high" in context


def test_dividend_defensive_context_surfaces_alternatives(monkeypatch):
    _base_mocks(
        monkeypatch,
        daily={"trade_date": "20260525", "dv_ttm": 3.2, "pe_ttm": 12, "pb": 1.4, "total_mv": 10000},
        dividends=pd.DataFrame([{"ann_date": "20260401", "end_date": "20251231", "cash_div_tax": 1.0}]),
        income=pd.DataFrame([{"end_date": "20251231", "total_revenue": 1000, "n_income_attr_p": 120}]),
        cashflow=pd.DataFrame([{"end_date": "20251231", "n_cashflow_act": 160, "c_pay_acq_const_fiolta": 20, "c_pay_dist_dpcp_int_exp": 60}]),
    )
    same = pd.DataFrame(
        [
            {"ts_code": "000002.SZ", "name": "BetterPeer", "industry": "software", "dv_ttm": 4.0, "defensive_score": 88.0}
        ]
    )
    cross = pd.DataFrame(
        [
            {"ts_code": "600000.SH", "name": "YieldPeer", "industry": "\u94f6\u884c", "dv_ttm": 5.0, "defensive_score": 91.0}
        ]
    )
    monkeypatch.setattr(ddr, "_peer_tables", lambda symbol, basic, curr_date, trade_date, peer_limit: (same, cross, []))

    context = ddr.get_dividend_defensive_context("300000.SZ", "2026-05-26")

    assert "BetterPeer" in context
    assert "YieldPeer" in context
    assert "Cross-Industry Defensive Alternatives" in context
