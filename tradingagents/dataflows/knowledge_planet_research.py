"""Local Knowledge Planet intelligence retrieval and daily synthesis.

The Knowledge Planet database is a private, local research layer built from
manually imported posts and PDFs. It is intentionally treated as alternative
intelligence: useful for finding expectations, channel checks, sell-side lenses,
and tradable narratives, but not as filing-grade proof.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, Iterable

from tradingagents.dataflows.config import get_config

try:  # Optional: only used to add company name/industry search terms.
    from tradingagents.dataflows.tushare_a_stock import (
        TushareDataError,
        _fetch_daily_basic_latest,
        _fetch_daily_with_backfill,
        _fetch_fina_indicator,
        _fetch_stock_basic,
        resolve_a_share_symbol,
    )
except Exception:  # pragma: no cover - defensive import guard
    TushareDataError = Exception
    _fetch_daily_basic_latest = None
    _fetch_daily_with_backfill = None
    _fetch_fina_indicator = None
    _fetch_stock_basic = None
    resolve_a_share_symbol = None


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

THEME_DISPLAY_NAMES = {
    "earnings": "业绩/指引",
    "price": "价格/涨价",
    "valuation": "估值重估",
    "inventory": "库存/供需",
    "liquidity": "流动性/风偏",
    "destocking": "去库",
    "export": "出口链",
    "AI": "AI",
}

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

CANDIDATE_NOISE_SUBSTRINGS = (
    "核心",
    "产品",
    "进展",
    "估值",
    "水平",
    "海外",
    "正在",
    "产业",
    "情况",
    "逻辑",
    "机会",
    "行业",
    "会议",
    "纪要",
    "重点",
    "梳理",
    "更新",
    "关注",
    "观点",
    "汇报",
    "周期",
    "上行",
)

COMMON_A_SHARE_ALIASES = {
    "宁德时代": "300750.SZ",
    "寒武纪": "688256.SH",
    "寒武纪-U": "688256.SH",
    "国瓷材料": "300285.SZ",
    "元力股份": "300174.SZ",
    "深科达": "688328.SH",
    "三未信安": "688489.SH",
    "海光": "688041.SH",
    "海光信息": "688041.SH",
    "芯原": "688521.SH",
    "芯原股份": "688521.SH",
    "中芯": "688981.SH",
    "中芯国际": "688981.SH",
    "华虹": "688347.SH",
    "华虹公司": "688347.SH",
    "裕同科技": "002831.SZ",
    "和胜股份": "002824.SZ",
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


@dataclass(frozen=True)
class CandidateMarketScore:
    candidate: str
    symbol: str
    company_name: str
    industry: str
    fundamental_score: int | None
    technical_score: int | None
    total_market_score: int | None
    summary: str
    status: str


@dataclass(frozen=True)
class KpEventSignal:
    event_type: str
    confidence: str
    source_type: str
    title: str
    published_at: str
    interpretation: str
    verification: str
    risk: str
    tickers: tuple[str, ...]
    companies: tuple[str, ...]
    themes: tuple[str, ...]


@dataclass(frozen=True)
class CandidateLLMAnalysis:
    candidate: str
    logic_score: int | None
    information_quality: str
    signal_interpretation: str
    expectation_gap: str
    thesis_path: str
    company_relevance: str
    win_rate_view: str
    payoff_risk: str
    catalyst_clock: str
    verification_points: str
    falsification_points: str
    entry_plan: str
    position_sizing: str
    trading_action: str
    risk_flags: str
    summary: str
    status: str


@dataclass(frozen=True)
class _SimpleLLMResponse:
    content: str


def _load_local_env_value(key: str) -> str:
    value = (os.getenv(key) or "").strip()
    if value:
        return value
    for env_path in (Path.cwd() / ".env", _REPO_ROOT / ".env"):
        if not env_path.exists():
            continue
        for raw_line in env_path.read_text(encoding="utf-8-sig").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            env_key, env_value = line.split("=", 1)
            if env_key.strip() != key:
                continue
            return env_value.strip().strip('"').strip("'")
    return ""


class _DirectDeepSeekLLM:
    def __init__(self, model: str, base_url: str | None = None, timeout: int = 90):
        self.model = model
        self.base_url = (base_url or "https://api.deepseek.com").rstrip("/")
        self.timeout = timeout
        self.api_key = _load_local_env_value("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise RuntimeError("DEEPSEEK_API_KEY is not configured in environment or .env")

    def invoke(self, input_):
        if isinstance(input_, str):
            messages = [{"role": "user", "content": input_}]
        else:
            messages = []
            for message in input_:
                role = "user"
                class_name = message.__class__.__name__.lower()
                if "system" in class_name:
                    role = "system"
                elif "ai" in class_name or "assistant" in class_name:
                    role = "assistant"
                messages.append({"role": role, "content": str(getattr(message, "content", message))})
        payload = json.dumps(
            {
                "model": self.model,
                "messages": messages,
                "temperature": 0.2,
                "response_format": {"type": "json_object"},
            },
            ensure_ascii=False,
        ).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"DeepSeek HTTP {exc.code}: {_compact_text(body, 300)}") from exc
        data = json.loads(raw)
        content = data["choices"][0]["message"]["content"]
        return _SimpleLLMResponse(content=content)


def _create_market_analysis_llm(
    provider: str,
    model: str,
    base_url: str | None,
    progress: Callable[[str], None] | None = None,
):
    if provider.lower() == "deepseek":
        try:
            from tradingagents.llm_clients import create_llm_client

            return create_llm_client(
                provider=provider,
                model=model,
                base_url=base_url,
                timeout=90,
                max_retries=2,
            ).get_llm()
        except Exception as exc:
            if progress:
                progress(
                    "[llm market analysis] framework client unavailable, "
                    f"using direct DeepSeek fallback: {_compact_text(str(exc), 120)}"
                )
            return _DirectDeepSeekLLM(model=model, base_url=base_url)

    from tradingagents.llm_clients import create_llm_client

    return create_llm_client(
        provider=provider,
        model=model,
        base_url=base_url,
        timeout=90,
        max_retries=2,
    ).get_llm()


def _db_path() -> Path:
    configured = get_config().get("knowledge_planet_db_path")
    return Path(configured).expanduser().resolve() if configured else DEFAULT_KP_DB


def _enabled() -> bool:
    return bool(get_config().get("knowledge_planet_enabled", True))


def _auto_sync_enabled() -> bool:
    return bool(get_config().get("knowledge_planet_auto_sync_enabled", True))


def _sync_state_dir() -> Path:
    return _db_path().parent / ".sync_state"


def _sync_stamp_path(sync_date: str) -> Path:
    safe_date = re.sub(r"[^0-9-]", "_", str(sync_date or ""))[:20] or "unknown"
    return _sync_state_dir() / f"zsxq_{safe_date}.ok"


def _run_project_script(args: list[str], timeout: int = 900) -> tuple[int, str]:
    completed = subprocess.run(
        [sys.executable, *args],
        cwd=str(_REPO_ROOT),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=timeout,
    )
    output = "\n".join(part for part in (completed.stdout.strip(), completed.stderr.strip()) if part)
    return completed.returncode, output


def ensure_knowledge_planet_upstream_synced(
    sync_date: str,
    *,
    force: bool = False,
    progress: Callable[[str], None] | None = None,
) -> str:
    """Sync zsxq upstream data and import it before local reads.

    This is deliberately best-effort. TradingAgents should still be able to use
    the last local index if network/login/PDF downloads fail.
    """
    if not _enabled():
        return "disabled"
    if not _auto_sync_enabled():
        return "auto_sync_disabled"
    if os.getenv("PYTEST_CURRENT_TEST"):
        return "auto_sync_skipped:pytest"

    sync_date = (sync_date or datetime.now().strftime("%Y-%m-%d"))[:10]
    stamp = _sync_stamp_path(sync_date)
    config = get_config()
    min_interval = int(config.get("knowledge_planet_auto_sync_min_interval_minutes", 30) or 0)
    if stamp.exists() and not force and min_interval > 0:
        stamp_age = datetime.now() - datetime.fromtimestamp(stamp.stat().st_mtime)
        if stamp_age < timedelta(minutes=min_interval):
            age_minutes = max(0, int(stamp_age.total_seconds() // 60))
            return f"recently_synced:{age_minutes}m:{stamp}"

    group_spec = str(config.get("knowledge_planet_auto_sync_group") or "").strip()
    if not group_spec:
        return "auto_sync_skipped:no_group"

    max_pages = int(config.get("knowledge_planet_auto_sync_max_pages", 20) or 20)
    max_images = int(config.get("knowledge_planet_auto_sync_max_image_downloads", 100) or 100)
    max_files = int(config.get("knowledge_planet_auto_sync_max_file_downloads", 50) or 50)

    sync_script = _REPO_ROOT / "scripts" / "sync_knowledge_planet_from_zsxq.py"
    import_script = _REPO_ROOT / "scripts" / "import_knowledge_planet.py"
    if not sync_script.exists() or not import_script.exists():
        return "auto_sync_failed:missing_scripts"

    if progress:
        progress(f"[knowledge planet sync] syncing {group_spec} for {sync_date}")

    sync_args = [
        str(sync_script),
        "--date",
        sync_date,
        "--group-id",
        group_spec,
        "--max-pages",
        str(max_pages),
        "--max-image-downloads",
        str(max_images),
        "--max-file-downloads",
        str(max_files),
    ]
    try:
        sync_code, sync_output = _run_project_script(sync_args, timeout=1200)
    except Exception as exc:
        return f"auto_sync_failed:sync_exception:{_compact_text(str(exc), 180)}"
    if sync_code != 0:
        return f"auto_sync_failed:sync_exit_{sync_code}:{_compact_text(sync_output, 240)}"

    if progress and sync_output:
        progress(_compact_text(sync_output, 500))

    try:
        import_code, import_output = _run_project_script([str(import_script)], timeout=1200)
    except Exception as exc:
        return f"auto_sync_failed:import_exception:{_compact_text(str(exc), 180)}"
    if import_code != 0:
        return f"auto_sync_failed:import_exit_{import_code}:{_compact_text(import_output, 240)}"

    _sync_state_dir().mkdir(parents=True, exist_ok=True)
    stamp.write_text(
        "\n".join(
            [
                f"date={sync_date}",
                f"group={group_spec}",
                f"synced_at={datetime.now().isoformat(timespec='seconds')}",
                "",
                sync_output,
                "",
                import_output,
            ]
        ),
        encoding="utf-8",
    )
    if progress:
        progress(f"[knowledge planet sync] done; stamp={stamp}")
    return f"synced:{stamp}"


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


def _event_type_for_text(text: str, source_type: str) -> str:
    checks = [
        ("订单/排产", ("订单", "排产", "出货", "交付", "产能利用率")),
        ("涨价/价格弹性", ("涨价", "提价", "价格", "价差", "ASP")),
        ("库存/供需", ("库存", "去库", "补库", "供给", "紧缺", "短缺")),
        ("客户验证/导入", ("验证", "送样", "客户", "认证", "导入", "中标")),
        ("产能/扩产", ("扩产", "产能", "投产", "量产", "爬坡")),
        ("政策/监管", ("政策", "限制", "出口管制", "补贴", "监管", "会议")),
        ("业绩/指引", ("业绩", "指引", "上修", "利润", "收入", "毛利")),
        ("海外映射", ("美股", "海外", "英伟达", "台积电", "美光", "高盛", "BofA", "Morgan")),
        ("研报框架", ("研报", ".pdf", "PDF", "外资研报", "深度")),
    ]
    for label, keywords in checks:
        if any(keyword.lower() in text.lower() for keyword in keywords):
            return label
    if source_type in SELL_SIDE_TYPES:
        return "卖方观点/情绪"
    return "其他线索"


def _event_confidence(source_type: str, text: str, pump_risk: int) -> str:
    has_numbers = bool(re.search(r"\d+(?:\.\d+)?\s*(?:%|亿|万|吨|台|元|美元|平|w|W)", text))
    has_verbs = any(word in text for word in ("订单", "排产", "库存", "价格", "验证", "客户", "产能", "交付"))
    if source_type in INFORMATION_RICH_TYPES and has_numbers and has_verbs:
        return "高：数据/调研线索"
    if source_type in INFORMATION_RICH_TYPES:
        return "中高：调研/渠道线索"
    if source_type in SELL_SIDE_TYPES and pump_risk >= 14:
        return "低：卖方强推待验证"
    if source_type in SELL_SIDE_TYPES:
        return "中：卖方框架待验证"
    if source_type in NOISE_TYPES:
        return "低：噪声/传闻"
    return "中：普通线索"


def _verification_hint(event_type: str) -> str:
    return {
        "订单/排产": "跟踪订单公告、排产环比、客户确认、收入兑现节奏。",
        "涨价/价格弹性": "跟踪报价、毛利率、竞品价格、下游接受度。",
        "库存/供需": "跟踪库存周度数据、开工率、现货/期货价格。",
        "客户验证/导入": "跟踪送样验证进度、认证节点、批量订单。",
        "产能/扩产": "跟踪投产时间、良率、资本开支和产能利用率。",
        "政策/监管": "跟踪政策落地细则、受益范围和执行强度。",
        "业绩/指引": "跟踪季度收入、利润、毛利率和管理层指引。",
        "海外映射": "跟踪海外龙头业绩/指引与A股映射链条是否直接。",
        "研报框架": "提取业务/KPI框架，回到公告、财务和行情交叉验证。",
        "卖方观点/情绪": "强制拆产品到利润桥，观察量价确认和拥挤度。",
    }.get(event_type, "定义下一个可观察代理指标。")


def _event_risk_hint(event_type: str, confidence: str) -> str:
    if "低" in confidence:
        return "只能作为观察线索，不能单独触发交易。"
    if event_type in {"海外映射", "卖方观点/情绪"}:
        return "警惕映射链过长、已被交易拥挤或卖方乐观假设。"
    if event_type in {"涨价/价格弹性", "库存/供需"}:
        return "警惕价格信号短周期反复，需确认能否传导到公司利润。"
    return "需确认是否已被股价提前定价。"


def _parse_event_signal(item: KpItem, source_type: str, scores: dict[str, int]) -> KpEventSignal:
    text = f"{item.title}\n{item.text}\n{item.summary}"
    event_type = _event_type_for_text(text, source_type)
    confidence = _event_confidence(source_type, text, scores.get("pump_risk", 0))
    interpretation = f"{event_type}：{_compact_text(item.summary or item.text or item.title, 180)}"
    return KpEventSignal(
        event_type=event_type,
        confidence=confidence,
        source_type=source_type,
        title=item.title,
        published_at=item.published_at,
        interpretation=interpretation,
        verification=_verification_hint(event_type),
        risk=_event_risk_hint(event_type, confidence),
        tickers=item.tickers,
        companies=item.companies,
        themes=item.themes,
    )


def _extract_candidate_names(text: str) -> list[str]:
    names: list[str] = []
    bracket_names = [match.group(1).strip() for match in re.finditer(r"【([^】]{2,24})】", text)]
    hashtag_names = [match.group(1).strip() for match in re.finditer(r"#([^#\n]{2,16})#", text)]
    for name in [*bracket_names, *hashtag_names]:
        for part in re.split(r"[、/，,]", name):
            if _looks_like_candidate_name(part):
                names.append(part.strip().strip("：:，,。；; "))
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
    if any(token in cleaned for token in CANDIDATE_NOISE_SUBSTRINGS):
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


def _to_float(value: object) -> float | None:
    try:
        if value is None:
            return None
        text = str(value).strip()
        if not text or text.lower() in {"nan", "none", "<na>"}:
            return None
        return float(text)
    except Exception:
        return None


def _score_range(value: float | None, bands: list[tuple[float, int]]) -> int:
    if value is None:
        return 0
    for threshold, score in bands:
        if value >= threshold:
            return score
    return 0


def _format_metric(label: str, value: float | None, suffix: str = "") -> str | None:
    if value is None:
        return None
    return f"{label} {value:.1f}{suffix}"


def _pct_change(series, periods: int) -> float | None:
    if series is None or len(series) <= periods:
        return None
    base = float(series.iloc[-periods - 1])
    latest = float(series.iloc[-1])
    if not base:
        return None
    return (latest / base - 1) * 100


def _resolve_candidate_symbol(name: str) -> str | None:
    normalized = str(name or "").strip()
    if re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", normalized, flags=re.IGNORECASE):
        return normalized.upper()
    if normalized in COMMON_A_SHARE_ALIASES:
        return COMMON_A_SHARE_ALIASES[normalized]
    if not resolve_a_share_symbol:
        return None
    try:
        return resolve_a_share_symbol(normalized)
    except Exception:
        return None


def _latest_fina_row(symbol: str, report_date: str, notes: list[str] | None = None):
    if not _fetch_fina_indicator:
        return None
    try:
        data = _fetch_fina_indicator(symbol, report_date)
    except Exception as exc:
        if notes is not None:
            notes.append(f"财务指标不可用: {_compact_text(str(exc), 80)}")
        return None
    if data is None or getattr(data, "empty", True):
        return None
    return data.iloc[0]


def _score_candidate_market(candidate: str, report_date: str) -> CandidateMarketScore:
    symbol = _resolve_candidate_symbol(candidate)
    if not symbol:
        return CandidateMarketScore(
            candidate=candidate,
            symbol="",
            company_name="",
            industry="",
            fundamental_score=None,
            technical_score=None,
            total_market_score=None,
            summary="未能解析为 A 股代码，暂不做基本面/技术面评分",
            status="unresolved",
        )

    basic = None
    if _fetch_stock_basic:
        try:
            basic = _fetch_stock_basic(symbol)
        except Exception:
            basic = None
    company_name = str((basic.get("name") if basic is not None else None) or candidate or "").strip()
    industry = str((basic.get("industry") if basic is not None else None) or "").strip()

    fundamental_score: int | None = None
    technical_score: int | None = None
    notes: list[str] = []

    daily_basic = None
    if _fetch_daily_basic_latest:
        try:
            daily_basic = _fetch_daily_basic_latest(symbol, report_date)
        except Exception as exc:
            notes.append(f"估值快照不可用: {_compact_text(str(exc), 80)}")

    fina = _latest_fina_row(symbol, report_date, notes)
    if daily_basic is not None or fina is not None:
        score = 0
        roe = _to_float(fina.get("roe") if fina is not None else None)
        roe_waa = _to_float(fina.get("roe_waa") if fina is not None else None)
        netprofit_yoy = _to_float(fina.get("netprofit_yoy") if fina is not None else None)
        revenue_yoy = _to_float(fina.get("or_yoy") if fina is not None else None)
        gross_margin = _to_float(fina.get("grossprofit_margin") if fina is not None else None)
        net_margin = _to_float(fina.get("netprofit_margin") if fina is not None else None)
        ocf_to_or = _to_float(fina.get("ocf_to_or") if fina is not None else None)
        debt_to_assets = _to_float(fina.get("debt_to_assets") if fina is not None else None)
        current_ratio = _to_float(fina.get("current_ratio") if fina is not None else None)
        pe_ttm = _to_float(daily_basic.get("pe_ttm") if daily_basic is not None else None)
        pb = _to_float(daily_basic.get("pb") if daily_basic is not None else None)
        total_mv_yi = _to_float(daily_basic.get("total_mv") if daily_basic is not None else None)
        circ_mv_yi = _to_float(daily_basic.get("circ_mv") if daily_basic is not None else None)
        total_mv_yi = total_mv_yi / 10000 if total_mv_yi is not None else None
        circ_mv_yi = circ_mv_yi / 10000 if circ_mv_yi is not None else None

        growth_score = 0
        growth_score += _score_range(netprofit_yoy, [(80, 8), (35, 7), (15, 5), (0, 2)])
        growth_score += _score_range(revenue_yoy, [(45, 6), (20, 5), (8, 3), (0, 1)])
        if netprofit_yoy is not None and netprofit_yoy < -20:
            growth_score -= 3
        if revenue_yoy is not None and revenue_yoy < -15:
            growth_score -= 2
        growth_score = max(0, min(14, growth_score))

        quality_score = 0
        effective_roe = roe if roe is not None else roe_waa
        quality_score += _score_range(effective_roe, [(22, 6), (15, 5), (9, 3), (3, 1)])
        quality_score += _score_range(gross_margin, [(45, 3), (25, 2), (12, 1)])
        quality_score += _score_range(net_margin, [(18, 2), (8, 1)])
        quality_score = max(0, min(10, quality_score))

        balance_score = 0
        balance_score += _score_range(ocf_to_or, [(25, 4), (10, 3), (0, 1)])
        if debt_to_assets is not None:
            if debt_to_assets <= 45:
                balance_score += 3
            elif debt_to_assets <= 65:
                balance_score += 2
            elif debt_to_assets <= 78:
                balance_score += 0
            else:
                balance_score -= 3
        if current_ratio is not None:
            if current_ratio >= 1.5:
                balance_score += 1
            elif current_ratio < 0.9:
                balance_score -= 1
        balance_score = max(0, min(8, balance_score))

        valuation_score = 0
        growth_anchor = max(
            [value for value in (netprofit_yoy, revenue_yoy) if value is not None],
            default=None,
        )
        if pe_ttm is not None:
            if 0 < pe_ttm <= 35:
                valuation_score += 4
            elif 35 < pe_ttm <= 80:
                valuation_score += 3 if (growth_anchor is not None and growth_anchor >= 25) else 1
            elif 80 < pe_ttm <= 150:
                valuation_score += 2 if (growth_anchor is not None and growth_anchor >= 50) else -1
            elif pe_ttm > 150:
                valuation_score -= 2
        if pb is not None:
            if 0 < pb <= 5:
                valuation_score += 2
            elif 5 < pb <= 12:
                valuation_score += 1
            elif pb > 20:
                valuation_score -= 2
        elastic_mv = circ_mv_yi if circ_mv_yi is not None else total_mv_yi
        if elastic_mv is not None:
            if 40 <= elastic_mv <= 600:
                valuation_score += 2
            elif 600 < elastic_mv <= 2000:
                valuation_score += 1
            elif elastic_mv > 4000:
                valuation_score -= 1
            elif elastic_mv < 25:
                valuation_score -= 1
        valuation_score = max(0, min(8, valuation_score))

        score = growth_score + quality_score + balance_score + valuation_score
        fundamental_score = max(0, min(40, score))
        parts = [
            _format_metric("收入同比", revenue_yoy, "%"),
            _format_metric("净利同比", netprofit_yoy, "%"),
            _format_metric("ROE", effective_roe, "%"),
            _format_metric("毛利率", gross_margin, "%"),
            _format_metric("PE(TTM)", pe_ttm),
            _format_metric("流通市值", elastic_mv, "亿"),
        ]
        parts = [part for part in parts if part]
        if parts:
            notes.append(
                "基本面: "
                f"题材承接 {fundamental_score}/40"
                f"（增长{growth_score}/14、质量{quality_score}/10、现金/负债{balance_score}/8、估值弹性{valuation_score}/8）；"
                + "，".join(parts)
            )
    else:
        notes.append("基本面数据不可用")

    if _fetch_daily_with_backfill:
        try:
            end_dt = _parse_date(report_date) or datetime.now()
            start_dt = end_dt - timedelta(days=220)
            daily, notice = _fetch_daily_with_backfill(
                symbol,
                start_dt.strftime("%Y-%m-%d"),
                end_dt.strftime("%Y-%m-%d"),
            )
            if daily is not None and not daily.empty and "Close" in daily.columns:
                ordered = daily.sort_values("Date").copy()
                close = ordered["Close"].astype(float)
                latest_close = float(close.iloc[-1])
                high = ordered["High"].astype(float) if "High" in ordered.columns else close
                amount = ordered["Amount"].astype(float) if "Amount" in ordered.columns else None
                pct = close.pct_change() * 100
                ma10 = float(close.tail(10).mean()) if len(close) >= 10 else None
                ma20 = float(close.tail(20).mean()) if len(close) >= 20 else None
                ma60 = float(close.tail(60).mean()) if len(close) >= 60 else None
                ret5 = _pct_change(close, 5)
                ret20 = _pct_change(close, 20)
                ret60 = _pct_change(close, 60)
                high60 = float(high.tail(60).max()) if len(high) >= 20 else None
                low60 = float(close.tail(60).min()) if len(close) >= 20 else None
                dist_high60 = (latest_close / high60 - 1) * 100 if high60 else None
                range_pos60 = (
                    (latest_close - low60) / (high60 - low60) * 100
                    if high60 and low60 is not None and high60 > low60
                    else None
                )
                vol20 = float(pct.tail(20).std()) if len(pct.dropna()) >= 20 else None
                amount_ratio = None
                if amount is not None and len(amount.dropna()) >= 21:
                    avg_amount20 = float(amount.tail(21).iloc[:-1].mean())
                    latest_amount = float(amount.iloc[-1])
                    if avg_amount20:
                        amount_ratio = latest_amount / avg_amount20

                trend_score = 0
                if ma10 and latest_close > ma10:
                    trend_score += 3
                if ma20 and latest_close > ma20:
                    trend_score += 4
                if ma60 and latest_close > ma60:
                    trend_score += 3
                if ma20 and ma60 and ma20 > ma60:
                    trend_score += 2
                trend_score = max(0, min(12, trend_score))

                momentum_score = 0
                if ret5 is not None:
                    if -3 <= ret5 <= 12:
                        momentum_score += 3
                    elif 12 < ret5 <= 25:
                        momentum_score += 1
                    elif ret5 > 25:
                        momentum_score -= 3
                    elif ret5 < -8:
                        momentum_score -= 2
                if ret20 is not None:
                    if 3 <= ret20 <= 28:
                        momentum_score += 4
                    elif 0 < ret20 < 3:
                        momentum_score += 2
                    elif 28 < ret20 <= 50:
                        momentum_score += 1
                    elif ret20 > 50:
                        momentum_score -= 4
                    elif ret20 < -15:
                        momentum_score -= 4
                if ret60 is not None:
                    if 5 <= ret60 <= 60:
                        momentum_score += 3
                    elif 60 < ret60 <= 100:
                        momentum_score += 1
                    elif ret60 > 100:
                        momentum_score -= 3
                    elif ret60 < -25:
                        momentum_score -= 3
                momentum_score = max(0, min(10, momentum_score))

                liquidity_score = 0
                turnover = _to_float(daily_basic.get("turnover_rate") if daily_basic is not None else None)
                volume_ratio = _to_float(daily_basic.get("volume_ratio") if daily_basic is not None else None)
                if turnover is not None:
                    if 1 <= turnover <= 12:
                        liquidity_score += 3
                    elif 12 < turnover <= 25:
                        liquidity_score += 1
                    elif turnover < 0.4:
                        liquidity_score -= 1
                    elif turnover > 30:
                        liquidity_score -= 2
                if volume_ratio is not None:
                    if 1.1 <= volume_ratio <= 4:
                        liquidity_score += 3
                    elif 4 < volume_ratio <= 7:
                        liquidity_score += 1
                    elif volume_ratio > 7:
                        liquidity_score -= 2
                if amount_ratio is not None:
                    if 1.1 <= amount_ratio <= 3.5:
                        liquidity_score += 2
                    elif amount_ratio > 6:
                        liquidity_score -= 1
                liquidity_score = max(0, min(8, liquidity_score))

                position_score = 0
                if range_pos60 is not None:
                    if 55 <= range_pos60 <= 92:
                        position_score += 4
                    elif 35 <= range_pos60 < 55:
                        position_score += 2
                    elif range_pos60 > 97:
                        position_score -= 1
                    elif range_pos60 < 20:
                        position_score -= 2
                if dist_high60 is not None:
                    if -12 <= dist_high60 <= -2:
                        position_score += 3
                    elif -2 < dist_high60 <= 1:
                        position_score += 2
                    elif dist_high60 < -25:
                        position_score -= 3
                if vol20 is not None:
                    if 1.0 <= vol20 <= 4.5:
                        position_score += 3
                    elif 4.5 < vol20 <= 7.0:
                        position_score += 1
                    elif vol20 > 8.0:
                        position_score -= 2
                position_score = max(0, min(10, position_score))

                technical_score = max(
                    0,
                    min(40, trend_score + momentum_score + liquidity_score + position_score),
                )
                tech_parts = [
                    f"交易位置 {technical_score}/40"
                    f"（趋势{trend_score}/12、动量{momentum_score}/10、量能{liquidity_score}/8、位置风险{position_score}/10）",
                    f"收盘 {latest_close:.2f}",
                ]
                if ret5 is not None:
                    tech_parts.append(f"5日 {ret5:.1f}%")
                if ret20 is not None:
                    tech_parts.append(f"20日 {ret20:.1f}%")
                if ret60 is not None:
                    tech_parts.append(f"60日 {ret60:.1f}%")
                if turnover is not None:
                    tech_parts.append(f"换手 {turnover:.1f}%")
                if amount_ratio is not None:
                    tech_parts.append(f"量能/20日均值 {amount_ratio:.1f}x")
                if dist_high60 is not None:
                    tech_parts.append(f"距60日高点 {dist_high60:.1f}%")
                if notice:
                    tech_parts.append("行情可能滞后")
                notes.append("技术面: " + "，".join(tech_parts))
            else:
                notes.append("技术面行情数据不可用")
        except Exception as exc:
            notes.append(f"技术面数据不可用: {_compact_text(str(exc), 80)}")
    else:
        notes.append("技术面接口不可用")

    available_scores = [score for score in (fundamental_score, technical_score) if score is not None]
    total = sum(available_scores) if available_scores else None
    status = "scored" if total is not None else "unscored"
    return CandidateMarketScore(
        candidate=candidate,
        symbol=symbol,
        company_name=company_name,
        industry=industry,
        fundamental_score=fundamental_score,
        technical_score=technical_score,
        total_market_score=total,
        summary="；".join(notes) if notes else "无补充说明",
        status=status,
    )


def _fundamental_validation(
    fundamental_score: int | None,
) -> tuple[str, int, int | None, bool]:
    """Map fundamentals into thesis validation, not an additive score.

    Returns label, score adjustment, optional total-score cap, and whether the
    name is eligible for the A bucket.
    """
    if fundamental_score is None:
        return "待验证", 0, 62, False
    if fundamental_score >= 30:
        return "验证通过", 12, None, True
    if fundamental_score >= 22:
        return "部分验证", 5, None, True
    if fundamental_score >= 14:
        return "弱验证", -6, 76, False
    return "承接不足", -18, 58, False


def _theme_stock_style(row: dict) -> str:
    fundamental_text = str(row.get("fundamental_text", ""))
    technical = row.get("technical")
    pump = int(row.get("pump") or 0)
    llm_score = row.get("llm_score")
    total = int(row.get("total_score") or 0)
    tags: list[str] = []
    if "验证通过" in fundamental_text or "部分验证" in fundamental_text:
        tags.append("故事有基本面承接")
    elif "承接不足" in fundamental_text or "弱验证" in fundamental_text:
        tags.append("故事需小仓试错")
    else:
        tags.append("基本面待验证")
    try:
        tech_value = int(technical)
    except Exception:
        tech_value = -1
    if tech_value >= 32:
        tags.append("技术强但防加速末端")
    elif tech_value >= 22:
        tags.append("技术可交易")
    elif tech_value >= 0:
        tags.append("技术窗口一般")
    else:
        tags.append("缺行情确认")
    if pump >= 25:
        tags.append("吹票/拥挤风险高")
    elif pump >= 10:
        tags.append("有情绪溢价")
    if llm_score is not None and int(llm_score) >= 80 and total >= 70:
        tags.append("可进入重点复核")
    return "；".join(tags)


def _display_theme(theme: str) -> str:
    return THEME_DISPLAY_NAMES.get(theme, theme)


def _desk_mainline_rows(
    theme_counts: Counter,
    event_signals: list[KpEventSignal],
    candidate_rows: list[dict],
) -> list[tuple[str, int, str, str, str]]:
    event_score = Counter()
    for event in event_signals:
        weight = 4
        if "高" in event.confidence:
            weight += 8
        elif "中" in event.confidence:
            weight += 4
        if event.event_type in {"订单/排产", "涨价/价格弹性", "库存/供需", "客户验证/导入", "业绩/指引"}:
            weight += 4
        for theme in event.themes:
            event_score[theme] += weight
    for theme, count in theme_counts.items():
        event_score[theme] += count * 2

    rows: list[tuple[str, int, str, str, str]] = []
    for theme, score in event_score.most_common(6):
        related = [
            row
            for row in candidate_rows
            if theme.lower() in str(row.get("note", "")).lower()
            or theme.lower() in str(row.get("thesis_path", "")).lower()
            or theme.lower() in str(row.get("signal_interpretation", "")).lower()
        ]
        if not related:
            related = candidate_rows[:3]
        leaders = " / ".join(str(row["name"]) for row in related[:3])
        high_quality_events = [event for event in event_signals if theme in event.themes and "低" not in event.confidence]
        event_desc = (
            _compact_text("；".join(event.event_type for event in high_quality_events[:3]), 80)
            if high_quality_events
            else "主要来自热度和候选映射"
        )
        action = "只做主线观察"
        if related and int(related[0].get("total_score") or 0) >= 70:
            action = "龙头/中军优先，分歧低吸"
        elif related and int(related[0].get("total_score") or 0) >= 55:
            action = "等待回踩或二次确认"
        rows.append((_display_theme(theme), int(score), leaders, event_desc, action))
    return rows


def _opening_playbook(candidate_rows: list[dict]) -> list[str]:
    if not candidate_rows:
        return ["候选不足，先观察主线强弱，不做强行交易。"]
    top = candidate_rows[0]
    name = str(top.get("name"))
    bucket = str(top.get("bucket"))
    action = str(top.get("action"))
    return [
        f"若主线高开但量能不足，优先观察 {name} 是否承接；不因榜单排名直接追高。",
        f"若 {name} 分歧回踩但题材未破、量能健康，按“{bucket}”处理：{_compact_text(action, 80)}。",
        "若板块只有后排补涨、龙头放量滞涨，降低仓位，把知识星球线索转为观察而非买点。",
    ]


def _json_from_text(text: str) -> dict:
    cleaned = str(text or "").strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?", "", cleaned.strip(), flags=re.IGNORECASE).strip()
        cleaned = re.sub(r"```$", "", cleaned.strip()).strip()
    try:
        return json.loads(cleaned)
    except Exception:
        pass
    match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
    if not match:
        raise ValueError("LLM response did not contain a JSON object")
    return json.loads(match.group(0))


def _md_cell(value: object) -> str:
    return str(value if value is not None else "").replace("|", "｜").replace("\n", " ")


def _compact_evidence_for_llm(name: str, data: dict, limit: int = 6) -> str:
    rows: list[str] = []
    item_list = data.get("items", [])
    if isinstance(item_list, list):
        for item in item_list[:limit]:
            if not isinstance(item, KpItem):
                continue
            rows.append(
                "- "
                f"标题：{_compact_text(item.title, 120)}\n"
                f"  来源类型：{item.source_type}；时间：{item.published_at[:16]}\n"
                f"  内容：{_compact_text(item.summary or item.text, 520)}"
            )
    if not rows:
        return f"- 候选 {name} 暂无可用观点流证据。"
    return "\n".join(rows)


def _build_llm_market_prompt(
    name: str,
    data: dict,
    market: CandidateMarketScore | None,
) -> str:
    market_summary = market.summary if market else "未取得行情/财务评分。"
    symbol = market.symbol if market and market.symbol else "未解析"
    fundamental = market.fundamental_score if market else None
    technical = market.technical_score if market else None
    evidence = _compact_evidence_for_llm(name, data)
    return f"""你是A股题材交易日报的资深交易员和深度卖方分析师。请只基于下面给定材料做盘前交易分析，不要编造未给出的事实。

候选标的：{name}
代码：{symbol}
规则辅助信息：
- 观点流信号分：{min(100, int(data.get("score", 0)))}
- 吹票风险分：{int(data.get("pump", 0))}
- 基本面验证分：{fundamental if fundamental is not None else "NA"}
- 技术面分：{technical if technical is not None else "NA"}
- 行情/财务摘要：{market_summary}

知识星球证据：
{evidence}

请用机构交易者/顶级游资视角拆解，不要用“提及次数多所以重要”作为理由。你的任务不是复述材料，而是把段子翻译成交易判断。

必须按这个链路思考：
1. 信息翻译：这条段子/调研如果为真，真正新增的信息是什么？是订单、价格、供给约束、客户验证、业绩弹性、政策、还是纯情绪？
2. 预期差：市场可能还没充分定价的点是什么？如果已经涨很多，预期差是否被消化？
3. 公司承接：公司是核心受益、弹性受益、补涨映射，还是蹭概念？逻辑链有几跳，哪一跳最弱？
4. 基本面交叉验证：当前基本面分、增长、盈利质量、估值和市值弹性能否支撑这个故事？基本面差时不能只因为题材热就给高分。
5. 技术面交易窗口：趋势/量能/位置是支持建仓、只适合低吸、还是已经过热只能等回踩？
6. 胜率赔率：这笔交易的胜率来自信息质量、逻辑直接度、催化剂时钟和技术确认；赔率来自空间、估值弹性、市值大小和拥挤程度。
7. 交易计划：给出盘前可执行动作，不要泛泛说“关注”。要说明触发条件、买点、仓位级别、止损/证伪条件。

请返回严格 JSON，不要 Markdown，不要额外解释。字段如下：
{{
  "logic_score": 0到100的整数，代表题材交易逻辑质量，不是热度分,
  "information_quality": "高/中/低/待验证",
  "signal_interpretation": "把原始段子翻译成一句真实增量信息，指出它属于订单/价格/客户/产能/业绩/政策/情绪中的哪类",
  "expectation_gap": "市场可能还没定价或可能已透支的预期差，一定要说清楚",
  "thesis_path": "题材->业务环节->收入/利润/估值 的一句话链条",
  "company_relevance": "核心受益/弹性受益/补涨映射/蹭概念/无法判断，并说明一句",
  "win_rate_view": "胜率判断：高/中/低，并说明来自信息质量、逻辑直接度、催化剂和技术确认中的哪些",
  "payoff_risk": "赔率判断：空间在哪里，主要回撤风险在哪里",
  "catalyst_clock": "催化剂时钟：未来1天/1周/1月分别看什么，没有就写无明确短催化",
  "verification_points": "未来1-4周最需要验证的2-3个指标",
  "falsification_points": "什么发生说明这条交易逻辑可能错了",
  "entry_plan": "盘前交易计划：追、低吸、等回踩、放弃、只观察，并给触发条件",
  "position_sizing": "仓位建议：试错/小仓/中仓/不参与，并说明为什么",
  "trading_action": "建仓候选/观察/等回踩/只短线/回避，并说明一句",
  "risk_flags": "主要风险，特别指出卖方吹票、逻辑链过长或技术过热",
  "summary": "给日报表格展示的一句话结论，尽量具体"
}}
"""


def _run_llm_market_analysis(
    name: str,
    data: dict,
    market: CandidateMarketScore | None,
    llm,
) -> CandidateLLMAnalysis:
    try:
        prompt = _build_llm_market_prompt(name, data, market)
        system_text = (
            "你是A股题材交易盘前助手。输出必须是可解析JSON。"
            "不要给投资建议保证，不要编造事实。"
        )
        try:
            from langchain_core.messages import HumanMessage, SystemMessage

            llm_input = [SystemMessage(content=system_text), HumanMessage(content=prompt)]
        except Exception:
            llm_input = f"{system_text}\n\n{prompt}"
        response = llm.invoke(llm_input)
        content = getattr(response, "content", response)
        parsed = _json_from_text(str(content))
        logic_score = parsed.get("logic_score")
        try:
            logic_score = int(logic_score)
        except Exception:
            logic_score = None
        if logic_score is not None:
            logic_score = max(0, min(100, logic_score))
        return CandidateLLMAnalysis(
            candidate=name,
            logic_score=logic_score,
            information_quality=str(parsed.get("information_quality", "待验证")),
            signal_interpretation=_compact_text(str(parsed.get("signal_interpretation", "")), 220),
            expectation_gap=_compact_text(str(parsed.get("expectation_gap", "")), 220),
            thesis_path=_compact_text(str(parsed.get("thesis_path", "")), 220),
            company_relevance=_compact_text(str(parsed.get("company_relevance", "")), 160),
            win_rate_view=_compact_text(str(parsed.get("win_rate_view", "")), 180),
            payoff_risk=_compact_text(str(parsed.get("payoff_risk", "")), 180),
            catalyst_clock=_compact_text(str(parsed.get("catalyst_clock", "")), 180),
            verification_points=_compact_text(str(parsed.get("verification_points", "")), 180),
            falsification_points=_compact_text(str(parsed.get("falsification_points", "")), 180),
            entry_plan=_compact_text(str(parsed.get("entry_plan", "")), 180),
            position_sizing=_compact_text(str(parsed.get("position_sizing", "")), 140),
            trading_action=_compact_text(str(parsed.get("trading_action", "")), 140),
            risk_flags=_compact_text(str(parsed.get("risk_flags", "")), 180),
            summary=_compact_text(str(parsed.get("summary", "")), 220),
            status="analyzed",
        )
    except Exception as exc:
        return CandidateLLMAnalysis(
            candidate=name,
            logic_score=None,
            information_quality="分析失败",
            signal_interpretation="",
            expectation_gap="",
            thesis_path="",
            company_relevance="",
            win_rate_view="",
            payoff_risk="",
            catalyst_clock="",
            verification_points="",
            falsification_points="",
            entry_plan="",
            position_sizing="",
            trading_action="",
            risk_flags="",
            summary=f"LLM 分析失败: {_compact_text(str(exc), 180)}",
            status="failed",
        )


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

    sync_status = ensure_knowledge_planet_upstream_synced(curr_date)

    conn = _connect()
    if conn is None:
        return (
            "# Knowledge Planet intelligence context unavailable\n\n"
            f"- Upstream sync: {sync_status}\n"
            "- Reason: local index.sqlite was not found. Run scripts/import_knowledge_planet.cmd first."
        )

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
        f"- Upstream sync: {sync_status}",
        f"- Matched stream items: {len(items)}",
        f"- Matched PDF reports: {len(reports)}",
        "- Evidence discipline: this is supplemental alternative/local research intelligence. Use it to enrich the objective TradingAgents chain, not to replace filings, announcements, financial statements, price/volume evidence, or reputable news. Industry weekly data, channel checks, and company research feedback may be valuable hard-to-publicly-verify clues; sell-side pushes and target-market-cap claims require story-to-profit validation and objective cross-checks.",
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
    include_market_scores: bool = False,
    max_scored_candidates: int = 12,
    include_llm_market_analysis: bool = False,
    max_llm_candidates: int = 8,
    llm_provider: str = "deepseek",
    llm_model: str = "deepseek-chat",
    llm_base_url: str | None = None,
    progress: Callable[[str], None] | None = None,
) -> str:
    """Build a deterministic theme-trading daily report from the local database."""
    sync_status = ensure_knowledge_planet_upstream_synced(report_date, progress=progress)

    conn = _connect()
    if conn is None:
        return (
            "# Knowledge Planet Daily Report unavailable\n\n"
            f"- Upstream sync: {sync_status}\n"
            "- Reason: local index.sqlite was not found. Run scripts/import_knowledge_planet.cmd first."
        )

    items = _items_for_window(conn, report_date, look_back_days)
    reports = _reports_for_window(conn, report_date, look_back_days)
    conn.close()

    start_date, end_date = _date_window(report_date, look_back_days)
    source_counts = Counter(infer_private_source_type(f"{item.title}\n{item.text}", item.source_type) for item in items)
    theme_counts = Counter()
    candidate_scores: dict[str, dict[str, object]] = defaultdict(
        lambda: {"mentions": 0, "score": 0, "pump": 0, "items": [], "display_name": "", "symbol": "", "aliases": []}
    )
    information_items: list[tuple[KpItem, str]] = []
    pump_items: list[tuple[KpItem, int]] = []
    event_signals: list[KpEventSignal] = []

    for item in items:
        text = f"{item.title}\n{item.text}\n{item.summary}"
        source_type = infer_private_source_type(text, item.source_type)
        for theme in THEME_KEYWORDS:
            if theme.lower() in text.lower():
                theme_counts[theme] += 1
        scores = _score_item(item)
        event_signals.append(_parse_event_signal(item, source_type, scores))
        if source_type in INFORMATION_RICH_TYPES:
            information_items.append((item, source_type))
        if scores["pump_risk"] >= 14:
            pump_items.append((item, scores["pump_risk"]))
        raw_names = [*item.tickers, *item.companies, *_extract_candidate_names(text)]
        names = []
        for raw_name in raw_names:
            cleaned_name = str(raw_name or "").strip()
            if cleaned_name and cleaned_name not in names:
                names.append(cleaned_name)
        for name in names[:5]:
            resolved_symbol = _resolve_candidate_symbol(name)
            candidate_key = resolved_symbol or name
            bucket = candidate_scores[candidate_key]
            display_name = str(bucket.get("display_name") or "")
            name_is_code = bool(re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", name, flags=re.IGNORECASE))
            display_is_code = bool(re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", display_name, flags=re.IGNORECASE))
            if (
                not display_name
                or (display_is_code and not name_is_code)
                or (resolved_symbol and not name_is_code and not display_is_code and len(name) > len(display_name))
            ):
                bucket["display_name"] = name
            if resolved_symbol:
                bucket["symbol"] = resolved_symbol
            aliases = bucket.get("aliases")
            if isinstance(aliases, list) and name not in aliases:
                aliases.append(name)
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
    stock_ranked = [
        (name, data)
        for name, data in ranked
        if data.get("symbol") or re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", str(name), flags=re.IGNORECASE)
    ]
    stock_keys = {name for name, _data in stock_ranked}
    unresolved_ranked = [(name, data) for name, data in ranked if name not in stock_keys]

    market_scores: dict[str, CandidateMarketScore] = {}
    if include_market_scores:
        score_targets = stock_ranked[: max(0, int(max_scored_candidates or 0))]
        for idx, (name, _data) in enumerate(score_targets, start=1):
            display_name = str(_data.get("display_name") or name)
            if progress:
                progress(f"[market scoring] {idx}/{len(score_targets)} {display_name}")
            market_scores[name] = _score_candidate_market(name, end_date)
        if progress:
            scored_count = sum(1 for score in market_scores.values() if score.status == "scored")
            unresolved_count = sum(1 for score in market_scores.values() if score.status == "unresolved")
            unscored_count = sum(1 for score in market_scores.values() if score.status == "unscored")
            progress(
                "[market scoring] done: "
                f"scored={scored_count}, unscored={unscored_count}, unresolved={unresolved_count}"
            )

    llm_analyses: dict[str, CandidateLLMAnalysis] = {}
    llm_attempted = 0
    llm_unavailable_reason = ""
    if include_llm_market_analysis:
        try:
            llm = _create_market_analysis_llm(
                llm_provider,
                llm_model,
                llm_base_url,
                progress=progress,
            )
            llm_targets = stock_ranked[: max(0, int(max_llm_candidates or 0))]
            llm_attempted = len(llm_targets)
            for idx, (name, data) in enumerate(llm_targets, start=1):
                display_name = str(data.get("display_name") or name)
                if progress:
                    progress(f"[llm market analysis] {idx}/{len(llm_targets)} {display_name}")
                llm_analyses[name] = _run_llm_market_analysis(
                    display_name,
                    data,
                    market_scores.get(name),
                    llm,
                )
            if progress:
                analyzed = sum(1 for analysis in llm_analyses.values() if analysis.status == "analyzed")
                failed = sum(1 for analysis in llm_analyses.values() if analysis.status == "failed")
                progress(f"[llm market analysis] done: analyzed={analyzed}, failed={failed}")
        except Exception as exc:
            llm_unavailable_reason = _compact_text(str(exc), 180)
            if progress:
                progress(f"[llm market analysis] unavailable: {llm_unavailable_reason}")

    lines = [
        f"# 知识星球题材交易日报 - {end_date}",
        "",
        f"- 统计窗口：{start_date} 至 {end_date}",
        f"- 观点流条目：{len(items)}",
        f"- PDF 研报：{len(reports)}",
        f"- 上游同步：{sync_status}",
        f"- 基本面/技术面评分：{'已启用，前 ' + str(max_scored_candidates) + ' 个候选尝试评分' if include_market_scores else '未启用'}",
        f"- LLM 逻辑拆解：{'已启用，' + llm_provider + '/' + llm_model + '，前 ' + str(max_llm_candidates) + ' 个候选' if include_llm_market_analysis else '未启用'}",
        (
            "- LLM 诊断："
            + (
                f"已尝试 {llm_attempted} 个，成功 {sum(1 for a in llm_analyses.values() if a.status == 'analyzed')} 个，"
                f"失败 {sum(1 for a in llm_analyses.values() if a.status == 'failed')} 个"
                + (f"，初始化失败：{llm_unavailable_reason}" if llm_unavailable_reason else "")
                if include_llm_market_analysis
                else "未启用"
            )
        ),
        (
            "- 评分诊断："
            + (
                f"已尝试 {len(market_scores)} 个，成功 {sum(1 for score in market_scores.values() if score.status == 'scored')} 个，"
                f"数据不可用 {sum(1 for score in market_scores.values() if score.status == 'unscored')} 个，"
                f"代码未解析 {sum(1 for score in market_scores.values() if score.status == 'unresolved')} 个"
                if include_market_scores
                else "快速模式未尝试基本面/技术面评分"
            )
        ),
        "- 用途：发现可交易叙事、高价值产业/渠道线索、卖方研究视角和吹票风险。它不是直接买入清单。",
        "",
        "## 评分口径",
        "",
        "- 观点流信号只用于候选召回和辅助展示，不作为高质量排序的核心依据；提及次数本身不构成买入理由。",
        "- LLM 逻辑拆解是高质量日报的主评分：先把段子翻译成真实增量信息，再判断预期差、公司承接、胜率赔率、催化剂时钟、交易计划和吹票风险。",
        "- 基本面验证不是独立加分项，而是题材逻辑的交叉验证：验证通过会强化观点流，承接不足会压低综合分上限；缺数据时不能进入 A 桶。",
        "- 基本面验证重点看收入/利润增速、ROE/毛利率、现金流/负债、估值和市值弹性，用来回答“故事能不能落到业绩和市值承接”。",
        "- 技术面最高 40 分，作为相对独立的交易时点评估：均线趋势、5/20/60 日动量、换手/量能确认、距离高点和过热风险。",
        "- 吹票/拥挤风险作为独立扣分项；A 桶仍需要单票 TradingAgents 复核后再考虑建仓。",
        "",
        "## 来源结构",
        "",
        "| 来源类型 | 数量 | 处理方式 |",
        "| --- | ---: | --- |",
    ]
    for source_type, count in source_counts.most_common():
        treatment = "信息含量较高，可作为私域/调研线索" if source_type in INFORMATION_RICH_TYPES else "卖方/情绪线索，需要传导验证"
        if source_type in NOISE_TYPES:
            treatment = "低置信度，除非后续交叉验证"
        lines.append(f"| {source_type} | {count} | {treatment} |")

    lines.extend(["", "## 题材热度图", "", "| 题材 | 提及次数 |", "| --- | ---: |"])
    for theme, count in theme_counts.most_common(15):
        lines.append(f"| {theme} | {count} |")

    candidate_rows: list[dict] = []
    display_ranked = stock_ranked if (include_market_scores or include_llm_market_analysis) else ranked
    for name, data in display_ranked:
        display_name = str(data.get("display_name") or name)
        score = int(data["score"])
        pump = int(data["pump"])
        market = market_scores.get(name)
        fundamental = market.fundamental_score if market else None
        technical = market.technical_score if market else None
        market_total = market.total_market_score if market else None
        signal_score = min(100, score)
        llm_analysis = llm_analyses.get(name)
        validation_label, validation_adjust, score_cap, a_eligible = _fundamental_validation(
            fundamental
        )
        if include_llm_market_analysis and llm_analysis and llm_analysis.logic_score is not None:
            logic_component = min(70, int(llm_analysis.logic_score * 0.7))
            technical_component = min(20, int((technical or 0) * 0.5))
            total_score = (
                logic_component
                + technical_component
                + validation_adjust
                - min(15, pump // 2)
            )
            if score_cap is not None:
                total_score = min(total_score, score_cap)
            total_score = max(0, total_score)
        elif include_market_scores:
            signal_component = min(40, signal_score)
            technical_component = min(40, technical or 0)
            total_score = signal_component + technical_component + validation_adjust - min(15, pump // 2)
            if score_cap is not None:
                total_score = min(total_score, score_cap)
            total_score = max(0, total_score)
        else:
            validation_label = "未评分"
            a_eligible = True
            total_score = min(100, signal_score + int(data["mentions"]) * 8 - min(15, pump // 2))
        if include_llm_market_analysis and (not llm_analysis or llm_analysis.status != "analyzed"):
            bucket = "B：题材观察/待LLM复核" if total_score >= 35 and pump < 35 else "C：只适合战术跟踪"
        elif include_market_scores and market_total is None:
            bucket = "B：题材观察/待行情验证" if total_score >= 35 and pump < 35 else "C：只适合战术跟踪"
        elif total_score >= 82 and pump < 25 and a_eligible and (technical or 0) >= 22:
            bucket = "A：深挖/可建仓候选"
        elif total_score >= 58 and pump < 35:
            bucket = "B：题材观察/等待验证"
        elif pump >= 35:
            bucket = "D：吹票/拥挤风险观察"
        else:
            bucket = "C：只适合战术跟踪"
        item_list = data.get("items", [])
        note = ""
        if llm_analysis:
            llm_parts = [
                llm_analysis.summary,
                f"预期差：{llm_analysis.expectation_gap}" if llm_analysis.expectation_gap else "",
                f"计划：{llm_analysis.entry_plan}" if llm_analysis.entry_plan else "",
                f"路径：{llm_analysis.thesis_path}" if llm_analysis.thesis_path else "",
                f"验证：{llm_analysis.verification_points}" if llm_analysis.verification_points else "",
                f"风险：{llm_analysis.risk_flags}" if llm_analysis.risk_flags else "",
            ]
            note = _compact_text("；".join(part for part in llm_parts if part), 320)
        if market and market.summary:
            note = _compact_text(f"{note}；{market.summary}" if note else market.summary, 360)
        if isinstance(item_list, list) and item_list:
            title_note = _compact_text("; ".join(item.title for item in item_list), 180)
            note = _compact_text(f"{note}；{title_note}" if note else title_note, 420)
        aliases = data.get("aliases")
        alias_text = ""
        if isinstance(aliases, list) and len(aliases) > 1:
            alias_text = " / ".join(str(alias) for alias in aliases[:4])
        candidate_rows.append(
            {
                "name": display_name,
                "symbol": (market.symbol if market and market.symbol else str(data.get("symbol") or "未评分")),
                "aliases": alias_text,
                "signal_score": signal_score,
                "llm_score": llm_analysis.logic_score if llm_analysis else None,
                "llm_status": llm_analysis.status if llm_analysis else "not_run",
                "information_quality": llm_analysis.information_quality if llm_analysis else "",
                "signal_interpretation": llm_analysis.signal_interpretation if llm_analysis else "",
                "expectation_gap": llm_analysis.expectation_gap if llm_analysis else "",
                "thesis_path": llm_analysis.thesis_path if llm_analysis else "",
                "company_relevance": llm_analysis.company_relevance if llm_analysis else "",
                "win_rate_view": llm_analysis.win_rate_view if llm_analysis else "",
                "payoff_risk": llm_analysis.payoff_risk if llm_analysis else "",
                "catalyst_clock": llm_analysis.catalyst_clock if llm_analysis else "",
                "verification_points": llm_analysis.verification_points if llm_analysis else "",
                "falsification_points": llm_analysis.falsification_points if llm_analysis else "",
                "entry_plan": llm_analysis.entry_plan if llm_analysis else "",
                "position_sizing": llm_analysis.position_sizing if llm_analysis else "",
                "risk_flags": llm_analysis.risk_flags if llm_analysis else "",
                "fundamental_text": (
                    f"{validation_label}{' ' + str(fundamental) + '/40' if fundamental is not None else ''}"
                ),
                "technical": technical if technical is not None else "NA",
                "pump": pump,
                "total_score": total_score,
                "bucket": bucket,
                "action": (
                    llm_analysis.trading_action
                    if llm_analysis and llm_analysis.trading_action
                    else ("LLM分析失败" if llm_analysis and llm_analysis.status == "failed" else "未做LLM分析")
                ),
                "note": note,
            }
        )
        candidate_rows[-1]["theme_stock_style"] = _theme_stock_style(candidate_rows[-1])

    if include_llm_market_analysis:
        candidate_rows.sort(
            key=lambda row: (
                int(row["total_score"]),
                int(row["llm_score"] or -1),
                int(row["signal_score"]),
            ),
            reverse=True,
        )

    lines.extend(["", "## 交易台主线总控"])
    mainline_rows = _desk_mainline_rows(theme_counts, event_signals, candidate_rows)
    if mainline_rows:
        lines.extend(["", "| 主线 | 强度 | 代表候选 | 主要事件 | 交易处理 |", "| --- | ---: | --- | --- | --- |"])
        for theme, score, leaders, event_desc, action in mainline_rows:
            lines.append(
                f"| {_md_cell(theme)} | {score} | {_md_cell(leaders)} | {_md_cell(event_desc)} | {_md_cell(action)} |"
            )
    else:
        lines.append("- 本窗口未形成清晰主线，先保持观察。")

    lines.extend(["", "### 开盘剧本"])
    for item in _opening_playbook(candidate_rows):
        lines.append(f"- {item}")

    lines.extend(["", "## 信息事件解析"])
    high_value_events = [
        event
        for event in event_signals
        if "低" not in event.confidence
        and event.event_type
        in {"订单/排产", "涨价/价格弹性", "库存/供需", "客户验证/导入", "产能/扩产", "政策/监管", "业绩/指引", "海外映射"}
    ]
    if high_value_events:
        lines.extend(["", "| 时间 | 类型 | 置信度 | 线索 | 验证 | 风险 |", "| --- | --- | --- | --- | --- | --- |"])
        for event in high_value_events[:15]:
            lines.append(
                f"| {event.published_at[:16]} | {_md_cell(event.event_type)} | {_md_cell(event.confidence)} | "
                f"{_md_cell(_compact_text(event.interpretation, 110))} | {_md_cell(event.verification)} | {_md_cell(event.risk)} |"
            )
    else:
        lines.append("- 本窗口没有足够明确的订单、涨价、库存、客户验证或政策类事件。")

    lines.extend(
        [
            "",
            "## 候选标的综合排序",
            "",
            "| 排名 | 标的 | 综合分 | 分层 | 题材交易标签 | 交易动作 |",
            "| ---: | --- | ---: | --- | --- | --- |",
        ]
    )
    for idx, row in enumerate(candidate_rows, start=1):
        candidate_label = f"{row['name']}（{row['symbol']}）"
        lines.append(
            f"| {idx} | {_md_cell(candidate_label)} | {row['total_score']} | "
            f"{_md_cell(row['bucket'])} | {_md_cell(row['theme_stock_style'])} | "
            f"{_md_cell(_compact_text(str(row['action']), 80))} |"
        )

    lines.extend(["", "## 候选逻辑详情"])
    for idx, row in enumerate(candidate_rows, start=1):
        lines.extend(
            [
                "",
                f"### {idx}. {_md_cell(row['name'])}（{_md_cell(row['symbol'])}）",
                f"- **分层/综合分**：{row['bucket']}，{row['total_score']} 分；观点流信号 {row['signal_score']}，吹票风险 {row['pump']}。",
                f"- **交易动作**：{row['action']}",
                f"- **题材交易标签**：{row['theme_stock_style']}",
                f"- **基本面/技术面**：{row['fundamental_text']}；技术面 {row['technical']}/40。",
            ]
        )
        if row["aliases"]:
            lines.append(f"- **别名合并**：{_md_cell(row['aliases'])}")
        if row["llm_status"] == "analyzed":
            lines.extend(
                [
                    f"- **LLM逻辑分/信息质量**：{row['llm_score']}/100；{row['information_quality']}。",
                    f"- **信息翻译**：{row['signal_interpretation'] or '未提取'}",
                    f"- **预期差判断**：{row['expectation_gap'] or '未提取'}",
                    f"- **题材传导路径**：{row['thesis_path'] or '未提取'}",
                    f"- **公司相关性**：{row['company_relevance'] or '未提取'}",
                    f"- **胜率判断**：{row['win_rate_view'] or '未提取'}",
                    f"- **赔率/回撤**：{row['payoff_risk'] or '未提取'}",
                    f"- **催化剂时钟**：{row['catalyst_clock'] or '未提取'}",
                    f"- **入场计划**：{row['entry_plan'] or '未提取'}",
                    f"- **仓位建议**：{row['position_sizing'] or '未提取'}",
                    f"- **验证指标**：{row['verification_points'] or '未提取'}",
                    f"- **证伪条件**：{row['falsification_points'] or '未提取'}",
                    f"- **风险标记**：{row['risk_flags'] or '未提取'}",
                ]
            )
        elif row["llm_status"] == "failed":
            lines.append(f"- **LLM状态**：分析失败。{row['note']}")
        else:
            lines.append("- **LLM状态**：未做 LLM 分析或 LLM 初始化失败，请查看报告顶部 LLM 诊断。")
        if row["note"] and row["llm_status"] != "failed":
            lines.append(f"- **证据摘要**：{row['note']}")

    if unresolved_ranked:
        lines.extend(["", "## 未进入主榜的未解析线索"])
        lines.append("- 以下内容未能解析为 A 股股票代码，暂不进入候选标的主榜；可作为产业线索或后续人工补充映射。")
        for name, data in unresolved_ranked[:12]:
            item_list = data.get("items", [])
            evidence = ""
            if isinstance(item_list, list) and item_list:
                evidence = _compact_text("; ".join(item.title for item in item_list[:2]), 180)
            lines.append(f"- **{_md_cell(data.get('display_name') or name)}**：{evidence}")

    lines.extend(["", "## 高价值产业/调研线索"])
    if information_items:
        for item, source_type in information_items[:20]:
            lines.append(
                f"- **{_compact_text(item.title, 100)}** ({source_type}, {item.published_at[:16]}): {_compact_text(item.summary or item.text, 260)}"
            )
    else:
        lines.append("- 本窗口未识别到信息含量较高的产业数据或调研反馈。")

    lines.extend(["", "## 卖方推票 / 吹票风险观察"])
    if pump_items:
        for item, risk in sorted(pump_items, key=lambda pair: pair[1], reverse=True)[:15]:
            lines.append(
                f"- **{_compact_text(item.title, 100)}**（吹票风险 {risk}）：需要补齐故事到利润的传导、催化剂时间表、估值消化能力和量价确认。"
            )
    else:
        lines.append("- 关键词规则未识别到高吹票风险条目。")

    lines.extend(["", "## PDF 研报研究视角"])
    if reports:
        for report in reports[:20]:
            lines.append(
                f"- **{_compact_text(report.title, 120)}**（{report.broker or 'unknown'}，{report.published_at[:10]}）：用于提取业务/KPI框架、预测假设、可比公司和潜在乐观偏差。"
            )
    else:
        lines.append("- 本窗口未导入 PDF 研报。")

    lines.extend(
        [
            "",
            "## 交易台检查清单",
            "- 不要因为提及次数最高就直接买入。需要量价确认，避免在没有新催化剂的加速段追高。",
            "- 对 A/B 桶候选，建仓前应跑单票 TradingAgents，并启用 Knowledge Planet 上下文。",
            "- 对私域/渠道数据保留 `hard_to_publicly_verify` 标签，但不要简单丢弃；要定义下一个可观察验证指标。",
            "- 对卖方目标市值故事，强制拆成：产品/业务驱动 -> 收入 -> 毛利/净利 -> EPS/FCF -> 估值。",
            "- 后续记录候选标的 1/3/5/10 日收益，逐步给来源和作者建立质量评分。",
        ]
    )
    return "\n".join(lines)
