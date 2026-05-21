import pandas as pd

from tradingagents.dataflows import tushare_research


def test_stock_basic_universe_falls_back_when_requested_fields_are_incomplete():
    class FakePro:
        def __init__(self):
            self.calls = 0

        def stock_basic(self, **kwargs):
            self.calls += 1
            if "fields" in kwargs:
                return pd.DataFrame([{"ts_code": "000967.SZ", "name": "Infore Env"}])
            return pd.DataFrame(
                [
                    {
                        "ts_code": "000967.SZ",
                        "name": "Infore Env",
                        "industry": "Environmental",
                    }
                ]
            )

    pro = FakePro()

    universe = tushare_research._fetch_stock_basic_universe(pro)

    assert pro.calls == 2
    assert "industry" in universe.columns


def test_peer_comparison_reports_missing_universe_columns_without_keyerror(monkeypatch):
    basic = pd.Series({"name": "Infore Env", "industry": "Environmental"})
    latest = pd.Series({"trade_date": "20260520", "total_mv": 100})

    class FakePro:
        pass

    monkeypatch.setattr(tushare_research, "_fetch_stock_basic", lambda symbol: basic)
    monkeypatch.setattr(tushare_research, "_fetch_daily_basic_latest", lambda symbol, curr_date: latest)
    monkeypatch.setattr(tushare_research, "_get_pro_client", lambda: FakePro())
    monkeypatch.setattr(
        tushare_research,
        "_fetch_stock_basic_universe",
        lambda pro: pd.DataFrame([{"ts_code": "000967.SZ", "name": "Infore Env"}]),
    )

    rendered = tushare_research.get_peer_comparison("000967.SZ", "2026-05-21")

    assert "Same-industry peer comparison unavailable" in rendered
    assert "industry" in rendered
