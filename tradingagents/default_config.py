import os

_TRADINGAGENTS_HOME = os.path.join(os.path.expanduser("~"), ".tradingagents")


def _env_or_default(name: str, default: str) -> str:
    """Treat empty environment variables as unset.

    Windows shells commonly leave variables present-but-empty after a session
    or helper script mutates them. For path settings, an empty string should not
    silently disable a core subsystem such as memory persistence.
    """
    return os.getenv(name) or default

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
    "llm_provider": "openai",
    "deep_think_llm": "gpt-5.4",
    "quick_think_llm": "gpt-5.4-mini",
    # When None, each provider's client falls back to its own default endpoint
    # (api.openai.com for OpenAI, generativelanguage.googleapis.com for Gemini, ...).
    # The CLI overrides this per provider when the user picks one. Keeping a
    # provider-specific URL here would leak (e.g. OpenAI's /v1 was previously
    # being forwarded to Gemini, producing malformed request URLs).
    "backend_url": None,
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
