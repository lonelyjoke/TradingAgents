"""Deterministic extraction of official earnings-guidance headline metrics.

The raw PDF text used by the research pipeline often wraps a metric name and
its value onto different lines.  Keeping the values in one stable record
prevents later prompt compaction from retaining the label while dropping the
number.
"""

from __future__ import annotations

import re
from typing import Any, Mapping


_VALUE = r"(-?\d[\d,]*(?:\.\d+)?)\s*(万元|亿元|CNY\s*mn)"

_METRIC_LABELS: dict[str, tuple[str, ...]] = {
    "parent_net_profit_cny_mn": (
        "归属于上市公司股东的净利润",
        "归母净利润",
        "parent net profit",
    ),
    "deducted_parent_net_profit_cny_mn": (
        "扣除非经常性损益后的净利润",
        "归属于上市公司股东扣除非经常性损益后的净利润",
        "扣非归母净利润",
        "扣非净利润",
        "deducted parent net profit",
    ),
    "revenue_cny_mn": ("营业收入", "revenue"),
}


def _numbers_with_positions(line: str) -> list[tuple[float, int]]:
    """Return non-percentage numeric tokens with their layout columns."""

    values: list[tuple[float, int]] = []
    for match in re.finditer(r"-?\d[\d,]*(?:\.\d+)?", line or ""):
        tail = line[match.end() : match.end() + 2]
        if "%" in tail:
            continue
        try:
            values.append((float(match.group(0).replace(",", "")), match.start()))
        except ValueError:
            continue
    return values


def _table_unit(lines: list[str], header_index: int) -> str:
    for line in lines[max(0, header_index - 4) : header_index + 3]:
        match = re.search(r"单位\s*[:：]\s*(万元|亿元|CNY\s*mn)", line, re.I)
        if match:
            return match.group(1)
    return ""


def _layout_table_metrics(text: str) -> dict[str, Any]:
    """Parse CNINFO guidance tables while preserving current/prior columns.

    Poppler commonly emits a current-period value on the line immediately
    above its metric label while leaving the prior-period comparison value on
    the metric line.  Binding the label to the nearest value therefore selects
    the wrong column.  This parser uses the ``本报告期``/``上年同期`` header
    positions and never promotes the comparison column to current guidance.
    """

    lines = [raw.rstrip("\r") for raw in (text or "").splitlines()]
    result: dict[str, Any] = {}
    for header_index, header in enumerate(lines):
        if "本报告期" not in header or not re.search(r"上年同期|上期|去年同期", header):
            continue
        current_column = header.find("本报告期")
        prior_match = re.search(r"上年同期|上期|去年同期", header)
        if prior_match is None:
            continue
        prior_column = prior_match.start()
        split_column = (current_column + prior_column) / 2.0
        unit = _table_unit(lines, header_index)
        if not unit:
            continue

        table_end = min(len(lines), header_index + 35)
        for index in range(header_index + 1, table_end):
            line = lines[index]
            if index > header_index + 2 and re.match(r"\s*[二三四五六七八九十]+[、.]", line):
                break
            metric_key = ""
            matched_label = ""
            for candidate_key, labels in _METRIC_LABELS.items():
                for label in labels:
                    if label.lower() in line.lower():
                        metric_key = candidate_key
                        matched_label = label
                        break
                if metric_key:
                    break
            if not metric_key:
                continue

            current_values: list[float] = []
            prior_values: list[float] = []
            for neighbor_index in range(max(header_index + 1, index - 2), min(table_end, index + 2)):
                neighbor = lines[neighbor_index]
                # Do not borrow values from a different metric row.
                if neighbor_index != index and any(
                    label.lower() in neighbor.lower()
                    for labels in _METRIC_LABELS.values()
                    for label in labels
                ):
                    continue
                for value, column in _numbers_with_positions(neighbor):
                    if column < max(0, current_column - 8):
                        continue
                    if column < split_column:
                        current_values.append(value)
                    else:
                        prior_values.append(value)

            # A labelled metric line can contain a prior-period value only;
            # the current-period value is usually the numeric-only line above.
            if current_values:
                result[metric_key] = _to_cny_mn(str(current_values[0]), unit)
                result[f"{metric_key.removesuffix('_cny_mn')}_basis"] = "current_period_table_column"
            if prior_values:
                prior_key = metric_key.replace("_cny_mn", "_prior_cny_mn")
                result[prior_key] = _to_cny_mn(str(prior_values[0]), unit)
            if current_values or prior_values:
                result.setdefault("table_unit", unit)
                result.setdefault("table_layout_control", "current_vs_prior_columns_resolved")
                result.setdefault("table_metric_labels", []).append(matched_label)
        if result:
            break
    return result


def _to_cny_mn(value: str, unit: str) -> float:
    amount = float(value.replace(",", ""))
    normalized = re.sub(r"\s+", "", unit).lower()
    if normalized == "万元":
        return amount / 100.0
    if normalized == "亿元":
        return amount * 100.0
    return amount


def _metric(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        matches = list(re.finditer(label + r".{0,100}?" + _VALUE, text, re.I))
        if matches:
            match = matches[-1]
            return _to_cny_mn(match.group(1), match.group(2))
    return None


def parse_official_guidance_metrics(text: str) -> dict[str, Any]:
    """Return headline guidance metrics in canonical CNY million units.

    This parser is intentionally narrow: it recognizes only explicit official
    period labels and metric names.  It does not infer a full-year value from a
    partial-period preview and it does not turn percentage growth into money.
    """

    raw_text = text or ""
    compact = re.sub(r"\s+", "", raw_text)
    if not compact:
        return {}

    period = ""
    half_years = re.findall(r"(20\d{2})年(?:半年度|上半年)", compact)
    all_years = re.findall(r"(20\d{2})年", compact)
    year = max(half_years or all_years, default="")
    if re.search(r"半年度|上半年", compact):
        period = f"{year}H1" if year else "H1"
    elif re.search(r"前三季度|三季度", compact):
        period = f"{year}Q3" if year else "Q3"
    elif re.search(r"第一季度|一季度", compact):
        period = f"{year}Q1" if year else "Q1"
    elif re.search(r"年度", compact):
        period = f"{year}FY" if year else "FY"

    layout_metrics = _layout_table_metrics(raw_text)
    comparative_table_detected = bool(
        re.search(r"本报告期.{0,80}(?:上年同期|上期|去年同期)", raw_text, re.S)
    )

    # Parse the more specific deducted-profit label first.  Parent profit uses
    # the explicit “的净利润” spelling so it cannot accidentally consume the
    # deducted-profit row.
    deducted_profit = layout_metrics.get("deducted_parent_net_profit_cny_mn")
    if deducted_profit is None and not comparative_table_detected:
        deducted_profit = _metric(
            compact,
            (
                r"归属于上市公司股东扣除非经常性损益后的净利润",
                r"归属于上市公司股东的扣除非经常性损益的净利润",
                r"扣除非经常性损益后的归属于上市公司股东的净利润",
                r"扣非归母净利润",
                r"扣非净利润",
                r"deductedparentnetprofit",
            ),
        )
    parent_profit = layout_metrics.get("parent_net_profit_cny_mn")
    if parent_profit is None and not comparative_table_detected:
        parent_profit = _metric(
            compact,
            (
                r"归属于上市公司股东的净利润",
                r"归母净利润",
                r"parentnetprofit",
            ),
        )
    revenue = layout_metrics.get("revenue_cny_mn")
    if revenue is None and not comparative_table_detected:
        revenue = _metric(compact, (r"营业收入", r"revenue"))

    result: dict[str, Any] = {}
    if period:
        result["period"] = period
    if revenue is not None:
        result["revenue_cny_mn"] = revenue
    if parent_profit is not None:
        result["parent_net_profit_cny_mn"] = parent_profit
    if deducted_profit is not None:
        result["deducted_parent_net_profit_cny_mn"] = deducted_profit
    for key, value in layout_metrics.items():
        if key not in result:
            result[key] = value
    return result if len(result) > (1 if period else 0) else {}


def official_guidance_record(metrics: Mapping[str, Any]) -> str:
    """Render one compaction-safe machine-readable evidence line."""

    if not metrics:
        return ""
    fields = [f"period={metrics.get('period', 'unspecified')}"]
    for key in (
        "revenue_cny_mn",
        "parent_net_profit_cny_mn",
        "deducted_parent_net_profit_cny_mn",
        "revenue_prior_cny_mn",
        "parent_net_profit_prior_cny_mn",
        "deducted_parent_net_profit_prior_cny_mn",
    ):
        value = metrics.get(key)
        if value is not None:
            fields.append(f"{key}={float(value):g}")
    return "Parsed official guidance metrics: " + "; ".join(fields) + "; unit=CNY mn"


def parse_official_guidance_record(text: str) -> dict[str, Any]:
    """Read the stable record after it has travelled through report contexts."""

    records = re.findall(r"Parsed official guidance metrics:[^\n|]*", text or "", re.I)
    if not records:
        return parse_official_guidance_metrics(text)
    result: dict[str, Any] = {}
    for record in records:
        period_match = re.search(r"period=([^;\s]+)", record, re.I)
        if period_match:
            result["period"] = period_match.group(1)
        for key in (
            "revenue_cny_mn",
            "parent_net_profit_cny_mn",
            "deducted_parent_net_profit_cny_mn",
            "revenue_prior_cny_mn",
            "parent_net_profit_prior_cny_mn",
            "deducted_parent_net_profit_prior_cny_mn",
        ):
            match = re.search(rf"{key}=(-?\d+(?:\.\d+)?)", record, re.I)
            if match:
                result[key] = float(match.group(1))
    return result
