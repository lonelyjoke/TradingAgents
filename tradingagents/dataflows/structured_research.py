"""Structured, LLM-assisted research preprocessing.

Markdown remains useful for humans, but it is a poor system-of-record.  This
module converts heterogeneous research contexts into a typed JSON-compatible
bundle before analysts run.  A quick LLM performs semantic work that keyword
rules handle poorly (segment identity, causal mapping, conflicts, and KPE
hypotheses); deterministic code then validates grounding, periods, units, and
financial arithmetic.  If the LLM is unavailable, the deterministic evidence
ledger remains usable and the pipeline degrades without blocking a report.
"""

from __future__ import annotations

import json
import re
from typing import Any, Literal, Mapping

from pydantic import BaseModel, Field

from .research_evidence import extract_evidence_records
from .underwriting_packet import (
    build_company_underwriting_packet,
    compact_underwriting_packet,
)


EvidenceStatus = Literal[
    "reported",
    "calculated",
    "estimated",
    "private_proxy",
    "missing",
    "unverified",
]


class SemanticMetric(BaseModel):
    segment: str = "consolidated"
    variable: str
    value: float | None = None
    value_text: str = ""
    unit: str = ""
    period: str = "unspecified"
    comparison_basis: str = ""
    source_module: str
    source_quote: str
    evidence_status: EvidenceStatus = "unverified"
    direction: str = ""
    materiality: str = ""
    model_role: str = ""


class SegmentSemanticProfile(BaseModel):
    segment: str
    aliases: list[str] = Field(default_factory=list)
    products_or_services: str = ""
    revenue_weight_pct: float | None = None
    gross_profit_or_profit_weight_pct: float | None = None
    business_model: str = ""
    key_drivers: list[str] = Field(default_factory=list)
    prosperity_level: str = "evidence_limited"
    marginal_direction: str = "unknown"
    causal_chain: str = ""
    supporting_metric_refs: list[str] = Field(default_factory=list)
    counterevidence: list[str] = Field(default_factory=list)
    confidence: str = "low"
    missing_inputs: list[str] = Field(default_factory=list)
    revenue_cny_mn: float | None = None
    revenue_reported_value: float | None = None
    revenue_reported_unit: str = ""
    revenue_growth_pct: float | None = None
    gross_margin_pct: float | None = None
    gross_margin_change_pp: float | None = None
    period: str = "unspecified"
    source_module: str = ""
    evidence_quote: str = ""
    extraction_mode: str = "llm_semantic"


class SemanticConflict(BaseModel):
    topic: str
    segment: str = "consolidated"
    claim_a: str
    source_a: str
    claim_b: str
    source_b: str
    conflict_type: str
    required_resolution: str


class KPEHypothesis(BaseModel):
    evidence_id: str
    segment: str = "consolidated"
    variable: str
    direction: str = "unknown"
    horizon: str = ""
    baseline_value: float | None = None
    revised_value: float | None = None
    unit: str = ""
    revenue_base_cny_mn: float | None = None
    revenue_impact_pct: float | None = None
    margin_impact_pp: float | None = None
    incremental_net_margin_pct: float | None = None
    tax_rate_pct: float | None = None
    share_count_mn: float | None = None
    cash_conversion_ratio: float | None = None
    bull_probability_before_pct: float | None = None
    bull_probability_after_pct: float | None = None
    base_probability_before_pct: float | None = None
    base_probability_after_pct: float | None = None
    bear_probability_before_pct: float | None = None
    bear_probability_after_pct: float | None = None
    disposition: str = "watch"
    evidence_quote: str = ""
    verification_gate: str = ""
    missing_inputs: list[str] = Field(default_factory=list)


class SemanticResearchExtraction(BaseModel):
    company_summary: str = ""
    segments: list[SegmentSemanticProfile] = Field(default_factory=list)
    metrics: list[SemanticMetric] = Field(default_factory=list)
    conflicts: list[SemanticConflict] = Field(default_factory=list)
    kpe_hypotheses: list[KPEHypothesis] = Field(default_factory=list)
    preprocessing_notes: list[str] = Field(default_factory=list)


def _normalize(text: str) -> str:
    return re.sub(r"\s+", "", str(text or "")).lower()


def _safe_float(value: float | None) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _known_kpe_rows(text: str) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not re.match(r"^\|\s*KPE\d+\s*\|", line, re.I):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 8:
            continue
        rows[cells[0].upper()] = {
            "date": cells[1],
            "source": cells[2],
            "source_type": cells[3],
            "credibility": cells[4],
            "decision_role": cells[5],
            "evidence": cells[6],
            "verification": cells[7],
            "affected_variable": cells[8] if len(cells) > 8 else "",
            "required_outcome": cells[9] if len(cells) > 9 else "",
        }
    return rows


def _compact_source_payload(
    contexts: Mapping[str, str],
    *,
    max_chars: int = 42000,
) -> dict[str, Any]:
    evidence = extract_evidence_records(contexts, max_records=120)
    evidence_rows = [
        {
            "evidence_id": row.evidence_id,
            "source_module": row.source_module,
            "source_tier": row.source_tier,
            "evidence_type": row.evidence_type,
            "status": row.status,
            "model_variable": row.model_variable,
            "period": row.period,
            "text": row.text,
        }
        for row in evidence
    ]
    semantic_terms = re.compile(
        r"segment|business|revenue|profit|margin|shipment|volume|order|backlog|asp|"
        r"price|capacity|utilization|inventory|cash flow|capex|market share|kpe|"
        r"分部|业务|收入|利润|毛利|出货|销量|订单|排产|价格|产能|利用率|库存|现金流|资本开支|份额|景气",
        re.I,
    )
    snippets: dict[str, list[str]] = {}
    used_chars = len(json.dumps(evidence_rows, ensure_ascii=False))
    per_source_limit = max(1200, (max_chars - used_chars) // max(len(contexts), 1))
    for source, text in contexts.items():
        selected: list[str] = []
        chars = 0
        for raw in (text or "").splitlines():
            line = re.sub(r"\s+", " ", raw.strip())
            if not line or line.startswith("| ---") or not semantic_terms.search(line):
                continue
            wide_segment_row = any(
                marker in line.lower()
                for marker in (
                    "segment economics pack",
                    "filing_segment",
                    "分产品",
                    "主营业务分产品",
                )
            )
            clipped = line[:2400] if wide_segment_row else line[:700]
            if chars + len(clipped) > per_source_limit:
                break
            selected.append(clipped)
            chars += len(clipped)
        if selected:
            snippets[source] = selected
    return {"deterministic_evidence": evidence_rows, "source_snippets": snippets}


def _semantic_prompt(symbol: str, as_of_date: str, payload: dict[str, Any], kpe_rows: dict[str, dict[str, str]]) -> str:
    schema = json.dumps(
        SemanticResearchExtraction.model_json_schema(),
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return f"""You are the semantic preprocessing layer of an institutional equity-research system.

Target: {symbol}
As-of date: {as_of_date}

Convert the supplied evidence into the requested structured schema. This is preprocessing, not an investment recommendation.

Rules:
1. Dynamically identify the company's real business segments; do not rely on a fixed keyword taxonomy when evidence supports a better split.
2. Map every metric to segment, variable, value, unit, period, comparison basis, source module, and an exact source quote.
3. Separate reported facts, reproducible calculations, model estimates, private proxies, missing data, and unverified claims.
4. Identify contradictions across filings, market data, peers, Knowledge Planet, and sell-side research instead of averaging them.
5. For each material segment, explain the demand -> supply/capacity -> price/volume -> utilization/mix -> margin -> cash-flow chain. Distinguish prosperity level from marginal direction.
6. For Knowledge Planet, use only the supplied KPE ids. Map each clue to a segment and model variable. Quantify baseline/revised assumptions and financial bridge inputs only when supported. Never invent a baseline, unit, share count, or revenue base; list it in missing_inputs instead.
7. A private clue may change scenario probability or verification timing before it changes a base-case forecast. Record before/after values only when you can state the reasoning.
8. source_quote must be short and copied from the supplied material. A paraphrase without a quote will be downgraded by deterministic validation.
9. Return exactly one JSON object conforming to the JSON Schema below. Do not return Markdown fences, analysis, commentary, or an empty answer. Use empty arrays and explicit preprocessing_notes when evidence is insufficient.

JSON Schema:
{schema}

Known KPE ledger:
{json.dumps(kpe_rows, ensure_ascii=False)}

Evidence payload:
{json.dumps(payload, ensure_ascii=False)}
"""


def _json_object(text: str) -> dict[str, Any]:
    cleaned = str(text or "").strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.I).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def _invoke_semantic_llm(llm: Any, prompt: str) -> SemanticResearchExtraction:
    if llm is None:
        return SemanticResearchExtraction(preprocessing_notes=["LLM semantic preprocessing unavailable; deterministic fallback used."])
    structured_error: Exception | None = None
    try:
        structured = llm.with_structured_output(SemanticResearchExtraction)
        result = structured.invoke(prompt)
        if isinstance(result, SemanticResearchExtraction):
            return result
        if result is None:
            raise ValueError("structured semantic preprocessing returned no object")
        return SemanticResearchExtraction.model_validate(result)
    except Exception as exc:
        structured_error = exc
        response = llm.invoke(prompt)
        content = getattr(response, "content", response)
        if isinstance(content, Mapping):
            return SemanticResearchExtraction.model_validate(content)
        if isinstance(content, list):
            content = "\n".join(
                str(item.get("text", ""))
                if isinstance(item, dict) and item.get("type") == "text"
                else str(item)
                if isinstance(item, str)
                else ""
                for item in content
            )
        if not str(content or "").strip():
            raise ValueError(
                "semantic free-text fallback returned empty content; "
                f"structured path failed first: {structured_error}"
            )
        try:
            return SemanticResearchExtraction.model_validate(_json_object(str(content)))
        except Exception as fallback_error:
            raise ValueError(
                "semantic fallback did not return schema-valid JSON; "
                f"structured_error={structured_error}; fallback_error={fallback_error}"
            ) from fallback_error


_SEGMENT_NUMERIC_ROW_RE = re.compile(
    r"(?P<name>[\u4e00-\u9fffA-Za-z0-9][^|\n\r%]{1,48}?)\s+"
    r"(?P<revenue>-?[\d,]+(?:\.\d+)?)\s+"
    r"(?P<cost>-?[\d,]+(?:\.\d+)?)\s+"
    r"(?P<margin>-?\d+(?:\.\d+)?)%?\s+"
    r"(?P<growth>-?\d+(?:\.\d+)?)%?\s+"
    r"(?P<cost_growth>-?\d+(?:\.\d+)?)%?\s+"
    r"(?P<margin_change>-?\d+(?:\.\d+)?)%?"
)

# PDF extraction sometimes drops the cost-growth column while preserving the
# other audited fields. Recover that row instead of discarding every later
# product and asking the LLM to reconstruct the table from prose.
_SEGMENT_NUMERIC_COMPACT_ROW_RE = re.compile(
    r"(?P<name>[\u4e00-\u9fffA-Za-z0-9][^|\n\r%]{1,48}?)\s+"
    r"(?P<revenue>-?[\d,]+(?:\.\d+)?)\s+"
    r"(?P<cost>-?[\d,]+(?:\.\d+)?)\s+"
    r"(?P<margin>-?\d+(?:\.\d+)?)%?\s+"
    r"(?P<growth>-?\d+(?:\.\d+)?)%?\s+"
    r"(?P<margin_change>-?\d+(?:\.\d+)?)%?"
)


def _clean_segment_name(value: str) -> str:
    name = re.sub(r"\s+", " ", str(value or "")).strip(" :：-/")
    for marker in ("分产品或服务", "分产品", "分业务", "分行业"):
        if marker in name:
            name = name.rsplit(marker, 1)[-1]
    if ":" in name or "：" in name:
        name = re.split(r"[:：]", name)[-1]
    for header in ("营业收入", "营业成本", "毛利率", "比上年增减", "同比"):
        name = name.replace(header, " ")
    name = re.sub(r"\s+", " ", name).strip()
    name = re.sub(
        r"^(?:项目|营业收入|营业成本|毛利率|主营业务|年度报告|半年度报告)\s*",
        "",
        name,
    ).strip()
    return name[-32:].strip()


def _prosperity_from_reported_growth(
    growth_pct: float,
    margin_change_pp: float,
) -> tuple[str, str]:
    if growth_pct >= 20:
        level = "high"
    elif growth_pct >= 10:
        level = "medium-high"
    elif growth_pct >= 0:
        level = "neutral"
    elif growth_pct >= -10:
        level = "weakening"
    else:
        level = "low"
    if growth_pct >= 10 and margin_change_pp >= -1:
        direction = "improving"
    elif growth_pct < 0 or margin_change_pp <= -2:
        direction = "deteriorating"
    else:
        direction = "stable"
    return level, direction


def _deterministic_segment_profiles(
    contexts: Mapping[str, str],
) -> list[SegmentSemanticProfile]:
    """Recover reported segment economics when semantic extraction is unavailable.

    This parser is intentionally narrow: it only accepts filing-style rows with
    revenue, cost, margin, growth, cost growth, and margin change.  It therefore
    supplies a safe structured fallback without guessing segment identities from
    generic keywords or promotional prose.
    """
    candidates: dict[str, dict[str, Any]] = {}
    excluded = {
        "境内",
        "境外",
        "国内",
        "海外",
        "合计",
        "总计",
        "其他",
    }
    for source_module in ("filing_intelligence", "company_business_model"):
        text = contexts.get(source_module, "")
        for raw in text.splitlines():
            line = re.sub(r"\s+", " ", raw.strip())
            if not line or not any(marker in line for marker in ("分产品", "分业务", "分行业")):
                continue
            if "年度报告" not in line or "半年度报告" in line:
                continue
            matches = list(_SEGMENT_NUMERIC_ROW_RE.finditer(line))
            if not matches:
                matches = list(_SEGMENT_NUMERIC_COMPACT_ROW_RE.finditer(line))
            for match in matches:
                name = _clean_segment_name(match.group("name"))
                if not name or name in excluded or len(name) < 2:
                    continue
                revenue = float(match.group("revenue").replace(",", ""))
                cost = float(match.group("cost").replace(",", ""))
                margin = float(match.group("margin"))
                growth = float(match.group("growth"))
                margin_change = float(match.group("margin_change"))
                if revenue <= 0 or not (-100.0 <= margin <= 100.0):
                    continue
                candidates.setdefault(
                    _normalize(name),
                    {
                        "name": name,
                        "revenue": revenue,
                        "cost": cost,
                        "margin": margin,
                        "growth": growth,
                        "margin_change": margin_change,
                        "source_module": source_module,
                        "quote": line[:2400],
                    },
                )
    if not candidates:
        return []

    rows = list(candidates.values())
    revenue_total = sum(row["revenue"] for row in rows)
    gross_profit_total = sum(
        row["revenue"] * row["margin"] / 100.0 for row in rows
    )
    result: list[SegmentSemanticProfile] = []
    for row in rows:
        level, direction = _prosperity_from_reported_growth(
            row["growth"], row["margin_change"]
        )
        result.append(
            SegmentSemanticProfile(
                segment=row["name"],
                revenue_weight_pct=(
                    row["revenue"] / revenue_total * 100.0
                    if revenue_total > 0
                    else None
                ),
                gross_profit_or_profit_weight_pct=(
                    row["revenue"]
                    * row["margin"]
                    / 100.0
                    / gross_profit_total
                    * 100.0
                    if gross_profit_total > 0
                    else None
                ),
                business_model="filing-reported business segment",
                prosperity_level=level,
                marginal_direction=direction,
                causal_chain=(
                    "Reported segment revenue growth and gross-margin movement are available; "
                    "demand, supply/capacity, ASP, utilization, working-capital and cash links "
                    "still require semantic and source cross-checking."
                ),
                counterevidence=[
                    "A filing growth rate alone cannot establish full segment prosperity."
                ],
                confidence="medium",
                missing_inputs=[
                    "dated demand/order evidence",
                    "capacity/utilization evidence",
                    "ASP/price evidence",
                    "segment cash-conversion evidence",
                ],
                revenue_cny_mn=None,
                revenue_reported_value=row["revenue"],
                revenue_reported_unit="filing table unit not explicit in extracted row",
                revenue_growth_pct=row["growth"],
                gross_margin_pct=row["margin"],
                gross_margin_change_pp=row["margin_change"],
                period="annual filing",
                source_module=row["source_module"],
                evidence_quote=row["quote"],
                extraction_mode="deterministic_filing_row",
            )
        )
    return sorted(
        result,
        key=lambda item: item.revenue_reported_value or 0.0,
        reverse=True,
    )


def _quote_grounded(quote: str, source_text: str) -> bool:
    needle = _normalize(quote)
    haystack = _normalize(source_text)
    return bool(needle and len(needle) >= 8 and needle in haystack)


def _validate_probability_triplet(hypothesis: KPEHypothesis, suffix: str) -> bool:
    values = [
        _safe_float(getattr(hypothesis, f"bull_probability_{suffix}_pct")),
        _safe_float(getattr(hypothesis, f"base_probability_{suffix}_pct")),
        _safe_float(getattr(hypothesis, f"bear_probability_{suffix}_pct")),
    ]
    supplied = [value for value in values if value is not None]
    return not supplied or (len(supplied) == 3 and abs(sum(supplied) - 100.0) <= 0.6)


def _quantify_kpe(hypothesis: KPEHypothesis, known: dict[str, str]) -> dict[str, Any]:
    baseline = _safe_float(hypothesis.baseline_value)
    revised = _safe_float(hypothesis.revised_value)
    assumption_delta = revised - baseline if baseline is not None and revised is not None else None

    revenue_delta: float | None = None
    profit_delta: float | None = None
    eps_delta: float | None = None
    fcf_delta: float | None = None
    missing = list(dict.fromkeys(hypothesis.missing_inputs))

    revenue_base = _safe_float(hypothesis.revenue_base_cny_mn)
    revenue_impact_pct = _safe_float(hypothesis.revenue_impact_pct)
    margin_impact_pp = _safe_float(hypothesis.margin_impact_pp)
    incremental_margin = _safe_float(hypothesis.incremental_net_margin_pct)
    tax_rate = _safe_float(hypothesis.tax_rate_pct)
    share_count = _safe_float(hypothesis.share_count_mn)
    cash_conversion = _safe_float(hypothesis.cash_conversion_ratio)

    if revenue_base is not None and revenue_impact_pct is not None:
        revenue_delta = revenue_base * revenue_impact_pct / 100.0
        if incremental_margin is not None:
            profit_delta = revenue_delta * incremental_margin / 100.0
        else:
            missing.append("incremental_net_margin_pct")
    elif revenue_impact_pct is not None:
        missing.append("revenue_base_cny_mn")

    if revenue_base is not None and margin_impact_pp is not None:
        margin_profit_delta = revenue_base * margin_impact_pp / 100.0
        if tax_rate is not None:
            margin_profit_delta *= 1.0 - tax_rate / 100.0
        profit_delta = (profit_delta or 0.0) + margin_profit_delta
    elif margin_impact_pp is not None:
        missing.append("revenue_base_cny_mn")

    variable_lower = hypothesis.variable.lower()
    if profit_delta is None and assumption_delta is not None and any(
        token in variable_lower for token in ("profit", "net income", "净利润", "归母")
    ) and hypothesis.unit.lower() in {"cny mn", "cny_mn", "百万元", "百万人民币"}:
        profit_delta = assumption_delta

    if profit_delta is not None:
        if share_count is not None and share_count > 0:
            eps_delta = profit_delta / share_count
        else:
            missing.append("share_count_mn")
        if cash_conversion is not None:
            fcf_delta = profit_delta * cash_conversion
        else:
            missing.append("cash_conversion_ratio")

    probability_valid = _validate_probability_triplet(hypothesis, "before") and _validate_probability_triplet(hypothesis, "after")
    if not probability_valid:
        missing.append("valid bull/base/bear probability triplets summing to 100%")

    if any(value is not None for value in (revenue_delta, profit_delta, eps_delta, fcf_delta)):
        status = "quantified"
    elif assumption_delta is not None:
        status = "assumption_quantified_financial_bridge_missing"
    elif any(
        getattr(hypothesis, field) is not None
        for field in (
            "bull_probability_before_pct",
            "bull_probability_after_pct",
            "base_probability_before_pct",
            "base_probability_after_pct",
            "bear_probability_before_pct",
            "bear_probability_after_pct",
        )
    ) and probability_valid:
        status = "probability_only"
    else:
        status = "unquantified"

    disposition = str(hypothesis.disposition or "watch").strip().lower()
    if status == "quantified":
        decision_outcome = (
            "model assumption changed through the deterministic financial bridge"
        )
    elif status == "probability_only":
        decision_outcome = (
            "scenario probabilities changed; use only the validated before/after triplets"
        )
    elif disposition in {"reject", "rejected", "不采纳", "拒绝"}:
        decision_outcome = "rejected: no model, valuation, rating, or sizing impact"
    else:
        decision_outcome = (
            "unchanged/watch: no model assumption or scenario probability change until "
            + (hypothesis.verification_gate or known.get("verification", "objective verification"))
        )

    return {
        **hypothesis.model_dump(),
        "known_kpe": known,
        "assumption_delta": assumption_delta,
        "revenue_delta_cny_mn": revenue_delta,
        "parent_profit_delta_cny_mn": profit_delta,
        "eps_delta_cny": eps_delta,
        "fcf_delta_cny_mn": fcf_delta,
        "probability_triplets_valid": probability_valid,
        "quantification_status": status,
        "decision_outcome": decision_outcome,
        "missing_inputs": list(dict.fromkeys(missing)),
    }


def _segment_match_tokens(segment: SegmentSemanticProfile) -> list[str]:
    values = [segment.segment, *segment.aliases]
    tokens: list[str] = []
    for value in values:
        cleaned = re.sub(
            r"(?:系统|业务|产品|服务|板块|segment|business|division)$",
            "",
            str(value or "").strip(),
            flags=re.I,
        )
        if len(cleaned) >= 2:
            tokens.append(cleaned.lower())
        core_token = re.sub(
            r"(?:电池|材料|设备|系统|业务|产品|服务|板块)",
            "",
            cleaned,
        ).strip()
        if len(core_token) >= 2:
            tokens.append(core_token.lower())
        if len(str(value or "").strip()) >= 2:
            tokens.append(str(value).strip().lower())
    return list(dict.fromkeys(tokens))


def _match_kpe_segment(
    known: Mapping[str, str],
    segments: list[SegmentSemanticProfile],
) -> str:
    evidence = " ".join(
        str(known.get(key, ""))
        for key in ("evidence", "affected_variable", "verification")
    ).lower()
    matches: list[tuple[int, str]] = []
    for segment in segments:
        score = sum(len(token) for token in _segment_match_tokens(segment) if token in evidence)
        if score:
            matches.append((score, segment.segment))
    if not matches:
        return "consolidated/unmapped"
    matches.sort(reverse=True)
    return matches[0][1]


def build_structured_research_bundle(
    symbol: str,
    as_of_date: str,
    *,
    contexts: Mapping[str, str],
    llm: Any = None,
    underwriting_llm: Any = None,
    enable_llm: bool = True,
    enable_underwriting: bool = True,
    max_prompt_chars: int = 42000,
    underwriting_prompt_max_chars: int = 60000,
) -> dict[str, Any]:
    payload = _compact_source_payload(contexts, max_chars=max_prompt_chars)
    kpe_rows = _known_kpe_rows(contexts.get("knowledge_planet", ""))
    deterministic_segments = _deterministic_segment_profiles(contexts)
    semantic = SemanticResearchExtraction()
    mode = "deterministic_only"
    errors: list[str] = []
    if enable_llm and llm is not None:
        try:
            semantic = _invoke_semantic_llm(
                llm,
                _semantic_prompt(symbol, as_of_date, payload, kpe_rows),
            )
            mode = "llm_semantic_plus_deterministic_validation"
        except Exception as exc:
            errors.append(f"semantic LLM failed: {exc}")

    if not semantic.segments and deterministic_segments:
        semantic.segments = deterministic_segments
        errors.append(
            "semantic segment extraction unavailable; recovered filing-reported segment rows deterministically"
        )
    elif deterministic_segments:
        semantic_names = {_normalize(segment.segment) for segment in semantic.segments}
        for segment in deterministic_segments:
            if _normalize(segment.segment) not in semantic_names:
                semantic.segments.append(segment)

    validated_metrics: list[dict[str, Any]] = []
    for metric in semantic.metrics:
        source_text = contexts.get(metric.source_module, "")
        grounded = _quote_grounded(metric.source_quote, source_text)
        item = metric.model_dump()
        item["grounding_status"] = "grounded_quote" if grounded else "unverified_quote"
        if not grounded:
            item["evidence_status"] = "unverified"
        if not metric.period or metric.period == "unspecified":
            item["control_flags"] = ["missing_period"]
        else:
            item["control_flags"] = []
        validated_metrics.append(item)

    quantified_kpe: list[dict[str, Any]] = []
    quantified_ids: set[str] = set()
    for hypothesis in semantic.kpe_hypotheses:
        evidence_id = hypothesis.evidence_id.upper()
        if evidence_id not in kpe_rows:
            errors.append(f"ignored unknown KPE id: {hypothesis.evidence_id}")
            continue
        grounded = _quote_grounded(hypothesis.evidence_quote, kpe_rows[evidence_id]["evidence"])
        quantified = _quantify_kpe(hypothesis, kpe_rows[evidence_id])
        quantified["grounding_status"] = "grounded_quote" if grounded else "unverified_quote"
        if not grounded:
            quantified["quantification_status"] = "unverified"
        quantified_kpe.append(quantified)
        quantified_ids.add(evidence_id)

    for evidence_id, known in kpe_rows.items():
        if evidence_id in quantified_ids:
            continue
        quantified_kpe.append(
            {
                "evidence_id": evidence_id,
                "segment": _match_kpe_segment(known, semantic.segments),
                "variable": known.get("affected_variable") or "unmapped",
                "direction": "unknown",
                "horizon": "",
                "baseline_value": None,
                "revised_value": None,
                "unit": "",
                "assumption_delta": None,
                "revenue_delta_cny_mn": None,
                "parent_profit_delta_cny_mn": None,
                "eps_delta_cny": None,
                "fcf_delta_cny_mn": None,
                "quantification_status": "watch_no_model_change",
                "grounding_status": "ledger_only",
                "known_kpe": known,
                "verification_gate": known.get("verification", ""),
                "disposition": "watch_unchanged",
                "decision_outcome": (
                    "unchanged/watch: no model assumption, scenario probability, valuation, "
                    "rating, or sizing change until "
                    + (known.get("verification") or "objective verification")
                ),
                "missing_inputs": [
                    "baseline and revised operating assumption",
                    "unit and financial transmission inputs",
                ],
            }
        )

    bundle: dict[str, Any] = {
        "schema_version": 3,
        "symbol": symbol,
        "as_of_date": str(as_of_date),
        "preprocessing_mode": mode,
        "company_summary": semantic.company_summary,
        "segments": [segment.model_dump() for segment in semantic.segments],
        "semantic_metrics": validated_metrics,
        "deterministic_evidence": payload["deterministic_evidence"],
        "conflicts": [conflict.model_dump() for conflict in semantic.conflicts],
        "kpe_impacts": quantified_kpe,
        "known_kpe_ledger": kpe_rows,
        "preprocessing_notes": [*semantic.preprocessing_notes, *errors],
    }
    bundle["underwriting_packet"] = build_company_underwriting_packet(
        symbol,
        str(as_of_date),
        contexts=contexts,
        structured_research=bundle,
        llm=underwriting_llm or llm,
        enable_llm=enable_underwriting,
        max_prompt_chars=underwriting_prompt_max_chars,
    )
    return bundle


def compact_structured_research_for_prompt(
    bundle: Mapping[str, Any] | None,
    *,
    max_chars: int = 18000,
) -> str:
    if not bundle:
        return "{}"
    compact = {
        "schema_version": bundle.get("schema_version"),
        "symbol": bundle.get("symbol"),
        "as_of_date": bundle.get("as_of_date"),
        "preprocessing_mode": bundle.get("preprocessing_mode"),
        "company_summary": bundle.get("company_summary"),
        "segments": list(bundle.get("segments", []))[:10],
        "semantic_metrics": list(bundle.get("semantic_metrics", []))[:40],
        "deterministic_evidence": list(bundle.get("deterministic_evidence", []))[:35],
        "conflicts": list(bundle.get("conflicts", []))[:12],
        "kpe_impacts": list(bundle.get("kpe_impacts", []))[:12],
        "preprocessing_notes": list(bundle.get("preprocessing_notes", []))[:8],
        "underwriting_packet": compact_underwriting_packet(
            bundle.get("underwriting_packet", {})
        ),
    }
    rendered = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
    if len(rendered) <= max_chars:
        return rendered
    for key in ("deterministic_evidence", "semantic_metrics", "conflicts", "kpe_impacts", "segments"):
        values = compact.get(key)
        if not isinstance(values, list):
            continue
        while values and len(rendered) > max_chars:
            values.pop()
            rendered = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
    if len(rendered) > max_chars and isinstance(compact.get("underwriting_packet"), dict):
        packet = compact["underwriting_packet"]
        for key in ("preprocessing_notes", "analyst_instructions", "reconciliation_checks"):
            packet.pop(key, None)
        for key in ("underwriting_questions", "evidence_change_rules", "scenarios", "forecast_lines", "segment_models"):
            values = packet.get(key)
            if not isinstance(values, list):
                continue
            while values and len(rendered) > max_chars:
                values.pop()
                rendered = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
    return rendered
