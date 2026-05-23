from tradingagents.dataflows.prompt_compaction import (
    compact_for_prompt,
    compact_state_fields,
)


def test_compaction_preserves_high_signal_failure_and_verdict_lines():
    text = "\n".join(
        [
            "# Filing intelligence",
            "Routine background line " + ("x" * 500),
            "Revenue table row " + ("1,2,3 " * 200),
            "Data coverage audit: financial-report extraction partial",
            "Research gap: product spread is missing and caps conviction",
            "Final verdict: evidence-limited Overweight",
            *[f"low value table row {i} " + ("z" * 120) for i in range(120)],
            "Ending caveat: verify inventory and cash flow next quarter.",
        ]
    )

    compacted = compact_for_prompt(
        text,
        label="filing_intelligence_context",
        profile="risk",
        max_chars=1200,
    )

    assert len(compacted) < len(text)
    assert "Data coverage audit" in compacted
    assert "Research gap" in compacted
    assert "Final verdict" in compacted
    assert "Ending caveat" in compacted


def test_compact_state_fields_returns_compacted_copy_without_mutating_state():
    long_context = "# Theme\n" + "\n".join(
        [f"table row {i} " + ("x" * 80) for i in range(100)]
    )
    state = {
        "thematic_catalyst_context": long_context,
        "commodity_context": "short commodity context",
    }

    compacted = compact_state_fields(
        state,
        profile="risk",
        keys={"thematic_catalyst_context", "commodity_context"},
    )

    assert compacted["commodity_context"] == "short commodity context"
    assert len(compacted["thematic_catalyst_context"]) < len(long_context)
    assert state["thematic_catalyst_context"] == long_context


def test_compaction_preserves_compute_leasing_diligence_gap():
    text = "\n".join(
        [
            "# Thematic catalyst",
            *[f"low value concept row {i} " + ("z" * 100) for i in range(80)],
            (
                "| \u7b97\u529b\u79df\u8d41/\u667a\u4e91\u8ba1\u7b97 | investor-interaction | "
                "no valuation credit; diligence red flag until filings clarify economics | "
                "Q: \u516c\u53f8\u662f\u5426\u5f00\u5c55\u7b97\u529b\u79df\u8d41\uff1f / "
                "A: \u8bf7\u4ee5\u6307\u5b9a\u4fe1\u606f\u62ab\u9732\u5a92\u4f53\u4e3a\u51c6 |"
            ),
            *[f"more low value row {i} " + ("y" * 100) for i in range(80)],
        ]
    )

    compacted = compact_for_prompt(
        text,
        label="thematic_catalyst_context",
        profile="portfolio",
        max_chars=1000,
    )

    assert "\u7b97\u529b\u79df\u8d41" in compacted
    assert "\u6307\u5b9a\u4fe1\u606f\u62ab\u9732\u5a92\u4f53" in compacted


def test_compaction_preserves_segment_valuation_and_competitor_sections():
    text = "\n".join(
        [
            "# Combined context",
            *[f"routine table row {i} " + ("x" * 100) for i in range(90)],
            "## Business Segment Valuation Map",
            "| business_bucket | valuation_anchor | verification_need |",
            "| emerging_or_second_curve | SOTP/scenario value | verify revenue, margin, customer quality, and cash conversion |",
            "## Competitor Analysis For Peer Recommendation",
            "| competitor | apparent_edges | diligence_use |",
            "| Peer Alpha | ROE higher and PE lower | Verify filing-based business overlap and segment economics |",
            *[f"more routine row {i} " + ("y" * 100) for i in range(90)],
        ]
    )

    compacted = compact_for_prompt(
        text,
        label="filing_intelligence_context",
        profile="portfolio",
        max_chars=1400,
    )

    assert "Business Segment Valuation Map" in compacted
    assert "Competitor Analysis For Peer Recommendation" in compacted
    assert "SOTP/scenario value" in compacted
    assert "Verify filing-based business overlap" in compacted
