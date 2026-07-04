import json
import hashlib
import sqlite3
from pathlib import Path
from types import SimpleNamespace

from tradingagents.default_config import DEFAULT_CONFIG
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
    monkeypatch.setattr(kp, "_text_only_enabled", lambda: False)
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
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

    context = kp.get_knowledge_planet_context("300750.SZ", "2026-06-19", look_back_days=6)

    assert "Matched stream items: 1" in context
    assert "Matched PDF reports: 1" in context
    assert "channel_check" in context
    assert "high_private_channel_hard_to_verify" in context


def test_single_stock_pdf_recall_filters_sector_only_reports(tmp_path, monkeypatch):
    monkeypatch.setattr(kp, "_text_only_enabled", lambda: False)
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    for idx, title in enumerate(
        [
            "Eastroc Beverage 605499.SH functional beverage channel report",
            "General beverage sector weekly without target company",
        ],
        start=1,
    ):
        conn.execute(
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
                f"report-hash-{idx}",
                "knowledge_planet",
                f"report-{idx}.pdf",
                f"data/knowledge_planet/reports/processed/report-{idx}.pdf",
                f"data/knowledge_planet/reports/extracted/report-{idx}.txt",
                f"data/knowledge_planet/reports/extracted/report-{idx}.json",
                f"report-{idx}.pdf",
                "ok",
                title,
                "GS",
                "GS",
                "2026-06-19",
                "2026-06-19T11:00:00",
                json.dumps(["605499.SH"] if idx == 1 else [], ensure_ascii=False),
                json.dumps(["Eastroc Beverage"] if idx == 1 else [], ensure_ascii=False),
                json.dumps(["beverage"], ensure_ascii=False),
                json.dumps(["consumer"], ensure_ascii=False),
                "functional beverage research",
            ),
        )
    conn.commit()

    rows = kp._query_reports(
        conn,
        terms=["Eastroc Beverage", "605499.SH", "beverage"],
        primary_terms=["Eastroc Beverage", "605499.SH"],
        start_date="2026-06-18",
        end_date="2026-06-20",
        limit=10,
    )
    conn.close()

    assert [row.title for row in rows] == [
        "Eastroc Beverage 605499.SH functional beverage channel report"
    ]


def test_single_stock_stream_recall_filters_sector_only_items(tmp_path):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    _insert_item(
        conn,
        "Eastroc Beverage 605499.SH channel note",
        "Company-specific distributor feedback shows energy drink sell-through improved.",
        source_type="channel_check",
        ticker="605499.SH",
    )
    _insert_item(
        conn,
        "General beverage weekly",
        "Beverage sector inventory and promotions are being discussed, without target company detail.",
        source_type="industry_weekly_data",
        ticker="",
    )
    conn.commit()

    rows = kp._query_items(
        conn,
        terms=["Eastroc Beverage", "605499.SH", "beverage"],
        primary_terms=["Eastroc Beverage", "605499.SH"],
        start_date="2026-06-18",
        end_date="2026-06-20",
        limit=10,
    )
    conn.close()

    assert [row.title for row in rows] == [
        "Eastroc Beverage 605499.SH channel note"
    ]


def test_single_stock_context_includes_private_proxy_evidence_ledger(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    _insert_item(
        conn,
        "Eastroc Beverage 605499.SH channel note",
        "Company-specific channel check says sell-through improved and inventory was lower.",
        source_type="channel_check",
        ticker="605499.SH",
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)

    context = kp.get_knowledge_planet_context("605499.SH", "2026-06-19")

    assert "### Private / Proxy Evidence Ledger" in context
    assert "KPE01" in context
    assert "probability/verification proxy" in context
    assert "## PM Knowledge Planet Clue Verdict" in context


def test_hog_context_extracts_private_proxy_kpis(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    _insert_item(
        conn,
        "hog breeder 002714.SZ industry weekly",
        "Hog price improved, piglet price rose, sow inventory declined, complete cost was lower.",
        source_type="industry_weekly_data",
        ticker="002714.SZ",
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)
    monkeypatch.setattr(kp, "is_hog_breeding_text", lambda *_args: True)

    context = kp.get_knowledge_planet_context("hog breeder 002714.SZ", "2026-06-19")

    assert "### Hog KPI Extraction" in context
    assert "| hog ASP / live-hog price | private_proxy |" in context
    assert "| piglet price | private_proxy |" in context
    assert "| sow inventory / sow price | private_proxy |" in context
    assert "| complete breeding cost | private_proxy |" in context


def test_preprocess_extracts_pdf_report_structures(tmp_path, monkeypatch):
    monkeypatch.setattr(kp, "_text_only_enabled", lambda: False)
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    text_path = tmp_path / "catl_report.txt"
    text_path.write_text(
        "\n".join(
            [
                "Core assumption: battery orders recover and utilization rises.",
                "Revenue forecast: 2026 revenue 120 billion yuan and net profit 15 billion yuan.",
                "Valuation: apply 25x PE and target price 120 yuan.",
                "Rating: upgrade to Buy from Neutral.",
                "Figure 3: utilization reaches 85% and gross margin improves 3pct.",
            ]
        ),
        encoding="utf-8",
    )
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    _insert_report(conn)
    conn.execute(
        """
        UPDATE kp_reports
        SET title = ?, summary = ?, extracted_text_path = ?
        WHERE id = 1
        """,
        (
            "CATL 300750.SZ earnings forecast and target price",
            "CATL revenue forecast valuation target price rating",
            str(text_path),
        ),
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)

    stats = kp.preprocess_knowledge_planet_window("2026-06-19", 6)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT category, extracted_value, model_check FROM kp_report_structures ORDER BY category"
    ).fetchall()
    conn.close()
    categories = {row["category"] for row in rows}

    assert stats.report_assumptions == 1
    assert "core_assumption" in categories
    assert "earnings_forecast" in categories
    assert "valuation_method" in categories
    assert "rating_target_change" in categories
    assert "key_chart_number" in categories
    assert "model_conflict_check" in categories
    assert any("TradingAgents earnings model" in row["model_check"] for row in rows)

    context = kp.get_knowledge_planet_context("300750.SZ", "2026-06-19", look_back_days=6)

    assert "### PDF Report Structured Thesis Map" in context
    assert "earnings_forecast" in context
    assert "valuation_method" in context
    assert "model_conflict_check" in context


def test_preprocess_can_llm_enrich_pdf_report_structures(tmp_path, monkeypatch):
    monkeypatch.setattr(kp, "_text_only_enabled", lambda: False)
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    text_path = tmp_path / "sellside_report.txt"
    text_path.write_text(
        "Revenue forecast: 2026 revenue 120 billion yuan. Valuation: 25x PE target price 120 yuan.",
        encoding="utf-8",
    )
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    _insert_report(conn)
    conn.execute(
        "UPDATE kp_reports SET title = ?, summary = ?, extracted_text_path = ? WHERE id = 1",
        (
            "CATL 300750.SZ model conflict report",
            "CATL revenue forecast valuation target price",
            str(text_path),
        ),
    )
    conn.commit()
    conn.close()

    class DummyLLM:
        def invoke(self, _messages):
            return SimpleNamespace(
                content=json.dumps(
                    {
                        "structures": [
                            {
                                "category": "research_value",
                                "extracted_value": "Sell-side assumes battery recovery drives 2026 revenue.",
                                "evidence": "2026 revenue 120 billion yuan",
                                "model_check": "Compare with TradingAgents revenue bridge and utilization assumptions.",
                                "status": "llm_enriched",
                            },
                            {
                                "category": "model_conflict_check",
                                "extracted_value": "25x PE and 120 yuan target may exceed our valuation bridge.",
                                "evidence": "25x PE target price 120 yuan",
                                "model_check": "Rebuild target-price math and downside support before using rating.",
                                "status": "llm_enriched",
                            },
                        ]
                    },
                    ensure_ascii=False,
                )
            )

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)
    monkeypatch.setattr(
        kp,
        "_create_market_analysis_llm",
        lambda *_args, **_kwargs: DummyLLM(),
    )

    kp.preprocess_knowledge_planet_window(
        "2026-06-19",
        6,
        include_llm_report_analysis=True,
        max_llm_reports=1,
    )

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT category, status, extracted_value FROM kp_report_structures WHERE status = 'llm_enriched'"
    ).fetchall()
    conn.close()

    assert {row["category"] for row in rows} >= {"research_value", "model_conflict_check"}
    assert any("Sell-side assumes" in row["extracted_value"] for row in rows)

    context = kp.get_knowledge_planet_context("300750.SZ", "2026-06-19", look_back_days=6)

    assert "llm_enriched" in context
    assert "research_value" in context


def test_single_stock_knowledge_defaults_use_lightweight_sync():
    assert DEFAULT_CONFIG["knowledge_planet_text_only"] is True
    assert DEFAULT_CONFIG["knowledge_planet_auto_sync_context_lookback_days"] == 30
    assert DEFAULT_CONFIG["knowledge_planet_context_sync_max_pages"] == 20
    assert DEFAULT_CONFIG["knowledge_planet_context_sync_max_image_downloads"] == 0
    assert DEFAULT_CONFIG["knowledge_planet_context_sync_max_file_downloads"] == 0


def test_preprocess_cache_check_returns_before_loading_details(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    kp._init_preprocess_tables(conn)
    conn.execute(
        """
        INSERT INTO kp_preprocess_runs (
            run_key, start_date, end_date, schema_version, items_scanned,
            reports_scanned, quality_rows, content_units, events, clusters,
            mappings, report_assumptions, opportunities, ocr_low_quality,
            pdf_pending_or_limited, status, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
                "2026-06-14:2026-06-20:v4:text:"
                + hashlib.sha1("0|".encode("utf-8")).hexdigest()[:12],
            "2026-06-14",
            "2026-06-20",
                4,
            0,
            0,
            0,
            0,
            3,
            1,
            0,
            0,
            0,
            0,
            0,
            "ok",
            "2026-06-20T10:00:00",
        ),
    )
    conn.commit()
    conn.close()

    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)

    stats = kp.preprocess_knowledge_planet_window("2026-06-20", 6)

    assert stats.status == "cached"
    assert stats.events == 3
    assert stats.clusters == 1


def test_daily_report_flags_information_and_pump_risk(tmp_path, monkeypatch):
    monkeypatch.setattr(kp, "_text_only_enabled", lambda: False)
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
    assert "今日主榜与观察榜" in report
    assert "主榜 10" in report
    assert "观察榜 5" in report
    assert "排序得分" in report
    assert "漏斗评分解释" in report
    assert "候选证据摘要" in report
    assert "题材热度边际变化" in report
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


def test_llm_market_analysis_retries_with_short_evidence():
    class FlakyLLM:
        def __init__(self):
            self.calls = 0

        def invoke(self, _messages):
            self.calls += 1
            if self.calls == 1:
                raise RuntimeError("connection reset")
            return SimpleNamespace(
                content=json.dumps(
                    {
                        "logic_score": 72,
                        "information_quality": "中",
                        "signal_interpretation": "订单类增量",
                        "thesis_path": "订单改善->收入修复->估值修复",
                        "trading_action": "观察，等订单验证",
                        "summary": "短证据重试后完成分析",
                    },
                    ensure_ascii=False,
                )
            )

    analysis = kp._run_llm_market_analysis(
        "宁德时代",
        {"score": 80, "pump": 10, "items": []},
        None,
        FlakyLLM(),
    )

    assert analysis.status == "analyzed"
    assert analysis.logic_score == 72
    assert "短证据重试成功" in analysis.summary


def test_board_keeps_failed_llm_candidates_out_of_main_board():
    analyzed = {
        "name": "通过票",
        "symbol": "300750.SZ",
        "llm_status": "analyzed",
        "llm_required": True,
        "market_scores_required": True,
        "llm_score": 78,
        "signal_score": 80,
        "fundamental_text": "部分验证 28/40",
        "technical": 24,
        "action": "观察，等回踩确认",
        "thesis_path": "排产改善->收入修复->估值修复",
        "raw_evidence": ["2026-06-19 10:33｜渠道反馈｜排产改善，订单上修。"],
        "hard_increment_count": 1,
        "pump": 5,
        "tradability_score": 62,
        "scorecard": {
            "total": 62,
            "components": {"逻辑": 12, "预期差": 15, "基本面": 18, "技术": 9, "催化": 12},
            "risk_penalty": 4,
            "hard_reject": False,
            "hard_reject_reasons": [],
            "trade_type": "低位拐点反转",
        },
    }
    failed = {
        **analyzed,
        "name": "失败票",
        "symbol": "000001.SZ",
        "llm_status": "failed",
        "llm_score": None,
        "action": "LLM分析失败",
        "tradability_score": 95,
        "scorecard": {
            **analyzed["scorecard"],
            "total": 95,
            "hard_reject": True,
            "hard_reject_reasons": ["LLM未完成深度拆解"],
        },
    }

    report = "\n".join(kp._board_candidate_lines([failed, analyzed]))
    before_pending = report.split("### 待补分析池", 1)[0]

    assert "通过票（300750.SZ）" in before_pending
    assert "失败票（000001.SZ）" not in before_pending
    assert "### 待补分析池" in report
    assert "失败票（000001.SZ）" in report


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

    def fake_sync(start_date, end_date, stamp_dates, **_kwargs):
        calls.append((start_date, end_date, stamp_dates))
        return "synced_window"

    monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)
    monkeypatch.setattr(kp, "_enabled", lambda: True)
    monkeypatch.setattr(kp, "_auto_sync_enabled", lambda: True)
    monkeypatch.setattr(kp, "_sync_skip_status", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(kp, "_sync_knowledge_planet_range", fake_sync)

    status = kp.ensure_knowledge_planet_upstream_synced_for_window(
        "2026-06-19",
        2,
        import_local=False,
    )

    assert calls == [
        ("2026-06-17", "2026-06-19", ["2026-06-17", "2026-06-18", "2026-06-19"])
    ]
    assert "2026-06-17=synced_window" in status
    assert "2026-06-19=synced_window" in status


def test_text_only_import_uses_stream_mode(monkeypatch):
    calls = []
    monkeypatch.setattr(kp, "_text_only_enabled", lambda: True)
    monkeypatch.setattr(
        kp,
        "_run_project_script",
        lambda args, **kwargs: (calls.append((args, kwargs)) or (0, "ok")),
    )

    status = kp._import_knowledge_planet_local_index()

    assert status.startswith("local_import_ok")
    assert "--stream" in calls[0][0]
    assert "--backfill-report-text" not in calls[0][0]


def test_text_only_sync_disables_all_attachment_work(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(kp, "_text_only_enabled", lambda: True)
    monkeypatch.setattr(kp, "_sync_state_dir", lambda: tmp_path)
    monkeypatch.setattr(
        kp,
        "_run_project_script",
        lambda args, **kwargs: (calls.append(args) or (0, "wrote 1 topic(s)")),
    )

    status = kp._sync_knowledge_planet_range(
        "2026-06-19",
        "2026-06-19",
        ["2026-06-19"],
        progress=None,
        max_pages=20,
        max_image_downloads=100,
        max_file_downloads=50,
    )

    assert status.startswith("synced_window")
    assert "--no-download-images" in calls[0]
    assert "--no-ocr-images" in calls[0]
    assert "--no-download-files" in calls[0]


def test_context_sync_imports_before_reading(tmp_path, monkeypatch):
    db_path = tmp_path / "kp.sqlite"
    _make_db(db_path)
    calls = []
    monkeypatch.setattr(kp, "DEFAULT_KP_DB", db_path)
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)
    monkeypatch.setattr(
        kp,
        "ensure_knowledge_planet_upstream_synced_for_window",
        lambda *_args, **kwargs: (calls.append(kwargs) or "synced"),
    )

    kp.get_knowledge_planet_context("300750.SZ", "2026-06-19", look_back_days=0)

    assert calls[0]["import_local"] is True


def test_stock_terms_include_common_aliases_without_tushare(monkeypatch):
    monkeypatch.setattr(kp, "_fetch_stock_basic", None)

    terms = kp._stock_terms("601318.SH")

    assert "601318.SH" in terms
    assert "601318" in terms
    assert "中国平安" in terms
