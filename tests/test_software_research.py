from tradingagents.dataflows.software_research import get_software_context


def test_software_context_triggers_for_kingsoft_office(monkeypatch):
    monkeypatch.setattr(
        "tradingagents.dataflows.software_research._fetch_stock_basic",
        lambda symbol: {"name": "\u91d1\u5c71\u529e\u516c", "industry": "\u8f6f\u4ef6\u670d\u52a1"},
    )
    monkeypatch.setattr(
        "tradingagents.dataflows.software_research._load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: ("", []),
    )

    rendered = get_software_context("688111.SH", "2026-06-03")

    assert "Status: triggered" in rendered
    assert "office productivity subscription / enterprise SaaS" in rendered
    assert "WPS Office MAU and paid-user conversion" in rendered
    assert "AI features are not AI revenue" in rendered
    assert "contract liabilities" in rendered
    assert "Software Business-Model Taxonomy" in rendered
    assert "Model-Labeled Peer Map" in rendered
    assert "Company-Specific Deep-Dive Questions" in rendered
    assert "Free MAU to paid conversion" in rendered


def test_software_context_not_applicable_for_unrelated_stock(monkeypatch):
    monkeypatch.setattr(
        "tradingagents.dataflows.software_research._fetch_stock_basic",
        lambda symbol: {"name": "\u5b8f\u548c\u79d1\u6280", "industry": "\u73bb\u7483\u7ea4\u7ef4"},
    )
    monkeypatch.setattr(
        "tradingagents.dataflows.software_research._load_financial_report_texts",
        lambda symbol, curr_date, look_back_days: ("", []),
    )

    rendered = get_software_context("603256.SH", "2026-06-03")

    assert "Status: not_applicable" in rendered


def test_software_web_queries_use_saas_terms():
    from tradingagents.dataflows.web_fact_research import _fact_queries

    queries = _fact_queries("688111.SH", "\u91d1\u5c71\u529e\u516c", "\u8f6f\u4ef6\u670d\u52a1")

    joined = " ".join(queries)
    assert "ARPU" in joined
    assert "\u4ed8\u8d39\u7528\u6237" in joined
    assert "\u5408\u540c\u8d1f\u503a" in joined
    assert "\u6e20\u9053\u5e93\u5b58" not in joined
