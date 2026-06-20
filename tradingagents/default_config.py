import os

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover - dotenv is optional at import time
    load_dotenv = None

_TRADINGAGENTS_HOME = os.path.join(os.path.expanduser("~"), ".tradingagents")
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def _load_environment_files() -> None:
    if load_dotenv is None:
        return
    load_dotenv(os.path.join(_REPO_ROOT, ".env"), override=False, encoding="utf-8-sig")
    load_dotenv(
        os.path.join(_REPO_ROOT, ".env.enterprise"),
        override=False,
        encoding="utf-8-sig",
    )


_load_environment_files()


def _env_or_default(name: str, default: str) -> str:
    """Treat empty environment variables as unset.

    Windows shells commonly leave variables present-but-empty after a session
    or helper script mutates them. For path settings, an empty string should not
    silently disable a core subsystem such as memory persistence.
    """
    return os.getenv(name) or default


def _env_int_or_default(name: str, default: int) -> int:
    value = os.getenv(name)
    if not value:
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _env_bool_or_default(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


def _env_or_none(name: str) -> str | None:
    value = os.getenv(name)
    return value or None


def _default_llm_provider() -> str:
    configured = os.getenv("TRADINGAGENTS_LLM_PROVIDER")
    if configured:
        return configured.lower()
    if os.getenv("DEEPSEEK_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        return "deepseek"
    return "openai"


def _default_deep_model(provider: str) -> str:
    if provider == "deepseek":
        return "deepseek-v4-pro"
    return "gpt-5.4"


def _default_quick_model(provider: str) -> str:
    if provider == "deepseek":
        return "deepseek-v4-flash"
    return "gpt-5.4-mini"


_DEFAULT_LLM_PROVIDER = _default_llm_provider()


DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": _env_or_default("TRADINGAGENTS_RESULTS_DIR", os.path.join(_TRADINGAGENTS_HOME, "logs")),
    "data_cache_dir": _env_or_default("TRADINGAGENTS_CACHE_DIR", os.path.join(_TRADINGAGENTS_HOME, "cache")),
    "memory_log_path": _env_or_default(
        "TRADINGAGENTS_MEMORY_LOG_PATH",
        os.path.join(_TRADINGAGENTS_HOME, "memory", "trading_memory.md"),
    ),
    # Optional cap on the number of resolved memory log entries. When set,
    # the oldest resolved entries are pruned once this limit is exceeded.
    # Pending entries are never pruned. None disables rotation entirely.
    "memory_log_max_entries": None,
    # LLM settings
    "llm_provider": _DEFAULT_LLM_PROVIDER,
    "deep_think_llm": _env_or_default(
        "TRADINGAGENTS_DEEP_THINK_LLM",
        _default_deep_model(_DEFAULT_LLM_PROVIDER),
    ),
    "quick_think_llm": _env_or_default(
        "TRADINGAGENTS_QUICK_THINK_LLM",
        _default_quick_model(_DEFAULT_LLM_PROVIDER),
    ),
    # When None, each provider's client falls back to its own default endpoint
    # (api.openai.com for OpenAI, generativelanguage.googleapis.com for Gemini, ...).
    # The CLI overrides this per provider when the user picks one. Keeping a
    # provider-specific URL here would leak (e.g. OpenAI's /v1 was previously
    # being forwarded to Gemini, producing malformed request URLs).
    "backend_url": _env_or_none("TRADINGAGENTS_BACKEND_URL"),
    # Network settings for LLM calls. Set TRADINGAGENTS_LLM_PROXY to values
    # such as http://127.0.0.1:7890 when OpenAI-compatible endpoints require
    # a local proxy. The client still honors provider/base_url settings.
    "llm_timeout": _env_int_or_default("TRADINGAGENTS_LLM_TIMEOUT", 120),
    "llm_max_retries": _env_int_or_default("TRADINGAGENTS_LLM_MAX_RETRIES", 5),
    "llm_proxy": os.getenv("TRADINGAGENTS_LLM_PROXY"),
    # Provider-specific thinking configuration
    "google_thinking_level": None,      # "high", "minimal", etc.
    "openai_reasoning_effort": None,    # "medium", "high", "low"
    "anthropic_effort": None,           # "high", "medium", "low"
    # Checkpoint/resume: when True, LangGraph saves state after each node
    # so a crashed run can resume from the last successful step.
    "checkpoint_enabled": False,
    # Output language for analyst reports and final decision
    # Internal agent debate stays in English for reasoning quality
    "output_language": "English",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Deterministically compact long precomputed contexts before LLM prompt
    # injection. Raw contexts are still kept in state and saved reports.
    "prompt_context_compaction_enabled": True,
    # A-share precomputed contexts are independent IO-heavy calls. Fetch a few
    # in parallel so the CLI does not sit idle before the first analyst starts.
    "a_share_context_fetch_workers": 4,
    # Fail fast before LLM generation when required A-share Tushare data is
    # unavailable. This avoids spending tokens on reports built from missing
    # core market/fundamental data.
    "a_share_data_preflight_enabled": True,
    "a_share_data_preflight_max_staleness_days": 21,
    # Treat readable filing text as a required pre-LLM input for A-share work.
    # This warms the disclosure cache and blocks shallow reports when MD&A,
    # segment, and business-model text cannot be read.
    "a_share_filing_text_preflight_enabled": True,
    "a_share_filing_text_preflight_look_back_days": 900,
    "a_share_filing_text_preflight_min_chars": 500,
    # Optional web-search context for simple but thesis-critical high-frequency
    # facts not covered well by Tushare or filings, such as baijiu wholesale
    # prices, channel inventory, terminal discounts, and product price changes.
    "web_fact_check_enabled": True,
    "web_fact_check_timeout_sec": 6,
    "web_fact_check_max_queries": 3,
    "web_fact_check_max_results_per_query": 4,
    # Local Knowledge Planet alternative-intelligence layer. The importer
    # builds the SQLite/PDF-text index ahead of time, so single-stock analysis
    # only performs bounded local lookups in the recent window.
    "knowledge_planet_enabled": True,
    "knowledge_planet_db_path": _env_or_none("KNOWLEDGE_PLANET_DB_PATH"),
    "knowledge_planet_lookback_days": _env_int_or_default(
        "KNOWLEDGE_PLANET_LOOKBACK_DAYS",
        30,
    ),
    "knowledge_planet_max_items": _env_int_or_default(
        "KNOWLEDGE_PLANET_MAX_ITEMS",
        30,
    ),
    "knowledge_planet_max_reports": _env_int_or_default(
        "KNOWLEDGE_PLANET_MAX_REPORTS",
        12,
    ),
    # Auto-sync upstream zsxq data before Knowledge Planet contexts/reports are
    # read. A date-level stamp prevents repeated downloads during the same day.
    "knowledge_planet_auto_sync_enabled": _env_bool_or_default(
        "KNOWLEDGE_PLANET_AUTO_SYNC",
        True,
    ),
    "knowledge_planet_auto_sync_group": _env_or_default(
        "KNOWLEDGE_PLANET_AUTO_SYNC_GROUP",
        "28888112822211:前沿信息收录",
    ),
    "knowledge_planet_auto_sync_max_pages": _env_int_or_default(
        "KNOWLEDGE_PLANET_AUTO_SYNC_MAX_PAGES",
        120,
    ),
    "knowledge_planet_auto_sync_max_image_downloads": _env_int_or_default(
        "KNOWLEDGE_PLANET_AUTO_SYNC_MAX_IMAGE_DOWNLOADS",
        100,
    ),
    "knowledge_planet_auto_sync_max_file_downloads": _env_int_or_default(
        "KNOWLEDGE_PLANET_AUTO_SYNC_MAX_FILE_DOWNLOADS",
        50,
    ),
    "knowledge_planet_auto_sync_min_interval_minutes": _env_int_or_default(
        "KNOWLEDGE_PLANET_AUTO_SYNC_MIN_INTERVAL_MINUTES",
        30,
    ),
    "knowledge_planet_auto_sync_context_lookback_days": _env_int_or_default(
        "KNOWLEDGE_PLANET_AUTO_SYNC_CONTEXT_LOOKBACK_DAYS",
        30,
    ),
    # Build cached intermediate research assets from raw Knowledge Planet
    # content before reports/contexts are generated. This keeps expensive LLM
    # calls focused on judgment instead of repeatedly cleaning raw streams.
    "knowledge_planet_preprocess_enabled": _env_bool_or_default(
        "KNOWLEDGE_PLANET_PREPROCESS",
        True,
    ),
    "knowledge_planet_preprocess_cache_enabled": _env_bool_or_default(
        "KNOWLEDGE_PLANET_PREPROCESS_CACHE",
        True,
    ),
    "knowledge_planet_context_item_display_limit": _env_int_or_default(
        "KNOWLEDGE_PLANET_CONTEXT_ITEM_DISPLAY_LIMIT",
        12,
    ),
    "knowledge_planet_context_report_display_limit": _env_int_or_default(
        "KNOWLEDGE_PLANET_CONTEXT_REPORT_DISPLAY_LIMIT",
        8,
    ),
    # Gated A-share compute-leasing verification layer. The module returns a
    # not_applicable status unless official or semi-official evidence indicates
    # compute leasing / AI-compute exposure, so unrelated names are not forced
    # into an AI data-center framework.
    "compute_leasing_context_enabled": True,
    # Gated defensive dividend layer. It returns not_applicable unless the
    # target looks like a dividend/defensive candidate, then tests whether the
    # yield is supported by profit, cash flow, industry durability, and peers.
    "dividend_defensive_context_enabled": True,
    # Filing intelligence can become very slow on giant annual reports. This
    # caps the text scanned by rule-based extractors while keeping high-signal
    # keyword windows, opening slices, and ending slices.
    "filing_intelligence_max_chars_per_report": 180_000,
    "filing_intelligence_max_total_chars": 420_000,
    # Data vendor configuration
    # Category-level configuration (default for all tools in category)
    "data_vendors": {
        "core_stock_apis": "yfinance",       # Options: alpha_vantage, yfinance
        "technical_indicators": "yfinance",  # Options: alpha_vantage, yfinance
        "fundamental_data": "yfinance",      # Options: alpha_vantage, yfinance
        "news_data": "yfinance",             # Options: alpha_vantage, yfinance
    },
    # Tool-level configuration (takes precedence over category-level)
    "tool_vendors": {
        # Example: "get_stock_data": "alpha_vantage",  # Override category default
    },
}
