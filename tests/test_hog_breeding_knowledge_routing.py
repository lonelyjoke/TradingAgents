import json
import sqlite3

from tradingagents.dataflows import knowledge_planet_research as kp
from tradingagents.dataflows.industry_kpi_research import build_industry_kpi_context
from tradingagents.dataflows.thesis_question_research import build_thesis_question_context


def test_hog_breeder_terms_expand_without_tushare(monkeypatch):
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)

    terms = kp._stock_terms("002714.SZ")

    assert "002714.SZ" in terms
    assert "002714" in terms
    assert "\u751f\u732a" in terms
    assert "\u732a\u4ef7" in terms
    assert "\u80fd\u7e41\u6bcd\u732a" in terms
    assert "\u7267\u539f" in terms


def test_hog_breeder_contexts_force_hog_playbook():
    kp_context = "# Knowledge Planet\n\u751f\u732a \u732a\u4ef7 \u4ed4\u732a \u80fd\u7e41\u6bcd\u732a \u7267\u539f \u5b8c\u5168\u6210\u672c"

    kpi = build_industry_kpi_context(
        "002714.SZ",
        "2026-06-20",
        knowledge_planet_context=kp_context,
    )
    questions = build_thesis_question_context(
        "002714.SZ",
        "2026-06-20",
        knowledge_planet_context=kp_context,
    )

    assert "hog breeding / live-hog cycle" in kpi
    assert "hog-breeding cyclical company" in questions
    assert "HG-1" in questions
    assert "HG-4" in questions


def test_single_stock_fusion_pack_is_the_first_reasoning_layer():
    lines = kp._stock_fusion_pack_lines(
        ticker="002714.SZ",
        preprocessed_snapshot={},
        items=[],
        reports=[],
        primary_terms=["002714.SZ", "\u7267\u539f"],
        expanded_terms=["\u751f\u732a", "\u732a\u4ef7"],
    )
    text = "\n".join(lines)

    assert "Single-Stock Knowledge Fusion Pack" in text
    assert "Hard / Proxy Clues To Fuse" in text
    assert "PDF / Research-Assumption Cross-Checks" not in text
    assert "pdf_assumptions" not in text
    assert "downstream agents should use this fusion pack first" in text


def test_company_matches_rank_above_broad_hog_industry_items(tmp_path):
    db_path = tmp_path / "kp.sqlite"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.executescript(
        """
        CREATE TABLE kp_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            text TEXT,
            summary TEXT,
            source_type TEXT,
            published_at TEXT,
            imported_at TEXT,
            source_platform TEXT,
            source_file TEXT,
            credibility TEXT,
            author TEXT,
            tickers_json TEXT,
            company_names_json TEXT,
            industries_json TEXT,
            themes_json TEXT,
            content_hash TEXT
        );
        """
    )
    conn.execute(
        """
        INSERT INTO kp_items (
            title, text, summary, source_type, published_at, imported_at,
            source_platform, source_file, credibility, author, tickers_json,
            company_names_json, industries_json, themes_json, content_hash
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "\u751f\u732a\u884c\u4e1a\u5468\u62a5",
            "\u4ed4\u732a\u4ef7\u683c\u548c\u80fd\u7e41\u6bcd\u732a\u5b58\u680f\u66f4\u65b0",
            "\u884c\u4e1a\u66f4\u65b0",
            "industry_weekly_data",
            "2026-06-20 10:00",
            "2026-06-20 10:00",
            "knowledge_planet",
            "daily.md",
            "",
            "tester",
            json.dumps([], ensure_ascii=False),
            json.dumps([], ensure_ascii=False),
            json.dumps(["\u751f\u732a"], ensure_ascii=False),
            json.dumps([], ensure_ascii=False),
            "broad",
        ),
    )
    conn.execute(
        """
        INSERT INTO kp_items (
            title, text, summary, source_type, published_at, imported_at,
            source_platform, source_file, credibility, author, tickers_json,
            company_names_json, industries_json, themes_json, content_hash
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "\u7267\u539f\u80a1\u4efd\u8c03\u7814\u53cd\u9988",
            "\u7267\u539f\u5b8c\u5168\u6210\u672c\u548c\u51fa\u680f\u8282\u594f\u66f4\u65b0",
            "\u7267\u539f\u66f4\u65b0",
            "company_research_feedback",
            "2026-06-18 10:00",
            "2026-06-18 10:00",
            "knowledge_planet",
            "daily.md",
            "",
            "tester",
            json.dumps(["002714.SZ"], ensure_ascii=False),
            json.dumps(["\u7267\u539f\u80a1\u4efd"], ensure_ascii=False),
            json.dumps(["\u751f\u732a"], ensure_ascii=False),
            json.dumps([], ensure_ascii=False),
            "company",
        ),
    )
    conn.commit()

    rows = kp._query_items(
        conn,
        terms=["\u7267\u539f", "\u751f\u732a", "\u4ed4\u732a"],
        primary_terms=["\u7267\u539f"],
        start_date="2026-06-17",
        end_date="2026-06-20",
        limit=2,
    )
    conn.close()

    assert rows[0].title == "\u7267\u539f\u80a1\u4efd\u8c03\u7814\u53cd\u9988"
