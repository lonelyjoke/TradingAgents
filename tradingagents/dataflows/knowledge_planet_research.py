"""Local Knowledge Planet intelligence retrieval and daily synthesis.

The Knowledge Planet database is a private, local research layer built from
manually imported posts and PDFs. It is intentionally treated as alternative
intelligence: useful for finding expectations, channel checks, sell-side lenses,
and tradable narratives, but not as filing-grade proof.
"""

from __future__ import annotations

import json
import hashlib
import math
import os
import re
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, Iterable

from tradingagents.dataflows.config import get_config
from tradingagents.dataflows.industry_identity import is_hog_breeding_text

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
DAILY_MAIN_BOARD_SIZE = 10
DAILY_WATCH_BOARD_SIZE = 5
DAILY_ANALYSIS_TARGETS = DAILY_MAIN_BOARD_SIZE + DAILY_WATCH_BOARD_SIZE
DAILY_MAIN_MIN_SCORE = 55
DAILY_WATCH_MIN_SCORE = 35

PREPROCESS_SCHEMA_VERSION = 2

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

TECH_HOT_THEME_KEYWORDS = {
    "AI",
    "算力",
    "国产算力",
    "半导体",
    "PCB",
    "存储",
    "光模块",
    "机器人",
    "锂电",
    "光伏",
}

NON_TECH_ALPHA_KEYWORDS = {
    "农业",
    "食品",
    "消费",
    "煤炭",
    "化工",
    "医药",
    "中药",
    "环保",
    "资源化",
    "UCO",
    "有色",
    "钨",
    "油气",
    "油服",
    "服饰",
    "纺织",
    "机械",
    "军工",
    "电力",
    "公用",
    "白酒",
    "啤酒",
    "猪",
    "养殖",
}

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
    "中国平安": "601318.SH",
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
    "中国太保": "601601.SH",
    "海航控股": "600221.SH",
    "生益科技": "600183.SH",
    "中际旭创": "300308.SZ",
    "力源信息": "300184.SZ",
    "西部材料": "002149.SZ",
    "三夫户外": "002780.SZ",
    "上海银行": "601229.SH",
    "同星科技": "301252.SZ",
}

COMMON_A_SHARE_NAMES_BY_SYMBOL = {symbol: name for name, symbol in COMMON_A_SHARE_ALIASES.items()}

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
class PmControlAnalysis:
    market_posture: str
    mainline_judgment: str
    opportunity_focus: str
    watchlist: str
    avoid_list: str
    trigger_conditions: str
    portfolio_action: str
    review_tasks: str
    status: str


@dataclass(frozen=True)
class EventLLMReview:
    event_type: str
    increment_level: str
    evidence_grade: str
    impact_path: str
    beneficiaries: str
    verification: str
    risk: str
    summary: str
    status: str


@dataclass(frozen=True)
class KpPreprocessStats:
    start_date: str
    end_date: str
    items_scanned: int
    reports_scanned: int
    quality_rows: int
    content_units: int
    events: int
    clusters: int
    mappings: int
    report_assumptions: int
    opportunities: int
    ocr_low_quality: int
    pdf_pending_or_limited: int
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
        last_error: Exception | None = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    raw = response.read().decode("utf-8")
                break
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"DeepSeek HTTP {exc.code}: {_compact_text(body, 300)}") from exc
            except Exception as exc:
                last_error = exc
                if attempt < 2:
                    time.sleep(1.2 * (attempt + 1))
                    continue
                raise RuntimeError(f"DeepSeek request failed after retries: {_compact_text(str(last_error), 220)}") from exc
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


def _sync_stamp_is_empty(stamp: Path) -> bool:
    try:
        text = stamp.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return "wrote 0 topic(s)" in text or ": 0 topic(s)" in text


def _is_past_sync_date(sync_date: str) -> bool:
    sync_dt = _parse_date(sync_date)
    if not sync_dt:
        return False
    return sync_dt.date() < datetime.now().date()


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
    max_pages: int | None = None,
    max_image_downloads: int | None = None,
    max_file_downloads: int | None = None,
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
    if stamp.exists() and not force and not _sync_stamp_is_empty(stamp):
        if _is_past_sync_date(sync_date):
            return f"already_synced_past_date:{stamp}"
        if min_interval > 0:
            stamp_age = datetime.now() - datetime.fromtimestamp(stamp.stat().st_mtime)
            if stamp_age < timedelta(minutes=min_interval):
                age_minutes = max(0, int(stamp_age.total_seconds() // 60))
                return f"recently_synced:{age_minutes}m:{stamp}"

    group_spec = str(config.get("knowledge_planet_auto_sync_group") or "").strip()
    if not group_spec:
        return "auto_sync_skipped:no_group"

    max_pages = int(
        config.get("knowledge_planet_auto_sync_max_pages", 20)
        if max_pages is None
        else max_pages
    )
    max_images = int(
        config.get("knowledge_planet_auto_sync_max_image_downloads", 100)
        if max_image_downloads is None
        else max_image_downloads
    )
    max_files = int(
        config.get("knowledge_planet_auto_sync_max_file_downloads", 50)
        if max_file_downloads is None
        else max_file_downloads
    )

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


def _dates_for_window(curr_date: str, look_back_days: int) -> list[str]:
    start_text, end_text = _date_window(curr_date, look_back_days)
    start = _parse_date(start_text) or datetime.now()
    end = _parse_date(end_text) or start
    days = max(0, (end.date() - start.date()).days)
    return [(start + timedelta(days=offset)).strftime("%Y-%m-%d") for offset in range(days + 1)]


def ensure_knowledge_planet_upstream_synced_for_window(
    end_date: str,
    look_back_days: int,
    *,
    force: bool = False,
    progress: Callable[[str], None] | None = None,
    max_pages: int | None = None,
    max_image_downloads: int | None = None,
    max_file_downloads: int | None = None,
) -> str:
    """Best-effort upstream sync for every calendar date in a report/context window."""
    statuses: list[str] = []
    for sync_date in _dates_for_window(end_date, look_back_days):
        statuses.append(
            f"{sync_date}="
            f"{ensure_knowledge_planet_upstream_synced(sync_date, force=force, progress=progress, max_pages=max_pages, max_image_downloads=max_image_downloads, max_file_downloads=max_file_downloads)}"
        )
    return "; ".join(statuses) if statuses else "auto_sync_skipped:no_dates"


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


def _research_layer_for_signal(text: str, source_type: str, event_type: str = "") -> str:
    """Classify messy stream content into a research-consumption layer.

    The Knowledge Planet stream mixes hard-to-publicly-verify data, sell-side
    narratives, report inventories, and screenshots. This layer label tells
    downstream agents how to use the clue instead of treating all mentions as
    equal.
    """
    body = f"{event_type}\n{source_type}\n{text}"
    if source_type == "report_list_post":
        return "report_inventory"
    if source_type in {"industry_weekly_data", "industry_data_snippet", "broker_survey_data"}:
        return "industry_kpi_or_weekly_data"
    if source_type == "channel_check":
        return "channel_or_supply_chain_check"
    if source_type in {"company_research_feedback", "expert_call"}:
        return "company_research_feedback"
    if event_type == "政策/监管" or re.search(r"(政策|监管|财政|货币|利率|汇率|通胀|CPI|PPI|PMI|流动性|资金面)", body):
        return "macro_policy_or_liquidity"
    if event_type == "海外映射" or re.search(r"(海外|美股|全球|英伟达|台积电|美光|高盛|摩根|BofA|Morgan)", body):
        return "overseas_mapping"
    if event_type == "研报框架" or source_type in {"broker_report_summary"}:
        return "sell_side_research_framework"
    if source_type in SELL_SIDE_TYPES:
        return "sell_side_narrative_or_promotion"
    if source_type in NOISE_TYPES:
        return "low_confidence_noise"
    return "general_research_clue"


def _fusion_route_for_layer(research_layer: str, event_type: str = "") -> str:
    if research_layer == "industry_kpi_or_weekly_data":
        return "Industry/KPI layer -> Fundamentals analyst; map into sector KPI, supply-demand, ASP/cost/margin, then verify with Tushare/filings/price data."
    if research_layer == "channel_or_supply_chain_check":
        return "Supply-chain clue -> Bull/Bear debate; test order/customer/production bridge and require follow-up confirmation."
    if research_layer == "company_research_feedback":
        return "Company research feedback -> Fundamentals/Research Manager; convert management or channel wording into forecast assumptions and falsification points."
    if research_layer == "macro_policy_or_liquidity":
        return "Macro/policy context -> News/Research Manager; use as top-down constraint or catalyst, not standalone company proof."
    if research_layer == "overseas_mapping":
        return "Overseas mapping -> News/Research Manager; verify mapping chain length, A-share pass-through, and whether it is already priced."
    if research_layer == "sell_side_research_framework":
        return "Sell-side framework -> Fundamentals analyst; borrow KPI framework but re-underwrite assumptions with objective data."
    if research_layer == "sell_side_narrative_or_promotion":
        return "Narrative/promotion -> Bear researcher first; challenge story-to-profit bridge, crowding, target-market-cap math, and valuation absorption."
    if research_layer == "report_inventory":
        return "Report inventory -> retrieval layer; use only matched PDF assumptions/text, not the mere existence of a report list."
    if research_layer == "low_confidence_noise":
        return "Noise layer -> watch only; never change rating or sizing without independent confirmation."
    if event_type in {"订单/排产", "客户验证/导入", "涨价/价格弹性", "库存/供需", "业绩/指引"}:
        return "Event clue -> convert into earnings/valuation bridge and date-stamped verification task."
    return "General clue -> use as background unless it maps to a company KPI, catalyst, or falsification signal."


def _objective_anchor_for_event(event_type: str, research_layer: str = "") -> str:
    if event_type == "订单/排产":
        return "订单公告、排产环比、产能利用率、合同负债/预收款、收入确认节奏"
    if event_type == "涨价/价格弹性":
        return "产品报价、毛利率、竞品价格、下游接受度、行业价格指数"
    if event_type == "库存/供需":
        return "周度库存、开工率、出货/销量、现货/期货价格、供需平衡表"
    if event_type == "客户验证/导入":
        return "送样/认证节点、客户公告、批量订单、收入分客户或分产品验证"
    if event_type == "产能/扩产":
        return "投产时间、良率、资本开支、在建工程、产能利用率"
    if event_type == "政策/监管":
        return "政策原文、执行细则、受益范围、时间表、预算/补贴落地"
    if event_type == "业绩/指引":
        return "季度收入、利润、毛利率、费用率、管理层指引、市场一致预期"
    if event_type == "海外映射":
        return "海外龙头业绩/指引、供应链关系、A股收入敞口、估值/涨幅差"
    if event_type == "研报框架" or research_layer == "sell_side_research_framework":
        return "研报假设拆解、公司公告、Tushare财务、同行KPI、估值分位"
    if research_layer == "macro_policy_or_liquidity":
        return "宏观数据、政策原文、利率/汇率/资金面、行业 beta 与公司 alpha 拆分"
    return "公告、财务、同行、价格成交、后续调研或可观察代理指标"


def _extract_key_metrics(text: str, limit: int = 8) -> list[str]:
    body = _strip_zsxq_metadata(text)
    pattern = re.compile(
        r"[^。；;\n]{0,18}\d+(?:\.\d+)?\s*(?:%|pct|BP|bp|亿|万|吨|台|件|元|美元|万元|亿元|万吨|GW|MW|GWh|MWh|w|W)[^。；;\n]{0,24}",
        re.IGNORECASE,
    )
    metrics: list[str] = []
    for match in pattern.finditer(body):
        metric = _compact_text(match.group(0), 80)
        if metric and metric not in metrics:
            metrics.append(metric)
        if len(metrics) >= limit:
            break
    return metrics


HOG_KP_EXPANSION_TERMS = (
    "\u751f\u732a",
    "\u5546\u54c1\u732a",
    "\u732a\u4ef7",
    "\u732a\u5468\u671f",
    "\u4ed4\u732a",
    "\u6bcd\u732a",
    "\u80fd\u7e41\u6bcd\u732a",
    "\u6bcd\u732a\u5b58\u680f",
    "\u51fa\u680f",
    "\u5c60\u5bb0",
    "\u5b8c\u5168\u6210\u672c",
    "\u517b\u6b96\u6210\u672c",
    "\u81ea\u7e41\u81ea\u517b",
    "\u51bb\u54c1\u5e93\u5b58",
    "\u9972\u6599",
    "\u7389\u7c73",
    "\u8c46\u7c95",
    "\u6d8c\u76ca",
    "\u94a2\u8054",
    "\u5353\u521b",
    "\u519c\u4e1a\u5468\u62a5",
    "\u517b\u6b96\u5468\u62a5",
    "\u755c\u7267",
    "\u7267\u539f",
    "\u7267\u539f\u80a1\u4efd",
    "\u6e29\u6c0f",
    "\u6e29\u6c0f\u80a1\u4efd",
    "\u65b0\u5e0c\u671b",
    "\u5929\u90a6\u98df\u54c1",
    "\u5510\u4eba\u795e",
    "\u5de8\u661f\u519c\u7267",
    "\u795e\u519c\u96c6\u56e2",
    "\u4e1c\u745e\u80a1\u4efd",
    "\u65b0\u4e94\u4e30",
    "\u50b2\u519c",
    "live hog",
    "hog",
    "piglet",
    "sow",
    "breeding sow",
    "slaughter",
    "complete cost",
    "LH",
)


def _stock_terms(ticker: str, *, include_industry_expansion: bool = True) -> list[str]:
    terms = []
    raw = str(ticker or "").strip()
    normalized = raw.upper()
    if raw:
        terms.append(raw)
        terms.append(normalized)
        terms.append(raw.replace(".", ""))
        if "." in raw:
            terms.append(raw.split(".")[0])

    if normalized:
        for alias, symbol in COMMON_A_SHARE_ALIASES.items():
            if normalized == symbol or normalized == symbol.replace(".", ""):
                terms.append(alias)

    if _fetch_stock_basic and re.match(r"^\d{6}\.(SH|SZ|BJ)$", normalized):
        try:
            basic = _fetch_stock_basic(normalized)
            if basic is not None:
                for field in ("name", "industry"):
                    value = str(basic.get(field) or "").strip()
                    if value:
                        terms.append(value)
        except Exception:
            pass

    base_terms = list(terms)
    if include_industry_expansion and is_hog_breeding_text(normalized or raw, *base_terms):
        terms.extend(HOG_KP_EXPANSION_TERMS)

    unique = []
    for term in terms:
        term = term.strip()
        if len(term) >= 2 and term not in unique:
            unique.append(term)
    return unique


def _term_in_text(term: str, text: str) -> bool:
    term = str(term or "").strip()
    if not term:
        return False
    if any(ord(ch) > 127 for ch in term):
        return term in text
    return term.lower() in text.lower()


def _item_match_score(item: KpItem, terms: list[str], primary_terms: list[str]) -> int:
    title = item.title or ""
    body = "\n".join(
        [
            item.title,
            item.summary,
            item.text,
            " ".join(item.tickers),
            " ".join(item.companies),
            " ".join(item.industries),
            " ".join(item.themes),
        ]
    )
    score = 0
    for term in primary_terms:
        if _term_in_text(term, title):
            score += 120
        elif _term_in_text(term, body):
            score += 80
    for term in terms:
        if term in primary_terms:
            continue
        if _term_in_text(term, title):
            score += 30
        elif _term_in_text(term, body):
            score += 16
    source_type = infer_private_source_type(f"{item.title}\n{item.text}", item.source_type)
    if source_type in INFORMATION_RICH_TYPES:
        score += 24
    elif source_type in SELL_SIDE_TYPES:
        score += 8
    if item.tickers or item.companies:
        score += 10
    return score


def _report_match_score(report: KpReport, terms: list[str], primary_terms: list[str]) -> int:
    title = report.title or ""
    body = "\n".join(
        [
            report.title,
            report.summary,
            report.broker,
            " ".join(report.tickers),
            " ".join(report.companies),
            " ".join(report.industries),
            " ".join(report.themes),
        ]
    )
    score = 0
    for term in primary_terms:
        if _term_in_text(term, title):
            score += 140
        elif _term_in_text(term, body):
            score += 90
    for term in terms:
        if term in primary_terms:
            continue
        if _term_in_text(term, title):
            score += 36
        elif _term_in_text(term, body):
            score += 18
    if report.tickers or report.companies:
        score += 12
    return score


def _query_items(
    conn: sqlite3.Connection,
    *,
    terms: list[str],
    primary_terms: list[str] | None = None,
    start_date: str,
    end_date: str,
    limit: int,
) -> list[KpItem]:
    if not terms:
        return []
    clauses = []
    params: list[str] = [start_date, end_date]
    for term in terms:
        like = _safe_like_term(term)
        clauses.append(
            "(title LIKE ? OR text LIKE ? OR summary LIKE ? OR tickers_json LIKE ? OR company_names_json LIKE ? OR industries_json LIKE ? OR themes_json LIKE ?)"
        )
        params.extend([like, like, like, like, like, like, like])
    sql_limit = min(max(int(limit) * 8, int(limit) + 80), 300)
    sql = f"""
        SELECT *
        FROM kp_items
        WHERE substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) <= ?
          AND ({' OR '.join(clauses)})
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) DESC, id DESC
        LIMIT {int(sql_limit)}
    """
    rows = [_row_to_item(row) for row in conn.execute(sql, params)]
    primary = primary_terms or terms
    rows.sort(
        key=lambda item: (
            _item_match_score(item, terms, primary),
            item.published_at or "",
            item.row_id,
        ),
        reverse=True,
    )
    return rows[: int(limit)]


def _query_reports(
    conn: sqlite3.Connection,
    *,
    terms: list[str],
    primary_terms: list[str] | None = None,
    start_date: str,
    end_date: str,
    limit: int,
) -> list[KpReport]:
    if not terms:
        return []
    clauses = []
    params: list[str] = [start_date, end_date]
    for term in terms:
        like = _safe_like_term(term)
        clauses.append(
            "(r.title LIKE ? OR r.summary LIKE ? OR r.tickers_json LIKE ? OR r.company_names_json LIKE ? OR r.industries_json LIKE ? OR r.themes_json LIKE ? OR t.text LIKE ?)"
        )
        params.extend([like, like, like, like, like, like, like])
    sql_limit = min(max(int(limit) * 8, int(limit) + 40), 180)
    sql = f"""
        SELECT DISTINCT r.*
        FROM kp_reports r
        LEFT JOIN kp_report_text_fts t ON CAST(t.report_id AS INTEGER) = r.id
        WHERE substr(COALESCE(NULLIF(r.published_at, ''), r.imported_at), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(r.published_at, ''), r.imported_at), 1, 10) <= ?
          AND ({' OR '.join(clauses)})
        ORDER BY COALESCE(NULLIF(r.published_at, ''), r.imported_at) DESC, r.id DESC
        LIMIT {int(sql_limit)}
    """
    rows = [_row_to_report(row) for row in conn.execute(sql, params)]
    primary = primary_terms or terms
    scored = [
        (_report_match_score(report, terms, primary), report)
        for report in rows
    ]
    min_score = 80 if primary_terms else 0
    scored = [(score, report) for score, report in scored if score >= min_score]
    scored.sort(
        key=lambda pair: (
            pair[0],
            pair[1].published_at or "",
            pair[1].row_id,
        ),
        reverse=True,
    )
    return [report for _, report in scored[: int(limit)]]


def _compact_text(text: str, max_chars: int) -> str:
    cleaned = re.sub(r"\s+", " ", text or "").strip()
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 3].rstrip() + "..."


def _strip_zsxq_metadata(text: str) -> str:
    cleaned = re.sub(r"<e\b[^>]*?/?>", " ", text or "", flags=re.IGNORECASE)
    cleaned = re.sub(r"\b(?:source|group_id|group_name|topic_id|author|published_at):\s*[^\n\r]+", " ", cleaned)
    cleaned = re.sub(r"\bfile_id=\d+\b", " ", cleaned)
    cleaned = re.sub(r"\bFiles:\s*", " ", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+-\s+", "；", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _clean_report_snippet(text: str, max_chars: int = 120) -> str:
    cleaned = _strip_zsxq_metadata(text)
    cleaned = re.sub(r"\s+source:\s*zsxq\b.*", "", cleaned, flags=re.IGNORECASE | re.DOTALL)
    cleaned = re.sub(r"\b(?:group_id|group_name|topic_id|author|published_at):\s*\S+", "", cleaned)
    cleaned = cleaned.replace("#", "").strip(" -:：")
    return _compact_text(cleaned, max_chars)


def _json_values(value: object) -> list[str]:
    try:
        parsed = json.loads(str(value or "[]"))
    except Exception:
        return []
    if not isinstance(parsed, list):
        return []
    result: list[str] = []
    for item in parsed:
        text = str(item or "").strip()
        if text and text not in result:
            result.append(text)
    return result


def _resolve_local_path(path_text: str) -> Path | None:
    if not path_text:
        return None
    path = Path(path_text)
    if path.is_absolute():
        return path
    candidates = [
        _REPO_ROOT / path,
        _REPO_ROOT / "data" / "knowledge_planet" / path,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return _REPO_ROOT / path


def _read_text_excerpt(path_text: str, max_chars: int = 5000) -> str:
    path = _resolve_local_path(path_text)
    if not path or not path.exists() or not path.is_file():
        return ""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    return _compact_text(text, max_chars)


def _report_research_excerpt(report: KpReport, max_chars: int = 2400) -> str:
    """Prefer extracted PDF text over titles so the report layer has real assumptions."""
    parts: list[str] = []
    if report.summary and report.summary.strip() and report.summary.strip() != report.title.strip():
        parts.append(report.summary.strip())
    extracted = _read_text_excerpt(report.extracted_text_path, max_chars=max_chars)
    if extracted:
        parts.append(extracted)
    if not parts:
        parts.append(report.title)
    return _compact_text("\n".join(parts), max_chars)


def _item_days_old(item: KpItem, end_date: str) -> int:
    published = _parse_date(item.published_at) or _parse_date(item.imported_at)
    end = _parse_date(end_date) or datetime.now()
    if not published:
        return 99
    return max(0, (end.date() - published.date()).days)


def _recency_weight(days_old: int) -> float:
    if days_old <= 0:
        return 2.0
    if days_old <= 2:
        return 1.5
    if days_old <= 6:
        return 1.0
    return 0.6


def _weighted_score(value: int, weight: float) -> int:
    return int(round(float(value) * weight))


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
    interpretation_source = _clean_report_snippet(item.summary or item.text or item.title, 260)
    interpretation = f"{event_type}：{interpretation_source}"
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


def _theme_marginal_view(theme: str, one_day: int, three_day: int, seven_day: int) -> tuple[str, str]:
    prior_four_days = max(0, seven_day - three_day)
    if one_day >= 3 and one_day >= prior_four_days:
        return "今日明显升温", "优先看是否有新催化剂，而不是简单追热度。"
    if three_day >= 5 and three_day > prior_four_days:
        return "近三日持续发酵", "适合寻找分歧低吸和最直接受益标的。"
    if prior_four_days > three_day and one_day == 0:
        return "热度边际回落", "更像背景主线，除非出现新事件，否则降低追高优先级。"
    if seven_day >= 5:
        return "七日延续", "有持续关注度，但需要公司层面验证承接。"
    return "低频线索", "作为观察项，暂不单独驱动交易。"


def _theme_daily_share_data(items: list[KpItem], report_dates: list[str], max_themes: int = 6) -> tuple[list[str], list[str], dict[str, list[float]]]:
    day_total: dict[str, int] = {date: 0 for date in report_dates}
    day_theme_counts: dict[str, Counter] = {date: Counter() for date in report_dates}
    seen_by_day: dict[str, set[str]] = {date: set() for date in report_dates}
    valid_dates = set(report_dates)
    for item in items:
        date = _item_date(item)
        if date not in valid_dates:
            continue
        key = _compact_text(f"{item.title}|{item.summary or item.text}", 120)
        if key in seen_by_day[date]:
            continue
        seen_by_day[date].add(key)
        text = f"{item.title}\n{item.text}\n{item.summary}"
        matched = [theme for theme in THEME_KEYWORDS if theme.lower() in text.lower()]
        if not matched:
            continue
        day_total[date] += 1
        for theme in set(matched):
            day_theme_counts[date][theme] += 1
    theme_scores = Counter()
    for date in report_dates:
        total = max(1, day_total[date])
        for theme, count in day_theme_counts[date].items():
            theme_scores[theme] += count / total
    top_themes = [theme for theme, _score in theme_scores.most_common(max_themes)]
    shares: dict[str, list[float]] = {}
    for theme in top_themes:
        shares[theme] = [
            round(day_theme_counts[date][theme] * 100 / max(1, day_total[date]), 1)
            for date in report_dates
        ]
    return report_dates, top_themes, shares


def _sparkline(values: list[float]) -> str:
    if not values:
        return ""
    blocks = "▁▂▃▄▅▆▇█"
    low = min(values)
    high = max(values)
    if high <= low:
        return blocks[0] * len(values)
    return "".join(blocks[min(len(blocks) - 1, int((value - low) / (high - low) * (len(blocks) - 1)))] for value in values)


def _theme_share_trend_lines(items: list[KpItem], report_dates: list[str]) -> list[str]:
    dates, themes, shares = _theme_daily_share_data(items, report_dates, max_themes=6)
    lines = [
        "",
        "## 题材热度边际变化",
        "",
        "按每日去重后的观点流占比衡量热度，而不是看绝对条数。这样能避免某天信息总量变化造成误判。",
    ]
    if not themes:
        lines.append("- 本窗口没有足够题材数据形成趋势。")
        return lines
    labels = [date[5:] for date in dates]
    max_share = max(max(values) for values in shares.values()) if shares else 10
    y_max = max(10, int(math.ceil(max_share / 10.0) * 10))
    lines.extend(["", "```mermaid", "xychart-beta", '  title "近七日题材热度占比（去重后）"'])
    lines.append("  x-axis [" + ", ".join(f'"{label}"' for label in labels) + "]")
    lines.append(f'  y-axis "占比%" 0 --> {y_max}')
    for theme in themes[:4]:
        values = ", ".join(f"{value:.1f}" for value in shares[theme])
        lines.append(f"  line [{values}]")
    lines.extend(["```", ""])
    lines.extend(["| 题材 | 趋势 | " + " | ".join(labels) + " | 边际判断 |", "| --- | --- | " + " | ".join("---:" for _ in labels) + " | --- |"])
    for theme in themes:
        values = shares[theme]
        first = values[0] if values else 0.0
        last = values[-1] if values else 0.0
        delta = last - first
        if delta >= 5:
            view = f"占比提升 {delta:.1f}pct，边际升温"
        elif delta <= -5:
            view = f"占比下降 {abs(delta):.1f}pct，边际降温"
        else:
            view = "占比变化不大，更多是延续"
        lines.append(
            f"| {_md_cell(theme)} | {_sparkline(values)} | "
            + " | ".join(f"{value:.1f}%" for value in values)
            + f" | {_md_cell(view)} |"
        )
    return lines


def _theme_lifecycle_view(theme: str, one_day: int, three_day: int, seven_day: int) -> tuple[str, str, str]:
    prior = max(0, seven_day - three_day)
    if one_day == 0 and three_day == 0 and seven_day > 0:
        return "退潮/背景", "只保留行业理解，不作为今日买点。", "等新事件或量价二次确认"
    if one_day >= 3 and three_day <= max(5, prior):
        return "早期升温", "优先寻找低位、直接受益、尚未被充分推荐的标的。", "小仓试错/埋伏"
    if three_day >= 8 and three_day > prior * 1.2:
        return "主升发酵", "看龙头承接和产业事件能否继续增强。", "分歧低吸，避免后排追高"
    if seven_day >= 20 and prior >= three_day:
        return "一致性偏高", "主线仍强，但更多是共识交易，赔率开始下降。", "只做核心，降低追高"
    if seven_day >= 8:
        return "持续观察", "有连续关注度，但需要公司层面验证和行情确认。", "观察/等催化"
    return "萌芽线索", "信息频率还低，先做产业链映射和候选储备。", "研究跟踪"


def _candidate_marginal_label(row: dict) -> str:
    one_day = int(row.get("mentions_1d") or 0)
    three_day_extra = int(row.get("mentions_3d") or 0)
    prior = int(row.get("mentions_prior") or 0)
    if one_day > 0 and three_day_extra + prior == 0:
        return "今日新增"
    if one_day >= 2:
        return "今日升温"
    if one_day > 0 and three_day_extra > 0:
        return "近三日延续"
    if three_day_extra > prior:
        return "近三日发酵"
    if prior > 0 and one_day == 0 and three_day_extra == 0:
        return "热度回落"
    return "七日背景"


def _candidate_crowding_label(row: dict) -> str:
    pump = int(row.get("pump") or 0)
    technical = row.get("technical")
    try:
        technical_value = int(technical)
    except Exception:
        technical_value = -1
    action = str(row.get("action") or "")
    if pump >= 45:
        return "极拥挤：卖方/情绪语言过强，优先回避追高"
    if pump >= 28 and technical_value >= 30:
        return "拥挤且偏高位：逻辑对也要等分歧"
    if pump >= 28:
        return "卖方一致性较高：需要二次验证"
    if "回避" in action or "不参与" in action:
        return "交易性不足：不因题材热度强做"
    if technical_value >= 34:
        return "趋势强但可能加速末端"
    if technical_value >= 20:
        return "拥挤度可控，等待触发"
    return "未明显拥挤，但需量价确认"


def _candidate_conviction_label(row: dict) -> str:
    total = int(row.get("total_score") or 0)
    pump = int(row.get("pump") or 0)
    llm_score = row.get("llm_score")
    try:
        llm_value = int(llm_score)
    except Exception:
        llm_value = -1
    fundamental = str(row.get("fundamental_text") or "")
    technical = row.get("technical")
    try:
        technical_value = int(technical)
    except Exception:
        technical_value = -1
    if total >= 78 and llm_value >= 78 and pump < 25 and "承接不足" not in fundamental:
        return "主升潜力：可重点深挖"
    if llm_value >= 65 and "承接不足" not in fundamental and pump < 35:
        return "逻辑成立：等回踩/二次验证"
    if pump >= 35:
        return "热闹但拥挤：防吹票"
    if technical_value >= 32 and total < 45:
        return "行情强于逻辑：防补涨陷阱"
    if "承接不足" in fundamental:
        return "承接偏弱：只观察"
    return "战术跟踪：等待更强证据"


def _event_date(event: KpEventSignal) -> str:
    return str(event.published_at or "")[:10]


def _item_date(item: KpItem) -> str:
    return str(item.published_at or item.imported_at or "")[:10]


def _high_value_event(event: KpEventSignal) -> bool:
    return (
        "低" not in event.confidence
        and event.event_type
        in {
            "订单/排产",
            "涨价/价格弹性",
            "库存/供需",
            "客户验证/导入",
            "产能/扩产",
            "政策/监管",
            "业绩/指引",
            "海外映射",
        }
    )


def _balanced_events_by_date(
    events: list[KpEventSignal],
    dates: list[str],
    *,
    max_per_day: int = 4,
    max_total: int = 18,
) -> list[KpEventSignal]:
    selected: list[KpEventSignal] = []
    seen_titles: set[str] = set()
    by_date: dict[str, list[KpEventSignal]] = defaultdict(list)
    for event in events:
        by_date[_event_date(event)].append(event)
    for date in dates:
        day_count = 0
        for event in by_date.get(date, []):
            key = _compact_text(event.title, 80)
            if key in seen_titles:
                continue
            selected.append(event)
            seen_titles.add(key)
            day_count += 1
            if day_count >= max_per_day:
                break
            if len(selected) >= max_total:
                return selected
    return selected


def _market_regime_lines(
    dates: list[str],
    event_signals: list[KpEventSignal],
    candidate_rows: list[dict],
) -> list[str]:
    latest_date = dates[-1] if dates else ""
    latest_events = [event for event in event_signals if _event_date(event) == latest_date and _high_value_event(event)]
    recent_events = [
        event
        for event in event_signals
        if _event_date(event) in set(dates[-3:])
        and _high_value_event(event)
    ]
    high_pump = sum(1 for row in candidate_rows[:10] if int(row.get("pump") or 0) >= 28)
    overheat = 0
    for row in candidate_rows[:10]:
        try:
            if int(row.get("technical") or 0) >= 32:
                overheat += 1
        except Exception:
            continue
    if latest_events:
        posture = "可以做题材，但只围绕真增量和直接受益标的。"
    elif recent_events:
        posture = "今日新增不足，更多是延续交易；适合等分歧，不适合追高。"
    else:
        posture = "缺少近端高质量催化，先把观点源作为观察池。"
    if high_pump >= 4 or overheat >= 4:
        posture += " 前排拥挤/高位特征明显，仓位应更轻。"
    return [
        f"- **市场环境**：最新日期高置信事件 {len(latest_events)} 条，近三日高置信事件 {len(recent_events)} 条；{posture}",
        f"- **风险偏好读法**：高吹票/高拥挤候选 {high_pump} 个，技术高位候选 {overheat} 个。若开盘强而量能不跟，优先兑现观察而非追入。",
    ]


def _event_quality_rows(event_signals: list[KpEventSignal], max_rows: int = 8) -> list[tuple[str, str, str, str, str]]:
    priority = {
        "订单/排产": 9,
        "客户验证/导入": 8,
        "涨价/价格弹性": 8,
        "库存/供需": 7,
        "业绩/指引": 7,
        "产能/扩产": 6,
        "政策/监管": 6,
        "海外映射": 5,
    }
    scored = []
    seen: set[str] = set()
    for event in event_signals:
        if not _high_value_event(event):
            continue
        key = _compact_text(event.interpretation or event.title, 80)
        if key in seen:
            continue
        seen.add(key)
        score = priority.get(event.event_type, 1)
        if "高" in event.confidence:
            score += 4
        elif "中" in event.confidence:
            score += 2
        scored.append((score, event))
    rows = []
    for _score, event in sorted(scored, key=lambda pair: pair[0], reverse=True)[:max_rows]:
        true_increment = "真增量" if event.event_type in {"订单/排产", "客户验证/导入", "涨价/价格弹性", "库存/供需", "业绩/指引"} else "半增量"
        rows.append(
            (
                event.published_at[:16],
                event.event_type,
                true_increment,
                _clean_report_snippet(event.interpretation or event.title, 120),
                event.verification,
            )
        )
    return rows


def _events_for_llm_review(event_signals: list[KpEventSignal], max_events: int = 14) -> list[KpEventSignal]:
    priority = {
        "客户验证/导入": 10,
        "订单/排产": 9,
        "涨价/价格弹性": 8,
        "库存/供需": 8,
        "业绩/指引": 7,
        "产能/扩产": 6,
        "政策/监管": 6,
        "海外映射": 5,
    }
    scored: list[tuple[int, KpEventSignal]] = []
    seen: set[str] = set()
    for event in event_signals:
        if not _high_value_event(event):
            continue
        key = _compact_text(f"{event.event_type}:{event.interpretation or event.title}", 100)
        if key in seen:
            continue
        seen.add(key)
        score = priority.get(event.event_type, 1)
        if "高" in event.confidence:
            score += 5
        elif "中" in event.confidence:
            score += 3
        if event.source_type in INFORMATION_RICH_TYPES:
            score += 3
        if _event_date(event) == max((_event_date(item) for item in event_signals), default=""):
            score += 2
        scored.append((score, event))

    by_type: dict[str, list[KpEventSignal]] = defaultdict(list)
    for _score, event in sorted(scored, key=lambda pair: pair[0], reverse=True):
        by_type[event.event_type].append(event)

    selected: list[KpEventSignal] = []
    while len(selected) < max_events and any(by_type.values()):
        for event_type in sorted(by_type, key=lambda item: priority.get(item, 0), reverse=True):
            if not by_type[event_type]:
                continue
            selected.append(by_type[event_type].pop(0))
            if len(selected) >= max_events:
                break
    return selected


def _event_evidence_for_llm(event_signals: list[KpEventSignal], max_events: int = 14) -> str:
    rows = []
    selected_events = _events_for_llm_review(event_signals, max_events=max_events)
    for index, event in enumerate(selected_events, start=1):
        rows.append(
            f"{index}. 时间：{event.published_at[:16]}\n"
            f"   来源类型：{event.source_type}；事件类型：{event.event_type}；规则置信度：{event.confidence}\n"
            f"   线索：{_clean_report_snippet(event.interpretation or event.title, 220)}\n"
            f"   涉及标的/主题：{' / '.join([*event.companies[:3], *event.themes[:3]]) or '待映射'}\n"
            f"   规则验证点：{event.verification}"
        )
    if not rows:
        return "本窗口没有规则层筛出的高价值事件。"
    return "\n".join(rows)


def _build_event_review_prompt(
    event_signals: list[KpEventSignal],
    *,
    start_date: str,
    end_date: str,
    max_events: int = 14,
) -> str:
    evidence = _event_evidence_for_llm(event_signals, max_events=max_events)
    return f"""你是A股基金经理的盘前研究员，任务是先审稿，不是选股。
统计窗口：{start_date} 至 {end_date}

下面是系统从知识星球观点流里初筛出来的事件线索：
{evidence}

请逐条判断：这条线索对交易到底是不是“真增量”。不要因为它看起来热、被频繁提及、或卖方措辞强就给高评价。

判断标准：
1. 真增量：订单/排产/价格/库存/客户验证/业绩指引/政策实质变化，且能映射到收入、利润、估值或风险偏好。
2. 半增量：有产业含义，但需要二次验证，或只是从宏观/海外/产业链映射到A股。
3. 情绪重复：主要是重复市场已知叙事、卖方强call、目标市值故事。
4. 噪音：缺少可验证指标，或和交易机会关系很弱。

请返回严格 JSON，不要 Markdown，不要额外解释。字段：
{{
  "events": [
    {{
      "event_type": "事件类型",
      "increment_level": "真增量/半增量/情绪重复/噪音",
      "evidence_grade": "高/中/低",
      "impact_path": "它如何影响收入/利润/估值/风险偏好/供需，若没有就写无清晰影响路径",
      "beneficiaries": "直接受益公司/环节；如果只是蹭概念要明确指出",
      "verification": "未来1-4周最该验证的指标",
      "risk": "最可能证伪或过度乐观的地方",
      "summary": "一句话给PM看的结论"
    }}
  ]
}}
"""


def _run_llm_event_review(
    llm,
    event_signals: list[KpEventSignal],
    *,
    start_date: str,
    end_date: str,
    max_events: int = 14,
) -> list[EventLLMReview]:
    if not event_signals:
        return []
    try:
        prompt = _build_event_review_prompt(
            event_signals,
            start_date=start_date,
            end_date=end_date,
            max_events=max_events,
        )
        system_text = (
            "你是A股盘前日报的事件审稿员。只判断信息是否构成交易增量。"
            "输出必须是可解析JSON，不要编造材料之外的信息。"
        )
        try:
            from langchain_core.messages import HumanMessage, SystemMessage

            llm_input = [SystemMessage(content=system_text), HumanMessage(content=prompt)]
        except Exception:
            llm_input = f"{system_text}\n\n{prompt}"
        response = llm.invoke(llm_input)
        parsed = _json_from_text(str(getattr(response, "content", response)))
        raw_events = parsed.get("events", [])
        if not isinstance(raw_events, list):
            return []
        reviews = []
        for raw in raw_events[:max_events]:
            if not isinstance(raw, dict):
                continue
            reviews.append(
                EventLLMReview(
                    event_type=_compact_text(str(raw.get("event_type", "")), 80),
                    increment_level=_compact_text(str(raw.get("increment_level", "待验证")), 40),
                    evidence_grade=_compact_text(str(raw.get("evidence_grade", "中")), 20),
                    impact_path=_compact_text(str(raw.get("impact_path", "")), 180),
                    beneficiaries=_compact_text(str(raw.get("beneficiaries", "")), 160),
                    verification=_compact_text(str(raw.get("verification", "")), 160),
                    risk=_compact_text(str(raw.get("risk", "")), 160),
                    summary=_compact_text(str(raw.get("summary", "")), 180),
                    status="analyzed",
                )
            )
        return reviews
    except Exception as exc:
        return [
            EventLLMReview(
                event_type="事件审稿失败",
                increment_level="待验证",
                evidence_grade="低",
                impact_path="",
                beneficiaries="",
                verification="",
                risk=_compact_text(str(exc), 160),
                summary="LLM事件审稿失败，回退到规则事件库。",
                status="failed",
            )
        ]


def _event_review_lines_for_prompt(event_reviews: list[EventLLMReview]) -> list[str]:
    lines = []
    for review in event_reviews:
        if review.status == "failed":
            continue
        lines.append(
            "- "
            f"{review.event_type}/{review.increment_level}/{review.evidence_grade}: "
            f"{review.summary or review.impact_path}；受益：{review.beneficiaries or '待定'}；"
            f"验证：{review.verification or '待验证'}；风险：{review.risk or 'NA'}"
        )
    return lines


def _candidate_data_value(data: dict) -> float:
    mentions = max(1, int(data.get("mentions") or 0))
    score = int(data.get("score") or 0)
    pump = int(data.get("pump") or 0)
    recency = float(data.get("recency_score") or 0.0)
    return score / mentions + recency * 2 - pump * 0.25


def _candidate_data_text(data: dict) -> str:
    parts = [
        str(data.get("display_name") or ""),
        " ".join(str(item) for item in data.get("source_labels", []) if item),
        " ".join(str(item) for item in data.get("opportunity_types", []) if item),
        " ".join(str(item) for item in data.get("preprocess_evidence", []) if item),
    ]
    item_list = data.get("items", [])
    if isinstance(item_list, list):
        parts.extend(str(getattr(item, "title", "")) for item in item_list[:3])
    return " ".join(parts)


def _candidate_data_lane(data: dict) -> str:
    text = _candidate_data_text(data)
    opportunity_types = {str(item) for item in data.get("opportunity_types", []) if item}
    source_labels = {str(item) for item in data.get("source_labels", []) if item}
    if "低频预期差" in opportunity_types:
        return "low_frequency"
    if "研报假设待交叉验证" in opportunity_types or "研报假设资产" in source_labels:
        return "report_assumption"
    if any(keyword in text for keyword in NON_TECH_ALPHA_KEYWORDS):
        return "non_tech_alpha"
    if int(data.get("mentions") or 0) <= 3 or float(data.get("recency_score") or 0.0) <= 3.5:
        return "low_frequency"
    if any(keyword in text for keyword in TECH_HOT_THEME_KEYWORDS):
        return "tech_hot"
    return "balanced"


def _select_candidate_targets(
    stock_ranked: list[tuple[str, dict]],
    limit: int,
) -> list[tuple[str, dict]]:
    """Diversify expensive Tushare/LLM work across hot names, research assets, and low-frequency alpha."""
    if limit <= 0:
        return []
    selected: list[tuple[str, dict]] = []
    selected_keys: set[str] = set()

    def add_many(rows: list[tuple[str, dict]], count: int) -> None:
        for key, data in rows:
            if len(selected) >= limit or count <= 0:
                return
            if key in selected_keys:
                continue
            selected.append((key, data))
            selected_keys.add(key)
            count -= 1

    lane_rows: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for key, data in stock_ranked:
        lane_rows[_candidate_data_lane(data)].append((key, data))
    for lane in lane_rows:
        lane_rows[lane].sort(key=lambda pair: _candidate_data_value(pair[1]), reverse=True)

    quotas = [
        ("non_tech_alpha", max(1, int(limit * 0.22))),
        ("report_assumption", max(1, int(round(limit * 0.30)))),
        ("low_frequency", max(1, int(limit * 0.22))),
        ("balanced", max(1, int(limit * 0.12))),
        ("tech_hot", max(1, limit - len(selected))),
    ]
    for lane, quota in quotas:
        add_many(lane_rows.get(lane, []), quota)
    add_many(stock_ranked, limit - len(selected))
    return selected


def _six_dimension_overview_lines(
    *,
    report_dates: list[str],
    theme_1d_counts: Counter,
    theme_3d_counts: Counter,
    theme_7d_counts: Counter,
    event_signals: list[KpEventSignal],
    candidate_rows: list[dict],
) -> list[str]:
    lines = [
        "",
        "## 六维投资判断总览",
        "",
        "### 1. 市场环境判断",
    ]
    lines.extend(_market_regime_lines(report_dates, event_signals, candidate_rows))

    lines.extend(
        [
            "",
            "### 2. 观点源真增量过滤",
            "",
            "| 时间 | 类型 | 增量属性 | 信息翻译 | 下一步验证 |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    event_rows = _event_quality_rows(event_signals)
    if event_rows:
        for date, event_type, increment, interpretation, verification in event_rows:
            lines.append(
                f"| {date} | {_md_cell(event_type)} | {_md_cell(increment)} | {_md_cell(interpretation)} | {_md_cell(verification)} |"
            )
    else:
        lines.append("| NA | NA | 缺少真增量 | 本窗口高质量事件不足，先观察。 | 等新增订单/价格/客户验证 |")

    lines.extend(
        [
            "",
            "### 3. 题材生命周期判断",
            "",
            "| 题材 | 近1日 | 近3日 | 近7日 | 生命周期 | 操作含义 | 交易姿态 |",
            "| --- | ---: | ---: | ---: | --- | --- | --- |",
        ]
    )
    themes = sorted(
        set(theme_7d_counts) | set(theme_3d_counts) | set(theme_1d_counts),
        key=lambda theme: (theme_1d_counts[theme] * 4 + theme_3d_counts[theme] * 2 + theme_7d_counts[theme]),
        reverse=True,
    )
    for theme in themes[:10]:
        one_day = int(theme_1d_counts[theme])
        three_day = int(theme_3d_counts[theme])
        seven_day = int(theme_7d_counts[theme])
        stage, implication, posture = _theme_lifecycle_view(theme, one_day, three_day, seven_day)
        lines.append(
            f"| {_md_cell(theme)} | {one_day} | {three_day} | {seven_day} | {_md_cell(stage)} | {_md_cell(implication)} | {_md_cell(posture)} |"
        )

    lines.extend(
        [
            "",
            "### 4. 单票：预期差 - 承接 - 交易点",
            "",
            "| 标的 | 判断 | 预期差 | 公司承接 | 交易点 |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in candidate_rows[:8]:
        name = f"{row.get('name')}（{row.get('symbol')}）"
        conviction = _candidate_conviction_label(row)
        expectation = _compact_text(str(row.get("expectation_gap") or row.get("signal_interpretation") or row.get("note") or ""), 110)
        relevance = _compact_text(str(row.get("company_relevance") or row.get("fundamental_text") or ""), 80)
        entry = _compact_text(str(row.get("entry_plan") or row.get("action") or ""), 100)
        lines.append(
            f"| {_md_cell(name)} | {_md_cell(conviction)} | {_md_cell(expectation)} | {_md_cell(relevance)} | {_md_cell(entry)} |"
        )

    lines.extend(
        [
            "",
            "### 5. 拥挤度 / 一致预期风控",
            "",
            "| 标的 | 吹票风险 | 技术面 | 拥挤度判断 | 处理 |",
            "| --- | ---: | --- | --- | --- |",
        ]
    )
    for row in sorted(candidate_rows[:10], key=lambda item: int(item.get("pump") or 0), reverse=True)[:6]:
        name = f"{row.get('name')}（{row.get('symbol')}）"
        lines.append(
            f"| {_md_cell(name)} | {int(row.get('pump') or 0)} | {_md_cell(row.get('technical'))}/40 | "
            f"{_md_cell(_candidate_crowding_label(row))} | {_md_cell(_compact_text(str(row.get('action') or row.get('bucket')), 80))} |"
        )

    lines.extend(
        [
            "",
            "### 6. 复盘学习样本",
            "",
            "| 标的 | 当前动作 | 复盘窗口 | 需要记录的结果 |",
            "| --- | --- | --- | --- |",
        ]
    )
    review_rows = candidate_rows[:6]
    if review_rows:
        for row in review_rows:
            name = f"{row.get('name')}（{row.get('symbol')}）"
            lines.append(
                f"| {_md_cell(name)} | {_md_cell(_compact_text(str(row.get('action') or row.get('bucket')), 80))} | 1/3/5/10 日 | "
                f"{_md_cell('是否触发买点、是否证伪、相对主线强弱、来源是否有效')} |"
            )
    else:
        lines.append("| 暂无 | 观察 | 1/3/5/10 日 | 无候选，不做强行复盘 |")
    return lines


def _candidate_main_rise_score(row: dict) -> int:
    """Score whether a candidate can evolve into a multi-day main-rise idea."""
    llm_score = row.get("llm_score")
    try:
        logic = int(llm_score)
    except Exception:
        logic = min(65, int(row.get("signal_score") or 0))
    recency = min(15, int(float(row.get("recency_score") or 0.0) * 3))
    fundamental_text = str(row.get("fundamental_text") or "")
    if "验证通过" in fundamental_text:
        fundamental = 18
    elif "部分验证" in fundamental_text:
        fundamental = 12
    elif "弱验证" in fundamental_text:
        fundamental = 4
    elif "承接不足" in fundamental_text:
        fundamental = -12
    else:
        fundamental = 0
    try:
        technical = int(row.get("technical") or 0)
    except Exception:
        technical = 0
    if 18 <= technical <= 32:
        tech_window = 12
    elif technical > 32:
        tech_window = 4
    elif technical > 0:
        tech_window = 6
    else:
        tech_window = 0
    pump_penalty = min(25, int(row.get("pump") or 0) // 2)
    score = int(logic * 0.45) + recency + fundamental + tech_window - pump_penalty
    return max(0, min(100, score))


def _candidate_short_trade_score(row: dict) -> int:
    """Score whether a candidate is actionable in the near-term trading window."""
    try:
        technical = int(row.get("technical") or 0)
    except Exception:
        technical = 0
    try:
        logic = int(row.get("llm_score") or 0)
    except Exception:
        logic = int(row.get("signal_score") or 0)
    one_day = int(row.get("mentions_1d") or 0)
    three_day = int(row.get("mentions_3d") or 0)
    recency = min(18, one_day * 5 + three_day * 2)
    pump = int(row.get("pump") or 0)
    overheat_penalty = 0
    action = str(row.get("action") or "")
    if technical >= 35:
        overheat_penalty += 8
    if "追高" in action or "回避" in action or "不参与" in action:
        overheat_penalty += 10
    score = int(technical * 1.1) + int(logic * 0.25) + recency - min(20, pump // 2) - overheat_penalty
    return max(0, min(100, score))


def _dual_score_label(row: dict) -> str:
    main_score = int(row.get("main_rise_score") or 0)
    trade_score = int(row.get("short_trade_score") or 0)
    if main_score >= 72 and trade_score >= 55:
        return "主升潜力较强，等待触发后可小仓"
    if main_score >= 72:
        return "适合埋伏研究，但今日交易点不佳"
    if trade_score >= 65:
        return "短线可交易，但不一定适合埋伏"
    if main_score >= 55:
        return "有研究价值，等待新证据"
    return "暂不进入核心机会池"


def _dual_score_lines(candidate_rows: list[dict]) -> list[str]:
    lines = [
        "",
        "## 双评分系统：主升潜力 vs 短线交易",
        "",
        "| 标的 | 主升潜力分 | 短线交易分 | 结论 |",
        "| --- | ---: | ---: | --- |",
    ]
    for row in sorted(
        candidate_rows,
        key=lambda item: (int(item.get("main_rise_score") or 0), int(item.get("short_trade_score") or 0)),
        reverse=True,
    )[:10]:
        name = f"{row.get('name')}（{row.get('symbol')}）"
        lines.append(
            f"| {_md_cell(name)} | {int(row.get('main_rise_score') or 0)} | "
            f"{int(row.get('short_trade_score') or 0)} | {_md_cell(_dual_score_label(row))} |"
        )
    return lines


def _structured_event_library_lines(
    event_signals: list[KpEventSignal],
    event_reviews: list[EventLLMReview] | None = None,
) -> list[str]:
    lines = [
        "",
        "## 结构化事件库：LLM前置审稿",
        "",
        "| 事件类型 | 增量属性 | 证据等级 | 影响环节 | 代表线索 | 验证指标 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    analyzed_reviews = [
        review
        for review in (event_reviews or [])
        if review.status == "analyzed"
    ]
    if analyzed_reviews:
        for review in analyzed_reviews[:14]:
            lines.append(
                f"| {_md_cell(review.event_type)} | {_md_cell(review.increment_level)} | "
                f"{_md_cell(review.evidence_grade)} | {_md_cell(review.impact_path)} | "
                f"{_md_cell(review.beneficiaries or review.summary)} | {_md_cell(review.verification)} |"
            )
        return lines
    failed_reviews = [
        review
        for review in (event_reviews or [])
        if review.status == "failed"
    ]
    if failed_reviews:
        lines.append(
            f"| 事件审稿失败 | 待验证 | 低 | 回退规则层 | "
            f"{_md_cell(failed_reviews[0].summary)} | {_md_cell(failed_reviews[0].risk)} |"
        )
    rows = _event_quality_rows(event_signals, max_rows=14)
    if not rows:
        lines.append("| 暂无 | 噪音偏多 | 低 | NA | 缺少真增量 | 等待后续事件 |")
        return lines
    for _date, event_type, increment, interpretation, verification in rows:
        if event_type in {"订单/排产", "客户验证/导入"}:
            impact = "收入/订单兑现"
        elif event_type in {"涨价/价格弹性", "库存/供需"}:
            impact = "毛利率/供需"
        elif event_type == "业绩/指引":
            impact = "盈利预测"
        elif event_type == "政策/监管":
            impact = "风险偏好/估值"
        else:
            impact = "产业趋势/映射"
        evidence = "高：数据/渠道" if increment == "真增量" else "中：推演/映射"
        lines.append(
            f"| {_md_cell(event_type)} | {_md_cell(increment)} | {_md_cell(evidence)} | {_md_cell(impact)} | "
            f"{_md_cell(interpretation)} | {_md_cell(verification)} |"
        )
    return lines


def _pdf_research_lens_lines(reports: list[KpReport], max_rows: int = 12) -> list[str]:
    lines = [
        "",
        "## PDF 研报结构化抽取层",
        "",
        "| 研报 | 研究用途 | 可抽取假设 | 如何交叉验证观点流 |",
        "| --- | --- | --- | --- |",
    ]
    if not reports:
        lines.append("| 暂无 | NA | NA | 本窗口未导入 PDF 研报 |")
        return lines
    for report in reports[:max_rows]:
        text = " ".join([report.title, report.summary, " ".join(report.themes), " ".join(report.industries)])
        if any(word in text for word in ("策略", "宏观", "资产", "资金流")):
            use = "判断风险偏好和市场环境"
            assumption = "资产配置、流动性、风险偏好"
            cross = "用于校准今日题材仓位，不直接推单票"
        elif any(word in text for word in ("周报", "价格", "库存", "供需", "SMM")):
            use = "提取行业 KPI"
            assumption = "价格、库存、开工率、订单"
            cross = "验证观点流里的涨价/去库/排产线索"
        elif report.tickers or report.companies:
            use = "单票框架和盈利假设"
            assumption = "收入、毛利率、估值方法、目标价假设"
            cross = "检查卖方故事能否落到业绩和市值空间"
        else:
            use = "产业链映射"
            assumption = "环节位置、可比公司、关键变量"
            cross = "辅助判断谁是核心受益而非蹭概念"
        lines.append(
            f"| {_md_cell(_compact_text(report.title, 90))} | {_md_cell(use)} | {_md_cell(assumption)} | {_md_cell(cross)} |"
        )
    return lines


def _theme_lifecycle_persistence_rows(
    theme_1d_counts: Counter,
    theme_3d_counts: Counter,
    theme_7d_counts: Counter,
) -> list[dict]:
    rows = []
    themes = sorted(
        set(theme_7d_counts) | set(theme_3d_counts) | set(theme_1d_counts),
        key=lambda theme: (theme_1d_counts[theme] * 4 + theme_3d_counts[theme] * 2 + theme_7d_counts[theme]),
        reverse=True,
    )
    for theme in themes[:20]:
        one_day = int(theme_1d_counts[theme])
        three_day = int(theme_3d_counts[theme])
        seven_day = int(theme_7d_counts[theme])
        stage, implication, posture = _theme_lifecycle_view(theme, one_day, three_day, seven_day)
        rows.append(
            {
                "theme": theme,
                "one_day": one_day,
                "three_day": three_day,
                "seven_day": seven_day,
                "stage": stage,
                "implication": implication,
                "posture": posture,
            }
        )
    return rows


def _persist_daily_research_state(
    report_date: str,
    theme_rows: list[dict],
    candidate_rows: list[dict],
) -> str:
    try:
        db_path = _db_path()
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(db_path)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS kp_theme_lifecycle (
                report_date TEXT NOT NULL,
                theme TEXT NOT NULL,
                one_day INTEGER,
                three_day INTEGER,
                seven_day INTEGER,
                stage TEXT,
                implication TEXT,
                posture TEXT,
                updated_at TEXT,
                PRIMARY KEY (report_date, theme)
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS kp_daily_candidate_reviews (
                report_date TEXT NOT NULL,
                symbol TEXT NOT NULL,
                name TEXT,
                main_rise_score INTEGER,
                short_trade_score INTEGER,
                bucket TEXT,
                action TEXT,
                review_status TEXT,
                payload_json TEXT,
                updated_at TEXT,
                PRIMARY KEY (report_date, symbol)
            )
            """
        )
        now_text = datetime.now().isoformat(timespec="seconds")
        for row in theme_rows:
            conn.execute(
                """
                INSERT OR REPLACE INTO kp_theme_lifecycle (
                    report_date, theme, one_day, three_day, seven_day, stage,
                    implication, posture, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    report_date,
                    row["theme"],
                    row["one_day"],
                    row["three_day"],
                    row["seven_day"],
                    row["stage"],
                    row["implication"],
                    row["posture"],
                    now_text,
                ),
            )
        for row in candidate_rows[:20]:
            symbol = str(row.get("symbol") or row.get("name") or "UNKNOWN")
            conn.execute(
                """
                INSERT OR REPLACE INTO kp_daily_candidate_reviews (
                    report_date, symbol, name, main_rise_score, short_trade_score,
                    bucket, action, review_status, payload_json, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    report_date,
                    symbol,
                    str(row.get("name") or ""),
                    int(row.get("main_rise_score") or 0),
                    int(row.get("short_trade_score") or 0),
                    str(row.get("bucket") or ""),
                    str(row.get("action") or ""),
                    "pending_1_3_5_10d_review",
                    json.dumps(row, ensure_ascii=False, default=str),
                    now_text,
                ),
            )
        conn.commit()
        conn.close()
        return f"已写入主题生命周期 {len(theme_rows)} 条、候选复盘 {min(20, len(candidate_rows))} 条"
    except Exception as exc:
        return f"写入失败：{_compact_text(str(exc), 160)}"


def _pm_control_prompt(
    *,
    start_date: str,
    end_date: str,
    event_signals: list[KpEventSignal],
    event_reviews: list[EventLLMReview] | None,
    candidate_rows: list[dict],
    lifecycle_rows: list[dict],
    reports: list[KpReport],
) -> str:
    event_lines = _event_review_lines_for_prompt(event_reviews or [])
    if not event_lines:
        for _date, event_type, increment, interpretation, verification in _event_quality_rows(event_signals, max_rows=10):
            event_lines.append(f"- {event_type}/{increment}: {interpretation}；验证：{verification}")
    candidate_lines = []
    for row in candidate_rows[:10]:
        candidate_lines.append(
            "- "
            f"{row.get('name')}({row.get('symbol')}): 主升{row.get('main_rise_score')}, "
            f"短线{row.get('short_trade_score')}, 分层{row.get('bucket')}, "
            f"拥挤{row.get('pump')}, 结论{_compact_text(str(row.get('action') or ''), 80)}, "
            f"预期差{_compact_text(str(row.get('expectation_gap') or row.get('signal_interpretation') or ''), 100)}"
        )
    lifecycle_lines = [
        f"- {row['theme']}: {row['stage']}，近1/3/7日={row['one_day']}/{row['three_day']}/{row['seven_day']}，{row['posture']}"
        for row in lifecycle_rows[:10]
    ]
    report_lines = [
        f"- {report.title}: {_report_research_excerpt(report, max_chars=320)}"
        for report in reports[:10]
    ]
    return f"""你是一个A股题材交易基金经理总控，不是单票分析师。你要读完结构化事件、题材生命周期、候选双评分和研报线索后，做最终盘前取舍。

统计窗口：{start_date} 至 {end_date}

LLM/规则前置事件审稿：
{chr(10).join(event_lines) or "- 暂无高质量事件"}

题材生命周期：
{chr(10).join(lifecycle_lines) or "- 暂无清晰主线"}

候选双评分：
{chr(10).join(candidate_lines) or "- 暂无候选"}

PDF研报线索：
{chr(10).join(report_lines) or "- 暂无PDF研报"}

请用优秀基金经理/顶级游资交易员的视角输出最终判断。重点不是复述，而是取舍：今天能不能做、做哪条主线、哪些票适合埋伏、哪些只等回踩、哪些热但不能碰。

必须遵守：
1. 不要平均主义。如果没有合格建仓对象，必须明确说没有。
2. 先按事件审稿判断“真增量”是否足够，再决定候选票是否值得进入组合。
3. 必须指出最容易骗过系统的热门陷阱，例如卖方强call、逻辑链太长、技术面加速末端。
4. 必须找出一个低频但可能有预期差的线索；如果没有，也要明确说没有。
5. 行业研究、宏观研究、海外映射和策略研报不能只当背景，必须提炼成“对题材仓位/主线/验证指标的影响”。
6. PM层不直接替代单票TradingAgents，A桶或中仓动作必须要求单票复核。

返回严格 JSON，不要 Markdown，不要额外解释。字段：
{{
  "market_posture": "今日市场/题材环境判断，说明适合小仓试错、低吸、追强还是观望",
  "mainline_judgment": "最重要主线的生命周期和取舍",
  "opportunity_focus": "最值得深挖或埋伏的1-3个机会，没有就说没有，并说明原因",
  "watchlist": "等回踩/二次验证的名单和条件",
  "avoid_list": "热但赔率差或吹票拥挤的名单",
  "trigger_conditions": "明日/未来一周最关键的触发条件",
  "portfolio_action": "组合动作：仓位、节奏、是否需要单票TradingAgents复核",
    "review_tasks": "需要进入1/3/5/10日复盘的内容"
}}
"""


def _llm_field_text(value: object, max_chars: int = 260) -> str:
    if value is None:
        return ""
    if isinstance(value, dict):
        parts = []
        for key, item in value.items():
            if isinstance(item, (list, tuple)):
                item_text = "；".join(str(part) for part in item)
            elif isinstance(item, dict):
                item_text = "；".join(f"{inner_key}: {inner_value}" for inner_key, inner_value in item.items())
            else:
                item_text = str(item)
            parts.append(f"{key}: {item_text}")
        return _compact_text("；".join(parts), max_chars)
    if isinstance(value, (list, tuple)):
        return _compact_text("；".join(str(item) for item in value), max_chars)
    return _compact_text(str(value), max_chars)


def _run_pm_control_analysis(
    llm,
    *,
    start_date: str,
    end_date: str,
    event_signals: list[KpEventSignal],
    event_reviews: list[EventLLMReview] | None,
    candidate_rows: list[dict],
    lifecycle_rows: list[dict],
    reports: list[KpReport],
) -> PmControlAnalysis:
    try:
        prompt = _pm_control_prompt(
            start_date=start_date,
            end_date=end_date,
            event_signals=event_signals,
            event_reviews=event_reviews,
            candidate_rows=candidate_rows,
            lifecycle_rows=lifecycle_rows,
            reports=reports,
        )
        system_text = "你是A股题材交易日报的PM总控。输出必须是可解析JSON。"
        try:
            from langchain_core.messages import HumanMessage, SystemMessage

            llm_input = [SystemMessage(content=system_text), HumanMessage(content=prompt)]
        except Exception:
            llm_input = f"{system_text}\n\n{prompt}"
        response = llm.invoke(llm_input)
        parsed = _json_from_text(str(getattr(response, "content", response)))
        return PmControlAnalysis(
            market_posture=_llm_field_text(parsed.get("market_posture", ""), 260),
            mainline_judgment=_llm_field_text(parsed.get("mainline_judgment", ""), 260),
            opportunity_focus=_llm_field_text(parsed.get("opportunity_focus", ""), 260),
            watchlist=_llm_field_text(parsed.get("watchlist", ""), 260),
            avoid_list=_llm_field_text(parsed.get("avoid_list", ""), 260),
            trigger_conditions=_llm_field_text(parsed.get("trigger_conditions", ""), 260),
            portfolio_action=_llm_field_text(parsed.get("portfolio_action", ""), 260),
            review_tasks=_llm_field_text(parsed.get("review_tasks", ""), 260),
            status="analyzed",
        )
    except Exception as exc:
        return PmControlAnalysis(
            market_posture="PM总控LLM分析失败，使用规则层六维判断。",
            mainline_judgment="",
            opportunity_focus="",
            watchlist="",
            avoid_list="",
            trigger_conditions="",
            portfolio_action="",
            review_tasks=_compact_text(str(exc), 160),
            status="failed",
        )


def _deterministic_pm_control(
    candidate_rows: list[dict],
    lifecycle_rows: list[dict],
    event_signals: list[KpEventSignal],
) -> PmControlAnalysis:
    top_main = sorted(candidate_rows, key=lambda row: int(row.get("main_rise_score") or 0), reverse=True)[:3]
    top_trade = sorted(candidate_rows, key=lambda row: int(row.get("short_trade_score") or 0), reverse=True)[:3]
    crowded = [row for row in candidate_rows if int(row.get("pump") or 0) >= 28][:3]
    mainline = lifecycle_rows[0] if lifecycle_rows else {}
    high_events = [event for event in event_signals if _high_value_event(event)]
    posture = "有高质量事件，可小仓试错或等待分歧低吸。" if high_events else "缺少高质量事件，优先观望。"
    return PmControlAnalysis(
        market_posture=posture,
        mainline_judgment=(
            f"{mainline.get('theme', '无清晰主线')}处于{mainline.get('stage', 'NA')}，"
            f"{mainline.get('posture', '先观察')}"
        ),
        opportunity_focus="、".join(str(row.get("name")) for row in top_main) or "暂无",
        watchlist="、".join(str(row.get("name")) for row in top_trade) or "暂无",
        avoid_list="、".join(str(row.get("name")) for row in crowded) or "暂无",
        trigger_conditions="订单/价格/客户验证继续增强，且核心票出现缩量回踩或二次放量确认。",
        portfolio_action="先以观察池和小仓试错为主；A/B桶建仓前仍建议跑单票TradingAgents复核。",
        review_tasks="记录前排候选1/3/5/10日收益、是否触发买点、是否证伪、是否跑赢主线。",
        status="rule_based",
    )


def _pm_control_lines(pm_control: PmControlAnalysis) -> list[str]:
    return [
        "",
        "## PM总控层：最终取舍",
        "",
        f"- **状态**：{pm_control.status}",
        f"- **市场姿态**：{pm_control.market_posture or 'NA'}",
        f"- **主线判断**：{pm_control.mainline_judgment or 'NA'}",
        f"- **机会焦点**：{pm_control.opportunity_focus or '暂无'}",
        f"- **观察/等回踩**：{pm_control.watchlist or '暂无'}",
        f"- **回避/降权**：{pm_control.avoid_list or '暂无'}",
        f"- **触发条件**：{pm_control.trigger_conditions or '暂无'}",
        f"- **组合动作**：{pm_control.portfolio_action or '暂无'}",
        f"- **复盘任务**：{pm_control.review_tasks or '暂无'}",
    ]


def _daily_evolution_rows(
    items: list[KpItem],
    event_signals: list[KpEventSignal],
    dates: list[str],
) -> list[tuple[str, int, int, str, str, str]]:
    rows: list[tuple[str, int, int, str, str, str]] = []
    items_by_date: dict[str, list[KpItem]] = defaultdict(list)
    events_by_date: dict[str, list[KpEventSignal]] = defaultdict(list)
    for item in items:
        items_by_date[_item_date(item)].append(item)
    for event in event_signals:
        events_by_date[_event_date(event)].append(event)

    previous_theme_score: Counter | None = None
    for date in dates:
        day_items = items_by_date.get(date, [])
        day_events = [event for event in events_by_date.get(date, []) if _high_value_event(event)]
        theme_score = Counter()
        for item in day_items:
            text = f"{item.title}\n{item.text}\n{item.summary}"
            for theme in THEME_KEYWORDS:
                if theme.lower() in text.lower():
                    theme_score[theme] += 1
        top_themes = " / ".join(theme for theme, _count in theme_score.most_common(4)) or "无清晰主线"
        if previous_theme_score is None:
            marginal = "窗口起点，建立背景样本。"
        else:
            rising = [
                theme
                for theme, count in theme_score.most_common(6)
                if count > previous_theme_score.get(theme, 0)
            ]
            fading = [
                theme
                for theme, count in previous_theme_score.most_common(6)
                if theme_score.get(theme, 0) < count
            ]
            if rising:
                marginal = "升温：" + " / ".join(rising[:3])
            elif fading:
                marginal = "降温：" + " / ".join(fading[:3])
            else:
                marginal = "延续，无明显新升温主线。"
        event_text = "；".join(
            _clean_report_snippet(event.interpretation or event.title, 70) for event in day_events[:3]
        ) or "缺少高置信事件，更多是背景噪声。"
        rows.append((date, len(day_items), len(day_events), top_themes, marginal, event_text))
        previous_theme_score = theme_score
    return rows


def _pm_takeaway_lines(
    candidate_rows: list[dict],
    mainline_rows: list[tuple[str, int, str, str, str]],
    event_signals: list[KpEventSignal],
    reports: list[KpReport],
) -> list[str]:
    buildable = [
        row
        for row in candidate_rows
        if str(row.get("bucket", "")).startswith("A")
        and int(row.get("pump") or 0) < 28
    ]
    watchable = [
        row
        for row in candidate_rows
        if _candidate_conviction_label(row) in {"主升潜力：可重点深挖", "逻辑成立：等回踩/二次验证"}
    ]
    hot_but_risky = [
        row
        for row in candidate_rows
        if int(row.get("pump") or 0) >= 28
        or "追高" in str(row.get("action", ""))
    ]
    core_line = mainline_rows[0][0] if mainline_rows else "无清晰主线"
    event_mix = Counter(event.event_type for event in event_signals if _high_value_event(event))
    event_desc = " / ".join(f"{kind}{count}" for kind, count in event_mix.most_common(3)) or "缺少高置信事件"
    build_candidates = "、".join(str(row.get("name")) for row in buildable[:3]) or "暂无"
    watch_candidates = "、".join(str(row.get("name")) for row in watchable[:5]) or "暂无"
    avoid_candidates = "、".join(str(row.get("name")) for row in hot_but_risky[:3]) or "暂无"
    report_lens = (
        "PDF研报较多，重点用来抽取产业链KPI和海外映射，不直接继承目标价。"
        if reports
        else "本窗口PDF研报较少，更多依赖观点流和行情验证。"
    )
    action = "以观察和低吸为主"
    if buildable:
        action = "允许小仓试错，但必须等待触发条件"
    elif watchable:
        action = "没有直接建仓票，重点等待分歧和二次验证"
    else:
        action = "没有足够强的建仓候选，先观察主线强弱"
    return [
        "",
        "## 基金经理摘要",
        f"- **核心判断**：本窗口的主矛盾集中在 `{core_line}`，高置信事件主要来自 {event_desc}。观点源给出的方向有交易价值，但仍需要用基本面承接和量价确认过滤。",
        f"- **可直接建仓候选**：{build_candidates}。若为空，不代表没有机会，而是当前缺少“真增量 + 承接 + 交易点”同时满足的票。",
        f"- **重点观察/等回踩**：{watch_candidates}。这些名字进入观察池的原因不是提及次数，而是观点源逻辑、基本面/技术面验证和边际热度相对更一致。",
        f"- **谨慎处理**：{avoid_candidates}。这类标的可能已经被卖方情绪充分交易，除非出现新催化剂或缩量回踩，否则不宜追。",
        f"- **组合动作**：{action}。优先找“观点源边际变强 + 业绩/订单/价格能验证 + 技术面不过热”的交集。",
        f"- **研报使用方式**：{report_lens}",
        "- **明日需要验证**：主线是否继续放量、龙头是否能承接分歧、观点流中的订单/涨价/排产线索是否能找到公告或行情响应。",
    ]


def _pm_candidate_focus_lines(candidate_rows: list[dict], limit: int = 6) -> list[str]:
    lines = [
        "",
        "## PM观察清单",
        "",
        "| 标的 | 组合处理 | 为什么值得看 | 主要风险/证伪 |",
        "| --- | --- | --- | --- |",
    ]
    for row in candidate_rows[:limit]:
        name = f"{row.get('name')}（{row.get('symbol')}）"
        action = _compact_text(str(row.get("action") or row.get("bucket") or "观察"), 70)
        why_parts = [
            str(row.get("marginal_label") or ""),
            str(row.get("theme_stock_style") or ""),
            str(row.get("expectation_gap") or row.get("signal_interpretation") or row.get("note") or ""),
        ]
        why = _compact_text("；".join(part for part in why_parts if part), 120)
        risk = _compact_text(
            str(row.get("falsification_points") or row.get("risk_flags") or "等待量价和基本面验证"),
            100,
        )
        lines.append(f"| {_md_cell(name)} | {_md_cell(action)} | {_md_cell(why)} | {_md_cell(risk)} |")
    if len(lines) == 4:
        lines.append("| 暂无 | 观察 | 没有形成足够强的交集 | 不强行交易 |")
    return lines


def _row_int(row: dict, key: str, default: int = 0) -> int:
    try:
        return int(row.get(key) or default)
    except Exception:
        return default


def _row_label(row: dict) -> str:
    name = str(row.get("name") or "").strip()
    symbol = str(row.get("symbol") or "").strip()
    if not symbol or symbol == "未评分":
        return name
    if name and name != symbol:
        return f"{name}（{symbol}）"
    return f"未命名标的（{symbol}）"


def _is_low_frequency_candidate(row: dict) -> bool:
    mentions_total = _row_int(row, "mentions_1d") + _row_int(row, "mentions_3d") + _row_int(row, "mentions_prior")
    marginal = str(row.get("marginal_label") or "")
    return mentions_total <= 3 or marginal in {"今日新增", "低频线索"}


def _is_hot_candidate(row: dict) -> bool:
    return (
        _row_int(row, "mentions_3d") + _row_int(row, "mentions_prior") >= 4
        or _row_int(row, "pump") >= 25
        or _row_int(row, "technical", -1) >= 30
    )


def _looks_like_generated_evidence(text: str) -> bool:
    return any(
        marker in text
        for marker in (
            "候选机会资产",
            "热门优选",
            "验证：跟踪",
            "风险：警惕",
            "预处理资产",
        )
    )


def _format_item_evidence(item: KpItem, max_chars: int = 520) -> str:
    title = _clean_report_snippet(item.title, 120)
    body = _clean_report_snippet(item.text or item.summary, max_chars)
    if not body:
        body = _clean_report_snippet(item.summary, max_chars)
    if title and body and title not in body:
        return f"{item.published_at[:16]}｜{title}｜{body}"
    return f"{item.published_at[:16]}｜{body or title}"


def _candidate_raw_snippets(row: dict, limit: int = 2) -> list[str]:
    raw = row.get("raw_evidence")
    primary: list[str] = []
    fallback: list[str] = []
    if isinstance(raw, list):
        for item in raw:
            text = _compact_text(str(item or ""), 520)
            if not text:
                continue
            target = fallback if _looks_like_generated_evidence(text) else primary
            if text not in primary and text not in fallback:
                target.append(text)
            if len(primary) >= limit:
                return primary[:limit]
    note = _compact_text(str(row.get("note") or ""), 280)
    snippets = primary or fallback
    return snippets[:limit] or ([note] if note else [])


def _candidate_column_score(row: dict) -> str:
    scorecard = row.get("scorecard")
    if isinstance(scorecard, dict):
        parts = scorecard.get("components", {})
        if isinstance(parts, dict):
            detail = "；".join(f"{key}{value}" for key, value in parts.items())
        else:
            detail = ""
        return f"交易可行性 {scorecard.get('total', 0)}/100；{detail}"
    return (
        f"综合优先级 {_opportunity_priority(row)}；"
        f"LLM/信号 {_row_int(row, 'llm_score', _row_int(row, 'signal_score'))}，"
        f"主升 {_row_int(row, 'main_rise_score')}，短线 {_row_int(row, 'short_trade_score')}，"
        f"基本面 {row.get('fundamental_text')}，技术 {row.get('technical')}/40。"
    )


def _candidate_trade_type(row: dict) -> str:
    text = " ".join(
        str(row.get(key) or "")
        for key in (
            "signal_interpretation",
            "expectation_gap",
            "thesis_path",
            "note",
            "opportunity_types",
            "raw_evidence",
        )
    )
    if any(word in text for word in ("涨价", "提价", "价格", "业绩", "指引", "毛利", "利润")):
        return "业绩/价格上修"
    if any(word in text for word in ("政策", "定增", "公告", "中标", "客户验证", "认证", "订单")):
        return "事件催化"
    if (
        str(row.get("candidate_lane") or "") == "tech_hot"
        or _is_hot_candidate(row)
        or _candidate_position_bucket(row) in {"高位强趋势", "高位过热"}
    ):
        return "高热趋势延续"
    if str(row.get("candidate_lane") or "") in {"non_tech_alpha", "report_assumption", "low_frequency"} or _candidate_position_bucket(row) == "低位/左侧":
        return "低位拐点反转"
    return "主题扩散"


def _candidate_trade_lane(row: dict) -> str:
    trade_type = str(row.get("trade_type") or _candidate_trade_type(row))
    if trade_type in {"高热趋势延续", "业绩/价格上修", "事件催化"}:
        return "高热/催化验证"
    if trade_type == "低位拐点反转":
        return "低位拐点验证"
    return "主题扩散验证"


def _component_logic(row: dict, max_points: int) -> int:
    score = _row_int(row, "llm_score", _row_int(row, "signal_score"))
    value = int(min(max_points, max_points * max(0, min(score, 100)) / 100))
    if str(row.get("llm_status") or "") != "analyzed":
        value = min(value, int(max_points * 0.55))
    return value


def _component_expectation(row: dict, max_points: int) -> int:
    text = " ".join(str(row.get(key) or "") for key in ("expectation_gap", "signal_interpretation", "note"))
    value = 0
    if text:
        value += int(max_points * 0.35)
    if any(word in text for word in ("预期差", "未充分", "低估", "修复", "拐点", "上修", "超预期")):
        value += int(max_points * 0.35)
    if _row_int(row, "hard_increment_count") > 0:
        value += int(max_points * 0.25)
    if str(row.get("candidate_lane") or "") in {"non_tech_alpha", "low_frequency", "report_assumption"}:
        value += int(max_points * 0.15)
    return min(max_points, value)


def _component_fundamental(row: dict, max_points: int) -> int:
    text = str(row.get("fundamental_text") or "")
    if "验证通过" in text:
        return max_points
    if "部分验证" in text:
        return int(max_points * 0.72)
    if "弱验证" in text:
        return int(max_points * 0.45)
    if "承接不足" in text:
        return int(max_points * 0.18)
    return int(max_points * 0.28) if text and "待验证" not in text else 0


def _component_technical(row: dict, trade_type: str, max_points: int) -> int:
    technical = _row_int(row, "technical", -1)
    if technical < 0:
        return 0
    if trade_type == "低位拐点反转":
        if 12 <= technical <= 26:
            return int(max_points * 0.85)
        if 27 <= technical <= 33:
            return int(max_points * 0.65)
        if technical < 12:
            return int(max_points * 0.35)
        return int(max_points * 0.25)
    if trade_type == "高热趋势延续":
        if 24 <= technical <= 34:
            return max_points
        if 18 <= technical < 24:
            return int(max_points * 0.65)
        if technical > 34:
            return int(max_points * 0.55)
        return int(max_points * 0.25)
    return min(max_points, int(technical * max_points / 40))


def _component_catalyst(row: dict, max_points: int) -> int:
    text = " ".join(str(row.get(key) or "") for key in ("catalyst_clock", "verification_points", "entry_plan", "raw_evidence"))
    value = min(max_points, _row_int(row, "hard_increment_count") * int(max_points * 0.35))
    if text:
        value += int(max_points * 0.35)
    if any(word in text for word in ("1天", "1周", "公告", "订单", "价格", "中报", "季报", "验证", "催化")):
        value += int(max_points * 0.30)
    return min(max_points, value)


def _risk_penalty(row: dict, trade_type: str) -> int:
    penalty = min(20, _row_int(row, "pump") // 2)
    technical = _row_int(row, "technical", -1)
    if technical >= 35:
        penalty += 10 if trade_type != "高热趋势延续" else 6
    if str(row.get("llm_status") or "") != "analyzed":
        penalty += 8
    if str(row.get("fundamental_text") or "").startswith("待验证"):
        penalty += 8
    if any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与")):
        penalty += 18
    if trade_type == "主题扩散":
        penalty += 8
    return min(35, penalty)


def _candidate_trade_hypothesis(row: dict) -> str:
    thesis = str(row.get("thesis_path") or "").strip()
    if thesis:
        return thesis
    signal = str(row.get("signal_interpretation") or row.get("expectation_gap") or "").strip()
    if signal:
        return _compact_text(signal, 220)
    snippets = _candidate_raw_snippets(row, limit=1)
    if snippets:
        return _compact_text(snippets[0], 220)
    return "未能从观点源抽出清晰交易假设"


def _candidate_scorecard(row: dict) -> dict:
    trade_type = _candidate_trade_type(row)
    if trade_type == "高热趋势延续":
        weights = {"逻辑": 15, "预期差": 15, "基本面": 15, "技术": 25, "催化": 10}
    elif trade_type == "低位拐点反转":
        weights = {"逻辑": 20, "预期差": 25, "基本面": 25, "技术": 10, "催化": 10}
    elif trade_type == "业绩/价格上修":
        weights = {"逻辑": 15, "预期差": 20, "基本面": 25, "技术": 15, "催化": 15}
    elif trade_type == "事件催化":
        weights = {"逻辑": 20, "预期差": 15, "基本面": 15, "技术": 15, "催化": 25}
    else:
        weights = {"逻辑": 15, "预期差": 15, "基本面": 15, "技术": 10, "催化": 10}
    components = {
        "逻辑": _component_logic(row, weights["逻辑"]),
        "预期差": _component_expectation(row, weights["预期差"]),
        "基本面": _component_fundamental(row, weights["基本面"]),
        "技术": _component_technical(row, trade_type, weights["技术"]),
        "催化": _component_catalyst(row, weights["催化"]),
    }
    penalty = _risk_penalty(row, trade_type)
    total = max(0, min(100, sum(components.values()) - penalty))
    hard_reject_reasons = _candidate_hard_gate_failures(row)
    if "基本面承接不足" in hard_reject_reasons and trade_type in {"事件催化", "主题扩散"}:
        hard_reject_reasons = [reason for reason in hard_reject_reasons if reason != "基本面承接不足"]
    return {
        "trade_type": trade_type,
        "components": components,
        "risk_penalty": penalty,
        "total": total,
        "hard_reject": bool(hard_reject_reasons),
        "hard_reject_reasons": hard_reject_reasons,
    }


def _candidate_column_lines(row: dict, idx: int, board_title: str) -> list[str]:
    scorecard = row.get("scorecard") if isinstance(row.get("scorecard"), dict) else {}
    lane_title = str(scorecard.get("trade_type") or row.get("trade_type") or _candidate_trade_type(row))
    snippets = _candidate_raw_snippets(row, limit=2)
    raw_lines = [f"> {snippet}" for snippet in snippets] or ["> 暂无可展示原始段子，需回看知识星球原文。"]
    hot_or_low_question = (
        "高热票先判断上行空间、拥挤度和回踩买点，不能只看逻辑正确。"
        if lane_title in {"高热趋势延续", "业绩/价格上修", "事件催化"}
        else "低位票先判断拐点是否真实、市场为何没定价，以及赔率能否覆盖等待成本。"
    )
    if lane_title in {"高热趋势延续", "业绩/价格上修", "事件催化"}:
        key_question = _compact_text(
            str(row.get("payoff_risk") or row.get("expectation_gap") or "重点判断高位是否仍有预期差、空间和量价承接。"),
            220,
        )
    else:
        key_question = _compact_text(
            str(row.get("expectation_gap") or row.get("signal_interpretation") or "重点判断卖方/私域线索能否落到未来1-4周可验证的业绩或价格拐点。"),
            220,
        )
    thesis = _compact_text(_candidate_trade_hypothesis(row), 220)
    verification = _compact_text(str(row.get("verification_points") or row.get("entry_plan") or "等待公告、财报、价格和量价确认。"), 220)
    risk = _compact_text(str(row.get("falsification_points") or row.get("risk_flags") or "若后续没有硬数据验证，则降级。"), 220)
    score_reasons = ""
    if scorecard:
        components = scorecard.get("components", {})
        component_text = "；".join(f"{key}{value}" for key, value in components.items()) if isinstance(components, dict) else ""
        reject = "；硬淘汰风险：" + "、".join(scorecard.get("hard_reject_reasons", [])) if scorecard.get("hard_reject_reasons") else ""
        score_reasons = f"{component_text}；风险扣分{scorecard.get('risk_penalty', 0)}{reject}"
    return [
        "",
        "---",
        "",
        f"### {idx}. {_md_cell(_row_label(row))}｜{board_title}｜{lane_title}｜{row.get('position_bucket') or _candidate_position_bucket(row)}｜{row.get('buildability_label') or _candidate_buildability_label(row)}",
        "",
        f"**最终结论**：{_candidate_clear_conclusion(row)}",
        "",
        f"**排序得分**：{_candidate_column_score(row)}",
        "",
        f"**漏斗评分解释**：{score_reasons or '暂无结构化评分解释'}",
        "",
        "**参考段子**：",
        *raw_lines,
        "",
        f"**1. 卖方观点识别**：{_compact_text(str(row.get('signal_interpretation') or row.get('note') or '卖方观点尚未被充分抽取'), 220)}",
        "",
        f"**2. 交易假设**：{thesis}",
        "",
        f"**3. 类型判断**：{lane_title}。{hot_or_low_question}",
        "",
        f"**4. 预期差/空间判断**：{key_question}",
        "",
        f"**5. 基本面与技术面验证**：{row.get('fundamental_text')}；技术 {row.get('technical')}/40；位置判断为 {row.get('position_bucket') or _candidate_position_bucket(row)}。"
        f" {verification}",
        "",
        f"**6. 交易处理**：{_compact_text(str(row.get('action') or row.get('bucket') or '观察'), 220)}",
        "",
        f"**7. 证伪/风险**：{risk}",
    ]


def _candidate_board_rows(
    candidate_rows: list[dict],
    *,
    main_size: int = DAILY_MAIN_BOARD_SIZE,
    watch_size: int = DAILY_WATCH_BOARD_SIZE,
) -> tuple[list[dict], list[dict]]:
    sorted_rows = sorted(candidate_rows, key=_opportunity_priority, reverse=True)

    def main_threshold(row: dict) -> int:
        return DAILY_MAIN_MIN_SCORE if row.get("llm_required") or row.get("market_scores_required") else 20

    def watch_threshold(row: dict) -> int:
        return DAILY_WATCH_MIN_SCORE if row.get("llm_required") or row.get("market_scores_required") else 10

    main_rows = [
        row
        for row in sorted_rows
        if not _candidate_hard_gate_failures(row)
        and _opportunity_priority(row) >= main_threshold(row)
    ]
    watch_rows = [
        row
        for row in sorted_rows
        if row not in main_rows
        and (not row.get("llm_required") or str(row.get("llm_status") or "") == "analyzed")
        and not any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与"))
        and _opportunity_priority(row) >= watch_threshold(row)
    ]
    return main_rows[:main_size], watch_rows[:watch_size]


def _candidate_pending_analysis_rows(candidate_rows: list[dict], limit: int = 8) -> list[dict]:
    pending = [
        row
        for row in candidate_rows
        if row.get("llm_required") and str(row.get("llm_status") or "") != "analyzed"
    ]
    return sorted(pending, key=lambda row: (int(row.get("signal_score") or 0), int(row.get("mentions_1d") or 0)), reverse=True)[:limit]


def _board_summary_lines(rows: list[dict]) -> list[str]:
    lines = [
        "| 排名 | 标的 | 类型 | 交易可行性 | 位置 | 动作 |",
        "| ---: | --- | --- | ---: | --- | --- |",
    ]
    for idx, row in enumerate(rows, start=1):
        lines.append(
            f"| {idx} | {_md_cell(_row_label(row))} | {_md_cell(_candidate_trade_lane(row))} | "
            f"{_opportunity_priority(row)} | {_md_cell(row.get('position_bucket') or _candidate_position_bucket(row))} | "
            f"{_md_cell(_candidate_clear_conclusion(row))} |"
        )
    return lines


def _board_section_lines(title: str, rows: list[dict]) -> list[str]:
    lines = ["", f"#### {title}"]
    if not rows:
        lines.append("- 暂无合格标的。")
        return lines
    lines.extend(_board_summary_lines(rows))
    return lines


def _board_candidate_lines(candidate_rows: list[dict]) -> list[str]:
    main_rows, watch_rows = _candidate_board_rows(candidate_rows)
    pending_rows = _candidate_pending_analysis_rows(candidate_rows)
    main_hot = [row for row in main_rows if _candidate_trade_lane(row) == "高热/催化验证"]
    main_low = [row for row in main_rows if _candidate_trade_lane(row) == "低位拐点验证"]
    main_other = [row for row in main_rows if row not in main_hot and row not in main_low]
    lines = [
        "",
        "## 今日主榜与观察榜",
        "",
        f"主榜容量 {DAILY_MAIN_BOARD_SIZE} 个，观察榜容量 {DAILY_WATCH_BOARD_SIZE} 个；宁缺毋滥，不因格式固定而强行填满。排序目标是交易可行性，不是信息热度。",
        f"今日合格：主榜 {len(main_rows)}/{DAILY_MAIN_BOARD_SIZE}，观察榜 {len(watch_rows)}/{DAILY_WATCH_BOARD_SIZE}，待补分析 {len(pending_rows)} 个。",
        "",
        "### 主榜 10",
        ]
    lines.extend(_board_section_lines("高热/催化验证", main_hot))
    lines.extend(_board_section_lines("低位拐点验证", main_low))
    if main_other:
        lines.extend(_board_section_lines("主题扩散验证", main_other))
    if main_rows:
        for idx, row in enumerate(main_rows, start=1):
            lines.extend(_candidate_column_lines(row, idx, "主榜"))
    else:
        lines.append("- 今日没有主榜候选。")
    lines.extend(
        [
            "",
            "### 观察榜 5",
        ]
    )
    lines.extend(_board_summary_lines(watch_rows))
    if watch_rows:
        for idx, row in enumerate(watch_rows, start=1):
            lines.extend(_candidate_column_lines(row, idx, "观察榜"))
    else:
        lines.append("- 今日没有观察榜候选。")
    if pending_rows:
        lines.extend(
            [
                "",
                "### 待补分析池",
                "",
                "以下候选未完成 LLM 深度拆解，暂不进入主榜/观察榜；优先排查网络、返回截断或 JSON 解析问题后重跑。",
                "",
                "| 标的 | 信号分 | 失败/缺口 | 原始线索 |",
                "| --- | ---: | --- | --- |",
            ]
        )
        for row in pending_rows:
            snippets = _candidate_raw_snippets(row, limit=1)
            lines.append(
                f"| {_md_cell(_row_label(row))} | {_row_int(row, 'signal_score')} | "
                f"{_md_cell(_candidate_clear_conclusion(row))} | {_md_cell(snippets[0] if snippets else '')} |"
            )
    return lines


def _is_fully_analyzed_candidate(row: dict) -> bool:
    """Top opportunities should not bypass the analyst stack."""
    if str(row.get("llm_status") or "") != "analyzed":
        return False
    if str(row.get("technical") or "NA") == "NA":
        return False
    if str(row.get("fundamental_text") or "").startswith("待验证"):
        return False
    return True


def _opportunity_priority(row: dict) -> int:
    if row.get("tradability_score") is not None:
        return _row_int(row, "tradability_score")
    llm_score = _row_int(row, "llm_score", _row_int(row, "signal_score"))
    main_score = _row_int(row, "main_rise_score")
    trade_score = _row_int(row, "short_trade_score")
    pump = _row_int(row, "pump")
    technical = _row_int(row, "technical", 0)
    increment_bonus = min(18, _row_int(row, "hard_increment_count") * 9)
    low_freq_bonus = 10 if _is_low_frequency_candidate(row) else 0
    lane = str(row.get("candidate_lane") or "")
    lane_bonus = 0
    if lane == "non_tech_alpha":
        lane_bonus = 12
    elif lane == "report_assumption":
        lane_bonus = 8
    elif lane == "low_frequency":
        lane_bonus = 8
    overheat_penalty = 12 if technical >= 35 else 0
    tech_hot_penalty = 0
    if lane == "tech_hot" and _row_int(row, "hard_increment_count") == 0:
        tech_hot_penalty += 10
    if lane == "tech_hot" and pump >= 28:
        tech_hot_penalty += 8
    no_increment_penalty = 8 if _row_int(row, "hard_increment_count") == 0 and llm_score < 75 else 0
    analysis_gap_penalty = 0
    if str(row.get("llm_status") or "") != "analyzed":
        analysis_gap_penalty += 10
    if str(row.get("technical") or "NA") == "NA":
        analysis_gap_penalty += 16
    if str(row.get("fundamental_text") or "").startswith("待验证"):
        analysis_gap_penalty += 12
    avoid_penalty = 25 if any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与")) else 0
    return int(
        llm_score * 0.35
        + main_score * 0.35
        + trade_score * 0.2
        + increment_bonus
        + low_freq_bonus
        + lane_bonus
        - pump * 0.35
        - overheat_penalty
        - tech_hot_penalty
        - no_increment_penalty
        - analysis_gap_penalty
        - avoid_penalty
    )


def _normalized_symbol_tokens(value: str) -> set[str]:
    text = str(value or "").strip().upper()
    if not text or text == "未评分":
        return set()
    tokens = {text}
    match = re.search(r"\b(\d{6})(?:\.(?:SH|SZ|BJ))?\b", text)
    if match:
        tokens.add(match.group(1))
    return tokens


def _candidate_match_tokens(row: dict) -> set[str]:
    tokens: set[str] = set()
    for value in (row.get("name"), row.get("symbol")):
        text = str(value or "").strip()
        if text and text != "未评分":
            tokens.add(text)
            tokens.update(_normalized_symbol_tokens(text))
    for alias in re.split(r"\s*/\s*", str(row.get("aliases") or "")):
        alias = alias.strip()
        if alias:
            tokens.add(alias)
            tokens.update(_normalized_symbol_tokens(alias))
    return {token for token in tokens if token}


def _event_text(event: KpEventSignal) -> str:
    return " ".join(
        [
            event.title,
            event.interpretation,
            " ".join(event.tickers),
            " ".join(event.companies),
            " ".join(event.themes),
        ]
    )


def _event_is_trade_increment(event: KpEventSignal) -> bool:
    if event.event_type not in {"订单/排产", "涨价/价格弹性", "库存/供需", "客户验证/导入", "业绩/指引", "政策/监管"}:
        return False
    if "低" in event.confidence and event.source_type not in INFORMATION_RICH_TYPES:
        return False
    return True


def _candidate_event_links(row: dict, event_signals: list[KpEventSignal], limit: int = 3) -> list[KpEventSignal]:
    tokens = _candidate_match_tokens(row)
    if not tokens:
        return []
    linked: list[KpEventSignal] = []
    for event in event_signals:
        text = _event_text(event)
        event_tokens = set(event.tickers) | set(event.companies)
        for ticker in event.tickers:
            event_tokens.update(_normalized_symbol_tokens(ticker))
        direct_match = bool(tokens & event_tokens) or any(token and token in text for token in tokens)
        if direct_match:
            linked.append(event)
    return sorted(
        linked,
        key=lambda event: (
            1 if _event_is_trade_increment(event) else 0,
            1 if event.source_type in INFORMATION_RICH_TYPES else 0,
            event.published_at,
        ),
        reverse=True,
    )[:limit]


def _mapped_candidates_for_event(event: KpEventSignal, candidate_rows: list[dict], limit: int = 4) -> list[dict]:
    event_text = _event_text(event)
    event_tokens = set(event.tickers) | set(event.companies)
    for ticker in event.tickers:
        event_tokens.update(_normalized_symbol_tokens(ticker))
    rows: list[dict] = []
    for row in candidate_rows:
        tokens = _candidate_match_tokens(row)
        if bool(tokens & event_tokens) or any(token and token in event_text for token in tokens):
            rows.append(row)
    return sorted(rows, key=_opportunity_priority, reverse=True)[:limit]


def _mapped_candidates_for_review(review: EventLLMReview, candidate_rows: list[dict], limit: int = 4) -> list[dict]:
    text = " ".join([review.beneficiaries, review.summary, review.impact_path])
    rows = []
    for row in candidate_rows:
        if any(token and token in text for token in _candidate_match_tokens(row)):
            rows.append(row)
    return sorted(rows, key=_opportunity_priority, reverse=True)[:limit]


def _candidate_position_bucket(row: dict) -> str:
    technical = _row_int(row, "technical", -1)
    if technical < 0:
        return "未评分位置"
    if technical >= 35:
        return "高位过热"
    if technical >= 29:
        return "高位强趋势"
    if technical >= 18:
        return "中位确认"
    return "低位/左侧"


def _candidate_buildability_label(row: dict) -> str:
    action = str(row.get("action") or "")
    fundamental_text = str(row.get("fundamental_text") or "")
    market_required = bool(row.get("market_scores_required"))
    position = _candidate_position_bucket(row)
    priority = _opportunity_priority(row)
    hard_increment_count = _row_int(row, "hard_increment_count")
    llm_required = bool(row.get("llm_required"))
    if llm_required and str(row.get("llm_status") or "") == "failed":
        return "待补分析：LLM短证据重试仍失败"
    if llm_required and str(row.get("llm_status") or "") == "not_run":
        return "待补分析：未进入LLM深度拆解"
    if any(word in action for word in ("回避", "放弃", "不参与")):
        return "不建仓：动作层已回避"
    if market_required and ("待验证" in fundamental_text or str(row.get("technical")) == "NA"):
        return "不可建仓：基本面/技术面未闭环"
    if hard_increment_count == 0:
        return "观察：缺少可映射真增量"
    if position == "高位过热":
        return "只等回踩：逻辑可跟但位置透支"
    if priority >= 70 and "承接不足" not in fundamental_text:
        return "建仓候选：小仓试错/触发后加"
    if priority >= 50:
        return "研究候选：等验证或买点"
    return "观察：赔率或胜率不足"


def _candidate_hard_gate_failures(row: dict) -> list[str]:
    failures: list[str] = []
    llm_required = bool(row.get("llm_required"))
    if llm_required and str(row.get("llm_status") or "") != "analyzed":
        failures.append("LLM未完成深度拆解")
    if _candidate_trade_hypothesis(row) == "未能从观点源抽出清晰交易假设":
        failures.append("缺少清晰交易假设")
    market_required = bool(row.get("market_scores_required"))
    if market_required and "承接不足" in str(row.get("fundamental_text") or ""):
        failures.append("基本面承接不足")
    if market_required and str(row.get("technical") or "NA") == "NA":
        failures.append("缺少技术面评分")
    if _row_int(row, "technical", -1) >= 35 and _row_int(row, "hard_increment_count") == 0:
        failures.append("高位且缺少新增变量")
    if any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与")):
        failures.append("动作层已回避")
    return failures


def _candidate_clear_conclusion(row: dict) -> str:
    failures = _candidate_hard_gate_failures(row)
    if failures:
        return f"{_candidate_buildability_label(row)}：{'、'.join(failures[:2])}"
    action = str(row.get("action") or "").strip()
    if action:
        return _compact_text(action, 110)
    return _candidate_buildability_label(row)


def _candidate_score_breakdown(row: dict) -> str:
    scorecard = row.get("scorecard")
    if isinstance(scorecard, dict):
        components = scorecard.get("components", {})
        component_text = " + ".join(f"{key}{value}" for key, value in components.items()) if isinstance(components, dict) else ""
        return (
            f"交易可行性 {scorecard.get('total', 0)} = {component_text} "
            f"- 风险扣分{scorecard.get('risk_penalty', 0)}"
        )
    increment = f"真增量+{min(18, _row_int(row, 'hard_increment_count') * 9)}"
    llm_score = _row_int(row, "llm_score", _row_int(row, "signal_score"))
    main_score = _row_int(row, "main_rise_score")
    trade_score = _row_int(row, "short_trade_score")
    low_freq = "+10低频" if _is_low_frequency_candidate(row) else "0"
    lane = str(row.get("candidate_lane") or "")
    if lane == "non_tech_alpha":
        lane_text = "+12非科技低频"
    elif lane == "report_assumption":
        lane_text = "+8研报假设"
    elif lane == "low_frequency":
        lane_text = "+8低频来源"
    else:
        lane_text = "0"
    pump = f"-{int(_row_int(row, 'pump') * 0.35)}拥挤"
    overheat = "-12高位" if _row_int(row, "technical", 0) >= 35 else "0"
    tech_hot_penalty = 0
    if lane == "tech_hot" and _row_int(row, "hard_increment_count") == 0:
        tech_hot_penalty += 10
    if lane == "tech_hot" and _row_int(row, "pump") >= 28:
        tech_hot_penalty += 8
    tech_hot_text = f"-{tech_hot_penalty}科技拥挤" if tech_hot_penalty else "0"
    no_increment = "-8缺增量" if _row_int(row, "hard_increment_count") == 0 and llm_score < 75 else "0"
    analysis_gap = 0
    if str(row.get("llm_status") or "") != "analyzed":
        analysis_gap += 10
    if str(row.get("technical") or "NA") == "NA":
        analysis_gap += 16
    if str(row.get("fundamental_text") or "").startswith("待验证"):
        analysis_gap += 12
    analysis_gap_text = f"-{analysis_gap}分析缺口" if analysis_gap else "0"
    return (
        f"优先级 {_opportunity_priority(row)} = "
        f"LLM/信号{int(llm_score * 0.35)} + 主升{int(main_score * 0.35)} + 短线{int(trade_score * 0.2)} "
        f"+ {increment} + {low_freq} + {lane_text} {pump} {overheat} {tech_hot_text} {no_increment} {analysis_gap_text}"
    )


def _candidate_track(row: dict) -> str:
    if _is_low_frequency_candidate(row):
        return "低频预期差/边际改善"
    if _is_hot_candidate(row):
        return "热门主线优中选优"
    return "常规观察"


def _top_opportunity_rows(candidate_rows: list[dict], limit: int = 5) -> list[dict]:
    has_analyzed = any(_is_fully_analyzed_candidate(row) for row in candidate_rows)
    eligible = [
        row
        for row in candidate_rows
        if _opportunity_priority(row) >= 35
        and (not has_analyzed or _is_fully_analyzed_candidate(row))
        and not any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与"))
    ]
    rows = sorted(eligible, key=_opportunity_priority, reverse=True)
    if rows:
        return rows[:limit]
    return sorted(candidate_rows, key=_opportunity_priority, reverse=True)[:limit]


def _avoid_rows(candidate_rows: list[dict], limit: int = 5) -> list[dict]:
    rows = [
        row
        for row in candidate_rows
        if _row_int(row, "pump") >= 28
        or _row_int(row, "technical", -1) >= 34
        or any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与"))
        or "承接不足" in str(row.get("fundamental_text") or "")
    ]
    return sorted(
        rows,
        key=lambda row: (_row_int(row, "pump"), _row_int(row, "technical", 0), -_opportunity_priority(row)),
        reverse=True,
    )[:limit]


def _low_frequency_rows(candidate_rows: list[dict], limit: int = 5) -> list[dict]:
    rows = [
        row
        for row in candidate_rows
        if _is_low_frequency_candidate(row)
        and not any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与"))
    ]
    return sorted(rows, key=_opportunity_priority, reverse=True)[:limit]


def _true_increment_reviews(event_reviews: list[EventLLMReview], limit: int = 5) -> list[EventLLMReview]:
    priority = {"真增量": 4, "半增量": 2, "情绪重复": 0, "噪音": -2}
    evidence = {"高": 3, "中": 2, "低": 0}
    rows = [review for review in event_reviews if review.status == "analyzed"]
    return sorted(
        rows,
        key=lambda review: (
            priority.get(review.increment_level, 1),
            evidence.get(review.evidence_grade, 1),
            1 if review.verification else 0,
        ),
        reverse=True,
    )[:limit]


def _low_frequency_labels(
    candidate_rows: list[dict],
    preprocessed_snapshot: dict[str, list[sqlite3.Row]] | None = None,
    limit: int = 3,
) -> list[str]:
    labels = [str(row.get("name")) for row in _low_frequency_rows(candidate_rows, limit=limit)]
    if len(labels) >= limit or not preprocessed_snapshot:
        return labels[:limit]
    seen = set(labels)
    for row in preprocessed_snapshot.get("opportunities", []):
        opportunity_type = str(row["opportunity_type"] or "")
        score = int(row["priority_score"] or 0)
        if "研报" not in opportunity_type and score >= 80:
            continue
        label = str(row["symbol_or_name"] or "").strip()
        if label and label not in seen:
            labels.append(label)
            seen.add(label)
        if len(labels) >= limit:
            return labels[:limit]
    for row in preprocessed_snapshot.get("assumptions", []):
        names = [*_json_values(row["linked_tickers_json"]), *_json_values(row["linked_companies_json"])]
        label = " / ".join(names[:2]) if names else _compact_text(str(row["title"] or ""), 20)
        if label and label not in seen:
            labels.append(label)
            seen.add(label)
        if len(labels) >= limit:
            break
    return labels[:limit]


def _pm_one_page_lines(
    pm_control: PmControlAnalysis,
    candidate_rows: list[dict],
    event_reviews: list[EventLLMReview],
    preprocessed_snapshot: dict[str, list[sqlite3.Row]] | None = None,
) -> list[str]:
    opportunities = _top_opportunity_rows(candidate_rows, limit=3)
    avoid = _avoid_rows(candidate_rows, limit=3)
    low_freq = _low_frequency_labels(candidate_rows, preprocessed_snapshot, limit=3)
    true_events = [
        review
        for review in event_reviews
        if review.status == "analyzed" and review.increment_level == "真增量"
    ]
    action = _compact_text(pm_control.portfolio_action or "没有明确动作，保持观察。", 300)
    trigger_conditions = _compact_text(
        pm_control.trigger_conditions or "跟踪订单、价格、库存、排产、客户验证和量价承接。",
        300,
    )
    return [
        "",
        "## PM总控层：最终取舍",
        "",
        f"- **今日姿态**：{pm_control.market_posture or '暂无明确市场姿态'}",
        f"- **能否出手**：{action}",
        f"- **最值得盯的机会**：{'、'.join(str(row.get('name')) for row in opportunities) or '暂无'}",
        f"- **高热但要警惕**：{'、'.join(str(row.get('name')) for row in avoid) or '暂无'}",
        f"- **低频预期差**：{'、'.join(low_freq) or '本窗口暂未筛出'}",
        f"- **真实增量密度**：LLM审稿真增量 {len(true_events)} 条；若真增量不足，宁可少做，不用热度替代逻辑。",
        f"- **明日验证**：{trigger_conditions}",
    ]


def _true_increment_event_lines(
    event_reviews: list[EventLLMReview],
    event_signals: list[KpEventSignal],
    limit: int = 5,
) -> list[str]:
    lines = [
        "",
        "## 今日真实增量事件 Top 5",
        "",
        "| 排名 | 增量属性 | 证据 | 事件/影响路径 | 受益映射 | 验证指标 | 风险 |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    reviews = _true_increment_reviews(event_reviews, limit=limit)
    if reviews:
        for idx, review in enumerate(reviews, start=1):
            lines.append(
                f"| {idx} | {_md_cell(review.increment_level)} | {_md_cell(review.evidence_grade)} | "
                f"{_md_cell(review.summary or review.impact_path)} | {_md_cell(review.beneficiaries)} | "
                f"{_md_cell(review.verification)} | {_md_cell(review.risk)} |"
            )
        return lines
    rows = _event_quality_rows(event_signals, max_rows=limit)
    if not rows:
        lines.append("| 1 | 暂无 | 低 | 本窗口没有足够明确的新订单、涨价、库存、客户验证或政策变化 | NA | 等待新信息 | 噪音偏多 |")
        return lines
    for idx, (_date, event_type, increment, interpretation, verification) in enumerate(rows, start=1):
        lines.append(
            f"| {idx} | {_md_cell(increment)} | 规则初筛 | {_md_cell(event_type + '：' + interpretation)} | 待映射 | {_md_cell(verification)} | 待LLM审稿 |"
        )
    return lines


def _increment_to_opportunity_lines(
    event_reviews: list[EventLLMReview],
    event_signals: list[KpEventSignal],
    candidate_rows: list[dict],
    limit: int = 6,
) -> list[str]:
    lines = [
        "",
        "## 今日真增量到交易映射",
        "",
        "| 增量是什么 | 来源/证据 | 映射标的 | 交易含义 | 必须验证 |",
        "| --- | --- | --- | --- | --- |",
    ]
    used = 0
    source_events = _events_for_llm_review(event_signals, max_events=max(limit, len(event_reviews), 14))
    review_source_pairs: list[tuple[EventLLMReview, KpEventSignal | None]] = []
    for idx, review in enumerate(event_reviews):
        source_event = source_events[idx] if idx < len(source_events) else None
        review_source_pairs.append((review, source_event))
    review_source_pairs.sort(
        key=lambda pair: (
            {"真增量": 4, "半增量": 2, "情绪重复": 0, "噪音": -2}.get(pair[0].increment_level, 1),
            {"高": 3, "中": 2, "低": 0}.get(pair[0].evidence_grade, 1),
            1 if pair[1] and _event_is_trade_increment(pair[1]) else 0,
        ),
        reverse=True,
    )
    for review, source_event in review_source_pairs:
        if review.status != "analyzed":
            continue
        if used >= limit:
            break
        mapped = _mapped_candidates_for_review(review, candidate_rows, limit=3)
        if not mapped and source_event is not None:
            mapped = _mapped_candidates_for_event(source_event, candidate_rows, limit=3)
        mapped_text = " / ".join(_row_label(row) for row in mapped) or "未映射到候选"
        implication = (
            "可进入机会卡片复核"
            if mapped
            else "只作为行业背景，不单独触发交易"
        )
        source_text = review.increment_level + "/" + review.evidence_grade
        if source_event is not None:
            source_text += f"；{source_event.source_type}/{source_event.confidence}"
        lines.append(
            f"| {_md_cell(_compact_text(review.summary or review.impact_path, 140))} | "
            f"{_md_cell(source_text)} | "
            f"{_md_cell(mapped_text)} | {_md_cell(implication)} | {_md_cell(_compact_text(review.verification, 120))} |"
        )
        used += 1
    if used < limit:
        for event in sorted(event_signals, key=lambda item: (1 if _event_is_trade_increment(item) else 0, item.published_at), reverse=True):
            if not _event_is_trade_increment(event):
                continue
            mapped = _mapped_candidates_for_event(event, candidate_rows, limit=3)
            mapped_text = " / ".join(_row_label(row) for row in mapped) or "未映射到候选"
            implication = (
                "映射到候选，进入评分拆解"
                if mapped
                else "没有对应A股候选，不作为交易依据"
            )
            lines.append(
                f"| {_md_cell(_compact_text(event.interpretation, 140))} | "
                f"{_md_cell(event.source_type + '/' + event.confidence)} | "
                f"{_md_cell(mapped_text)} | {_md_cell(implication)} | {_md_cell(event.verification)} |"
            )
            used += 1
            if used >= limit:
                break
    if used == 0:
        lines.append("| 暂无 | 本窗口没有足够明确的订单、价格、库存、客户验证、政策或业绩变化 | 未映射 | 不把热度当成交易信号 | 等新增硬信息 |")
    return lines


def _opportunity_card_lines(candidate_rows: list[dict], limit: int = 5) -> list[str]:
    lines = [
        "",
        "## 建仓价值候选 Top 5",
        "",
    ]
    rows = _top_opportunity_rows(candidate_rows, limit=limit)
    if not rows:
        lines.append("- 暂无合格建仓候选。今天更适合观察，不要为了生成报告而硬凑交易。")
        return lines
    for idx, row in enumerate(rows, start=1):
        linked_events = row.get("linked_events") or []
        if isinstance(linked_events, list) and linked_events:
            event_text = "；".join(_compact_text(event.interpretation, 90) for event in linked_events[:2])
        else:
            event_text = "未映射到硬增量，不能只凭热度交易"
        lines.extend(
            [
                f"### {idx}. {_md_cell(_row_label(row))}｜{_candidate_position_bucket(row)}｜{row.get('buildability_label') or _candidate_buildability_label(row)}",
                f"- **真增量映射**：{_compact_text(event_text, 220)}",
                f"- **预期差**：{_compact_text(str(row.get('expectation_gap') or '等待进一步验证预期差'), 180)}",
                f"- **传导链/公司承接**：{_compact_text(str(row.get('thesis_path') or row.get('company_relevance') or row.get('fundamental_text') or '承接待验证'), 180)}",
                f"- **数据与技术验证**：{_md_cell(row.get('fundamental_text'))}；技术 {row.get('technical')}/40；主升 {row.get('main_rise_score')}，短线 {row.get('short_trade_score')}。",
                f"- **评分拆解**：{_candidate_score_breakdown(row)}。",
                f"- **交易动作**：{_compact_text(str(row.get('action') or row.get('bucket') or '观察'), 180)}",
                f"- **证伪/风险**：{_compact_text(str(row.get('falsification_points') or row.get('risk_flags') or '若后续没有订单/价格/业绩/量价验证，则降级'), 180)}",
            ]
        )
    return lines


def _position_opportunity_lines(candidate_rows: list[dict], limit: int = 8) -> list[str]:
    lines = [
        "",
        "## 高位与低位挖掘",
        "",
        "| 分组 | 标的 | 建仓价值 | 评分拆解 | 触发条件 |",
        "| --- | --- | --- | --- | --- |",
    ]
    rows = sorted(candidate_rows, key=_opportunity_priority, reverse=True)
    selected: list[dict] = []
    for group in ("低位/左侧", "中位确认", "高位强趋势", "高位过热"):
        group_rows = [row for row in rows if _candidate_position_bucket(row) == group]
        for row in group_rows[:2]:
            selected.append(row)
            if len(selected) >= limit:
                break
        if len(selected) >= limit:
            break
    if not selected:
        lines.append("| 暂无 | 暂无 | 未形成可分组候选 | NA | 等待基本面/技术面评分 |")
        return lines
    seen: set[str] = set()
    for row in selected:
        label = _row_label(row)
        if label in seen:
            continue
        seen.add(label)
        trigger = _compact_text(str(row.get("entry_plan") or row.get("verification_points") or row.get("action") or "等待量价和基本面验证"), 130)
        lines.append(
            f"| {_md_cell(_candidate_position_bucket(row))} | {_md_cell(label)} | "
            f"{_md_cell(row.get('buildability_label') or _candidate_buildability_label(row))} | "
            f"{_md_cell(_candidate_score_breakdown(row))} | {_md_cell(trigger)} |"
        )
    return lines


def _non_tech_alpha_queue_lines(candidate_rows: list[dict], limit: int = 8) -> list[str]:
    lines = [
        "",
        "## 非科技/低频研究队列",
        "",
        "| 标的 | 来源类型 | 建仓价值 | 目前看到的差异化线索 | 下一步验证 |",
        "| --- | --- | --- | --- | --- |",
    ]
    rows = [
        row
        for row in candidate_rows
        if str(row.get("candidate_lane") or "") in {"non_tech_alpha", "report_assumption", "low_frequency", "balanced"}
        and str(row.get("candidate_lane") or "") != "tech_hot"
    ]
    rows = sorted(rows, key=_opportunity_priority, reverse=True)[:limit]
    if not rows:
        lines.append("| 暂无 | NA | 未筛出 | 当前样本仍被科技热门主线占据 | 需要扩展研报假设抽取和非科技关键词映射 |")
        return lines
    for row in rows:
        signal = _compact_text(
            str(row.get("expectation_gap") or row.get("signal_interpretation") or row.get("note") or ""),
            150,
        )
        verify = _compact_text(str(row.get("verification_points") or row.get("entry_plan") or "回到公告、财报、价格和量价验证"), 130)
        source = str(row.get("opportunity_types") or row.get("source_labels") or row.get("candidate_lane") or "")
        lines.append(
            f"| {_md_cell(_row_label(row))} | {_md_cell(source)} | "
            f"{_md_cell(row.get('buildability_label') or _candidate_buildability_label(row))} | "
            f"{_md_cell(signal or '尚无足够差异化观点')} | {_md_cell(verify)} |"
        )
    return lines


def _watch_and_avoid_lines(candidate_rows: list[dict], limit: int = 8) -> list[str]:
    lines = [
        "",
        "## 待验证与回避清单",
        "",
        "| 标的 | 当前处理 | 原因 | 下一步 |",
        "| --- | --- | --- | --- |",
    ]
    rows = [
        row
        for row in candidate_rows
        if "不可建仓" in str(row.get("buildability_label") or "")
        or "观察" in str(row.get("buildability_label") or "")
        or any(word in str(row.get("action") or "") for word in ("回避", "放弃", "不参与"))
        or _row_int(row, "pump") >= 28
    ]
    rows = sorted(rows, key=lambda row: (_row_int(row, "pump"), -_opportunity_priority(row)), reverse=True)[:limit]
    if not rows:
        lines.append("| 暂无 | NA | 没有明显待验证/回避样本 | 继续按机会卡片复盘 |")
        return lines
    for row in rows:
        reason = _compact_text(
            str(row.get("risk_flags") or row.get("falsification_points") or row.get("fundamental_text") or row.get("crowding_label") or ""),
            130,
        )
        next_step = _compact_text(str(row.get("verification_points") or row.get("entry_plan") or "等待新硬信息和量价确认"), 120)
        lines.append(
            f"| {_md_cell(_row_label(row))} | {_md_cell(row.get('buildability_label') or _candidate_buildability_label(row))} | "
            f"{_md_cell(reason)} | {_md_cell(next_step)} |"
        )
    return lines


def _hot_avoid_lines(candidate_rows: list[dict], limit: int = 5) -> list[str]:
    lines = [
        "",
        "## 高热但应回避的票",
        "",
        "| 标的 | 回避原因 | 拥挤/位置 | 证伪或等待条件 |",
        "| --- | --- | --- | --- |",
    ]
    rows = _avoid_rows(candidate_rows, limit=limit)
    if not rows:
        lines.append("| 暂无 | 暂未识别出明显高热低赔率标的 | NA | 继续观察 |")
        return lines
    for row in rows:
        reason = _compact_text(str(row.get("risk_flags") or row.get("action") or row.get("crowding_label") or ""), 130)
        crowding = f"{_candidate_crowding_label(row)}；吹票 {row.get('pump')}；技术 {row.get('technical')}/40"
        wait = _compact_text(str(row.get("falsification_points") or row.get("entry_plan") or "等待缩量回踩和新催化"), 130)
        lines.append(f"| {_md_cell(_row_label(row))} | {_md_cell(reason)} | {_md_cell(crowding)} | {_md_cell(wait)} |")
    return lines


def _low_frequency_alpha_lines(
    candidate_rows: list[dict],
    preprocessed_snapshot: dict[str, list[sqlite3.Row]] | None = None,
    limit: int = 5,
) -> list[str]:
    lines = [
        "",
        "## 低频预期差线索",
        "",
        "| 标的 | 为什么不是热搜逻辑 | 边际改善/反转线索 | 下一步验证 |",
        "| --- | --- | --- | --- |",
    ]
    rows = _low_frequency_rows(candidate_rows, limit=limit)
    if not rows:
        fallback_rows = []
        if preprocessed_snapshot:
            for row in preprocessed_snapshot.get("opportunities", []):
                opportunity_type = str(row["opportunity_type"] or "")
                score = int(row["priority_score"] or 0)
                if "研报" in opportunity_type or score < 80:
                    fallback_rows.append(row)
        for row in fallback_rows[:limit]:
            lines.append(
                f"| {_md_cell(row['symbol_or_name'])} | 预处理资产低频召回，尚未完成完整交易验证 | "
                f"{_md_cell(_compact_text(str(row['reason']), 160))} | "
                f"{_md_cell(_compact_text(str(row['verification']), 120))} |"
            )
        if len(lines) < 5 + limit and preprocessed_snapshot:
            used_names = {str(row["symbol_or_name"]) for row in fallback_rows}
            for row in preprocessed_snapshot.get("assumptions", []):
                names = [*_json_values(row["linked_tickers_json"]), *_json_values(row["linked_companies_json"])]
                assumption_type = str(row["assumption_type"] or "")
                if assumption_type not in {"single_stock_assumption", "industry_kpi", "industry_framework", "overseas_mapping"}:
                    continue
                if not names and assumption_type == "single_stock_assumption":
                    continue
                label = " / ".join(names[:2]) if names else _compact_text(str(row["title"] or "行业线索"), 24)
                if label in used_names:
                    continue
                used_names.add(label)
                lines.append(
                    f"| {_md_cell(label)} | 研报/行业材料低频召回，尚未进入主候选 | "
                    f"{_md_cell(_compact_text(str(row['key_assumption'] or row['title']), 160))} | "
                    f"{_md_cell('用观点流、公告、财务和行情验证是否能映射到可交易标的')} |"
                )
                if len(lines) >= 5 + limit:
                    break
        if len(lines) == 5:
            lines.append("| 暂无 | 本窗口未筛出低频且可验证的标的 | 不硬凑冷门票 | 等新调研、价格、订单或财报线索 |")
        return lines
    for row in rows:
        why = f"{row.get('marginal_label')}；提及分布 {row.get('mentions_1d')}/{row.get('mentions_3d')}/{row.get('mentions_prior')}"
        signal = _compact_text(str(row.get("expectation_gap") or row.get("signal_interpretation") or row.get("note") or ""), 160)
        verify = _compact_text(str(row.get("verification_points") or row.get("entry_plan") or "等待经营数据和量价确认"), 140)
        lines.append(f"| {_md_cell(_row_label(row))} | {_md_cell(why)} | {_md_cell(signal)} | {_md_cell(verify)} |")
    return lines


def _research_assumption_lines(
    preprocessed_snapshot: dict[str, list[sqlite3.Row]] | None,
    candidate_rows: list[dict],
    max_rows: int = 8,
) -> list[str]:
    lines = [
        "",
        "## 行业/宏观研究观点",
        "",
        "| 材料类型 | 核心观点/假设 | 对交易的影响 | 下一步验证 |",
        "| --- | --- | --- | --- |",
    ]
    assumptions = list((preprocessed_snapshot or {}).get("assumptions", []))
    if not assumptions:
        lines.append("| 暂无 | 本窗口未形成结构化行业/宏观假设 | 不作为仓位依据 | 等待研报正文抽取 |")
        return lines
    candidate_text = " ".join(str(row.get("name")) + " " + str(row.get("note")) for row in candidate_rows[:16])
    used = 0
    for row in assumptions:
        assumption_type = str(row["assumption_type"] or "")
        tickers = _json_values(row["linked_tickers_json"])
        companies = _json_values(row["linked_companies_json"])
        themes = _json_values(row["linked_themes_json"])
        if tickers and assumption_type == "single_stock_assumption":
            continue
        assumption = _compact_text(str(row["key_assumption"] or row["title"] or ""), 180)
        if not assumption:
            continue
        if assumption_type == "macro_allocation":
            impact = "校准仓位和风险偏好，不直接推单票"
            verify = "观察指数风险偏好、利率/汇率/资金流是否配合"
        elif assumption_type == "industry_kpi":
            impact = "作为行业景气验证，寻找低位或弹性标的"
            verify = "跟踪价格、库存、开工率、订单和毛利率"
        elif assumption_type == "overseas_mapping":
            impact = "用于海外产业趋势映射，必须确认A股环节是否直接受益"
            verify = "跟踪海外龙头指引、CAPEX、A股供应商订单"
        else:
            impact = "补充产业链框架，帮助判断谁是核心受益而非蹭概念"
            verify = "回到观点流、财报、公告和行情承接交叉验证"
        linked = " / ".join([*themes[:2], *companies[:2]]) or "行业/宏观"
        if linked != "行业/宏观" and linked not in candidate_text:
            impact += "；当前尚未映射到主候选"
        lines.append(
            f"| {_md_cell(assumption_type)} | {_md_cell(assumption)} | {_md_cell(impact)} | {_md_cell(verify)} |"
        )
        used += 1
        if used >= max_rows:
            break
    if used == 0:
        lines.append("| 暂无 | 行业/宏观材料未能抽出可用假设 | 降低其在主报告中的权重 | 优先补PDF正文抽取 |")
    return lines


def _report_cross_validation_lines(
    reports: list[KpReport],
    candidate_rows: list[dict],
    preprocessed_snapshot: dict[str, list[sqlite3.Row]] | None = None,
    max_rows: int = 8,
) -> list[str]:
    lines = [
        "",
        "## 研报交叉验证",
        "",
        "| 研报/材料 | 可用于验证什么 | 关联候选/主线 | 目前结论 |",
        "| --- | --- | --- | --- |",
    ]
    assumptions = list((preprocessed_snapshot or {}).get("assumptions", []))
    if assumptions:
        candidate_text = " ".join(str(row.get("name")) + " " + str(row.get("symbol")) + " " + str(row.get("note")) for row in candidate_rows[:16])
        used = 0
        for row in assumptions:
            title = str(row["title"] or "")
            assumption = str(row["key_assumption"] or title)
            tickers = _json_values(row["linked_tickers_json"])
            companies = _json_values(row["linked_companies_json"])
            themes = _json_values(row["linked_themes_json"])
            linked = []
            for item in [*tickers, *companies, *themes]:
                if item and item in candidate_text:
                    linked.append(item)
            assumption_type = str(row["assumption_type"] or "")
            if assumption_type == "single_stock_assumption":
                validate = "单票假设：收入、毛利、估值弹性"
            elif assumption_type == "industry_kpi":
                validate = "行业KPI：价格、库存、供需、开工率"
            elif assumption_type == "macro_allocation":
                validate = "宏观/策略：仓位、风偏、市场环境"
            elif assumption_type == "overseas_mapping":
                validate = "海外映射：CAPEX、产业趋势、供应链"
            else:
                validate = "产业链框架：核心变量和受益环节"
            conclusion = (
                f"可验证 {'/'.join(linked[:3])} 的交易假设"
                if linked
                else "暂未映射主候选，但可影响主线和仓位判断"
            )
            lines.append(
                f"| {_md_cell(_compact_text(title, 80))} | {_md_cell(validate + '；' + _compact_text(assumption, 90))} | "
                f"{_md_cell(' / '.join(linked[:3]) or '主线/背景')} | {_md_cell(conclusion)} |"
            )
            used += 1
            if used >= max_rows:
                return lines

    if not reports:
        lines.append("| 暂无PDF | NA | NA | 本窗口缺少研报交叉验证，降低结论置信度 |")
        return lines
    candidate_text = " ".join(str(row.get("name")) + " " + str(row.get("note")) for row in candidate_rows[:12])
    for report in reports[:max_rows]:
        text = " ".join([report.title, report.summary, " ".join(report.themes), " ".join(report.industries), " ".join(report.companies)])
        if any(word in text for word in ("价格", "库存", "供需", "周报", "涨价")):
            validate = "行业KPI：价格、库存、供需、开工率"
        elif report.companies or report.tickers:
            validate = "单票假设：收入、毛利率、估值、目标价"
        elif any(word in text for word in ("策略", "宏观", "资产", "资金")):
            validate = "市场环境和仓位风险偏好"
        else:
            validate = "产业链映射和关键变量"
        linked = []
        for row in candidate_rows[:12]:
            name = str(row.get("name") or "")
            if name and name in text:
                linked.append(name)
        if not linked:
            for theme in THEME_KEYWORDS:
                if theme in text and theme in candidate_text:
                    linked.append(theme)
                    break
        conclusion = "可作为观点流交叉验证材料，需抽正文假设" if linked else "暂未和主候选形成强映射，放入背景库"
        lines.append(
            f"| {_md_cell(_compact_text(report.title, 80))} | {_md_cell(validate)} | "
            f"{_md_cell(' / '.join(linked[:3]) or '背景材料')} | {_md_cell(conclusion)} |"
        )
    return lines


def _review_task_lines(candidate_rows: list[dict], event_reviews: list[EventLLMReview], research_state_status: str) -> list[str]:
    lines = [
        "",
        "## 复盘任务",
        "",
        f"- **数据落库**：{research_state_status}",
        "- **复盘窗口**：1/3/5/10 日，分别记录是否触发买点、是否证伪、是否跑赢所属主线、来源是否有效。",
    ]
    rows = _top_opportunity_rows(candidate_rows, limit=3)
    if rows:
        for row in rows:
            lines.append(
                f"- **{_row_label(row)}**：跟踪 `{_compact_text(str(row.get('verification_points') or row.get('entry_plan') or row.get('action')), 120)}`。"
            )
    true_events = _true_increment_reviews(event_reviews, limit=3)
    for review in true_events:
        lines.append(
            f"- **事件复盘**：{_compact_text(review.summary or review.impact_path, 100)}；验证 `{_compact_text(review.verification, 100)}`。"
        )
    return lines


def _quality_daily_main_lines(
    *,
    pm_control: PmControlAnalysis,
    candidate_rows: list[dict],
    event_reviews: list[EventLLMReview],
    event_signals: list[KpEventSignal],
    reports: list[KpReport],
    research_state_status: str,
    preprocessed_snapshot: dict[str, list[sqlite3.Row]] | None = None,
) -> list[str]:
    lines: list[str] = []
    lines.extend(_pm_one_page_lines(pm_control, candidate_rows, event_reviews, preprocessed_snapshot))
    lines.extend(_board_candidate_lines(candidate_rows))
    lines.extend(_watch_and_avoid_lines(candidate_rows, limit=8))
    lines.extend(_report_cross_validation_lines(reports, candidate_rows, preprocessed_snapshot, max_rows=4))
    lines.extend(_review_task_lines(candidate_rows, event_reviews, research_state_status))
    lines.extend(
        [
            "",
            "## 研究流水线状态",
            f"- **事件库**：规则层已抽取 {len([event for event in event_signals if _high_value_event(event)])} 条高价值事件；"
            f"LLM前置审稿 {sum(1 for review in event_reviews if review.status == 'analyzed')} 条。",
            f"- **PM总控**：{pm_control.status}。",
            "- **候选进入深度分析**：先要求真增量映射，再看基本面承接、技术位置和拥挤度。",
            "- **评分透明度**：机会卡片已展示优先级拆解；缺真增量、待验证或高位拥挤会直接降级。",
            "- **复盘闭环**：候选已写入待复盘表，后续补 1/3/5/10 日表现和来源质量评分。",
        ]
    )
    return lines


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
    preprocess_rows = data.get("preprocess_evidence", [])
    if isinstance(preprocess_rows, list):
        for row in preprocess_rows[:limit]:
            rows.append(f"- 预处理资产：{_compact_text(str(row), 620)}")
    item_list = data.get("items", [])
    if isinstance(item_list, list):
        remaining = max(0, limit - len(rows))
        for item in item_list[:remaining]:
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
    *,
    evidence_limit: int = 6,
) -> str:
    market_summary = market.summary if market else "未取得行情/财务评分。"
    symbol = market.symbol if market and market.symbol else "未解析"
    fundamental = market.fundamental_score if market else None
    technical = market.technical_score if market else None
    evidence = _compact_evidence_for_llm(name, data, limit=evidence_limit)
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
如果候选只是AI/算力/半导体等热门科技线的重复推荐，没有新的订单、价格、客户、业绩或政策证据，必须把 logic_score 压到55分以下，并把 trading_action 写成观察/回避。
如果候选来自研报假设、低频线索或非科技行业，不要因为热度低而忽略；重点寻找基本面拐点、价格/库存/订单边际变化、估值修复空间和未来1-4周可验证KPI。

必须按这个链路思考：
1. 信息翻译：这条段子/调研如果为真，真正新增的信息是什么？是订单、价格、供给约束、客户验证、业绩弹性、政策，还是纯情绪重复？
2. 题材生命周期：这条线索更像萌芽、早期升温、主升发酵、扩散补涨、一致性过强，还是退潮后卖方继续吹？
3. 预期差：市场可能还没充分定价的点是什么？如果已经涨很多，预期差是否被消化？
4. 公司承接：公司是核心受益、弹性受益、补涨映射，还是蹭概念？逻辑链有几跳，哪一跳最弱？
5. 基本面交叉验证：当前基本面分、增长、盈利质量、估值和市值弹性能否支撑这个故事？基本面差时不能只因为题材热就给高分。
6. 技术面交易窗口：趋势/量能/位置是支持建仓、只适合低吸、还是已经过热只能等回踩？
7. 拥挤度：卖方是否密集强call、是否目标市值叙事过满、是否已经被股价透支？逻辑对但拥挤时也要降级。
8. 胜率赔率：这笔交易的胜率来自信息质量、逻辑直接度、催化剂时钟和技术确认；赔率来自空间、估值弹性、市值大小和拥挤程度。
9. 交易计划：给出盘前可执行动作，不要泛泛说“关注”。要说明触发条件、买点、仓位级别、止损/证伪条件。
10. 差异化观点：必须说明“市场共识是什么、这条材料相对共识多了什么、如果没有多出东西为什么不值得交易”。没有差异化观点时，不允许给建仓候选。

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
    last_error = ""
    for attempt, evidence_limit in enumerate((6, 3, 1), start=1):
        try:
            prompt = _build_llm_market_prompt(name, data, market, evidence_limit=evidence_limit)
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
            retry_note = "" if attempt == 1 else f"；第{attempt}轮短证据重试成功"
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
                summary=_compact_text(f"{parsed.get('summary', '')}{retry_note}", 220),
                status="analyzed",
            )
        except Exception as exc:
            last_error = _compact_text(str(exc), 180)
            if attempt < 3:
                time.sleep(0.8 * attempt)
                continue
            break
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
        summary=f"LLM 分析失败，已用短证据重试仍未成功: {last_error}",
        status="failed",
    )


def _llm_failure_diagnostics(analyses: dict[str, CandidateLLMAnalysis], limit: int = 3) -> str:
    failures = [
        f"{analysis.candidate}: {_compact_text(analysis.summary, 90)}"
        for analysis in analyses.values()
        if analysis.status == "failed"
    ]
    if not failures:
        return "无"
    return "；".join(failures[:limit])


def _init_preprocess_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS kp_preprocess_runs (
            run_key TEXT PRIMARY KEY,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            schema_version INTEGER NOT NULL,
            items_scanned INTEGER,
            reports_scanned INTEGER,
            quality_rows INTEGER,
            content_units INTEGER,
            events INTEGER,
            clusters INTEGER,
            mappings INTEGER,
            report_assumptions INTEGER,
            opportunities INTEGER,
            ocr_low_quality INTEGER,
            pdf_pending_or_limited INTEGER,
            status TEXT,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS kp_raw_quality (
            source_table TEXT NOT NULL,
            source_id INTEGER NOT NULL,
            published_date TEXT,
            quality_status TEXT NOT NULL,
            quality_score INTEGER NOT NULL,
            issue_flags_json TEXT NOT NULL,
            snippet TEXT,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (source_table, source_id)
        );
        CREATE TABLE IF NOT EXISTS kp_content_units (
            unit_id TEXT PRIMARY KEY,
            source_table TEXT NOT NULL,
            source_id INTEGER NOT NULL,
            content_hash TEXT NOT NULL,
            published_at TEXT,
            source_type TEXT,
            research_layer TEXT,
            fusion_route TEXT,
            unit_kind TEXT NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            quality_status TEXT NOT NULL,
            tickers_json TEXT NOT NULL,
            company_names_json TEXT NOT NULL,
            industries_json TEXT NOT NULL,
            themes_json TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS kp_events (
            event_id TEXT PRIMARY KEY,
            unit_id TEXT NOT NULL,
            source_id INTEGER NOT NULL,
            published_at TEXT,
            source_type TEXT,
            event_type TEXT NOT NULL,
            direction TEXT NOT NULL,
            research_layer TEXT,
            fusion_route TEXT,
            objective_anchor TEXT,
            key_metrics_json TEXT,
            increment_level TEXT NOT NULL,
            evidence_grade TEXT NOT NULL,
            confidence TEXT NOT NULL,
            title TEXT NOT NULL,
            summary TEXT NOT NULL,
            verification TEXT NOT NULL,
            risk TEXT NOT NULL,
            tickers_json TEXT NOT NULL,
            company_names_json TEXT NOT NULL,
            themes_json TEXT NOT NULL,
            cluster_key TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS kp_event_clusters (
            cluster_key TEXT PRIMARY KEY,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            theme TEXT NOT NULL,
            event_type TEXT NOT NULL,
            title TEXT NOT NULL,
            event_count INTEGER NOT NULL,
            true_increment_count INTEGER NOT NULL,
            source_mix_json TEXT NOT NULL,
            tickers_json TEXT NOT NULL,
            company_names_json TEXT NOT NULL,
            themes_json TEXT NOT NULL,
            summary TEXT NOT NULL,
            verification TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS kp_event_stock_mapping (
            cluster_key TEXT NOT NULL,
            symbol_or_name TEXT NOT NULL,
            relation_type TEXT NOT NULL,
            evidence TEXT NOT NULL,
            chain_strength INTEGER NOT NULL,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (cluster_key, symbol_or_name)
        );
        CREATE TABLE IF NOT EXISTS kp_report_assumptions (
            assumption_id TEXT PRIMARY KEY,
            report_id INTEGER NOT NULL,
            published_at TEXT,
            assumption_type TEXT NOT NULL,
            title TEXT NOT NULL,
            key_assumption TEXT NOT NULL,
            linked_tickers_json TEXT NOT NULL,
            linked_companies_json TEXT NOT NULL,
            linked_themes_json TEXT NOT NULL,
            status TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS kp_candidate_opportunities (
            report_date TEXT NOT NULL,
            symbol_or_name TEXT NOT NULL,
            opportunity_type TEXT NOT NULL,
            cluster_key TEXT,
            priority_score INTEGER NOT NULL,
            action_bucket TEXT NOT NULL,
            reason TEXT NOT NULL,
            verification TEXT NOT NULL,
            risk TEXT NOT NULL,
            payload_json TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (report_date, symbol_or_name, opportunity_type)
        );
        """
    )
    _ensure_preprocess_columns(conn)
    conn.commit()


def _ensure_preprocess_columns(conn: sqlite3.Connection) -> None:
    def ensure(table: str, column: str, definition: str) -> None:
        existing = {str(row[1]) for row in conn.execute(f"PRAGMA table_info({table})")}
        if column not in existing:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")

    ensure("kp_content_units", "research_layer", "TEXT")
    ensure("kp_content_units", "fusion_route", "TEXT")
    ensure("kp_events", "research_layer", "TEXT")
    ensure("kp_events", "fusion_route", "TEXT")
    ensure("kp_events", "objective_anchor", "TEXT")
    ensure("kp_events", "key_metrics_json", "TEXT")


def _quality_flags_for_text(text: str) -> tuple[str, int, list[str]]:
    flags: list[str] = []
    body = str(text or "")
    if not body.strip():
        flags.append("empty_text")
    replacement_count = body.count("\ufffd")
    if replacement_count:
        flags.append("replacement_char")
    ocr_text = ""
    marker = "Image OCR:"
    if marker in body:
        ocr_text = body.split(marker, 1)[1]
        if len(ocr_text.strip()) < 30:
            flags.append("ocr_too_short")
        suspicious = len(re.findall(r"[�□]{1,}|[ҪժحͶ]{2,}", ocr_text))
        cjk = len(re.findall(r"[\u4e00-\u9fff]", ocr_text))
        latin_noise = len(re.findall(r"[А-Яа-яҪժحͶ]", ocr_text))
        if suspicious >= 3 or (latin_noise > cjk and latin_noise > 20):
            flags.append("ocr_low_quality")
    if re.search(r"\S+�\.(?:pdf|PDF)", body):
        flags.append("filename_abnormal")
    if "file_failures" in body or "download_limited" in body:
        flags.append("download_issue")
    score = 100
    score -= min(30, replacement_count * 2)
    if "ocr_low_quality" in flags:
        score -= 45
    if "ocr_too_short" in flags:
        score -= 15
    if "filename_abnormal" in flags:
        score -= 8
    if "empty_text" in flags:
        score = 0
    status = "ok"
    if "ocr_low_quality" in flags or score < 55:
        status = "low_quality"
    elif flags:
        status = "usable_with_warnings"
    return status, max(0, min(100, score)), flags


def _unit_kind_for_item(item: KpItem, source_type: str, quality_status: str) -> str:
    text = f"{item.title}\n{item.text}\n{item.summary}"
    if quality_status == "low_quality":
        return "low_quality_or_ocr_noise"
    if source_type in INFORMATION_RICH_TYPES:
        if "周度" in text or "价格" in text or "库存" in text:
            return "data_or_channel_evidence"
        return "research_feedback"
    if source_type in SELL_SIDE_TYPES:
        return "sell_side_view"
    if re.search(r"(强call|目标市值|翻倍|空间巨大)", text):
        return "promotion_or_crowding"
    return "general_stream"


def _increment_level_for_event(event: KpEventSignal, quality_status: str) -> str:
    if quality_status == "low_quality" or "低" in event.confidence:
        return "噪音"
    if event.event_type in {"订单/排产", "客户验证/导入", "涨价/价格弹性", "库存/供需", "业绩/指引"}:
        if event.source_type in INFORMATION_RICH_TYPES:
            return "真增量"
        return "半增量"
    if event.event_type in {"海外映射", "卖方观点/情绪", "研报框架"}:
        return "情绪重复"
    return "半增量"


def _evidence_grade_for_event(event: KpEventSignal, quality_score: int) -> str:
    if quality_score < 55 or "低" in event.confidence:
        return "低"
    if "高" in event.confidence:
        return "高"
    return "中"


def _direction_for_text(text: str) -> str:
    if re.search(r"(利空|下滑|下降|恶化|亏损|降价|库存累|需求弱|不及预期)", text):
        return "negative"
    if re.search(r"(利好|改善|上修|涨价|去库|订单|中标|验证|超预期|紧缺)", text):
        return "positive"
    return "neutral"


def _cluster_key_for_event(event: KpEventSignal) -> str:
    theme = event.themes[0] if event.themes else event.event_type
    company = event.companies[0] if event.companies else ""
    raw = f"{theme}|{event.event_type}|{company}".lower()
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]
    return f"cluster_{digest}"


def _report_assumption_type(report: KpReport) -> str:
    text = " ".join([report.title, report.summary, " ".join(report.themes), " ".join(report.industries)])
    if any(word in text for word in ("价格", "库存", "供需", "周报", "涨价")):
        return "industry_kpi"
    if report.tickers or report.companies:
        return "single_stock_assumption"
    if any(word in text for word in ("策略", "宏观", "资产", "资金", "流动性")):
        return "macro_strategy"
    if any(word in text for word in ("海外", "美股", "全球", "高盛", "摩根")):
        return "overseas_mapping"
    return "industry_framework"


def _insert_json(conn: sqlite3.Connection, sql: str, params: tuple[object, ...]) -> None:
    conn.execute(sql, params)


def preprocess_knowledge_planet_window(
    report_date: str,
    look_back_days: int = 6,
    *,
    progress: Callable[[str], None] | None = None,
) -> KpPreprocessStats:
    """Build cached research assets from raw Knowledge Planet items/reports."""
    conn = _connect()
    if conn is None:
        start_date, end_date = _date_window(report_date, look_back_days)
        return KpPreprocessStats(start_date, end_date, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "no_db")
    _init_preprocess_tables(conn)
    start_date, end_date = _date_window(report_date, look_back_days)
    now_text = datetime.now().isoformat(timespec="seconds")
    run_key = f"{start_date}:{end_date}:v{PREPROCESS_SCHEMA_VERSION}"

    if bool(get_config().get("knowledge_planet_preprocess_cache_enabled", True)):
        cached = conn.execute(
            """
            SELECT *
            FROM kp_preprocess_runs
            WHERE run_key = ? AND status = 'ok'
            """,
            (run_key,),
        ).fetchone()
        if cached is not None:
            item_count = int(
                conn.execute(
                    """
                    SELECT COUNT(*) AS n
                    FROM kp_items
                    WHERE substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) >= ?
                      AND substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) <= ?
                    """,
                    (start_date, end_date),
                ).fetchone()["n"]
                or 0
            )
            report_count = int(
                conn.execute(
                    """
                    SELECT COUNT(*) AS n
                    FROM kp_reports
                    WHERE substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) >= ?
                      AND substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) <= ?
                    """,
                    (start_date, end_date),
                ).fetchone()["n"]
                or 0
            )
            if (
                int(cached["items_scanned"] or 0) == item_count
                and int(cached["reports_scanned"] or 0) == report_count
            ):
                conn.close()
                stats = KpPreprocessStats(
                    start_date=start_date,
                    end_date=end_date,
                    items_scanned=int(cached["items_scanned"] or 0),
                    reports_scanned=int(cached["reports_scanned"] or 0),
                    quality_rows=int(cached["quality_rows"] or 0),
                    content_units=int(cached["content_units"] or 0),
                    events=int(cached["events"] or 0),
                    clusters=int(cached["clusters"] or 0),
                    mappings=int(cached["mappings"] or 0),
                    report_assumptions=int(cached["report_assumptions"] or 0),
                    opportunities=int(cached["opportunities"] or 0),
                    ocr_low_quality=int(cached["ocr_low_quality"] or 0),
                    pdf_pending_or_limited=int(cached["pdf_pending_or_limited"] or 0),
                    status="cached",
                )
                if progress:
                    progress(
                        "[preprocess] cached: "
                        f"items={item_count}, reports={report_count}, "
                        f"events={stats.events}, clusters={stats.clusters}, "
                        f"opportunities={stats.opportunities}, "
                        f"ocr_low_quality={stats.ocr_low_quality}"
                    )
                return stats

    item_rows = conn.execute(
        """
        SELECT *
        FROM kp_items
        WHERE substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) <= ?
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) ASC, id ASC
        """,
        (start_date, end_date),
    ).fetchall()
    report_rows = conn.execute(
        """
        SELECT *
        FROM kp_reports
        WHERE substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) <= ?
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) ASC, id ASC
        """,
        (start_date, end_date),
    ).fetchall()
    items = [_row_to_item(row) for row in item_rows]
    reports = [_row_to_report(row) for row in report_rows]
    if progress:
        progress(f"[preprocess] items={len(items)}, reports={len(reports)}, window={start_date}..{end_date}")

    old_clusters = [
        str(row["cluster_key"])
        for row in conn.execute(
            """
            SELECT cluster_key
            FROM kp_event_clusters
            WHERE start_date = ? AND end_date = ?
            """,
            (start_date, end_date),
        ).fetchall()
    ]
    for cluster_key in old_clusters:
        conn.execute("DELETE FROM kp_event_stock_mapping WHERE cluster_key = ?", (cluster_key,))
    conn.execute("DELETE FROM kp_event_clusters WHERE start_date = ? AND end_date = ?", (start_date, end_date))
    conn.execute(
        """
        DELETE FROM kp_events
        WHERE substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) <= ?
        """,
        (end_date, start_date, end_date, end_date),
    )
    conn.execute(
        """
        DELETE FROM kp_content_units
        WHERE substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) <= ?
        """,
        (end_date, start_date, end_date, end_date),
    )
    conn.execute(
        "DELETE FROM kp_raw_quality WHERE published_date >= ? AND published_date <= ?",
        (start_date, end_date),
    )
    conn.execute(
        """
        DELETE FROM kp_report_assumptions
        WHERE substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) <= ?
        """,
        (end_date, start_date, end_date, end_date),
    )
    conn.execute("DELETE FROM kp_candidate_opportunities WHERE report_date = ?", (end_date,))

    events_for_cluster: list[dict[str, object]] = []
    quality_rows = 0
    content_units = 0
    events_count = 0
    ocr_low_quality = 0
    pdf_pending_or_limited = 0

    for item in items:
        raw_text = f"{item.title}\n{item.text}\n{item.summary}"
        source_type = infer_private_source_type(raw_text, item.source_type)
        quality_status, quality_score, flags = _quality_flags_for_text(raw_text)
        if "ocr_low_quality" in flags:
            ocr_low_quality += 1
        if "download_issue" in flags:
            pdf_pending_or_limited += 1
        scores = _score_item(item)
        event = _parse_event_signal(item, source_type, scores)
        research_layer = _research_layer_for_signal(raw_text, source_type, event.event_type)
        fusion_route = _fusion_route_for_layer(research_layer, event.event_type)
        objective_anchor = _objective_anchor_for_event(event.event_type, research_layer)
        key_metrics = _extract_key_metrics(raw_text)
        quality_rows += 1
        _insert_json(
            conn,
            """
            INSERT OR REPLACE INTO kp_raw_quality (
                source_table, source_id, published_date, quality_status,
                quality_score, issue_flags_json, snippet, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "kp_items",
                item.row_id,
                item.published_at[:10],
                quality_status,
                quality_score,
                json.dumps(flags, ensure_ascii=False),
                _compact_text(item.summary or item.text or item.title, 260),
                now_text,
            ),
        )

        unit_id = f"item:{item.row_id}:main"
        unit_text = _compact_text(item.text, 4000)
        unit_kind = _unit_kind_for_item(item, source_type, quality_status)
        content_units += 1
        _insert_json(
            conn,
            """
            INSERT OR REPLACE INTO kp_content_units (
                unit_id, source_table, source_id, content_hash, published_at, source_type,
                research_layer, fusion_route, unit_kind, title, text, quality_status, tickers_json, company_names_json,
                industries_json, themes_json, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                unit_id,
                "kp_items",
                item.row_id,
                hashlib.sha1(f"{item.row_id}:{unit_text}".encode("utf-8")).hexdigest(),
                item.published_at,
                source_type,
                research_layer,
                fusion_route,
                unit_kind,
                item.title,
                unit_text,
                quality_status,
                json.dumps(list(item.tickers), ensure_ascii=False),
                json.dumps(list(item.companies), ensure_ascii=False),
                json.dumps(list(item.industries), ensure_ascii=False),
                json.dumps(list(item.themes), ensure_ascii=False),
                now_text,
            ),
        )
        if quality_status == "low_quality":
            continue
        increment = _increment_level_for_event(event, quality_status)
        evidence = _evidence_grade_for_event(event, quality_score)
        cluster_key = _cluster_key_for_event(event)
        event_id = f"event:{item.row_id}:{hashlib.sha1((event.event_type + event.interpretation).encode('utf-8')).hexdigest()[:10]}"
        events_count += 1
        events_for_cluster.append(
            {
                "cluster_key": cluster_key,
                "event": event,
                "increment": increment,
                "evidence": evidence,
                "direction": _direction_for_text(raw_text),
                "source_type": source_type,
                "research_layer": research_layer,
            }
        )
        _insert_json(
            conn,
            """
            INSERT OR REPLACE INTO kp_events (
                event_id, unit_id, source_id, published_at, source_type, event_type,
                direction, research_layer, fusion_route, objective_anchor, key_metrics_json,
                increment_level, evidence_grade, confidence, title, summary,
                verification, risk, tickers_json, company_names_json, themes_json,
                cluster_key, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_id,
                unit_id,
                item.row_id,
                item.published_at,
                source_type,
                event.event_type,
                _direction_for_text(raw_text),
                research_layer,
                fusion_route,
                objective_anchor,
                json.dumps(key_metrics, ensure_ascii=False),
                increment,
                evidence,
                event.confidence,
                item.title,
                _clean_report_snippet(event.interpretation, 360),
                event.verification,
                event.risk,
                json.dumps(list(event.tickers), ensure_ascii=False),
                json.dumps(list(event.companies), ensure_ascii=False),
                json.dumps(list(event.themes), ensure_ascii=False),
                cluster_key,
                now_text,
            ),
        )

    cluster_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in events_for_cluster:
        cluster_groups[str(row["cluster_key"])].append(row)
    clusters = 0
    mappings = 0
    opportunities = 0
    for cluster_key, rows in cluster_groups.items():
        events = [row["event"] for row in rows if isinstance(row.get("event"), KpEventSignal)]
        if not events:
            continue
        first_event = events[0]
        source_mix = Counter(str(row.get("source_type") or "") for row in rows)
        layer_mix = Counter(str(row.get("research_layer") or "") for row in rows)
        tickers = sorted({ticker for event in events for ticker in event.tickers})
        companies = sorted({company for event in events for company in event.companies})
        themes = sorted({theme for event in events for theme in event.themes})
        true_count = sum(1 for row in rows if row.get("increment") == "真增量")
        event_count = len(rows)
        theme = themes[0] if themes else first_event.event_type
        title = f"{theme}｜{first_event.event_type}"
        summary = _compact_text("；".join(event.interpretation for event in events[:3]), 500)
        verification = _compact_text("；".join(sorted({event.verification for event in events})[:3]), 300)
        clusters += 1
        _insert_json(
            conn,
            """
            INSERT OR REPLACE INTO kp_event_clusters (
                cluster_key, start_date, end_date, theme, event_type, title,
                event_count, true_increment_count, source_mix_json, tickers_json,
                company_names_json, themes_json, summary, verification, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cluster_key,
                start_date,
                end_date,
                theme,
                first_event.event_type,
                title,
                event_count,
                true_count,
                json.dumps(dict(source_mix), ensure_ascii=False),
                json.dumps(tickers, ensure_ascii=False),
                json.dumps(companies, ensure_ascii=False),
                json.dumps(themes, ensure_ascii=False),
                summary,
                verification,
                now_text,
            ),
        )
        related_names = tickers or companies
        for idx, name in enumerate(related_names[:8]):
            resolved_name = _resolve_candidate_symbol(name)
            if not resolved_name and re.fullmatch(r"[A-Z]{1,5}", str(name or "").strip()):
                continue
            symbol_or_name = resolved_name or name
            relation = "核心受益" if idx == 0 and true_count else "弹性/映射"
            strength = min(
                100,
                18
                + min(event_count, 6) * 5
                + min(true_count, 4) * 9
                + (10 if idx == 0 else 0),
            )
            mappings += 1
            _insert_json(
                conn,
                """
                INSERT OR REPLACE INTO kp_event_stock_mapping (
                    cluster_key, symbol_or_name, relation_type, evidence, chain_strength, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    cluster_key,
                    symbol_or_name,
                    relation,
                    _compact_text(summary, 220),
                    strength,
                    now_text,
                ),
            )
            priority = min(
                88,
                strength
                + min(true_count, 3) * 5
                - (0 if relation == "核心受益" else 8),
            )
            if priority >= 28:
                opportunities += 1
                if true_count and priority >= 58:
                    opportunity_type = "低频预期差" if event_count <= 3 else "热门优选"
                    action_bucket = "研究/等触发"
                else:
                    opportunity_type = "观察池"
                    action_bucket = "待验证"
                _insert_json(
                    conn,
                    """
                    INSERT OR REPLACE INTO kp_candidate_opportunities (
                        report_date, symbol_or_name, opportunity_type, cluster_key,
                        priority_score, action_bucket, reason, verification, risk,
                        payload_json, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        end_date,
                        name,
                        opportunity_type,
                        cluster_key,
                        priority,
                        action_bucket,
                        _compact_text(summary, 260),
                        verification,
                        first_event.risk,
                        json.dumps(
                            {
                                "event_count": event_count,
                                "true_increment_count": true_count,
                                "source_mix": dict(source_mix),
                                "research_layer_mix": dict(layer_mix),
                                "themes": themes,
                            },
                            ensure_ascii=False,
                        ),
                        now_text,
                    ),
                )

    report_assumptions = 0
    for report in reports:
        assumption_type = _report_assumption_type(report)
        title = report.title or report.summary or "Untitled report"
        assumption = _clean_report_snippet(_report_research_excerpt(report), 620)
        status = "pdf_text_available" if report.extracted_text_path else "metadata_only"
        if "download" in status.lower():
            pdf_pending_or_limited += 1
        assumption_id = f"report:{report.row_id}:{assumption_type}"
        report_assumptions += 1
        _insert_json(
            conn,
            """
            INSERT OR REPLACE INTO kp_report_assumptions (
                assumption_id, report_id, published_at, assumption_type, title,
                key_assumption, linked_tickers_json, linked_companies_json,
                linked_themes_json, status, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                assumption_id,
                report.row_id,
                report.published_at,
                assumption_type,
                title,
                assumption,
                json.dumps(list(report.tickers), ensure_ascii=False),
                json.dumps(list(report.companies), ensure_ascii=False),
                json.dumps(list(report.themes), ensure_ascii=False),
                status,
                now_text,
            ),
        )
        linked_names = [
            *list(report.tickers),
            *list(report.companies),
        ]
        for idx, raw_name in enumerate(linked_names[:8]):
            name = str(raw_name or "").strip()
            if not name:
                continue
            resolved_symbol = _resolve_candidate_symbol(name)
            symbol_or_name = resolved_symbol or name
            base_priority = {
                "single_stock_assumption": 58,
                "industry_kpi": 48,
                "industry_framework": 42,
                "overseas_mapping": 40,
                "macro_allocation": 34,
            }.get(assumption_type, 36)
            text_bonus = 8 if status == "pdf_text_available" else 0
            first_bonus = 6 if idx == 0 else 0
            priority = min(100, base_priority + text_bonus + first_bonus)
            if priority < 42:
                continue
            opportunities += 1
            _insert_json(
                conn,
                """
                INSERT OR REPLACE INTO kp_candidate_opportunities (
                    report_date, symbol_or_name, opportunity_type, cluster_key,
                    priority_score, action_bucket, reason, verification, risk,
                    payload_json, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    end_date,
                    symbol_or_name,
                    "研报假设待交叉验证",
                    f"report:{report.row_id}:{assumption_type}",
                    priority,
                    "研报验证/待单票复核",
                    _compact_text(f"{title}：{assumption}", 420),
                    "回到观点流、公告、财务和行情验证研报假设是否被市场重新定价。",
                    "卖方假设可能乐观，且研报标题/正文提及不等于短期催化。",
                    json.dumps(
                        {
                            "report_id": report.row_id,
                            "assumption_type": assumption_type,
                            "status": status,
                            "themes": list(report.themes),
                        },
                        ensure_ascii=False,
                    ),
                    now_text,
                ),
            )

    stats = KpPreprocessStats(
        start_date=start_date,
        end_date=end_date,
        items_scanned=len(items),
        reports_scanned=len(reports),
        quality_rows=quality_rows,
        content_units=content_units,
        events=events_count,
        clusters=clusters,
        mappings=mappings,
        report_assumptions=report_assumptions,
        opportunities=opportunities,
        ocr_low_quality=ocr_low_quality,
        pdf_pending_or_limited=pdf_pending_or_limited,
        status="ok",
    )
    conn.execute(
        """
        INSERT OR REPLACE INTO kp_preprocess_runs (
            run_key, start_date, end_date, schema_version, items_scanned,
            reports_scanned, quality_rows, content_units, events, clusters,
            mappings, report_assumptions, opportunities, ocr_low_quality,
            pdf_pending_or_limited, status, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            run_key,
            stats.start_date,
            stats.end_date,
            PREPROCESS_SCHEMA_VERSION,
            stats.items_scanned,
            stats.reports_scanned,
            stats.quality_rows,
            stats.content_units,
            stats.events,
            stats.clusters,
            stats.mappings,
            stats.report_assumptions,
            stats.opportunities,
            stats.ocr_low_quality,
            stats.pdf_pending_or_limited,
            stats.status,
            now_text,
        ),
    )
    conn.commit()
    conn.close()
    if progress:
        progress(
            "[preprocess] done: "
            f"events={stats.events}, clusters={stats.clusters}, opportunities={stats.opportunities}, "
            f"ocr_low_quality={stats.ocr_low_quality}"
        )
    return stats


def _like_filter_for_fields(
    fields: tuple[str, ...],
    terms: list[str],
    *,
    prefix: str = " AND ",
) -> tuple[str, list[object]]:
    like_terms = [term for term in (terms or []) if str(term or "").strip()]
    if not like_terms:
        return "", []
    clauses: list[str] = []
    params: list[object] = []
    for term in like_terms:
        like = _safe_like_term(term)
        clauses.append("(" + " OR ".join(f"{field} LIKE ?" for field in fields) + ")")
        params.extend([like] * len(fields))
    return prefix + "(" + " OR ".join(clauses) + ")", params


def _preprocess_snapshot(
    conn: sqlite3.Connection,
    end_date: str,
    lookback_days: int,
    *,
    terms: list[str] | None = None,
    limit: int = 12,
) -> dict[str, list[sqlite3.Row]]:
    start_date, window_end = _date_window(end_date, lookback_days)
    snapshot: dict[str, list[sqlite3.Row]] = {}
    event_filter, event_params = _like_filter_for_fields(
        ("tickers_json", "company_names_json", "themes_json", "title", "summary"),
        terms or [],
    )
    cluster_filter, cluster_params = _like_filter_for_fields(
        ("tickers_json", "company_names_json", "themes_json", "title", "summary"),
        terms or [],
    )
    opportunity_filter, opportunity_params = _like_filter_for_fields(
        ("symbol_or_name", "opportunity_type", "reason", "verification", "payload_json"),
        terms or [],
    )
    assumption_filter, assumption_params = _like_filter_for_fields(
        ("title", "key_assumption", "linked_tickers_json", "linked_companies_json", "linked_themes_json"),
        terms or [],
    )
    try:
        snapshot["events"] = conn.execute(
            f"""
            SELECT *
            FROM kp_events
            WHERE substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) >= ?
              AND substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) <= ?
              {event_filter}
            ORDER BY CASE increment_level WHEN '真增量' THEN 0 WHEN '半增量' THEN 1 WHEN '情绪重复' THEN 2 ELSE 3 END,
                     evidence_grade DESC,
                     published_at DESC
            LIMIT {int(limit)}
            """,
            [window_end, start_date, window_end, window_end, *event_params],
        ).fetchall()
    except sqlite3.OperationalError:
        snapshot["events"] = []
    try:
        snapshot["clusters"] = conn.execute(
            f"""
            SELECT *
            FROM kp_event_clusters
            WHERE start_date <= ? AND end_date >= ?
              {cluster_filter}
            ORDER BY true_increment_count DESC, event_count DESC
            LIMIT {int(limit)}
            """,
            [window_end, start_date, *cluster_params],
        ).fetchall()
    except sqlite3.OperationalError:
        snapshot["clusters"] = []
    try:
        snapshot["opportunities"] = conn.execute(
            f"""
            SELECT *
            FROM kp_candidate_opportunities
            WHERE report_date = ?
              {opportunity_filter}
            ORDER BY priority_score DESC
            LIMIT {int(limit)}
            """,
            [window_end, *opportunity_params],
        ).fetchall()
    except sqlite3.OperationalError:
        snapshot["opportunities"] = []
    try:
        snapshot["assumptions"] = conn.execute(
            f"""
            SELECT *
            FROM kp_report_assumptions
            WHERE substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) >= ?
              AND substr(COALESCE(NULLIF(published_at, ''), ?), 1, 10) <= ?
              {assumption_filter}
            ORDER BY published_at DESC, report_id DESC
            LIMIT {int(limit)}
            """,
            [window_end, start_date, window_end, window_end, *assumption_params],
        ).fetchall()
    except sqlite3.OperationalError:
        snapshot["assumptions"] = []
    try:
        snapshot["quality"] = conn.execute(
            """
            SELECT quality_status, count(*) AS n
            FROM kp_raw_quality
            WHERE published_date >= ? AND published_date <= ?
            GROUP BY quality_status
            """,
            (start_date, window_end),
        ).fetchall()
    except sqlite3.OperationalError:
        snapshot["quality"] = []
    return snapshot


def _preprocess_snapshot_from_db(
    end_date: str,
    lookback_days: int,
    *,
    terms: list[str] | None = None,
    limit: int = 12,
) -> dict[str, list[sqlite3.Row]]:
    conn = _connect()
    if conn is None:
        return {}
    try:
        return _preprocess_snapshot(conn, end_date, lookback_days, terms=terms, limit=limit)
    finally:
        conn.close()


def _preprocess_asset_lines(snapshot: dict[str, list[sqlite3.Row]]) -> list[str]:
    lines = ["", "## 预处理研究资产"]
    quality = {str(row["quality_status"]): int(row["n"]) for row in snapshot.get("quality", [])}
    if quality:
        lines.append(
            "- **质量审计**：" + "，".join(f"{key} {value}" for key, value in sorted(quality.items()))
        )
    opportunities = snapshot.get("opportunities", [])
    if opportunities:
        lines.extend(["", "| 机会 | 类型 | 分数 | 理由 | 验证 |", "| --- | --- | ---: | --- | --- |"])
        for row in opportunities[:8]:
            lines.append(
                f"| {_md_cell(row['symbol_or_name'])} | {_md_cell(row['opportunity_type'])} | {row['priority_score']} | "
                f"{_md_cell(_compact_text(row['reason'], 120))} | {_md_cell(_compact_text(row['verification'], 100))} |"
            )
    clusters = snapshot.get("clusters", [])
    if clusters:
        lines.extend(["", "| 事件簇 | 事件数 | 真增量 | 摘要 |", "| --- | ---: | ---: | --- |"])
        for row in clusters[:8]:
            lines.append(
                f"| {_md_cell(row['title'])} | {row['event_count']} | {row['true_increment_count']} | "
                f"{_md_cell(_compact_text(row['summary'], 140))} |"
            )
    events = snapshot.get("events", [])
    if events:
        lines.extend(
            [
                "",
                "| 事件 | 研究层 | 增量 | 客观验证锚 |",
                "| --- | --- | --- | --- |",
            ]
        )
        for row in events[:8]:
            lines.append(
                f"| {_md_cell(row['event_type'])} | {_md_cell(_row_get(row, 'research_layer', 'general_research_clue'))} | "
                f"{_md_cell(row['increment_level'])} | {_md_cell(_compact_text(_row_get(row, 'objective_anchor', row['verification']), 120))} |"
            )
    return lines


def _counter_from_rows(rows: list[sqlite3.Row], field: str) -> Counter:
    counter: Counter = Counter()
    for row in rows:
        try:
            value = str(row[field] or "").strip()
        except Exception:
            value = ""
        if value:
            counter[value] += 1
    return counter


def _row_get(row: sqlite3.Row, field: str, default: str = "") -> str:
    try:
        value = row[field]
    except Exception:
        return default
    return str(value or default)


def _stock_fusion_pack_lines(
    *,
    ticker: str,
    preprocessed_snapshot: dict[str, list[sqlite3.Row]],
    items: list[KpItem],
    reports: list[KpReport],
    primary_terms: list[str],
    expanded_terms: list[str],
) -> list[str]:
    events = list(preprocessed_snapshot.get("events", []))
    assumptions = list(preprocessed_snapshot.get("assumptions", []))
    opportunities = list(preprocessed_snapshot.get("opportunities", []))
    quality_rows = list(preprocessed_snapshot.get("quality", []))
    quality = {str(row["quality_status"]): int(row["n"]) for row in quality_rows}
    source_mix = _counter_from_rows(events, "source_type")
    layer_mix = _counter_from_rows(events, "research_layer")
    increment_mix = _counter_from_rows(events, "increment_level")
    hard_events = [
        row
        for row in events
        if str(row["source_type"] or "") in INFORMATION_RICH_TYPES
        or "增量" in str(row["increment_level"] or "")
    ]
    promotional_events = [
        row
        for row in events
        if str(row["source_type"] or "") in SELL_SIDE_TYPES
        or "情绪" in str(row["increment_level"] or "")
    ]

    lines = [
        "## Single-Stock Knowledge Fusion Pack",
        f"- Fusion target: {ticker}",
        f"- Direct terms: {', '.join(primary_terms) if primary_terms else '(none)'}",
        f"- Sector/KPI terms used for recall: {', '.join(expanded_terms[:18]) if expanded_terms else '(none)'}",
        f"- Raw matches: stream={len(items)}, pdf={len(reports)}; preprocessed matches: events={len(events)}, opportunities={len(opportunities)}, pdf_assumptions={len(assumptions)}",
    ]
    if quality:
        lines.append(
            "- Raw quality mix: "
            + ", ".join(f"{key}={value}" for key, value in sorted(quality.items()))
        )
    if source_mix:
        lines.append(
            "- Source mix after preprocessing: "
            + ", ".join(f"{key}={value}" for key, value in source_mix.most_common(6))
        )
    if layer_mix:
        lines.append(
            "- Research-layer mix: "
            + ", ".join(f"{key}={value}" for key, value in layer_mix.most_common(6))
        )
    if increment_mix:
        lines.append(
            "- Increment mix: "
            + ", ".join(f"{key}={value}" for key, value in increment_mix.most_common(6))
        )

    lines.extend(["", "### Hard / Proxy Clues To Fuse"])
    if hard_events:
        lines.extend(["| date | layer | type | evidence | clue | objective anchor |", "| --- | --- | --- | --- | --- | --- |"])
        for row in hard_events[:6]:
            lines.append(
                f"| {str(row['published_at'])[:16]} | {_md_cell(_row_get(row, 'research_layer', 'general_research_clue'))} | "
                f"{_md_cell(row['event_type'])} | {_md_cell(row['evidence_grade'])} | "
                f"{_md_cell(_compact_text(row['summary'], 140))} | "
                f"{_md_cell(_compact_text(_row_get(row, 'objective_anchor', row['verification']), 120))} |"
            )
    else:
        lines.append("- No high-information preprocessed clue matched this stock/window. Treat Knowledge Planet as weak background unless raw stream/PDF matches below are company-specific.")

    lines.extend(["", "### Sell-Side / Narrative Claims To Challenge"])
    if promotional_events:
        for row in promotional_events[:5]:
            lines.append(
                f"- {_compact_text(str(row['title'] or row['summary']), 150)}; challenge: "
                f"{_compact_text(str(row['risk'] or 'check story-to-profit bridge, crowding, and valuation absorption'), 130)} "
                f"Route: {_compact_text(_row_get(row, 'fusion_route'), 140)}"
            )
    else:
        lines.append("- No obvious promotional preprocessed claim matched this stock/window.")

    lines.extend(["", "### PDF / Research-Assumption Cross-Checks"])
    if assumptions:
        lines.extend(["| date | assumption type | research assumption | required cross-check |", "| --- | --- | --- | --- |"])
        for row in assumptions[:5]:
            lines.append(
                f"| {str(row['published_at'])[:10]} | {_md_cell(row['assumption_type'])} | "
                f"{_md_cell(_compact_text(row['key_assumption'], 150))} | "
                "map to filings, Tushare financials/valuation, sector KPI, and price/volume confirmation |"
            )
    else:
        lines.append("- No matched PDF assumption was found; do not infer sell-side research support from unrelated report lists.")

    lines.extend(
        [
            "",
            "### Fusion Instructions For Agents",
            "- Use Knowledge Planet as an alternative-intelligence prior, then reconcile it with filings, Tushare financials, peer data, price/volume behavior, and official announcements.",
            "- Treat industry weekly data, channel checks, broker survey data, and company research feedback as thesis-grade private/proxy evidence when source type and content quality are high. These clues may change the bull/base/bear probabilities, but they must be mapped into KPI, forecast, valuation, catalyst, and falsification fields.",
            "- Promote a clue into the main thesis only when it has a clear path: information -> business driver -> earnings/cash-flow or valuation assumption -> catalyst clock -> falsification signal.",
            "- For every high-information clue, downstream agents must assign one decision role: probability adjustment, valuation input, catalyst/verification item, sizing/timing adjustment, or rejected/noisy clue. Do not leave company-specific or industry-KPI-like clues as generic background.",
            "- If a clue is not used, state the exact rejection reason: stale, promotional, not company-specific / not ticker-specific, contradicted by filings/Tushare/price-volume data, already priced, or missing a product-to-profit bridge.",
            "- When a clue is used only as private/proxy evidence, translate it into scenario probabilities and verification gates rather than treating it as a hard fact.",
            "- Respect the research-layer tags: industry KPI data feeds the KPI/forecast layer; channel/research feedback feeds hypothesis and verification; macro/overseas mapping sets context; sell-side narratives go through bear-side challenge first.",
            "- If Knowledge Planet contradicts objective data, surface the contradiction instead of averaging the views.",
            "- If Knowledge Planet is rich but objective data is missing, do not dismiss it as noise. Use it to shape the working hypothesis, cap sizing/conviction, and create dated verification tasks.",
            "- To save tokens, downstream agents should use this fusion pack first; raw stream notes below are backup evidence, not the main reasoning spine.",
            "",
        ]
    )
    return lines


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

    config = get_config()
    lookback = int(
        config.get("knowledge_planet_lookback_days", 30)
        if look_back_days is None
        else look_back_days
    )
    sync_lookback = min(
        lookback,
        int(config.get("knowledge_planet_auto_sync_context_lookback_days", 7) or 0),
    )
    sync_status = ensure_knowledge_planet_upstream_synced_for_window(
        curr_date,
        sync_lookback,
        max_pages=int(config.get("knowledge_planet_context_sync_max_pages", 20) or 0),
        max_image_downloads=int(
            config.get("knowledge_planet_context_sync_max_image_downloads", 0) or 0
        ),
        max_file_downloads=int(
            config.get("knowledge_planet_context_sync_max_file_downloads", 0) or 0
        ),
    )
    preprocess_status = "disabled"
    if bool(config.get("knowledge_planet_preprocess_enabled", True)):
        preprocess_stats = preprocess_knowledge_planet_window(curr_date, lookback)
        preprocess_status = (
            f"{preprocess_stats.status}: events={preprocess_stats.events}, "
            f"clusters={preprocess_stats.clusters}, opportunities={preprocess_stats.opportunities}, "
            f"ocr_low_quality={preprocess_stats.ocr_low_quality}"
        )

    conn = _connect()
    if conn is None:
        return (
            "# Knowledge Planet intelligence context unavailable\n\n"
            f"- Upstream sync: {sync_status}\n"
            "- Reason: local index.sqlite was not found. Run scripts/import_knowledge_planet.cmd first."
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
    item_display_limit = min(
        item_limit,
        int(config.get("knowledge_planet_context_item_display_limit", 12) or 12),
    )
    report_display_limit = min(
        report_limit,
        int(config.get("knowledge_planet_context_report_display_limit", 8) or 8),
    )
    start_date, end_date = _date_window(curr_date, lookback)
    primary_terms = _stock_terms(ticker, include_industry_expansion=False)
    terms = _stock_terms(ticker, include_industry_expansion=True)
    expanded_terms = [term for term in terms if term not in primary_terms]

    items = _query_items(
        conn,
        terms=terms,
        primary_terms=primary_terms,
        start_date=start_date,
        end_date=end_date,
        limit=item_limit,
    )
    reports = _query_reports(
        conn,
        terms=terms,
        primary_terms=primary_terms,
        start_date=start_date,
        end_date=end_date,
        limit=report_limit,
    )
    preprocessed_snapshot = _preprocess_snapshot_from_db(
        curr_date,
        lookback,
        terms=terms,
        limit=10,
    )
    conn.close()

    lines = [
        f"# Knowledge Planet Alternative Intelligence Context for {ticker}",
        "",
        f"- Window: {start_date} to {end_date} ({lookback} days)",
        f"- Primary query terms: {', '.join(primary_terms) if primary_terms else '(none)'}",
        f"- Sector/KPI expansion terms: {', '.join(expanded_terms[:30]) if expanded_terms else '(none)'}",
        f"- Upstream sync: {sync_status}",
        f"- Preprocess: {preprocess_status}",
        f"- Matched stream items: {len(items)}",
        f"- Matched PDF reports: {len(reports)}",
        "- Evidence discipline: this is supplemental alternative/local research intelligence. Use it to enrich the objective TradingAgents chain, not to replace filings, announcements, financial statements, price/volume evidence, or reputable news. Industry weekly data, channel checks, broker survey data, and company research feedback are thesis-grade private/proxy evidence when content quality is high; they can change scenario probabilities after being mapped into KPI, forecast, valuation, catalyst, and falsification fields. Sell-side pushes and target-market-cap claims require story-to-profit validation and objective cross-checks.",
        "",
    ]

    if not items and not reports and not preprocessed_snapshot.get("events") and not preprocessed_snapshot.get("opportunities"):
        lines.extend(
            [
                "## Status",
                "No relevant Knowledge Planet stream items or PDF reports were found for this window.",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        _stock_fusion_pack_lines(
            ticker=ticker,
            preprocessed_snapshot=preprocessed_snapshot,
            items=items,
            reports=reports,
            primary_terms=primary_terms,
            expanded_terms=expanded_terms,
        )
    )

    if preprocessed_snapshot.get("events") or preprocessed_snapshot.get("opportunities"):
        lines.extend(["## Preprocessed Research Assets", ""])
        events = preprocessed_snapshot.get("events", [])
        if events:
            lines.extend(
                [
                    "| date | layer | event | increment | evidence | summary | objective anchor |",
                    "| --- | --- | --- | --- | --- | --- | --- |",
                ]
            )
            for row in events[:8]:
                lines.append(
                    f"| {str(row['published_at'])[:16]} | {_md_cell(_row_get(row, 'research_layer', 'general_research_clue'))} | "
                    f"{_md_cell(row['event_type'])} | {_md_cell(row['increment_level'])} | "
                    f"{_md_cell(row['evidence_grade'])} | {_md_cell(_compact_text(row['summary'], 120))} | "
                    f"{_md_cell(_compact_text(_row_get(row, 'objective_anchor', row['verification']), 100))} |"
                )
            lines.append("")
        opportunities = preprocessed_snapshot.get("opportunities", [])
        if opportunities:
            lines.extend(["| opportunity | type | score | reason | verification |", "| --- | --- | ---: | --- | --- |"])
            for row in opportunities[:6]:
                lines.append(
                    f"| {_md_cell(row['symbol_or_name'])} | {_md_cell(row['opportunity_type'])} | {row['priority_score']} | "
                    f"{_md_cell(_compact_text(row['reason'], 120))} | {_md_cell(_compact_text(row['verification'], 100))} |"
                )
            lines.append("")

    if items:
        lines.extend(["## Recent Stream Intelligence", "", "| date | type | credibility | title | use |", "| --- | --- | --- | --- | --- |"])
        for item in items[:item_display_limit]:
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
        for item in items[: min(6, item_display_limit)]:
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
        for report in reports[:report_display_limit]:
            lines.append(
                f"| {report.published_at[:10]} | {report.broker or 'unknown'} | {_compact_text(report.title, 100)} | extract framework, KPIs, assumptions, and optimism bias; do not inherit conclusion |"
            )
        lines.append("")

    if is_hog_breeding_text(ticker, *terms):
        lines.extend(
            [
                "## Hog-Breeding Intelligence Routing",
                "- Treat Knowledge Planet livestock data as a private/proxy KPI layer, not as a final conclusion.",
                "- Extract hog ASP, piglet price, sow price/inventory, output/slaughter weight, complete cost, feed cost, and frozen-pork inventory into the industry KPI and forecast bridge.",
                "- Translate sell-side hog-cycle calls into a hog-price sensitivity table and an implied-hog-price check before allowing them into valuation.",
                "- Do not value hog breeders with a standalone PE shortcut. Use unit spread, PB/NAV floor, normalized cycle earnings, and current-market-cap implied hog price together.",
                "",
            ]
        )

    lines.extend(
        [
            "## Required Agent Treatment",
            "- Use this context to discover what market participants may be trading and what sell-side frameworks are using.",
            "- Separate hard-to-publicly-verify but information-rich data from rumor or pure promotion.",
            "- High-confidence private/channel evidence should affect the research conclusion through scenario probabilities, catalyst timing, and verification thresholds; do not ignore it merely because it is not an official announcement.",
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
        WHERE substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) <= ?
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) DESC, id DESC
        """,
        (start_date, end_date),
    ).fetchall()
    return [_row_to_item(row) for row in rows]


def _reports_for_window(conn: sqlite3.Connection, report_date: str, lookback_days: int) -> list[KpReport]:
    start_date, end_date = _date_window(report_date, lookback_days)
    rows = conn.execute(
        """
        SELECT *
        FROM kp_reports
        WHERE substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) >= ?
          AND substr(COALESCE(NULLIF(published_at, ''), imported_at), 1, 10) <= ?
        ORDER BY COALESCE(NULLIF(published_at, ''), imported_at) DESC, id DESC
        """,
        (start_date, end_date),
    ).fetchall()
    return [_row_to_report(row) for row in rows]


def _seed_candidate_scores_from_preprocessed_assets(
    candidate_scores: dict[str, dict[str, object]],
    preprocessed_snapshot: dict[str, list[sqlite3.Row]],
    end_date: str,
) -> None:
    """Use preprocessed research assets as the first-class candidate source."""

    def add_signal(
        raw_name: str,
        *,
        score: int,
        pump: int,
        evidence: str,
        latest_date: str,
        source_label: str,
        opportunity_type: str = "",
    ) -> None:
        name = str(raw_name or "").strip()
        if not name:
            return
        resolved_symbol = _resolve_candidate_symbol(name)
        candidate_key = resolved_symbol or name
        bucket = candidate_scores[candidate_key]
        current_display = str(bucket.get("display_name") or "")
        name_is_code = bool(re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", name, flags=re.IGNORECASE))
        display_is_code = bool(re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", current_display, flags=re.IGNORECASE))
        if not current_display or (display_is_code and not name_is_code):
            bucket["display_name"] = name
        if resolved_symbol:
            bucket["symbol"] = resolved_symbol
        aliases = bucket.get("aliases")
        if isinstance(aliases, list) and name not in aliases:
            aliases.append(name)
        bucket["mentions"] = int(bucket.get("mentions") or 0) + 1
        days_old = 99
        parsed_latest = _parse_date(latest_date)
        parsed_end = _parse_date(end_date)
        if parsed_latest and parsed_end:
            days_old = max(0, (parsed_end.date() - parsed_latest.date()).days)
        if days_old <= 0:
            bucket["mentions_1d"] = int(bucket.get("mentions_1d") or 0) + 1
        elif days_old <= 2:
            bucket["mentions_3d"] = int(bucket.get("mentions_3d") or 0) + 1
        else:
            bucket["mentions_prior"] = int(bucket.get("mentions_prior") or 0) + 1
        recency_weight = _recency_weight(days_old)
        bucket["recency_score"] = float(bucket.get("recency_score") or 0.0) + recency_weight
        bucket["score"] = int(bucket.get("score") or 0) + _weighted_score(score, recency_weight)
        bucket["pump"] = int(bucket.get("pump") or 0) + pump
        if latest_date and latest_date > str(bucket.get("latest_date") or ""):
            bucket["latest_date"] = latest_date
        evidence_rows = bucket.setdefault("preprocess_evidence", [])
        if isinstance(evidence_rows, list):
            evidence_rows.append(f"{source_label}｜{_compact_text(evidence, 560)}")
        source_labels = bucket.setdefault("source_labels", [])
        if isinstance(source_labels, list) and source_label and source_label not in source_labels:
            source_labels.append(source_label)
        opportunity_types = bucket.setdefault("opportunity_types", [])
        if isinstance(opportunity_types, list) and opportunity_type and opportunity_type not in opportunity_types:
            opportunity_types.append(opportunity_type)

    for row in preprocessed_snapshot.get("opportunities", []):
        score = int(row["priority_score"] or 0)
        add_signal(
            str(row["symbol_or_name"] or ""),
            score=max(24, score),
            pump=0,
            evidence=f"{row['opportunity_type']}；{row['action_bucket']}；{row['reason']}；验证：{row['verification']}；风险：{row['risk']}",
            latest_date=end_date,
            source_label="候选机会资产",
            opportunity_type=str(row["opportunity_type"] or ""),
        )

    for row in preprocessed_snapshot.get("events", []):
        names = [*_json_values(row["tickers_json"]), *_json_values(row["company_names_json"])]
        if not names:
            continue
        increment = str(row["increment_level"] or "")
        evidence_grade = str(row["evidence_grade"] or "")
        base_score = 36
        if increment == "真增量":
            base_score += 22
        elif increment == "半增量":
            base_score += 10
        if evidence_grade == "高":
            base_score += 10
        elif "中" in evidence_grade:
            base_score += 4
        research_layer = _row_get(row, "research_layer", "general_research_clue")
        objective_anchor = _row_get(row, "objective_anchor", str(row["verification"] or ""))
        fusion_route = _row_get(row, "fusion_route", "")
        key_metrics = _json_values(_row_get(row, "key_metrics_json", "[]"))
        metric_text = "；关键数值：" + " / ".join(key_metrics[:3]) if key_metrics else ""
        for name in names[:6]:
            add_signal(
                name,
                score=base_score,
                pump=0,
                evidence=(
                    f"{row['event_type']}；{increment}/{evidence_grade}；研究层：{research_layer}；"
                    f"{row['summary']}{metric_text}；客观验证锚：{objective_anchor}；"
                    f"融合路径：{fusion_route}；风险：{row['risk']}"
                ),
                latest_date=str(row["published_at"] or "")[:10],
                source_label="事件资产",
                opportunity_type=str(row["event_type"] or ""),
            )

    for row in preprocessed_snapshot.get("assumptions", []):
        names = [*_json_values(row["linked_tickers_json"]), *_json_values(row["linked_companies_json"])]
        if not names:
            continue
        assumption_type = str(row["assumption_type"] or "")
        base_score = 34
        if assumption_type == "single_stock_assumption":
            base_score = 56
        elif assumption_type == "industry_kpi":
            base_score = 46
        for name in names[:6]:
            add_signal(
                name,
                score=base_score,
                pump=0,
                evidence=f"{assumption_type}；{row['title']}；核心假设：{row['key_assumption']}；状态：{row['status']}",
                latest_date=str(row["published_at"] or "")[:10],
                source_label="研报假设资产",
                opportunity_type="研报假设待交叉验证",
            )


def build_knowledge_planet_daily_report(
    report_date: str,
    look_back_days: int = 6,
    max_candidates: int = DAILY_ANALYSIS_TARGETS,
    include_market_scores: bool = False,
    max_scored_candidates: int = DAILY_ANALYSIS_TARGETS,
    include_llm_market_analysis: bool = False,
    max_llm_candidates: int = DAILY_ANALYSIS_TARGETS,
    llm_provider: str = "deepseek",
    llm_model: str = "deepseek-chat",
    llm_base_url: str | None = None,
    progress: Callable[[str], None] | None = None,
) -> str:
    """Build a deterministic theme-trading daily report from the local database."""
    max_candidates = max(DAILY_ANALYSIS_TARGETS, int(max_candidates or 0))
    max_scored_candidates = DAILY_ANALYSIS_TARGETS
    max_llm_candidates = DAILY_ANALYSIS_TARGETS
    sync_status = ensure_knowledge_planet_upstream_synced_for_window(
        report_date,
        look_back_days,
        progress=progress,
    )
    preprocess_status = "disabled"
    if bool(get_config().get("knowledge_planet_preprocess_enabled", True)):
        preprocess_stats = preprocess_knowledge_planet_window(
            report_date,
            look_back_days,
            progress=progress,
        )
        preprocess_status = (
            f"{preprocess_stats.status}: events={preprocess_stats.events}, "
            f"clusters={preprocess_stats.clusters}, opportunities={preprocess_stats.opportunities}, "
            f"ocr_low_quality={preprocess_stats.ocr_low_quality}"
        )

    conn = _connect()
    if conn is None:
        return (
            "# Knowledge Planet Daily Report unavailable\n\n"
            f"- Upstream sync: {sync_status}\n"
            "- Reason: local index.sqlite was not found. Run scripts/import_knowledge_planet.cmd first."
        )

    items = _items_for_window(conn, report_date, look_back_days)
    reports = _reports_for_window(conn, report_date, look_back_days)
    preprocessed_snapshot = _preprocess_snapshot(
        conn,
        report_date,
        look_back_days,
        limit=max(128, int(max_candidates or 0) * 4),
    )
    conn.close()

    start_date, end_date = _date_window(report_date, look_back_days)
    report_dates = _dates_for_window(end_date, look_back_days)
    source_counts = Counter(infer_private_source_type(f"{item.title}\n{item.text}", item.source_type) for item in items)
    theme_counts = Counter()
    theme_weighted_counts = Counter()
    theme_1d_counts = Counter()
    theme_3d_counts = Counter()
    theme_7d_counts = Counter()
    candidate_scores: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "mentions": 0,
            "mentions_1d": 0,
            "mentions_3d": 0,
            "mentions_prior": 0,
            "recency_score": 0.0,
            "score": 0,
            "pump": 0,
            "items": [],
            "display_name": "",
            "symbol": "",
            "aliases": [],
            "latest_date": "",
            "source_labels": [],
            "opportunity_types": [],
        }
    )
    information_items: list[tuple[KpItem, str]] = []
    pump_items: list[tuple[KpItem, int]] = []
    event_signals: list[KpEventSignal] = []

    for item in items:
        text = f"{item.title}\n{item.text}\n{item.summary}"
        source_type = infer_private_source_type(text, item.source_type)
        days_old = _item_days_old(item, end_date)
        recency_weight = _recency_weight(days_old)
        for theme in THEME_KEYWORDS:
            if theme.lower() in text.lower():
                theme_counts[theme] += 1
                theme_weighted_counts[theme] += recency_weight
                if days_old <= 0:
                    theme_1d_counts[theme] += 1
                if days_old <= 2:
                    theme_3d_counts[theme] += 1
                if days_old <= 6:
                    theme_7d_counts[theme] += 1
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
            if days_old <= 0:
                bucket["mentions_1d"] = int(bucket["mentions_1d"]) + 1
            elif days_old <= 2:
                bucket["mentions_3d"] = int(bucket["mentions_3d"]) + 1
            elif days_old <= 6:
                bucket["mentions_prior"] = int(bucket["mentions_prior"]) + 1
            bucket["recency_score"] = float(bucket["recency_score"]) + recency_weight
            bucket["score"] = int(bucket["score"]) + _weighted_score(
                scores["hard_info"] + scores["catalyst"] + scores["source_quality"],
                recency_weight,
            )
            bucket["pump"] = int(bucket["pump"]) + _weighted_score(scores["pump_risk"], recency_weight)
            item_date = str(item.published_at or "")[:10]
            if item_date and item_date > str(bucket.get("latest_date") or ""):
                bucket["latest_date"] = item_date
            cast_items = bucket["items"]
            if isinstance(cast_items, list) and len(cast_items) < 3:
                cast_items.append(item)

    _seed_candidate_scores_from_preprocessed_assets(
        candidate_scores,
        preprocessed_snapshot,
        end_date,
    )

    ranked_all = sorted(
        candidate_scores.items(),
        key=lambda kv: (
            int(kv[1]["score"]) + float(kv[1]["recency_score"]) * 8 - int(kv[1]["pump"]) * 0.35
        ),
        reverse=True,
    )
    stock_ranked_all = [
        (name, data)
        for name, data in ranked_all
        if data.get("symbol") or re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", str(name), flags=re.IGNORECASE)
    ]
    stock_ranked = _select_candidate_targets(stock_ranked_all, max(0, int(max_candidates or 0)))
    stock_keys = {name for name, _data in stock_ranked_all}
    ranked = stock_ranked if stock_ranked else ranked_all[:max_candidates]
    unresolved_ranked = [(name, data) for name, data in ranked_all if name not in stock_keys][:max_candidates]

    market_scores: dict[str, CandidateMarketScore] = {}
    if include_market_scores:
        score_targets = _select_candidate_targets(stock_ranked_all, max(0, int(max_scored_candidates or 0)))
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
    market_llm = None
    if include_llm_market_analysis:
        try:
            llm = _create_market_analysis_llm(
                llm_provider,
                llm_model,
                llm_base_url,
                progress=progress,
            )
            market_llm = llm
            llm_targets = _select_candidate_targets(stock_ranked_all, max(0, int(max_llm_candidates or 0)))
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
        "- 时间权重：今日 2.0x，近三日 1.5x，近七日背景 1.0x；排序更重视边际变化，七日信息用于识别持续主线。",
        f"- 观点流条目：{len(items)}",
        f"- PDF 研报：{len(reports)}",
        f"- 上游同步：{sync_status}",
        f"- 预处理：{preprocess_status}",
        f"- 基本面/技术面评分：{'已启用，前 ' + str(max_scored_candidates) + ' 个候选尝试评分' if include_market_scores else '未启用'}",
        f"- LLM 逻辑拆解：{'已启用，' + llm_provider + '/' + llm_model + '，前 ' + str(max_llm_candidates) + ' 个候选' if include_llm_market_analysis else '未启用'}",
        (
            "- LLM 诊断："
            + (
                f"已尝试 {llm_attempted} 个，成功 {sum(1 for a in llm_analyses.values() if a.status == 'analyzed')} 个，"
                f"失败 {sum(1 for a in llm_analyses.values() if a.status == 'failed')} 个"
                f"，失败样例：{_llm_failure_diagnostics(llm_analyses)}"
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
        "- 先过硬门槛，再做软评分：LLM深度拆解、清晰交易假设、公司承接、技术评分、位置风险和动作层结论缺一不可；不过门槛不进主榜。",
        "- 观点流信号只用于候选召回和辅助展示，不作为高质量排序的核心依据；提及次数本身不构成买入理由。",
        "- LLM 逻辑拆解是高质量日报的主评分：先把段子翻译成真实增量信息，再判断预期差、公司承接、胜率赔率、催化剂时钟、交易计划和吹票风险。",
        "- 基本面验证不是独立加分项，而是题材逻辑的交叉验证：验证通过会强化观点流，承接不足会压低综合分上限；缺数据时不能进入 A 桶。",
        "- 基本面验证重点看收入/利润增速、ROE/毛利率、现金流/负债、估值和市值弹性，用来回答“故事能不能落到业绩和市值承接”。",
        "- 技术面最高 40 分，作为相对独立的交易时点评估：均线趋势、5/20/60 日动量、换手/量能确认、距离高点和过热风险。",
        "- 吹票/拥挤风险作为独立扣分项；A 桶仍需要单票 TradingAgents 复核后再考虑建仓。",
        "- 题材边际变化用每日去重后的观点流占比衡量，避免单日信息总量变化造成误判；近 7 日用于判断主线是否连续、是否只是短线噪声。",
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

    lines.extend(["", "## 题材热度图", "", "| 题材 | 七日提及 | 时间加权热度 |", "| --- | ---: | ---: |"])
    for theme, count in theme_weighted_counts.most_common(15):
        lines.append(f"| {theme} | {theme_counts[theme]} | {float(count):.1f} |")

    lines.extend(_theme_share_trend_lines(items, report_dates))

    candidate_rows: list[dict] = []
    display_ranked = stock_ranked if stock_ranked else ranked
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
        raw_evidence: list[str] = []
        if isinstance(item_list, list) and item_list:
            title_note = _compact_text("; ".join(item.title for item in item_list), 180)
            note = _compact_text(f"{note}；{title_note}" if note else title_note, 420)
            for item in item_list[:3]:
                raw_evidence.append(_format_item_evidence(item, max_chars=520))
        preprocess_evidence = data.get("preprocess_evidence")
        if isinstance(preprocess_evidence, list) and preprocess_evidence:
            asset_note = _compact_text("；".join(str(row) for row in preprocess_evidence[:2]), 260)
            note = _compact_text(f"{note}；{asset_note}" if note else asset_note, 520)
            for evidence in preprocess_evidence[:3]:
                raw_evidence.append(str(evidence))
        aliases = data.get("aliases")
        alias_text = ""
        if isinstance(aliases, list) and len(aliases) > 1:
            alias_text = " / ".join(str(alias) for alias in aliases[:4])
        row_display_name = display_name
        if market and market.company_name and re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)|\d{6}|BJ\d{6}", row_display_name, flags=re.IGNORECASE):
            row_display_name = market.company_name
        elif re.fullmatch(r"\d{6}\.(?:SH|SZ|BJ)", row_display_name, flags=re.IGNORECASE):
            row_display_name = COMMON_A_SHARE_NAMES_BY_SYMBOL.get(row_display_name.upper(), row_display_name)
        candidate_rows.append(
            {
                "name": row_display_name,
                "symbol": (market.symbol if market and market.symbol else str(data.get("symbol") or "未评分")),
                "aliases": alias_text,
                "signal_score": signal_score,
                "mentions_1d": int(data.get("mentions_1d") or 0),
                "mentions_3d": int(data.get("mentions_3d") or 0),
                "mentions_prior": int(data.get("mentions_prior") or 0),
                "recency_score": float(data.get("recency_score") or 0.0),
                "latest_date": str(data.get("latest_date") or ""),
                "llm_score": llm_analysis.logic_score if llm_analysis else None,
                "llm_status": llm_analysis.status if llm_analysis else "not_run",
                "llm_required": bool(include_llm_market_analysis),
                "market_scores_required": bool(include_market_scores),
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
                "candidate_lane": _candidate_data_lane(data),
                "source_labels": " / ".join(str(item) for item in data.get("source_labels", []) if item),
                "opportunity_types": " / ".join(str(item) for item in data.get("opportunity_types", []) if item),
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
                "raw_evidence": raw_evidence,
            }
        )
        candidate_rows[-1]["theme_stock_style"] = _theme_stock_style(candidate_rows[-1])
        candidate_rows[-1]["marginal_label"] = _candidate_marginal_label(candidate_rows[-1])
        candidate_rows[-1]["conviction_label"] = _candidate_conviction_label(candidate_rows[-1])
        candidate_rows[-1]["crowding_label"] = _candidate_crowding_label(candidate_rows[-1])
        candidate_rows[-1]["main_rise_score"] = _candidate_main_rise_score(candidate_rows[-1])
        candidate_rows[-1]["short_trade_score"] = _candidate_short_trade_score(candidate_rows[-1])
        linked_events = _candidate_event_links(candidate_rows[-1], event_signals)
        candidate_rows[-1]["linked_events"] = linked_events
        candidate_rows[-1]["hard_increment_count"] = sum(1 for event in linked_events if _event_is_trade_increment(event))
        candidate_rows[-1]["position_bucket"] = _candidate_position_bucket(candidate_rows[-1])
        candidate_rows[-1]["buildability_label"] = _candidate_buildability_label(candidate_rows[-1])
        candidate_rows[-1]["trade_hypothesis"] = _candidate_trade_hypothesis(candidate_rows[-1])
        candidate_rows[-1]["trade_type"] = _candidate_trade_type(candidate_rows[-1])
        candidate_rows[-1]["scorecard"] = _candidate_scorecard(candidate_rows[-1])
        candidate_rows[-1]["tradability_score"] = int(candidate_rows[-1]["scorecard"]["total"])
        candidate_rows[-1]["priority_score"] = _opportunity_priority(candidate_rows[-1])
        candidate_rows[-1]["score_breakdown"] = _candidate_score_breakdown(candidate_rows[-1])

    candidate_rows.sort(
        key=lambda row: (
            1 if _is_fully_analyzed_candidate(row) else 0,
            0 if _candidate_hard_gate_failures(row) else 1,
            _opportunity_priority(row),
            int(row.get("total_score") or 0),
            int(row.get("llm_score") or -1),
            int(row.get("signal_score") or 0),
        ),
        reverse=True,
    )

    mainline_rows = _desk_mainline_rows(theme_weighted_counts, event_signals, candidate_rows)
    report_dates = _dates_for_window(end_date, look_back_days)
    lifecycle_rows = _theme_lifecycle_persistence_rows(
        theme_1d_counts,
        theme_3d_counts,
        theme_7d_counts,
    )
    research_state_status = _persist_daily_research_state(end_date, lifecycle_rows, candidate_rows)
    event_reviews: list[EventLLMReview] = []
    if include_llm_market_analysis and market_llm is not None:
        if progress:
            progress("[event review] running front-loaded event quality review")
        event_reviews = _run_llm_event_review(
            market_llm,
            event_signals,
            start_date=start_date,
            end_date=end_date,
            max_events=14,
        )
        if progress:
            analyzed_events = sum(1 for review in event_reviews if review.status == "analyzed")
            failed_events = sum(1 for review in event_reviews if review.status == "failed")
            progress(f"[event review] done: analyzed={analyzed_events}, failed={failed_events}")
    if include_llm_market_analysis and market_llm is not None:
        if progress:
            progress("[pm control] running top-down PM synthesis")
        pm_control = _run_pm_control_analysis(
            market_llm,
            start_date=start_date,
            end_date=end_date,
            event_signals=event_signals,
            event_reviews=event_reviews,
            candidate_rows=candidate_rows,
            lifecycle_rows=lifecycle_rows,
            reports=reports,
        )
    else:
        pm_control = _deterministic_pm_control(candidate_rows, lifecycle_rows, event_signals)
    pm_insert_at = next((idx for idx, line in enumerate(lines) if line == "## 评分口径"), len(lines))
    pm_lines = _quality_daily_main_lines(
        pm_control=pm_control,
        candidate_rows=candidate_rows,
        event_reviews=event_reviews,
        event_signals=event_signals,
        reports=reports,
        research_state_status=research_state_status,
        preprocessed_snapshot=preprocessed_snapshot,
    )
    pm_lines.extend(
        [
            "",
            "## 附录：三日/窗口主线演化",
            "",
            "| 日期 | 观点流 | 高置信事件 | 当日主线 | 边际变化 | 代表线索 |",
            "| --- | ---: | ---: | --- | --- | --- |",
        ]
    )
    for date, item_count, event_count, themes, marginal, event_text in _daily_evolution_rows(
        items,
        event_signals,
        report_dates,
    ):
        pm_lines.append(
            f"| {date} | {item_count} | {event_count} | {_md_cell(themes)} | "
            f"{_md_cell(marginal)} | {_md_cell(event_text)} |"
        )
    lines[pm_insert_at:pm_insert_at] = pm_lines

    lines.extend(["", "## 附录：交易台主线总控"])
    if mainline_rows:
        lines.extend(["", "| 主线 | 强度 | 代表候选 | 主要事件 | 交易处理 |", "| --- | ---: | --- | --- | --- |"])
        for theme, score, leaders, event_desc, action in mainline_rows:
            lines.append(
                f"| {_md_cell(theme)} | {score} | {_md_cell(leaders)} | {_md_cell(event_desc)} | {_md_cell(action)} |"
            )
    else:
        lines.append("- 本窗口未形成清晰主线，先保持观察。")

    lines.extend(["", "### 附录：开盘剧本"])
    for item in _opening_playbook(candidate_rows):
        lines.append(f"- {item}")

    lines.extend(["", "## 附录：信息事件解析"])
    high_value_events_all = [event for event in event_signals if _high_value_event(event)]
    high_value_events = _balanced_events_by_date(
        high_value_events_all,
        report_dates,
        max_per_day=3,
        max_total=10,
    )
    if high_value_events:
        lines.extend(["", "| 时间 | 类型 | 置信度 | 线索 | 验证 | 风险 |", "| --- | --- | --- | --- | --- | --- |"])
        for event in high_value_events[:8]:
            lines.append(
                f"| {event.published_at[:16]} | {_md_cell(event.event_type)} | {_md_cell(event.confidence)} | "
                f"{_md_cell(_clean_report_snippet(event.interpretation or event.title, 110))} | {_md_cell(event.verification)} | {_md_cell(event.risk)} |"
            )
    else:
        lines.append("- 本窗口没有足够明确的订单、涨价、库存、客户验证或政策类事件。")

    lines.extend(
        [
            "",
            "## 附录：候选标的综合排序",
            "",
            "| 排名 | 标的 | 优先级 | 建仓价值 | 位置 | 边际变化 | 交易动作 |",
            "| ---: | --- | ---: | --- | --- | --- | --- |",
        ]
    )
    ranking_rows = candidate_rows[:15]
    for idx, row in enumerate(ranking_rows, start=1):
        candidate_label = f"{row['name']}（{row['symbol']}）"
        lines.append(
            f"| {idx} | {_md_cell(candidate_label)} | {_opportunity_priority(row)} | "
            f"{_md_cell(row.get('buildability_label') or _candidate_buildability_label(row))} | "
            f"{_md_cell(row.get('position_bucket') or _candidate_position_bucket(row))} | "
            f"{_md_cell(row['marginal_label'])} | "
            f"{_md_cell(_compact_text(str(row['action']), 80))} |"
        )
    if len(candidate_rows) > len(ranking_rows):
        lines.append(f"| ... | 其余 {len(candidate_rows) - len(ranking_rows)} 个候选 | NA | 仅入库复盘 | NA | NA | NA |")

    lines.extend(["", "## 附录：候选证据摘要"])
    detail_rows = candidate_rows[:5]
    for idx, row in enumerate(detail_rows, start=1):
        lines.extend(
            [
                "",
                f"### {idx}. {_md_cell(row['name'])}（{_md_cell(row['symbol'])}）",
                f"- **建仓价值/优先级**：{row.get('buildability_label') or _candidate_buildability_label(row)}；{row.get('score_breakdown') or _candidate_score_breakdown(row)}。",
                f"- **边际变化**：{row['marginal_label']}；近1日 {row['mentions_1d']} 次，近3日新增 {row['mentions_3d']} 次，七日更早线索 {row['mentions_prior']} 次，最近日期 {row['latest_date'] or 'NA'}。",
                f"- **交易动作**：{row['action']}",
                f"- **题材交易标签**：{row['theme_stock_style']}；位置：{row.get('position_bucket') or _candidate_position_bucket(row)}",
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
    if len(candidate_rows) > len(detail_rows):
        lines.append(f"- 其余 {len(candidate_rows) - len(detail_rows)} 个候选仅保留在排序表中，不展开证据。")

    if unresolved_ranked:
        lines.extend(["", "## 未进入主榜的未解析线索"])
        lines.append("- 以下内容未能解析为 A 股股票代码，暂不进入候选标的主榜；可作为产业线索或后续人工补充映射。")
        for name, data in unresolved_ranked[:6]:
            item_list = data.get("items", [])
            evidence = ""
            if isinstance(item_list, list) and item_list:
                evidence = _compact_text("; ".join(item.title for item in item_list[:2]), 180)
            lines.append(f"- **{_md_cell(data.get('display_name') or name)}**：{evidence}")

    lines.extend(["", "## 高价值产业/调研线索"])
    if information_items:
        for item, source_type in information_items[:8]:
            lines.append(
                f"- **{_compact_text(item.title, 100)}** ({source_type}, {item.published_at[:16]}): {_compact_text(item.summary or item.text, 260)}"
            )
    else:
        lines.append("- 本窗口未识别到信息含量较高的产业数据或调研反馈。")

    lines.extend(["", "## 卖方推票 / 吹票风险观察"])
    if pump_items:
        for item, risk in sorted(pump_items, key=lambda pair: pair[1], reverse=True)[:8]:
            lines.append(
                f"- **{_compact_text(item.title, 100)}**（吹票风险 {risk}）：需要补齐故事到利润的传导、催化剂时间表、估值消化能力和量价确认。"
            )
    else:
        lines.append("- 关键词规则未识别到高吹票风险条目。")

    lines.extend(["", "## PDF 研报研究视角"])
    if reports:
        for report in reports[:8]:
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
