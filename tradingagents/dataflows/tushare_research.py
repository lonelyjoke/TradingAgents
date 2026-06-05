from __future__ import annotations

from datetime import datetime, timedelta
import html
import re
from typing import Iterable

import pandas as pd
import requests
from dateutil.relativedelta import relativedelta

from .industry_classifier import is_banking_entity
from .tushare_a_stock import (
    TushareDataError,
    _fetch_daily_basic_latest,
    _fetch_fina_indicator,
    _fetch_stock_basic,
    _format_value,
    _format_yyyymmdd,
    _get_pro_client,
    _markdown_table,
    _query_pro_with_fallback,
    _select_existing,
    _to_tushare_date,
    is_a_share_symbol,
)

CNINFO_ANNOUNCEMENT_QUERY_URL = "http://www.cninfo.com.cn/new/hisAnnouncement/query"
CNINFO_STATIC_BASE_URL = "http://static.cninfo.com.cn/"
CNINFO_FINANCIAL_REPORT_CATEGORIES = (
    "category_ndbg_szsh",
    "category_bndbg_szsh",
    "category_yjdbg_szsh",
    "category_sjdbg_szsh",
)

BAIJIU_PEER_FALLBACK = {
    "600519.SH": "贵州茅台",
    "000858.SZ": "五粮液",
    "000568.SZ": "泸州老窖",
    "600809.SH": "山西汾酒",
    "002304.SZ": "洋河股份",
    "000596.SZ": "古井贡酒",
    "603369.SH": "今世缘",
    "600779.SH": "水井坊",
    "600702.SH": "舍得酒业",
    "603198.SH": "迎驾贡酒",
    "603589.SH": "口子窖",
    "600559.SH": "老白干酒",
    "000799.SZ": "酒鬼酒",
    "600197.SH": "伊力特",
}


def _date_window(curr_date: str, look_back_days: int) -> tuple[datetime, datetime, str, str]:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - timedelta(days=max(1, look_back_days))
    return start_dt, end_dt, start_dt.strftime("%Y%m%d"), end_dt.strftime("%Y%m%d")


def _datetime_window(curr_date: str, look_back_days: int) -> tuple[str, str]:
    start_dt, end_dt, _, _ = _date_window(curr_date, look_back_days)
    return start_dt.strftime("%Y-%m-%d 00:00:00"), end_dt.strftime("%Y-%m-%d 23:59:59")


def _query_optional_api(api_name: str, **kwargs) -> pd.DataFrame:
    data = _query_pro_with_fallback(api_name, empty_ok=True, **kwargs)
    if data is None:
        return pd.DataFrame()
    return data


def _safe_optional_query(api_name: str, **kwargs) -> pd.DataFrame | TushareDataError:
    try:
        return _query_optional_api(api_name, **kwargs)
    except Exception as exc:
        return TushareDataError(f"{api_name} unavailable: {exc}")


def _format_error(label: str, result: pd.DataFrame | TushareDataError) -> str:
    if isinstance(result, TushareDataError):
        return f"{label} unavailable: {result}"
    return f"{label} unavailable."


def _company_terms(symbol: str) -> tuple[pd.Series | None, list[str]]:
    basic = _fetch_stock_basic(symbol)
    terms = [symbol, symbol.split(".")[0]]
    if basic is not None:
        for col in ("name", "industry"):
            value = basic.get(col)
            if value is not None and not pd.isna(value):
                terms.append(str(value))
    deduped = []
    for term in terms:
        clean = str(term).strip()
        if clean and clean not in deduped:
            deduped.append(clean)
    return basic, deduped


def _filter_by_terms(data: pd.DataFrame, terms: Iterable[str], columns: Iterable[str]) -> pd.DataFrame:
    if data is None or data.empty:
        return pd.DataFrame()
    terms = [str(term).strip() for term in terms if str(term).strip()]
    if not terms:
        return data.copy()
    usable_cols = [col for col in columns if col in data.columns]
    if not usable_cols:
        return data

    mask = pd.Series(False, index=data.index)
    for col in usable_cols:
        series = data[col].fillna("").astype(str)
        for term in terms:
            if term:
                mask = mask | series.str.contains(term, case=False, regex=False)
    return data[mask].copy()


def _sort_by_existing_date(data: pd.DataFrame, date_cols: list[str]) -> pd.DataFrame:
    if data is None or data.empty:
        return pd.DataFrame()
    for col in date_cols:
        if col in data.columns:
            return data.sort_values(col, ascending=False)
    return data


def _cninfo_exchange_params(symbol: str) -> tuple[str, str]:
    if symbol.endswith(".SH"):
        return "sse", "sh"
    return "szse", "sz"


def _cninfo_stock_query_values(symbol: str) -> tuple[str, ...]:
    stock_code = symbol.split(".")[0]
    if symbol.endswith(".SH"):
        org_id = f"gssh{stock_code.zfill(7)}"
    else:
        org_id = f"gssz{stock_code.zfill(7)}"
    return (f"{stock_code},{org_id}", stock_code)


def _clean_cninfo_title(value: object) -> str:
    text = html.unescape(str(value or ""))
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _format_cninfo_ann_date(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    text = str(value).strip()
    try:
        if text.isdigit():
            timestamp = int(text)
            if timestamp > 10_000_000_000:
                timestamp = timestamp // 1000
            return datetime.fromtimestamp(timestamp).strftime("%Y%m%d")
        return datetime.strptime(text[:10], "%Y-%m-%d").strftime("%Y%m%d")
    except Exception:
        return text[:8]


def _cninfo_announcement_url(adjunct_url: object) -> str:
    path = str(adjunct_url or "").strip()
    if not path:
        return ""
    if path.startswith(("http://", "https://")):
        return path
    return CNINFO_STATIC_BASE_URL + path.lstrip("/")


def _parse_cninfo_announcements(payload: dict, symbol: str) -> pd.DataFrame:
    announcements = payload.get("announcements") or []
    rows = []
    for item in announcements:
        title = _clean_cninfo_title(item.get("announcementTitle"))
        if not title:
            continue
        rows.append(
            {
                "ann_date": _format_cninfo_ann_date(item.get("announcementTime")),
                "ts_code": symbol,
                "name": str(item.get("secName") or "").strip(),
                "title": title,
                "url": _cninfo_announcement_url(item.get("adjunctUrl")),
                "rec_time": _format_cninfo_ann_date(item.get("announcementTime")),
            }
        )
    if not rows:
        return pd.DataFrame(columns=["ann_date", "ts_code", "name", "title", "url", "rec_time"])
    return pd.DataFrame(rows)


def _fetch_cninfo_announcements(
    symbol: str,
    curr_date: str,
    look_back_days: int,
    *,
    categories: tuple[str, ...] | None = None,
) -> pd.DataFrame | TushareDataError:
    start_dt, end_dt, _, _ = _date_window(curr_date, look_back_days)
    column, plate = _cninfo_exchange_params(symbol)
    se_date = f"{start_dt.strftime('%Y-%m-%d')}~{end_dt.strftime('%Y-%m-%d')}"
    page_size = 30
    max_pages = 10 if look_back_days >= 365 else 4
    rows = []
    session = requests.Session()
    categories_to_try = categories or ("",)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://www.cninfo.com.cn/new/commonUrl/pageOfSearch",
        "User-Agent": "Mozilla/5.0 TradingAgents cninfo-announcement-fallback",
        "X-Requested-With": "XMLHttpRequest",
    }

    try:
        for stock_query in _cninfo_stock_query_values(symbol):
            stock_rows_start = len(rows)
            for category in categories_to_try:
                for page_num in range(1, max_pages + 1):
                    data = {
                        "stock": stock_query,
                        "searchkey": "",
                        "plate": plate,
                        "category": category,
                        "trade": "",
                        "column": column,
                        "columnTitle": "history",
                        "pageNum": str(page_num),
                        "pageSize": str(page_size),
                        "tabName": "fulltext",
                        "sortName": "",
                        "sortType": "",
                        "limit": "",
                        "showTitle": "",
                        "seDate": se_date,
                    }
                    response = session.post(
                        CNINFO_ANNOUNCEMENT_QUERY_URL,
                        data=data,
                        headers=headers,
                        timeout=20,
                    )
                    response.raise_for_status()
                    page = _parse_cninfo_announcements(response.json(), symbol)
                    if page.empty:
                        break
                    rows.append(page)
                    if len(page) < page_size:
                        break
            if len(rows) > stock_rows_start:
                break
    except Exception as exc:
        return TushareDataError(f"cninfo announcement fallback unavailable: {exc}")

    if not rows:
        return pd.DataFrame(columns=["ann_date", "ts_code", "name", "title", "url", "rec_time"])

    data = pd.concat(rows, ignore_index=True)
    if "title" in data.columns:
        data = data.drop_duplicates(subset=["ann_date", "title", "url"], keep="first")
    return _sort_by_existing_date(data, ["ann_date", "rec_time"])


def _fetch_announcements(symbol: str, curr_date: str, look_back_days: int) -> pd.DataFrame | TushareDataError:
    _, _, start, end = _date_window(curr_date, look_back_days)
    fields = "ann_date,ts_code,name,title,url,rec_time"
    result = _safe_optional_query(
        "anns_d",
        ts_code=symbol,
        start_date=start,
        end_date=end,
        fields=fields,
    )
    if isinstance(result, TushareDataError):
        result = _safe_optional_query(
            "anns",
            ts_code=symbol,
            start_date=start,
            end_date=end,
            fields=fields,
        )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        fallback = _fetch_cninfo_announcements(symbol, curr_date, look_back_days)
        if not isinstance(fallback, TushareDataError):
            return fallback
        if isinstance(result, TushareDataError):
            return TushareDataError(f"{result}; {fallback}")
        return fallback
    return _sort_by_existing_date(result, ["ann_date", "rec_time"])


def _fetch_major_news(terms: list[str], curr_date: str, look_back_days: int, limit: int = 20) -> pd.DataFrame | TushareDataError:
    start, end = _datetime_window(curr_date, look_back_days)
    result = _safe_optional_query(
        "major_news",
        src="",
        start_date=start,
        end_date=end,
        fields="title,content,pub_time,src",
    )
    if isinstance(result, TushareDataError):
        return result
    filtered = _filter_by_terms(result, terms, ["title", "content", "src"])
    filtered = _sort_by_existing_date(filtered, ["pub_time"])
    return filtered.head(limit)


def _fetch_news_feed(terms: list[str], curr_date: str, look_back_days: int, limit: int = 20) -> pd.DataFrame | TushareDataError:
    start, end = _datetime_window(curr_date, look_back_days)
    sources = ["sina", "10jqka", "eastmoney", "yuncaijing", "wallstreetcn"]
    frames = []
    errors = []
    for src in sources:
        result = _safe_optional_query(
            "news",
            src=src,
            start_date=start,
            end_date=end,
            fields="datetime,content,title,channels",
        )
        if isinstance(result, TushareDataError):
            errors.append(str(result))
            continue
        if result is not None and not result.empty:
            result = result.copy()
            result["src"] = src
            frames.append(result)

    if not frames:
        return TushareDataError("; ".join(errors) if errors else "news returned no data.")

    data = pd.concat(frames, ignore_index=True)
    filtered = _filter_by_terms(data, terms, ["title", "content", "channels"])
    filtered = _sort_by_existing_date(filtered, ["datetime"])
    if "title" in filtered.columns:
        filtered = filtered.drop_duplicates(subset=["title"], keep="first")
    return filtered.head(limit)


def _fetch_general_major_news(curr_date: str, look_back_days: int, limit: int) -> pd.DataFrame | TushareDataError:
    start, end = _datetime_window(curr_date, look_back_days)
    result = _safe_optional_query(
        "major_news",
        src="",
        start_date=start,
        end_date=end,
        fields="title,content,pub_time,src",
    )
    if isinstance(result, TushareDataError):
        return result
    result = _sort_by_existing_date(result, ["pub_time"])
    return result.head(limit)


def _fetch_cctv_policy(terms: list[str], curr_date: str, look_back_days: int, limit: int = 20) -> pd.DataFrame | TushareDataError:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    rows = []
    days_to_scan = min(max(1, look_back_days), 14)
    last_error = None
    for offset in range(days_to_scan):
        day = end_dt - timedelta(days=offset)
        result = _safe_optional_query("cctv_news", date=day.strftime("%Y%m%d"))
        if isinstance(result, TushareDataError):
            last_error = result
            continue
        if result is not None and not result.empty:
            rows.append(result)

    if not rows:
        return last_error or pd.DataFrame()

    data = pd.concat(rows, ignore_index=True)
    filtered = _filter_by_terms(data, terms, ["title", "content"])
    filtered = _sort_by_existing_date(filtered, ["date"])
    return filtered.head(limit)


def _format_event_table(data: pd.DataFrame, columns: list[str], limit: int) -> str:
    if data is None or data.empty:
        return "No matching records found."
    selected = _select_existing(data.head(limit), columns)
    return _markdown_table(selected)


def _classify_announcement(title: str) -> str:
    text = str(title or "")
    rules = [
        ("业绩/财报", ["业绩", "年报", "季报", "半年报", "财务报表", "利润分配"]),
        ("分红/权益", ["分红", "派息", "权益分派", "股息"]),
        ("回购/增减持", ["回购", "增持", "减持", "持股变动"]),
        ("融资/债券", ["债券", "可转债", "融资", "授信", "票据"]),
        ("并购/投资", ["收购", "出售资产", "重大资产", "投资", "并购", "重组"]),
        ("治理/人事", ["董事", "监事", "高管", "辞任", "聘任", "选举"]),
        ("股东大会", ["股东大会"]),
        ("关联交易", ["关联交易"]),
        ("监管/法律", ["问询", "监管", "处罚", "诉讼", "仲裁", "法律意见书"]),
    ]
    for label, keywords in rules:
        if any(keyword in text for keyword in keywords):
            return label
    return "一般公告"


def _add_announcement_category(data: pd.DataFrame) -> pd.DataFrame:
    if data is None or data.empty or "title" not in data.columns:
        return data
    enriched = data.copy()
    enriched["event_type"] = enriched["title"].map(_classify_announcement)
    return enriched


def _announcement_type_summary(data: pd.DataFrame) -> str:
    if data is None or data.empty or "event_type" not in data.columns:
        return "No announcement category summary available."
    counts = data["event_type"].value_counts().reset_index()
    counts.columns = ["event_type", "count"]
    return _markdown_table(counts)


def get_company_events(ticker: str, curr_date: str, look_back_days: int = 30) -> str:
    """Return recent A-share announcements, company news, and policy context."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare event research expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    basic, terms = _company_terms(symbol)
    company_name = _format_value(basic.get("name")) if basic is not None else symbol
    industry = _format_value(basic.get("industry")) if basic is not None else "N/A"

    lines = [
        f"# Tushare A-share event research for {symbol} as of {curr_date}",
        "",
        f"- Company: {company_name}",
        f"- Industry: {industry}",
        f"- Look-back window: {look_back_days} days",
        "",
        "## Company Announcements",
    ]

    announcements = _fetch_announcements(symbol, curr_date, look_back_days)
    if isinstance(announcements, TushareDataError):
        lines.append(_format_error("Company announcements", announcements))
    else:
        announcements = _add_announcement_category(announcements)
        lines.extend(
            [
                "### Announcement Type Summary",
                _announcement_type_summary(announcements),
                "",
                "### Announcement Evidence",
                _format_event_table(
                    announcements,
                    ["ann_date", "event_type", "ts_code", "name", "title", "url"],
                    15,
                ),
            ]
        )

    lines.extend(["", "## Company And Industry News"])
    news_terms = terms
    news = _fetch_major_news(news_terms, curr_date, look_back_days)
    news_feed = _fetch_news_feed(news_terms, curr_date, look_back_days)

    if isinstance(news, TushareDataError) and isinstance(news_feed, TushareDataError):
        lines.extend(
            [
                _format_error("Major news", news),
                _format_error("News feed", news_feed),
            ]
        )
    else:
        if not isinstance(news, TushareDataError):
            lines.extend(
                [
                    "### Major News Matches",
                    _format_event_table(news, ["pub_time", "src", "title", "content"], 12),
                ]
            )
        if not isinstance(news_feed, TushareDataError):
            lines.extend(
                [
                    "",
                    "### News Feed Matches",
                    _format_event_table(news_feed, ["datetime", "src", "channels", "title", "content"], 12),
                ]
            )

    lines.extend(["", "## Policy And Macro Signals"])
    policy_terms = [term for term in terms if term not in {symbol, symbol.split(".")[0]}]
    policy = _fetch_cctv_policy(policy_terms, curr_date, look_back_days)
    if isinstance(policy, TushareDataError):
        lines.append(_format_error("CCTV policy news", policy))
    else:
        lines.append(_format_event_table(policy, ["date", "title", "content"], 8))

    lines.extend(
        [
            "",
            "## Analyst Instructions",
            "- Treat announcements as harder evidence than market rumors or general news.",
            "- Separate company-specific events, industry events, and macro policy events.",
            "- For every material conclusion, cite the event date and title.",
            "- If a section is unavailable because of data permission, state that limitation explicitly.",
        ]
    )
    return "\n".join(lines)


def get_tushare_news(ticker: str, start_date: str, end_date: str) -> str:
    """Adapter for the existing news tool signature."""
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        look_back_days = max(1, (end_dt - start_dt).days)
    except Exception:
        look_back_days = 30
    return get_company_events(ticker, end_date, look_back_days)


def get_tushare_global_news(curr_date: str, look_back_days: int = 7, limit: int = 50) -> str:
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"# Tushare macro and policy news as of {curr_date}",
        "",
        f"- Look-back window: {look_back_days} days",
        "",
        "## Major News",
    ]
    major = _fetch_general_major_news(curr_date, look_back_days, limit)
    if isinstance(major, TushareDataError):
        lines.append(_format_error("Major news", major))
    else:
        lines.append(_format_event_table(major, ["pub_time", "src", "title", "content"], limit))

    lines.extend(["", "## CCTV Policy News"])
    policy = _fetch_cctv_policy([], curr_date, look_back_days, min(limit, 20))
    if isinstance(policy, TushareDataError):
        lines.append(_format_error("CCTV policy news", policy))
    else:
        lines.append(_format_event_table(policy, ["date", "title", "content"], min(limit, 20)))

    return "\n".join(lines)


def _latest_daily_basic_market(trade_date: str) -> pd.DataFrame:
    fields = ",".join(
        [
            "ts_code",
            "trade_date",
            "close",
            "turnover_rate",
            "pe_ttm",
            "pb",
            "ps_ttm",
            "dv_ttm",
            "total_mv",
            "circ_mv",
        ]
    )
    return _query_optional_api("daily_basic", trade_date=trade_date, fields=fields)


_PEER_DAILY_BASIC_COLS = [
    "ts_code",
    "trade_date",
    "close",
    "turnover_rate",
    "pe_ttm",
    "pb",
    "ps_ttm",
    "dv_ttm",
    "total_mv",
    "circ_mv",
]


def _daily_basic_row_dict(symbol: str, latest: pd.Series | None) -> dict[str, object]:
    row = {col: pd.NA for col in _PEER_DAILY_BASIC_COLS}
    row["ts_code"] = symbol
    if latest is None:
        return row
    for col in _PEER_DAILY_BASIC_COLS:
        if col in latest.index:
            row[col] = latest.get(col)
    row["ts_code"] = symbol
    return row


def _individual_peer_daily_basic(
    peers: pd.DataFrame,
    target_latest: pd.Series,
    symbol: str,
    curr_date: str,
) -> pd.DataFrame:
    rows = []
    for _, row in peers.iterrows():
        peer_symbol = str(row.get("ts_code") or "").strip()
        if not peer_symbol:
            continue
        if peer_symbol == symbol:
            latest = target_latest
        else:
            try:
                latest = _fetch_daily_basic_latest(peer_symbol, curr_date)
            except Exception:
                latest = None
        rows.append(_daily_basic_row_dict(peer_symbol, latest))
    return pd.DataFrame(rows, columns=_PEER_DAILY_BASIC_COLS)


def _merge_peer_financials(peer_data: pd.DataFrame, curr_date: str, limit: int) -> pd.DataFrame:
    rows = []
    for _, row in peer_data.head(limit).iterrows():
        symbol = row["ts_code"]
        try:
            indicators = _fetch_fina_indicator(symbol, curr_date)
        except Exception:
            indicators = pd.DataFrame()
        if indicators is None or indicators.empty:
            rows.append({})
        else:
            ordered = indicators.copy()
            if "end_date" in ordered.columns:
                ordered["end_date"] = ordered["end_date"].astype(str)
                ordered = ordered.sort_values("end_date", ascending=False)
            latest = ordered.iloc[0]
            annual = (
                ordered[ordered["end_date"].str.endswith("1231")].iloc[0]
                if "end_date" in ordered.columns
                and not ordered[ordered["end_date"].str.endswith("1231")].empty
                else latest
            )
            rows.append(
                {
                    "roe": latest.get("roe"),
                    "roe_annual": annual.get("roe"),
                    "roe_waa_annual": annual.get("roe_waa"),
                    "roa": latest.get("roa"),
                    "roa_annual": annual.get("roa"),
                    "grossprofit_margin": latest.get("grossprofit_margin"),
                    "netprofit_yoy": latest.get("netprofit_yoy"),
                    "debt_to_assets": latest.get("debt_to_assets"),
                }
            )
    financials = pd.DataFrame(rows)
    return pd.concat([peer_data.head(limit).reset_index(drop=True), financials], axis=1)


def _percent_rank(series: pd.Series, higher_is_better: bool) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce")
    ranked = numeric.rank(pct=True)
    if not higher_is_better:
        ranked = 1 - ranked
    return ranked.fillna(0.5)


def _score_peers(data: pd.DataFrame) -> pd.DataFrame:
    scored = data.copy()
    scored["v4_score"] = (
        _percent_rank(scored.get("roe", pd.Series(dtype=float)), True) * 25
        + _percent_rank(scored.get("netprofit_yoy", pd.Series(dtype=float)), True) * 20
        + _percent_rank(scored.get("debt_to_assets", pd.Series(dtype=float)), False) * 15
        + _percent_rank(scored.get("pe_ttm", pd.Series(dtype=float)), False) * 15
        + _percent_rank(scored.get("pb", pd.Series(dtype=float)), False) * 10
        + _percent_rank(scored.get("dv_ttm", pd.Series(dtype=float)), True) * 10
        + _percent_rank(scored.get("total_mv", pd.Series(dtype=float)), True) * 5
    )
    scored["v4_score"] = scored["v4_score"].round(1)
    return scored.sort_values("v4_score", ascending=False)


def _score_bank_peers(data: pd.DataFrame) -> pd.DataFrame:
    scored = data.copy()
    scored["v4_score"] = (
        _percent_rank(scored.get("roe_annual", scored.get("roe", pd.Series(dtype=float))), True) * 30
        + _percent_rank(scored.get("roa_annual", scored.get("roa", pd.Series(dtype=float))), True) * 15
        + _percent_rank(scored.get("pb", pd.Series(dtype=float)), False) * 20
        + _percent_rank(scored.get("pe_ttm", pd.Series(dtype=float)), False) * 10
        + _percent_rank(scored.get("dv_ttm", pd.Series(dtype=float)), True) * 15
        + _percent_rank(scored.get("debt_to_assets", pd.Series(dtype=float)), False) * 5
        + _percent_rank(scored.get("total_mv", pd.Series(dtype=float)), True) * 5
    )
    scored["v4_score"] = scored["v4_score"].round(1)
    return scored.sort_values("v4_score", ascending=False)


def _fetch_stock_basic_universe(pro=None) -> pd.DataFrame:
    fields = "ts_code,symbol,name,area,industry,market,exchange,list_date"
    try:
        if pro is None:
            universe = _query_pro_with_fallback(
                "stock_basic", empty_ok=True, list_status="L", fields=fields
            )
        else:
            universe = pro.stock_basic(list_status="L", fields=fields)
    except Exception:
        if pro is None:
            universe = _query_pro_with_fallback(
                "stock_basic", empty_ok=True, list_status="L"
            )
        else:
            universe = pro.stock_basic(list_status="L")
    if universe is None:
        return pd.DataFrame()
    if universe.empty and pro is None:
        try:
            fallback = _query_pro_with_fallback(
                "stock_basic", empty_ok=True, list_status="L"
            )
        except Exception:
            fallback = pd.DataFrame()
        if fallback is not None and not fallback.empty:
            universe = fallback
    missing = {"ts_code", "name", "industry"} - set(universe.columns)
    if missing:
        try:
            if pro is None:
                fallback = _query_pro_with_fallback(
                    "stock_basic", empty_ok=True, list_status="L"
                )
            else:
                fallback = pro.stock_basic(list_status="L")
        except Exception:
            fallback = pd.DataFrame()
        if fallback is not None and not fallback.empty:
            universe = fallback
    return universe if universe is not None else pd.DataFrame()


def _curated_peer_universe(symbol: str, basic: pd.Series | None) -> pd.DataFrame:
    """Return a small curated peer universe when broad stock_basic is unavailable."""
    industry = str(basic.get("industry") if basic is not None else "" or "").strip()
    company_name = str(basic.get("name") if basic is not None else "" or "").strip()
    is_baijiu = (
        symbol in BAIJIU_PEER_FALLBACK
        or "白酒" in industry
        or any(term in company_name for term in ("茅台", "五粮液", "老窖", "汾酒", "洋河"))
    )
    if not is_baijiu:
        return pd.DataFrame()
    rows = [
        {
            "ts_code": code,
            "symbol": code.split(".")[0],
            "name": name,
            "industry": "白酒",
        }
        for code, name in BAIJIU_PEER_FALLBACK.items()
    ]
    return pd.DataFrame(rows)


def _row_numeric(row: pd.Series, columns: list[str]) -> float | None:
    for col in columns:
        if col not in row.index:
            continue
        value = pd.to_numeric(pd.Series([row.get(col)]), errors="coerce").iloc[0]
        if not pd.isna(value):
            return float(value)
    return None


def _metric_contrast(
    peer: pd.Series,
    target: pd.Series,
    columns: list[str],
    label: str,
    higher_is_better: bool,
    want_strength: bool,
) -> str | None:
    peer_value = _row_numeric(peer, columns)
    target_value = _row_numeric(target, columns)
    if peer_value is None or target_value is None or peer_value == target_value:
        return None
    is_strength = peer_value > target_value if higher_is_better else peer_value < target_value
    if is_strength != want_strength:
        return None
    direction = "higher" if peer_value > target_value else "lower"
    return f"{label} {direction} ({peer_value:.2f} vs target {target_value:.2f})"


def _build_competitor_analysis_rows(
    scored: pd.DataFrame,
    symbol: str,
    limit: int = 5,
) -> list[dict[str, str]]:
    if scored is None or scored.empty or "ts_code" not in scored.columns:
        return []
    target_rows = scored[scored["ts_code"] == symbol]
    if target_rows.empty:
        return []
    target = target_rows.iloc[0]
    target_score = _row_numeric(target, ["v4_score"])
    candidates = scored[scored["ts_code"] != symbol].sort_values("v4_score", ascending=False).head(limit)
    rows = []
    metric_specs = [
        (["pe_ttm"], "PE TTM", False),
        (["pb"], "PB", False),
        (["ps_ttm"], "PS TTM", False),
        (["roe_annual", "roe"], "ROE", True),
        (["roa_annual", "roa"], "ROA", True),
        (["grossprofit_margin"], "gross margin", True),
        (["netprofit_yoy"], "profit growth", True),
        (["debt_to_assets"], "debt ratio", False),
        (["dv_ttm"], "dividend yield", True),
        (["total_mv"], "market cap scale", True),
    ]
    for rank, (_, peer) in enumerate(candidates.iterrows(), start=1):
        strengths = [
            signal
            for columns, label, higher_is_better in metric_specs
            if (signal := _metric_contrast(peer, target, columns, label, higher_is_better, True))
        ]
        weaknesses = [
            signal
            for columns, label, higher_is_better in metric_specs[:-1]
            if (signal := _metric_contrast(peer, target, columns, label, higher_is_better, False))
        ]
        peer_score = _row_numeric(peer, ["v4_score"])
        score_gap = (
            f"{peer_score - target_score:+.1f}"
            if peer_score is not None and target_score is not None
            else "N/A"
        )
        rows.append(
            {
                "rank": str(rank),
                "competitor": f"{_format_value(peer.get('name'))} ({_format_value(peer.get('ts_code'))})",
                "score_gap_vs_target": score_gap,
                "apparent_edges": "; ".join(strengths[:4]) if strengths else "No obvious quantitative edge versus target",
                "possible_weaknesses": "; ".join(weaknesses[:3]) if weaknesses else "No obvious quantitative weakness in the selected metrics",
                "diligence_use": (
                    "Verify filing-based business overlap, segment economics, cash conversion, "
                    "and whether the peer has a separate new-business valuation bucket."
                ),
            }
        )
    return rows


def get_peer_comparison(ticker: str, curr_date: str, peer_limit: int = 12) -> str:
    """Compare an A-share company with same-industry peers."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare peer comparison expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    basic = _fetch_stock_basic(symbol)
    universe = _fetch_stock_basic_universe(None)
    if universe.empty:
        universe = _curated_peer_universe(symbol, basic)
    if basic is None and not universe.empty and "ts_code" in universe.columns:
        matched = universe[universe["ts_code"].astype(str) == symbol]
        if not matched.empty:
            basic = matched.iloc[0]
    if basic is None:
        return f"# Same-industry peer comparison unavailable for {symbol}\n\n- Reason: No Tushare stock_basic data found for {symbol}."
    industry = str(basic.get("industry") or "").strip()
    if not industry:
        return f"No industry classification found for {symbol}; peer comparison unavailable."

    latest = _fetch_daily_basic_latest(symbol, curr_date)
    if latest is None:
        return f"No daily_basic valuation snapshot found for {symbol} near {curr_date}."
    trade_date = str(latest.get("trade_date"))

    required_cols = {"ts_code", "name", "industry"}
    missing_cols = sorted(required_cols - set(universe.columns))
    if universe.empty or missing_cols:
        return (
            f"Same-industry peer comparison unavailable for {symbol}: "
            f"Tushare stock_basic universe missing required columns {missing_cols or 'all'}."
        )
    peers = universe[universe["industry"].fillna("").astype(str) == industry].copy()
    if peers.empty:
        return f"No same-industry peers found for {symbol} in Tushare stock_basic."

    peer_count = max(peer_limit, 3)
    data_notes: list[str] = []
    try:
        market_daily = _latest_daily_basic_market(trade_date)
    except Exception as exc:
        market_daily = pd.DataFrame()
        data_notes.append(f"daily_basic market snapshot unavailable, fell back to per-peer lookup: {exc}")

    if market_daily is None or market_daily.empty or "ts_code" not in market_daily.columns:
        if market_daily is not None and not market_daily.empty and "ts_code" not in market_daily.columns:
            data_notes.append("daily_basic market snapshot lacked ts_code, fell back to per-peer lookup.")
        target_rows = peers[peers["ts_code"] == symbol]
        peer_rows = peers[peers["ts_code"] != symbol].head(peer_count - 1)
        selected_basics = pd.concat([target_rows, peer_rows], ignore_index=True)
        peer_daily = _individual_peer_daily_basic(selected_basics, latest, symbol, curr_date)
        selected = selected_basics.merge(peer_daily, on="ts_code", how="left")
    else:
        merged = peers.merge(market_daily, on="ts_code", how="left")
        target_mv = pd.to_numeric(latest.get("total_mv"), errors="coerce")
        merged["mv_distance"] = (
            pd.to_numeric(merged["total_mv"], errors="coerce") - target_mv
        ).abs()
        merged["is_target"] = merged["ts_code"] == symbol
        selected = pd.concat(
            [
                merged[merged["is_target"]],
                merged[~merged["is_target"]].sort_values("mv_distance").head(peer_count - 1),
            ],
            ignore_index=True,
        )
        if selected.empty:
            selected_basics = pd.concat(
                [
                    peers[peers["ts_code"] == symbol],
                    peers[peers["ts_code"] != symbol].head(peer_count - 1),
                ],
                ignore_index=True,
            )
            peer_daily = _individual_peer_daily_basic(selected_basics, latest, symbol, curr_date)
            selected = selected_basics.merge(peer_daily, on="ts_code", how="left")
            data_notes.append("same-industry market-value selection was empty, fell back to per-peer lookup.")

    enriched = _merge_peer_financials(selected, curr_date, peer_count)
    is_banking = is_banking_entity(symbol, basic=basic, industry=industry)
    scored = _score_bank_peers(enriched) if is_banking else _score_peers(enriched)
    target_score = scored.loc[scored["ts_code"] == symbol, "v4_score"]
    target_score_value = float(target_score.iloc[0]) if not target_score.empty else None
    better = scored[(scored["ts_code"] != symbol) & (scored["v4_score"] > (target_score_value or 0))]
    ranked = scored.sort_values("v4_score", ascending=False).reset_index(drop=True)
    target_rank = None
    if symbol in ranked["ts_code"].values:
        target_rank = int(ranked.index[ranked["ts_code"] == symbol][0]) + 1
    best_peer = ranked.iloc[0] if not ranked.empty else None

    display_cols = [
        "ts_code",
        "name",
        "industry",
        "total_mv",
        "pe_ttm",
        "pb",
        "ps_ttm",
        "dv_ttm",
        "roe_annual",
        "roa_annual",
        "roe",
        "roa",
        "netprofit_yoy",
        "debt_to_assets",
        "v4_score",
    ]
    display = _select_existing(scored, display_cols)
    competitor_rows = _build_competitor_analysis_rows(scored, symbol)

    lines = [
        f"# Tushare same-industry peer comparison for {symbol} as of {curr_date}",
        "",
        f"- Target company: {_format_value(basic.get('name'))}",
        f"- Industry: {industry}",
        f"- Valuation trade date: {_format_yyyymmdd(trade_date)}",
        f"- Peer sample: same Tushare stock_basic industry, closest by market value.",
        *(f"- Data note: {note}" for note in data_notes),
        *(
            [
                "- Banking peer screen: PB/ROE, ROA, dividend yield, and capital-quality proxies receive priority; use filing KPIs for NIM, asset quality, provision coverage, and CET1 before making a final allocation call.",
                "- Banking ROE/ROA columns use latest annual rows when available for scoring; latest-period ROE/ROA are shown only as secondary context because interim Tushare ratios may be period-scaled.",
            ]
            if is_banking
            else []
        ),
        "",
        "## Peer Table",
        _markdown_table(display),
        "",
        "## Peer Selection Verdict",
    ]
    if target_rank is None:
        lines.append(
            "Peer-selection verdict unavailable because the target could not be ranked in the selected sample."
        )
    elif better.empty:
        lines.append(
            f"The target ranks #{target_rank} of {len(ranked)} in the selected peer sample on the v4 screen, "
            "and no sampled peer currently outranks it. Treat this as 'no clearly better alternative emerged,' "
            "not as proof that the target is automatically the best investable name."
        )
    else:
        leader_bits = []
        if best_peer is not None:
            leader_bits.append(
                f"{_format_value(best_peer.get('name'))} ({_format_value(best_peer.get('ts_code'))}) "
                f"leads the screen with v4_score {_format_value(best_peer.get('v4_score'))}"
            )
        leader_text = "; ".join(leader_bits) if leader_bits else "At least one peer outranks the target"
        lines.append(
            f"The target ranks #{target_rank} of {len(ranked)} in the selected peer sample. "
            f"{leader_text}. A better build candidate may exist if its higher score is supported by "
            "real business quality rather than a one-off or data distortion."
        )
    lines.extend(
        [
            "",
        "## Potentially Better Peer Candidates",
        ]
    )
    if better.empty:
        lines.append(
            "No peer in this sample scored higher than the target on the simple v4 screen. This does not prove the target is best; it only means no clear alternative emerged from the selected valuation-quality-growth metrics."
        )
    else:
        better_cols = ["ts_code", "name", "pe_ttm", "pb", "roe", "roa", "netprofit_yoy", "debt_to_assets", "v4_score"]
        lines.append(_markdown_table(_select_existing(better, better_cols)))
        lines.append(
            "These are screening candidates, not final recommendations. Ask whether the higher score comes from genuinely better business quality, temporarily depressed valuation, or data distortions."
        )

    lines.extend(
        [
            "",
            "## Competitor Analysis For Peer Recommendation",
        ]
    )
    if competitor_rows:
        lines.append(_markdown_table(pd.DataFrame(competitor_rows)))
        lines.append(
            "Use this table to decide which same-industry names deserve deeper competitor analysis. "
            "The table is a quantitative screen; it must be reconciled with filing evidence on actual business overlap, segment economics, and split valuation."
        )
    else:
        lines.append(
            "No competitor analysis rows were generated because the target or peer scores were unavailable."
        )

    lines.extend(
        [
            "",
            "## Analyst Instructions",
            "- Compare the target against peers on valuation, profitability, growth, leverage, and shareholder return.",
            *(
                [
                    "- For banks, do not rank by generic leverage alone. Final peer judgment must compare PB/ROE, ROA, NIM, asset quality, provision coverage, CET1, RWA growth, and dividend sustainability.",
                ]
                if is_banking
                else []
            ),
            "- If another peer appears better, explain the specific metrics and the investment caveat.",
            "- Do not claim a peer is superior only because it has a lower PE; check quality and growth together.",
            "- Use the competitor analysis table to choose which peers deserve deeper work, then verify from filings whether their products, customer mix, regions, and business segments truly compete with the target.",
            "- If the target or peer has a new business or second curve, compare that segment separately instead of forcing one blended peer multiple.",
        ]
    )
    return "\n".join(lines)


def _metric_percentile(series: pd.Series, latest_value) -> tuple[str, str, str, str, str]:
    numeric = pd.to_numeric(series, errors="coerce").dropna()
    latest = pd.to_numeric(pd.Series([latest_value]), errors="coerce").iloc[0]
    if numeric.empty or pd.isna(latest):
        return "N/A", "N/A", "N/A", "N/A", "N/A"
    percentile = (numeric <= latest).mean() * 100
    return (
        f"{latest:.2f}",
        f"{percentile:.1f}%",
        f"{numeric.min():.2f}",
        f"{numeric.median():.2f}",
        f"{numeric.max():.2f}",
    )


def _valuation_comment(metric: str, percentile_text: str) -> str:
    if percentile_text == "N/A":
        return "Insufficient history"
    percentile = float(percentile_text.rstrip("%"))
    if metric in {"dv_ttm"}:
        if percentile >= 80:
            return "Dividend yield is historically high"
        if percentile <= 20:
            return "Dividend yield is historically low"
        return "Dividend yield is near historical middle range"
    if percentile <= 20:
        return "Historically low valuation"
    if percentile <= 40:
        return "Relatively low valuation"
    if percentile <= 60:
        return "Mid-range valuation"
    if percentile <= 80:
        return "Relatively high valuation"
    return "Historically high valuation"


def get_valuation_percentiles(ticker: str, curr_date: str, years: int = 5) -> str:
    """Return historical PE/PB/PS/dividend percentile context for an A-share symbol."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare valuation percentiles expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    fields = "ts_code,trade_date,pe_ttm,pb,ps_ttm,dv_ttm,total_mv"
    data = _query_optional_api(
        "daily_basic",
        ts_code=symbol,
        start_date=start_dt.strftime("%Y%m%d"),
        end_date=end_dt.strftime("%Y%m%d"),
        fields=fields,
    )
    if data is None or data.empty:
        return f"No Tushare daily_basic valuation history found for {symbol}."
    data = data.sort_values("trade_date")
    latest = data.dropna(how="all", subset=["pe_ttm", "pb", "ps_ttm", "dv_ttm"]).iloc[-1]

    metric_names = {
        "pe_ttm": "PE TTM",
        "pb": "PB",
        "ps_ttm": "PS TTM",
        "dv_ttm": "Dividend Yield TTM",
    }
    rows = []
    for metric, label in metric_names.items():
        latest_value, percentile, min_v, median_v, max_v = _metric_percentile(data[metric], latest.get(metric))
        rows.append(
            {
                "metric": label,
                "latest": latest_value,
                "percentile": percentile,
                "min": min_v,
                "median": median_v,
                "max": max_v,
                "comment": _valuation_comment(metric, percentile),
            }
        )

    lines = [
        f"# Tushare historical valuation percentiles for {symbol} as of {curr_date}",
        "",
        f"- History window: {years} years",
        f"- Latest valuation trade date: {_format_yyyymmdd(latest.get('trade_date'))}",
        f"- Available observations: {len(data)} trading days",
        "",
        "## Valuation Percentile Table",
        _markdown_table(pd.DataFrame(rows)),
        "",
        "## Analyst Instructions",
        "- Low PE/PB percentile can mean undervaluation, but can also reflect deteriorating fundamentals.",
        "- Compare valuation percentile with ROE, growth, cash flow, and event risk before drawing conclusions.",
        "- Dividend yield percentile should be interpreted separately: a high yield can be attractive or can signal market concern.",
    ]
    return "\n".join(lines)


def _index_price_position(ts_code: str, curr_date: str, look_back_days: int) -> dict[str, str]:
    _, _, start, end = _date_window(curr_date, look_back_days)
    data = _query_optional_api(
        "index_daily",
        ts_code=ts_code,
        start_date=start,
        end_date=end,
    )
    if data is None or data.empty or "close" not in data.columns:
        return {
            "recent_change": "N/A",
            "drawdown_from_high": "N/A",
            "price_position": "N/A",
        }

    data = data.sort_values("trade_date")
    close = pd.to_numeric(data["close"], errors="coerce").dropna()
    if close.empty:
        return {
            "recent_change": "N/A",
            "drawdown_from_high": "N/A",
            "price_position": "N/A",
        }

    latest = close.iloc[-1]
    first = close.iloc[0]
    high = close.max()
    recent_change = "N/A" if first == 0 else f"{(latest / first - 1) * 100:.2f}%"
    drawdown = "N/A" if high == 0 else f"{(latest / high - 1) * 100:.2f}%"
    position = f"{(close <= latest).mean() * 100:.1f}%"
    return {
        "recent_change": recent_change,
        "drawdown_from_high": drawdown,
        "price_position": position,
    }


def _index_valuation_position(ts_code: str, curr_date: str, years: int) -> dict[str, str]:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(years=max(1, years))
    result = _safe_optional_query(
        "index_dailybasic",
        ts_code=ts_code,
        start_date=start_dt.strftime("%Y%m%d"),
        end_date=end_dt.strftime("%Y%m%d"),
        fields="ts_code,trade_date,pe,pe_ttm,pb,turnover_rate",
    )
    if isinstance(result, TushareDataError) or result is None or result.empty:
        return {
            "pe_ttm_percentile": "N/A",
            "pb_percentile": "N/A",
            "turnover_rate": "N/A",
        }

    result = result.sort_values("trade_date")
    latest = result.iloc[-1]
    _, pe_pct, _, _, _ = _metric_percentile(result.get("pe_ttm", pd.Series(dtype=float)), latest.get("pe_ttm"))
    _, pb_pct, _, _, _ = _metric_percentile(result.get("pb", pd.Series(dtype=float)), latest.get("pb"))
    return {
        "pe_ttm_percentile": pe_pct,
        "pb_percentile": pb_pct,
        "turnover_rate": _format_value(latest.get("turnover_rate"), "%"),
    }


def _risk_label(percentile_text: str, high_is_risky: bool = True) -> str:
    if percentile_text == "N/A":
        return "Unknown"
    percentile = float(percentile_text.rstrip("%"))
    if high_is_risky:
        if percentile >= 80:
            return "High"
        if percentile >= 60:
            return "Elevated"
        if percentile <= 20:
            return "Low"
        return "Neutral"
    if percentile <= 20:
        return "High"
    if percentile <= 40:
        return "Elevated"
    if percentile >= 80:
        return "Low"
    return "Neutral"


def _pct_to_float(percentile_text: str) -> float | None:
    if percentile_text == "N/A":
        return None
    try:
        return float(str(percentile_text).rstrip("%"))
    except Exception:
        return None


def _market_regime(rows: list[dict[str, str]]) -> tuple[str, str, str]:
    price_positions = [
        value for value in (_pct_to_float(row.get("price_position", "N/A")) for row in rows)
        if value is not None
    ]
    pe_positions = [
        value for value in (_pct_to_float(row.get("pe_ttm_percentile", "N/A")) for row in rows)
        if value is not None
    ]
    pb_positions = [
        value for value in (_pct_to_float(row.get("pb_percentile", "N/A")) for row in rows)
        if value is not None
    ]
    drawdowns = []
    for row in rows:
        text = str(row.get("drawdown_from_high", "N/A"))
        try:
            drawdowns.append(float(text.rstrip("%")))
        except Exception:
            pass

    if not price_positions:
        return "Unknown", "No reliable index position data.", "Neutral"

    avg_price = sum(price_positions) / len(price_positions)
    valuation_positions = pe_positions + pb_positions
    avg_valuation = (
        sum(valuation_positions) / len(valuation_positions)
        if valuation_positions
        else 50.0
    )
    avg_drawdown = sum(drawdowns) / len(drawdowns) if drawdowns else 0.0

    if avg_price <= 15 and avg_valuation <= 25:
        return (
            "Extreme pessimism / depressed market",
            "Market price and valuation percentiles are both very low; contrarian opportunities deserve more attention, but liquidity and trend risk remain.",
            "Allow slightly more aggressive entries after confirming company-level evidence.",
        )
    if avg_price <= 30 or avg_drawdown <= -15:
        return (
            "Bearish / risk-off market",
            "Index position is low or drawdown is meaningful; trend risk is elevated.",
            "Keep ratings conservative unless valuation, balance sheet, and catalysts are strong.",
        )
    if avg_price >= 85 and avg_valuation >= 75:
        return (
            "Extreme optimism / crowded market",
            "Market price and valuation percentiles are both high; upside should be discounted and profit-taking discipline matters.",
            "Be more conservative: prefer staged profit-taking and tighter risk controls.",
        )
    if avg_price >= 70 or avg_valuation >= 70:
        return (
            "Bullish but risk elevated",
            "Market is strong or valuations are high; momentum may persist, but margin of safety is thinner.",
            "Do not upgrade ratings mechanically; require stronger company-specific upside.",
        )
    return (
        "Neutral / balanced market",
        "No extreme market-wide sentiment or valuation condition is detected.",
        "Use company and sector evidence as the primary rating driver.",
    )


def _industry_cross_section(symbol: str, curr_date: str) -> tuple[pd.Series, pd.DataFrame, pd.DataFrame]:
    basic = _fetch_stock_basic(symbol)
    if basic is None:
        raise TushareDataError(f"No stock_basic data found for {symbol}.")
    industry = str(basic.get("industry") or "").strip()
    if not industry:
        raise TushareDataError(f"No industry classification found for {symbol}.")

    latest = _fetch_daily_basic_latest(symbol, curr_date)
    if latest is None:
        raise TushareDataError(f"No daily_basic valuation snapshot found for {symbol}.")
    trade_date = str(latest.get("trade_date"))

    pro = _get_pro_client()
    universe = _fetch_stock_basic_universe(pro)
    required_cols = {"ts_code", "name", "industry"}
    missing_cols = sorted(required_cols - set(universe.columns))
    if universe.empty or missing_cols:
        raise TushareDataError(
            f"Tushare stock_basic universe missing required columns {missing_cols or 'all'}."
        )
    daily = _latest_daily_basic_market(trade_date)
    merged = universe.merge(daily, on="ts_code", how="inner")
    merged["industry"] = merged["industry"].fillna("").astype(str)

    numeric_cols = ["pe_ttm", "pb", "ps_ttm", "dv_ttm", "turnover_rate", "total_mv"]
    for col in numeric_cols:
        if col in merged.columns:
            merged[col] = pd.to_numeric(merged[col], errors="coerce")

    industry_stats = (
        merged.groupby("industry")
        .agg(
            stock_count=("ts_code", "count"),
            median_pe_ttm=("pe_ttm", "median"),
            median_pb=("pb", "median"),
            median_ps_ttm=("ps_ttm", "median"),
            median_dv_ttm=("dv_ttm", "median"),
            median_turnover=("turnover_rate", "median"),
            median_total_mv=("total_mv", "median"),
        )
        .reset_index()
    )
    target_industry = industry_stats[industry_stats["industry"] == industry]
    if target_industry.empty:
        raise TushareDataError(f"No same-industry valuation data found for {symbol}.")
    return target_industry.iloc[0], industry_stats, merged[merged["industry"] == industry].copy()


def _industry_metric_percentile(industry_stats: pd.DataFrame, target_row: pd.Series, col: str) -> str:
    values = pd.to_numeric(industry_stats[col], errors="coerce").dropna()
    latest = pd.to_numeric(pd.Series([target_row.get(col)]), errors="coerce").iloc[0]
    if values.empty or pd.isna(latest):
        return "N/A"
    return f"{(values <= latest).mean() * 100:.1f}%"


def get_market_sector_risk(ticker: str, curr_date: str, look_back_days: int = 120, years: int = 5) -> str:
    """Assess broad-market and same-industry valuation risk for an A-share symbol."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare market/sector risk expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    indexes = {
        "000001.SH": "SSE Composite",
        "000300.SH": "CSI 300",
        "000905.SH": "CSI 500",
        "399006.SZ": "ChiNext Index",
    }
    index_rows = []
    for code, name in indexes.items():
        try:
            price = _index_price_position(code, curr_date, look_back_days)
        except Exception:
            price = {
                "recent_change": "N/A",
                "drawdown_from_high": "N/A",
                "price_position": "N/A",
            }
        try:
            valuation = _index_valuation_position(code, curr_date, years)
        except Exception:
            valuation = {
                "pe_ttm_percentile": "N/A",
                "pb_percentile": "N/A",
                "turnover_rate": "N/A",
            }
        risk_votes = [
            _risk_label(price["price_position"]),
            _risk_label(valuation["pe_ttm_percentile"]),
            _risk_label(valuation["pb_percentile"]),
        ]
        index_rows.append(
            {
                "index": f"{name} ({code})",
                "recent_change": price["recent_change"],
                "drawdown_from_high": price["drawdown_from_high"],
                "price_position": price["price_position"],
                "pe_ttm_percentile": valuation["pe_ttm_percentile"],
                "pb_percentile": valuation["pb_percentile"],
                "risk_hint": "High" if "High" in risk_votes else ("Elevated" if "Elevated" in risk_votes else "Neutral"),
            }
        )

    basic = _fetch_stock_basic(symbol)
    latest = _fetch_daily_basic_latest(symbol, curr_date)
    if basic is None or latest is None:
        industry_section = "Industry risk unavailable because stock_basic or daily_basic data is missing."
        divergence_section = "No divergence diagnosis available."
    else:
        try:
            industry_row, industry_stats, same_industry = _industry_cross_section(symbol, curr_date)
            pe_pct = _industry_metric_percentile(industry_stats, industry_row, "median_pe_ttm")
            pb_pct = _industry_metric_percentile(industry_stats, industry_row, "median_pb")
            ps_pct = _industry_metric_percentile(industry_stats, industry_row, "median_ps_ttm")
            turnover_pct = _industry_metric_percentile(industry_stats, industry_row, "median_turnover")

            target_pe = pd.to_numeric(pd.Series([latest.get("pe_ttm")]), errors="coerce").iloc[0]
            target_pb = pd.to_numeric(pd.Series([latest.get("pb")]), errors="coerce").iloc[0]
            industry_pe = pd.to_numeric(pd.Series([industry_row.get("median_pe_ttm")]), errors="coerce").iloc[0]
            industry_pb = pd.to_numeric(pd.Series([industry_row.get("median_pb")]), errors="coerce").iloc[0]
            target_low_vs_sector = (
                pd.notna(target_pe)
                and pd.notna(industry_pe)
                and target_pe < industry_pe
                and pd.notna(target_pb)
                and pd.notna(industry_pb)
                and target_pb < industry_pb
            )
            sector_high_risk = _risk_label(pe_pct) in {"High", "Elevated"} or _risk_label(pb_pct) in {"High", "Elevated"}

            industry_table = pd.DataFrame(
                [
                    {
                        "industry": industry_row.get("industry"),
                        "stock_count": industry_row.get("stock_count"),
                        "median_pe_ttm": industry_row.get("median_pe_ttm"),
                        "median_pb": industry_row.get("median_pb"),
                        "median_ps_ttm": industry_row.get("median_ps_ttm"),
                        "median_dv_ttm": industry_row.get("median_dv_ttm"),
                        "pe_cross_section_percentile": pe_pct,
                        "pb_cross_section_percentile": pb_pct,
                        "ps_cross_section_percentile": ps_pct,
                        "turnover_cross_section_percentile": turnover_pct,
                    }
                ]
            )
            target_table = pd.DataFrame(
                [
                    {
                        "ts_code": symbol,
                        "name": basic.get("name"),
                        "industry": basic.get("industry"),
                        "pe_ttm": latest.get("pe_ttm"),
                        "pb": latest.get("pb"),
                        "ps_ttm": latest.get("ps_ttm"),
                        "dv_ttm": latest.get("dv_ttm"),
                        "total_mv": latest.get("total_mv"),
                    }
                ]
            )
            industry_section = (
                "### Industry Cross-Section Risk\n\n"
                + _markdown_table(industry_table)
                + "\n\n### Target Versus Industry Median\n\n"
                + _markdown_table(target_table)
            )
            if sector_high_risk and target_low_vs_sector:
                divergence_section = (
                    "The sector appears relatively expensive or active in the current cross-section, "
                    "while the target trades below the sector median on both PE TTM and PB. This is a useful deep-dive signal: "
                    "it may indicate a neglected value opportunity, but it may also indicate company-specific problems that peers do not share."
                )
            elif sector_high_risk:
                divergence_section = (
                    "The sector itself carries elevated valuation or trading risk. A bullish view on the target should require stronger company-specific evidence and a margin-of-safety check."
                )
            else:
                divergence_section = (
                    "No obvious sector-level valuation alarm was detected from the current cross-section. Still verify industry cycle, policy risk, and event risk manually."
                )
        except Exception as exc:
            industry_section = f"Industry risk unavailable: {exc}"
            divergence_section = "No divergence diagnosis available."

    lines = [
        f"# Tushare market and sector risk for {symbol} as of {curr_date}",
        "",
        f"- Market look-back window: {look_back_days} days",
        f"- Index valuation history window: {years} years",
        "",
        "## Broad Market Risk",
        _markdown_table(pd.DataFrame(index_rows)),
        "",
        "## Sector Risk",
        industry_section,
        "",
        "## Divergence Diagnosis",
        divergence_section,
        "",
        "## Analyst Instructions",
        "- If broad-market or sector valuation risk is high, reduce confidence in aggressive upside claims unless stock-specific evidence is strong.",
        "- If the sector is high-risk but the target is low versus peers, investigate whether it is mispriced or impaired.",
        "- Separate market beta risk, sector crowding risk, and company-specific risk.",
    ]
    return "\n".join(lines)


def get_market_timing_context(ticker: str, curr_date: str, look_back_days: int = 120, years: int = 5) -> str:
    """Return market mood and rating-calibration guidance for an A-share symbol."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare market timing expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    indexes = {
        "000001.SH": "SSE Composite",
        "000300.SH": "CSI 300",
        "000905.SH": "CSI 500",
        "399006.SZ": "ChiNext Index",
    }
    rows = []
    for code, name in indexes.items():
        try:
            price = _index_price_position(code, curr_date, look_back_days)
        except Exception:
            price = {
                "recent_change": "N/A",
                "drawdown_from_high": "N/A",
                "price_position": "N/A",
            }
        try:
            valuation = _index_valuation_position(code, curr_date, years)
        except Exception:
            valuation = {
                "pe_ttm_percentile": "N/A",
                "pb_percentile": "N/A",
                "turnover_rate": "N/A",
            }
        rows.append(
            {
                "index": f"{name} ({code})",
                "recent_change": price["recent_change"],
                "drawdown_from_high": price["drawdown_from_high"],
                "price_position": price["price_position"],
                "pe_ttm_percentile": valuation["pe_ttm_percentile"],
                "pb_percentile": valuation["pb_percentile"],
                "turnover_rate": valuation["turnover_rate"],
            }
        )

    regime, diagnosis, calibration = _market_regime(rows)

    lines = [
        f"# Market timing and rating calibration for {symbol} as of {curr_date}",
        "",
        f"- Market regime: {regime}",
        f"- Diagnosis: {diagnosis}",
        f"- Rating calibration: {calibration}",
        "",
        "## Market Mood Evidence",
        _markdown_table(pd.DataFrame(rows)),
        "",
        "## Action Range Guidance",
        "- If the final view is bullish, provide a staged profit-taking or trimming zone based on valuation percentile, resistance/price target, and market regime.",
        "- If the final view is bearish, provide an entry watch zone where risk/reward may become attractive again, based on historical valuation, technical support, and market regime.",
        "- In extreme pessimism, avoid being mechanically bearish at low valuations; require confirmation, but allow contrarian watch zones.",
        "- In extreme optimism, avoid being mechanically bullish at high valuations; emphasize staged profit-taking and downside protection.",
        "- Do not provide exact ranges unless supported by market/valuation/technical evidence; otherwise label them as scenario ranges.",
    ]
    return "\n".join(lines)
