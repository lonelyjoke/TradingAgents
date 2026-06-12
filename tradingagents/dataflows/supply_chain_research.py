from __future__ import annotations

from dataclasses import dataclass
from statistics import median

import pandas as pd

from .tushare_a_stock import (
    TushareDataError,
    _fetch_daily_basic_latest,
    _fetch_stock_basic,
    _format_value,
    _format_yyyymmdd,
    _markdown_table,
    is_a_share_symbol,
)
from .tushare_research import (
    _latest_daily_basic_market,
    _merge_peer_financials,
    _score_peers,
)


@dataclass(frozen=True)
class SupplyChainSegment:
    key: str
    name: str
    role: str
    tickers: tuple[str, ...]


@dataclass(frozen=True)
class SupplyChainMap:
    key: str
    name: str
    target_symbols: tuple[str, ...]
    segments: tuple[SupplyChainSegment, ...]


_SUPPLY_CHAIN_MAPS: tuple[SupplyChainMap, ...] = (
    SupplyChainMap(
        key="lithium_battery_chain",
        name="Lithium battery chain",
        target_symbols=(
            "002460.SZ",
            "002466.SZ",
            "000792.SZ",
            "000762.SZ",
            "002738.SZ",
            "300750.SZ",
            "300014.SZ",
            "002074.SZ",
            "300438.SZ",
            "688567.SH",
            "300073.SZ",
            "301358.SZ",
            "300769.SZ",
            "002709.SZ",
            "300568.SZ",
            "300037.SZ",
            "603659.SH",
            "688275.SH",
        ),
        segments=(
            SupplyChainSegment(
                key="upstream_resources",
                name="Upstream resources",
                role="lithium ore / brine / resource ownership",
                tickers=("002460.SZ", "002466.SZ", "000792.SZ", "000762.SZ", "002738.SZ"),
            ),
            SupplyChainSegment(
                key="midstream_materials",
                name="Midstream materials",
                role="cathode / electrolyte / separator / anode materials",
                tickers=("301358.SZ", "300073.SZ", "300769.SZ", "688275.SH", "002709.SZ", "300568.SZ", "300037.SZ", "603659.SH"),
            ),
            SupplyChainSegment(
                key="downstream_cells",
                name="Downstream cells",
                role="battery cell manufacturing and system integration",
                tickers=("300750.SZ", "300014.SZ", "002074.SZ", "300438.SZ", "688567.SH"),
            ),
        ),
    ),
    SupplyChainMap(
        key="wind_power_chain",
        name="Wind-power chain",
        target_symbols=(
            "002202.SZ",
            "300772.SZ",
            "688349.SH",
            "688660.SH",
            "002531.SZ",
            "300129.SZ",
            "300443.SZ",
            "601016.SH",
            "600905.SH",
            "600163.SH",
        ),
        segments=(
            SupplyChainSegment(
                key="components",
                name="Components",
                role="towers / forgings / blades / key parts",
                tickers=("002531.SZ", "300129.SZ", "300443.SZ"),
            ),
            SupplyChainSegment(
                key="turbine_oem",
                name="Turbine OEM",
                role="whole-machine manufacturing",
                tickers=("002202.SZ", "300772.SZ", "688349.SH", "688660.SH"),
            ),
            SupplyChainSegment(
                key="operators",
                name="Operators",
                role="wind-farm ownership and power generation",
                tickers=("601016.SH", "600905.SH", "600163.SH"),
            ),
        ),
    ),
)


def _find_supply_chain(symbol: str) -> SupplyChainMap | None:
    clean = symbol.strip().upper()
    for chain in _SUPPLY_CHAIN_MAPS:
        if clean in chain.target_symbols:
            return chain
    return None


def _supply_chain_filing_probe(symbol: str, curr_date: str) -> str:
    try:
        from .filing_research import _load_financial_report_texts

        _, reports = _load_financial_report_texts(symbol, curr_date, 900)
    except Exception:
        return ""
    return " ".join(text[:5000] for _, text in reports[:3])


def _infer_lithium_chain_segment(symbol: str, curr_date: str = "") -> tuple[SupplyChainMap, SupplyChainSegment, str] | None:
    try:
        basic = _fetch_stock_basic(symbol)
    except Exception:
        basic = None
    if basic is None:
        return None
    haystack = f"{_format_value(basic.get('name'))} {_format_value(basic.get('industry'))} {_supply_chain_filing_probe(symbol, curr_date)}"
    chain = next((item for item in _SUPPLY_CHAIN_MAPS if item.key == "lithium_battery_chain"), None)
    if chain is None:
        return None
    segment_key = ""
    reason = ""
    if any(token in haystack for token in ("锂矿", "盐湖", "锂业", "小金属")):
        segment_key = "upstream_resources"
        reason = "inferred from lithium resource / mining name or industry keywords"
    elif any(token in haystack for token in ("正极", "负极", "材料", "磷酸铁锂", "三元", "隔膜", "电解液", "化工原料")):
        segment_key = "midstream_materials"
        reason = "inferred from lithium-battery material keywords"
    elif any(token in haystack for token in ("电池", "储能", "电芯", "电气设备")):
        segment_key = "downstream_cells"
        reason = "inferred from battery / cell / storage keywords"
    if not segment_key:
        return None
    segment = next((item for item in chain.segments if item.key == segment_key), None)
    if segment is None:
        return None
    return chain, segment, reason


def _chain_universe(chain: SupplyChainMap) -> pd.DataFrame:
    rows = []
    for segment in chain.segments:
        for ticker in segment.tickers:
            basic = _fetch_stock_basic(ticker)
            if basic is None:
                continue
            rows.append(
                {
                    "ts_code": ticker,
                    "segment_key": segment.key,
                    "segment": segment.name,
                    "segment_role": segment.role,
                    "name": basic.get("name"),
                    "industry": basic.get("industry"),
                }
            )
    return pd.DataFrame(rows)


def _summarize_segments(scored: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for segment, group in scored.groupby("segment", dropna=False):
        ranked = group.sort_values("v4_score", ascending=False)
        leader = ranked.iloc[0]
        rows.append(
            {
                "segment": segment,
                "sample_size": len(group),
                "median_v4_score": round(float(median(pd.to_numeric(group["v4_score"], errors="coerce").dropna())), 1)
                if not pd.to_numeric(group["v4_score"], errors="coerce").dropna().empty
                else None,
                "median_pe_ttm": round(float(median(pd.to_numeric(group["pe_ttm"], errors="coerce").dropna())), 1)
                if not pd.to_numeric(group["pe_ttm"], errors="coerce").dropna().empty
                else None,
                "median_pb": round(float(median(pd.to_numeric(group["pb"], errors="coerce").dropna())), 1)
                if not pd.to_numeric(group["pb"], errors="coerce").dropna().empty
                else None,
                "median_roe": round(float(median(pd.to_numeric(group["roe"], errors="coerce").dropna())), 1)
                if not pd.to_numeric(group["roe"], errors="coerce").dropna().empty
                else None,
                "median_netprofit_yoy": round(float(median(pd.to_numeric(group["netprofit_yoy"], errors="coerce").dropna())), 1)
                if not pd.to_numeric(group["netprofit_yoy"], errors="coerce").dropna().empty
                else None,
                "leader": f"{_format_value(leader.get('name'))} ({_format_value(leader.get('ts_code'))})",
                "leader_v4_score": leader.get("v4_score"),
            }
        )
    return pd.DataFrame(rows).sort_values("median_v4_score", ascending=False)


def get_supply_chain_comparison(ticker: str, curr_date: str) -> str:
    """Compare an A-share target against alternative positions within the same industrial chain."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare supply-chain comparison expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    chain = _find_supply_chain(symbol)
    inferred_segment: SupplyChainSegment | None = None
    inferred_reason = ""
    if chain is None:
        inferred = _infer_lithium_chain_segment(symbol, curr_date)
        if inferred is None:
            return (
                f"# Supply-chain position comparison for {symbol} as of {curr_date}\n\n"
                "- No curated or inferred supply-chain map is available for this ticker yet.\n"
                "- Do not invent a cross-position verdict when the value chain has not been explicitly mapped."
            )
        chain, inferred_segment, inferred_reason = inferred

    latest = _fetch_daily_basic_latest(symbol, curr_date)
    if latest is None:
        return f"No daily_basic valuation snapshot found for {symbol} near {curr_date}."
    trade_date = str(latest.get("trade_date"))

    universe = _chain_universe(chain)
    if universe.empty:
        return f"No curated supply-chain universe found for {symbol}."
    if symbol not in set(universe["ts_code"].astype(str)) and inferred_segment is not None:
        basic = _fetch_stock_basic(symbol)
        universe = pd.concat(
            [
                universe,
                pd.DataFrame(
                    [
                        {
                            "ts_code": symbol,
                            "segment_key": inferred_segment.key,
                            "segment": inferred_segment.name,
                            "segment_role": inferred_segment.role,
                            "name": None if basic is None else basic.get("name"),
                            "industry": None if basic is None else basic.get("industry"),
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )

    market_daily = _latest_daily_basic_market(trade_date)
    merged = universe.merge(market_daily, on="ts_code", how="left")
    enriched = _merge_peer_financials(merged, curr_date, len(merged))
    scored = _score_peers(enriched)
    segment_summary = _summarize_segments(scored)

    target_segment = scored.loc[scored["ts_code"] == symbol, "segment"]
    target_segment_name = target_segment.iloc[0] if not target_segment.empty else "Unknown"
    best_segment = segment_summary.iloc[0] if not segment_summary.empty else None
    target_segment_row = (
        segment_summary[segment_summary["segment"] == target_segment_name].iloc[0]
        if target_segment_name in segment_summary["segment"].values
        else None
    )

    display_cols = [
        "ts_code",
        "name",
        "segment",
        "industry",
        "pe_ttm",
        "pb",
        "roe",
        "netprofit_yoy",
        "debt_to_assets",
        "v4_score",
    ]
    lines = [
        f"# Supply-chain position comparison for {symbol} as of {curr_date}",
        "",
        f"- Chain: {chain.name}",
        f"- Target segment: {target_segment_name}",
        f"- Mapping basis: {'curated ticker map' if inferred_segment is None else inferred_reason}",
        f"- Valuation trade date: {_format_yyyymmdd(trade_date)}",
        "- Method: curated chain universe, then cross-position comparison using valuation / quality / growth / leverage metrics.",
        "",
        "## Segment Summary",
        _markdown_table(segment_summary),
        "",
        "## Cross-Position Verdict",
    ]
    if best_segment is None or target_segment_row is None:
        lines.append(
            "Cross-position verdict unavailable because the target or segment summary could not be scored."
        )
    elif best_segment["segment"] == target_segment_name:
        lines.append(
            f"The target sits in the currently strongest sampled segment: {target_segment_name}, "
            f"whose median v4 score is {_format_value(target_segment_row['median_v4_score'])}. "
            "The analyst should still compare individual names before concluding the target itself is the best build."
        )
    else:
        lines.append(
            f"The target sits in {target_segment_name}, while the currently stronger sampled segment is "
            f"{_format_value(best_segment['segment'])} with median v4 score {_format_value(best_segment['median_v4_score'])} "
            f"versus {_format_value(target_segment_row['median_v4_score'])} for the target segment. "
            "This means the better bet may be a different profit pool in the same chain, not merely a different company."
        )

    lines.extend(
        [
            "",
            "## Chain Constituents",
            _markdown_table(scored[display_cols]),
            "",
            "## Analyst Instructions",
            "- First decide which part of the chain owns the best economics today: upstream resource beta, midstream manufacturing spread, or downstream demand capture.",
            "- Then decide whether the target is the best expression of that position; do not confuse a good company with the best chain-level bet.",
            "- Explain why the stronger segment is stronger: pricing power, scarcity, margin capture, balance-sheet quality, valuation, or earnings revision potential.",
            "- If the target sits in a weaker segment, say whether the right action is still to own it, to wait, or to rotate to a better-positioned segment.",
        ]
    )
    return "\n".join(lines)
