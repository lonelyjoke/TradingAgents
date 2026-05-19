import pandas as pd

from tradingagents.dataflows import price_earnings_decomposition as ped


def test_build_price_eps_pe_history_computes_eps_proxy():
    prices = pd.DataFrame(
        [
            {"ts_code": "000001.SZ", "trade_date": "20260102", "close": 10.0},
            {"ts_code": "000001.SZ", "trade_date": "20260103", "close": 12.0},
        ]
    )
    valuations = pd.DataFrame(
        [
            {"ts_code": "000001.SZ", "trade_date": "20260102", "pe_ttm": 10.0, "pb": 1.0, "ps_ttm": 2.0, "total_mv": 1000},
            {"ts_code": "000001.SZ", "trade_date": "20260103", "pe_ttm": 12.0, "pb": 1.1, "ps_ttm": 2.1, "total_mv": 1200},
        ]
    )

    history = ped._build_price_eps_pe_history(prices, valuations)

    assert len(history) == 2
    assert history.iloc[0]["eps_ttm_proxy"] == 1.0
    assert history.iloc[1]["eps_ttm_proxy"] == 1.0
    assert history.iloc[1]["market_cap_cny"] == 12_000_000


def test_classify_driver_distinguishes_eps_and_multiple():
    assert "earnings-led" in ped._classify_driver(0.20, 0.25, -0.04)
    assert "multiple-led" in ped._classify_driver(0.20, 0.01, 0.18)
    assert "double engine" in ped._classify_driver(0.40, 0.20, 0.15)
    assert "derating despite EPS growth" in ped._classify_driver(-0.10, 0.20, -0.25)


def test_same_price_summary_flags_lower_current_eps_support():
    history = pd.DataFrame(
        [
            {"trade_date": "20240102", "close": 10.0, "pe_ttm": 10.0, "eps_ttm_proxy": 1.0},
            {"trade_date": "20250102", "close": 10.2, "pe_ttm": 8.5, "eps_ttm_proxy": 1.2},
            {"trade_date": "20260501", "close": 10.0, "pe_ttm": 20.0, "eps_ttm_proxy": 0.5},
        ]
    )
    history["trade_dt"] = pd.to_datetime(history["trade_date"], format="%Y%m%d")

    summary = ped._same_price_summary(history, band=0.05, min_age_days=60)

    assert summary["similar_price_days"] == 2
    assert summary["latest_eps_vs_same_price_history"].startswith("-")
    assert "relies more on valuation hope" in summary["interpretation"]


def test_context_renders_with_mocked_tushare(monkeypatch):
    prices = pd.DataFrame(
        [
            {"ts_code": "000001.SZ", "trade_date": "20250102", "close": 10.0},
            {"ts_code": "000001.SZ", "trade_date": "20260702", "close": 15.0},
        ]
    )
    valuations = pd.DataFrame(
        [
            {"ts_code": "000001.SZ", "trade_date": "20250102", "pe_ttm": 10.0, "pb": 1.0, "ps_ttm": 2.0, "total_mv": 1000},
            {"ts_code": "000001.SZ", "trade_date": "20260702", "pe_ttm": 12.0, "pb": 1.2, "ps_ttm": 2.2, "total_mv": 1500},
        ]
    )

    def fake_query(api_name, **kwargs):
        if api_name == "daily":
            return prices
        if api_name == "daily_basic":
            return valuations
        raise AssertionError(api_name)

    monkeypatch.setattr(ped, "_query_optional_api", fake_query)
    monkeypatch.setattr(ped, "_fetch_stock_basic", lambda symbol: pd.Series({"name": "平安银行"}))

    text = ped.get_price_earnings_decomposition_context("000001.SZ", "2026-07-03")

    assert "Historical price-EPS-PE decomposition" in text
    assert "Price Move Decomposition" in text
    assert "EPS TTM proxy" in text
    assert "Portfolio Manager should integrate" in text
