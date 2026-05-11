from __future__ import annotations

from datetime import datetime, timedelta
from typing import Iterable

import pandas as pd
from dateutil.relativedelta import relativedelta

from .tushare_a_stock import (
    TushareDataError,
    _fetch_daily_basic_latest,
    _fetch_fina_indicator,
    _fetch_stock_basic,
    _format_value,
    _format_yyyymmdd,
    _get_pro_client,
    _markdown_table,
    _select_existing,
    _to_tushare_date,
    is_a_share_symbol,
)


def _date_window(curr_date: str, look_back_days: int) -> tuple[datetime, datetime, str, str]:
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - timedelta(days=max(1, look_back_days))
    return start_dt, end_dt, start_dt.strftime("%Y%m%d"), end_dt.strftime("%Y%m%d")


def _datetime_window(curr_date: str, look_back_days: int) -> tuple[str, str]:
    start_dt, end_dt, _, _ = _date_window(curr_date, look_back_days)
    return start_dt.strftime("%Y-%m-%d 00:00:00"), end_dt.strftime("%Y-%m-%d 23:59:59")


def _query_optional_api(api_name: str, **kwargs) -> pd.DataFrame:
    pro = _get_pro_client()
    func = getattr(pro, api_name, None)
    if callable(func):
        data = func(**kwargs)
    elif hasattr(pro, "query"):
        data = pro.query(api_name, **kwargs)
    else:
        raise TushareDataError(f"Tushare client does not expose {api_name}.")

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
    if isinstance(result, TushareDataError):
        return result
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
        lines.append(_format_event_table(announcements, ["ann_date", "ts_code", "name", "title", "url"], 15))

    lines.extend(["", "## Company And Industry News"])
    news_terms = terms
    news = _fetch_major_news(news_terms, curr_date, look_back_days)
    if isinstance(news, TushareDataError):
        lines.append(_format_error("Major news", news))
    else:
        lines.append(_format_event_table(news, ["pub_time", "src", "title", "content"], 12))

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
            latest = indicators.iloc[0]
            rows.append(
                {
                    "roe": latest.get("roe"),
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
    if basic is None:
        return f"No Tushare stock_basic data found for {symbol}."
    industry = str(basic.get("industry") or "").strip()
    if not industry:
        return f"No industry classification found for {symbol}; peer comparison unavailable."

    latest = _fetch_daily_basic_latest(symbol, curr_date)
    if latest is None:
        return f"No daily_basic valuation snapshot found for {symbol} near {curr_date}."
    trade_date = str(latest.get("trade_date"))

    pro = _get_pro_client()
    universe = pro.stock_basic(
        list_status="L",
        fields="ts_code,symbol,name,area,industry,market,exchange,list_date",
    )
    peers = universe[universe["industry"].fillna("").astype(str) == industry].copy()
    if peers.empty:
        return f"No same-industry peers found for {symbol} in Tushare stock_basic."

    market_daily = _latest_daily_basic_market(trade_date)
    merged = peers.merge(market_daily, on="ts_code", how="left")
    target_mv = pd.to_numeric(latest.get("total_mv"), errors="coerce")
    merged["mv_distance"] = (
        pd.to_numeric(merged["total_mv"], errors="coerce") - target_mv
    ).abs()
    merged["is_target"] = merged["ts_code"] == symbol
    peer_count = max(peer_limit, 3)
    selected = pd.concat(
        [
            merged[merged["is_target"]],
            merged[~merged["is_target"]].sort_values("mv_distance").head(peer_count - 1),
        ],
        ignore_index=True,
    )

    enriched = _merge_peer_financials(selected, curr_date, peer_count)
    scored = _score_peers(enriched)
    target_score = scored.loc[scored["ts_code"] == symbol, "v4_score"]
    target_score_value = float(target_score.iloc[0]) if not target_score.empty else None
    better = scored[(scored["ts_code"] != symbol) & (scored["v4_score"] > (target_score_value or 0))]

    display_cols = [
        "ts_code",
        "name",
        "industry",
        "total_mv",
        "pe_ttm",
        "pb",
        "ps_ttm",
        "dv_ttm",
        "roe",
        "netprofit_yoy",
        "debt_to_assets",
        "v4_score",
    ]
    display = _select_existing(scored, display_cols)

    lines = [
        f"# Tushare same-industry peer comparison for {symbol} as of {curr_date}",
        "",
        f"- Target company: {_format_value(basic.get('name'))}",
        f"- Industry: {industry}",
        f"- Valuation trade date: {_format_yyyymmdd(trade_date)}",
        f"- Peer sample: same Tushare stock_basic industry, closest by market value.",
        "",
        "## Peer Table",
        _markdown_table(display),
        "",
        "## Potentially Better Peer Candidates",
    ]
    if better.empty:
        lines.append(
            "No peer in this sample scored higher than the target on the simple v4 screen. This does not prove the target is best; it only means no clear alternative emerged from the selected valuation-quality-growth metrics."
        )
    else:
        better_cols = ["ts_code", "name", "pe_ttm", "pb", "roe", "netprofit_yoy", "debt_to_assets", "v4_score"]
        lines.append(_markdown_table(_select_existing(better, better_cols)))
        lines.append(
            "These are screening candidates, not final recommendations. Ask whether the higher score comes from genuinely better business quality, temporarily depressed valuation, or data distortions."
        )

    lines.extend(
        [
            "",
            "## Analyst Instructions",
            "- Compare the target against peers on valuation, profitability, growth, leverage, and shareholder return.",
            "- If another peer appears better, explain the specific metrics and the investment caveat.",
            "- Do not claim a peer is superior only because it has a lower PE; check quality and growth together.",
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
    universe = pro.stock_basic(
        list_status="L",
        fields="ts_code,name,industry,market,exchange",
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
