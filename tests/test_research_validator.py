"""Tests for saved-report parsing used by validation scripts."""

from tradingagents.evaluation.research_validator import (
    audit_decision_depth,
    _extract_rating,
    _extract_section,
    _normalize_rating,
)


def test_audit_decision_depth_flags_missing_segment_and_peer_sections():
    issues = audit_decision_depth(
        "**Investment Thesis**: 公司很好，估值合理。\n\n"
        "**Verification & Falsification**: 继续观察。"
    )
    sections = {issue.section for issue in issues}

    assert "business_segment_breakdown" in sections
    assert "peer_comparison_summary" in sections
    assert "valuation_expectation" in sections
    assert "verification_and_falsification" in sections


def test_audit_decision_depth_accepts_rich_buy_side_sections():
    text = (
        "**Investment Thesis**: Business Segment Breakdown: 核心业务收入规模、收入增长、"
        "毛利率、净利率、利润贡献、现金转换和估值处理均已讨论；第二曲线未披露利润，"
        "因此 not disclosed 并只给场景估值。Peer Comparison Summary: 同行排名、"
        "可比公司、估值、ROE、margin、growth、leverage 和 allocation 影响均已说明。"
        "Market-implied expectation: current PE multiple implied EPS and ROE recovery, "
        "but cash flow must confirm.\n\n"
        "**Verification & Falsification**: confirm orders and margin; weaken if cash "
        "flow falls; downgrade if revenue growth and 毛利 deteriorate."
    )

    assert audit_decision_depth(text) == []


def test_normalize_rating_handles_empty_label_value():
    assert _normalize_rating("") == "Unknown"


def test_extract_rating_handles_chinese_only_rating():
    text = "# 投资组合经理最终决策\n\n**评级：卖出**\n\n正文"
    assert _extract_rating(text) == "Sell"


def test_extract_rating_handles_chinese_rating_with_english_alias():
    text = "**评级：低配（Underweight）**\n**当前价格：约76元**"
    assert _extract_rating(text) == "Underweight"


def test_extract_rating_ignores_prior_rating_without_value():
    text = (
        "**Portfolio Manager Decision**\n\n"
        "**投资决策：Underweight（减持）**\n\n"
        "**Prior Rating:**\n\n"
        "No prior rating was available."
    )
    assert _extract_rating(text) == "Underweight"


def test_extract_core_bet_from_same_line_chinese_label():
    text = "**核心判断**：当前报价隐含高位商品价格与产量加速的组合假设。"
    assert _extract_section(text, ["核心判断"]) == "当前报价隐含高位商品价格与产量加速的组合假设。"


def test_extract_core_bet_from_header_and_next_paragraph():
    text = (
        "**核心押注**\n"
        "\n"
        "市场正在为可持续盈利复苏定价，但现金转换质量仍需验证。\n"
    )
    assert (
        _extract_section(text, ["核心押注"])
        == "市场正在为可持续盈利复苏定价，但现金转换质量仍需验证。"
    )
