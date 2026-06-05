from pathlib import Path

import pandas as pd
import pytest

from tradingagents.dataflows import a_share_preflight
from tradingagents.dataflows.a_share_preflight import (
    AShareDataPreflightError,
    run_a_share_data_preflight,
)
from tradingagents.dataflows.tushare_a_stock import TushareDataError


def _ready_daily(*_args, **_kwargs):
    return (
        pd.DataFrame(
            {
                "Date": [pd.Timestamp("2026-06-02")],
                "Close": [50.0],
            }
        ),
        "",
    )


def _ready_frame(*_args, **_kwargs):
    return pd.DataFrame({"end_date": ["20260331"], "value": [1.0]})


def _ready_filing_text(*_args, **_kwargs):
    return (
        pd.DataFrame(
            [
                {
                    "ann_date": "20260429",
                    "title": "2026 first-quarter report",
                    "url": "https://example.com/q1.pdf",
                }
            ]
        ),
        [("2026 first-quarter report", "readable filing text " * 80)],
    )


def test_a_share_preflight_passes_when_core_market_and_financial_data_ready(monkeypatch):
    monkeypatch.setattr(a_share_preflight, "_fetch_stock_basic", lambda symbol: {"name": "中国平安", "industry": "保险"})
    monkeypatch.setattr(a_share_preflight, "_fetch_daily_with_backfill", _ready_daily)
    monkeypatch.setattr(
        a_share_preflight,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"trade_date": "20260602", "pe_ttm": 8.0}),
    )
    monkeypatch.setattr(a_share_preflight, "_fetch_fina_indicator", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_income_statement_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_balance_sheet_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_cashflow_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_load_financial_report_texts", _ready_filing_text)

    rendered = run_a_share_data_preflight(
        "601318.SH",
        "2026-06-03",
        selected_analysts=["market", "fundamentals"],
    )

    assert "A-share Data Preflight for 601318.SH" in rendered
    assert "| daily_basic | ready | latest 2026-06-02 |" in rendered
    assert "| cashflow | ready |" in rendered
    assert "| filing_text | ready |" in rendered


def test_a_share_preflight_fails_fast_when_daily_basic_unavailable(monkeypatch):
    monkeypatch.setattr(a_share_preflight, "_fetch_stock_basic", lambda symbol: {"name": "中国平安", "industry": "保险"})
    monkeypatch.setattr(a_share_preflight, "_fetch_daily_with_backfill", _ready_daily)
    monkeypatch.setattr(
        a_share_preflight,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: (_ for _ in ()).throw(
            TushareDataError("daily_basic unavailable: read timeout")
        ),
    )
    monkeypatch.setattr(a_share_preflight, "_fetch_fina_indicator", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_income_statement_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_balance_sheet_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_cashflow_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_load_financial_report_texts", _ready_filing_text)

    with pytest.raises(AShareDataPreflightError) as excinfo:
        run_a_share_data_preflight(
            "601318.SH",
            "2026-06-03",
            selected_analysts=["market", "fundamentals"],
        )

    message = str(excinfo.value)
    assert "A-share data preflight failed" in message
    assert "daily_basic" in message
    assert "read timeout" in message


def test_a_share_preflight_uses_curated_stock_basic_fallback(monkeypatch):
    monkeypatch.setattr(
        a_share_preflight,
        "_fetch_stock_basic",
        lambda symbol: (_ for _ in ()).throw(RuntimeError("gateway empty")),
    )
    monkeypatch.setattr(a_share_preflight, "_fetch_daily_with_backfill", _ready_daily)
    monkeypatch.setattr(
        a_share_preflight,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"trade_date": "20260602", "pe_ttm": 8.0}),
    )
    monkeypatch.setattr(a_share_preflight, "_fetch_fina_indicator", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_income_statement_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_balance_sheet_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_cashflow_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_load_financial_report_texts", _ready_filing_text)

    rendered = run_a_share_data_preflight(
        "601600.SH",
        "2026-06-03",
        selected_analysts=["market", "fundamentals"],
    )

    assert "| stock_basic | ready | 中国铝业 / 铝 (curated fallback;" in rendered


def test_a_share_preflight_fails_fast_when_statement_data_missing(monkeypatch):
    monkeypatch.setattr(a_share_preflight, "_fetch_stock_basic", lambda symbol: {"name": "中国平安", "industry": "保险"})
    monkeypatch.setattr(a_share_preflight, "_fetch_daily_with_backfill", _ready_daily)
    monkeypatch.setattr(
        a_share_preflight,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"trade_date": "20260602"}),
    )
    monkeypatch.setattr(a_share_preflight, "_fetch_fina_indicator", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_income_statement_data", lambda *args: pd.DataFrame())
    monkeypatch.setattr(a_share_preflight, "_fetch_balance_sheet_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_cashflow_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_load_financial_report_texts", _ready_filing_text)

    with pytest.raises(AShareDataPreflightError) as excinfo:
        run_a_share_data_preflight(
            "601318.SH",
            "2026-06-03",
            selected_analysts=["fundamentals"],
        )

    assert "income" in str(excinfo.value)
    assert "no rows returned" in str(excinfo.value)


def test_a_share_preflight_fails_fast_when_filing_text_missing(monkeypatch):
    monkeypatch.setattr(a_share_preflight, "_fetch_stock_basic", lambda symbol: {"name": "安井食品", "industry": "食品"})
    monkeypatch.setattr(a_share_preflight, "_fetch_daily_with_backfill", _ready_daily)
    monkeypatch.setattr(
        a_share_preflight,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"trade_date": "20260602"}),
    )
    monkeypatch.setattr(a_share_preflight, "_fetch_fina_indicator", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_income_statement_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_balance_sheet_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_cashflow_data", _ready_frame)
    monkeypatch.setattr(
        a_share_preflight,
        "_load_financial_report_texts",
        lambda *args, **kwargs: (pd.DataFrame(), []),
    )
    monkeypatch.setattr(
        a_share_preflight,
        "_financial_report_text_audit_markdown",
        lambda *args, **kwargs: "mock filing text audit",
    )

    with pytest.raises(AShareDataPreflightError) as excinfo:
        run_a_share_data_preflight(
            "603345.SH",
            "2026-06-05",
            selected_analysts=["market", "fundamentals"],
        )

    message = str(excinfo.value)
    assert "filing_text" in message
    assert "no readable annual/semiannual/quarterly report text returned" in message
    assert "mock filing text audit" in message


def test_a_share_preflight_allows_explicit_filing_text_bypass(monkeypatch):
    monkeypatch.setattr(a_share_preflight, "_fetch_stock_basic", lambda symbol: {"name": "安井食品", "industry": "食品"})
    monkeypatch.setattr(a_share_preflight, "_fetch_daily_with_backfill", _ready_daily)
    monkeypatch.setattr(
        a_share_preflight,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"trade_date": "20260602"}),
    )
    monkeypatch.setattr(a_share_preflight, "_fetch_fina_indicator", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_income_statement_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_balance_sheet_data", _ready_frame)
    monkeypatch.setattr(a_share_preflight, "_fetch_cashflow_data", _ready_frame)

    rendered = run_a_share_data_preflight(
        "603345.SH",
        "2026-06-05",
        selected_analysts=["market", "fundamentals"],
        require_filing_text=False,
    )

    assert "filing_text" not in rendered


def test_trading_graph_runs_preflight_before_context_fetch():
    source = (
        Path(__file__).resolve().parents[1]
        / "tradingagents"
        / "graph"
        / "trading_graph.py"
    ).read_text(encoding="utf-8")

    assert "run_a_share_data_preflight" in source
    assert "self._run_a_share_data_preflight(company_name, trade_date)" in source
    assert "a_share_filing_text_preflight_enabled" in source
