"""Derived company business-model and segment-economics primer."""

from __future__ import annotations

import re
from typing import Iterable, Mapping


_SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)


def _section(text: str, title: str, *, max_chars: int = 2400) -> str:
    matches = list(_SECTION_RE.finditer(text or ""))
    for index, match in enumerate(matches):
        if match.group(1).strip().lower() != title.lower():
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = (text[start:end] or "").strip()
        return body[:max_chars].strip()
    return ""


def _compact_lines(text: str, *, limit: int = 8, max_line: int = 260) -> list[str]:
    rows: list[str] = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("| ---"):
            continue
        if line.startswith("#"):
            continue
        line = re.sub(r"\s+", " ", line)
        if len(line) > max_line:
            line = line[: max_line - 3] + "..."
        rows.append(line)
        if len(rows) >= limit:
            break
    return rows


def _extract_company_meta(filing_intelligence_context: str) -> tuple[str, str]:
    company = ""
    industry = ""
    for line in (filing_intelligence_context or "").splitlines():
        if line.startswith("- Company:"):
            company = line.split(":", 1)[1].strip()
        elif line.startswith("- Vendor industry:"):
            industry = line.split(":", 1)[1].strip()
    return company, industry


def _bullet_rows(lines: Iterable[str]) -> list[str]:
    return [f"- {line.replace('|', '/')}" for line in lines]


def build_company_business_model_context(
    symbol: str,
    curr_date: str,
    *,
    filing_intelligence_context: str = "",
    peer_comparison_context: str = "",
    supply_chain_comparison_context: str = "",
    commodity_context: str = "",
    investor_interaction_context: str = "",
) -> str:
    """Build a reader-facing business model primer from existing contexts."""

    company, industry = _extract_company_meta(filing_intelligence_context)
    business_model = _section(filing_intelligence_context, "Business Model Map")
    segment_economics = _section(filing_intelligence_context, "Segment Economics Pack")
    segment_valuation = _section(filing_intelligence_context, "Business Segment Valuation Map")
    archetype = _section(filing_intelligence_context, "Company-Specific Business Archetype", max_chars=1200)
    growth_vectors = _section(filing_intelligence_context, "Growth Vector Map", max_chars=1600)
    underwriting = _section(filing_intelligence_context, "Pre-Debate Underwriting Questions", max_chars=1800)

    business_rows = _compact_lines(business_model, limit=6)
    segment_rows = _compact_lines(segment_economics, limit=8)
    valuation_rows = _compact_lines(segment_valuation, limit=6)
    archetype_rows = _compact_lines(archetype, limit=3)
    growth_rows = _compact_lines(growth_vectors, limit=5)
    peer_rows = _compact_lines(peer_comparison_context, limit=4)
    chain_rows = _compact_lines(supply_chain_comparison_context, limit=4)
    commodity_rows = _compact_lines(commodity_context, limit=3)
    interaction_rows = _compact_lines(investor_interaction_context, limit=3)

    if not business_rows and not segment_rows:
        business_rows = [
            "No clean business-model or segment-economics filing section was available; the report must explicitly downgrade confidence before describing the business model."
        ]

    return "\n".join(
        [
            f"# Company Business Model Primer for {symbol} as of {curr_date}",
            "",
            f"- Company: {company or symbol}",
            f"- Vendor industry: {industry or 'unknown'}",
            "- Purpose: make the reader understand how the company earns money before valuation or cycle language.",
            "",
            "## Business Archetype",
            *_bullet_rows(archetype_rows or ["No clean archetype row extracted."]),
            "",
            "## How The Company Makes Money",
            *_bullet_rows(business_rows),
            "",
            "## Segment Economics / Profit Pools",
            *_bullet_rows(segment_rows or ["Segment revenue, cost, gross-margin, or growth split was not cleanly extracted; do not value all businesses with one multiple without caveat."]),
            "",
            "## Segment Valuation / Evidence Gates",
            *_bullet_rows(valuation_rows or ["No clean segment valuation map was extracted; use blended valuation only as a rough cross-check."]),
            "",
            "## Growth Vectors And Second Curves",
            *_bullet_rows(growth_rows or ["No monetized growth-vector row extracted; keep optionality outside base valuation."]),
            "",
            "## External Cross-Checks",
            "- Peer comparison:",
            *_bullet_rows(peer_rows or ["No compact peer line extracted."]),
            "- Supply-chain position:",
            *_bullet_rows(chain_rows or ["No compact supply-chain line extracted."]),
            "- Product/commodity linkage:",
            *_bullet_rows(commodity_rows or ["No compact product-price line extracted."]),
            "- Investor concern map:",
            *_bullet_rows(interaction_rows or ["No compact investor-interaction line extracted."]),
            "",
            "## Analyst Instructions",
            "- Start the public report with a concise explanation of business model, revenue engine, cost/margin drivers, customers/channels, and capital intensity.",
            "- For multi-business companies, split core mature businesses, cyclical businesses, emerging second curves, geographies, and channels before using a blended PE/PB.",
            "- Treat undisclosed segment margin as a research gap, not as proof of either high quality or poor quality.",
            "- Explain the moat in operational terms: resource ownership, cost curve, customer stickiness, technology/process capability, licenses/regulation, channel control, scale, or balance-sheet endurance.",
            "- If a second curve lacks segment profit, utilization, customer quality, capex, or cash-conversion evidence, keep it in SOTP/scenario value rather than the base case.",
            "",
            "## Underwriting Agenda Seed",
            *(_bullet_rows(_compact_lines(underwriting, limit=6)) if underwriting else ["- No pre-debate underwriting questions were extracted; create company-specific questions from the business model primer."]),
        ]
    )


def get_company_business_model_context(
    ticker: str,
    curr_date: str,
    contexts: Mapping[str, str] | None = None,
) -> str:
    supplied = dict(contexts or {})
    return build_company_business_model_context(
        ticker,
        curr_date,
        filing_intelligence_context=supplied.get("filing_intelligence_context", ""),
        peer_comparison_context=supplied.get("peer_comparison_context", ""),
        supply_chain_comparison_context=supplied.get("supply_chain_comparison_context", ""),
        commodity_context=supplied.get("commodity_context", ""),
        investor_interaction_context=supplied.get("investor_interaction_context", ""),
    )
