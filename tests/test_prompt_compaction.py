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
