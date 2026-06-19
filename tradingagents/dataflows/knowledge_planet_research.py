"""Local Knowledge Planet intelligence retrieval and daily synthesis.

The Knowledge Planet database is a private, local research layer built from
manually imported posts and PDFs. It is intentionally treated as alternative
intelligence: useful for finding expectations, channel checks, sell-side lenses,
and tradable narratives, but not as filing-grade proof.
"""

from __future__ import annotations

import json
import re
import sqlite3
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable

from tradingagents.dataflows.config import get_config

try:  # Optional: only used to add company name/industry search terms.
    from tradingagents.dataflows.tushare_a_stock import _fetch_stock_basic
except Exception:  # pragma: no cover - defensive import guard
    _fetch_stock_basic = None


_REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_KP_DB = _REPO_ROOT / "data" / "knowledge_planet" / "index.sqlite"

INFORMATION_RICH_TYPES = {
    "industry_weekly_data",
    "industry_data_snippet",
    "channel_check",
    "expert_call",
    "company_research_feedback",
    "broker_survey_data",
}

SELL_SIDE_TYPES = {
    "sell_side_push",
    "strategy_view",
    "broker_report_summary",
    "report_list_post",
}

NOISE_TYPES = {"market_joke", "rumor", "unverified_rumor", "raw_note"}

HARD_INFO_KEYWORDS = (
    "订单",
    "排产",
    "产能",
    "出货",
    "库存",
    "价格",
    "涨价",
    "降价",
    "客户",
    "验证",
    "招标",
    "中标",
    "合同",
    "毛利",
    "净利",
    "利润",
    "收入",
    "ASP",
    "SMM",
    "库存",
    "周度",
    "调研",
    "会议",
)

PUMP_KEYWORDS = (
    "强call",
    "大call",
    "重点推荐",
    "目标市值",
    "翻倍",
    "十倍",
    "千亿",
    "空间巨大",
    "现价",
    "弹性巨大",
    "重磅推荐",
)

CATALYST_KEYWORDS = (
    "公告",
    "订单",
    "业绩",
    "财报",
    "股东大会",
    "新品",
    "发布",
    "政策",
    "涨价",
    "降价",
    "去库",
    "扩产",
    "收购",
    "并购",
)

THEME_KEYWORDS = (
    "AI",
    "算力",
    "国产算力",
    "半导体",
    "机器人",
    "光伏",
    "锂电",
    "碳酸锂",
    "券商",
    "非银",
    "保险",
    "游戏",
    "医美",
    "量子",
    "风电",
    "光模块",
    "PCB",
    "存储",
    "食品饮料",
)

CANDIDATE_STOPWORDS = {
    "国产算力",
    "先进制程",
    "订单",
    "产能",
    "库存",
    "价格",
    "调研",
    "更新",
    "投资梳理",
    "数据库",
    "周报",
    "策略",
    "观点",
    "外资研报",
}

BROKER_TEAM_PREFIXES = (
    "国金",
    "中泰",
    "天风",
    "中信",
    "高盛",
    "东吴",
    "广发",
    "招商",
    "申万",
    "华泰",
    "海通",
    "国盛",
    "民生",
    "浙商",
    "西部",
)


@dataclass(frozen=True)
class KpItem:
    row_id: int
    title: str
    text: str
    summary: str
    source_type: str
    credibility: str
    published_at: str
    author: str
    source_file: str
    tickers: tuple[str, ...]
    companies: tuple[str, ...]
    industries: tuple[str, ...]
    themes: tuple[str, ...]


@dataclass(frozen=True)
class KpReport:
    row_id: int
    title: str
    summary: str
    broker: str
    published_at: str
    stored_path: str
    extracted_text_path: str
    tickers: tuple[str, ...]
    companies: tuple[str, ...]
    industries: tuple[str, ...]
    themes: tuple[str, ...]


def _db_path() -> Path:
    configured = get_config().get("knowledge_planet_db_path")
    return Path(configured).expanduser().resolve() if configured else DEFAULT_KP_DB


def _enabled() -> bool:
    return bool(get_config().get("knowledge_planet_enabled", True))


def _json_tuple(value: str | None) -> tuple[str, ...]:
    if not value:
        return ()
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return ()
    if isinstance(parsed, list):
        return tuple(str(item) for item in parsed if str(item).strip())
    return ()


def _connect() -> sqlite3.Connection | None:
    db_path = _db_path()
    if not db_path.exists():
        return None
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def _parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    text = str(value).strip()
    match = re.search(
        r"(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})(?:\s+(\d{1,2}):(\d{2}))?",
        text,
    )
    if match:
        year, month, day, hour, minute = match.groups()
        return datetime(
            int(year),
            int(month),
            int(day),
            int(hour or 0),
            int(minute or 0),
        )
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y%m%d"):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        return None


def _date_window(curr_date: str, look_back_days: int) -> tuple[str, str]:
    end = _parse_date(curr_date) or datetime.now()
    start = end - timedelta(days=max(0, int(look_back_days or 0)))
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


def _safe_like_term(term: str) -> str:
    return f"%{term.replace('%', '').replace('_', '')}%"


def _row_to_item(row: sqlite3.Row) -> KpItem:
    return KpItem(
        row_id=int(row["id"]),
        title=str(row["title"] or ""),
        text=str(row["text"] or ""),
        summary=str(row["summary"] or ""),
        source_type=str(row["source_type"] or ""),
        credibility=str(row["credibility"] or ""),
        published_at=str(row["published_at"] or ""),
        author=str(row["author"] or ""),
        source_file=str(row["source_file"] or ""),
        tickers=_json_tuple(row["tickers_json"]),
        companies=_json_tuple(row["company_names_json"]),
        industries=_json_tuple(row["industries_json"]),
        themes=_json_tuple(row["themes_json"]),
    )


def _row_to_report(row: sqlite3.Row) -> KpReport:
    return KpReport(
        row_id=int(row["id"]),
        title=str(row["title"] or ""),
        summary=str(row["summary"] or ""),
        broker=str(row["broker"] or row["broker_short"] or ""),
        published_at=str(row["published_at"] or ""),
        stored_path=str(row["stored_path"] or ""),
        extracted_text_path=str(row["extracted_text_path"] or ""),
        tickers=_json_tuple(row["tickers_json"]),
        companies=_json_tuple(row["company_names_json"]),
        industries=_json_tuple(row["industries_json"]),
        themes=_json_tuple(row["themes_json"]),
    )


def infer_private_source_type(text: str, current: str = "") -> str:
    """Upgrade coarse import labels into research-useful source classes."""
    body = f"{current}\n{text}"
    if re.search(r"(渠道|终端|经销商|客户|供应商|订单|验证|送样)", body):
        return "channel_check"
    if re.search(r"(周度|数据库|库存|价格|排产|出货|SMM|PPI|开工率|稼动率)", body):
        return "industry_weekly_data"
    if re.search(r"(调研|会议纪要|交流|专家|反馈|产业链)", body):
        return "company_research_feedback"
    if re.search(r"(目标市值|强call|重点推荐|大call|翻倍|现价)", body):
        return "sell_side_push"
    if current and current != "raw_note":
        return current
    return "raw_note"


def infer_credibility(source_type: str) -> str:
    if source_type in {"industry_weekly_data", "industry_data_snippet"}:
        return "broker_survey_or_industry_data"
    if source_type == "channel_check":
        return "high_private_channel_hard_to_verify"
    if source_type == "company_research_feedback":
        return "research_feedback_hard_to_publicly_verify"
    if source_type == "sell_side_push":
        return "sell_side_view_with_optimism_bias"
    if source_type in {"unverified_rumor", "rumor"}:
        return "unverified_rumor"
    if source_type == "market_joke":
        return "sentiment_only"
    return "unclassified_needs_review"


def _stock_terms(ticker: str) -> list[str]:
    terms = []
    raw = str(ticker or "").strip()
    if raw:
        terms.append(raw)
        terms.append(raw.upper())
        terms.append(raw.replace(".", ""))
        if "." in raw:
            terms.append(raw.split(".")[0])

    if _fetch_stock_basic and re.match(r"^\d{6}\.(SH|SZ|BJ)$", raw.upper()):
        try:
            basic = _fetch_stock_basic(raw.upper())
            if basic is not None:
                for field in ("name", "industry"):
                    value = str(basic.get(field) or "").strip()
                    if value:
                        terms.append(value)
        except Exception:
            pass

    unique = []
    for term in terms:
        term = term.strip()
        if len(term) >= 2 and term not in unique:
            unique.append(term)
    return unique


def _query_items(
    conn: sqlite3.Connection,
    *,
    terms: list[str],
    start_date: str,
    end_date: str,
    limit: int,
) -> list[KpItem]:
    if not terms:
        return []
    clauses = []
    params: list[str] = [start_date, f"{end_date} 23:59"]
    for term in terms:
        like = _safe_like_term(term)
        clauses.append(
            "(title LIKE ? OR text LIKE ? OR summary LIKE ? OR tickers_json LIKE ? OR company_names_json LIKE ? OR industries_json LIKE ? OR themes_json LIKE ?)"
        )
        params.extend([like, like, like, like, like, like, like])
    sql = f"""
        SELECT *
        FROM kp_items
        WHERE COALESCE(NULLIF(published_at, ''), imported_at) >= ?
          AND COALESCE(NULLIF(published_at, ''), imported_at) <= ?
          AND ({' OR '.join(clauses)})
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) DESC, id DESC
        LIMIT {int(limit)}
    """
    return [_row_to_item(row) for row in conn.execute(sql, params)]


def _query_reports(
    conn: sqlite3.Connection,
    *,
    terms: list[str],
    start_date: str,
    end_date: str,
    limit: int,
) -> list[KpReport]:
    if not terms:
        return []
    clauses = []
    params: list[str] = [start_date, f"{end_date} 23:59"]
    for term in terms:
        like = _safe_like_term(term)
        clauses.append(
            "(r.title LIKE ? OR r.summary LIKE ? OR r.tickers_json LIKE ? OR r.company_names_json LIKE ? OR r.industries_json LIKE ? OR r.themes_json LIKE ? OR t.text LIKE ?)"
        )
        params.extend([like, like, like, like, like, like, like])
    sql = f"""
        SELECT DISTINCT r.*
        FROM kp_reports r
        LEFT JOIN kp_report_text_fts t ON CAST(t.report_id AS INTEGER) = r.id
        WHERE COALESCE(NULLIF(r.published_at, ''), r.imported_at) >= ?
          AND COALESCE(NULLIF(r.published_at, ''), r.imported_at) <= ?
          AND ({' OR '.join(clauses)})
        ORDER BY COALESCE(NULLIF(r.published_at, ''), r.imported_at) DESC, r.id DESC
        LIMIT {int(limit)}
    """
    return [_row_to_report(row) for row in conn.execute(sql, params)]


def _compact_text(text: str, max_chars: int) -> str:
    cleaned = re.sub(r"\s+", " ", text or "").strip()
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 3].rstrip() + "..."


def _score_item(item: KpItem) -> dict[str, int]:
    text = f"{item.title}\n{item.text}\n{item.summary}"
    source_type = infer_private_source_type(text, item.source_type)
    hard_info = sum(1 for kw in HARD_INFO_KEYWORDS if kw.lower() in text.lower())
    catalyst = sum(1 for kw in CATALYST_KEYWORDS if kw.lower() in text.lower())
    pump = sum(1 for kw in PUMP_KEYWORDS if kw.lower() in text.lower())
    source_quality = 0
    if source_type in INFORMATION_RICH_TYPES:
        source_quality = 30
    elif source_type in SELL_SIDE_TYPES:
        source_quality = 18
    elif source_type in NOISE_TYPES:
        source_quality = 6
    return {
        "hard_info": min(35, hard_info * 5),
        "catalyst": min(20, catalyst * 4),
        "source_quality": source_quality,
        "pump_risk": min(30, pump * 7),
    }


def _extract_candidate_names(text: str) -> list[str]:
    names: list[str] = []
    bracket_names = [match.group(1).strip() for match in re.finditer(r"【([^】]{2,24})】", text)]
    hashtag_names = [match.group(1).strip() for match in re.finditer(r"#([^#\n]{2,16})#", text)]
    for name in [*bracket_names, *hashtag_names]:
        if _looks_like_candidate_name(name):
            names.append(name)
    for match in re.finditer(r"\b\d{6}\.(?:SH|SZ|BJ)\b|\(([A-Z]{1,5})\)", text):
        value = match.group(0).strip("()")
        names.append(value)
    unique = []
    for name in names:
        if name not in unique:
            unique.append(name)
    return unique


def _looks_like_candidate_name(name: str) -> bool:
    cleaned = name.strip().strip("：:，,。；; ")
    if len(cleaned) < 2 or len(cleaned) > 12:
        return False
    if cleaned.startswith("#") or " " in cleaned:
        return False
    if any(token in cleaned for token in ("欢迎", "沟通", "私下", "勿转", "领导", "详情况")):
        return False
    if cleaned in CANDIDATE_STOPWORDS or cleaned in THEME_KEYWORDS:
        return False
    if re.fullmatch(r"[A-Z]{5,}", cleaned):
        return False
    if any(cleaned.startswith(prefix) for prefix in BROKER_TEAM_PREFIXES) and len(cleaned) <= 6:
        return False
    return True


def get_knowledge_planet_context(
    ticker: str,
    curr_date: str,
    look_back_days: int | None = None,
    max_items: int | None = None,
    max_reports: int | None = None,
) -> str:
    """Return local alternative-intelligence context for one stock."""
    if not _enabled():
        return "# Knowledge Planet intelligence context disabled\n\n- Reason: `knowledge_planet_enabled` is false."

    conn = _connect()
    if conn is None:
        return "# Knowledge Planet intelligence context unavailable\n\n- Reason: local index.sqlite was not found. Run scripts/import_knowledge_planet.cmd first."

    config = get_config()
    lookback = int(
        config.get("knowledge_planet_lookback_days", 30)
        if look_back_days is None
        else look_back_days
    )
    item_limit = int(
        config.get("knowledge_planet_max_items", 30)
        if max_items is None
        else max_items
    )
    report_limit = int(
        config.get("knowledge_planet_max_reports", 12)
        if max_reports is None
        else max_reports
    )
    start_date, end_date = _date_window(curr_date, lookback)
    terms = _stock_terms(ticker)

    items = _query_items(conn, terms=terms, start_date=start_date, end_date=end_date, limit=item_limit)
    reports = _query_reports(conn, terms=terms, start_date=start_date, end_date=end_date, limit=report_limit)
    conn.close()

    lines = [
        f"# Knowledge Planet Alternative Intelligence Context for {ticker}",
        "",
        f"- Window: {start_date} to {end_date} ({lookback} days)",
        f"- Query terms: {', '.join(terms) if terms else '(none)'}",
        f"- Matched stream items: {len(items)}",
        f"- Matched PDF reports: {len(reports)}",
        "- Evidence discipline: this is alternative/local research intelligence. Industry weekly data, channel checks, and company research feedback may be valuable hard-to-publicly-verify clues; sell-side pushes and target-market-cap claims require story-to-profit validation.",
        "",
    ]

    if not items and not reports:
        lines.extend(
            [
                "## Status",
                "No relevant Knowledge Planet stream items or PDF reports were found for this window.",
            ]
        )
        return "\n".join(lines)

    if items:
        lines.extend(["## Recent Stream Intelligence", "", "| date | type | credibility | title | use |", "| --- | --- | --- | --- | --- |"])
        for item in items[:item_limit]:
            text = f"{item.title}\n{item.text}"
            source_type = infer_private_source_type(text, item.source_type)
            credibility = infer_credibility(source_type)
            use = "private data / channel clue" if source_type in INFORMATION_RICH_TYPES else "sell-side lens / sentiment clue"
            if source_type in {"sell_side_push", "strategy_view"}:
                use = "requires expectation-gap and valuation bridge"
            lines.append(
                f"| {item.published_at[:16]} | {source_type} | {credibility} | {_compact_text(item.title, 80)} | {use} |"
            )
        lines.append("")
        lines.append("### Stream Item Notes")
        for item in items[: min(10, item_limit)]:
            text = f"{item.title}\n{item.text}"
            source_type = infer_private_source_type(text, item.source_type)
            lines.extend(
                [
                    f"- **{_compact_text(item.title, 90)}** ({item.published_at[:16]}, {source_type}): {_compact_text(item.summary or item.text, 320)}",
                ]
            )
        lines.append("")

    if reports:
        lines.extend(["## Sell-Side Research Lens / PDF Matches", "", "| date | broker | title | use |", "| --- | --- | --- | --- |"])
        for report in reports[:report_limit]:
            lines.append(
                f"| {report.published_at[:10]} | {report.broker or 'unknown'} | {_compact_text(report.title, 100)} | extract framework, KPIs, assumptions, and optimism bias; do not inherit conclusion |"
            )
        lines.append("")

    lines.extend(
        [
            "## Required Agent Treatment",
            "- Use this context to discover what market participants may be trading and what sell-side frameworks are using.",
            "- Separate hard-to-publicly-verify but information-rich data from rumor or pure promotion.",
            "- Translate every promoted story into a product, revenue/profit driver, valuation assumption, catalyst clock, and falsification signal.",
            "- The bull case may use private/channel evidence as a tradable clue, but must label it as such and size conviction accordingly.",
            "- The bear case should attack optimistic sell-side bridges, target-market-cap leaps, crowded trades, and missing public verification without dismissing all private data as worthless.",
        ]
    )
    return "\n".join(lines)


def _items_for_window(conn: sqlite3.Connection, report_date: str, lookback_days: int) -> list[KpItem]:
    start_date, end_date = _date_window(report_date, lookback_days)
    rows = conn.execute(
        """
        SELECT *
        FROM kp_items
        WHERE COALESCE(NULLIF(published_at, ''), imported_at) >= ?
          AND COALESCE(NULLIF(published_at, ''), imported_at) <= ?
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) DESC, id DESC
        """,
        (start_date, f"{end_date} 23:59"),
    ).fetchall()
    return [_row_to_item(row) for row in rows]


def _reports_for_window(conn: sqlite3.Connection, report_date: str, lookback_days: int) -> list[KpReport]:
    start_date, end_date = _date_window(report_date, lookback_days)
    rows = conn.execute(
        """
        SELECT *
        FROM kp_reports
        WHERE COALESCE(NULLIF(published_at, ''), imported_at) >= ?
          AND COALESCE(NULLIF(published_at, ''), imported_at) <= ?
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) DESC, id DESC
        """,
        (start_date, f"{end_date} 23:59"),
    ).fetchall()
    return [_row_to_report(row) for row in rows]


def build_knowledge_planet_daily_report(
    report_date: str,
    look_back_days: int = 0,
    max_candidates: int = 30,
) -> str:
    """Build a deterministic theme-trading daily report from the local database."""
    conn = _connect()
    if conn is None:
        return "# Knowledge Planet Daily Report unavailable\n\n- Reason: local index.sqlite was not found. Run scripts/import_knowledge_planet.cmd first."

    items = _items_for_window(conn, report_date, look_back_days)
    reports = _reports_for_window(conn, report_date, look_back_days)
    conn.close()

    start_date, end_date = _date_window(report_date, look_back_days)
    source_counts = Counter(infer_private_source_type(f"{item.title}\n{item.text}", item.source_type) for item in items)
    theme_counts = Counter()
    candidate_scores: dict[str, dict[str, object]] = defaultdict(lambda: {"mentions": 0, "score": 0, "pump": 0, "items": []})
    information_items: list[tuple[KpItem, str]] = []
    pump_items: list[tuple[KpItem, int]] = []

    for item in items:
        text = f"{item.title}\n{item.text}\n{item.summary}"
        source_type = infer_private_source_type(text, item.source_type)
        for theme in THEME_KEYWORDS:
            if theme.lower() in text.lower():
                theme_counts[theme] += 1
        scores = _score_item(item)
        if source_type in INFORMATION_RICH_TYPES:
            information_items.append((item, source_type))
        if scores["pump_risk"] >= 14:
            pump_items.append((item, scores["pump_risk"]))
        names = _extract_candidate_names(text)
        if not names and item.tickers:
            names = list(item.tickers)
        for name in names[:5]:
            bucket = candidate_scores[name]
            bucket["mentions"] = int(bucket["mentions"]) + 1
            bucket["score"] = int(bucket["score"]) + scores["hard_info"] + scores["catalyst"] + scores["source_quality"]
            bucket["pump"] = int(bucket["pump"]) + scores["pump_risk"]
            cast_items = bucket["items"]
            if isinstance(cast_items, list) and len(cast_items) < 3:
                cast_items.append(item)

    ranked = sorted(
        candidate_scores.items(),
        key=lambda kv: (int(kv[1]["score"]) + int(kv[1]["mentions"]) * 8 - int(kv[1]["pump"]) * 0.35),
        reverse=True,
    )[:max_candidates]

    lines = [
        f"# Knowledge Planet Theme Trading Daily - {end_date}",
        "",
        f"- Window: {start_date} to {end_date}",
        f"- Stream items: {len(items)}",
        f"- PDF reports: {len(reports)}",
        "- Purpose: discover tradable narratives, high-value private/channel clues, sell-side research lenses, and pump-risk names. This is not a standalone buy list.",
        "",
        "## Source Mix",
        "",
        "| source type | count | treatment |",
        "| --- | ---: | --- |",
    ]
    for source_type, count in source_counts.most_common():
        treatment = "information-rich clue" if source_type in INFORMATION_RICH_TYPES else "sell-side / sentiment / needs bridge"
        if source_type in NOISE_TYPES:
            treatment = "low-confidence unless corroborated"
        lines.append(f"| {source_type} | {count} | {treatment} |")

    lines.extend(["", "## Narrative Heat Map", "", "| theme | mentions |", "| --- | ---: |"])
    for theme, count in theme_counts.most_common(15):
        lines.append(f"| {theme} | {count} |")

    lines.extend(
        [
            "",
            "## Candidate Ranking",
            "",
            "| rank | candidate | mentions | theme score | pump risk | initial bucket | evidence notes |",
            "| ---: | --- | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for idx, (name, data) in enumerate(ranked, start=1):
        score = int(data["score"])
        pump = int(data["pump"])
        if score >= 55 and pump < 20:
            bucket = "A: deep-dive / build candidate"
        elif score >= 35 and pump < 35:
            bucket = "B: theme watch"
        elif pump >= 35:
            bucket = "D: pump-risk watch"
        else:
            bucket = "C: tactical only"
        item_list = data.get("items", [])
        note = ""
        if isinstance(item_list, list) and item_list:
            note = _compact_text("; ".join(item.title for item in item_list), 180)
        lines.append(f"| {idx} | {name} | {data['mentions']} | {score} | {pump} | {bucket} | {note} |")

    lines.extend(["", "## High-Value Industry / Research Clues"])
    if information_items:
        for item, source_type in information_items[:20]:
            lines.append(
                f"- **{_compact_text(item.title, 100)}** ({source_type}, {item.published_at[:16]}): {_compact_text(item.summary or item.text, 260)}"
            )
    else:
        lines.append("- No information-rich industry data or research-feedback items were identified in this window.")

    lines.extend(["", "## Sell-Side Push / Pump-Risk Watch"])
    if pump_items:
        for item, risk in sorted(pump_items, key=lambda pair: pair[1], reverse=True)[:15]:
            lines.append(
                f"- **{_compact_text(item.title, 100)}** (pump risk {risk}): require story-to-profit bridge, catalyst clock, valuation digestion, and price/volume confirmation."
            )
    else:
        lines.append("- No high pump-risk items were identified by keyword rules.")

    lines.extend(["", "## PDF Research Lens"])
    if reports:
        for report in reports[:20]:
            lines.append(
                f"- **{_compact_text(report.title, 120)}** ({report.broker or 'unknown'}, {report.published_at[:10]}): use to extract business/KPI framework, forecast assumptions, comparable companies, and optimism bias."
            )
    else:
        lines.append("- No PDF reports were imported for this window.")

    lines.extend(
        [
            "",
            "## Trading Desk Checklist",
            "- Do not buy the hottest name solely from mention count. Require price/volume confirmation and avoid late acceleration without a new catalyst.",
            "- For A/B candidates, run single-stock TradingAgents analysis with Knowledge Planet context enabled before sizing.",
            "- For private/channel data, keep the label `hard_to_publicly_verify` but do not discard it; instead define the next observable proxy.",
            "- For sell-side target-market-cap stories, force product -> revenue -> margin -> EPS/FCF -> valuation bridge.",
            "- Track 1/3/5/10-day forward returns by candidate and source to build a source-quality score over time.",
        ]
    )
    return "\n".join(lines)
