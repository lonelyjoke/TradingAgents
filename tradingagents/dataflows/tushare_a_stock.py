from __future__ import annotations

from datetime import datetime
from typing import Annotated

import pandas as pd
from dateutil.relativedelta import relativedelta

from .tushare_client import TushareClientError, get_tushare_pro_client


class TushareDataError(RuntimeError):
    """Raised when Tushare cannot provide the requested A-share data."""


INDICATOR_DESCRIPTIONS = {
    "close_50_sma": (
        "50 SMA: A medium-term trend indicator. Usage: Identify trend direction "
        "and serve as dynamic support/resistance. Tips: It lags price; combine "
        "with faster indicators for timely signals."
    ),
    "close_200_sma": (
        "200 SMA: A long-term trend benchmark. Usage: Confirm overall market "
        "trend and identify golden/death cross setups. Tips: It reacts slowly; "
        "best for strategic trend confirmation rather than frequent trading entries."
    ),
    "close_10_ema": (
        "10 EMA: A responsive short-term average. Usage: Capture quick shifts "
        "in momentum and potential entry points. Tips: Prone to noise in choppy "
        "markets; use alongside longer averages for filtering false signals."
    ),
    "macd": (
        "MACD: Computes momentum via differences of EMAs. Usage: Look for "
        "crossovers and divergence as signals of trend changes. Tips: Confirm "
        "with other indicators in low-volatility or sideways markets."
    ),
    "macds": (
        "MACD Signal: An EMA smoothing of the MACD line. Usage: Use crossovers "
        "with the MACD line to trigger trades. Tips: Should be part of a broader "
        "strategy to avoid false positives."
    ),
    "macdh": (
        "MACD Histogram: Shows the gap between the MACD line and its signal. "
        "Usage: Visualize momentum strength and spot divergence early. Tips: "
        "Can be volatile; complement with additional filters in fast-moving markets."
    ),
    "rsi": (
        "RSI: Measures momentum to flag overbought/oversold conditions. Usage: "
        "Apply 70/30 thresholds and watch for divergence to signal reversals. "
        "Tips: In strong trends, RSI may remain extreme; always cross-check "
        "with trend analysis."
    ),
    "boll": (
        "Bollinger Middle: A 20 SMA serving as the basis for Bollinger Bands. "
        "Usage: Acts as a dynamic benchmark for price movement."
    ),
    "boll_ub": (
        "Bollinger Upper Band: Typically 2 standard deviations above the middle "
        "line. Usage: Signals potential overbought conditions and breakout zones."
    ),
    "boll_lb": (
        "Bollinger Lower Band: Typically 2 standard deviations below the middle "
        "line. Usage: Indicates potential oversold conditions."
    ),
    "atr": (
        "ATR: Averages true range to measure volatility. Usage: Set stop-loss "
        "levels and adjust position sizes based on current market volatility."
    ),
    "vwma": (
        "VWMA: A moving average weighted by volume. Usage: Confirm trends by "
        "integrating price action with volume data."
    ),
    "mfi": (
        "MFI: The Money Flow Index uses both price and volume to measure buying "
        "and selling pressure. Usage: Identify overbought or oversold conditions."
    ),
}


def is_a_share_symbol(symbol: str) -> bool:
    """Return True for common Tushare A-share symbols such as 000001.SZ."""
    upper = symbol.strip().upper()
    return upper.endswith((".SZ", ".SH", ".BJ"))


def _to_tushare_date(date_str: str) -> str:
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y%m%d")


def _get_pro_client():
    try:
        return get_tushare_pro_client()
    except TushareClientError as exc:
        raise TushareDataError(str(exc)) from exc


def _format_value(value, suffix: str = "") -> str:
    if value is None or pd.isna(value):
        return "N/A"
    if isinstance(value, float):
        rendered = f"{value:.4f}".rstrip("0").rstrip(".")
    else:
        rendered = str(value)
    return rendered + suffix


def _format_yyyymmdd(value) -> str:
    text = str(value or "")
    if len(text) == 8 and text.isdigit():
        return f"{text[:4]}-{text[4:6]}-{text[6:]}"
    return text or "N/A"


def _safe_query(description: str, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        return TushareDataError(f"{description} unavailable: {exc}")


def _sort_latest_reports(data: pd.DataFrame, curr_date: str | None, freq: str, limit: int = 8) -> pd.DataFrame:
    if data is None or data.empty:
        return pd.DataFrame()

    reports = data.copy()
    if "end_date" in reports.columns:
        reports["end_date"] = reports["end_date"].astype(str)
        if curr_date:
            cutoff = _to_tushare_date(curr_date)
            reports = reports[reports["end_date"] <= cutoff]
        if freq == "annual":
            reports = reports[reports["end_date"].str.endswith("1231")]
        reports = reports.sort_values("end_date", ascending=False)
        reports = reports.drop_duplicates(subset=["end_date"], keep="first")
    elif "ann_date" in reports.columns:
        reports = reports.sort_values("ann_date", ascending=False)

    return reports.head(limit)


def _query_financial_api(api_name: str, symbol: str, curr_date: str | None, fields: list[str], years: int = 6) -> pd.DataFrame:
    pro = _get_pro_client()
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start = (end_dt - relativedelta(years=years)).strftime("%Y%m%d")
    end = end_dt.strftime("%Y%m%d")

    query = getattr(pro, api_name)
    field_string = ",".join(fields)
    try:
        return query(ts_code=symbol, start_date=start, end_date=end, fields=field_string)
    except Exception:
        # Some shared gateways or Tushare versions are picky about fields. Fall
        # back to the default field set, then select what we can use locally.
        return query(ts_code=symbol, start_date=start, end_date=end)


def _select_existing(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    existing = [col for col in columns if col in data.columns]
    return data[existing].copy() if existing else pd.DataFrame()


def _format_dataframe_report(title: str, data: pd.DataFrame, value_columns: list[str]) -> str:
    if data.empty:
        return f"# {title}\n\nNo data returned."

    cols = [col for col in ["ts_code", "ann_date", "end_date"] + value_columns if col in data.columns]
    rendered = data[cols].copy()
    for col in rendered.columns:
        if col not in {"ts_code", "ann_date", "end_date"}:
            numeric = pd.to_numeric(rendered[col], errors="coerce")
            if not numeric.isna().all():
                rendered[col] = numeric

    return f"# {title}\n\n" + _markdown_table(rendered)


def _markdown_table(data: pd.DataFrame) -> str:
    if data.empty:
        return "No data returned."
    rows = ["| " + " | ".join(map(str, data.columns)) + " |"]
    rows.append("| " + " | ".join(["---"] * len(data.columns)) + " |")
    for _, row in data.iterrows():
        values = []
        for value in row:
            if value is None or pd.isna(value):
                values.append("N/A")
            elif isinstance(value, float):
                values.append(f"{value:.4f}".rstrip("0").rstrip("."))
            else:
                values.append(str(value))
        rows.append("| " + " | ".join(values) + " |")
    return "\n".join(rows)


def _fetch_fina_indicator(symbol: str, curr_date: str | None) -> pd.DataFrame:
    fields = [
        "ts_code",
        "ann_date",
        "end_date",
        "eps",
        "dt_eps",
        "bps",
        "ocfps",
        "grossprofit_margin",
        "netprofit_margin",
        "roe",
        "roe_waa",
        "roe_dt",
        "roa",
        "roic",
        "debt_to_assets",
        "current_ratio",
        "quick_ratio",
        "ocf_to_or",
        "ocf_to_opincome",
        "salescash_to_or",
        "or_yoy",
        "netprofit_yoy",
        "profit_dedt",
    ]
    data = _query_financial_api("fina_indicator", symbol, curr_date, fields)
    return _sort_latest_reports(data, curr_date, "quarterly", limit=8)


def _fetch_income_statement_data(
    symbol: str, curr_date: str | None, freq: str = "quarterly", limit: int = 8
) -> pd.DataFrame:
    fields = [
        "ts_code",
        "ann_date",
        "end_date",
        "basic_eps",
        "diluted_eps",
        "total_revenue",
        "revenue",
        "total_cogs",
        "operate_profit",
        "total_profit",
        "n_income",
        "n_income_attr_p",
        "sell_exp",
        "admin_exp",
        "fin_exp",
        "rd_exp",
        "ebit",
        "ebitda",
    ]
    data = _query_financial_api("income", symbol, curr_date, fields)
    return _sort_latest_reports(data, curr_date, freq, limit=limit)


def _fetch_balance_sheet_data(
    symbol: str, curr_date: str | None, freq: str = "quarterly", limit: int = 8
) -> pd.DataFrame:
    fields = [
        "ts_code",
        "ann_date",
        "end_date",
        "total_assets",
        "total_liab",
        "total_hldr_eqy_exc_min_int",
        "total_hldr_eqy_inc_min_int",
        "money_cap",
        "notes_receiv",
        "accounts_receiv",
        "oth_receiv",
        "prepayment",
        "inventories",
        "contract_assets",
        "fix_assets",
        "goodwill",
        "st_borr",
        "lt_borr",
        "bond_payable",
        "notes_payable",
        "acct_payable",
        "oth_payable",
        "adv_receipts",
        "contract_liab",
        "total_cur_assets",
        "total_cur_liab",
    ]
    data = _query_financial_api("balancesheet", symbol, curr_date, fields)
    return _sort_latest_reports(data, curr_date, freq, limit=limit)


def _fetch_cashflow_data(
    symbol: str, curr_date: str | None, freq: str = "quarterly", limit: int = 8
) -> pd.DataFrame:
    fields = [
        "ts_code",
        "ann_date",
        "end_date",
        "net_profit",
        "finan_exp",
        "c_fr_sale_sg",
        "recp_tax_rends",
        "n_cashflow_act",
        "st_cash_out_act",
        "c_pay_acq_const_fiolta",
        "c_recp_disp_fiolta",
        "c_pay_dist_dpcp_int_exp",
        "n_cashflow_inv_act",
        "n_cashflow_fin_act",
        "c_cash_equ_beg_period",
        "c_cash_equ_end_period",
    ]
    data = _query_financial_api("cashflow", symbol, curr_date, fields)
    return _sort_latest_reports(data, curr_date, freq, limit=limit)


def _matching_report_row(data: pd.DataFrame | TushareDataError, end_date: str) -> pd.Series:
    if isinstance(data, TushareDataError) or data is None or data.empty or "end_date" not in data.columns:
        return pd.Series(dtype="object")
    matches = data[data["end_date"].astype(str) == str(end_date)]
    if matches.empty:
        return pd.Series(dtype="object")
    return matches.iloc[0]


def _numeric_value(row: pd.Series, *columns: str) -> float | None:
    for col in columns:
        if col in row.index:
            value = pd.to_numeric(pd.Series([row.get(col)]), errors="coerce").iloc[0]
            if not pd.isna(value):
                return float(value)
    return None


def _safe_ratio(numerator: float | None, denominator: float | None, multiplier: float = 100.0) -> float | None:
    if numerator is None or denominator is None:
        return None
    if pd.isna(numerator) or pd.isna(denominator) or denominator == 0:
        return None
    return numerator / denominator * multiplier


def _derive_financial_metrics(
    income: pd.DataFrame | TushareDataError,
    balance: pd.DataFrame | TushareDataError,
    cashflow: pd.DataFrame | TushareDataError,
    fina_indicator: pd.DataFrame | TushareDataError,
) -> pd.DataFrame:
    if isinstance(income, TushareDataError) or income is None or income.empty:
        return pd.DataFrame()

    rows = []
    for _, inc in income.iterrows():
        end_date = str(inc.get("end_date", ""))
        bal = _matching_report_row(balance, end_date)
        cf = _matching_report_row(cashflow, end_date)
        ind = _matching_report_row(fina_indicator, end_date)

        revenue = _numeric_value(inc, "revenue", "total_revenue")
        # Balance-sheet items are stock measures while revenue is a flow
        # measure. Annualize interim-period revenue before comparing the two,
        # otherwise Q1 working-capital ratios look mechanically inflated.
        annualization_factor = 1.0
        if end_date.endswith("0331"):
            annualization_factor = 4.0
        elif end_date.endswith("0630"):
            annualization_factor = 2.0
        elif end_date.endswith("0930"):
            annualization_factor = 4.0 / 3.0
        revenue_for_stock_ratios = None if revenue is None else revenue * annualization_factor
        total_cogs = _numeric_value(inc, "total_cogs")
        operating_profit = _numeric_value(inc, "operate_profit")
        net_profit_parent = _numeric_value(inc, "n_income_attr_p", "n_income")
        net_profit_cf = _numeric_value(cf, "net_profit")
        operating_cash_flow = _numeric_value(cf, "n_cashflow_act")
        total_assets = _numeric_value(bal, "total_assets")
        total_liab = _numeric_value(bal, "total_liab")
        equity = _numeric_value(bal, "total_hldr_eqy_inc_min_int", "total_hldr_eqy_exc_min_int")
        receivables = sum(
            value or 0
            for value in [
                _numeric_value(bal, "notes_receiv"),
                _numeric_value(bal, "accounts_receiv"),
                _numeric_value(bal, "oth_receiv"),
            ]
        )
        inventories = _numeric_value(bal, "inventories")
        contract_assets = _numeric_value(bal, "contract_assets")
        contract_like_liab = sum(
            value or 0
            for value in [
                _numeric_value(bal, "contract_liab"),
                _numeric_value(bal, "adv_receipts"),
            ]
        )
        interest_bearing_debt = sum(
            value or 0
            for value in [
                _numeric_value(bal, "st_borr"),
                _numeric_value(bal, "lt_borr"),
                _numeric_value(bal, "bond_payable"),
            ]
        )
        payables = sum(
            value or 0
            for value in [
                _numeric_value(bal, "notes_payable"),
                _numeric_value(bal, "acct_payable"),
                _numeric_value(bal, "oth_payable"),
            ]
        )
        money_cap = _numeric_value(bal, "money_cap")
        total_cur_assets = _numeric_value(bal, "total_cur_assets")
        total_cur_liab = _numeric_value(bal, "total_cur_liab")

        rows.append(
            {
                "end_date": end_date,
                "ann_date": inc.get("ann_date"),
                "revenue_base": revenue,
                "reported_gross_margin": _numeric_value(ind, "grossprofit_margin"),
                "derived_gross_margin": _safe_ratio(
                    None if revenue is None or total_cogs is None else revenue - total_cogs,
                    revenue,
                ),
                "derived_operating_margin": _safe_ratio(operating_profit, revenue),
                "derived_net_margin": _safe_ratio(net_profit_parent, revenue),
                "selling_expense_ratio": _safe_ratio(_numeric_value(inc, "sell_exp"), revenue),
                "admin_expense_ratio": _safe_ratio(_numeric_value(inc, "admin_exp"), revenue),
                "rd_expense_ratio": _safe_ratio(_numeric_value(inc, "rd_exp"), revenue),
                "finance_expense_ratio": _safe_ratio(_numeric_value(inc, "fin_exp"), revenue),
                "ocf_to_net_profit": _safe_ratio(
                    operating_cash_flow,
                    net_profit_parent if net_profit_parent is not None else net_profit_cf,
                    multiplier=1.0,
                ),
                "ocf_to_revenue": _safe_ratio(operating_cash_flow, revenue),
                "debt_to_assets_derived": _safe_ratio(total_liab, total_assets),
                "cash_to_assets": _safe_ratio(money_cap, total_assets),
                "net_cash": None if money_cap is None else money_cap - interest_bearing_debt,
                "working_capital": (
                    None if total_cur_assets is None or total_cur_liab is None else total_cur_assets - total_cur_liab
                ),
                "contract_like_liab": contract_like_liab,
                "contract_like_liab_to_revenue": _safe_ratio(contract_like_liab, revenue_for_stock_ratios),
                "receivables_to_revenue": _safe_ratio(receivables, revenue_for_stock_ratios),
                "inventory_to_revenue": _safe_ratio(inventories, revenue_for_stock_ratios),
                "contract_assets_to_revenue": _safe_ratio(contract_assets, revenue_for_stock_ratios),
                "prepayment_to_revenue": _safe_ratio(_numeric_value(bal, "prepayment"), revenue_for_stock_ratios),
                "payables_to_cogs": _safe_ratio(payables, total_cogs),
                "goodwill_to_assets": _safe_ratio(_numeric_value(bal, "goodwill"), total_assets),
                "equity_multiplier": _safe_ratio(total_assets, equity, multiplier=1.0),
            }
        )

    derived = pd.DataFrame(rows)
    for col in ["contract_like_liab", "receivables_to_revenue", "inventory_to_revenue"]:
        if col in derived.columns:
            prev = pd.to_numeric(derived[col].shift(-1), errors="coerce")
            curr = pd.to_numeric(derived[col], errors="coerce")
            derived[f"{col}_seq_change"] = (curr / prev - 1) * 100

    return derived


def _fetch_index_daily(ts_code: str, curr_date: str, lookback_days: int = 45) -> pd.DataFrame:
    pro = _get_pro_client()
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start = (end_dt - relativedelta(days=lookback_days)).strftime("%Y%m%d")
    end = end_dt.strftime("%Y%m%d")
    data = pro.index_daily(ts_code=ts_code, start_date=start, end_date=end)
    if data is None or data.empty:
        return pd.DataFrame()
    return data.sort_values("trade_date")


def _pct_change_over_window(data: pd.DataFrame) -> str:
    if data is None or data.empty or "close" not in data.columns or len(data) < 2:
        return "N/A"
    close = pd.to_numeric(data["close"], errors="coerce").dropna()
    if len(close) < 2 or close.iloc[0] == 0:
        return "N/A"
    pct = (close.iloc[-1] / close.iloc[0] - 1) * 100
    return f"{pct:.2f}%"


def _market_context(curr_date: str) -> str:
    indexes = {
        "000001.SH": "SSE Composite",
        "000300.SH": "CSI 300",
        "000905.SH": "CSI 500",
        "399006.SZ": "ChiNext Index",
    }
    lines = ["## Market And Industry Context", "", "| Index | Recent Change |", "| --- | ---: |"]
    for code, name in indexes.items():
        result = _safe_query(f"index_daily {code}", _fetch_index_daily, code, curr_date)
        if isinstance(result, TushareDataError):
            lines.append(f"| {name} ({code}) | unavailable |")
        else:
            lines.append(f"| {name} ({code}) | {_pct_change_over_window(result)} |")

    pro = _get_pro_client()
    trade_date = _to_tushare_date(curr_date)
    sw_daily = _safe_query(
        "sw_daily",
        pro.sw_daily,
        trade_date=trade_date,
        fields="ts_code,trade_date,name,close,pct_change",
        limit=8,
    )
    if isinstance(sw_daily, TushareDataError):
        lines.extend(["", f"SW industry snapshot unavailable: {sw_daily}"])
    elif sw_daily is not None and not sw_daily.empty:
        lines.extend(["", "Recent SW industry snapshot:", ""])
        lines.append(_markdown_table(sw_daily[["ts_code", "name", "close", "pct_change"]]))

    return "\n".join(lines)


_STOCK_BASIC_CACHE: dict[str, pd.Series | None] = {}


def _fetch_stock_basic(symbol: str) -> pd.Series | None:
    cached = _STOCK_BASIC_CACHE.get(symbol)
    if cached is not None:
        return cached.copy()
    if symbol in _STOCK_BASIC_CACHE:
        return None

    pro = _get_pro_client()
    data = pro.stock_basic(
        ts_code=symbol,
        fields="ts_code,symbol,name,area,industry,market,exchange,list_date",
    )
    if data is None or data.empty:
        _STOCK_BASIC_CACHE[symbol] = None
        return None
    row = data.iloc[0].copy()
    _STOCK_BASIC_CACHE[symbol] = row
    return row.copy()


def _fetch_daily_basic_latest(symbol: str, curr_date: str) -> pd.Series | None:
    pro = _get_pro_client()
    curr_date_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start = (curr_date_dt - relativedelta(days=14)).strftime("%Y%m%d")
    end = curr_date_dt.strftime("%Y%m%d")
    fields = ",".join(
        [
            "ts_code",
            "trade_date",
            "close",
            "turnover_rate",
            "turnover_rate_f",
            "volume_ratio",
            "pe",
            "pe_ttm",
            "pb",
            "ps",
            "ps_ttm",
            "dv_ratio",
            "dv_ttm",
            "total_share",
            "float_share",
            "free_share",
            "total_mv",
            "circ_mv",
        ]
    )
    data = pro.daily_basic(ts_code=symbol, start_date=start, end_date=end, fields=fields)
    if data is None or data.empty:
        return None
    data = data.sort_values("trade_date", ascending=False)
    return data.iloc[0]


def _fetch_daily(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    symbol = symbol.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare A-share vendor expects symbols like 000001.SZ, 600519.SH, "
            f"or 920001.BJ; got {symbol!r}."
        )

    start = _to_tushare_date(start_date)
    end = _to_tushare_date(end_date)

    pro = _get_pro_client()
    data = pro.daily(ts_code=symbol, start_date=start, end_date=end)

    if data is None or data.empty:
        return pd.DataFrame()

    data = data.rename(
        columns={
            "trade_date": "Date",
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "vol": "Volume",
            "amount": "Amount",
        }
    )
    data["Date"] = pd.to_datetime(data["Date"], format="%Y%m%d", errors="coerce")
    data = data.dropna(subset=["Date"]).sort_values("Date")

    keep_cols = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Amount",
        "pre_close",
        "change",
        "pct_chg",
    ]
    keep_cols = [col for col in keep_cols if col in data.columns]
    data = data[keep_cols].copy()

    numeric_cols = [col for col in data.columns if col != "Date"]
    data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors="coerce")

    return data


def get_stock(
    symbol: Annotated[str, "A-share ticker symbol, e.g. 000001.SZ or 600519.SH"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
) -> str:
    """Return Tushare A-share daily OHLCV data as a CSV string."""
    data = _fetch_daily(symbol, start_date, end_date)
    if data.empty:
        return f"No Tushare daily data found for symbol '{symbol}' between {start_date} and {end_date}"

    rounded = data.copy()
    for col in ["Open", "High", "Low", "Close", "Amount", "pre_close", "change", "pct_chg"]:
        if col in rounded.columns:
            rounded[col] = rounded[col].round(4)

    header = f"# Tushare A-share daily data for {symbol.upper()} from {start_date} to {end_date}\n"
    header += f"# Total records: {len(rounded)}\n"
    header += f"# Data retrieved on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return header + rounded.to_csv(index=False)


def get_indicator(
    symbol: Annotated[str, "A-share ticker symbol, e.g. 000001.SZ or 600519.SH"],
    indicator: Annotated[str, "technical indicator name"],
    curr_date: Annotated[str, "The current trading date, YYYY-mm-dd"],
    look_back_days: Annotated[int, "how many calendar days to look back"],
) -> str:
    """Calculate stockstats indicators from Tushare daily OHLCV data."""
    from dateutil.relativedelta import relativedelta
    from stockstats import wrap

    indicator = indicator.strip().lower()
    if indicator not in INDICATOR_DESCRIPTIONS:
        raise ValueError(
            f"Indicator {indicator} is not supported. Please choose from: {list(INDICATOR_DESCRIPTIONS.keys())}"
        )

    curr_date_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    before = curr_date_dt - relativedelta(days=look_back_days)

    # Fetch extra history so longer indicators like 50/200 SMA have enough context.
    history_start = curr_date_dt - relativedelta(days=max(look_back_days + 260, 320))
    data = _fetch_daily(symbol, history_start.strftime("%Y-%m-%d"), curr_date)
    if data.empty:
        return f"No Tushare daily data found for {symbol} before {curr_date}"

    stats_data = data.rename(
        columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
        }
    )
    df = wrap(stats_data[["Date", "open", "high", "low", "close", "volume"]].copy())
    df[indicator]
    df["Date"] = pd.to_datetime(df["Date"])
    window = df[(df["Date"] >= before) & (df["Date"] <= curr_date_dt)]

    ind_string = ""
    for _, row in window.iterrows():
        value = row[indicator]
        rendered = "N/A" if pd.isna(value) else str(value)
        ind_string += f"{row['Date'].strftime('%Y-%m-%d')}: {rendered}\n"

    if not ind_string:
        ind_string = "No trading data available for the specified date range.\n"

    return (
        f"## {indicator} values from {before.strftime('%Y-%m-%d')} to {curr_date}:\n\n"
        + ind_string
        + "\n\n"
        + INDICATOR_DESCRIPTIONS[indicator]
    )


def get_fundamentals(
    ticker: Annotated[str, "A-share ticker symbol, e.g. 000001.SZ or 600519.SH"],
    curr_date: Annotated[str, "Current date in yyyy-mm-dd format"] = None,
) -> str:
    """Return an A-share company profile and valuation snapshot from Tushare."""
    symbol = ticker.strip().upper()
    if not is_a_share_symbol(symbol):
        raise TushareDataError(
            f"Tushare fundamentals expects A-share symbols like 000001.SZ or 600519.SH; got {ticker!r}."
        )
    if not curr_date:
        curr_date = datetime.now().strftime("%Y-%m-%d")

    basic = _fetch_stock_basic(symbol)
    daily_basic = _fetch_daily_basic_latest(symbol, curr_date)
    fina_indicator = _safe_query(
        "fina_indicator", _fetch_fina_indicator, symbol, curr_date
    )
    income_data = _safe_query("income", _fetch_income_statement_data, symbol, curr_date)
    balance_data = _safe_query("balancesheet", _fetch_balance_sheet_data, symbol, curr_date)
    cashflow_data = _safe_query("cashflow", _fetch_cashflow_data, symbol, curr_date)
    derived_metrics = _derive_financial_metrics(
        income_data, balance_data, cashflow_data, fina_indicator
    )

    if basic is None and daily_basic is None:
        return f"No Tushare fundamentals data found for {symbol} as of {curr_date}."

    lines = [f"# Tushare A-share fundamentals for {symbol} as of {curr_date}", ""]

    if basic is not None:
        lines.extend(
            [
                "## Company Profile",
                f"- Name: {_format_value(basic.get('name'))}",
                f"- Area: {_format_value(basic.get('area'))}",
                f"- Industry: {_format_value(basic.get('industry'))}",
                f"- Market: {_format_value(basic.get('market'))}",
                f"- Exchange: {_format_value(basic.get('exchange'))}",
                f"- List Date: {_format_yyyymmdd(basic.get('list_date'))}",
                "",
            ]
        )

    if daily_basic is not None:
        total_mv = daily_basic.get("total_mv")
        circ_mv = daily_basic.get("circ_mv")
        lines.extend(
            [
                "## Valuation And Trading Snapshot",
                f"- Snapshot Trade Date: {_format_yyyymmdd(daily_basic.get('trade_date'))}",
                f"- Close: {_format_value(daily_basic.get('close'))}",
                f"- PE: {_format_value(daily_basic.get('pe'))}",
                f"- PE TTM: {_format_value(daily_basic.get('pe_ttm'))}",
                f"- PB: {_format_value(daily_basic.get('pb'))}",
                f"- PS: {_format_value(daily_basic.get('ps'))}",
                f"- PS TTM: {_format_value(daily_basic.get('ps_ttm'))}",
                f"- Dividend Yield: {_format_value(daily_basic.get('dv_ratio'), '%')}",
                f"- Dividend Yield TTM: {_format_value(daily_basic.get('dv_ttm'), '%')}",
                f"- Turnover Rate: {_format_value(daily_basic.get('turnover_rate'), '%')}",
                f"- Free-float Turnover Rate: {_format_value(daily_basic.get('turnover_rate_f'), '%')}",
                f"- Volume Ratio: {_format_value(daily_basic.get('volume_ratio'))}",
                f"- Total Market Value: {_format_value(total_mv)} ten-thousand CNY",
                f"- Circulating Market Value: {_format_value(circ_mv)} ten-thousand CNY",
                "",
                "## Key Metrics Table",
                "| Metric | Value |",
                "| --- | ---: |",
                f"| Close | {_format_value(daily_basic.get('close'))} |",
                f"| PE TTM | {_format_value(daily_basic.get('pe_ttm'))} |",
                f"| PB | {_format_value(daily_basic.get('pb'))} |",
                f"| PS TTM | {_format_value(daily_basic.get('ps_ttm'))} |",
                f"| Turnover Rate | {_format_value(daily_basic.get('turnover_rate'), '%')} |",
                f"| Total Market Value | {_format_value(total_mv)} ten-thousand CNY |",
                f"| Circulating Market Value | {_format_value(circ_mv)} ten-thousand CNY |",
            ]
        )

    if isinstance(fina_indicator, TushareDataError):
        lines.extend(["", f"## Financial Quality", str(fina_indicator)])
    elif fina_indicator is not None and not fina_indicator.empty:
        latest = fina_indicator.iloc[0]
        lines.extend(
            [
                "",
                "## Financial Quality Snapshot",
                f"- Latest Financial Period: {_format_yyyymmdd(latest.get('end_date'))}",
                f"- Announcement Date: {_format_yyyymmdd(latest.get('ann_date'))}",
                f"- EPS: {_format_value(latest.get('eps'))}",
                f"- Book Value Per Share: {_format_value(latest.get('bps'))}",
                f"- Operating Cash Flow Per Share: {_format_value(latest.get('ocfps'))}",
                f"- Gross Profit Margin: {_format_value(latest.get('grossprofit_margin'), '%')}",
                f"- Net Profit Margin: {_format_value(latest.get('netprofit_margin'), '%')}",
                f"- ROE: {_format_value(latest.get('roe'), '%')}",
                f"- ROE Weighted Average: {_format_value(latest.get('roe_waa'), '%')}",
                f"- ROA: {_format_value(latest.get('roa'), '%')}",
                f"- ROIC: {_format_value(latest.get('roic'), '%')}",
                f"- Debt To Assets: {_format_value(latest.get('debt_to_assets'), '%')}",
                f"- Current Ratio: {_format_value(latest.get('current_ratio'))}",
                f"- Quick Ratio: {_format_value(latest.get('quick_ratio'))}",
                f"- Revenue YoY: {_format_value(latest.get('or_yoy'), '%')}",
                f"- Net Profit YoY: {_format_value(latest.get('netprofit_yoy'), '%')}",
                "",
                "## Recent Financial Indicator Trend",
            ]
        )
        trend_cols = [
            "end_date",
            "eps",
            "roe",
            "roa",
            "grossprofit_margin",
            "netprofit_margin",
            "debt_to_assets",
            "or_yoy",
            "netprofit_yoy",
        ]
        lines.append(_markdown_table(_select_existing(fina_indicator, trend_cols)))

    if not derived_metrics.empty:
        latest_derived = derived_metrics.iloc[0]
        derived_cols = [
            "end_date",
            "revenue_base",
            "reported_gross_margin",
            "derived_gross_margin",
            "derived_operating_margin",
            "derived_net_margin",
            "selling_expense_ratio",
            "admin_expense_ratio",
            "rd_expense_ratio",
            "finance_expense_ratio",
            "ocf_to_net_profit",
            "debt_to_assets_derived",
            "cash_to_assets",
            "net_cash",
            "working_capital",
            "contract_like_liab",
            "contract_like_liab_to_revenue",
            "contract_like_liab_seq_change",
            "receivables_to_revenue",
            "receivables_to_revenue_seq_change",
            "inventory_to_revenue",
            "inventory_to_revenue_seq_change",
            "prepayment_to_revenue",
            "payables_to_cogs",
            "goodwill_to_assets",
        ]
        lines.extend(
            [
                "",
                "## Derived Financial Metrics",
                "These ratios are calculated from Tushare income statement, balance sheet, and cash flow fields when ready-made financial indicators are missing. Treat interim-report income and cash-flow items as period-to-date unless separately adjusted.",
                "Forward-looking accounting signals use contract liabilities/advance receipts, receivables, inventories, prepayments, payables, goodwill, net cash, and working capital to infer possible order visibility, collection pressure, stocking risk, upstream locking, bargaining power, impairment risk, and balance-sheet resilience.",
                "",
                "### Latest Derived Snapshot",
                f"- Derived Gross Margin: {_format_value(latest_derived.get('derived_gross_margin'), '%')}",
                f"- Derived Operating Margin: {_format_value(latest_derived.get('derived_operating_margin'), '%')}",
                f"- Derived Net Margin: {_format_value(latest_derived.get('derived_net_margin'), '%')}",
                f"- Operating Cash Flow / Net Profit: {_format_value(latest_derived.get('ocf_to_net_profit'))}",
                f"- Derived Debt To Assets: {_format_value(latest_derived.get('debt_to_assets_derived'), '%')}",
                f"- Contract Liabilities + Advance Receipts / Revenue: {_format_value(latest_derived.get('contract_like_liab_to_revenue'), '%')}",
                f"- Receivables / Revenue: {_format_value(latest_derived.get('receivables_to_revenue'), '%')}",
                f"- Inventory / Revenue: {_format_value(latest_derived.get('inventory_to_revenue'), '%')}",
                f"- Payables / COGS: {_format_value(latest_derived.get('payables_to_cogs'), '%')}",
                "",
                "### Recent Derived Metric Trend",
                _markdown_table(_select_existing(derived_metrics, derived_cols)),
            ]
        )

    lines.extend(["", _market_context(curr_date)])

    return "\n".join(lines)


def get_balance_sheet(ticker: str, freq: str = "quarterly", curr_date: str = None) -> str:
    symbol = ticker.strip().upper()
    fields = [
        "ts_code",
        "ann_date",
        "end_date",
        "total_assets",
        "total_liab",
        "total_hldr_eqy_exc_min_int",
        "total_hldr_eqy_inc_min_int",
        "money_cap",
        "notes_receiv",
        "accounts_receiv",
        "oth_receiv",
        "prepayment",
        "inventories",
        "contract_assets",
        "fix_assets",
        "goodwill",
        "st_borr",
        "lt_borr",
        "bond_payable",
        "notes_payable",
        "acct_payable",
        "oth_payable",
        "adv_receipts",
        "contract_liab",
        "total_cur_assets",
        "total_cur_liab",
    ]
    data = _fetch_balance_sheet_data(symbol, curr_date, freq=freq, limit=8)
    value_cols = [col for col in fields if col not in {"ts_code", "ann_date", "end_date"}]
    return _format_dataframe_report(f"Tushare balance sheet for {symbol}", data, value_cols)


def get_cashflow(ticker: str, freq: str = "quarterly", curr_date: str = None) -> str:
    symbol = ticker.strip().upper()
    fields = [
        "ts_code",
        "ann_date",
        "end_date",
        "net_profit",
        "finan_exp",
        "c_fr_sale_sg",
        "recp_tax_rends",
        "n_cashflow_act",
        "st_cash_out_act",
        "n_cashflow_inv_act",
        "n_cashflow_fin_act",
        "c_cash_equ_beg_period",
        "c_cash_equ_end_period",
    ]
    data = _fetch_cashflow_data(symbol, curr_date, freq=freq, limit=8)
    value_cols = [col for col in fields if col not in {"ts_code", "ann_date", "end_date"}]
    return _format_dataframe_report(f"Tushare cash flow statement for {symbol}", data, value_cols)


def get_income_statement(ticker: str, freq: str = "quarterly", curr_date: str = None) -> str:
    symbol = ticker.strip().upper()
    fields = [
        "ts_code",
        "ann_date",
        "end_date",
        "basic_eps",
        "diluted_eps",
        "total_revenue",
        "revenue",
        "total_cogs",
        "operate_profit",
        "total_profit",
        "n_income",
        "n_income_attr_p",
        "sell_exp",
        "admin_exp",
        "fin_exp",
        "rd_exp",
        "ebit",
        "ebitda",
    ]
    data = _fetch_income_statement_data(symbol, curr_date, freq=freq, limit=8)
    value_cols = [col for col in fields if col not in {"ts_code", "ann_date", "end_date"}]
    return _format_dataframe_report(f"Tushare income statement for {symbol}", data, value_cols)
