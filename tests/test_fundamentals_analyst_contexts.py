from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableLambda

from tradingagents.agents.analysts.fundamentals_analyst import (
    create_fundamentals_analyst,
)
from tradingagents.dataflows.prompt_compaction import _CONTEXT_KEYS


FUNDAMENTALS_ANALYST_PATH = (
    Path(__file__).resolve().parents[1]
    / "tradingagents"
    / "agents"
    / "analysts"
    / "fundamentals_analyst.py"
)


def test_fundamentals_analyst_uses_official_contexts_and_coverage_audit():
    source = FUNDAMENTALS_ANALYST_PATH.read_text(encoding="utf-8")

    assert "raw_investor_interaction_context" in source
    assert "raw_policy_planning_context" in source
    assert "investor_interaction_context = prompt_contexts" in source
    assert "policy_planning_context = prompt_contexts" in source
    assert "data_coverage_context = prompt_contexts" in source
    assert "get_investor_interaction_context" in source
    assert "get_policy_planning_context" in source
    assert "Precomputed official investor-interaction context" in source
    assert "Precomputed official policy-planning context" in source
    assert "Precomputed data coverage audit" in source


class _CapturingLLM(RunnableLambda):
    def __init__(self, func=None):
        super().__init__(func or (lambda _prompt: AIMessage(content="fundamentals memo")))
        self.bound_tools = []

    def bind_tools(self, tools):
        self.bound_tools = list(tools)
        return self


def test_precomputed_dossier_filters_unhashable_core_tools_without_crashing():
    llm = _CapturingLLM()
    state = {
        "trade_date": "2026-08-01",
        "company_of_interest": "600426.SH",
        "messages": [HumanMessage(content="600426.SH")],
        "structured_research_context": {
            "schema_version": 3,
            "company_summary": "华鲁恒升测试资料",
        },
    }
    for key in _CONTEXT_KEYS:
        state[key] = "precomputed context"

    # Leave one specialist context absent so the node still binds a tool after
    # removing the duplicated core financial tools.
    state["shipping_context"] = ""

    result = create_fundamentals_analyst(llm)(state)

    assert result["fundamentals_report"] == "fundamentals memo"
    bound_names = {tool.name for tool in llm.bound_tools}
    assert "get_shipping_context" in bound_names
    assert "get_fundamentals" not in bound_names
    assert "get_balance_sheet" not in bound_names
    assert "get_cashflow" not in bound_names
    assert "get_income_statement" not in bound_names


def test_unrelated_gated_sector_playbooks_are_not_injected_into_prompt():
    captured = {}

    def respond(prompt):
        captured["system"] = prompt.to_messages()[0].content
        return AIMessage(content="fundamentals memo")

    llm = _CapturingLLM(respond)
    state = {
        "trade_date": "2026-08-01",
        "company_of_interest": "600426.SH",
        "messages": [HumanMessage(content="600426.SH")],
        "structured_research_context": {"schema_version": 3},
    }
    for key in _CONTEXT_KEYS:
        state[key] = "- Status: not_applicable\n- Reason: unrelated sector"

    create_fundamentals_analyst(llm)(state)

    assert "No sector-specific playbook was triggered" in captured["system"]
    assert "Compute-Leasing Discipline" not in captured["system"]
    assert "AI Optical-Module Verification" not in captured["system"]
