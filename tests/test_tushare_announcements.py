import pandas as pd

from tradingagents.dataflows.tushare_a_stock import TushareDataError
from tradingagents.dataflows.tushare_research import (
    _fetch_announcements,
    _parse_cninfo_announcements,
)


def test_parse_cninfo_announcements_normalizes_pdf_rows():
    payload = {
        "announcements": [
            {
                "announcementTime": "2026-04-28 00:00:00",
                "announcementTitle": "<em>2025</em>年年度报告",
                "adjunctUrl": "finalpage/2026-04-28/123.PDF",
                "secName": "天承科技",
            }
        ]
    }

    result = _parse_cninfo_announcements(payload, "688603.SH")

    assert list(result.columns) == ["ann_date", "ts_code", "name", "title", "url", "rec_time"]
    assert result.iloc[0]["ann_date"] == "20260428"
    assert result.iloc[0]["ts_code"] == "688603.SH"
    assert result.iloc[0]["name"] == "天承科技"
    assert result.iloc[0]["title"] == "2025年年度报告"
    assert result.iloc[0]["url"] == "http://static.cninfo.com.cn/finalpage/2026-04-28/123.PDF"


def test_fetch_announcements_uses_cninfo_when_tushare_errors(monkeypatch):
    fallback = pd.DataFrame(
        [
            {
                "ann_date": "20260428",
                "ts_code": "688603.SH",
                "name": "天承科技",
                "title": "2025年年度报告",
                "url": "http://static.cninfo.com.cn/finalpage/2026-04-28/123.PDF",
                "rec_time": "20260428",
            }
        ]
    )

    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._safe_optional_query",
        lambda *args, **kwargs: TushareDataError("anns unavailable"),
    )
    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._fetch_cninfo_announcements",
        lambda *args, **kwargs: fallback,
    )

    result = _fetch_announcements("688603.SH", "2026-05-19", 900)

    assert result.equals(fallback)


def test_fetch_announcements_uses_cninfo_when_tushare_returns_empty(monkeypatch):
    fallback = pd.DataFrame(
        [
            {
                "ann_date": "20260428",
                "ts_code": "688603.SH",
                "name": "天承科技",
                "title": "2025年年度报告",
                "url": "http://static.cninfo.com.cn/finalpage/2026-04-28/123.PDF",
                "rec_time": "20260428",
            }
        ]
    )

    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._safe_optional_query",
        lambda *args, **kwargs: pd.DataFrame(),
    )
    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._fetch_cninfo_announcements",
        lambda *args, **kwargs: fallback,
    )

    result = _fetch_announcements("688603.SH", "2026-05-19", 900)

    assert result.equals(fallback)
