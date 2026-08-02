from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tradingagents.agents.utils.agent_utils import (
    build_instrument_context,
    get_focused_report_instruction,
    get_indicators,
    get_language_instruction,
    get_stock_data,
)
from tradingagents.dataflows.config import get_config
from tradingagents.dataflows.prompt_compaction import compact_state_fields
from tradingagents.dataflows.tushare_a_stock import is_a_share_symbol


def create_market_analyst(llm):

    def market_analyst_node(state):
        current_date = state["trade_date"]
        instrument_context = build_instrument_context(state["company_of_interest"])

        tools = [
            get_stock_data,
            get_indicators,
        ]
        is_a_share = is_a_share_symbol(state["company_of_interest"])
        prompt_contexts = compact_state_fields(
            state,
            profile="analyst",
            keys={
                "price_move_attribution_context",
                "intraday_behavior_context",
                "relative_strength_context",
                "market_expectation_context",
                "data_coverage_context",
            },
        )
        precomputed_market_context = "\n\n".join(
            f"### {label}\n{prompt_contexts[key]}"
            for key, label in (
                ("price_move_attribution_context", "Price-move attribution"),
                ("intraday_behavior_context", "Intraday behavior"),
                ("relative_strength_context", "Relative strength"),
                ("market_expectation_context", "Market expectation"),
                ("data_coverage_context", "Data coverage"),
            )
            if prompt_contexts.get(key)
        )
        use_precomputed = bool(
            is_a_share
            and precomputed_market_context
            and not get_config().get("a_share_agent_tool_requery_enabled", False)
        )
        if use_precomputed:
            tools = []
        data_access_instruction = (
            "The A-share market data was fetched and calculated before this agent started. "
            "Use the precomputed price, relative-strength, intraday and expectation evidence "
            "below directly; do not request the same data again."
            if use_precomputed
            else (
                "Call get_stock_data first to retrieve the CSV, then use get_indicators "
                "with the selected indicator names."
            )
        )

        system_message = (
            """You are a trading assistant tasked with analyzing financial markets. Your role is to select the **most relevant indicators** for a given market condition or trading strategy from the following list. The goal is to choose up to **8 indicators** that provide complementary insights without redundancy. Categories and each category's indicators are:

Moving Averages:
- close_50_sma: 50 SMA: A medium-term trend indicator. Usage: Identify trend direction and serve as dynamic support/resistance. Tips: It lags price; combine with faster indicators for timely signals.
- close_200_sma: 200 SMA: A long-term trend benchmark. Usage: Confirm overall market trend and identify golden/death cross setups. Tips: It reacts slowly; best for strategic trend confirmation rather than frequent trading entries.
- close_10_ema: 10 EMA: A responsive short-term average. Usage: Capture quick shifts in momentum and potential entry points. Tips: Prone to noise in choppy markets; use alongside longer averages for filtering false signals.

MACD Related:
- macd: MACD: Computes momentum via differences of EMAs. Usage: Look for crossovers and divergence as signals of trend changes. Tips: Confirm with other indicators in low-volatility or sideways markets.
- macds: MACD Signal: An EMA smoothing of the MACD line. Usage: Use crossovers with the MACD line to trigger trades. Tips: Should be part of a broader strategy to avoid false positives.
- macdh: MACD Histogram: Shows the gap between the MACD line and its signal. Usage: Visualize momentum strength and spot divergence early. Tips: Can be volatile; complement with additional filters in fast-moving markets.

Momentum Indicators:
- rsi: RSI: Measures momentum to flag overbought/oversold conditions. Usage: Apply 70/30 thresholds and watch for divergence to signal reversals. Tips: In strong trends, RSI may remain extreme; always cross-check with trend analysis.

Volatility Indicators:
- boll: Bollinger Middle: A 20 SMA serving as the basis for Bollinger Bands. Usage: Acts as a dynamic benchmark for price movement. Tips: Combine with the upper and lower bands to effectively spot breakouts or reversals.
- boll_ub: Bollinger Upper Band: Typically 2 standard deviations above the middle line. Usage: Signals potential overbought conditions and breakout zones. Tips: Confirm signals with other tools; prices may ride the band in strong trends.
- boll_lb: Bollinger Lower Band: Typically 2 standard deviations below the middle line. Usage: Indicates potential oversold conditions. Tips: Use additional analysis to avoid false reversal signals.
- atr: ATR: Averages true range to measure volatility. Usage: Set stop-loss levels and adjust position sizes based on current market volatility. Tips: It's a reactive measure, so use it as part of a broader risk management strategy.

Volume-Based Indicators:
- vwma: VWMA: A moving average weighted by volume. Usage: Confirm trends by integrating price action with volume data. Tips: Watch for skewed results from volume spikes; use in combination with other volume analyses.

- Select up to 5 non-redundant indicators that answer decision questions: trend, momentum, volatility, support/resistance, and volume confirmation. Avoid cataloging every signal. When you tool call, please use the exact name of the indicators provided above as they are defined parameters, otherwise your call will fail. """
            + data_access_instruction
            + " For exchange-qualified A-share tickers such as 600519.SH, treat unavailable OHLCV as a Tushare date-window, network, permission, or quota limitation; do not claim the data source lacks A-share coverage. Write a compact technical memo focused on whether price action confirms, contradicts, or merely times the fundamental thesis."
            + ("\n\nPrecomputed A-share market evidence:\n" + precomputed_market_context if use_precomputed else "")
            + """ Append a compact Markdown table only for trend, support/resistance, momentum, risk level, and trading implication."""
            + get_focused_report_instruction()
            + get_language_instruction()
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you are unable to fully answer, that's OK; another assistant with different tools"
                    " will help where you left off. Execute what you can to make progress."
                    " Your deliverable is an analyst memo only. Do not issue FINAL TRANSACTION PROPOSAL lines;"
                    " final trading actions are produced later by the Trader and Portfolio Manager."
                    " You have access to the following tools: {tool_names}.\n{system_message}"
                    "For your reference, the current date is {current_date}. {instrument_context}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(instrument_context=instrument_context)

        chain = prompt | (llm.bind_tools(tools) if tools else llm)

        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "market_report": report,
        }

    return market_analyst_node
