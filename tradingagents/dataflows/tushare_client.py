from __future__ import annotations

import os


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
