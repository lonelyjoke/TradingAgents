"""Test checkpoint resume: crash mid-analysis, re-run resumes from last node."""

import sqlite3
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, StateGraph

from cli.main import _stream_graph_with_checkpoint
from tradingagents.graph.checkpointer import (
    checkpoint_step,
    clear_checkpoint,
    get_checkpointer,
    has_checkpoint,
    thread_id,
)
from tradingagents.graph.trading_graph import TradingAgentsGraph

# Mutable flag to simulate crash on first run
_should_crash = False


class _SimpleState(TypedDict):
    count: int


def _node_a(state: _SimpleState) -> dict:
    return {"count": state["count"] + 1}


def _node_b(state: _SimpleState) -> dict:
    if _should_crash:
        raise RuntimeError("simulated mid-analysis crash")
    return {"count": state["count"] + 10}


def _build_graph() -> StateGraph:
    builder = StateGraph(_SimpleState)
    builder.add_node("analyst", _node_a)
    builder.add_node("trader", _node_b)
    builder.set_entry_point("analyst")
    builder.add_edge("analyst", "trader")
    builder.add_edge("trader", END)
    return builder


class TestCheckpointResume(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.ticker = "TEST"
        self.date = "2026-04-20"

    def test_crash_and_resume(self):
        """Crash at 'trader' node, then resume from checkpoint."""
        global _should_crash
        builder = _build_graph()
        tid = thread_id(self.ticker, self.date)
        cfg = {"configurable": {"thread_id": tid}}

        # Run 1: crash at trader node
        _should_crash = True
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            with self.assertRaises(RuntimeError):
                graph.invoke({"count": 0}, config=cfg)

        # Checkpoint should exist at step 1 (analyst completed)
        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))
        step = checkpoint_step(self.tmpdir, self.ticker, self.date)
        self.assertEqual(step, 1)

        # Run 2: resume — trader succeeds this time
        _should_crash = False
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            result = graph.invoke(None, config=cfg)

        # analyst added 1, trader added 10 → 11
        self.assertEqual(result["count"], 11)

    def test_clear_checkpoint_allows_fresh_start(self):
        """After clearing, the graph starts from scratch."""
        global _should_crash
        builder = _build_graph()
        tid = thread_id(self.ticker, self.date)
        cfg = {"configurable": {"thread_id": tid}}

        # Create a checkpoint by crashing
        _should_crash = True
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            with self.assertRaises(RuntimeError):
                graph.invoke({"count": 0}, config=cfg)

        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))

        # Clear it
        clear_checkpoint(self.tmpdir, self.ticker, self.date)
        self.assertFalse(has_checkpoint(self.tmpdir, self.ticker, self.date))

        # Fresh run succeeds from scratch
        _should_crash = False
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            result = graph.invoke({"count": 0}, config=cfg)

        self.assertEqual(result["count"], 11)


    def test_different_date_starts_fresh(self):
        """A different date must NOT resume from an existing checkpoint."""
        global _should_crash
        builder = _build_graph()
        date2 = "2026-04-21"

        # Run with date1 — crash to leave a checkpoint
        _should_crash = True
        tid1 = thread_id(self.ticker, self.date)
        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            with self.assertRaises(RuntimeError):
                graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid1}})

        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))

        # date2 should have no checkpoint
        self.assertFalse(has_checkpoint(self.tmpdir, self.ticker, date2))

        # Run with date2 — should start fresh and succeed
        _should_crash = False
        tid2 = thread_id(self.ticker, date2)
        self.assertNotEqual(tid1, tid2)

        with get_checkpointer(self.tmpdir, self.ticker) as saver:
            graph = builder.compile(checkpointer=saver)
            result = graph.invoke({"count": 0}, config={"configurable": {"thread_id": tid2}})

        # Fresh run: analyst +1, trader +10 = 11
        self.assertEqual(result["count"], 11)

        # Original date checkpoint still exists (untouched)
        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))

    def test_cli_stream_retains_failed_checkpoint_and_resumes_with_none_input(self):
        """The interactive CLI wrapper must implement the same resume contract."""
        global _should_crash

        class _GraphWrapper:
            def __init__(self, workflow):
                self.workflow = workflow
                self.graph = workflow.compile()

        graph = _GraphWrapper(_build_graph())
        args = {"stream_mode": "values"}
        config = {
            "checkpoint_enabled": True,
            "data_cache_dir": self.tmpdir,
        }
        failures = []

        _should_crash = True
        with self.assertRaises(RuntimeError):
            list(
                _stream_graph_with_checkpoint(
                    graph,
                    {"count": 0},
                    args,
                    config=config,
                    ticker=self.ticker,
                    analysis_date=self.date,
                    on_error=failures.append,
                )
            )

        self.assertEqual(len(failures), 1)
        self.assertTrue(has_checkpoint(self.tmpdir, self.ticker, self.date))

        _should_crash = False
        chunks = list(
            _stream_graph_with_checkpoint(
                graph,
                None,
                args,
                config=config,
                ticker=self.ticker,
                analysis_date=self.date,
            )
        )

        self.assertEqual(chunks[-1]["count"], 11)
        self.assertFalse(has_checkpoint(self.tmpdir, self.ticker, self.date))

    def test_programmatic_resume_skips_paid_context_rebuild(self):
        graph = TradingAgentsGraph.__new__(TradingAgentsGraph)
        graph.config = {"checkpoint_enabled": True}
        graph.propagator = SimpleNamespace(get_graph_args=lambda: {"stream_mode": "values"})
        graph._run_a_share_data_preflight = lambda *_args: self.fail(
            "resume must not repeat preflight or context preparation"
        )
        captured = {}

        def execute(company_name, trade_date, graph_input, args):
            captured.update(
                company_name=company_name,
                trade_date=trade_date,
                graph_input=graph_input,
                args=args,
            )
            return "resumed"

        graph._execute_graph = execute

        result = graph._run_graph(self.ticker, self.date, resume=True)

        self.assertEqual(result, "resumed")
        self.assertIsNone(captured["graph_input"])
        self.assertEqual(
            captured["args"]["config"]["configurable"]["thread_id"],
            thread_id(self.ticker, self.date),
        )


if __name__ == "__main__":
    unittest.main()
