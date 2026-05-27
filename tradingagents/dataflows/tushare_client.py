from __future__ import annotations

import os
from typing import Iterable


class TushareClientError(RuntimeError):
    """Raised when the Tushare client cannot be initialized."""


def _load_env() -> None:
    try:
        from dotenv import load_dotenv

        # Prefer the project .env over an already-open shell session so users
        # can switch Tushare tokens without restarting PowerShell.
        load_dotenv(override=True)
    except ImportError:
        pass


def get_tushare_token() -> str:
    """Read the Tushare token from environment or .env."""
    _load_env()
    token = os.getenv("TUSHARE_TOKEN")
    if not token:
        raise TushareClientError(
            "TUSHARE_TOKEN is not configured. Set it in the current shell or .env."
        )
    return token


def get_tushare_pro_client():
    """Create a Tushare pro client using the shared local configuration.

    Supported environment variables:
    - TUSHARE_TOKEN: required API token.
    - TUSHARE_HTTP_URL: optional custom Tushare-compatible gateway.

    Some shared/proxied Tushare deployments require overriding the private
    DataApi endpoint after creating the client. Keep that detail in one place
    so the dataflow modules do not need to duplicate it.
    """
    try:
        import tushare as ts
    except ImportError as exc:
        raise TushareClientError(
            "The tushare package is not installed. Install it with: "
            "python -m pip install tushare"
        ) from exc

    pro = ts.pro_api(get_tushare_token())
    http_url = os.getenv("TUSHARE_HTTP_URL")
    if http_url:
        pro._DataApi__http_url = http_url.rstrip("/") + "/"
    return pro


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
    if http_url:
        configured._DataApi__http_url = http_url.rstrip("/") + "/"
        clients.append(("configured_http_url", configured))
    else:
        clients.append(("official", configured))

    fallback_enabled = os.getenv("TUSHARE_DISABLE_OFFICIAL_FALLBACK", "").lower() not in {
        "1",
        "true",
        "yes",
    }
    if http_url and fallback_enabled:
        clients.append(("official", ts.pro_api(token)))

    return clients
