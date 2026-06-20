import json
import sqlite3
from pathlib import Path
from types import SimpleNamespace

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
    published_at: str = "2026-06-19 10:33",
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
            published_at,
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

    assert "候选标的综合排序" in report
    assert "PM总控层：最终取舍" in report
    assert "今日真增量到交易映射" in report
    assert "建仓价值候选 Top 5" in report
    assert "评分拆解" in report
    assert "高位与低位挖掘" in report
    assert "研究流水线状态" in report
    assert "宁德时代" in report
    assert "高价值产业/调研线索" in report
    assert "卖方推票 / 吹票风险观察" in report
    assert "飞天科技" in report


def test_daily_report_includes_iso_zsxq_timestamps(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    _insert_item(
        conn,
        "ISO timestamp item",
        "This item uses the native zsxq timestamp format.",
        published_at="2026-06-17T23:33:57.028+0800",
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)

    report = kp.build_knowledge_planet_daily_report("2026-06-17")

    assert "ISO timestamp item" in report


def test_daily_report_can_include_mocked_fundamental_and_technical_scores(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    _insert_item(
        conn,
        "【宁德时代】渠道反馈",
        "渠道反馈显示客户订单改善，排产上修，但仍需后续验证。",
        source_type="channel_check",
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(
        kp,
        "_score_candidate_market",
        lambda name, date: kp.CandidateMarketScore(
            candidate=name,
            symbol="300750.SZ",
            company_name="宁德时代",
            industry="电池",
            fundamental_score=28,
            technical_score=21,
            total_market_score=49,
            summary="基本面: ROE 18.0%，PE(TTM) 25.0；技术面: 20日 8.0%",
            status="scored",
        ),
    )

    report = kp.build_knowledge_planet_daily_report(
        "2026-06-19",
        include_market_scores=True,
        max_scored_candidates=3,
    )

    assert "300750.SZ" in report
    assert "| 1 | 宁德时代（300750.SZ）" in report
    assert "基本面验证" in report
    assert "部分验证 28/40" in report
    assert "28" in report
    assert "21" in report
    assert "基本面: ROE" in report


def test_daily_report_can_include_mocked_llm_market_analysis(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    _insert_item(
        conn,
        "【宁德时代】渠道反馈",
        "渠道反馈显示客户订单改善，排产上修，但仍需后续验证。",
        source_type="channel_check",
    )
    conn.commit()
    conn.close()

    class DummyLLM:
        def invoke(self, _messages):
            return SimpleNamespace(
                content=json.dumps(
                    {
                        "logic_score": 86,
                        "information_quality": "高",
                        "thesis_path": "新能源车需求->动力电池订单->产能利用率和盈利弹性",
                        "company_relevance": "核心受益，订单改善直接映射主业",
                        "verification_points": "排产、订单、价格",
                        "falsification_points": "排产回落或价格继续下行",
                        "trading_action": "建仓候选，等待量价确认",
                        "risk_flags": "需要警惕卖方乐观假设",
                        "summary": "逻辑链较清晰，但需要排产和价格继续验证。",
                    },
                    ensure_ascii=False,
                )
            )

    class DummyClient:
        def get_llm(self):
            return DummyLLM()

    import tradingagents.llm_clients as llm_clients

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(llm_clients, "create_llm_client", lambda **_kwargs: DummyClient())

    report = kp.build_knowledge_planet_daily_report(
        "2026-06-19",
        include_llm_market_analysis=True,
        max_llm_candidates=1,
    )

    assert "LLM 逻辑拆解：已启用" in report
    assert "LLM逻辑" in report
    assert "86" in report
    assert "建仓候选，等待量价确认" in report
    assert "新能源车需求->动力电池订单" in report


def test_candidate_target_selection_keeps_low_frequency_and_research_lanes():
    rows = [
        (
            f"tech_{idx}",
            {
                "display_name": f"科技热门{idx}",
                "mentions": 10,
                "score": 90 - idx,
                "pump": 20,
                "recency_score": 8,
                "preprocess_evidence": ["AI 算力 半导体 热门推荐"],
                "source_labels": ["候选机会资产"],
                "opportunity_types": ["热门优选"],
            },
        )
        for idx in range(10)
    ]
    rows.extend(
        [
            (
                "non_tech",
                {
                    "display_name": "山高环能",
                    "mentions": 2,
                    "score": 70,
                    "pump": 0,
                    "recency_score": 2,
                    "preprocess_evidence": ["环保 资源化 UCO 稀缺资产"],
                    "source_labels": ["候选机会资产"],
                    "opportunity_types": ["观察池"],
                },
            ),
            (
                "report",
                {
                    "display_name": "三力制药",
                    "mentions": 1,
                    "score": 66,
                    "pump": 0,
                    "recency_score": 1,
                    "preprocess_evidence": ["中药主业修复 研报假设"],
                    "source_labels": ["研报假设资产"],
                    "opportunity_types": ["研报假设待交叉验证"],
                },
            ),
            (
                "low_freq",
                {
                    "display_name": "低频周期股",
                    "mentions": 1,
                    "score": 60,
                    "pump": 0,
                    "recency_score": 1,
                    "preprocess_evidence": ["煤炭 价格 库存"],
                    "source_labels": ["候选机会资产"],
                    "opportunity_types": ["低频预期差"],
                },
            ),
        ]
    )

    selected = kp._select_candidate_targets(rows, 6)
    selected_keys = {key for key, _data in selected}

    assert "non_tech" in selected_keys
    assert "report" in selected_keys
    assert "low_freq" in selected_keys
    assert sum(1 for key in selected_keys if key.startswith("tech_")) < 6


def test_trading_graph_wires_knowledge_planet_context():
    source = Path("tradingagents/graph/trading_graph.py").read_text(encoding="utf-8")

    assert '"knowledge_planet_context"' in source
    assert '"get_knowledge_planet_context"' in source
    assert "knowledge_planet_context=knowledge_planet_context" in source


def test_window_sync_covers_each_date(monkeypatch):
    calls = []

    def fake_sync(sync_date, *, force=False, progress=None):
        calls.append(sync_date)
        return "synced"

    monkeypatch.setattr(kp, "ensure_knowledge_planet_upstream_synced", fake_sync)

    status = kp.ensure_knowledge_planet_upstream_synced_for_window("2026-06-19", 2)

    assert calls == ["2026-06-17", "2026-06-18", "2026-06-19"]
    assert "2026-06-17=synced" in status
    assert "2026-06-19=synced" in status


def test_stock_terms_include_common_aliases_without_tushare(monkeypatch):
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)

    terms = kp._stock_terms("601318.SH")

    assert "601318.SH" in terms
    assert "601318" in terms
    assert "中国平安" in terms
