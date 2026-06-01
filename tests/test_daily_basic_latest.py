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
