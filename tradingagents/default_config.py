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
    load_dotenv(os.path.join(_REPO_ROOT, ".env"), override=False)
    load_dotenv(os.path.join(_REPO_ROOT, ".env.enterprise"), override=False)


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
    # Optional web-search context for simple but thesis-critical high-frequency
    # facts not covered well by Tushare or filings, such as baijiu wholesale
    # prices, channel inventory, terminal discounts, and product price changes.
    "web_fact_check_enabled": True,
    "web_fact_check_timeout_sec": 6,
    "web_fact_check_max_queries": 3,
    "web_fact_check_max_results_per_query": 4,
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
