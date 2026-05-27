import pandas as pd

from tradingagents.dataflows import compute_leasing_research as clr
from tradingagents.dataflows.compute_leasing_research import (
    ComputeEvidenceHit,
    get_compute_leasing_context,
)
from tradingagents.dataflows.data_coverage import classify_context_coverage


def _empty_sources(monkeypatch):
    monkeypatch.setattr(clr, "_load_financial_report_texts", lambda *args, **kwargs: (pd.DataFrame(), []))
    monkeypatch.setattr(clr, "_fetch_announcements", lambda *args, **kwargs: pd.DataFrame())
    monkeypatch.setattr(clr, "fetch_investor_interaction_history", lambda *args, **kwargs: pd.DataFrame())
    monkeypatch.setattr(clr, "_fetch_major_news", lambda *args, **kwargs: pd.DataFrame())
    monkeypatch.setattr(clr, "_fetch_news_feed", lambda *args, **kwargs: pd.DataFrame())
    monkeypatch.setattr(clr, "_fetch_stock_basic", lambda symbol: pd.Series({"name": "TestCo", "industry": "software"}))


def test_compute_leasing_context_stays_dormant_without_trigger(monkeypatch):
    _empty_sources(monkeypatch)

    context = get_compute_leasing_context("300000.SZ", "2026-05-25")

    assert "Status: not_applicable" in context
    assert "do not inject compute-leasing analysis" in context
    assert classify_context_coverage("compute_leasing", context).status == "not_applicable"


def test_compute_leasing_context_triggers_on_official_filing_strong_signal(monkeypatch):
    _empty_sources(monkeypatch)
    monkeypatch.setattr(
        clr,
        "_load_financial_report_texts",
        lambda *args, **kwargs: (
            pd.DataFrame(),
            [
                (
                    "2025 annual report",
                    "\u516c\u53f8\u5df2\u5f00\u5c55\u7b97\u529b\u79df\u8d41\u4e1a\u52a1\uff0c"
                    "\u5e76\u63a8\u8fdb\u667a\u7b97\u4e2d\u5fc3\u5efa\u8bbe\u548c\u5ba2\u6237\u4ea4\u4ed8\u3002",
                )
            ],
        ),
    )

    context = get_compute_leasing_context("300000.SZ", "2026-05-25")

    assert "Status: triggered" in context
    assert "Asset gate" in context
    assert "Unit-economics gate" in context
    assert "SOTP gate" in context


def test_compute_leasing_context_does_not_trigger_on_news_only(monkeypatch):
    _empty_sources(monkeypatch)
    monkeypatch.setattr(
        clr,
        "_fetch_major_news",
        lambda *args, **kwargs: pd.DataFrame(
            [
                {
                    "pub_time": "2026-05-24 09:00:00",
                    "title": "market discusses AI compute leasing theme",
                    "content": "\u5e02\u573a\u4f20\u95fb\u516c\u53f8\u6d89\u53ca\u7b97\u529b\u79df\u8d41\u6982\u5ff5",
                    "src": "media",
                }
            ]
        ),
    )

    context = get_compute_leasing_context("300000.SZ", "2026-05-25")

    assert "Status: not_applicable" in context
    assert "Weak/Non-triggering Mentions" in context
    assert "News-only mentions cannot support valuation uplift" not in context


def test_trigger_verdict_accepts_multiple_official_weak_signals_with_monetization():
    hits = [
        ComputeEvidenceHit(
            source="announcement",
            date="20260501",
            title="project progress",
            excerpt="\u6570\u636e\u4e2d\u5fc3\u5efa\u8bbe\u9879\u76ee\u4e0e\u5ba2\u6237\u4ea4\u4ed8",
            matched_terms=("\u6570\u636e\u4e2d\u5fc3",),
            evidence_grade="weak",
        ),
        ComputeEvidenceHit(
            source="interaction",
            date="20260502",
            title="investor question",
            excerpt="\u516c\u53f8\u6b63\u5728\u63a8\u8fdbGPU\u670d\u52a1\u5668\u4e0a\u67b6",
            matched_terms=("GPU", "\u670d\u52a1\u5668"),
            evidence_grade="weak",
        ),
    ]

    triggered, reason = clr._trigger_verdict(hits)

    assert triggered
    assert "multiple official weak compute signals" in reason
