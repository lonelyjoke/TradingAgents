import sys
import types

if "langchain_core.messages" not in sys.modules:
    langchain_core = types.ModuleType("langchain_core")
    messages = types.ModuleType("langchain_core.messages")

    class AIMessage:
        pass

    messages.AIMessage = AIMessage
    sys.modules["langchain_core"] = langchain_core
    sys.modules["langchain_core.messages"] = messages

if "langchain_openai" not in sys.modules:
    langchain_openai = types.ModuleType("langchain_openai")

    class ChatOpenAI:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def invoke(self, input, config=None, **kwargs):
            return input

        def with_structured_output(self, schema, *, method=None, **kwargs):
            return self

    langchain_openai.ChatOpenAI = ChatOpenAI
    sys.modules["langchain_openai"] = langchain_openai

from tradingagents.llm_clients import openai_client
from tradingagents.llm_clients.openai_client import OpenAIClient


def test_openai_client_forwards_timeout_retries_and_proxy(monkeypatch):
    captured = {}

    class DummyChatOpenAI:
        def __init__(self, **kwargs):
            captured.update(kwargs)

    monkeypatch.setattr(openai_client, "NormalizedChatOpenAI", DummyChatOpenAI)

    client = OpenAIClient(
        "gpt-5.4",
        provider="openai",
        timeout=123,
        max_retries=4,
        proxy="http://127.0.0.1:7890",
    )
    client.get_llm()

    assert captured["timeout"] == 123
    assert captured["max_retries"] == 4
    assert captured["use_responses_api"] is True
    assert "http_client" in captured
    assert "http_async_client" in captured
