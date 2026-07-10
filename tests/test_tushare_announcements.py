import pandas as pd
from datetime import datetime, timedelta

from tradingagents.dataflows.tushare_a_stock import TushareDataError
from tradingagents.dataflows.tushare_research import (
    _fetch_announcements,
    _cninfo_stock_query_values,
    _earnings_guidance_section,
    _parse_cninfo_announcements,
)


def test_cninfo_stock_query_values_include_exchange_org_id():
    assert _cninfo_stock_query_values("000967.SZ")[0] == "000967,gssz0000967"
    assert _cninfo_stock_query_values("600519.SH")[0] == "600519,gssh0600519"
    assert _cninfo_stock_query_values("000967.SZ")[1] == "000967"


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
    assert result.iloc[0]["url"] == "https://static.cninfo.com.cn/finalpage/2026-04-28/123.PDF"


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


def test_fetch_announcements_includes_live_after_hours_next_day_cninfo(monkeypatch):
    today = datetime.now().date()
    next_day = today + timedelta(days=1)
    next_day_row = pd.DataFrame(
        [
            {
                "ann_date": next_day.strftime("%Y%m%d"),
                "ts_code": "000933.SZ",
                "name": "神火股份",
                "title": "河南神火煤电股份有限公司2026年半年度业绩预告",
                "url": "https://static.cninfo.com.cn/finalpage/2026-07-10/1225416665.PDF",
                "rec_time": next_day.strftime("%Y%m%d"),
            }
        ]
    )

    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._safe_optional_query",
        lambda *args, **kwargs: pd.DataFrame(),
    )

    def fake_cninfo(symbol, curr_date, look_back_days, **kwargs):
        if curr_date == next_day.strftime("%Y-%m-%d"):
            return next_day_row
        return pd.DataFrame(columns=["ann_date", "ts_code", "name", "title", "url", "rec_time"])

    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._fetch_cninfo_announcements",
        fake_cninfo,
    )

    result = _fetch_announcements("000933.SZ", today.strftime("%Y-%m-%d"), 7)

    assert not result.empty
    assert result.iloc[0]["title"] == "河南神火煤电股份有限公司2026年半年度业绩预告"
    assert result.iloc[0]["source_note"] == "cninfo_after_hours_next_day_official"


def test_earnings_guidance_section_extracts_preannouncement_text(monkeypatch):
    announcements = pd.DataFrame(
        [
            {
                "ann_date": "20260710",
                "ts_code": "000933.SZ",
                "name": "神火股份",
                "title": "河南神火煤电股份有限公司2026年半年度业绩预告",
                "url": "https://static.cninfo.com.cn/finalpage/2026-07-10/1225416665.PDF",
                "source_note": "cninfo_after_hours_next_day_official",
            }
        ]
    )
    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._download_announcement_text",
        lambda url: "\n".join(
            [
                "业绩预告期间：2026年1月1日至2026年6月30日",
                "归属于上市公司股东的净利润：480,000.00万元，同比增长152.04%",
                "扣除非经常性损益后的净利润：480,600.00万元，同比增长139.10%",
                "基本每股收益：2.169元/股",
                "本次业绩预告相关财务数据未经会计师事务所审计。",
            ]
        ),
    )

    section = _earnings_guidance_section(announcements)

    assert "Official Earnings Guidance / Performance Preannouncements" in section
    assert "480,000.00万元" in section
    assert "reconcile Q1, implied Q2, H1, H2 and full-year" in section
