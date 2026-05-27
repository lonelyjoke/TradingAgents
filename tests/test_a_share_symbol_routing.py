import sys
import types

import pandas as pd
import pytest

if "yfinance" not in sys.modules:
    yf_module = types.ModuleType("yfinance")
    yf_module.Ticker = lambda *args, **kwargs: None
    yf_module.download = lambda *args, **kwargs: None
    yf_exceptions = types.ModuleType("yfinance.exceptions")

    class YFRateLimitError(Exception):
        pass

    yf_exceptions.YFRateLimitError = YFRateLimitError
    yf_module.exceptions = yf_exceptions
    sys.modules["yfinance"] = yf_module
    sys.modules["yfinance.exceptions"] = yf_exceptions

if "stockstats" not in sys.modules:
    stockstats_module = types.ModuleType("stockstats")
    stockstats_module.wrap = lambda data: data
    sys.modules["stockstats"] = stockstats_module

from tradingagents.dataflows import interface
from tradingagents.dataflows import alpha_vantage_common
from tradingagents.dataflows import tushare_a_stock
from tradingagents.dataflows.tushare_a_stock import TushareDataError


def test_infer_a_share_symbol_from_bare_code():
    assert tushare_a_stock.infer_a_share_symbol("301396") == "301396.SZ"
    assert tushare_a_stock.infer_a_share_symbol("600519") == "600519.SH"
    assert tushare_a_stock.infer_a_share_symbol("835185") == "835185.BJ"


def test_to_tushare_date_accepts_iso_and_compact_dates():
    assert tushare_a_stock._to_tushare_date("2026-01-01") == "20260101"
    assert tushare_a_stock._to_tushare_date("20260101") == "20260101"


def test_resolve_a_share_symbol_from_name(monkeypatch):
    universe = pd.DataFrame(
        [
            {"ts_code": "301396.SZ", "symbol": "301396", "name": "宏景科技"},
            {"ts_code": "600519.SH", "symbol": "600519", "name": "贵州茅台"},
        ]
    )
    monkeypatch.setattr(tushare_a_stock, "_fetch_stock_basic_universe", lambda: universe)
    tushare_a_stock._A_SHARE_SYMBOL_RESOLUTION_CACHE.clear()

    assert tushare_a_stock.resolve_a_share_symbol("宏景科技") == "301396.SZ"


def test_route_to_vendor_uses_tushare_for_bare_a_share_code(monkeypatch):
    calls = []

    def fake_tushare(symbol, start_date, end_date):
        calls.append((symbol, start_date, end_date))
        return "tushare-ok"

    def fake_yfinance(symbol, start_date, end_date):
        raise AssertionError("A-share shorthand should not route to yfinance")

    monkeypatch.setitem(
        interface.VENDOR_METHODS,
        "get_stock_data",
        {"tushare": fake_tushare, "yfinance": fake_yfinance},
    )
    monkeypatch.setattr(interface, "get_vendor", lambda category, method=None: "yfinance")

    assert interface.route_to_vendor("get_stock_data", "301396", "2026-01-01", "2026-01-10") == "tushare-ok"
    assert calls == [("301396.SZ", "2026-01-01", "2026-01-10")]


def test_route_to_vendor_uses_tushare_for_qualified_a_share_code(monkeypatch):
    calls = []

    def fake_tushare(symbol, start_date, end_date):
        calls.append((symbol, start_date, end_date))
        return "tushare-ok"

    def fake_yfinance(symbol, start_date, end_date):
        raise AssertionError("Exchange-qualified A-share should not route to yfinance")

    monkeypatch.setitem(
        interface.VENDOR_METHODS,
        "get_stock_data",
        {"yfinance": fake_yfinance, "tushare": fake_tushare},
    )
    monkeypatch.setattr(interface, "get_vendor", lambda category, method=None: "yfinance")

    assert interface.route_to_vendor("get_stock_data", "600519.SH", "2026-01-01", "2026-01-10") == "tushare-ok"
    assert calls == [("600519.SH", "2026-01-01", "2026-01-10")]


def test_tushare_stock_backfills_when_requested_window_is_empty(monkeypatch):
    calls = []

    class FakePro:
        def daily(self, ts_code, start_date, end_date):
            calls.append((ts_code, start_date, end_date))
            if start_date == "20260101":
                return pd.DataFrame()
            return pd.DataFrame(
                [
                    {
                        "ts_code": ts_code,
                        "trade_date": "20251230",
                        "open": 1500.0,
                        "high": 1510.0,
                        "low": 1490.0,
                        "close": 1505.0,
                        "vol": 10000.0,
                        "amount": 1505000.0,
                        "pre_close": 1498.0,
                        "change": 7.0,
                        "pct_chg": 0.4673,
                    },
                    {
                        "ts_code": ts_code,
                        "trade_date": "20251231",
                        "open": 1506.0,
                        "high": 1520.0,
                        "low": 1500.0,
                        "close": 1518.0,
                        "vol": 12000.0,
                        "amount": 1821600.0,
                        "pre_close": 1505.0,
                        "change": 13.0,
                        "pct_chg": 0.8638,
                    },
                ]
            )

    monkeypatch.setattr(
        tushare_a_stock,
        "get_tushare_pro_clients",
        lambda: [("configured_http_url", FakePro())],
    )

    result = tushare_a_stock.get_stock("600519.SH", "2026-01-01", "2026-05-27")

    assert "Notice: Requested window 2026-01-01 to 2026-05-27 returned no rows." in result
    assert "2025-12-31" in result
    assert calls[0] == ("600519.SH", "20260101", "20260527")
    assert calls[1][0] == "600519.SH"
    assert calls[1][2] == "20260527"


def test_tushare_daily_uses_official_fallback_after_empty_gateway(monkeypatch):
    class EmptyGateway:
        def daily(self, **kwargs):
            return pd.DataFrame()

    class OfficialGateway:
        def daily(self, **kwargs):
            return pd.DataFrame(
                [
                    {
                        "trade_date": "20240102",
                        "open": 100.0,
                        "high": 101.0,
                        "low": 99.0,
                        "close": 100.5,
                        "vol": 1000.0,
                        "amount": 100500.0,
                    }
                ]
            )

    monkeypatch.setattr(
        tushare_a_stock,
        "get_tushare_pro_clients",
        lambda: [("configured_http_url", EmptyGateway()), ("official", OfficialGateway())],
    )

    result = tushare_a_stock.get_stock("600519.SH", "2024-01-01", "2024-01-10")

    assert "# Tushare A-share daily data for 600519.SH" in result
    assert "2024-01-02" in result
    assert "100.5" in result


def test_default_vendor_prefers_yfinance_not_alpha(monkeypatch):
    calls = []

    def fake_alpha(symbol, start_date, end_date):
        raise AssertionError("default routing should not try Alpha Vantage first")

    def fake_yfinance(symbol, start_date, end_date):
        calls.append((symbol, start_date, end_date))
        return "yfinance-ok"

    monkeypatch.setitem(
        interface.VENDOR_METHODS,
        "get_stock_data",
        {"alpha_vantage": fake_alpha, "tushare": lambda *args: "tushare-ok", "yfinance": fake_yfinance},
    )
    monkeypatch.setattr(interface, "get_vendor", lambda category, method=None: "default")

    assert interface.route_to_vendor("get_stock_data", "AAPL", "2026-01-01", "2026-01-10") == "yfinance-ok"
    assert calls == [("AAPL", "2026-01-01", "2026-01-10")]


def test_missing_alpha_key_falls_back(monkeypatch):
    monkeypatch.delenv("ALPHA_VANTAGE_API_KEY", raising=False)

    def fake_yfinance(symbol, start_date, end_date):
        return "yfinance-ok"

    monkeypatch.setitem(
        interface.VENDOR_METHODS,
        "get_stock_data",
        {
            "alpha_vantage": lambda *args: (_ for _ in ()).throw(ValueError("ALPHA_VANTAGE_API_KEY environment variable is not set.")),
            "yfinance": fake_yfinance,
        },
    )
    monkeypatch.setattr(interface, "get_vendor", lambda category, method=None: "alpha_vantage,yfinance")

    assert interface.route_to_vendor("get_stock_data", "AAPL", "2026-01-01", "2026-01-10") == "yfinance-ok"


def test_alpha_get_api_key_missing_raises_fallback_error(monkeypatch):
    monkeypatch.delenv("ALPHA_VANTAGE_API_KEY", raising=False)

    with pytest.raises(alpha_vantage_common.AlphaVantageRateLimitError):
        alpha_vantage_common.get_api_key()


def test_route_to_vendor_rejects_unresolved_a_share_name(monkeypatch):
    monkeypatch.setattr(interface, "resolve_a_share_symbol", lambda symbol: None)
    monkeypatch.setattr(interface, "looks_like_a_share_query", lambda symbol: True)

    with pytest.raises(TushareDataError):
        interface.route_to_vendor("get_stock_data", "宏景科技", "2026-01-01", "2026-01-10")
