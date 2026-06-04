import pandas as pd

from tradingagents.dataflows import price_move_attribution_research as attribution
from tradingagents.dataflows.price_move_attribution_research import (
    get_price_move_attribution_context,
)


def _daily_frame(symbol: str, drops: float = -9.0) -> pd.DataFrame:
    dates = pd.bdate_range("2026-05-01", periods=24)
    closes = [10 + i * 0.02 for i in range(23)]
    closes.append(closes[-1] * (1 + drops / 100))
    rows = []
    for i, (date, close) in enumerate(zip(dates, closes)):
        prev = closes[i - 1] if i else close
        rows.append(
            {
                "Date": date.strftime("%Y-%m-%d"),
                "Open": close,
                "High": close,
                "Low": close,
                "Close": close,
                "Volume": 1000,
                "Amount": 10000,
                "pre_close": prev,
                "change": close - prev,
                "pct_chg": 0 if i == 0 else (close / prev - 1) * 100,
            }
        )
    return pd.DataFrame(rows)


def test_price_move_attribution_flags_commodity_equity_divergence(monkeypatch):
    names = {
        "601600.SH": ("\u4e2d\u56fd\u94dd\u4e1a", "\u94dd"),
        "000807.SZ": ("\u4e91\u94dd\u80a1\u4efd", "\u94dd"),
        "000933.SZ": ("\u795e\u706b\u80a1\u4efd", "\u94dd"),
    }

    def fake_basic(symbol):
        name, industry = names.get(symbol, (symbol, "\u94dc"))
        return pd.Series({"ts_code": symbol, "name": name, "industry": industry})

    def fake_daily(symbol, start, end):
        if symbol == "601600.SH":
            return _daily_frame(symbol, -9.2)
        if symbol in {"000807.SZ", "000933.SZ"}:
            return _daily_frame(symbol, -6.0)
        return _daily_frame(symbol, -2.0)

    def fake_index(api_name, **kwargs):
        return pd.DataFrame(
            [
                {"trade_date": "20260603", "close": 1000, "pct_chg": 0.1},
                {"trade_date": "20260604", "close": 995, "pct_chg": -0.5},
            ]
        )

    monkeypatch.setattr(attribution, "_fetch_stock_basic", fake_basic)
    monkeypatch.setattr(attribution, "_fetch_daily", fake_daily)
    monkeypatch.setattr(
        attribution,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"volume_ratio": 1.6, "turnover_rate_f": 6.7, "pe_ttm": 12.7, "pb": 2.3}),
    )
    monkeypatch.setattr(attribution, "_query_pro_with_fallback", fake_index)
    monkeypatch.setattr(
        attribution,
        "_infer_products",
        lambda symbol: {
            "name": "\u4e2d\u56fd\u94dd\u4e1a",
            "products": [{"name": "Aluminum", "type": "futures", "role": "main product", "prefix": "AL", "exchange": "SHFE"}],
        },
    )
    monkeypatch.setattr(
        attribution,
        "_fetch_futures_product",
        lambda product, curr_date, look_back_days: {
            "latest_contract_or_source": "AL2607.SHF",
            "latest_price": "24315",
            "latest_date": "20260604",
            "change_over_window": "-0.5%",
            "evidence_status": "Verified by Tushare futures daily data.",
        },
    )
    monkeypatch.setattr(
        attribution,
        "_query_futures_history",
        lambda ts_code, exchange, start, end: pd.DataFrame(
            [
                {"trade_date": "20260603", "close": 24520},
                {"trade_date": "20260604", "close": 24315},
            ]
        ),
    )
    monkeypatch.setattr(attribution, "_fetch_announcements", lambda symbol, curr_date, days: pd.DataFrame())
    monkeypatch.setattr(
        attribution,
        "_fetch_major_news",
        lambda terms, curr_date, days, limit=10: pd.DataFrame(
            [
                {
                    "pub_time": "2026-06-04 10:30:00",
                    "src": "mock-news",
                    "title": "\u7f8e\u8054\u50a8\u52a0\u606f\u9884\u671f\u6270\u52a8\u6709\u8272\u91d1\u5c5e",
                    "content": "\u5b8f\u89c2\u5229\u7387\u4e0e\u7f8e\u5143\u56e0\u7d20\u5f71\u54cd\u6709\u8272\u677f\u5757\uff0c\u4f46\u94dd\u4ef7\u672a\u51fa\u73b0\u5927\u8dcc\u3002",
                }
            ]
        ),
    )
    monkeypatch.setattr(attribution, "_fetch_news_feed", lambda terms, curr_date, days, limit=10: pd.DataFrame())
    monkeypatch.setattr(attribution, "get_config", lambda: {"web_fact_check_enabled": False})

    rendered = get_price_move_attribution_context("601600.SH", "2026-06-04")

    assert "- Status: ready" in rendered
    assert "commodity_equity_divergence" in rendered
    assert "stock_specific_residual_weakness" in rendered
    assert "cross_metal_underperformance" in rendered
    assert "Attribution Residual Table" in rendered
    assert "Cross-Metal Equity Reference" in rendered
    assert "News & Rumor Probe" in rendered
    assert "plausible_but_incomplete" in rendered
    assert "emotionally undervalued" in rendered


def test_news_probe_marks_unsupported_commodity_crash_as_contradicted():
    commodities = pd.DataFrame([{"product": "Aluminum", "one_day_pct": -0.8}])

    grade, rationale = attribution._news_alignment(
        "\u5e02\u573a\u4f20\u94dd\u4ef7\u5927\u8dcc\u5bfc\u81f4\u4e2d\u56fd\u94dd\u4e1a\u627f\u538b",
        "tushare_major_news",
        commodities,
        "commodity_equity_divergence + cross_metal_underperformance",
    )

    assert grade == "contradicted"
    assert "did not move enough" in rationale
