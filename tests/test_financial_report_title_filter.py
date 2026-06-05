import pandas as pd

from tradingagents.dataflows import thematic_research


def test_financial_report_announcements_match_normal_chinese_titles(monkeypatch):
    data = pd.DataFrame(
        [
            {
                "ann_date": "20260430",
                "ts_code": "000967.SZ",
                "name": "\u76c8\u5cf0\u73af\u5883",
                "title": "\u76c8\u5cf0\u73af\u5883\uff1a2025\u5e74\u5e74\u5ea6\u62a5\u544a",
                "url": "https://example.com/annual.pdf",
                "rec_time": "20260430",
            },
            {
                "ann_date": "20260430",
                "ts_code": "000967.SZ",
                "name": "\u76c8\u5cf0\u73af\u5883",
                "title": "\u76c8\u5cf0\u73af\u5883\uff1a2025\u5e74\u5e74\u5ea6\u62a5\u544a\u6458\u8981",
                "url": "https://example.com/summary.pdf",
                "rec_time": "20260430",
            },
            {
                "ann_date": "20260429",
                "ts_code": "000967.SZ",
                "name": "\u76c8\u5cf0\u73af\u5883",
                "title": "\u76c8\u5cf0\u73af\u5883\uff1a2026\u5e74\u7b2c\u4e00\u5b63\u5ea6\u62a5\u544a",
                "url": "https://example.com/q1.pdf",
                "rec_time": "20260429",
            },
        ]
    )

    monkeypatch.setattr(thematic_research, "_fetch_announcements", lambda *args: data)

    reports = thematic_research._financial_report_announcements(
        "000967.SZ", "2026-05-21", 900
    )

    assert len(reports) == 2
    assert reports["title"].str.contains("\u5e74\u5ea6\u62a5\u544a$").any()
    assert reports["title"].str.contains("\u7b2c\u4e00\u5b63\u5ea6\u62a5\u544a").any()
    assert not reports["title"].str.contains("\u6458\u8981").any()


def test_financial_report_announcements_use_cninfo_when_tushare_lacks_reports(monkeypatch):
    tushare_rows = pd.DataFrame(
        [
            {
                "ann_date": "20260510",
                "ts_code": "000967.SZ",
                "name": "\u76c8\u5cf0\u73af\u5883",
                "title": "\u5173\u4e8e\u53ec\u5f00\u4e1a\u7ee9\u8bf4\u660e\u4f1a\u7684\u516c\u544a",
                "url": "https://example.com/notice.pdf",
                "rec_time": "20260510",
            }
        ]
    )
    cninfo_rows = pd.DataFrame(
        [
            {
                "ann_date": "20260430",
                "ts_code": "000967.SZ",
                "name": "\u76c8\u5cf0\u73af\u5883",
                "title": "\u76c8\u5cf0\u73af\u5883\uff1a2025\u5e74\u5e74\u5ea6\u62a5\u544a",
                "url": "https://example.com/annual.pdf",
                "rec_time": "20260430",
            },
            {
                "ann_date": "20260429",
                "ts_code": "000967.SZ",
                "name": "\u76c8\u5cf0\u73af\u5883",
                "title": "\u76c8\u5cf0\u73af\u5883\uff1a2026\u5e74\u7b2c\u4e00\u5b63\u5ea6\u62a5\u544a",
                "url": "https://example.com/q1.pdf",
                "rec_time": "20260429",
            },
        ]
    )

    monkeypatch.setattr(thematic_research, "_fetch_announcements", lambda *args: tushare_rows)
    monkeypatch.setattr(thematic_research, "_fetch_cninfo_announcements", lambda *args, **kwargs: cninfo_rows)

    reports = thematic_research._financial_report_announcements(
        "000967.SZ", "2026-05-21", 900
    )

    assert len(reports) == 2
    assert reports["title"].str.contains("\u5e74\u5ea6\u62a5\u544a").any()
    assert reports["title"].str.contains("\u7b2c\u4e00\u5b63\u5ea6\u62a5\u544a").any()


def test_financial_report_title_filter_accepts_cached_mojibake_titles():
    data = pd.DataFrame(
        [
            {
                "ann_date": "20260430",
                "ts_code": "603345.SH",
                "name": "\u5b89\u4e95\u98df\u54c1",
                "title": "2025骞村勾搴︽姤鍛?",
                "url": "https://example.com/annual.pdf",
                "rec_time": "20260430",
            },
            {
                "ann_date": "20260429",
                "ts_code": "603345.SH",
                "name": "\u5b89\u4e95\u98df\u54c1",
                "title": "2026骞寸涓€瀛ｅ害鎶ュ憡",
                "url": "https://example.com/q1.pdf",
                "rec_time": "20260429",
            },
        ]
    )

    reports = thematic_research._filter_financial_report_announcements(data)

    assert len(reports) == 2
