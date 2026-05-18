from tradingagents.dataflows.investor_interaction_research import (
    _build_cninfo_company_url,
    _build_cninfo_question_params,
    _build_sse_company_feed_params,
    _build_sse_company_url,
    _build_sse_feed_params,
    _classify_answer,
    _extract_interaction_theme,
    _extract_sse_uid_from_company_page,
    _interaction_exchange,
    _parse_cninfo_question_payload,
    _parse_sse_company_feed_html,
    _parse_sse_company_feed_records,
    _parse_sse_company_page,
    summarize_interaction_themes,
)


def test_interaction_exchange_routes_a_share_suffixes():
    assert _interaction_exchange("002202.SZ") == "szse"
    assert _interaction_exchange("600519.SH") == "sse"


def test_company_url_builders_preserve_official_routes():
    assert _build_sse_company_url("600519.SH").endswith("company.do?stockcode=600519")
    assert "orgId=gfbj0835960" in _build_cninfo_company_url("gfbj0835960", "002202.SZ")
    assert "stockcode=002202" in _build_cninfo_company_url("gfbj0835960", "002202.SZ")


def test_cninfo_question_params_match_official_query_shape():
    assert _build_cninfo_question_params("9900003947", "002202.SZ") == {
        "stockcode": "002202",
        "orgId": "9900003947",
        "pageSize": 10,
        "pageNum": 1,
        "keyWord": "",
        "startDay": "",
        "endDay": "",
    }


def test_sse_feed_params_default_to_public_interaction_feed():
    assert _build_sse_feed_params() == {
        "type": 11,
        "pageSize": 10,
        "show": 1,
        "page": 1,
    }


def test_sse_company_feed_helpers_capture_uid_and_empty_state():
    html = '<a href="ajax/userfeeds.do?typeCode=company&type=11&pageSize=10&uid=519&page=2"></a>'
    assert _extract_sse_uid_from_company_page(html) == "519"
    assert _build_sse_company_feed_params("519") == {
        "typeCode": "company",
        "type": 11,
        "pageSize": 10,
        "uid": "519",
        "page": 1,
    }
    parsed = _parse_sse_company_feed_html("<div>近1个月暂无回复</div>")
    assert parsed["is_empty_recent_reply"] is True


def test_parse_sse_company_page_detects_company_and_qa_markers():
    parsed = _parse_sse_company_page(
        "<html><head><title>上证e互动</title></head><body>上证e互动 问答</body></html>"
    )

    assert parsed["title"] == "上证e互动"
    assert parsed["has_company_page"] is True
    assert parsed["has_qa_section"] is True


def test_parse_cninfo_question_payload_normalizes_answered_and_unanswered_rows():
    payload = {
        "rows": [
            {
                "indexId": "1",
                "mainContent": "请问什么时候投产？",
                "pubDate": 1777287734000,
                "attachedContent": "您好，公司已经开始推动战略合作的落地实施，感谢您的关注。",
                "attachedPubDate": None,
                "updateDate": 1778145452000,
            },
            {
                "indexId": "2",
                "mainContent": "请问股东人数？",
                "pubDate": 1778808755000,
                "attachedContent": None,
                "attachedPubDate": None,
                "updateDate": 1778834013000,
            },
        ]
    }

    result = _parse_cninfo_question_payload(payload, "002202.SZ")

    assert list(result["question_id"]) == ["1", "2"]
    assert result.iloc[0]["question_time"] == "2026-04-27"
    assert result.iloc[0]["answer_time"] == "2026-05-07"
    assert result.iloc[0]["answer_class"] == "directional-but-unquantified"
    assert result.iloc[1]["answer"] is None
    assert result.iloc[1]["answer_class"] == "unanswered"


def test_classify_answer_separates_substantive_from_non_committal():
    assert _classify_answer("您好，公司2026年一季度营业收入为154.85亿元。") == "substantive"
    assert _classify_answer("您好，感谢您的关注。") == "non-committal"


def test_extract_interaction_theme_reads_story_from_official_text():
    result = _extract_interaction_theme(
        "公司是否有算电协同项目？",
        "您好，公司已在数据中心场景推进算电协同。",
    )

    assert result["theme"] == "compute-power"
    assert "computing infrastructure" in result["story_read"]


def test_summarize_interaction_themes_counts_repeated_signals():
    records = _parse_cninfo_question_payload(
        {
            "rows": [
                {
                    "indexId": "1",
                    "mainContent": "公司是否有算电协同项目？",
                    "pubDate": 1777287734000,
                    "attachedContent": "您好，公司已在数据中心场景推进算电协同。",
                    "attachedPubDate": None,
                    "updateDate": 1778145452000,
                },
                {
                    "indexId": "2",
                    "mainContent": "算力业务如何推进？",
                    "pubDate": 1777287735000,
                    "attachedContent": "您好，公司正在推进算力相关业务。",
                    "attachedPubDate": None,
                    "updateDate": 1778145453000,
                },
            ]
        },
        "002202.SZ",
    )

    summary = summarize_interaction_themes(records)

    assert summary.iloc[0]["theme"] == "compute-power"
    assert summary.iloc[0]["mentions"] == 2


def test_parse_sse_company_feed_records_normalizes_question_and_answer():
    html = """
    <div class="m_feed_item" id="item-1700800">
      <div class="m_feed_detail">
        <div class="m_feed_txt">
          <a href='user.do?uid=1318'>:中国平安(601318)</a>恭喜公司2025年取得优异成绩！
        </div>
        <div class="m_feed_from"><span>2026年04月10日 12:14</span></div>
      </div>
      <div class="m_feed_detail m_qa">
        <div class="m_feed_txt" id="m_feed_txt-1700800">
          您好，公司保险资金投资始终秉持长期投资、价值投资。谢谢！
        </div>
        <div class="m_feed_from"><span>2026年04月24日 17:14</span></div>
      </div>
    </div>
    """

    result = _parse_sse_company_feed_records(html, "601318.SH")

    assert list(result["question_id"]) == ["1700800"]
    assert result.iloc[0]["question_time"] == "2026-04-10"
    assert result.iloc[0]["answer_time"] == "2026-04-24"
    assert result.iloc[0]["question"].startswith("恭喜公司2025年取得优异成绩")
    assert result.iloc[0]["answer_class"] == "substantive"
    assert result.iloc[0]["source_type"] == "sse_e_interaction"
