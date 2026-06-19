import json
import sqlite3
from pathlib import Path

from tradingagents.dataflows import knowledge_planet_research as kp


def _make_db(path: Path) -> None:
    conn = sqlite3.connect(path)
    conn.executescript(
        """
        CREATE TABLE kp_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_hash TEXT,
            source_platform TEXT,
            source_file TEXT,
            source_type TEXT,
            credibility TEXT,
            title TEXT,
            text TEXT,
            summary TEXT,
            published_at TEXT,
            imported_at TEXT,
            author TEXT,
            tickers_json TEXT,
            company_names_json TEXT,
            industries_json TEXT,
            themes_json TEXT
        );
        CREATE TABLE kp_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_hash TEXT,
            source_platform TEXT,
            original_filename TEXT,
            stored_path TEXT,
            extracted_text_path TEXT,
            metadata_path TEXT,
            suggested_filename TEXT,
            extraction_status TEXT,
            title TEXT,
            broker TEXT,
            broker_short TEXT,
            published_at TEXT,
            imported_at TEXT,
            tickers_json TEXT,
            company_names_json TEXT,
            industries_json TEXT,
            themes_json TEXT,
            summary TEXT
        );
        CREATE TABLE kp_report_text_fts (
            report_id TEXT,
            title TEXT,
            text TEXT
        );
        """
    )
    conn.commit()
    conn.close()


def _insert_item(
    conn: sqlite3.Connection,
    title: str,
    text: str,
    *,
    source_type: str = "raw_note",
    ticker: str = "300750.SZ",
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO kp_items (
            content_hash, source_platform, source_file, source_type, credibility,
            title, text, summary, published_at, imported_at, author,
            tickers_json, company_names_json, industries_json, themes_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            title,
            "knowledge_planet",
            "daily.md",
            source_type,
            "unclassified_needs_review",
            title,
            text,
            text[:120],
            "2026-06-19 10:33",
            "2026-06-19T11:00:00",
            "tester",
            json.dumps([ticker], ensure_ascii=False),
            json.dumps(["宁德时代"], ensure_ascii=False),
            json.dumps(["锂电"], ensure_ascii=False),
            json.dumps(["AI"], ensure_ascii=False),
        ),
    )
    return int(cursor.lastrowid)


def _insert_report(conn: sqlite3.Connection) -> None:
    cursor = conn.execute(
        """
        INSERT INTO kp_reports (
            file_hash, source_platform, original_filename, stored_path,
            extracted_text_path, metadata_path, suggested_filename,
            extraction_status, title, broker, broker_short, published_at,
            imported_at, tickers_json, company_names_json, industries_json,
            themes_json, summary
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "report-hash",
            "knowledge_planet",
            "report.pdf",
            "data/knowledge_planet/reports/processed/report.pdf",
            "data/knowledge_planet/reports/extracted/report.txt",
            "data/knowledge_planet/reports/extracted/report.json",
            "20260619_gs_report.pdf",
            "ok",
            "宁德时代 锂电池 周度研究 300750.SZ",
            "高盛",
            "GS",
            "2026-06-19",
            "2026-06-19T11:00:00",
            json.dumps(["300750.SZ"], ensure_ascii=False),
            json.dumps(["宁德时代"], ensure_ascii=False),
            json.dumps(["锂电"], ensure_ascii=False),
            json.dumps(["储能"], ensure_ascii=False),
            "锂电池订单和库存研究",
        ),
    )
    conn.execute(
        "INSERT INTO kp_report_text_fts(report_id, title, text) VALUES (?, ?, ?)",
        (str(cursor.lastrowid), "report", "宁德时代 300750.SZ 电池订单、库存和价格框架"),
    )


def test_single_stock_context_retrieves_stream_and_pdf(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    _insert_item(
        conn,
        "【宁德时代】渠道反馈",
        "渠道反馈显示客户订单改善，排产上修，但仍需后续验证。",
        source_type="raw_note",
    )
    _insert_report(conn)
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)

    context = kp.get_knowledge_planet_context("300750.SZ", "2026-06-19")

    assert "Matched stream items: 1" in context
    assert "Matched PDF reports: 1" in context
    assert "channel_check" in context
    assert "high_private_channel_hard_to_verify" in context


def test_daily_report_flags_information_and_pump_risk(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    _insert_item(
        conn,
        "【宁德时代】行业周度数据",
        "周度更新：库存下降，价格改善，SMM 数据显示排产提升。",
        source_type="industry_data_snippet",
    )
    _insert_item(
        conn,
        "【飞天科技】强call",
        "重点推荐，目标市值翻倍，现价空间巨大。",
        source_type="raw_note",
        ticker="000001.SZ",
    )
    _insert_report(conn)
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)

    report = kp.build_knowledge_planet_daily_report("2026-06-19")

    assert "Candidate Ranking" in report
    assert "宁德时代" in report
    assert "High-Value Industry / Research Clues" in report
    assert "Sell-Side Push / Pump-Risk Watch" in report
    assert "飞天科技" in report


def test_trading_graph_wires_knowledge_planet_context():
    source = Path("tradingagents/graph/trading_graph.py").read_text(encoding="utf-8")

    assert '"knowledge_planet_context"' in source
    assert '"get_knowledge_planet_context"' in source
    assert "knowledge_planet_context=knowledge_planet_context" in source
