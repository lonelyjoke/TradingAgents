from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


MIN_TUSHARE_TOKEN_LENGTH = 32


class TushareClientError(RuntimeError):
    """Raised when the Tushare client cannot be initialized."""


def _load_env_file(path: Path, *, override: bool = True) -> bool:
    """Minimal .env loader used when python-dotenv is not installed."""
    if not path.exists():
        return False
    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            continue
        value = value.strip()
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]
        if override or key not in os.environ:
            os.environ[key] = value
    return True


def _load_env() -> None:
    cwd_env = Path.cwd() / ".env"
    repo_env = Path(__file__).resolve().parents[2] / ".env"
    try:
        from dotenv import load_dotenv

        # Prefer the project .env over an already-open shell session so users
        # can switch Tushare tokens without restarting PowerShell.
        if cwd_env.exists():
            load_dotenv(cwd_env, override=True)
        elif repo_env.exists():
            load_dotenv(repo_env, override=True)
        else:
            load_dotenv(override=True)
    except ImportError:
        _load_env_file(cwd_env, override=True) or _load_env_file(repo_env, override=True)


def get_tushare_token() -> str:
    """Read the Tushare token from environment or .env."""
    _load_env()
    token = (os.getenv("TUSHARE_TOKEN") or "").strip()
    if not token:
        raise TushareClientError(
            "TUSHARE_TOKEN is not configured. Set it in the current shell or .env."
        )
    if len(token) < MIN_TUSHARE_TOKEN_LENGTH:
        raise TushareClientError(
            "TUSHARE_TOKEN length is "
            f"{len(token)}, expected at least {MIN_TUSHARE_TOKEN_LENGTH}. "
            "The full token is not printed; update .env or clear the stale shell "
            "environment variable before running A-share research."
        )
    return token


def _is_probable_local_proxy_url(value: str | None) -> bool:
    """Return True when TUSHARE_HTTP_URL looks like a local VPN/proxy endpoint."""
    if not value:
        return False
    try:
        parsed = urlparse(value)
    except Exception:
        return False
    host = (parsed.hostname or "").lower()
    port = parsed.port
    return host in {"127.0.0.1", "localhost", "::1"} and port in {
        7890,
        7891,
        7897,
        1080,
        10809,
    }


def _env_flag(name: str) -> bool:
    return (os.getenv(name) or "").lower() in {"1", "true", "yes", "on"}


def _official_fallback_enabled(use_configured_gateway: bool) -> bool:
    if not use_configured_gateway:
        return False
    if _env_flag("TUSHARE_ENABLE_OFFICIAL_FALLBACK"):
        return True
    if _env_flag("TUSHARE_DISABLE_OFFICIAL_FALLBACK"):
        return False
    # Gateway tokens are often not valid on official api.waditu.com. Keep the
    # official endpoint opt-in to avoid repeated false "token invalid" errors.
    return False


def get_tushare_pro_client():
    """Create a Tushare pro client using the shared local configuration.

    Supported environment variables:
    - TUSHARE_TOKEN: required API token.
    - TUSHARE_HTTP_URL: optional custom Tushare-compatible gateway.

    Some shared/proxied Tushare deployments require overriding the private
    DataApi endpoint after creating the client, for example:

        pro = ts.pro_api(token)
        pro._DataApi__http_url = "https://tt.dailyfetch.top/"

    Keep that detail in one place so the dataflow modules do not need to
    duplicate it.
    """
    try:
        import tushare as ts
    except ImportError as exc:
        raise TushareClientError(
            "The tushare package is not installed. Install it with: "
            "python -m pip install tushare"
        ) from exc

    token = get_tushare_token()
    pro = ts.pro_api(token)
    pro._DataApi__token = token
    http_url = os.getenv("TUSHARE_HTTP_URL")
    if http_url and not _is_probable_local_proxy_url(http_url):
        pro._DataApi__http_url = http_url.rstrip("/")
    return pro


def get_tushare_pro_bar(**kwargs: Any):
    """Call ``ts.pro_bar`` with the shared configured pro client.

    Shared Tushare gateways often require ``ts.pro_bar(api=pro, ...)`` instead
    of letting ``pro_bar`` create its own official client. Use this wrapper for
    daily/minute/bar data so the configured gateway and token are always used.
    """
    try:
        import tushare as ts
    except ImportError as exc:
        raise TushareClientError(
            "The tushare package is not installed. Install it with: "
            "python -m pip install tushare"
        ) from exc

    kwargs.setdefault("api", get_tushare_pro_client())
    return ts.pro_bar(**kwargs)


def get_tushare_pro_clients() -> Iterable[tuple[str, object]]:
    """Return configured Tushare client plus official fallback when useful.

    A locally configured TUSHARE_HTTP_URL can be a proxy or shared gateway.
    Some gateways expose announcements but not daily/daily_basic/statement
    endpoints. Keep the configured gateway first, then try the official
    endpoint unless explicitly disabled.
    """
    _load_env()
    try:
        import tushare as ts
    except ImportError as exc:
        raise TushareClientError(
            "The tushare package is not installed. Install it with: "
            "python -m pip install tushare"
        ) from exc

    token = get_tushare_token()
    http_url = os.getenv("TUSHARE_HTTP_URL")
    clients: list[tuple[str, object]] = []

    configured = ts.pro_api(token)
    configured._DataApi__token = token
    use_configured_gateway = bool(http_url) and not _is_probable_local_proxy_url(http_url)
    if use_configured_gateway:
        configured._DataApi__http_url = http_url.rstrip("/")
        clients.append(("configured_http_url", configured))
    else:
        clients.append(("official", configured))

    if _official_fallback_enabled(use_configured_gateway):
        clients.append(("official", ts.pro_api(token)))

    return clients
