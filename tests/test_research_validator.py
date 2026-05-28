"""Tests for saved-report parsing used by validation scripts."""

from tradingagents.evaluation.research_validator import (
    audit_decision_depth,
    _extract_rating,
    _extract_section,
    _normalize_rating,
)


def test_audit_decision_depth_flags_missing_buy_side_sections():
    issues = audit_decision_depth(
        "**Investment Thesis**: The company is good and valuation is fair.\n\n"
        "**Verification & Falsification**: Keep watching."
    )
    sections = {issue.section for issue in issues}

    assert "business_segment_breakdown" in sections
    assert "peer_comparison_summary" in sections
    assert "valuation_expectation" in sections
    assert "verification_and_falsification" in sections
    assert "key_data_check" in sections
    assert "expectation_gap_evidence" in sections
    assert "underwriting_modules" in sections
    assert "filing_internal_quality" in sections
    assert "verification_calendar" in sections


def test_audit_decision_depth_accepts_rich_buy_side_sections():
    text = (
        "**Investment Thesis**: Business Segment Breakdown: core business revenue, "
        "growth, gross margin, net margin, profit, cash conversion, valuation, "
        "and not disclosed second-curve economics are discussed. "
        "Peer Comparison Summary: peer rank, comparable universe, valuation, ROE, "
        "margin, growth, leverage, and allocation impact are discussed. "
        "Market-implied expectation: current PE multiple implied EPS and ROE recovery, "
        "but cash flow must confirm. Key data check: reconcile revenue, net profit, "
        "EPS, market cap, PE, PB, operating cash flow, capex, and contract liabilities. "
        "Expectation-gap evidence: valuation percentile, price-EPS decomposition, "
        "consensus, holder behavior, technical action, and investor interaction. "
        "Filing internal quality review: accounting reconciliation, segment economics, "
        "footnote radar, cash-flow quality, capex CIP return bridge, MD&A text change, "
        "non-recurring profit, balance-sheet forward signals, shareholder-return "
        "authenticity, and disclosure quality are integrated into risk and valuation. "
        "Unit-economics bridge: platform GMV x take rate x margin; breakeven not disclosed. "
        "Project ramp capacity bridge: occupancy and utilization drive capex ROIC. "
        "Financing / listing scenario: use of proceeds and dilution are tested.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash "
        "flow falls; downgrade if revenue growth and margin deteriorate.\n\n"
        "**Verification Calendar**: next disclosure: add on margin confirmation, "
        "hold if stable, trim on weak cash flow, downgrade and exit on failed evidence."
    )

    assert audit_decision_depth(text) == []


def test_normalize_rating_handles_empty_label_value():
    assert _normalize_rating("") == "Unknown"


def test_extract_rating_handles_chinese_only_rating():
    text = "# Portfolio Manager\n\n**\u8bc4\u7ea7\uff1a\u5356\u51fa**\n\nBody"
    assert _extract_rating(text) == "Sell"


def test_extract_rating_handles_chinese_rating_with_english_alias():
    text = "**\u8bc4\u7ea7\uff1a\u4f4e\u914d\uff08Underweight\uff09**\n**Price: 76**"
    assert _extract_rating(text) == "Underweight"


def test_extract_rating_ignores_prior_rating_without_value():
    text = (
        "**Portfolio Manager Decision**\n\n"
        "**Investment Decision: Underweight**\n\n"
        "**Prior Rating:**\n\n"
        "No prior rating was available."
    )
    assert _extract_rating(text) == "Underweight"


def test_extract_core_bet_from_same_line_chinese_label():
    text = (
        "**\u6838\u5fc3\u5224\u65ad**\uff1a"
        "\u5f53\u524d\u62a5\u4ef7\u9690\u542b\u9ad8\u4f4d\u5546\u54c1"
        "\u4ef7\u683c\u4e0e\u4ea7\u91cf\u52a0\u901f\u7684\u7ec4\u5408\u5047\u8bbe\u3002"
    )
    assert _extract_section(text, ["\u6838\u5fc3\u5224\u65ad"]) == (
        "\u5f53\u524d\u62a5\u4ef7\u9690\u542b\u9ad8\u4f4d\u5546\u54c1"
        "\u4ef7\u683c\u4e0e\u4ea7\u91cf\u52a0\u901f\u7684\u7ec4\u5408\u5047\u8bbe\u3002"
    )


def test_extract_core_bet_from_header_and_next_paragraph():
    text = (
        "**\u6838\u5fc3\u62bc\u6ce8**\n"
        "\n"
        "\u5e02\u573a\u6b63\u5728\u4e3a\u53ef\u6301\u7eed\u76c8\u5229"
        "\u590d\u82cf\u5b9a\u4ef7\uff0c\u4f46\u73b0\u91d1\u8f6c\u6362"
        "\u8d28\u91cf\u4ecd\u9700\u9a8c\u8bc1\u3002\n"
    )
    assert _extract_section(text, ["\u6838\u5fc3\u62bc\u6ce8"]) == (
        "\u5e02\u573a\u6b63\u5728\u4e3a\u53ef\u6301\u7eed\u76c8\u5229"
        "\u590d\u82cf\u5b9a\u4ef7\uff0c\u4f46\u73b0\u91d1\u8f6c\u6362"
        "\u8d28\u91cf\u4ecd\u9700\u9a8c\u8bc1\u3002"
    )
