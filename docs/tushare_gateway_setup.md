# Tushare Gateway Setup

The shared Tushare initialization lives in:

```python
from tradingagents.dataflows.tushare_client import (
    get_tushare_pro_bar,
    get_tushare_pro_client,
)
```

Use `get_tushare_pro_client()` for normal Pro API calls:

```python
pro = get_tushare_pro_client()
df = pro.index_basic(limit=5)
```

Use `get_tushare_pro_bar(...)` for `ts.pro_bar` calls. This wrapper always
passes the configured `api=pro` client:

```python
df = get_tushare_pro_bar(ts_code="000001.SZ", limit=3)
```

The project `.env` should contain:

```text
TUSHARE_TOKEN=your_token
TUSHARE_HTTP_URL=https://tt.dailyfetch.top/
TUSHARE_DISABLE_OFFICIAL_FALLBACK=true
```

Do not call `ts.pro_api(...)` or `ts.pro_bar(...)` directly in new dataflow
code. Import this file instead, so custom gateways keep using:

```python
pro._DataApi__http_url = "https://tt.dailyfetch.top/"
```
