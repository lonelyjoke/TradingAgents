from scripts import sync_knowledge_planet_from_zsxq as sync


def _topic(date_text: str, topic_id: str) -> dict:
    return {
        "topic_id": topic_id,
        "create_time": f"{date_text}T10:00:00.000+0800",
        "content": topic_id,
    }


def test_fetch_window_raises_when_page_limit_does_not_reach_start(monkeypatch):
    monkeypatch.setattr(
        sync,
        "_run_zsxq_json",
        lambda _args: {
            "topics_brief": [_topic("2026-06-20", "a"), _topic("2026-06-19", "b")],
            "has_more": True,
            "next_end_time": "cursor-2",
        },
    )

    try:
        sync.fetch_topics_for_window(
            sync.ZsxqGroup("group-1"),
            "2026-06-17",
            "2026-06-19",
            limit_per_page=30,
            max_pages=1,
        )
    except sync.PaginationLimitReached as exc:
        assert "increase --max-pages" in str(exc)
        assert "oldest_date=2026-06-19" in str(exc)
    else:
        raise AssertionError("expected PaginationLimitReached")


def test_fetch_window_scans_once_and_collects_requested_dates(monkeypatch):
    pages = iter(
        [
            {
                "topics_brief": [_topic("2026-06-20", "outside"), _topic("2026-06-19", "d19")],
                "has_more": True,
                "next_end_time": "cursor-2",
            },
            {
                "topics_brief": [_topic("2026-06-18", "d18"), _topic("2026-06-16", "older")],
                "has_more": True,
                "next_end_time": "cursor-3",
            },
        ]
    )
    calls = []

    def fake_run(args):
        calls.append(args)
        return next(pages)

    monkeypatch.setattr(sync, "_run_zsxq_json", fake_run)

    topics = sync.fetch_topics_for_window(
        sync.ZsxqGroup("group-1"),
        "2026-06-17",
        "2026-06-19",
        limit_per_page=30,
        max_pages=5,
    )

    assert [topic["topic_id"] for topic in topics] == ["d19", "d18"]
    assert len(calls) == 2
    assert "--end-time" in calls[1]


def test_text_only_attachment_sync_never_requests_file_download_url(tmp_path, monkeypatch):
    calls = []

    def forbidden_download_url(file_id: str) -> str:
        calls.append(file_id)
        raise AssertionError("text-only mode must not request a download URL")

    monkeypatch.setattr(sync, "_get_file_download_url", forbidden_download_url)
    topic = {
        "topic_id": "topic-1",
        "files": [
            {"file_id": "file-1", "name": "研究报告.pdf"},
            {
                "file_id": "file-2",
                "name": "会议纪要.mp3",
                "download_url": "https://example.invalid/file-2",
            },
        ],
    }

    result = sync.sync_topic_attachments(
        topic,
        root=tmp_path,
        target_date="2026-07-06",
        download_images=False,
        ocr_images=False,
        ocr_language="zh-Hans-CN",
        download_files=False,
        max_image_downloads=0,
        max_file_downloads=0,
    )

    assert calls == []
    assert result.files_downloaded == 0
    assert result.file_failures == 0
    assert result.file_lines == [
        "Files:",
        "- 研究报告.pdf file_id=file-1",
        "- 会议纪要.mp3 file_id=file-2",
    ]
    assert not list(tmp_path.rglob("*.pdf"))
    assert not list(tmp_path.rglob("*.mp3"))


def test_only_frontier_information_group_is_allowed():
    sync.validate_allowed_groups([sync.ZsxqGroup("28888112822211", "前沿信息收录")])

    try:
        sync.validate_allowed_groups([sync.ZsxqGroup("other-group")])
    except ValueError as exc:
        assert "前沿信息收录" in str(exc)
        assert "other-group" in str(exc)
    else:
        raise AssertionError("expected out-of-scope group to be rejected")


def test_youdao_public_share_is_extracted_from_encoded_topic_link(monkeypatch):
    share_key = "b42b29a94073d2c3609f54cc22287771"
    url = f"https://note.youdao.com/ynoteshare/index.html?id={share_key}&type=note"
    topic = {"content": f'<e type="web" href="{url.replace("&", "%26")}">北方市场专家</e>'}

    links = sync._public_links_from_topic(topic)
    assert links[0] == url

    def fake_request_json(request_url, **_kwargs):
        if "personal/share" in request_url:
            return {"entry": {"name": "北方市场专家交流"}}
        return {"content": '{"children":[{"8":"山东终端动销与库存反馈"},{"8":"渠道库存处于正常区间"}]}' }

    monkeypatch.setattr(sync, "_request_json", fake_request_json)
    result = sync.resolve_public_link(
        url,
        allowed_domains={"note.youdao.com"},
        timeout_sec=3,
        max_bytes=100_000,
    )

    assert result.status == "resolved"
    assert result.title == "北方市场专家交流"
    assert "山东终端动销" in result.text
    assert "渠道库存" in result.text


def test_public_link_failure_is_a_non_blocking_artifact():
    result = sync.resolve_public_link(
        "https://example.com/private-note",
        allowed_domains={"note.youdao.com"},
        timeout_sec=1,
        max_bytes=1024,
    )

    assert result.status == "skipped"
    rendered = sync._format_topic_block(
        {"topic_id": "1", "content": "company research"},
        sync.ZsxqGroup("28888112822211", "前沿信息收录"),
        external_link_results=[result],
    )
    assert "external_link_status: skipped" in rendered
    assert "company research" in rendered
