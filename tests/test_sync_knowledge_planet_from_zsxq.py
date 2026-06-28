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
