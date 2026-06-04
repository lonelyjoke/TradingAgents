from tradingagents.dataflows import web_fact_research as web_facts


def test_maotai_queries_target_wholesale_price_terms():
    queries = web_facts._fact_queries(
        "600519.SH",
        "\u8d35\u5dde\u8305\u53f0",
        "\u767d\u9152",
    )

    assert any("\u4e00\u6279\u4ef7" in query for query in queries)
    assert any("\u539f\u7bb1" in query and "\u6563\u74f6" in query for query in queries)


def test_bank_queries_use_bank_specific_fact_terms():
    queries = web_facts._fact_queries("600036.SH", "\u62db\u5546\u94f6\u884c", "\u94f6\u884c")

    joined = " ".join(queries)
    assert "\u51c0\u606f\u5dee" in joined
    assert "\u4e0d\u826f\u7387" in joined
    assert "\u8ba2\u5355" not in joined
    assert "\u6bdb\u5229\u7387" not in joined


def test_resource_queries_use_resource_specific_fact_terms():
    queries = web_facts._fact_queries("601899.SH", "\u7d2b\u91d1\u77ff\u4e1a", "\u94dc")

    joined = " ".join(queries)
    assert "\u94dc" in joined
    assert "\u9ec4\u91d1" in joined
    assert "\u77ff\u5c71 \u9879\u76ee\u8fdb\u5c55" in joined
    assert "\u767d\u9152" not in joined


def test_biopharma_fact_queries_prioritize_clinical_and_regulatory_terms():
    queries = web_facts._fact_queries(
        "688235.SH",
        "\u767e\u6d4e\u795e\u5dde",
        "\u751f\u7269\u533b\u836f",
    )

    joined = " ".join(queries)
    assert "\u4e34\u5e8a" in joined
    assert "\u7ba1\u7ebf" in joined
    assert "NMPA" in joined
    assert "FDA" in joined
    assert "\u4ea7\u54c1\u4ef7\u683c \u6e20\u9053\u5e93\u5b58" not in joined


def test_pharma_services_fact_queries_prioritize_cro_cdmo_order_risk():
    queries = web_facts._fact_queries(
        "603259.SH",
        "\u836f\u660e\u5eb7\u5fb7",
        "\u533b\u836f\u670d\u52a1",
    )

    joined = " ".join(queries)
    assert "CRO" in joined
    assert "CDMO" in joined
    assert "\u8ba2\u5355" in joined
    assert "\u5730\u7f18\u98ce\u9669" in joined


def test_medical_device_fact_queries_prioritize_device_terms():
    queries = web_facts._fact_queries(
        "300760.SZ",
        "\u8fc8\u745e\u533b\u7597",
        "\u533b\u7597\u5668\u68b0",
    )

    joined = " ".join(queries)
    assert "\u8bbe\u5907\u66f4\u65b0" in joined
    assert "\u88c5\u673a" in joined
    assert "\u8bd5\u5242" in joined
    assert "\u96c6\u91c7" in joined
    assert "\u6ce8\u518c\u8bc1" in joined
    assert "\u4e34\u5e8a" not in joined
    assert "\u7ba1\u7ebf" not in joined


def test_bing_news_rss_parses_source_date_and_values(monkeypatch):
    class FakeResponse:
        text = """<?xml version="1.0" encoding="utf-8"?>
<rss><channel>
  <item>
    <title>Feitian Maotai wholesale 2200 \u5143</title>
    <description>Loose bottle reference price 2180 \u5143/\u74f6.</description>
    <source>Fact Source</source>
    <pubDate>Wed, 20 May 2026 08:00:00 GMT</pubDate>
    <link>https://example.com/fact</link>
  </item>
</channel></rss>"""

        def raise_for_status(self):
            return None

    captured = {}

    def fake_get(url, **kwargs):
        captured["url"] = url
        captured["params"] = kwargs["params"]
        return FakeResponse()

    monkeypatch.setattr(web_facts.requests, "get", fake_get)

    rows = web_facts._bing_news_rss("maotai price", timeout=1, max_results=3)

    assert captured["url"] == "https://www.bing.com/news/search"
    assert captured["params"]["format"] == "rss"
    assert rows[0].source == "Fact Source"
    assert rows[0].published == "2026-05-20"
    assert "2180\u5143/\u74f6" in rows[0].extracted_values


def test_bing_news_rss_falls_back_when_news_endpoint_is_not_rss(monkeypatch):
    class FakeResponse:
        def __init__(self, text):
            self.text = text

        def raise_for_status(self):
            return None

    rss = """<?xml version="1.0" encoding="utf-8"?>
<rss><channel>
  <item>
    <title>Order growth 12%</title>
    <description>Recent product price update.</description>
    <source>Search Source</source>
    <pubDate>Wed, 20 May 2026 08:00:00 GMT</pubDate>
    <link>https://example.com/search-fact</link>
  </item>
</channel></rss>"""

    urls = []

    def fake_get(url, **kwargs):
        urls.append(url)
        if url.endswith("/news/search"):
            return FakeResponse("temporarily unavailable")
        return FakeResponse(rss)

    monkeypatch.setattr(web_facts.requests, "get", fake_get)

    rows = web_facts._bing_news_rss("\u76c8\u5cf0\u73af\u5883 \u8ba2\u5355", timeout=1, max_results=3)

    assert urls == ["https://www.bing.com/news/search", "https://www.bing.com/search"]
    assert rows[0].source == "Search Source"


def test_resource_web_fact_context_uses_resource_purpose(monkeypatch):
    monkeypatch.setattr(
        web_facts,
        "_company_profile",
        lambda symbol: ("\u7d2b\u91d1\u77ff\u4e1a", "\u94dc"),
    )
    monkeypatch.setattr(web_facts, "_bing_news_rss", lambda *args, **kwargs: [])
    monkeypatch.setattr(web_facts.time, "sleep", lambda seconds: None)

    context = web_facts.get_web_fact_check_context(
        "601899.SH",
        "2026-06-01",
        max_queries=3,
        max_results_per_query=1,
    )

    assert "resource-company facts" in context
    assert "\u7d2b\u91d1\u77ff\u4e1a \u94dc \u9ec4\u91d1 \u4ea7\u54c1\u4ef7\u683c \u5e93\u5b58" in context
    assert "\u77ff\u5c71 \u9879\u76ee\u8fdb\u5c55 \u5e76\u8d2d" in context
    assert "baijiu wholesale prices" not in context
    assert "For resource companies" in context
