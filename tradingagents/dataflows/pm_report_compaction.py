"""Deterministic separation of the public PM memo from research audit material."""

from __future__ import annotations

import re


_PUBLIC_PM_CONTRACT_HEADINGS = {
    "company disaggregation",
    "autonomous three-year forecast model",
    "thesis-to-financial bridge",
    "moat evidence scorecard",
    "valuation closure",
    "shared underwriting model change audit",
    "handoff integrity audit",
}

_PM_APPENDIX_HEADING_TERMS = (
    "附录a",
    "附录b",
    "内部附录",
    "internal appendix",
    "模型变更与交接审计",
    "质量自检",
    "业务机制与分部经济",
    "行业驱动与护城河机制",
    "财务质量核查明细",
    "替代信息与卖方预期审计",
    "模型交接与报告质量审计",
    "pm摘要",
    "pm summary",
    "辩论与决策",
    "debate and decision",
    "业务模式与分部",
    "business model and segment",
    "前瞻预测模型",
    "forward forecast model",
    "估值闭合与预期差",
    "valuation closure and expectation",
    "核心投资论点",
    "investment thesis detail",
    "知识星球线索审计",
    "knowledge planet audit",
    "信息利用审计",
    "information utilization audit",
    "报告质量自检",
    "report quality self-check",
    "最终决策",
    "final decision recap",
)


def split_pm_public_report(report: str) -> tuple[str, str, list[str]]:
    """Move duplicated/internal PM sections out of the public company memo."""
    text = str(report or "").strip()
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    if not matches:
        return text, "", []

    public_parts = [text[: matches[0].start()].rstrip()]
    appendix_parts: list[str] = []
    moved: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.start() : end].strip()
        heading = match.group(1).strip()
        normalized = re.sub(r"\s+", " ", heading).lower()
        move_to_appendix = (
            normalized not in _PUBLIC_PM_CONTRACT_HEADINGS
            and any(term in normalized for term in _PM_APPENDIX_HEADING_TERMS)
        )
        if move_to_appendix:
            appendix_parts.append(section)
            moved.append(heading)
        else:
            public_parts.append(section)

    public_report = "\n\n".join(part for part in public_parts if part).strip()
    appendix = "\n\n".join(appendix_parts).strip()
    return public_report, appendix, moved
