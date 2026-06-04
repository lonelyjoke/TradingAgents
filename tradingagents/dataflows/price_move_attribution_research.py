"""Short-horizon price-move attribution for A-share commodity equities."""

from __future__ import annotations

from datetime import datetime, timedelta
import statistics

import pandas as pd

from .commodity_research import (
    _fetch_futures_product,
    _infer_products,
    _query_futures_history,
)
from .tushare_a_stock import (
    TushareDataError,
    _fetch_daily,
    _fetch_daily_basic_latest,
    _fetch_stock_basic,
    _format_value,
    _markdown_table,
    _query_pro_with_fallback,
    is_a_share_symbol,
)
from .tushare_research import _fetch_announcements
from .tushare_research import _fetch_major_news, _fetch_news_feed
from .web_fact_research import _bing_news_rss
from .config import get_config


METAL_EQUITY_BASKETS = {
    "aluminum": (
        "601600.SH",
        "000807.SZ",
        "000933.SZ",
        "600219.SH",
        "002532.SZ",
        "600595.SH",
        "000612.SZ",
    ),
    "copper": ("601899.SH", "600362.SH", "000878.SZ", "000630.SZ", "603993.SH"),
    "precious_metals": ("600547.SH", "000975.SZ", "600489.SH", "600988.SH", "002155.SZ", "002237.SZ"),
    "lithium": ("002460.SZ", "002466.SZ", "000792.SZ", "300390.SZ"),
    "nickel_cobalt": ("603799.SH", "300618.SZ", "002340.SZ"),
    "zinc_lead_tin": ("600497.SH", "000751.SZ", "000960.SZ"),
}


MARKET_INDEXES = {
    "SSE Composite": "000001.SH",
    "CSI 300": "000300.SH",
    "CSI 500": "000905.SH",
}


PRODUCT_QUERY_TERMS = {
    "Aluminum": ("\u94dd", "\u94dd\u4ef7", "\u7535\u89e3\u94dd", "\u6c27\u5316\u94dd", "\u94dd\u5e93\u5b58"),
    "Copper": ("\u94dc", "\u94dc\u4ef7", "\u9634\u6781\u94dc", "\u94dc\u5e93\u5b58"),
    "Gold": ("\u9ec4\u91d1", "\u91d1\u4ef7", "COMEX\u9ec4\u91d1"),
    "Silver": ("\u767d\u94f6", "\u94f6\u4ef7", "COMEX\u767d\u94f6"),
    "Lithium carbonate": ("\u78b3\u9178\u9502", "\u9502\u4ef7", "\u9502\u76d0"),
    "Nickel": ("\u954d", "\u954d\u4ef7"),
    "Zinc": ("\u950c", "\u950c\u4ef7"),
    "Lead": ("\u94c5", "\u94c5\u4ef7"),
    "Tin": ("\u9521", "\u9521\u4ef7"),
    "Industrial silicon": ("\u5de5\u4e1a\u7845", "\u7845\u4ef7"),
}

BASKET_QUERY_TERMS = {
    "aluminum": "\u94dd",
    "copper": "\u94dc",
    "precious_metals": "\u8d35\u91d1\u5c5e",
    "lithium": "\u9502",
    "nickel_cobalt": "\u954d\u94b4",
    "zinc_lead_tin": "\u950c\u94c5\u9521",
}

RUMOR_WORDS = ("\u4f20\u95fb", "\u5e02\u573a\u4f20", "\u6d88\u606f\u79f0", "\u636e\u6089", "\u6216", "\u53ef\u80fd", "\u4f20")
MACRO_WORDS = ("\u7f8e\u8054\u50a8", "\u52a0\u606f", "\u964d\u606f", "\u7f8e\u503a", "\u7f8e\u5143", "\u6c47\u7387", "Fed", "FOMC")
COMMODITY_CRASH_WORDS = ("\u5927\u8dcc", "\u66b4\u8dcc", "\u5d29", "\u8df3\u6c34", "\u91cd\u632b")
FLOW_WORDS = ("\u8d44\u91d1", "\u51c0\u5356\u51fa", "\u878d\u8d44", "\u5317\u5411", "\u91cf\u5316", "\u6b62\u635f", "\u6740\u4f30\u503c", "\u98ce\u9669\u504f\u597d")
WEB_LOW_SIGNAL_MARKERS = (
    "\u767e\u5ea6\u767e\u79d1",
    "\u7ef4\u57fa\u767e\u79d1",
    "\u7ef4\u57fa\u8bcd\u5178",
    "\u4ec0\u4e48\u610f\u601d",
    "\u82f1\u6587",
    "\u7ffb\u8bd1",
    "\u97f3\u6807",
    "\u8bfb\u97f3",
    "\u7528\u6cd5",
    "\u4f8b\u53e5",
    "wikipedia",
    "baike.baidu",
    "iciba.com",
)


def _date_window(curr_date: str, look_back_days: int) -> tuple[str, str]:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - timedelta(days=max(look_back_days + 20, 45))
    return start_dt.strftime("%Y%m%d"), end_dt.strftime("%Y%m%d")


def _pct(current: object, base: object) -> float | None:
    current_num = pd.to_numeric(pd.Series([current]), errors="coerce").iloc[0]
    base_num = pd.to_numeric(pd.Series([base]), errors="coerce").iloc[0]
    if pd.isna(current_num) or pd.isna(base_num) or float(base_num) == 0:
        return None
    return (float(current_num) / float(base_num) - 1.0) * 100.0


def _median(values: list[float | None]) -> float | None:
    clean = [float(value) for value in values if value is not None and not pd.isna(value)]
    return statistics.median(clean) if clean else None


def _std(values: pd.Series) -> float | None:
    clean = pd.to_numeric(values, errors="coerce").dropna()
    if len(clean) < 2:
        return None
    return float(clean.std())


def _basket_name(symbol: str) -> str | None:
    for name, members in METAL_EQUITY_BASKETS.items():
        if symbol in members:
            return name
    return None


def _stock_rows(symbols: list[str], curr_date: str, look_back_days: int) -> pd.DataFrame:
    start, end = _date_window(curr_date, look_back_days)
    rows: list[dict[str, object]] = []
    for symbol in symbols:
        try:
            basic = _fetch_stock_basic(symbol)
            daily = _fetch_daily(symbol, start, end)
            if daily is None or daily.empty:
                raise TushareDataError("no daily rows returned")
            data = daily.sort_values("Date").reset_index(drop=True)
            latest = data.iloc[-1]
            prev = data.iloc[-2] if len(data) >= 2 else data.iloc[0]
            ret_series = pd.to_numeric(data["Close"], errors="coerce").pct_change() * 100.0
            pre_today = data.iloc[:-1] if len(data) > 1 else data
            recent_low = pd.to_numeric(pre_today.tail(30)["Close"], errors="coerce").min()
            recent_high = pd.to_numeric(pre_today.tail(30)["Close"], errors="coerce").max()
            max_close = pd.to_numeric(data["Close"], errors="coerce").max()
            daily_basic = _fetch_daily_basic_latest(symbol, curr_date)
            rows.append(
                {
                    "symbol": symbol,
                    "name": symbol if basic is None else _format_value(basic.get("name")),
                    "basket": _basket_name(symbol) or _format_value(None if basic is None else basic.get("industry")),
                    "latest_date": _format_value(latest.get("Date")),
                    "close": latest.get("Close"),
                    "one_day_pct": latest.get("pct_chg") if "pct_chg" in latest else _pct(latest.get("Close"), prev.get("Close")),
                    "ret_5d_pct": _pct(latest.get("Close"), data.iloc[-6].get("Close")) if len(data) >= 6 else None,
                    "ret_20d_pct": _pct(latest.get("Close"), data.iloc[-21].get("Close")) if len(data) >= 21 else None,
                    "ret_window_pct": _pct(latest.get("Close"), data.iloc[0].get("Close")),
                    "drawdown_from_window_high_pct": _pct(latest.get("Close"), max_close),
                    "pre_today_rebound_from_30d_low_pct": _pct(pre_today.iloc[-1].get("Close"), recent_low) if not pre_today.empty else None,
                    "pre_today_position_in_30d_range_pct": (
                        None
                        if pd.isna(recent_low) or pd.isna(recent_high) or recent_high == recent_low
                        else (float(pre_today.iloc[-1].get("Close")) - float(recent_low)) / (float(recent_high) - float(recent_low)) * 100.0
                    ),
                    "realized_vol_20d_daily_pct": _std(ret_series.tail(20)),
                    "max_abs_day_window_pct": float(ret_series.abs().max()) if not ret_series.dropna().empty else None,
                    "volume_ratio": None if daily_basic is None else daily_basic.get("volume_ratio"),
                    "turnover_rate_f": None if daily_basic is None else daily_basic.get("turnover_rate_f"),
                    "pe_ttm": None if daily_basic is None else daily_basic.get("pe_ttm"),
                    "pb": None if daily_basic is None else daily_basic.get("pb"),
                }
            )
        except Exception as exc:
            rows.append({"symbol": symbol, "name": symbol, "basket": _basket_name(symbol) or "unknown", "error": str(exc)[:160]})
    return pd.DataFrame(rows)


def _index_rows(curr_date: str, look_back_days: int) -> pd.DataFrame:
    start, end = _date_window(curr_date, look_back_days)
    rows = []
    for name, ts_code in MARKET_INDEXES.items():
        try:
            data = _query_pro_with_fallback("index_daily", ts_code=ts_code, start_date=start, end_date=end)
            data = data.sort_values("trade_date").reset_index(drop=True)
            latest = data.iloc[-1]
            rows.append(
                {
                    "index": name,
                    "trade_date": latest.get("trade_date"),
                    "close": latest.get("close"),
                    "one_day_pct": latest.get("pct_chg"),
                    "ret_20d_pct": _pct(latest.get("close"), data.iloc[-21].get("close")) if len(data) >= 21 else None,
                    "ret_window_pct": _pct(latest.get("close"), data.iloc[0].get("close")),
                }
            )
        except Exception as exc:
            rows.append({"index": name, "error": str(exc)[:160]})
    return pd.DataFrame(rows)


def _commodity_rows(symbol: str, curr_date: str, look_back_days: int) -> pd.DataFrame:
    mapping = _infer_products(symbol)
    rows = []
    for product in mapping.get("products", []):
        if product.get("type") != "futures":
            continue
        fetched = _fetch_futures_product(product, curr_date, look_back_days)
        row = {
            "product": product.get("name"),
            "role": product.get("role"),
            "exchange_proxy": fetched.get("latest_contract_or_source"),
            "latest_price": fetched.get("latest_price"),
            "latest_date": fetched.get("latest_date"),
            "window_change": fetched.get("change_over_window"),
            "status": fetched.get("evidence_status"),
            "one_day_pct": None,
            "ret_20d_pct": None,
            "realized_vol_20d_daily_pct": None,
        }
        try:
            ts_code = str(fetched.get("latest_contract_or_source") or "")
            history = _query_futures_history(ts_code, str(product.get("exchange")), *_date_window(curr_date, look_back_days))
            history = history.sort_values("trade_date").reset_index(drop=True)
            returns = pd.to_numeric(history["close"], errors="coerce").pct_change() * 100.0
            row["one_day_pct"] = returns.iloc[-1] if len(returns) else None
            row["ret_20d_pct"] = _pct(history.iloc[-1].get("close"), history.iloc[-21].get("close")) if len(history) >= 21 else None
            row["realized_vol_20d_daily_pct"] = _std(returns.tail(20))
        except Exception as exc:
            row["status"] = f"{row['status']}; history attribution unavailable: {str(exc)[:120]}"
        rows.append(row)
    if not rows:
        rows.append(
            {
                "product": "N/A",
                "role": "N/A",
                "exchange_proxy": "No mapped futures product",
                "latest_price": "N/A",
                "latest_date": "N/A",
                "window_change": "N/A",
                "status": "No commodity mapping; do not attribute the move to commodity prices without evidence.",
                "one_day_pct": None,
                "ret_20d_pct": None,
                "realized_vol_20d_daily_pct": None,
            }
        )
    return pd.DataFrame(rows)


def _recent_event_rows(symbol: str, curr_date: str, days: int = 7) -> pd.DataFrame:
    result = _fetch_announcements(symbol, curr_date, days)
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return pd.DataFrame()
    data = result.copy()
    cols = [col for col in ("ann_date", "title", "url") if col in data.columns]
    return data[cols].head(8)


def _news_probe_terms(symbol: str, target: pd.Series, commodities: pd.DataFrame) -> list[str]:
    terms = [symbol, symbol.split(".")[0], _format_value(target.get("name")), _format_value(target.get("basket"))]
    for product in commodities.get("product", pd.Series(dtype=str)).fillna("").astype(str).tolist():
        if not product or product == "N/A":
            continue
        terms.append(product)
        terms.extend(PRODUCT_QUERY_TERMS.get(product, ()))
    if str(target.get("basket")) == "aluminum":
        terms.extend(["\u6709\u8272\u91d1\u5c5e", "\u94dd\u677f\u5757", "\u4e2d\u56fd\u94dd\u4e1a \u5927\u8dcc", "\u4e2d\u56fd\u94dd\u4e1a \u539f\u56e0"])
    terms.extend(["\u7f8e\u8054\u50a8 \u52a0\u606f \u6709\u8272", "\u7f8e\u5143 \u6709\u8272\u91d1\u5c5e"])
    deduped = []
    for term in terms:
        clean = str(term or "").strip()
        if clean and clean != "N/A" and clean not in deduped:
            deduped.append(clean)
    return deduped[:18]


def _classify_news_topic(text: str) -> str:
    if any(word in text for word in MACRO_WORDS):
        return "macro_rate_fx"
    if any(word in text for word in FLOW_WORDS):
        return "flow_or_sentiment"
    if any(word in text for word in ("\u94dd", "\u94dc", "\u9ec4\u91d1", "\u767d\u94f6", "\u78b3\u9178\u9502", "\u5e93\u5b58", "\u671f\u8d27", "\u5546\u54c1")):
        return "commodity_or_sector"
    if any(word in text for word in ("\u516c\u544a", "\u89e3\u9664\u9650\u552e", "\u56de\u8d2d", "\u51cf\u6301", "\u4e1a\u7ee9", "\u9879\u76ee", "\u6295\u8d44")):
        return "company_event"
    return "unclassified"


def _clean_probe_text(value: object) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return str(value).strip()


def _web_probe_anchor_terms(target: pd.Series, commodities: pd.DataFrame) -> list[str]:
    anchors = [
        _clean_probe_text(target.get("symbol")).split(".")[0],
        _clean_probe_text(target.get("name")),
        _clean_probe_text(target.get("basket")),
        "\u6709\u8272",
        "\u91d1\u5c5e",
    ]
    for product in commodities.get("product", pd.Series(dtype=str)).tolist():
        clean_product = _clean_probe_text(product)
        if clean_product and clean_product != "N/A":
            anchors.append(clean_product)
            anchors.extend(PRODUCT_QUERY_TERMS.get(clean_product, ()))
    deduped = []
    for anchor in anchors:
        clean = _clean_probe_text(anchor)
        if len(clean) >= 2 and clean != "N/A" and clean not in deduped:
            deduped.append(clean)
    return deduped


def _is_low_signal_web_item(text: str) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in WEB_LOW_SIGNAL_MARKERS)


def _is_relevant_web_probe_item(text: str, anchors: list[str]) -> bool:
    if _is_low_signal_web_item(text):
        return False
    return any(anchor in text for anchor in anchors)


def _news_alignment(
    text: str,
    source_type: str,
    commodities: pd.DataFrame,
    attribution_label: str,
) -> tuple[str, str]:
    topic = _classify_news_topic(text)
    commodity_abs = [
        abs(float(value))
        for value in pd.to_numeric(commodities.get("one_day_pct", pd.Series(dtype=float)), errors="coerce").dropna().tolist()
    ]
    max_commodity_abs = max(commodity_abs) if commodity_abs else None
    if source_type == "official_announcement":
        return "confirmed", "Official announcement; hard evidence for event existence, not automatically the cause of the price move."
    if (
        topic == "commodity_or_sector"
        and max_commodity_abs is not None
        and max_commodity_abs <= 2
        and any(word in text for word in COMMODITY_CRASH_WORDS)
    ):
        return "contradicted", "Headline implies commodity/sector price crash, but mapped commodity futures did not move enough."
    if any(word in text for word in RUMOR_WORDS):
        return "weak_rumor", "Contains rumor/possibility wording; use only as a watch item."
    if source_type == "web_search":
        return "weak_rumor", "Web/search corroboration only; not filing or announcement grade."
    if topic == "macro_rate_fx" and "cross_metal_underperformance" in attribution_label:
        return "plausible_but_incomplete", "Macro explanation may affect metals broadly, but target underperformed cross-metal peers, so it is incomplete."
    return "plausible", "News topic is directionally relevant; reconcile with residual table before treating it as a cause."


def _append_probe_row(
    rows: list[dict[str, object]],
    *,
    source_type: str,
    source: str,
    published: object,
    title: object,
    content: object = "",
    link: object = "",
    commodities: pd.DataFrame,
    attribution_label: str,
) -> None:
    clean_title = _clean_probe_text(title)
    clean_content = _clean_probe_text(content)
    text = f"{clean_title} {clean_content}"
    grade, rationale = _news_alignment(text, source_type, commodities, attribution_label)
    rows.append(
        {
            "grade": grade,
            "topic": _classify_news_topic(text),
            "source_type": source_type,
            "source": _clean_probe_text(source),
            "published": _clean_probe_text(published),
            "title": clean_title[:100],
            "rationale": rationale,
            "link": _clean_probe_text(link),
        }
    )


def _news_and_rumor_probe(
    symbol: str,
    curr_date: str,
    target: pd.Series,
    commodities: pd.DataFrame,
    events: pd.DataFrame,
    attribution_label: str,
    days: int = 7,
) -> tuple[pd.DataFrame, list[str]]:
    terms = _news_probe_terms(symbol, target, commodities)
    rows: list[dict[str, object]] = []
    notes: list[str] = []
    event_iter = events.head(8).iterrows() if not events.empty else []
    for _, event in event_iter:
        _append_probe_row(
            rows,
            source_type="official_announcement",
            source="CNINFO/Tushare announcement",
            published=event.get("ann_date"),
            title=event.get("title"),
            link=event.get("url"),
            commodities=commodities,
            attribution_label=attribution_label,
        )

    for label, fetcher, columns in (
        ("tushare_major_news", _fetch_major_news, ("pub_time", "src", "title", "content")),
        ("tushare_news_feed", _fetch_news_feed, ("datetime", "src", "title", "content")),
    ):
        try:
            data = fetcher(terms, curr_date, days, limit=10)
            if isinstance(data, TushareDataError) or data is None or data.empty:
                notes.append(f"{label}: no matching rows or unavailable ({data}).")
                continue
            for _, item in data.head(8).iterrows():
                _append_probe_row(
                    rows,
                    source_type=label,
                    source=item.get(columns[1]),
                    published=item.get(columns[0]),
                    title=item.get(columns[2]),
                    content=item.get(columns[3]),
                    commodities=commodities,
                    attribution_label=attribution_label,
                )
        except Exception as exc:
            notes.append(f"{label}: unavailable ({str(exc)[:160]}).")

    config = get_config()
    if config.get("web_fact_check_enabled", True):
        timeout = float(config.get("web_fact_check_timeout_sec", 6))
        web_anchors = _web_probe_anchor_terms(target, commodities)
        basket_query = BASKET_QUERY_TERMS.get(_clean_probe_text(target.get("basket")), _format_value(target.get("basket")))
        web_queries = [
            f"{_format_value(target.get('name'))} \u5927\u8dcc \u539f\u56e0",
            f"{_format_value(target.get('name'))} \u4e0b\u8dcc \u4f20\u95fb",
            f"{basket_query} \u677f\u5757 \u5927\u8dcc \u539f\u56e0",
        ]
        for query in [q for q in web_queries if "N/A" not in q][:3]:
            try:
                for item in _bing_news_rss(query, timeout=timeout, max_results=3):
                    item_text = " ".join(
                        [
                            _clean_probe_text(item.title),
                            _clean_probe_text(item.snippet),
                            _clean_probe_text(item.link),
                        ]
                    )
                    if not _is_relevant_web_probe_item(item_text, web_anchors):
                        notes.append(f"web_search {query}: skipped low-signal result {_clean_probe_text(item.title)[:60]}.")
                        continue
                    _append_probe_row(
                        rows,
                        source_type="web_search",
                        source=item.source,
                        published=item.published,
                        title=item.title,
                        content=item.snippet,
                        link=item.link,
                        commodities=commodities,
                        attribution_label=attribution_label,
                    )
            except Exception as exc:
                notes.append(f"web_search {query}: unavailable ({str(exc)[:160]}).")
    else:
        notes.append("web_search: disabled by web_fact_check_enabled=false.")

    if not rows:
        return pd.DataFrame(), notes
    data = pd.DataFrame(rows)
    if {"grade", "title"}.issubset(data.columns):
        data = data.drop_duplicates(subset=["grade", "title"], keep="first")
    return data.head(24), notes


def _classification(target: pd.Series, indexes: pd.DataFrame, peers: pd.DataFrame, commodities: pd.DataFrame) -> tuple[str, str]:
    target_ret = pd.to_numeric(pd.Series([target.get("one_day_pct")]), errors="coerce").iloc[0]
    if pd.isna(target_ret):
        return "insufficient_price_data", "Target daily return is unavailable."

    market_ret = _median(indexes.get("one_day_pct", pd.Series(dtype=float)).tolist()) if not indexes.empty else None
    same_basket = str(target.get("basket") or "")
    same_peers = peers[(peers["symbol"] != target.get("symbol")) & (peers["basket"].astype(str) == same_basket)] if "basket" in peers.columns else pd.DataFrame()
    same_peer_median = _median(same_peers.get("one_day_pct", pd.Series(dtype=float)).tolist()) if not same_peers.empty else None
    cross_peer_median = _median(peers[peers["symbol"] != target.get("symbol")].get("one_day_pct", pd.Series(dtype=float)).tolist()) if not peers.empty else None
    commodity_abs = [
        abs(float(value))
        for value in pd.to_numeric(commodities.get("one_day_pct", pd.Series(dtype=float)), errors="coerce").dropna().tolist()
    ]
    max_commodity_abs = max(commodity_abs) if commodity_abs else None

    labels = []
    reasons = []
    if max_commodity_abs is not None and abs(float(target_ret)) >= 5 and max_commodity_abs <= 2:
        labels.append("commodity_equity_divergence")
        reasons.append("Mapped commodity futures did not move enough to explain the equity selloff.")
    if same_peer_median is not None and same_peer_median <= -4:
        labels.append("sector_equity_derating")
        reasons.append("Same-basket equities sold off together, so part of the move is sector equity risk-premium reset.")
    if same_peer_median is not None and float(target_ret) < same_peer_median - 2:
        labels.append("stock_specific_residual_weakness")
        reasons.append("Target underperformed its same-basket peers by more than 2 percentage points.")
    if cross_peer_median is not None and float(target_ret) < cross_peer_median - 2:
        labels.append("cross_metal_underperformance")
        reasons.append("Target also underperformed the broader copper/precious/lithium/small-metal equity reference basket.")
    if target.get("ret_20d_pct") is not None and float(target.get("ret_20d_pct")) < -5:
        labels.append("weak_trend_continuation")
        reasons.append("The stock was already in a weak 20-day trend; the drop looks like failed rebound / trend continuation, not a fresh commodity shock alone.")
    if not labels:
        labels.append("mixed_or_unclassified")
        reasons.append("No single attribution bucket dominates; use the residual table and events for judgment.")
    return " + ".join(labels), " ".join(reasons)


def _diagnostic_rows(target: pd.Series, indexes: pd.DataFrame, peers: pd.DataFrame, commodities: pd.DataFrame) -> pd.DataFrame:
    market_ret = _median(indexes.get("one_day_pct", pd.Series(dtype=float)).tolist()) if not indexes.empty else None
    same_basket = str(target.get("basket") or "")
    same_peers = peers[(peers["symbol"] != target.get("symbol")) & (peers["basket"].astype(str) == same_basket)] if "basket" in peers.columns else pd.DataFrame()
    same_peer_median = _median(same_peers.get("one_day_pct", pd.Series(dtype=float)).tolist()) if not same_peers.empty else None
    broad_peer_median = _median(peers[peers["symbol"] != target.get("symbol")].get("one_day_pct", pd.Series(dtype=float)).tolist()) if not peers.empty else None
    commodity_median = _median(commodities.get("one_day_pct", pd.Series(dtype=float)).tolist()) if not commodities.empty else None
    target_ret = target.get("one_day_pct")
    return pd.DataFrame(
        [
            {"bucket": "market", "proxy": "SSE/CSI median", "one_day_pct": market_ret, "target_minus_proxy": None if market_ret is None else float(target_ret) - market_ret},
            {"bucket": "same_metal_equities", "proxy": same_basket, "one_day_pct": same_peer_median, "target_minus_proxy": None if same_peer_median is None else float(target_ret) - same_peer_median},
            {"bucket": "cross_metal_equities", "proxy": "all configured metal equity baskets", "one_day_pct": broad_peer_median, "target_minus_proxy": None if broad_peer_median is None else float(target_ret) - broad_peer_median},
            {"bucket": "mapped_commodity", "proxy": "mapped futures products", "one_day_pct": commodity_median, "target_minus_proxy": None if commodity_median is None else float(target_ret) - commodity_median},
        ]
    )


def get_price_move_attribution_context(
    ticker: str,
    curr_date: str,
    look_back_days: int = 60,
) -> str:
    """Return a short-horizon drawdown attribution context for A-share names."""
    symbol = str(ticker or "").strip().upper()
    if not is_a_share_symbol(symbol):
        return f"# Price-move attribution context unavailable\n\n- Reason: expected A-share symbol; got {ticker!r}."

    basket = _basket_name(symbol)
    symbols = sorted({symbol, *(METAL_EQUITY_BASKETS.get(basket or "", ())), *sum((list(v) for v in METAL_EQUITY_BASKETS.values()), [])})
    stock_table = _stock_rows(symbols, curr_date, look_back_days)
    target_rows = stock_table[stock_table["symbol"] == symbol]
    if target_rows.empty or "one_day_pct" not in target_rows.columns:
        return f"# Price-move attribution context unavailable\n\n- Reason: no target daily price rows returned for {symbol}."
    target = target_rows.iloc[0]
    indexes = _index_rows(curr_date, look_back_days)
    commodities = _commodity_rows(symbol, curr_date, look_back_days)
    events = _recent_event_rows(symbol, curr_date)
    label, reason = _classification(target, indexes, stock_table, commodities)
    diagnostics = _diagnostic_rows(target, indexes, stock_table, commodities)
    news_probe, probe_notes = _news_and_rumor_probe(
        symbol,
        curr_date,
        target,
        commodities,
        events,
        label,
    )

    peer_cols = [
        "symbol",
        "name",
        "basket",
        "close",
        "one_day_pct",
        "ret_20d_pct",
        "ret_window_pct",
        "drawdown_from_window_high_pct",
        "pre_today_rebound_from_30d_low_pct",
        "realized_vol_20d_daily_pct",
        "volume_ratio",
        "pe_ttm",
        "pb",
    ]
    available_peer_cols = [col for col in peer_cols if col in stock_table.columns]
    sorted_peers = stock_table.copy()
    if "one_day_pct" in sorted_peers.columns:
        sorted_peers["_sort_ret"] = pd.to_numeric(sorted_peers["one_day_pct"], errors="coerce")
        sorted_peers = sorted_peers.sort_values("_sort_ret").drop(columns=["_sort_ret"])

    lines = [
        f"# Price-move attribution context for {symbol} as of {curr_date}",
        "",
        "- Status: ready",
        f"- Company: {_format_value(target.get('name'))}",
        f"- Basket: {_format_value(target.get('basket'))}",
        f"- Attribution label: {label}",
        f"- Attribution reason: {reason}",
        "",
        "## Target Move Snapshot",
        _markdown_table(pd.DataFrame([target.to_dict()])[available_peer_cols]),
        "",
        "## Attribution Residual Table",
        _markdown_table(diagnostics),
        "",
        "## Market Index Reference",
        _markdown_table(indexes),
        "",
        "## Mapped Commodity Reference",
        _markdown_table(commodities),
        "",
        "## Cross-Metal Equity Reference",
        _markdown_table(sorted_peers[available_peer_cols].head(24)),
        "",
        "## Recent Company Event Check",
        _markdown_table(events) if not events.empty else "No recent announcement rows found in the short event window.",
        "",
        "## News & Rumor Probe",
        _markdown_table(news_probe) if not news_probe.empty else "No matching news / rumor probe rows found.",
        "",
        "## News Probe Notes",
        "\n".join(f"- {note}" for note in probe_notes) if probe_notes else "No probe errors.",
        "",
        "## Mispricing Decision Gate",
        "- Do not call a sharp drop `emotionally undervalued` just because commodity futures did not fall.",
        "- A higher-confidence emotion-kill setup needs: weak commodity explanation, no material company event, target residual worse than peers, valuation/NAV/PB support, and stabilization after the forced selling day.",
        "- If PB/NAV or asset-value evidence is still high, classify the move as equity risk-premium reset or failed rebound until valuation support improves.",
        "- If copper/silver/small-metal equities did not sell off as much, highlight cross-metal underperformance as a separate residual instead of hiding it inside generic sector weakness.",
    ]
    return "\n".join(lines)
