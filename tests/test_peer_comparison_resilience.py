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


def test_peer_comparison_recovers_target_basic_from_universe(monkeypatch):
    latest = pd.Series({"trade_date": "20260520", "total_mv": 100, "pe_ttm": 6.0, "pb": 0.8, "dv_ttm": 5.0})

    class FakePro:
        pass

    universe = pd.DataFrame(
        [
            {"ts_code": "600036.SH", "name": "招商银行", "industry": "银行"},
            {"ts_code": "601398.SH", "name": "工商银行", "industry": "银行"},
        ]
    )
    market = pd.DataFrame(
        [
            {"ts_code": "600036.SH", "trade_date": "20260520", "total_mv": 100, "pe_ttm": 6.0, "pb": 0.8, "dv_ttm": 5.0},
            {"ts_code": "601398.SH", "trade_date": "20260520", "total_mv": 120, "pe_ttm": 5.0, "pb": 0.6, "dv_ttm": 6.0},
        ]
    )
    indicators = pd.DataFrame([{"roe": 12.0, "roa": 1.2, "netprofit_yoy": 1.0, "debt_to_assets": 90.0}])

    monkeypatch.setattr(tushare_research, "_fetch_stock_basic", lambda symbol: None)
    monkeypatch.setattr(tushare_research, "_fetch_daily_basic_latest", lambda symbol, curr_date: latest)
    monkeypatch.setattr(tushare_research, "_get_pro_client", lambda: FakePro())
    monkeypatch.setattr(tushare_research, "_fetch_stock_basic_universe", lambda pro: universe)
    monkeypatch.setattr(tushare_research, "_latest_daily_basic_market", lambda trade_date: market)
    monkeypatch.setattr(tushare_research, "_fetch_fina_indicator", lambda symbol, curr_date: indicators)

    rendered = tushare_research.get_peer_comparison("600036.SH", "2026-05-21")

    assert "招商银行" in rendered
    assert "Banking peer screen" in rendered
    assert "NIM" in rendered


def test_peer_comparison_includes_competitor_analysis(monkeypatch):
    basic = pd.Series({"name": "Target Mobility", "industry": "Mobility"})
    latest = pd.Series(
        {
            "trade_date": "20260520",
            "total_mv": 100,
            "pe_ttm": 12.0,
            "pb": 1.6,
            "ps_ttm": 2.5,
            "dv_ttm": 1.0,
        }
    )

    class FakePro:
        pass

    universe = pd.DataFrame(
        [
            {"ts_code": "689009.SH", "name": "Target Mobility", "industry": "Mobility"},
            {"ts_code": "300001.SZ", "name": "Peer Alpha", "industry": "Mobility"},
            {"ts_code": "300002.SZ", "name": "Peer Beta", "industry": "Mobility"},
        ]
    )
    market = pd.DataFrame(
        [
            {
                "ts_code": "689009.SH",
                "trade_date": "20260520",
                "total_mv": 100,
                "pe_ttm": 12.0,
                "pb": 1.6,
                "ps_ttm": 2.5,
                "dv_ttm": 1.0,
            },
            {
                "ts_code": "300001.SZ",
                "trade_date": "20260520",
                "total_mv": 110,
                "pe_ttm": 8.0,
                "pb": 1.0,
                "ps_ttm": 1.5,
                "dv_ttm": 2.0,
            },
            {
                "ts_code": "300002.SZ",
                "trade_date": "20260520",
                "total_mv": 90,
                "pe_ttm": 18.0,
                "pb": 2.0,
                "ps_ttm": 3.0,
                "dv_ttm": 0.5,
            },
        ]
    )
    indicator_by_symbol = {
        "689009.SH": pd.DataFrame(
            [
                {
                    "end_date": "20251231",
                    "roe": 8.0,
                    "roa": 3.0,
                    "grossprofit_margin": 25.0,
                    "netprofit_yoy": 5.0,
                    "debt_to_assets": 50.0,
                }
            ]
        ),
        "300001.SZ": pd.DataFrame(
            [
                {
                    "end_date": "20251231",
                    "roe": 16.0,
                    "roa": 6.0,
                    "grossprofit_margin": 35.0,
                    "netprofit_yoy": 25.0,
                    "debt_to_assets": 30.0,
                }
            ]
        ),
        "300002.SZ": pd.DataFrame(
            [
                {
                    "end_date": "20251231",
                    "roe": 4.0,
                    "roa": 1.0,
                    "grossprofit_margin": 18.0,
                    "netprofit_yoy": -10.0,
                    "debt_to_assets": 70.0,
                }
            ]
        ),
    }

    monkeypatch.setattr(tushare_research, "_fetch_stock_basic", lambda symbol: basic)
    monkeypatch.setattr(tushare_research, "_fetch_daily_basic_latest", lambda symbol, curr_date: latest)
    monkeypatch.setattr(tushare_research, "_get_pro_client", lambda: FakePro())
    monkeypatch.setattr(tushare_research, "_fetch_stock_basic_universe", lambda pro: universe)
    monkeypatch.setattr(tushare_research, "_latest_daily_basic_market", lambda trade_date: market)
    monkeypatch.setattr(
        tushare_research,
        "_fetch_fina_indicator",
        lambda symbol, curr_date: indicator_by_symbol[symbol],
    )

    rendered = tushare_research.get_peer_comparison("689009.SH", "2026-05-21", peer_limit=3)

    assert "## Competitor Analysis For Peer Recommendation" in rendered
    assert "Peer Alpha" in rendered
    assert "score_gap_vs_target" in rendered
    assert "Verify filing-based business overlap" in rendered
    assert "compare that segment separately" in rendered
