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
