from tradingagents.dataflows import tushare_client


class FakePro:
    pass


def test_local_proxy_url_is_not_used_as_tushare_http_gateway(monkeypatch):
    monkeypatch.setattr(tushare_client, "_load_env", lambda: None)
    monkeypatch.setenv("TUSHARE_TOKEN", "x" * 64)
    monkeypatch.setenv("TUSHARE_HTTP_URL", "http://127.0.0.1:7890")
    monkeypatch.setenv("TUSHARE_DISABLE_OFFICIAL_FALLBACK", "true")

    class FakeTushare:
        def pro_api(self, token):
            assert token == "x" * 64
            return FakePro()

    monkeypatch.setitem(__import__("sys").modules, "tushare", FakeTushare())

    clients = list(tushare_client.get_tushare_pro_clients())

    assert len(clients) == 1
    assert clients[0][0] == "official"
    assert not hasattr(clients[0][1], "_DataApi__http_url")


def test_custom_gateway_still_uses_configured_http_url(monkeypatch):
    monkeypatch.setattr(tushare_client, "_load_env", lambda: None)
    monkeypatch.setenv("TUSHARE_TOKEN", "x" * 64)
    monkeypatch.setenv("TUSHARE_HTTP_URL", "http://example.com/tushare")
    monkeypatch.setenv("TUSHARE_DISABLE_OFFICIAL_FALLBACK", "true")

    class FakeTushare:
        def pro_api(self, token):
            assert token == "x" * 64
            return FakePro()

    monkeypatch.setitem(__import__("sys").modules, "tushare", FakeTushare())

    clients = list(tushare_client.get_tushare_pro_clients())

    assert len(clients) == 1
    assert clients[0][0] == "configured_http_url"
    assert clients[0][1]._DataApi__http_url == "http://example.com/tushare/"


def test_pro_bar_uses_shared_configured_client(monkeypatch):
    monkeypatch.setattr(tushare_client, "_load_env", lambda: None)
    monkeypatch.setenv("TUSHARE_TOKEN", "x" * 64)
    monkeypatch.setenv("TUSHARE_HTTP_URL", "https://tt.dailyfetch.top/")

    class FakeTushare:
        def pro_api(self, token):
            assert token == "x" * 64
            return FakePro()

        def pro_bar(self, **kwargs):
            return kwargs

    monkeypatch.setitem(__import__("sys").modules, "tushare", FakeTushare())

    result = tushare_client.get_tushare_pro_bar(ts_code="000001.SZ", limit=3)

    assert result["ts_code"] == "000001.SZ"
    assert result["limit"] == 3
    assert result["api"]._DataApi__http_url == "https://tt.dailyfetch.top/"


def test_custom_gateway_does_not_try_official_fallback_by_default(monkeypatch):
    monkeypatch.setattr(tushare_client, "_load_env", lambda: None)
    monkeypatch.setenv("TUSHARE_TOKEN", "x" * 64)
    monkeypatch.setenv("TUSHARE_HTTP_URL", "http://example.com/tushare")
    monkeypatch.delenv("TUSHARE_DISABLE_OFFICIAL_FALLBACK", raising=False)
    monkeypatch.delenv("TUSHARE_ENABLE_OFFICIAL_FALLBACK", raising=False)

    class FakeTushare:
        def pro_api(self, token):
            return FakePro()

    monkeypatch.setitem(__import__("sys").modules, "tushare", FakeTushare())

    clients = list(tushare_client.get_tushare_pro_clients())

    assert [name for name, _ in clients] == ["configured_http_url"]


def test_custom_gateway_official_fallback_is_explicit_opt_in(monkeypatch):
    monkeypatch.setattr(tushare_client, "_load_env", lambda: None)
    monkeypatch.setenv("TUSHARE_TOKEN", "x" * 64)
    monkeypatch.setenv("TUSHARE_HTTP_URL", "http://example.com/tushare")
    monkeypatch.setenv("TUSHARE_ENABLE_OFFICIAL_FALLBACK", "true")

    class FakeTushare:
        def pro_api(self, token):
            return FakePro()

    monkeypatch.setitem(__import__("sys").modules, "tushare", FakeTushare())

    clients = list(tushare_client.get_tushare_pro_clients())

    assert [name for name, _ in clients] == ["configured_http_url", "official"]


def test_fallback_env_loader_overrides_stale_process_token(monkeypatch, tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("TUSHARE_TOKEN=" + "y" * 56 + "\n", encoding="utf-8")
    monkeypatch.setenv("TUSHARE_TOKEN", "x" * 16)

    loaded = tushare_client._load_env_file(env_file, override=True)
    monkeypatch.setattr(tushare_client, "_load_env", lambda: None)

    assert loaded is True
    assert tushare_client.get_tushare_token() == "y" * 56


def test_very_short_tushare_token_fails_before_api_call(monkeypatch):
    monkeypatch.setattr(tushare_client, "_load_env", lambda: None)
    monkeypatch.setenv("TUSHARE_TOKEN", "x" * 16)

    try:
        tushare_client.get_tushare_token()
    except tushare_client.TushareClientError as exc:
        assert "length is 16" in str(exc)
        assert "expected at least 32" in str(exc)
    else:
        raise AssertionError("Expected short token to fail fast.")
