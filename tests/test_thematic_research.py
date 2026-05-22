import pandas as pd

from tradingagents.dataflows.thematic_research import (
    ThemeCandidate,
    _FINANCIAL_REPORT_TEXT_CACHE,
    _build_interaction_option_rows,
    _build_cross_source_validation_rows,
    _build_valuation_rows,
    _build_narrative_option_rows,
    _build_concept_membership_rows,
    _catalyst_tier,
    _candidate_in_reports,
    _combine_news_frames,
    _extract_financial_candidates,
    _extract_news_candidates,
    _extract_reliable_filing_theme_candidates,
    _extract_reported_amount_cny,
    _filter_news_by_entity_terms,
    _news_has_catalyst,
    _portfolio_pattern_summary,
    _load_financial_report_texts,
    _extract_short_investee_name,
    _is_valid_asset_revaluation_candidate,
)


def test_financial_report_extracts_investee_and_business_theme():
    reports = [
        (
            "2025年半年度报告",
            """
            公司持有蓝箭航天空间科技股份有限公司非上市权益工具投资。
            公司已开展算力租赁业务，并推进智算中心建设。
            """,
        )
    ]

    candidates = _extract_financial_candidates(reports)
    names = {(candidate.name, candidate.kind) for candidate in candidates}

    assert ("蓝箭航天空间科技股份有限公司", "asset-revaluation") in names
    assert ("算力租赁", "business-realization") in names


def test_financial_report_extracts_short_investee_rows_inside_investment_section():
    reports = [
        (
            "2025年年度报告",
            """
            17、其他非流动金融资产
            项目 期末余额 期初余额
            蓝箭航天 811,952,039.53 150,662,280.21
            合计 811,952,039.53 150,662,280.21
            """,
        )
    ]

    candidates = _extract_financial_candidates(reports)
    names = {(candidate.name, candidate.kind) for candidate in candidates}

    assert ("蓝箭航天", "asset-revaluation") in names


def test_bank_balance_sheet_rows_are_not_asset_revaluation_candidates():
    assert not _is_valid_asset_revaluation_candidate("金融投资", "金融投资 (2,889) (2,400)")
    assert not _is_valid_asset_revaluation_candidate("债券投资及票据贴现", "债券投资及票据贴现 107,179 167,930")



def test_short_investee_extractor_rejects_accounting_rows_and_keeps_real_investee():
    noisy_rows = [
        "\u77ed\u671f\u501f\u6b3e 10,000,000.00",
        "\u957f\u671f\u501f\u6b3e 20,000,000.00",
        "\u5ba2\u6237\u4e00 30,000,000.00",
        "\u5408\u8ba1 40,000,000.00",
        "\u5883\u5185\u81ea\u7136\u4eba\u6301\u80a1 50,000,000.00",
        "\u6295\u8d44\u6027\u623f\u5730\u4ea7 60,000,000.00",
    ]

    assert all(_extract_short_investee_name(row) is None for row in noisy_rows)
    assert _extract_short_investee_name("\u84dd\u7bad\u822a\u5929 811,952,039.53 150,662,280.21") == "\u84dd\u7bad\u822a\u5929"

def test_news_candidate_requires_filing_validation():
    news = pd.DataFrame(
        [
            {
                "title": "公司商业航天题材升温",
                "content": "市场关注蓝箭航天空间科技股份有限公司IPO进展。",
            }
        ]
    )
    reports = [
        (
            "2025年半年度报告",
            "公司持有蓝箭航天空间科技股份有限公司非上市权益工具投资。",
        )
    ]

    candidates = _extract_news_candidates(news)
    investee = next(candidate for candidate in candidates if "蓝箭航天" in candidate.name)

    assert _candidate_in_reports(investee, reports) is True


def test_news_only_theme_is_not_validated_without_report_support():
    candidate = ThemeCandidate(
        name="机器人",
        kind="business-realization",
        origin="news",
        evidence="市场传闻公司布局机器人。",
    )
    reports = [("2025年半年度报告", "公司主营业务为风电设备。")]

    assert _candidate_in_reports(candidate, reports) is False


def test_news_catalyst_keyword_detection():
    assert _news_has_catalyst(["蓝箭航天IPO受理"])
    assert not _news_has_catalyst(["市场讨论商业航天概念"])


def test_combine_news_frames_deduplicates_company_and_investee_news():
    company_news = pd.DataFrame(
        [{"title": "金风科技持有蓝箭航天", "content": "蓝箭航天IPO推进"}]
    )
    investee_news = pd.DataFrame(
        [
            {"title": "金风科技持有蓝箭航天", "content": "蓝箭航天IPO推进"},
            {"title": "蓝箭航天IPO辅导", "content": "蓝箭航天IPO推进"},
        ]
    )

    result = _combine_news_frames(company_news, investee_news)

    assert list(result["title"]) == ["金风科技持有蓝箭航天", "蓝箭航天IPO辅导"]


def test_filter_news_by_entity_terms_drops_unrelated_articles_before_theme_extraction():
    news = pd.DataFrame(
        [
            {"title": "牧原股份推进降本", "content": "牧原股份披露完全成本改善。"},
            {"title": "某新能源公司签约", "content": "商业航天与储能概念升温。"},
        ]
    )

    result = _filter_news_by_entity_terms(news, ["牧原股份", "002714"])

    assert list(result["title"]) == ["牧原股份推进降本"]


def test_reported_amount_parser_accepts_raw_cny_table_values():
    text = "公司持有蓝箭航天空间科技股份有限公司非上市权益工具投资 811,952,039.53"

    assert _extract_reported_amount_cny(text) == 811_952_039.53


def test_valuation_bridge_separates_asset_revaluation_from_unquantified_business_theme():
    financial_candidates = [
        ThemeCandidate(
            name="蓝箭航天空间科技股份有限公司",
            kind="asset-revaluation",
            origin="financial report",
            evidence="2025年半年度报告: 公司持有蓝箭航天空间科技股份有限公司非上市权益工具投资 811,952,039.53",
        ),
        ThemeCandidate(
            name="算力租赁",
            kind="business-realization",
            origin="financial report",
            evidence="2025年年度报告: 公司已开展算力租赁业务，并推进智算中心建设。",
        ),
    ]
    news = pd.DataFrame(
        [
            {
                "title": "蓝箭航天IPO受理",
                "content": "蓝箭航天空间科技股份有限公司IPO受理。",
            }
        ]
    )

    rows = _build_valuation_rows(
        financial_candidates=financial_candidates,
        news_candidates=[],
        report_texts=[],
        major_news=news,
        news_feed=pd.DataFrame(),
        market_cap_cny=10_000_000_000,
    )
    rows_by_name = {row["candidate"]: row for row in rows}

    assert rows_by_name["蓝箭航天空间科技股份有限公司"]["vs_listed_mkt_cap"] == "8.1%"
    assert rows_by_name["蓝箭航天空间科技股份有限公司"]["valuation_treatment"] == "eligible for SOTP/NAV review"
    assert rows_by_name["算力租赁"]["valuation_treatment"] == "real theme, not yet separately quantifiable"


def test_portfolio_pattern_summary_detects_repeat_investing_skill_signal():
    financial_candidates = [
        ThemeCandidate(
            name="Investee A",
            kind="asset-revaluation",
            origin="financial report",
            evidence="annual report: Investee A 100,000,000",
        ),
        ThemeCandidate(
            name="Investee B",
            kind="asset-revaluation",
            origin="financial report",
            evidence="annual report: Investee B 200,000,000",
        ),
    ]
    reports = [
        (
            "2025 annual report",
            "\u516c\u53f8\u786e\u8ba4\u6295\u8d44\u6536\u76ca\uff0c\u5e76\u5904\u7f6e\u957f\u671f\u80a1\u6743\u6295\u8d44\u3002",
        )
    ]

    result = _portfolio_pattern_summary(financial_candidates, reports)

    assert result["verified_investee_count"] == "2"
    assert result["realized_investment_signal"] == "yes"
    assert result["pattern_read"].startswith("repeat-investor pattern worth explicit review")


def test_reliable_filing_theme_requires_monetization_evidence():
    reports = [
        (
            "2025 annual report",
            "\u516c\u53f8\u6d77\u5916\u5e02\u573a\u65b0\u589e\u8ba2\u5355 123,000,000 \u5143\uff0c"
            "\u5df2\u5b9e\u73b0\u4ea4\u4ed8\u3002",
        ),
        (
            "2025 annual report",
            "\u516c\u53f8\u5173\u6ce8\u65b0\u4ea7\u54c1\u673a\u4f1a\uff0c\u5c1a\u672a\u5f62\u6210\u6536\u5165\u3002",
        ),
    ]

    result = _extract_reliable_filing_theme_candidates(reports)
    names = {candidate.name for candidate in result}

    assert "overseas-expansion" in names
    assert "order-ramp" in names
    assert "new-product-commercialization" not in names


def test_financial_report_text_loader_reuses_same_run_bundle(monkeypatch, tmp_path):
    _FINANCIAL_REPORT_TEXT_CACHE.clear()
    calls = {"announcements": 0, "download": 0, "extract": 0}
    reports = pd.DataFrame(
        [
            {
                "ann_date": "20260328",
                "title": "2025 annual report",
                "url": "https://example.com/report.pdf",
            }
        ]
    )
    pdf_path = tmp_path / "report.pdf"
    pdf_path.write_bytes(b"%PDF-1.4")

    def fake_announcements(symbol, curr_date, look_back_days):
        calls["announcements"] += 1
        return reports

    def fake_download(url):
        calls["download"] += 1
        return pdf_path

    def fake_extract(path):
        calls["extract"] += 1
        return "company disclosed signed customer orders"

    monkeypatch.setattr(
        "tradingagents.dataflows.thematic_research._financial_report_announcements",
        fake_announcements,
    )
    monkeypatch.setattr(
        "tradingagents.dataflows.thematic_research._download_disclosure",
        fake_download,
    )
    monkeypatch.setattr(
        "tradingagents.dataflows.thematic_research._extract_pdf_text",
        fake_extract,
    )

    first_reports, first_texts = _load_financial_report_texts("002202.SZ", "2026-05-17")
    second_reports, second_texts = _load_financial_report_texts("002202.SZ", "2026-05-17")

    assert calls == {"announcements": 1, "download": 1, "extract": 1}
    assert first_texts == second_texts == [
        ("2025 annual report", "company disclosed signed customer orders")
    ]
    assert first_reports.equals(second_reports)


def test_short_investee_extractor_rejects_accounting_rows():
    assert _extract_short_investee_name("\u53d6\u5f97\u6295\u8d44\u6536\u76ca\u6536\u5230\u7684\u73b0\u91d1 120,229,758.21") is None
    assert _extract_short_investee_name("\u5176\u4ed6\u6743\u76ca\u5de5\u5177\u6295\u8d44 216,474,907.00") is None


def test_catalyst_tier_distinguishes_hard_and_soft_verified_themes():
    asset = ThemeCandidate(
        name="Investee A",
        kind="asset-revaluation",
        origin="financial report",
        evidence="Investee A 200,000,000",
    )
    business = ThemeCandidate(
        name="order-ramp",
        kind="business-realization",
        origin="financial report",
        evidence="新增订单 123,000,000 元，实现营业收入",
    )

    assert _catalyst_tier(asset, 200_000_000, 10_000_000_000, True)[0] == "tier-1 hard catalyst"
    assert _catalyst_tier(asset, 200_000_000, 10_000_000_000, False)[0] == "tier-2 soft catalyst"
    assert _catalyst_tier(business, None, 10_000_000_000, False)[0] == "tier-1 hard catalyst"


def test_news_only_theme_becomes_low_weight_narrative_option():
    news_candidate = ThemeCandidate(
        name="commercial-space",
        kind="business-realization",
        origin="news",
        evidence="媒体联想公司具备商业航天概念",
    )

    rows = _build_narrative_option_rows(
        [news_candidate],
        report_texts=[],
        major_news=pd.DataFrame([{"title": "商业航天概念", "content": "媒体联想公司具备商业航天概念"}]),
        news_feed=pd.DataFrame(),
    )

    assert rows[0]["catalyst_tier"] == "tier-3 narrative option"
    assert rows[0]["valuation_weight"] == "small imagination premium only"


def test_concept_membership_becomes_low_weight_narrative_option():
    concept_memberships = pd.DataFrame(
        [
            {
                "id": "TS001",
                "concept_name": "商业航天",
                "ts_code": "002202.SZ",
                "name": "金风科技",
                "in_date": "20240101",
                "out_date": "",
            }
        ]
    )

    rows = _build_concept_membership_rows(concept_memberships)

    assert rows[0]["candidate"] == "商业航天"
    assert rows[0]["kind"] == "concept-membership"
    assert rows[0]["catalyst_tier"] == "tier-3 narrative option"
def test_interaction_answer_becomes_low_weight_narrative_option():
    interactions = pd.DataFrame(
        [
            {
                "question": "公司是否推进 AI 气象合作？",
                "answer": "您好，公司已经开始推动战略合作的落地实施，感谢您的关注。",
                "answer_class": "directional-but-unquantified",
                "source_type": "cninfo_irm",
            },
            {
                "question": "请问股东人数？",
                "answer": None,
                "answer_class": "unanswered",
                "source_type": "cninfo_irm",
            },
        ]
    )

    rows = _build_interaction_option_rows(interactions)

    assert len(rows) == 1
    assert rows[0]["kind"] == "investor-interaction"
    assert rows[0]["catalyst_tier"] == "tier-3 narrative option"
    assert rows[0]["valuation_weight"] == "small imagination premium only"


def test_non_committal_compute_leasing_question_stays_as_diligence_gap():
    interactions = pd.DataFrame(
        [
            {
                "question": (
                    "\u516c\u53f8\u662f\u5426\u5728\u5f00\u5c55"
                    "\u7b97\u529b\u79df\u8d41\u4e1a\u52a1\uff1f"
                ),
                "answer": (
                    "\u516c\u53f8\u7ecf\u8425\u60c5\u51b5\u8be6\u89c1\u516c\u53f8"
                    "\u6307\u5b9a\u4fe1\u606f\u62ab\u9732\u5a92\u4f53\u3002"
                ),
                "answer_class": "non-committal",
                "theme": "compute-power",
                "source_type": "cninfo_irm",
                "story_read": "new-demand adjacency around power + computing infrastructure",
                "proof_needed": "needs revenue, order, or project economics before valuation uplift",
                "credibility": "weak-official-signal",
            }
        ]
    )

    rows = _build_interaction_option_rows(interactions)

    assert rows[0]["candidate"] == "\u7b97\u529b\u79df\u8d41/\u667a\u4e91\u8ba1\u7b97"
    assert rows[0]["valuation_weight"].startswith("no valuation credit")
    assert "\u7b97\u529b\u79df\u8d41" in rows[0]["evidence"]


def test_cross_source_validation_separates_pending_hard_from_correlated_narrative():
    filing = [
        ThemeCandidate(
            name="order-ramp",
            kind="business-realization",
            origin="financial report",
            evidence="新增订单 123,000,000 元",
        )
    ]
    news = [
        ThemeCandidate(
            name="commercial-space",
            kind="business-realization",
            origin="news",
            evidence="媒体联想商业航天",
        )
    ]
    concepts = pd.DataFrame([{"concept_name": "航天军工"}])
    interactions = pd.DataFrame(
        [
            {
                "theme": "commercial-space",
                "answer_class": "directional-but-unquantified",
            }
        ]
    )

    rows = _build_cross_source_validation_rows(filing, news, concepts, interactions)
    by_theme = {row["theme"]: row for row in rows}

    assert by_theme["order-ramp"]["suggested_tier"] == "tier-1 pending diligence"
    assert by_theme["commercial-space"]["suggested_tier"] == "tier-2 corroborated narrative"
