import pandas as pd

from tradingagents.dataflows import tushare_a_stock


def test_daily_basic_latest_widens_window_and_falls_back_to_default_fields(monkeypatch):
    calls = []

    def fake_query(api_name, **kwargs):
        calls.append(kwargs.copy())
        if len(calls) < 4:
            return pd.DataFrame()
        return pd.DataFrame(
            [
                {
                    "ts_code": "601899.SH",
                    "trade_date": "20260520",
                    "close": 30.19,
                    "pe_ttm": 13.0,
                    "total_mv": 80000000,
                }
            ]
        )

    monkeypatch.setattr(tushare_a_stock, "_query_pro_with_fallback", fake_query)

    row = tushare_a_stock._fetch_daily_basic_latest("601899.SH", "2026-06-01")

    assert row is not None
    assert row["trade_date"] == "20260520"
    assert row["pe_ttm"] == 13.0
    assert calls[-1]["start_date"] == "20260201"
    assert "fields" not in calls[-1]


def test_daily_basic_latest_falls_back_to_trade_date_queries(monkeypatch):
    calls = []

    def fake_query(api_name, **kwargs):
        calls.append(kwargs.copy())
        if kwargs.get("trade_date") == "20260603":
            return pd.DataFrame(
                [
                    {
                        "ts_code": "601600.SH",
                        "trade_date": "20260603",
                        "close": 12.01,
                        "pe_ttm": 14.05,
                    }
                ]
            )
        return pd.DataFrame()

    monkeypatch.setattr(tushare_a_stock, "_query_pro_with_fallback", fake_query)

    row = tushare_a_stock._fetch_daily_basic_latest("601600.SH", "2026-06-04")

    assert row is not None
    assert row["trade_date"] == "20260603"
    assert any(call.get("trade_date") == "20260603" for call in calls)


def test_daily_falls_back_to_trade_date_queries(monkeypatch):
    calls = []

    def fake_query(api_name, **kwargs):
        calls.append(kwargs.copy())
        if kwargs.get("trade_date") == "20260603":
            return pd.DataFrame(
                [
                    {
                        "ts_code": "601600.SH",
                        "trade_date": "20260603",
                        "open": 12.0,
                        "high": 12.2,
                        "low": 11.9,
                        "close": 12.01,
                        "vol": 1000,
                        "amount": 12000,
                    }
                ]
            )
        return pd.DataFrame()

    monkeypatch.setattr(tushare_a_stock, "_query_pro_with_fallback", fake_query)

    data = tushare_a_stock._fetch_daily("601600.SH", "2026-04-20", "2026-06-04")

    assert not data.empty
    assert data.iloc[-1]["Date"].strftime("%Y-%m-%d") == "2026-06-03"
    assert data.iloc[-1]["Close"] == 12.01
    assert any(call.get("trade_date") == "20260603" for call in calls)


def test_tushare_query_retries_empty_configured_gateway(monkeypatch):
    calls = {"count": 0}

    class FlakyGateway:
        def daily_basic(self, **kwargs):
            calls["count"] += 1
            if calls["count"] == 1:
                return pd.DataFrame()
            return pd.DataFrame(
                [
                    {
                        "ts_code": kwargs["ts_code"],
                        "trade_date": "20260604",
                        "close": 10.9,
                    }
                ]
            )

    monkeypatch.setattr(
        tushare_a_stock,
        "get_tushare_pro_clients",
        lambda: [("configured_http_url", FlakyGateway())],
    )
    monkeypatch.setattr(tushare_a_stock.time, "sleep", lambda *_args, **_kwargs: None)

    result = tushare_a_stock._query_pro_with_fallback(
        "daily_basic",
        ts_code="601600.SH",
        start_date="20260601",
        end_date="20260604",
    )

    assert calls["count"] == 2
    assert result.iloc[0]["close"] == 10.9


def test_fundamentals_continues_when_daily_basic_times_out(monkeypatch):
    monkeypatch.setattr(
        tushare_a_stock,
        "_fetch_stock_basic",
        lambda symbol: {
            "name": "中国平安",
            "area": "深圳",
            "industry": "保险",
            "market": "主板",
            "exchange": "SSE",
            "list_date": "20070301",
        },
    )
    monkeypatch.setattr(
        tushare_a_stock,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: (_ for _ in ()).throw(
            tushare_a_stock.TushareDataError("daily_basic unavailable: read timeout")
        ),
    )
    monkeypatch.setattr(tushare_a_stock, "_fetch_fina_indicator", lambda *args: pd.DataFrame())
    monkeypatch.setattr(tushare_a_stock, "_fetch_income_statement_data", lambda *args: pd.DataFrame())
    monkeypatch.setattr(tushare_a_stock, "_fetch_balance_sheet_data", lambda *args: pd.DataFrame())
    monkeypatch.setattr(tushare_a_stock, "_fetch_cashflow_data", lambda *args: pd.DataFrame())

    report = tushare_a_stock.get_fundamentals("601318.SH", "2026-06-03")

    assert "Tushare A-share fundamentals for 601318.SH" in report
    assert "Name: 中国平安" in report
    assert "Snapshot unavailable" in report
    assert "daily_basic unavailable" in report
