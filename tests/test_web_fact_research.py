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
