import importlib


def test_default_config_reads_llm_env_overrides(monkeypatch):
    monkeypatch.setenv("TRADINGAGENTS_LLM_PROVIDER", "deepseek")
    monkeypatch.setenv("TRADINGAGENTS_DEEP_THINK_LLM", "deepseek-v4-pro")
    monkeypatch.setenv("TRADINGAGENTS_QUICK_THINK_LLM", "deepseek-v4-flash")
    monkeypatch.setenv("TRADINGAGENTS_BACKEND_URL", "https://api.deepseek.com")

    import tradingagents.default_config as default_config

    reloaded = importlib.reload(default_config)
    config = reloaded.DEFAULT_CONFIG

    assert config["llm_provider"] == "deepseek"
    assert config["deep_think_llm"] == "deepseek-v4-pro"
    assert config["quick_think_llm"] == "deepseek-v4-flash"
    assert config["backend_url"] == "https://api.deepseek.com"


def test_default_config_infers_deepseek_when_only_deepseek_key_exists(monkeypatch):
    monkeypatch.delenv("TRADINGAGENTS_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("TRADINGAGENTS_DEEP_THINK_LLM", raising=False)
    monkeypatch.delenv("TRADINGAGENTS_QUICK_THINK_LLM", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("DEEPSEEK_API_KEY", "placeholder")

    import tradingagents.default_config as default_config

    reloaded = importlib.reload(default_config)
    config = reloaded.DEFAULT_CONFIG

    assert config["llm_provider"] == "deepseek"
    assert config["deep_think_llm"] == "deepseek-v4-pro"
    assert config["quick_think_llm"] == "deepseek-v4-flash"


def test_default_config_loads_repo_dotenv_without_manual_load(monkeypatch):
    monkeypatch.delenv("TRADINGAGENTS_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("TRADINGAGENTS_DEEP_THINK_LLM", raising=False)
    monkeypatch.delenv("TRADINGAGENTS_QUICK_THINK_LLM", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)

    import dotenv

    def fake_load_dotenv(path, override=False):
        if str(path).endswith(".env"):
            monkeypatch.setenv("DEEPSEEK_API_KEY", "placeholder")
        return True

    monkeypatch.setattr(dotenv, "load_dotenv", fake_load_dotenv)

    import tradingagents.default_config as default_config

    reloaded = importlib.reload(default_config)
    config = reloaded.DEFAULT_CONFIG

    assert config["llm_provider"] == "deepseek"
