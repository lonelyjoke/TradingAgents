import pandas as pd

from tradingagents.dataflows import medical_device_research
from tradingagents.dataflows.filing_research import _select_industry_profile
from tradingagents.dataflows.medical_device_research import get_medical_device_context


def test_medical_device_context_triggers_for_curated_mindray(monkeypatch):
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": "\u8fc8\u745e\u533b\u7597",
                "industry": "\u533b\u7597\u5668\u68b0",
            }
        ),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"pe_ttm": 25.0, "pb": 6.2, "dv_ttm": 2.1}),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_fina_indicator",
        lambda symbol, curr_date: pd.DataFrame(
            [
                {
                    "end_date": "20251231",
                    "roe_annual": 28.5,
                    "grossprofit_margin": 64.2,
                    "netprofit_margin": 31.8,
                    "netprofit_yoy": 8.1,
                    "or_yoy": 6.5,
                }
            ]
        ),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            [{"title": "\u8fc8\u745e\u533b\u75972025\u5e74\u5e74\u62a5"}],
            [
                (
                    "\u8fc8\u745e\u533b\u75972025\u5e74\u5e74\u62a5",
                    "\u516c\u53f8\u76d1\u62a4\u4eea\u3001\u9ebb\u9189\u673a\u3001\u8d85\u58f0\u548cIVD\u4ea7\u54c1\u6301\u7eed\u63a8\u8fdb\u88c5\u673a\uff0c"
                    "\u8bd5\u5242\u8017\u6750\u6536\u5165\u968f\u68c0\u9a8c\u8bbe\u5907\u88c5\u673a\u589e\u957f\uff0c\u6d77\u5916\u6e20\u9053\u548cFDA/CE\u6ce8\u518c\u7ee7\u7eed\u5b8c\u5584\u3002",
                )
            ],
        ),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_stock_basic_universe",
        lambda: pd.DataFrame(
            [
                {"ts_code": "300760.SZ", "name": "\u8fc8\u745e\u533b\u7597", "industry": "\u533b\u7597\u5668\u68b0"},
                {"ts_code": "688271.SH", "name": "\u8054\u5f71\u533b\u7597", "industry": "\u533b\u7597\u5668\u68b0"},
            ]
        ),
    )

    rendered = get_medical_device_context("300760.SZ", "2026-06-04")

    assert "- Status: triggered" in rendered
    assert "Medical-Device KPI Screen" in rendered
    assert "Business Model / Evidence Gate" in rendered
    assert "Medical-Device Evidence Gate Matrix" in rendered
    assert "Company-Specific Follow-Up Questions" in rendered
    assert "Depth Gate Verdict" in rendered
    assert "Required Medical-Device Valuation Bridge" in rendered
    assert "installed base" in rendered
    assert "IVD" in rendered
    assert "VBP" in rendered
    assert "Europe / overseas growth" in rendered


def test_medical_device_context_marks_thin_gates(monkeypatch):
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": "\u8fc8\u745e\u533b\u7597",
                "industry": "\u533b\u7597\u5668\u68b0",
            }
        ),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_daily_basic_latest",
        lambda symbol, curr_date: pd.Series({"pe_ttm": 25.0, "pb": 6.2, "dv_ttm": 2.1}),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_fina_indicator",
        lambda symbol, curr_date: pd.DataFrame(),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: (
            [],
            [("\u5e74\u62a5", "\u516c\u53f8\u662f\u533b\u7597\u5668\u68b0\u5e73\u53f0\uff0c\u4f46\u672a\u62ab\u9732\u66f4\u591a\u7ec6\u8282\u3002")],
        ),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_stock_basic_universe",
        lambda: pd.DataFrame(),
    )

    rendered = get_medical_device_context("300760.SZ", "2026-06-04")

    assert "Evidence-Limited" in rendered
    assert "missing" in rendered


def test_medical_device_context_not_applicable_for_non_device(monkeypatch):
    monkeypatch.setattr(
        medical_device_research,
        "_fetch_stock_basic",
        lambda symbol: pd.Series(
            {
                "ts_code": symbol,
                "name": "\u6d4b\u8bd5\u8f6f\u4ef6",
                "industry": "\u8f6f\u4ef6\u670d\u52a1",
            }
        ),
    )
    monkeypatch.setattr(
        medical_device_research,
        "_load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: ([], []),
    )

    rendered = get_medical_device_context("300000.SZ", "2026-06-04")

    assert "- Status: not_applicable" in rendered
    assert "Do not force installed-base" in rendered


def test_medical_device_profile_routes_mindray_filing_text():
    reports = [
        (
            "\u8fc8\u745e\u533b\u75972025\u5e74\u5e74\u62a5",
            "\u516c\u53f8\u533b\u7597\u5668\u68b0\u4ea7\u54c1\u5305\u62ec\u76d1\u62a4\u4eea\u3001\u9ebb\u9189\u673a\u3001"
            "\u8d85\u58f0\u3001\u4f53\u5916\u8bca\u65adIVD\u548c\u8bca\u65ad\u8bd5\u5242\uff0c\u6301\u7eed\u63a8\u8fdb\u8bbe\u5907\u66f4\u65b0\u548c\u6d77\u5916\u6ce8\u518c\u8bc1\u3002",
        )
    ]

    assert _select_industry_profile("\u8fc8\u745e\u533b\u7597", "\u533b\u7597\u5668\u68b0", reports) == "medical_device"
