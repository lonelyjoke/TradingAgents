import pandas as pd

from tradingagents.dataflows.policy_research import (
    PolicySource,
    _clean_policy_html,
    _infer_policy_relevance,
    _policy_source_frame,
    _select_industry_policy_sources,
)


def test_clean_policy_html_removes_markup_and_preserves_text():
    html = """
    <html><head><style>.x{}</style><script>alert(1)</script></head>
    <body><h1>风电</h1><p>建设新型能源体系</p></body></html>
    """

    assert _clean_policy_html(html) == "风电 建设新型能源体系"


def test_select_industry_policy_sources_routes_by_company_terms():
    sources = _select_industry_policy_sources(["金风科技", "电气设备"])

    assert any(source.title == "“十四五”可再生能源发展规划" for source in sources)


def test_policy_source_frame_renders_selected_sources():
    sources = (
        PolicySource(
            title="示例文件",
            issuer="示例部门",
            publish_date="2026-01-01",
            policy_level="industry-plan",
            url="https://example.com/policy",
        ),
    )

    result = _policy_source_frame(sources)

    assert list(result.columns) == [
        "title",
        "issuer",
        "publish_date",
        "policy_level",
        "url",
    ]
    assert result.iloc[0]["title"] == "示例文件"


def test_infer_policy_relevance_detects_multiple_policy_themes():
    docs = pd.DataFrame(
        [
            {
                "title": "示例规划",
                "issuer": "示例部门",
                "publish_date": "2026-01-01",
                "policy_level": "industry-plan",
                "text": "加快风电发展，建设新型能源体系，支持商业航天和人工智能。",
            }
        ]
    )

    result = _infer_policy_relevance(docs, ["金风科技"])

    assert set(result["policy_theme"]) >= {
        "renewable-energy",
        "commercial-space",
        "ai-and-digital",
    }
