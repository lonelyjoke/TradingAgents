from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from html import unescape
from pathlib import Path
import re
from typing import Any
from urllib.parse import urlencode

import pandas as pd
import requests

from .tushare_a_stock import TushareDataError, _markdown_table, is_a_share_symbol


CNINFO_HOME_URL = "https://irm.cninfo.com.cn/"
CNINFO_COMPANY_DETAIL_URL = "https://irm.cninfo.com.cn/ircs/company/companyDetail"
CNINFO_KEYWORD_SEARCH_URL = "https://irm.cninfo.com.cn/newircs/index/queryKeyboardInfo"
CNINFO_QUESTION_URL = "https://irm.cninfo.com.cn/newircs/company/question"

SSE_HOME_URL = "https://sns.sseinfo.com/"
SSE_COMPANY_URL = "https://sns.sseinfo.com/company.do"
SSE_FEEDS_URL = "https://sns.sseinfo.com/ajax/feeds.do"
SSE_USER_FEEDS_URL = "https://sns.sseinfo.com/ajax/userfeeds.do"
INTERACTION_CACHE_DIR = Path(__file__).resolve().parents[2] / "data" / "cache" / "investor_interactions"

_INTERACTION_THEME_RULES: dict[str, dict[str, Any]] = {
    "commercial-space": {
        "aliases": ("\u5546\u4e1a\u822a\u5929", "\u84dd\u7bad\u822a\u5929", "\u706b\u7bad", "\u536b\u661f"),
        "story_read": "space linkage / investee optionality",
        "proof_needed": "ownership, monetization, or investee milestone still needs filing support",
    },
    "compute-power": {
        "aliases": ("\u7b97\u529b", "\u6570\u636e\u4e2d\u5fc3", "\u7b97\u7535\u534f\u540c", "\u6e90\u7f51\u8377\u50a8"),
        "story_read": "new-demand adjacency around power + computing infrastructure",
        "proof_needed": "needs revenue, order, or project economics before valuation uplift",
    },
    "ai-meteorology": {
        "aliases": ("AI\u6c14\u8c61", "\u6c14\u8c61\u5927\u6a21\u578b", "\u5929\u6c14\u9884\u62a5", "\u6781\u7aef\u5929\u6c14\u9884\u8b66"),
        "story_read": "AI-enabled capability extension inside the core industrial chain",
        "proof_needed": "needs productization or customer monetization evidence",
    },
    "green-methanol": {
        "aliases": ("\u7eff\u8272\u7532\u9187", "\u7eff\u9187", "\u7532\u9187"),
        "story_read": "new-business commercialization path tied to energy transition",
        "proof_needed": "needs capacity, revenue, utilization, or offtake evidence",
    },
    "buyback-shareholder-return": {
        "aliases": ("\u56de\u8d2d", "\u6ce8\u9500", "\u5e02\u503c\u7ba1\u7406"),
        "story_read": "shareholder-return / valuation-support narrative",
        "proof_needed": "needs board approval, execution, and funding visibility",
    },
    "capital-allocation": {
        "aliases": ("\u957f\u671f\u80a1\u6743\u6295\u8d44", "\u4ef7\u503c\u6295\u8d44", "\u6295\u8d44\u7b56\u7565", "\u6295\u8d44\u6536\u76ca"),
        "story_read": "capital-allocation quality narrative",
        "proof_needed": "needs realized return history or portfolio evidence",
    },
}


@dataclass(frozen=True)
class InteractionRecord:
    ts_code: str
    exchange: str
    question_time: str | None
    answer_time: str | None
    question: str
    answer: str | None
    answer_class: str
    source_url: str
    source_type: str


def _interaction_exchange(symbol: str) -> str:
    upper = symbol.strip().upper()
    if upper.endswith(".SZ"):
        return "szse"
    if upper.endswith(".SH"):
        return "sse"
    raise TushareDataError(f"Unsupported A-share interaction symbol: {symbol!r}")


def _stockcode(symbol: str) -> str:
    return symbol.split(".")[0]


def _build_cninfo_company_url(org_id: str, symbol: str) -> str:
    return f"{CNINFO_COMPANY_DETAIL_URL}?{urlencode({'orgId': org_id, 'stockcode': _stockcode(symbol)})}"


def _build_cninfo_question_params(
    org_id: str,
    symbol: str,
    *,
    page_num: int = 1,
    page_size: int = 10,
    keyword: str = "",
    start_day: str = "",
    end_day: str = "",
) -> dict[str, Any]:
    return {
        "stockcode": _stockcode(symbol),
        "orgId": org_id,
        "pageSize": page_size,
        "pageNum": page_num,
        "keyWord": keyword,
        "startDay": start_day,
        "endDay": end_day,
    }


def _build_sse_company_url(symbol: str) -> str:
    return f"{SSE_COMPANY_URL}?{urlencode({'stockcode': _stockcode(symbol)})}"


def _build_sse_feed_params(
    page: int = 1,
    page_size: int = 10,
    feed_type: int = 11,
    show: int = 1,
) -> dict[str, Any]:
    return {
        "type": feed_type,
        "pageSize": page_size,
        "show": show,
        "page": page,
    }


def _extract_sse_uid_from_company_page(html: str) -> str | None:
    match = re.search(r"userfeeds\.do\?[^\"']*uid=(\d+)", html or "")
    return match.group(1) if match else None


def _build_sse_company_feed_params(uid: str, page: int = 1, page_size: int = 10) -> dict[str, Any]:
    return {
        "typeCode": "company",
        "type": 11,
        "pageSize": page_size,
        "uid": uid,
        "page": page,
    }


def _parse_sse_company_feed_html(html: str) -> dict[str, str | bool]:
    source = html or ""
    text = re.sub(r"<[^>]+>", " ", source)
    text = re.sub(r"\s+", " ", text).strip()
    return {
        "is_empty_recent_reply": "近1个月暂无回复" in text,
        "text_preview": text[:240],
    }


def _clean_html_text(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value or "")
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _extract_sse_first_text(block: str, class_name: str) -> str | None:
    match = re.search(
        rf'<div class="{re.escape(class_name)}"[^>]*>(.*?)</div>',
        block,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return _clean_html_text(match.group(1)) if match else None


def _extract_sse_dates(block: str) -> list[str]:
    return re.findall(
        r"<span>\s*(\d{4}年\d{2}月\d{2}日\s+\d{2}:\d{2})\s*</span>",
        block,
        flags=re.IGNORECASE,
    )


def _normalize_sse_date(value: str | None) -> str | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y年%m月%d日 %H:%M").date().isoformat()
    except ValueError:
        return None


def _parse_sse_company_feed_records(html: str, symbol: str) -> pd.DataFrame:
    normalized: list[dict[str, Any]] = []
    pattern = re.compile(
        r'<div class="m_feed_item"\s+id="item-(?P<item_id>\d+)">(.*?)(?=<div class="m_feed_item"\s+id="item-|\Z)',
        flags=re.IGNORECASE | re.DOTALL,
    )
    for match in pattern.finditer(html or ""):
        block = match.group(0)
        item_id = match.group("item_id")
        qa_split = re.split(
            r'<div class="m_feed_detail m_qa">',
            block,
            maxsplit=1,
            flags=re.IGNORECASE,
        )
        question_block = qa_split[0]
        answer_block = qa_split[1] if len(qa_split) > 1 else ""

        question = _extract_sse_first_text(question_block, "m_feed_txt")
        if question:
            question = re.sub(r"^:\s*[^)]*\)\s*", "", question).strip()
        answer = _extract_sse_first_text(answer_block, "m_feed_txt")
        dates = _extract_sse_dates(block)

        normalized.append(
            {
                "ts_code": symbol,
                "exchange": "sse",
                "question_id": item_id,
                "question_time": _normalize_sse_date(dates[0] if dates else None),
                "answer_time": _normalize_sse_date(dates[1] if len(dates) > 1 else None)
                if answer
                else None,
                "question": question or "",
                "answer": answer,
                "answer_class": _classify_answer(answer),
                **_extract_interaction_theme(question or "", answer),
                "credibility": _interaction_credibility(_classify_answer(answer)),
                "source_url": f"{SSE_HOME_URL}company.do?stockcode={_stockcode(symbol)}",
                "source_type": "sse_e_interaction",
            }
        )
    return pd.DataFrame(normalized, dtype=object)


def _default_headers() -> dict[str, str]:
    return {
        "User-Agent": "Mozilla/5.0 TradingAgents investor-interaction-research",
        "Accept": "application/json, text/plain, */*",
    }


def _cninfo_keyword_payload(keyword: str) -> dict[str, str]:
    return {"keyWord": keyword}


def _epoch_ms_to_date(value: Any) -> str | None:
    if value in (None, "", "null"):
        return None
    try:
        timestamp = float(value) / 1000
    except (TypeError, ValueError):
        return None
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).date().isoformat()


def _classify_answer(answer: str | None) -> str:
    text = (answer or "").strip()
    if not text:
        return "unanswered"

    quantitative_markers = (
        "亿元",
        "万元",
        "%",
        "MW",
        "订单",
        "收入",
        "净利润",
        "回购",
    )
    if any(marker in text for marker in quantitative_markers):
        return "substantive"

    directional_markers = (
        "已经开始",
        "正在",
        "处于",
        "有序建设",
        "战略合作",
    )
    if any(marker in text for marker in directional_markers):
        return "directional-but-unquantified"

    non_committal_markers = (
        "感谢您的关注",
        "敬请关注",
        "请以公司公告为准",
        "不便透露",
    )
    if any(marker in text for marker in non_committal_markers) and len(text) < 40:
        return "non-committal"
    return "substantive"


def _extract_interaction_theme(question: str | None, answer: str | None) -> dict[str, str]:
    text = f"{question or ''}\n{answer or ''}"
    for theme_name, rule in _INTERACTION_THEME_RULES.items():
        if any(alias in text for alias in rule["aliases"]):
            return {
                "theme": theme_name,
                "story_read": str(rule["story_read"]),
                "proof_needed": str(rule["proof_needed"]),
            }
    return {
        "theme": "unclassified",
        "story_read": "official interaction without a mapped investable theme",
        "proof_needed": "manual review required",
    }


def _interaction_credibility(answer_class: str) -> str:
    if answer_class == "substantive":
        return "higher-official-signal"
    if answer_class == "directional-but-unquantified":
        return "medium-official-signal"
    if answer_class == "non-committal":
        return "weak-official-signal"
    if answer_class == "unanswered":
        return "no-company-signal"
    return "unknown"


def _parse_cninfo_question_payload(payload: dict[str, Any], symbol: str) -> pd.DataFrame:
    normalized: list[dict[str, Any]] = []
    for row in payload.get("rows") or []:
        question_id = str(row.get("indexId") or "").strip()
        answer = row.get("attachedContent")
        normalized.append(
            {
                "ts_code": symbol,
                "exchange": "szse",
                "question_id": question_id,
                "question_time": _epoch_ms_to_date(row.get("pubDate")),
                "answer_time": (
                    _epoch_ms_to_date(
                        row.get("attachedPubDate")
                        if row.get("attachedPubDate") is not None
                        else row.get("updateDate")
                    )
                    if answer
                    else None
                ),
                "question": str(row.get("mainContent") or "").strip(),
                "answer": str(answer).strip() if answer else None,
                "answer_class": _classify_answer(answer),
                **_extract_interaction_theme(
                    str(row.get("mainContent") or "").strip(),
                    str(answer).strip() if answer else None,
                ),
                "credibility": _interaction_credibility(_classify_answer(answer)),
                "source_url": (
                    "https://irm.cninfo.com.cn/ircs/question/questionDetail?"
                    f"questionId={question_id}"
                ),
                "source_type": "cninfo_irm",
            }
        )
    return pd.DataFrame(normalized, dtype=object)


def _parse_sse_company_page(html: str) -> dict[str, str | bool]:
    source = html or ""
    title_match = re.search(r"<title[^>]*>(.*?)</title>", source, flags=re.IGNORECASE | re.DOTALL)
    title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip() if title_match else ""
    text = re.sub(r"<[^>]+>", " ", source)
    text = re.sub(r"\s+", " ", text)
    return {
        "title": title,
        "has_company_page": "上证e互动" in text or "Company" in text,
        "has_qa_section": "问答" in text or "Q&A" in text,
    }


def _safe_request(
    method: str,
    url: str,
    *,
    session: requests.Session | None = None,
    timeout: int = 15,
    **kwargs,
) -> requests.Response:
    client = session or requests.Session()
    kwargs.setdefault("headers", _default_headers())
    response = client.request(method, url, timeout=timeout, **kwargs)
    response.raise_for_status()
    return response


def _resolve_cninfo_org_id(
    symbol: str,
    session: requests.Session | None = None,
) -> str | None:
    response = _safe_request(
        "POST",
        CNINFO_KEYWORD_SEARCH_URL,
        session=session,
        data=_cninfo_keyword_payload(_stockcode(symbol)),
    )
    payload = response.json()
    for row in payload.get("data") or []:
        if str(row.get("stockCode") or "").strip() == _stockcode(symbol):
            return str(row.get("secid") or row.get("orgId") or "").strip() or None
    return None


def _fetch_cninfo_question_page(
    symbol: str,
    org_id: str,
    *,
    page_num: int = 1,
    page_size: int = 10,
    session: requests.Session | None = None,
) -> tuple[dict[str, Any], pd.DataFrame]:
    response = _safe_request(
        "POST",
        CNINFO_QUESTION_URL,
        session=session,
        params=_build_cninfo_question_params(
            org_id,
            symbol,
            page_num=page_num,
            page_size=page_size,
        ),
    )
    payload = response.json()
    return payload, _parse_cninfo_question_payload(payload, symbol)


def fetch_investor_interaction_records(
    ticker: str,
    *,
    page_size: int = 10,
    session: requests.Session | None = None,
) -> pd.DataFrame:
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Investor-interaction context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if _interaction_exchange(symbol) == "szse":
        org_id = _resolve_cninfo_org_id(symbol, session)
        if not org_id:
            raise TushareDataError(f"Could not resolve CNINFO orgId for {symbol}.")
        _, records = _fetch_cninfo_question_page(
            symbol,
            org_id,
            page_num=1,
            page_size=page_size,
            session=session,
        )
        return records

    company_response = _safe_request(
        "GET",
        _build_sse_company_url(symbol),
        session=session,
    )
    uid = _extract_sse_uid_from_company_page(company_response.text)
    if not uid:
        raise TushareDataError(f"Could not resolve SSE interaction uid for {symbol}.")
    feed_response = _safe_request(
        "GET",
        SSE_USER_FEEDS_URL,
        session=session,
        params=_build_sse_company_feed_params(uid, page=1, page_size=page_size),
    )
    return _parse_sse_company_feed_records(feed_response.text, symbol)


def _merge_interaction_cache(symbol: str, records: pd.DataFrame) -> pd.DataFrame:
    if records.empty:
        return records
    INTERACTION_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = INTERACTION_CACHE_DIR / f"{symbol.replace('.', '_')}.csv"
    if cache_path.exists():
        cached = pd.read_csv(cache_path)
        records = pd.concat([cached, records], ignore_index=True)
    deduped = records.drop_duplicates(subset=["question_id"], keep="last")
    deduped.to_csv(cache_path, index=False, encoding="utf-8-sig")
    return deduped


def fetch_investor_interaction_history(
    ticker: str,
    *,
    end_date: str | None = None,
    lookback_days: int = 180,
    page_size: int = 10,
    max_pages: int = 10,
    use_cache: bool = True,
    session: requests.Session | None = None,
) -> pd.DataFrame:
    """Fetch paginated official Q&A history, dedupe it, and apply a time window."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Investor-interaction context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    anchor = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else date.today()
    cutoff = anchor - timedelta(days=lookback_days)
    pages: list[pd.DataFrame] = []

    if _interaction_exchange(symbol) == "szse":
        org_id = _resolve_cninfo_org_id(symbol, session)
        if not org_id:
            raise TushareDataError(f"Could not resolve CNINFO orgId for {symbol}.")
        for page_num in range(1, max_pages + 1):
            payload, page = _fetch_cninfo_question_page(
                symbol,
                org_id,
                page_num=page_num,
                page_size=page_size,
                session=session,
            )
            if page.empty:
                break
            pages.append(page)
            total_page = int(payload.get("totalPage") or 1)
            if page_num >= total_page:
                break
    else:
        company_response = _safe_request("GET", _build_sse_company_url(symbol), session=session)
        uid = _extract_sse_uid_from_company_page(company_response.text)
        if not uid:
            raise TushareDataError(f"Could not resolve SSE interaction uid for {symbol}.")
        for page_num in range(1, max_pages + 1):
            feed_response = _safe_request(
                "GET",
                SSE_USER_FEEDS_URL,
                session=session,
                params=_build_sse_company_feed_params(uid, page=page_num, page_size=page_size),
            )
            page = _parse_sse_company_feed_records(feed_response.text, symbol)
            if page.empty:
                break
            pages.append(page)

    if not pages:
        return pd.DataFrame()

    records = pd.concat(pages, ignore_index=True).drop_duplicates(
        subset=["question_id"], keep="last"
    )
    if use_cache:
        records = _merge_interaction_cache(symbol, records)

    date_series = pd.to_datetime(records["question_time"], errors="coerce").dt.date
    records = records[(date_series >= cutoff) & (date_series <= anchor)]
    return records.sort_values(
        by=["question_time", "answer_time", "question_id"],
        ascending=[False, False, False],
    ).reset_index(drop=True)


def summarize_interaction_themes(records: pd.DataFrame) -> pd.DataFrame:
    if records is None or records.empty:
        return pd.DataFrame()
    filtered = records[records["theme"].fillna("unclassified") != "unclassified"].copy()
    if filtered.empty:
        return pd.DataFrame()
    summary = (
        filtered.groupby(["theme", "story_read", "proof_needed"], dropna=False)
        .agg(
            mentions=("question_id", "count"),
            answered=("answer", lambda s: int(s.notna().sum())),
            substantive=("answer_class", lambda s: int((s == "substantive").sum())),
            latest_question_time=("question_time", "max"),
        )
        .reset_index()
    )
    summary["signal_read"] = summary.apply(
        lambda row: (
            "repeated + substantive"
            if row["mentions"] >= 2 and row["substantive"] >= 1
            else "single-point official signal"
        ),
        axis=1,
    )
    return summary.sort_values(
        ["substantive", "mentions", "latest_question_time"],
        ascending=[False, False, False],
    )


def _probe_cninfo(symbol: str, session: requests.Session | None = None) -> dict[str, str]:
    if _interaction_exchange(symbol) != "szse":
        return {"source": "cninfo", "status": "not_applicable"}
    try:
        response = _safe_request(
            "POST",
            CNINFO_KEYWORD_SEARCH_URL,
            session=session,
            data=_cninfo_keyword_payload(_stockcode(symbol)),
        )
        return {
            "source": "cninfo",
            "status": "reachable",
            "content_type": response.headers.get("content-type", ""),
            "body_preview": response.text[:120],
        }
    except Exception as exc:
        return {
            "source": "cninfo",
            "status": "unavailable",
            "error": str(exc),
        }


def _probe_sse(symbol: str, session: requests.Session | None = None) -> dict[str, str]:
    if _interaction_exchange(symbol) != "sse":
        return {"source": "sse", "status": "not_applicable"}
    try:
        company_response = _safe_request(
            "GET",
            _build_sse_company_url(symbol),
            session=session,
        )
        company_page = _parse_sse_company_page(company_response.text)
        uid = _extract_sse_uid_from_company_page(company_response.text)
        feed_response = _safe_request(
            "GET",
            SSE_USER_FEEDS_URL if uid else SSE_FEEDS_URL,
            session=session,
            params=(
                _build_sse_company_feed_params(uid, page=1, page_size=5)
                if uid
                else _build_sse_feed_params(page=1, page_size=5, feed_type=11)
            ),
        )
        return {
            "source": "sse",
            "status": "reachable",
            "company_page": str(company_page),
            "uid": uid or "",
            "feed_preview": str(_parse_sse_company_feed_html(feed_response.text)),
        }
    except Exception as exc:
        return {
            "source": "sse",
            "status": "unavailable",
            "error": str(exc),
        }


def probe_investor_interaction_sources(
    ticker: str,
    session: requests.Session | None = None,
) -> pd.DataFrame:
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Investor-interaction context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    rows = [_probe_cninfo(symbol, session), _probe_sse(symbol, session)]
    return pd.DataFrame(rows)


def get_investor_interaction_context(ticker: str, curr_date: str) -> str:
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Investor-interaction context expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )

    exchange = _interaction_exchange(symbol)
    org_id = None
    if exchange == "szse":
        source_home = CNINFO_HOME_URL
        try:
            org_id = _resolve_cninfo_org_id(symbol)
        except Exception:
            org_id = None
        canonical_company_url = (
            _build_cninfo_company_url(org_id, symbol)
            if org_id
            else (
                "resolve orgId via queryKeyboardInfo, then build "
                f"{CNINFO_COMPANY_DETAIL_URL}?orgId=...&stockcode={_stockcode(symbol)}"
            )
        )
    else:
        source_home = SSE_HOME_URL
        canonical_company_url = _build_sse_company_url(symbol)

    try:
        probe = probe_investor_interaction_sources(symbol)
    except Exception as exc:
        probe = pd.DataFrame(
            [{"source": exchange, "status": "probe_failed", "error": str(exc)}]
        )

    try:
        interaction_records = fetch_investor_interaction_history(
            symbol,
            end_date=curr_date,
            lookback_days=180,
            max_pages=10,
        )
    except Exception as exc:
        interaction_records = pd.DataFrame(
            [
                {
                    "question_time": "N/A",
                    "answer_time": "N/A",
                    "question": f"Interaction retrieval unavailable: {exc}",
                    "answer": "",
                    "answer_class": "unavailable",
                    "theme": "unclassified",
                    "story_read": "",
                    "proof_needed": "",
                    "credibility": "unknown",
                }
            ]
        )

    recent_answered = interaction_records.copy()
    if "answer" in recent_answered.columns:
        recent_answered = recent_answered[recent_answered["answer"].notna()]
    recent_answered = recent_answered.head(10)
    theme_summary = summarize_interaction_themes(interaction_records)

    lines = [
        f"# Investor interaction context for {symbol} as of {curr_date}",
        "",
        f"- Exchange route: {exchange}",
        f"- Official source home: {source_home}",
        f"- Canonical company route: {canonical_company_url}",
        "",
        "## Official Endpoint Probe",
        _markdown_table(probe),
        "",
        "## Recent Official Q&A",
        _markdown_table(
            recent_answered[
                [
                    col
                    for col in [
                        "question_time",
                        "answer_time",
                        "question",
                        "answer",
                        "answer_class",
                    ]
                    if col in recent_answered.columns
                ]
            ]
        ),
        "",
        "## Official Interaction Theme Reads",
        _markdown_table(theme_summary),
        "",
        "## Normalized Record Schema",
        _markdown_table(
            pd.DataFrame(
                [
                    {"field": "ts_code", "meaning": "A-share ticker"},
                    {
                        "field": "question_time / answer_time",
                        "meaning": "official timestamps when exposed",
                    },
                    {
                        "field": "question / answer",
                        "meaning": "verbatim official interaction text",
                    },
                    {
                        "field": "answer_class",
                        "meaning": "substantive, directional-but-unquantified, non-committal, or unanswered",
                    },
                    {
                        "field": "theme / story_read / proof_needed",
                        "meaning": "mapped narrative, interpretation, and what still needs verification",
                    },
                    {
                        "field": "source_type",
                        "meaning": "cninfo_irm or sse_e_interaction",
                    },
                ]
            )
        ),
        "",
        "## Analyst Instructions",
        "- Treat official company answers as stronger narrative evidence than media association, but weaker than filings or announcements.",
        "- Before feeding interaction content into valuation, classify answers as substantive, directional-but-unquantified, non-committal, or unanswered.",
        "- Non-committal answers such as '感谢您的关注' or '请以公司公告为准' may remain narrative options, but they should not raise conviction.",
        "- Use substantive interaction answers as tier-3 narrative options unless filings or announcements independently verify the same claim.",
    ]
    return "\n".join(lines)
