import pandas as pd
from datetime import datetime, timedelta

from tradingagents.dataflows.tushare_a_stock import TushareDataError
from tradingagents.dataflows.tushare_research import (
    _announcement_download_candidates,
    _download_announcement_text,
    _fetch_announcements,
    _cninfo_stock_query_values,
    _earnings_guidance_section,
    _parse_cninfo_announcements,
)
from tradingagents.dataflows.official_guidance import (
    official_guidance_record,
    parse_official_guidance_metrics,
    parse_official_guidance_record,
)


def test_official_guidance_metrics_survive_pdf_line_wrapping():
    raw = """
    历史对照：2024年半年度归属于上市公司股东的净利润为51,700万元。
    公司预计 2026 年半年度归属于上市公司股东的净利润为 690,000 万元左右。
    公司预计 2026 年半年度归属于上市公司股东扣除非经常性损益后的净
    利润为 485,000 万元左右。
    公司预计 2026 年半年度实现营业收入 1,150,000 万元左右。
    """

    metrics = parse_official_guidance_metrics(raw)
    record = official_guidance_record(metrics)

    assert metrics == {
        "period": "2026H1",
        "revenue_cny_mn": 11500.0,
        "parent_net_profit_cny_mn": 6900.0,
        "deducted_parent_net_profit_cny_mn": 4850.0,
    }
    assert parse_official_guidance_record(record) == metrics


def test_official_guidance_metrics_resolve_cninfo_current_and_prior_columns():
    """Regression for Shenhuo's real Poppler ``-layout`` text structure."""

    raw = """
               河南神火煤电股份有限公司
                2026 年半年度业绩预告
  一、本期业绩预计情况
  1、业绩预告期间：2026 年 1 月 1 日至 2026 年 6 月 30 日。
  2、业绩预告情况：预计净利润为正值且属于同向上升情形
  （1）以确数进行业绩预告的
                                            单位：万元
     项   目             本报告期                上年同期
                              480,000.00
归属于上市公司股东的净利润                                190,445.68
                 比上年同期增长        152.04%
                              480,600.00
扣除非经常性损益后的净利润                                201,006.92
                 比上年同期增长        139.10%
基本每股收益（元/股）                        2.169          0.860
  二、与会计师事务所沟通情况
"""

    metrics = parse_official_guidance_metrics(raw)
    record = official_guidance_record(metrics)

    assert metrics["period"] == "2026H1"
    assert metrics["parent_net_profit_cny_mn"] == 4800.0
    assert metrics["parent_net_profit_prior_cny_mn"] == 1904.4568
    assert metrics["deducted_parent_net_profit_cny_mn"] == 4806.0
    assert round(metrics["deducted_parent_net_profit_prior_cny_mn"], 4) == 2010.0692
    assert metrics["table_layout_control"] == "current_vs_prior_columns_resolved"
    assert "parent_net_profit_cny_mn=4800" in record
    assert "parent_net_profit_prior_cny_mn=1904.46" in record
    assert parse_official_guidance_record(record)["parent_net_profit_cny_mn"] == 4800.0


def test_cninfo_detail_url_resolves_to_static_pdf_before_dynamic_page():
    url = (
        "http://www.cninfo.com.cn/new/disclosure/detail?stockCode=603986"
        "&announcementId=1225417171&orgId=9900026561"
        "&announcementTime=2026-07-10"
    )

    assert _announcement_download_candidates(url)[0] == (
        "https://static.cninfo.com.cn/finalpage/2026-07-10/1225417171.PDF"
    )


def test_download_announcement_text_uses_resolved_cninfo_pdf(monkeypatch):
    requested = []

    class FakeResponse:
        headers = {"Content-Type": "application/pdf"}
        content = b"%PDF-fake"
        text = ""
        encoding = "utf-8"
        url = "https://static.cninfo.com.cn/finalpage/2026-07-10/1225417171.PDF"

        def raise_for_status(self):
            return None

    def fake_get(url, **kwargs):
        requested.append(url)
        return FakeResponse()

    monkeypatch.setattr("tradingagents.dataflows.tushare_research.requests.get", fake_get)
    monkeypatch.setattr(
        "tradingagents.dataflows.tushare_research._extract_pdf_text",
        lambda content: "预计2026年半年度归母净利润为690,000万元左右",
    )

    text = _download_announcement_text(
        "https://www.cninfo.com.cn/new/disclosure/detail?"
        "announcementId=1225417171&announcementTime=2026-07-10"
    )

    assert requested == [
        "https://static.cninfo.com.cn/finalpage/2026-07-10/1225417171.PDF"
    ]
    assert "690,000万元" in text


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
