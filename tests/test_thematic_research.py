import pandas as pd

from tradingagents.dataflows.thematic_research import (
    ThemeCandidate,
    _build_valuation_rows,
    _candidate_in_reports,
    _combine_news_frames,
    _extract_financial_candidates,
    _extract_news_candidates,
    _extract_reported_amount_cny,
    _news_has_catalyst,
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
