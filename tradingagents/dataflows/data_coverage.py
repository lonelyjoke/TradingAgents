"""Summarize precomputed data coverage for downstream decision agents."""

from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class ContextCoverage:
    name: str
    status: str
    note: str


FAILURE_PATTERNS = (
    "context unavailable",
    "# financial-report intelligence unavailable",
    "# thematic catalyst cross-check unavailable",
    "# commodity/product-price context unavailable",
    "# same-industry peer comparison unavailable",
    "# supply-chain position comparison unavailable",
    "# earnings-model context unavailable",
    "# market-expectation context unavailable",
    "# price-eps-pe decomposition unavailable",
    "# management/capital-allocation context unavailable",
    "# shareholder-structure context unavailable",
    "# investor-interaction context unavailable",
    "# policy-planning context unavailable",
    "# baijiu verification context unavailable",
    "# compute-leasing verification layer unavailable",
    "# dividend defensive verification layer unavailable",
    "lookup unavailable",
    "unavailable\n\n- reason",
    "extraction status: financial-report text extraction unavailable",
    "narrative filing text extraction unavailable",
    "financial-report text extraction unavailable",
    "no readable report text",
    "no commodity mapping found",
    "| failed |",
    "api error",
    "traceback",
    "不可用",
    "无法获取",
    "无法加载",
    "提取失败",
    "调用失败",
    "请指定正确的接口名",
    "无可读",
    "失败",
)

SUCCESS_HINTS = (
    "##",
    "| --- |",
    "reachable",
    "coverage_grade",
    "Earnings Snapshots",
)


def _first_relevant_line(text: str) -> str:
    for raw in text.splitlines():
        line = raw.strip(" -")
        if not line or line.startswith("| ---"):
            continue
        lower = line.lower()
        if any(pattern in lower for pattern in FAILURE_PATTERNS):
            return line
    for raw in text.splitlines():
        line = raw.strip()
        if line:
            return line
    return ""


def classify_context_coverage(name: str, text: str) -> ContextCoverage:
    """Classify whether one precomputed research context is usable."""
    cleaned = (text or "").strip()
    if not cleaned:
        return ContextCoverage(name, "missing", "context is empty")

    lower = cleaned.lower()
    if "status: not_applicable" in lower:
        return ContextCoverage(name, "not_applicable", _first_relevant_line(cleaned))

    has_failure = any(pattern in lower for pattern in FAILURE_PATTERNS)
    has_success_hint = any(hint.lower() in lower for hint in SUCCESS_HINTS)

    if has_failure:
        status = "partial" if has_success_hint and len(cleaned) > 500 else "failed"
    else:
        status = "ready" if len(cleaned) > 120 else "thin"

    note = _first_relevant_line(cleaned)
    note = re.sub(r"\s+", " ", note)
    if len(note) > 180:
        note = note[:177] + "..."
    return ContextCoverage(name, status, note)


def build_data_coverage_context(contexts: dict[str, str]) -> str:
    """Render a compact data coverage audit for manager prompts and saved reports."""
    rows = [
        classify_context_coverage(name, value)
        for name, value in contexts.items()
    ]
    if not rows:
        return "# Data Coverage Audit\n\nNo precomputed context modules were supplied."

    lines = [
        "# Data Coverage Audit",
        "",
        "| module | status | note |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        note = row.note.replace("|", "/")
        lines.append(f"| {row.name} | {row.status} | {note} |")

    failed = [row.name for row in rows if row.status in {"failed", "missing"}]
    partial = [row.name for row in rows if row.status == "partial"]
    if failed or partial:
        lines.extend(
            [
                "",
                "## Required Manager Treatment",
                "- Do not treat failed or missing modules as neutral evidence.",
                "- Distinguish a narrative filing-text extraction gap from a full financial-data failure. If structured statements, market data, peers, or valuation contexts are present, say only that report-body/segment/management-discussion evidence is missing.",
                "- If a failed or partial module touches the core bet, name it as a research gap and cap conviction.",
                "- If other verified modules still support a directional view, state the view as evidence-limited and list the data needed to confirm or refute it.",
            ]
        )
    return "\n".join(lines)
