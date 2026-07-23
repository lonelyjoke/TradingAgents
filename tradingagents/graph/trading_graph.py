# TradingAgents/graph/trading_graph.py

import logging
import os
from pathlib import Path
import json
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Callable, Dict, Any, Tuple, List, Optional, Mapping

import yfinance as yf

logger = logging.getLogger(__name__)

from langgraph.prebuilt import ToolNode

from tradingagents.llm_clients import create_llm_client

from tradingagents.agents import *
from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.agents.utils.memory import TradingMemoryLog
from tradingagents.dataflows.utils import safe_ticker_component
from tradingagents.agents.utils.agent_states import (
    AgentState,
    InvestDebateState,
    RiskDebateState,
)
from tradingagents.dataflows.config import set_config
from tradingagents.dataflows.interface import route_to_vendor
from tradingagents.dataflows.tushare_a_stock import (
    looks_like_a_share_query,
    resolve_a_share_symbol,
    is_a_share_symbol,
)
from tradingagents.dataflows.data_coverage import build_data_coverage_context
from tradingagents.dataflows.a_share_preflight import run_a_share_data_preflight
from tradingagents.dataflows.business_model_research import (
    build_company_business_model_context,
)
from tradingagents.dataflows.forecast_model_research import build_forecast_model_context
from tradingagents.dataflows.industry_cycle_research import build_industry_cycle_context
from tradingagents.dataflows.industry_kpi_research import build_industry_kpi_context
from tradingagents.dataflows.quality_audit_research import build_quality_audit_context
from tradingagents.dataflows.structured_research import build_structured_research_bundle
from tradingagents.dataflows.thesis_question_research import build_thesis_question_context

# Import the new abstract tool methods from agent_utils
from tradingagents.agents.utils.agent_utils import (
    get_stock_data,
    get_indicators,
    get_fundamentals,
    get_earnings_model_context,
    get_financial_report_intelligence_context,
    get_balance_sheet,
    get_cashflow,
    get_income_statement,
    get_insurance_context,
    get_intraday_behavior_context,
    get_medical_device_context,
    get_metals_mining_context,
    get_optical_module_context,
    get_investor_interaction_context,
    get_commodity_context,
    get_compute_leasing_context,
    get_consumer_staples_context,
    get_dividend_defensive_context,
    get_news,
    get_company_events,
    get_insider_transactions,
    get_global_news,
    get_market_sector_risk,
    get_market_expectation_context,
    get_market_timing_context,
    get_relative_strength_context,
    get_management_capital_allocation_context,
    get_price_move_attribution_context,
    get_baijiu_context,
    get_biopharma_context,
    get_building_materials_context,
    get_software_context,
    get_policy_planning_context,
    get_peer_comparison,
    get_price_earnings_decomposition_context,
    get_shareholder_structure_context,
    get_shipping_context,
    get_supply_chain_comparison,
    get_thematic_catalyst_context,
    get_valuation_percentiles,
    get_web_fact_check_context,
    get_knowledge_planet_context,
)

from .checkpointer import checkpoint_step, clear_checkpoint, get_checkpointer, thread_id
from .conditional_logic import ConditionalLogic
from .setup import GraphSetup
from .propagation import Propagator
from .reflection import Reflector
from .signal_processing import SignalProcessor


def _build_precomputed_data_coverage(
    *,
    thematic_catalyst_context: str,
    commodity_context: str,
    price_move_attribution_context: str,
    intraday_behavior_context: str,
    relative_strength_context: str,
    shipping_context: str,
    filing_intelligence_context: str,
    peer_comparison_context: str,
    supply_chain_comparison_context: str,
    earnings_model_context: str,
    company_events_context: str,
    market_expectation_context: str,
    price_earnings_decomposition_context: str,
    management_capital_allocation_context: str,
    shareholder_structure_context: str,
    investor_interaction_context: str,
    policy_planning_context: str,
    web_fact_check_context: str,
    knowledge_planet_context: str,
    baijiu_context: str,
    compute_leasing_context: str,
    dividend_defensive_context: str,
    building_materials_context: str,
    consumer_staples_context: str,
    optical_module_context: str,
    biopharma_context: str,
    software_context: str,
    insurance_context: str,
    medical_device_context: str,
    metals_mining_context: str,
    industry_cycle_context: str,
    company_business_model_context: str,
    industry_kpi_context: str,
    forecast_model_context: str,
    quality_audit_context: str,
    thesis_question_context: str,
) -> str:
    return build_data_coverage_context(
        {
            "thesis_question_context": thesis_question_context,
            "industry_cycle_scan": industry_cycle_context,
            "company_business_model": company_business_model_context,
            "industry_kpi_checklist": industry_kpi_context,
            "forecast_model_scaffold": forecast_model_context,
            "sell_side_quality_audit": quality_audit_context,
            "thematic_catalyst": thematic_catalyst_context,
            "commodity_product_price": commodity_context,
            "price_move_attribution": price_move_attribution_context,
            "intraday_minute_behavior": intraday_behavior_context,
            "relative_strength": relative_strength_context,
            "shipping_cycle": shipping_context,
            "financial_report_intelligence": filing_intelligence_context,
            "peer_comparison": peer_comparison_context,
            "supply_chain_comparison": supply_chain_comparison_context,
            "earnings_model": earnings_model_context,
            "company_events": company_events_context,
            "market_expectation": market_expectation_context,
            "price_eps_pe_decomposition": price_earnings_decomposition_context,
            "management_capital_allocation": management_capital_allocation_context,
            "shareholder_structure": shareholder_structure_context,
            "investor_interaction": investor_interaction_context,
            "policy_planning": policy_planning_context,
            "web_fact_check": web_fact_check_context,
            "knowledge_planet": knowledge_planet_context,
            "baijiu": baijiu_context,
            "compute_leasing": compute_leasing_context,
            "dividend_defensive": dividend_defensive_context,
            "building_materials": building_materials_context,
            "consumer_staples": consumer_staples_context,
            "optical_module": optical_module_context,
            "biopharma": biopharma_context,
            "software": software_context,
            "insurance": insurance_context,
            "medical_device": medical_device_context,
            "metals_mining": metals_mining_context,
        }
    )


_A_SHARE_CONTEXT_SPECS = [
    (
        "thematic_catalyst_context",
        "get_thematic_catalyst_context",
        "Thematic catalyst cross-check",
    ),
    ("commodity_context", "get_commodity_context", "Commodity/product-price context"),
    (
        "price_move_attribution_context",
        "get_price_move_attribution_context",
        "Price-move attribution context",
    ),
    (
        "intraday_behavior_context",
        "get_intraday_behavior_context",
        "Intraday minute-line behavior context",
    ),
    (
        "relative_strength_context",
        "get_relative_strength_context",
        "Relative strength / index linkage context",
    ),
    ("shipping_context", "get_shipping_context", "Shipping/freight-rate context"),
    (
        "filing_intelligence_context",
        "get_financial_report_intelligence_context",
        "Financial-report intelligence",
    ),
    ("peer_comparison_context", "get_peer_comparison", "Same-industry peer comparison"),
    (
        "supply_chain_comparison_context",
        "get_supply_chain_comparison",
        "Supply-chain position comparison",
    ),
    ("earnings_model_context", "get_earnings_model_context", "Earnings-model context"),
    ("company_events_context", "get_company_events", "Company announcement/event context"),
    (
        "market_expectation_context",
        "get_market_expectation_context",
        "Market-expectation context",
    ),
    (
        "price_earnings_decomposition_context",
        "get_price_earnings_decomposition_context",
        "Price-EPS-PE decomposition",
    ),
    (
        "management_capital_allocation_context",
        "get_management_capital_allocation_context",
        "Management/capital-allocation context",
    ),
    (
        "shareholder_structure_context",
        "get_shareholder_structure_context",
        "Shareholder-structure context",
    ),
    (
        "investor_interaction_context",
        "get_investor_interaction_context",
        "Investor-interaction context",
    ),
    ("policy_planning_context", "get_policy_planning_context", "Policy-planning context"),
    ("web_fact_check_context", "get_web_fact_check_context", "Web fact-check context"),
    (
        "knowledge_planet_context",
        "get_knowledge_planet_context",
        "Knowledge Planet topic-text intelligence context",
    ),
    ("baijiu_context", "get_baijiu_context", "Baijiu verification context"),
    (
        "compute_leasing_context",
        "get_compute_leasing_context",
        "Compute-leasing verification context",
    ),
    (
        "dividend_defensive_context",
        "get_dividend_defensive_context",
        "Dividend defensive verification context",
    ),
    (
        "building_materials_context",
        "get_building_materials_context",
        "Building-materials verification context",
    ),
    (
        "consumer_staples_context",
        "get_consumer_staples_context",
        "Consumer-staples verification context",
    ),
    (
        "optical_module_context",
        "get_optical_module_context",
        "AI optical-module verification context",
    ),
    (
        "biopharma_context",
        "get_biopharma_context",
        "Biopharma verification context",
    ),
    (
        "software_context",
        "get_software_context",
        "Software/SaaS verification context",
    ),
    (
        "insurance_context",
        "get_insurance_context",
        "Insurance verification context",
    ),
    (
        "medical_device_context",
        "get_medical_device_context",
        "Medical-device verification context",
    ),
    (
        "metals_mining_context",
        "get_metals_mining_context",
        "Metals/mining verification context",
    ),
]


def _context_unavailable(title: str, exc: Exception) -> str:
    return f"# {title} unavailable\n\n- Reason: {exc}"


class TradingAgentsGraph:
    """Main class that orchestrates the trading agents framework."""

    def __init__(
        self,
        selected_analysts=["market", "social", "news", "fundamentals"],
        debug=False,
        config: Dict[str, Any] = None,
        callbacks: Optional[List] = None,
    ):
        """Initialize the trading agents graph and components.

        Args:
            selected_analysts: List of analyst types to include
            debug: Whether to run in debug mode
            config: Configuration dictionary. If None, uses default config
            callbacks: Optional list of callback handlers (e.g., for tracking LLM/tool stats)
        """
        self.debug = debug
        self.config = config or DEFAULT_CONFIG
        self.callbacks = callbacks or []
        self.selected_analysts = list(selected_analysts or [])

        # Update the interface's config
        set_config(self.config)

        # Create necessary directories
        os.makedirs(self.config["data_cache_dir"], exist_ok=True)
        os.makedirs(self.config["results_dir"], exist_ok=True)

        # Initialize LLMs with provider-specific thinking configuration
        llm_kwargs = self._get_provider_kwargs()

        # Add callbacks to kwargs if provided (passed to LLM constructor)
        if self.callbacks:
            llm_kwargs["callbacks"] = self.callbacks

        deep_client = create_llm_client(
            provider=self.config["llm_provider"],
            model=self.config["deep_think_llm"],
            base_url=self.config.get("backend_url"),
            **llm_kwargs,
        )
        quick_client = create_llm_client(
            provider=self.config["llm_provider"],
            model=self.config["quick_think_llm"],
            base_url=self.config.get("backend_url"),
            **llm_kwargs,
        )

        self.deep_thinking_llm = deep_client.get_llm()
        self.quick_thinking_llm = quick_client.get_llm()
        
        self.memory_log = TradingMemoryLog(self.config)

        # Create tool nodes
        self.tool_nodes = self._create_tool_nodes()

        # Initialize components
        self.conditional_logic = ConditionalLogic(
            max_debate_rounds=self.config["max_debate_rounds"],
            max_risk_discuss_rounds=self.config["max_risk_discuss_rounds"],
        )
        self.graph_setup = GraphSetup(
            self.quick_thinking_llm,
            self.deep_thinking_llm,
            self.tool_nodes,
            self.conditional_logic,
        )

        self.propagator = Propagator()
        self.reflector = Reflector(self.quick_thinking_llm)
        self.signal_processor = SignalProcessor(self.quick_thinking_llm)

        # State tracking
        self.curr_state = None
        self.ticker = None
        self.log_states_dict = {}  # date to full state dict

        # Set up the graph: keep the workflow for recompilation with a checkpointer.
        self.workflow = self.graph_setup.setup_graph(selected_analysts)
        self.graph = self.workflow.compile()
        self._checkpointer_ctx = None

    def _get_provider_kwargs(self) -> Dict[str, Any]:
        """Get provider-specific kwargs for LLM client creation."""
        kwargs = {}
        provider = self.config.get("llm_provider", "").lower()
        openai_compatible = {
            "openai",
            "xai",
            "deepseek",
            "qwen",
            "glm",
            "ollama",
            "openrouter",
        }

        timeout = self.config.get("llm_timeout")
        if timeout is not None:
            kwargs["timeout"] = timeout
        max_retries = self.config.get("llm_max_retries")
        if max_retries is not None:
            kwargs["max_retries"] = max_retries
        if provider in openai_compatible:
            llm_proxy = self.config.get("llm_proxy")
            if llm_proxy:
                kwargs["proxy"] = llm_proxy

        if provider == "google":
            thinking_level = self.config.get("google_thinking_level")
            if thinking_level:
                kwargs["thinking_level"] = thinking_level

        elif provider == "openai":
            reasoning_effort = self.config.get("openai_reasoning_effort")
            if reasoning_effort:
                kwargs["reasoning_effort"] = reasoning_effort

        elif provider == "anthropic":
            effort = self.config.get("anthropic_effort")
            if effort:
                kwargs["effort"] = effort

        return kwargs

    def _create_tool_nodes(self) -> Dict[str, ToolNode]:
        """Create tool nodes for different data sources using abstract methods."""
        return {
            "market": ToolNode(
                [
                    # Core stock data tools
                    get_stock_data,
                    # Technical indicators
                    get_indicators,
                ]
            ),
            "social": ToolNode(
                [
                    # News tools for social media analysis
                    get_news,
                ]
            ),
            "news": ToolNode(
                [
                    # News and insider information
                    get_news,
                    get_global_news,
                    get_company_events,
                    get_insider_transactions,
                    get_thematic_catalyst_context,
                ]
            ),
            "fundamentals": ToolNode(
                [
                    # Fundamental analysis tools
                    get_fundamentals,
                    get_balance_sheet,
                    get_cashflow,
                    get_income_statement,
                    get_commodity_context,
                    get_price_move_attribution_context,
                    get_intraday_behavior_context,
                    get_relative_strength_context,
                    get_shipping_context,
                    get_peer_comparison,
                    get_supply_chain_comparison,
                    get_valuation_percentiles,
                    get_market_sector_risk,
                    get_market_timing_context,
                    get_thematic_catalyst_context,
                    get_financial_report_intelligence_context,
                    get_earnings_model_context,
                    get_market_expectation_context,
                    get_knowledge_planet_context,
                    get_price_earnings_decomposition_context,
                    get_management_capital_allocation_context,
                    get_shareholder_structure_context,
                    get_investor_interaction_context,
                    get_policy_planning_context,
                    get_baijiu_context,
                    get_compute_leasing_context,
                    get_dividend_defensive_context,
                    get_building_materials_context,
                    get_consumer_staples_context,
                    get_optical_module_context,
                    get_biopharma_context,
                    get_software_context,
                    get_insurance_context,
                    get_medical_device_context,
                    get_metals_mining_context,
                ]
            ),
        }

    def _fetch_returns(
        self, ticker: str, trade_date: str, holding_days: int = 5
    ) -> Tuple[Optional[float], Optional[float], Optional[int]]:
        """Fetch raw and alpha return for ticker over holding_days from trade_date.

        Returns (raw_return, alpha_return, actual_holding_days) or
        (None, None, None) if price data is unavailable (too recent, delisted,
        or network error).
        """
        try:
            start = datetime.strptime(trade_date, "%Y-%m-%d")
            end = start + timedelta(days=holding_days + 7)  # buffer for weekends/holidays
            end_str = end.strftime("%Y-%m-%d")

            stock = yf.Ticker(ticker).history(start=trade_date, end=end_str)
            spy = yf.Ticker("SPY").history(start=trade_date, end=end_str)

            if len(stock) < 2 or len(spy) < 2:
                return None, None, None

            actual_days = min(holding_days, len(stock) - 1, len(spy) - 1)
            raw = float(
                (stock["Close"].iloc[actual_days] - stock["Close"].iloc[0])
                / stock["Close"].iloc[0]
            )
            spy_ret = float(
                (spy["Close"].iloc[actual_days] - spy["Close"].iloc[0])
                / spy["Close"].iloc[0]
            )
            alpha = raw - spy_ret
            return raw, alpha, actual_days
        except Exception as e:
            logger.warning(
                "Could not resolve outcome for %s on %s (will retry next run): %s",
                ticker, trade_date, e,
            )
            return None, None, None

    def _resolve_pending_entries(self, ticker: str) -> None:
        """Resolve pending log entries for ticker at the start of a new run.

        Fetches returns for each same-ticker pending entry, generates reflections,
        then writes all updates in a single atomic batch write to avoid redundant I/O.
        Skips entries whose price data is not yet available (too recent or delisted).

        Trade-off: only same-ticker entries are resolved per run.  Entries for
        other tickers accumulate until that ticker is run again.
        """
        pending = [e for e in self.memory_log.get_pending_entries() if e["ticker"] == ticker]
        if not pending:
            return

        updates = []
        for entry in pending:
            raw, alpha, days = self._fetch_returns(ticker, entry["date"])
            if raw is None:
                continue  # price not available yet — try again next run
            reflection = self.reflector.reflect_on_final_decision(
                final_decision=entry.get("decision", ""),
                raw_return=raw,
                alpha_return=alpha,
            )
            updates.append({
                "ticker": ticker,
                "trade_date": entry["date"],
                "raw_return": raw,
                "alpha_return": alpha,
                "holding_days": days,
                "reflection": reflection,
            })

        if updates:
            self.memory_log.batch_update_with_outcomes(updates)

    def propagate(self, company_name, trade_date):
        """Run the trading agents graph for a company on a specific date.

        When ``checkpoint_enabled`` is set in config, the graph is recompiled
        with a per-ticker SqliteSaver so a crashed run can resume from the last
        successful node on a subsequent invocation with the same ticker+date.
        """
        if looks_like_a_share_query(company_name):
            resolved_company_name = resolve_a_share_symbol(company_name)
            if resolved_company_name:
                logger.info("Resolved A-share input %s to %s", company_name, resolved_company_name)
                company_name = resolved_company_name

        self.ticker = company_name

        # Resolve any pending memory-log entries for this ticker before the pipeline runs.
        self._resolve_pending_entries(company_name)

        # Recompile with a checkpointer if the user opted in.
        if self.config.get("checkpoint_enabled"):
            self._checkpointer_ctx = get_checkpointer(
                self.config["data_cache_dir"], company_name
            )
            saver = self._checkpointer_ctx.__enter__()
            self.graph = self.workflow.compile(checkpointer=saver)

            step = checkpoint_step(
                self.config["data_cache_dir"], company_name, str(trade_date)
            )
            if step is not None:
                logger.info(
                    "Resuming from step %d for %s on %s", step, company_name, trade_date
                )
            else:
                logger.info("Starting fresh for %s on %s", company_name, trade_date)

        try:
            return self._run_graph(company_name, trade_date)
        finally:
            if self._checkpointer_ctx is not None:
                self._checkpointer_ctx.__exit__(None, None, None)
                self._checkpointer_ctx = None
                self.graph = self.workflow.compile()

    def _fetch_a_share_contexts(
        self,
        company_name: str,
        trade_date: str,
        progress_callback: Optional[
            Callable[[str, str, str, Optional[float], Optional[int]], None]
        ] = None,
    ) -> Dict[str, str]:
        """Fetch independent A-share precomputed contexts, usually in parallel."""
        contexts = {key: "" for key, _, _ in _A_SHARE_CONTEXT_SPECS}
        if not is_a_share_symbol(company_name):
            return contexts

        max_workers = int(self.config.get("a_share_context_fetch_workers", 4) or 1)
        max_workers = max(1, min(max_workers, len(_A_SHARE_CONTEXT_SPECS)))

        def fetch_one(key: str, method: str, title: str):
            start = time.perf_counter()
            try:
                text = route_to_vendor(method, company_name, trade_date)
                elapsed = time.perf_counter() - start
                return key, title, text or "", elapsed, None
            except Exception as exc:
                elapsed = time.perf_counter() - start
                return key, title, _context_unavailable(title, exc), elapsed, exc

        if max_workers == 1:
            for key, method, title in _A_SHARE_CONTEXT_SPECS:
                if progress_callback:
                    progress_callback("start", key, title, None, None)
                key, title, text, elapsed, exc = fetch_one(key, method, title)
                contexts[key] = text
                if progress_callback:
                    event = "failed" if exc else "done"
                    progress_callback(event, key, title, elapsed, len(text))
            return contexts

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_spec = {}
            for key, method, title in _A_SHARE_CONTEXT_SPECS:
                if progress_callback:
                    progress_callback("start", key, title, None, None)
                future = executor.submit(fetch_one, key, method, title)
                future_to_spec[future] = (key, title)

            for future in as_completed(future_to_spec):
                key, title, text, elapsed, exc = future.result()
                contexts[key] = text
                if progress_callback:
                    event = "failed" if exc else "done"
                    progress_callback(event, key, title, elapsed, len(text))
        return contexts

    def _run_a_share_data_preflight(self, company_name: str, trade_date: str) -> str:
        if not self.config.get("a_share_data_preflight_enabled", True):
            return ""
        return run_a_share_data_preflight(
            company_name,
            str(trade_date),
            selected_analysts=self.selected_analysts,
            max_staleness_days=int(
                self.config.get("a_share_data_preflight_max_staleness_days", 21)
                or 21
            ),
            require_filing_text=bool(
                self.config.get("a_share_filing_text_preflight_enabled", True)
            ),
            filing_text_look_back_days=int(
                self.config.get("a_share_filing_text_preflight_look_back_days", 900)
                or 900
            ),
            min_filing_text_chars=int(
                self.config.get("a_share_filing_text_preflight_min_chars", 500)
                or 500
            ),
            strict=bool(
                self.config.get("a_share_data_preflight_strict", False)
            ),
        )

    def _build_structured_research_context(
        self,
        company_name: str,
        trade_date: str,
        contexts: Mapping[str, str],
    ) -> dict[str, Any]:
        """Build the typed evidence/segment/KPE bundle consumed by agents."""
        if not self.config.get("structured_research_preprocess_enabled", True):
            return {}
        cache_path: Path | None = None
        if self.config.get("structured_research_cache_enabled", True):
            cache_path = self._structured_research_cache_path(
                company_name,
                trade_date,
                contexts,
            )
            try:
                cached = json.loads(cache_path.read_text(encoding="utf-8"))
            except (OSError, ValueError, TypeError):
                cached = None
            if isinstance(cached, dict) and cached.get("symbol") == company_name:
                logger.info("Structured research cache hit: %s", cache_path.name)
                return cached

        bundle = build_structured_research_bundle(
            company_name,
            str(trade_date),
            contexts=contexts,
            llm=self.quick_thinking_llm,
            underwriting_llm=self.deep_thinking_llm,
            enable_llm=bool(
                self.config.get("structured_research_llm_enabled", True)
            ),
            enable_underwriting=bool(
                self.config.get("company_underwriting_packet_enabled", True)
            ),
            max_prompt_chars=int(
                self.config.get("structured_research_prompt_max_chars", 42000)
                or 42000
            ),
            underwriting_prompt_max_chars=int(
                self.config.get("company_underwriting_prompt_max_chars", 60000)
                or 60000
            ),
        )
        if cache_path is not None and self._structured_research_cacheable(bundle):
            try:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                temporary = cache_path.with_suffix(".tmp")
                temporary.write_text(
                    json.dumps(bundle, ensure_ascii=False, sort_keys=True),
                    encoding="utf-8",
                )
                os.replace(temporary, cache_path)
            except OSError as exc:
                logger.warning("Could not write structured research cache: %s", exc)
        return bundle

    @staticmethod
    def _llm_cache_identity(llm: Any) -> str:
        parts = [f"{type(llm).__module__}.{type(llm).__qualname__}"]
        for attribute in ("model_name", "model", "model_id", "deployment_name"):
            value = getattr(llm, attribute, None)
            if value:
                parts.append(f"{attribute}={value}")
        return "|".join(parts)

    def _structured_research_cache_path(
        self,
        company_name: str,
        trade_date: str,
        contexts: Mapping[str, str],
    ) -> Path:
        implementation_files = [
            Path(build_structured_research_bundle.__code__.co_filename),
            Path(build_structured_research_bundle.__code__.co_filename).with_name(
                "underwriting_packet.py"
            ),
            Path(build_structured_research_bundle.__code__.co_filename).with_name(
                "knowledge_planet_research.py"
            ),
            Path(build_structured_research_bundle.__code__.co_filename).with_name(
                "official_guidance.py"
            ),
            Path(build_structured_research_bundle.__code__.co_filename).with_name(
                "commodity_research.py"
            ),
        ]
        implementation_hash = hashlib.sha256()
        for path in implementation_files:
            try:
                implementation_hash.update(path.read_bytes())
            except OSError:
                implementation_hash.update(str(path).encode("utf-8"))
        fingerprint_payload = {
            "symbol": company_name,
            "trade_date": str(trade_date),
            "contexts": {key: str(value or "") for key, value in sorted(contexts.items())},
            "semantic_llm": self._llm_cache_identity(self.quick_thinking_llm),
            "underwriting_llm": self._llm_cache_identity(self.deep_thinking_llm),
            "enable_semantic_llm": bool(
                self.config.get("structured_research_llm_enabled", True)
            ),
            "enable_underwriting": bool(
                self.config.get("company_underwriting_packet_enabled", True)
            ),
            "semantic_max_chars": int(
                self.config.get("structured_research_prompt_max_chars", 42000) or 42000
            ),
            "underwriting_max_chars": int(
                self.config.get("company_underwriting_prompt_max_chars", 60000) or 60000
            ),
            "implementation": implementation_hash.hexdigest(),
        }
        digest = hashlib.sha256(
            json.dumps(
                fingerprint_payload,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()[:24]
        cache_root = Path(self.config["data_cache_dir"]) / "structured_research"
        safe_symbol = safe_ticker_component(company_name)
        safe_date = str(trade_date).replace("/", "-")
        return cache_root / f"{safe_symbol}_{safe_date}_{digest}.json"

    @staticmethod
    def _structured_research_cacheable(bundle: Mapping[str, Any]) -> bool:
        if not bundle:
            return False
        notes = " ".join(str(note) for note in bundle.get("preprocessing_notes", []))
        packet = dict(bundle.get("underwriting_packet", {}) or {})
        readiness = " ".join(str(reason) for reason in packet.get("readiness_reasons", []))
        transient_failure = "semantic LLM failed:" in notes or "LLM company underwriting failed" in readiness
        return not transient_failure

    def create_initial_state_with_context(
        self,
        company_name,
        trade_date,
        progress_callback: Optional[
            Callable[[str, str, str, Optional[float], Optional[int]], None]
        ] = None,
    ):
        """Build the initialized state shared by batch and CLI executions."""
        self._run_a_share_data_preflight(company_name, trade_date)
        past_context = self.memory_log.get_past_context(company_name)
        recent_decision_context = self.memory_log.get_recent_decision_context(
            company_name
        )
        contexts = self._fetch_a_share_contexts(
            company_name,
            trade_date,
            progress_callback=progress_callback,
        )
        thematic_catalyst_context = contexts["thematic_catalyst_context"]
        commodity_context = contexts["commodity_context"]
        price_move_attribution_context = contexts["price_move_attribution_context"]
        intraday_behavior_context = contexts["intraday_behavior_context"]
        relative_strength_context = contexts["relative_strength_context"]
        shipping_context = contexts["shipping_context"]
        filing_intelligence_context = contexts["filing_intelligence_context"]
        peer_comparison_context = contexts["peer_comparison_context"]
        supply_chain_comparison_context = contexts["supply_chain_comparison_context"]
        earnings_model_context = contexts["earnings_model_context"]
        company_events_context = contexts["company_events_context"]
        market_expectation_context = contexts["market_expectation_context"]
        price_earnings_decomposition_context = contexts["price_earnings_decomposition_context"]
        management_capital_allocation_context = contexts["management_capital_allocation_context"]
        shareholder_structure_context = contexts["shareholder_structure_context"]
        investor_interaction_context = contexts["investor_interaction_context"]
        policy_planning_context = contexts["policy_planning_context"]
        web_fact_check_context = contexts["web_fact_check_context"]
        knowledge_planet_context = contexts["knowledge_planet_context"]
        baijiu_context = contexts["baijiu_context"]
        compute_leasing_context = contexts["compute_leasing_context"]
        dividend_defensive_context = contexts["dividend_defensive_context"]
        building_materials_context = contexts["building_materials_context"]
        consumer_staples_context = contexts["consumer_staples_context"]
        optical_module_context = contexts["optical_module_context"]
        biopharma_context = contexts["biopharma_context"]
        software_context = contexts["software_context"]
        insurance_context = contexts["insurance_context"]
        medical_device_context = contexts["medical_device_context"]
        metals_mining_context = contexts["metals_mining_context"]
        industry_cycle_context = build_industry_cycle_context(
            company_name,
            str(trade_date),
            commodity_context=commodity_context,
            shipping_context=shipping_context,
            baijiu_context=baijiu_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            metals_mining_context=metals_mining_context,
            policy_planning_context=policy_planning_context,
            investor_interaction_context=investor_interaction_context,
            filing_intelligence_context=filing_intelligence_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        company_business_model_context = build_company_business_model_context(
            company_name,
            str(trade_date),
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            commodity_context=commodity_context,
            investor_interaction_context=investor_interaction_context,
            industry_cycle_context=industry_cycle_context,
            earnings_model_context=earnings_model_context,
            policy_planning_context=policy_planning_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        industry_kpi_context = build_industry_kpi_context(
            company_name,
            str(trade_date),
            filing_intelligence_context=filing_intelligence_context,
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            commodity_context=commodity_context,
            insurance_context=insurance_context,
            metals_mining_context=metals_mining_context,
            peer_comparison_context=peer_comparison_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        structured_research_context = self._build_structured_research_context(
            company_name,
            str(trade_date),
            {
                "filing_intelligence": filing_intelligence_context,
                "earnings_model": earnings_model_context,
                "company_events": company_events_context,
                "company_business_model": company_business_model_context,
                "industry_cycle": industry_cycle_context,
                "industry_kpi": industry_kpi_context,
                "market_expectation": market_expectation_context,
                "peer_comparison": peer_comparison_context,
                "management_capital_allocation": management_capital_allocation_context,
                "commodity": commodity_context,
                "policy": policy_planning_context,
                "investor_interaction": investor_interaction_context,
                "knowledge_planet": knowledge_planet_context,
            },
        )
        forecast_model_context = build_forecast_model_context(
            company_name,
            str(trade_date),
            earnings_model_context=earnings_model_context,
            company_business_model_context=company_business_model_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            insurance_context=insurance_context,
            company_events_context=company_events_context,
            industry_kpi_context=industry_kpi_context,
            metals_mining_context=metals_mining_context,
            knowledge_planet_context=knowledge_planet_context,
            market_expectation_context=market_expectation_context,
            structured_research_context=structured_research_context,
        )
        quality_audit_context = build_quality_audit_context(
            company_name,
            str(trade_date),
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            peer_comparison_context=peer_comparison_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            earnings_model_context=earnings_model_context,
            filing_intelligence_context=filing_intelligence_context,
            metals_mining_context=metals_mining_context,
            commodity_context=commodity_context,
            knowledge_planet_context=knowledge_planet_context,
            structured_research_context=structured_research_context,
        )
        thesis_question_context = build_thesis_question_context(
            company_name,
            str(trade_date),
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            quality_audit_context=quality_audit_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            earnings_model_context=earnings_model_context,
            market_expectation_context=market_expectation_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            management_capital_allocation_context=management_capital_allocation_context,
            shareholder_structure_context=shareholder_structure_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            commodity_context=commodity_context,
            shipping_context=shipping_context,
            baijiu_context=baijiu_context,
            compute_leasing_context=compute_leasing_context,
            dividend_defensive_context=dividend_defensive_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            optical_module_context=optical_module_context,
            biopharma_context=biopharma_context,
            software_context=software_context,
            insurance_context=insurance_context,
            medical_device_context=medical_device_context,
            metals_mining_context=metals_mining_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        data_coverage_context = _build_precomputed_data_coverage(
            thematic_catalyst_context=thematic_catalyst_context,
            commodity_context=commodity_context,
            price_move_attribution_context=price_move_attribution_context,
            intraday_behavior_context=intraday_behavior_context,
            relative_strength_context=relative_strength_context,
            shipping_context=shipping_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            earnings_model_context=earnings_model_context,
            company_events_context=company_events_context,
            market_expectation_context=market_expectation_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            management_capital_allocation_context=management_capital_allocation_context,
            shareholder_structure_context=shareholder_structure_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            knowledge_planet_context=knowledge_planet_context,
            baijiu_context=baijiu_context,
            compute_leasing_context=compute_leasing_context,
            dividend_defensive_context=dividend_defensive_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            optical_module_context=optical_module_context,
            biopharma_context=biopharma_context,
            software_context=software_context,
            insurance_context=insurance_context,
            medical_device_context=medical_device_context,
            metals_mining_context=metals_mining_context,
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            quality_audit_context=quality_audit_context,
            thesis_question_context=thesis_question_context,
        )
        return self.propagator.create_initial_state(
            company_name,
            trade_date,
            past_context=past_context,
            recent_decision_context=recent_decision_context,
            thematic_catalyst_context=thematic_catalyst_context,
            commodity_context=commodity_context,
            price_move_attribution_context=price_move_attribution_context,
            intraday_behavior_context=intraday_behavior_context,
            relative_strength_context=relative_strength_context,
            shipping_context=shipping_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            earnings_model_context=earnings_model_context,
            market_expectation_context=market_expectation_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            management_capital_allocation_context=management_capital_allocation_context,
            shareholder_structure_context=shareholder_structure_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            knowledge_planet_context=knowledge_planet_context,
            baijiu_context=baijiu_context,
            compute_leasing_context=compute_leasing_context,
            dividend_defensive_context=dividend_defensive_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            optical_module_context=optical_module_context,
            biopharma_context=biopharma_context,
            software_context=software_context,
            insurance_context=insurance_context,
            medical_device_context=medical_device_context,
            metals_mining_context=metals_mining_context,
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            quality_audit_context=quality_audit_context,
            thesis_question_context=thesis_question_context,
            data_coverage_context=data_coverage_context,
            structured_research_context=structured_research_context,
        )

    def _run_graph(self, company_name, trade_date):
        """Execute the graph and write the resulting state to disk and memory log."""
        # Initialize state — inject continuity context plus resolved lessons.
        self._run_a_share_data_preflight(company_name, trade_date)
        past_context = self.memory_log.get_past_context(company_name)
        recent_decision_context = self.memory_log.get_recent_decision_context(
            company_name
        )
        raw_contexts = self._fetch_a_share_contexts(company_name, trade_date)
        normalized_contexts = (
            {
                str(key): value
                for key, value in raw_contexts.items()
                if isinstance(value, str)
            }
            if isinstance(raw_contexts, Mapping)
            else {}
        )
        contexts = defaultdict(str, normalized_contexts)
        thematic_catalyst_context = contexts["thematic_catalyst_context"]
        commodity_context = contexts["commodity_context"]
        price_move_attribution_context = contexts["price_move_attribution_context"]
        intraday_behavior_context = contexts["intraday_behavior_context"]
        relative_strength_context = contexts["relative_strength_context"]
        shipping_context = contexts["shipping_context"]
        filing_intelligence_context = contexts["filing_intelligence_context"]
        peer_comparison_context = contexts["peer_comparison_context"]
        supply_chain_comparison_context = contexts["supply_chain_comparison_context"]
        earnings_model_context = contexts["earnings_model_context"]
        company_events_context = contexts["company_events_context"]
        market_expectation_context = contexts["market_expectation_context"]
        price_earnings_decomposition_context = contexts["price_earnings_decomposition_context"]
        management_capital_allocation_context = contexts["management_capital_allocation_context"]
        shareholder_structure_context = contexts["shareholder_structure_context"]
        investor_interaction_context = contexts["investor_interaction_context"]
        policy_planning_context = contexts["policy_planning_context"]
        web_fact_check_context = contexts["web_fact_check_context"]
        knowledge_planet_context = contexts["knowledge_planet_context"]
        baijiu_context = contexts["baijiu_context"]
        compute_leasing_context = contexts["compute_leasing_context"]
        dividend_defensive_context = contexts["dividend_defensive_context"]
        building_materials_context = contexts["building_materials_context"]
        consumer_staples_context = contexts["consumer_staples_context"]
        optical_module_context = contexts["optical_module_context"]
        biopharma_context = contexts["biopharma_context"]
        software_context = contexts["software_context"]
        insurance_context = contexts["insurance_context"]
        medical_device_context = contexts["medical_device_context"]
        metals_mining_context = contexts["metals_mining_context"]
        industry_cycle_context = build_industry_cycle_context(
            company_name,
            str(trade_date),
            commodity_context=commodity_context,
            shipping_context=shipping_context,
            baijiu_context=baijiu_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            metals_mining_context=metals_mining_context,
            policy_planning_context=policy_planning_context,
            investor_interaction_context=investor_interaction_context,
            filing_intelligence_context=filing_intelligence_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        company_business_model_context = build_company_business_model_context(
            company_name,
            str(trade_date),
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            commodity_context=commodity_context,
            investor_interaction_context=investor_interaction_context,
            industry_cycle_context=industry_cycle_context,
            earnings_model_context=earnings_model_context,
            policy_planning_context=policy_planning_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        industry_kpi_context = build_industry_kpi_context(
            company_name,
            str(trade_date),
            filing_intelligence_context=filing_intelligence_context,
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            commodity_context=commodity_context,
            insurance_context=insurance_context,
            metals_mining_context=metals_mining_context,
            peer_comparison_context=peer_comparison_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        structured_research_context = self._build_structured_research_context(
            company_name,
            str(trade_date),
            {
                "filing_intelligence": filing_intelligence_context,
                "earnings_model": earnings_model_context,
                "company_events": company_events_context,
                "company_business_model": company_business_model_context,
                "industry_cycle": industry_cycle_context,
                "industry_kpi": industry_kpi_context,
                "market_expectation": market_expectation_context,
                "peer_comparison": peer_comparison_context,
                "management_capital_allocation": management_capital_allocation_context,
                "commodity": commodity_context,
                "policy": policy_planning_context,
                "investor_interaction": investor_interaction_context,
                "knowledge_planet": knowledge_planet_context,
            },
        )
        if not isinstance(structured_research_context, Mapping):
            structured_research_context = {}
        forecast_model_context = build_forecast_model_context(
            company_name,
            str(trade_date),
            earnings_model_context=earnings_model_context,
            company_business_model_context=company_business_model_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            insurance_context=insurance_context,
            company_events_context=company_events_context,
            industry_kpi_context=industry_kpi_context,
            metals_mining_context=metals_mining_context,
            knowledge_planet_context=knowledge_planet_context,
            market_expectation_context=market_expectation_context,
            structured_research_context=structured_research_context,
        )
        quality_audit_context = build_quality_audit_context(
            company_name,
            str(trade_date),
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            peer_comparison_context=peer_comparison_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            earnings_model_context=earnings_model_context,
            filing_intelligence_context=filing_intelligence_context,
            metals_mining_context=metals_mining_context,
            commodity_context=commodity_context,
            knowledge_planet_context=knowledge_planet_context,
            structured_research_context=structured_research_context,
        )
        thesis_question_context = build_thesis_question_context(
            company_name,
            str(trade_date),
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            quality_audit_context=quality_audit_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            earnings_model_context=earnings_model_context,
            market_expectation_context=market_expectation_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            management_capital_allocation_context=management_capital_allocation_context,
            shareholder_structure_context=shareholder_structure_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            commodity_context=commodity_context,
            shipping_context=shipping_context,
            baijiu_context=baijiu_context,
            compute_leasing_context=compute_leasing_context,
            dividend_defensive_context=dividend_defensive_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            optical_module_context=optical_module_context,
            biopharma_context=biopharma_context,
            software_context=software_context,
            insurance_context=insurance_context,
            medical_device_context=medical_device_context,
            metals_mining_context=metals_mining_context,
            knowledge_planet_context=knowledge_planet_context,
        )
        data_coverage_context = _build_precomputed_data_coverage(
            thematic_catalyst_context=thematic_catalyst_context,
            commodity_context=commodity_context,
            price_move_attribution_context=price_move_attribution_context,
            intraday_behavior_context=intraday_behavior_context,
            relative_strength_context=relative_strength_context,
            shipping_context=shipping_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            earnings_model_context=earnings_model_context,
            company_events_context=company_events_context,
            market_expectation_context=market_expectation_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            management_capital_allocation_context=management_capital_allocation_context,
            shareholder_structure_context=shareholder_structure_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            knowledge_planet_context=knowledge_planet_context,
            baijiu_context=baijiu_context,
            compute_leasing_context=compute_leasing_context,
            dividend_defensive_context=dividend_defensive_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            optical_module_context=optical_module_context,
            biopharma_context=biopharma_context,
            software_context=software_context,
            insurance_context=insurance_context,
            medical_device_context=medical_device_context,
            metals_mining_context=metals_mining_context,
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            quality_audit_context=quality_audit_context,
            thesis_question_context=thesis_question_context,
        )
        init_agent_state = self.propagator.create_initial_state(
            company_name,
            trade_date,
            past_context=past_context,
            recent_decision_context=recent_decision_context,
            thematic_catalyst_context=thematic_catalyst_context,
            commodity_context=commodity_context,
            price_move_attribution_context=price_move_attribution_context,
            intraday_behavior_context=intraday_behavior_context,
            relative_strength_context=relative_strength_context,
            shipping_context=shipping_context,
            filing_intelligence_context=filing_intelligence_context,
            peer_comparison_context=peer_comparison_context,
            supply_chain_comparison_context=supply_chain_comparison_context,
            earnings_model_context=earnings_model_context,
            market_expectation_context=market_expectation_context,
            price_earnings_decomposition_context=price_earnings_decomposition_context,
            management_capital_allocation_context=management_capital_allocation_context,
            shareholder_structure_context=shareholder_structure_context,
            investor_interaction_context=investor_interaction_context,
            policy_planning_context=policy_planning_context,
            web_fact_check_context=web_fact_check_context,
            knowledge_planet_context=knowledge_planet_context,
            baijiu_context=baijiu_context,
            compute_leasing_context=compute_leasing_context,
            dividend_defensive_context=dividend_defensive_context,
            building_materials_context=building_materials_context,
            consumer_staples_context=consumer_staples_context,
            optical_module_context=optical_module_context,
            biopharma_context=biopharma_context,
            software_context=software_context,
            insurance_context=insurance_context,
            medical_device_context=medical_device_context,
            metals_mining_context=metals_mining_context,
            industry_cycle_context=industry_cycle_context,
            company_business_model_context=company_business_model_context,
            industry_kpi_context=industry_kpi_context,
            forecast_model_context=forecast_model_context,
            quality_audit_context=quality_audit_context,
            thesis_question_context=thesis_question_context,
            data_coverage_context=data_coverage_context,
            structured_research_context=structured_research_context,
        )
        args = self.propagator.get_graph_args()

        # Inject thread_id so same ticker+date resumes, different date starts fresh.
        if self.config.get("checkpoint_enabled"):
            tid = thread_id(company_name, str(trade_date))
            args.setdefault("config", {}).setdefault("configurable", {})["thread_id"] = tid

        if self.debug:
            trace = []
            for chunk in self.graph.stream(init_agent_state, **args):
                if len(chunk["messages"]) == 0:
                    pass
                else:
                    chunk["messages"][-1].pretty_print()
                    trace.append(chunk)
            final_state = trace[-1]
        else:
            final_state = self.graph.invoke(init_agent_state, **args)

        # Store current state for reflection.
        self.curr_state = final_state

        # Log state to disk.
        self._log_state(trade_date, final_state)

        # Store decision for deferred reflection on the next same-ticker run.
        self.memory_log.store_decision(
            ticker=company_name,
            trade_date=trade_date,
            final_trade_decision=final_state["final_trade_decision"],
        )

        # Clear checkpoint on successful completion to avoid stale state.
        if self.config.get("checkpoint_enabled"):
            clear_checkpoint(
                self.config["data_cache_dir"], company_name, str(trade_date)
            )

        return final_state, self.process_signal(final_state["final_trade_decision"])

    def _log_state(self, trade_date, final_state):
        """Log the final state to a JSON file."""
        self.log_states_dict[str(trade_date)] = {
            "company_of_interest": final_state["company_of_interest"],
            "trade_date": final_state["trade_date"],
            "thematic_catalyst_context": final_state.get(
                "thematic_catalyst_context", ""
            ),
            "commodity_context": final_state.get(
                "commodity_context", ""
            ),
            "industry_cycle_context": final_state.get(
                "industry_cycle_context", ""
            ),
            "company_business_model_context": final_state.get(
                "company_business_model_context", ""
            ),
            "industry_kpi_context": final_state.get(
                "industry_kpi_context", ""
            ),
            "forecast_model_context": final_state.get(
                "forecast_model_context", ""
            ),
            "quality_audit_context": final_state.get(
                "quality_audit_context", ""
            ),
            "thesis_question_context": final_state.get(
                "thesis_question_context", ""
            ),
            "price_move_attribution_context": final_state.get(
                "price_move_attribution_context", ""
            ),
            "intraday_behavior_context": final_state.get(
                "intraday_behavior_context", ""
            ),
            "relative_strength_context": final_state.get(
                "relative_strength_context", ""
            ),
            "shipping_context": final_state.get(
                "shipping_context", ""
            ),
            "filing_intelligence_context": final_state.get(
                "filing_intelligence_context", ""
            ),
            "peer_comparison_context": final_state.get(
                "peer_comparison_context", ""
            ),
            "supply_chain_comparison_context": final_state.get(
                "supply_chain_comparison_context", ""
            ),
            "earnings_model_context": final_state.get(
                "earnings_model_context", ""
            ),
            "market_expectation_context": final_state.get(
                "market_expectation_context", ""
            ),
            "price_earnings_decomposition_context": final_state.get(
                "price_earnings_decomposition_context", ""
            ),
            "management_capital_allocation_context": final_state.get(
                "management_capital_allocation_context", ""
            ),
            "shareholder_structure_context": final_state.get(
                "shareholder_structure_context", ""
            ),
            "investor_interaction_context": final_state.get(
                "investor_interaction_context", ""
            ),
            "policy_planning_context": final_state.get(
                "policy_planning_context", ""
            ),
            "web_fact_check_context": final_state.get(
                "web_fact_check_context", ""
            ),
            "knowledge_planet_context": final_state.get(
                "knowledge_planet_context", ""
            ),
            "baijiu_context": final_state.get(
                "baijiu_context", ""
            ),
            "compute_leasing_context": final_state.get(
                "compute_leasing_context", ""
            ),
            "dividend_defensive_context": final_state.get(
                "dividend_defensive_context", ""
            ),
            "building_materials_context": final_state.get(
                "building_materials_context", ""
            ),
            "consumer_staples_context": final_state.get(
                "consumer_staples_context", ""
            ),
            "optical_module_context": final_state.get(
                "optical_module_context", ""
            ),
            "biopharma_context": final_state.get(
                "biopharma_context", ""
            ),
            "software_context": final_state.get(
                "software_context", ""
            ),
            "insurance_context": final_state.get(
                "insurance_context", ""
            ),
            "medical_device_context": final_state.get(
                "medical_device_context", ""
            ),
            "metals_mining_context": final_state.get(
                "metals_mining_context", ""
            ),
            "data_coverage_context": final_state.get(
                "data_coverage_context", ""
            ),
            "market_report": final_state["market_report"],
            "sentiment_report": final_state["sentiment_report"],
            "news_report": final_state["news_report"],
            "fundamentals_report": final_state["fundamentals_report"],
            "investment_debate_state": {
                "bull_history": final_state["investment_debate_state"]["bull_history"],
                "bear_history": final_state["investment_debate_state"]["bear_history"],
                "history": final_state["investment_debate_state"]["history"],
                "current_response": final_state["investment_debate_state"][
                    "current_response"
                ],
                "judge_decision": final_state["investment_debate_state"][
                    "judge_decision"
                ],
            },
            "trader_investment_decision": final_state["trader_investment_plan"],
            "risk_debate_state": {
                "aggressive_history": final_state["risk_debate_state"]["aggressive_history"],
                "conservative_history": final_state["risk_debate_state"]["conservative_history"],
                "neutral_history": final_state["risk_debate_state"]["neutral_history"],
                "history": final_state["risk_debate_state"]["history"],
                "judge_decision": final_state["risk_debate_state"]["judge_decision"],
            },
            "investment_plan": final_state["investment_plan"],
            "final_trade_decision": final_state["final_trade_decision"],
        }

        # Save to file. Reject ticker values that would escape the
        # results directory when joined as a path component.
        safe_ticker = safe_ticker_component(self.ticker)
        directory = Path(self.config["results_dir"]) / safe_ticker / "TradingAgentsStrategy_logs"
        directory.mkdir(parents=True, exist_ok=True)

        log_path = directory / f"full_states_log_{trade_date}.json"
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(self.log_states_dict[str(trade_date)], f, indent=4)

    def process_signal(self, full_signal):
        """Process a signal to extract the core decision."""
        return self.signal_processor.process_signal(full_signal)
