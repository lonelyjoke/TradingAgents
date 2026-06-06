import pandas as pd

from tradingagents.dataflows import tushare_research as research
from tradingagents.dataflows.tushare_research import get_relative_strength_context


def _price_frame(symbol: str, start: float, step: float, periods: int = 280) -> pd.DataFrame:
    dates = pd.bdate_range("2025-06-02", periods=periods)
    rows = []
    for i, date in enumerate(dates):
        close = start * ((1 + step) ** i)
        rows.append(
            {
                "ts_code": symbol,
                "trade_date": date.strftime("%Y%m%d"),
                "close": close,
                "pct_chg": 0 if i == 0 else step * 100,
            }
        )
    return pd.DataFrame(rows)


def test_relative_strength_context_renders_outperformance(monkeypatch):
    symbols = {
        "300308.SZ": ("中际旭创", "通信设备"),
        "300001.SZ": ("Peer A", "通信设备"),
        "300002.SZ": ("Peer B", "通信设备"),
    }

    monkeypatch.setattr(
        research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": symbols.get(symbol, (symbol, ""))[0],
                "industry": symbols.get(symbol, ("", "通信设备"))[1],
            }
        ),
    )
    monkeypatch.setattr(research, "_get_pro_client", lambda: object())
    monkeypatch.setattr(
        research,
        "_fetch_stock_basic_universe",
        lambda pro: pd.DataFrame(
            [
                {"ts_code": code, "name": name, "industry": industry}
                for code, (name, industry) in symbols.items()
            ]
        ),
    )
    monkeypatch.setattr(
        research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"trade_date": "20260605", "total_mv": 8_000_000}),
    )
    monkeypatch.setattr(
        research,
        "_latest_daily_basic_market",
        lambda trade_date: pd.DataFrame(
            [
                {"ts_code": "300001.SZ", "total_mv": 7_000_000},
                {"ts_code": "300002.SZ", "total_mv": 6_000_000},
            ]
        ),
    )

    def fake_daily(symbol, start, end):
        if symbol == "300308.SZ":
            return _price_frame(symbol, 10, 0.006)
        return _price_frame(symbol, 10, 0.002)

    monkeypatch.setattr(research, "_fetch_daily", fake_daily)
    monkeypatch.setattr(
        research,
        "_query_optional_api",
        lambda api_name, **kwargs: _price_frame(kwargs["ts_code"], 1000, 0.001),
    )

    rendered = get_relative_strength_context("300308.SZ", "2026-06-05")

    assert "# Relative strength and index linkage" in rendered
    assert "relative_outperformer" in rendered
    assert "Relative Strength Window Table" in rendered
    assert "same-industry equal-weight basket" in rendered
    assert "excess_return" in rendered
    assert "correlation" in rendered
    assert "beta" in rendered


def test_relative_strength_chooses_chinext_style_benchmark(monkeypatch):
    monkeypatch.setattr(
        research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"total_mv": 1_000_000}),
    )

    code, name, reason = research._choose_style_benchmark(
        "300308.SZ",
        pd.Series({"industry": "通信设备"}),
        "2026-06-05",
    )

    assert code == "399006.SZ"
    assert "创业板" in name
    assert "创业板" in reason
