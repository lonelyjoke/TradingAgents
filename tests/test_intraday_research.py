import pandas as pd

from tradingagents.dataflows import intraday_research
from tradingagents.dataflows.intraday_research import get_intraday_behavior_context


def test_intraday_behavior_context_renders_minute_metrics(monkeypatch):
    times = pd.date_range("2026-06-05 09:30:00", periods=60, freq="1min")
    frame = pd.DataFrame(
        {
            "trade_time": times,
            "open": [10.0 + i * 0.01 for i in range(60)],
            "high": [10.1 + i * 0.01 for i in range(60)],
            "low": [9.9 + i * 0.01 for i in range(60)],
            "close": [10.0 + i * 0.015 for i in range(60)],
            "vol": [1000 + i * 10 for i in range(60)],
        }
    )

    monkeypatch.setattr(intraday_research, "_fetch_intraday_bars", lambda *args, **kwargs: frame)

    rendered = get_intraday_behavior_context("000001.SZ", "2026-06-05")

    assert "## Intraday Minute-Line Behavior Context" in rendered
    assert "Status: ready" in rendered
    assert "Minute bars" in rendered
    assert "First 30min return" in rendered
    assert "Last 30min return" in rendered
    assert "PM usage rule" in rendered
    assert "Do not use it as a substitute for company research" in rendered


def test_intraday_behavior_context_handles_empty_bars(monkeypatch):
    monkeypatch.setattr(
        intraday_research,
        "_fetch_intraday_bars",
        lambda *args, **kwargs: pd.DataFrame(),
    )

    rendered = get_intraday_behavior_context("000001.SZ", "2026-06-05")

    assert "Status: partial" in rendered
    assert "no usable" in rendered
