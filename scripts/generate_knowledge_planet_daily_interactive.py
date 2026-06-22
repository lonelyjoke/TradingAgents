"""Menu launcher for Knowledge Planet theme-trading daily reports."""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_SCRIPT = REPO_ROOT / "scripts" / "generate_knowledge_planet_daily.py"

sys.path.insert(0, str(REPO_ROOT))

try:
    import questionary
except Exception:  # pragma: no cover - terminal fallback
    questionary = None

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except Exception:  # pragma: no cover - terminal fallback
    Console = None
    Panel = None
    Table = None

try:
    from tradingagents.llm_clients.model_catalog import MODEL_OPTIONS, get_model_options
    from tradingagents.dataflows.knowledge_planet_research import DAILY_ANALYSIS_TARGETS
except Exception:  # pragma: no cover - terminal fallback
    MODEL_OPTIONS = {}
    get_model_options = None
    DAILY_ANALYSIS_TARGETS = 15


console = Console() if Console else None


@dataclass(frozen=True)
class ProviderOption:
    label: str
    provider: str
    base_url: str | None
    default_model: str


PROVIDERS = [
    ProviderOption("DeepSeek", "deepseek", "https://api.deepseek.com", "deepseek-chat"),
    ProviderOption("OpenAI", "openai", "https://api.openai.com/v1", "gpt-5.4"),
    ProviderOption("Qwen", "qwen", "https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen3.6-plus"),
    ProviderOption("GLM", "glm", "https://open.bigmodel.cn/api/paas/v4/", "glm-5.1"),
    ProviderOption("OpenRouter", "openrouter", "https://openrouter.ai/api/v1", "openai/gpt-5.4"),
    ProviderOption("Ollama 本地模型", "ollama", "http://localhost:11434/v1", "qwen3:latest"),
]


RUN_MODES = [
    (
        "完整版：观点源 + Tushare 基本面/技术面 + LLM 交易逻辑拆解（推荐）",
        "full",
    ),
    (
        "标准版：观点源 + Tushare 基本面/技术面，不调用 LLM",
        "market",
    ),
    (
        "快速预览：只整理观点源，不做 Tushare/LLM",
        "fast",
    ),
]


def _date_is_valid(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def _print_header() -> None:
    title = "知识星球题材交易日报"
    body = (
        "选择截至日期、回溯窗口和模型后，系统会先同步/读取知识星球资料，"
        "再生成本地日报。分析层固定输出主榜10个、观察榜5个，完整版会对15个候选做交易逻辑拆解。"
    )
    if console and Panel:
        console.print(Panel(body, title=title, border_style="cyan"))
    else:
        print(title)
        print("=" * 48)
        print(body)
        print()


def _text(prompt: str, default: str, validate=None) -> str:
    if questionary:
        answer = questionary.text(
            prompt,
            default=default,
            validate=validate or (lambda text: bool(text.strip()) or "不能为空"),
        ).ask()
        if answer is None:
            raise KeyboardInterrupt
        return answer.strip() or default

    while True:
        raw = input(f"{prompt} [{default}]: ").strip() or default
        if validate:
            result = validate(raw)
            if result is True:
                return raw
            print(result if isinstance(result, str) else "输入不合法")
            continue
        return raw


def _int(prompt: str, default: int, minimum: int = 0, maximum: int | None = None) -> int:
    def validate(raw: str) -> bool | str:
        try:
            value = int(raw)
        except ValueError:
            return "请输入整数"
        if value < minimum:
            return f"不能小于 {minimum}"
        if maximum is not None and value > maximum:
            return f"不能大于 {maximum}"
        return True

    return int(_text(prompt, str(default), validate))


def _select(prompt: str, choices: list[tuple[str, Any]], default: Any | None = None) -> Any:
    if questionary:
        selected = questionary.select(
            prompt,
            choices=[
                questionary.Choice(label, value=value)
                for label, value in choices
            ],
            default=default,
        ).ask()
        if selected is None:
            raise KeyboardInterrupt
        return selected

    print(prompt)
    for index, (label, _) in enumerate(choices, start=1):
        print(f"  {index}. {label}")
    while True:
        raw = input("请选择序号: ").strip()
        if not raw and default is not None:
            return default
        try:
            index = int(raw)
        except ValueError:
            print("请输入序号")
            continue
        if 1 <= index <= len(choices):
            return choices[index - 1][1]
        print("序号超出范围")


def _confirm(prompt: str, default: bool = True) -> bool:
    if questionary:
        answer = questionary.confirm(prompt, default=default).ask()
        if answer is None:
            raise KeyboardInterrupt
        return bool(answer)

    suffix = "Y/n" if default else "y/N"
    raw = input(f"{prompt} [{suffix}]: ").strip().lower()
    if not raw:
        return default
    return raw in {"y", "yes", "1", "true", "是", "好", "确定"}


def _select_model(provider: ProviderOption) -> str:
    if provider.provider == "openrouter":
        return _text(
            "请输入 OpenRouter 模型 ID",
            provider.default_model,
        )
    if provider.provider not in MODEL_OPTIONS or get_model_options is None:
        return _text("请输入模型 ID", provider.default_model)

    choices = get_model_options(provider.provider, "deep")
    if not any(value == provider.default_model for _, value in choices):
        choices = [(provider.default_model, provider.default_model), *choices]
    model = _select(
        "请选择用于日报逻辑拆解的大模型",
        [(label, value) for label, value in choices],
        default=provider.default_model,
    )
    if model == "custom":
        return _text("请输入自定义模型 ID", provider.default_model)
    return model


def _show_summary(args: list[str], end_date: str, lookback_days: int, mode: str, provider: str | None, model: str | None) -> None:
    start_date = (
        datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=lookback_days)
    ).strftime("%Y-%m-%d")
    output = REPO_ROOT / "reports" / "knowledge_planet_daily" / end_date / "daily_report.md"

    if console and Table:
        table = Table(title="运行配置", show_header=True, header_style="bold cyan")
        table.add_column("项目", width=18)
        table.add_column("选择")
        table.add_row("信息窗口", f"{start_date} 至 {end_date}（含当天）")
        table.add_row("运行模式", mode)
        table.add_row("分析标的", f"固定 {DAILY_ANALYSIS_TARGETS} 个（主榜10 + 观察榜5）")
        table.add_row("LLM", f"{provider}/{model}" if provider and model else "不调用")
        table.add_row("输出文件", str(output))
        console.print(table)
        console.print("[dim]实际命令：[/dim] " + " ".join(args))
    else:
        print("运行配置")
        print(f"- 信息窗口: {start_date} 至 {end_date}（含当天）")
        print(f"- 运行模式: {mode}")
        print(f"- 分析标的: 固定 {DAILY_ANALYSIS_TARGETS} 个（主榜10 + 观察榜5）")
        print(f"- LLM: {provider}/{model}" if provider and model else "- LLM: 不调用")
        print(f"- 输出文件: {output}")
        print("实际命令: " + " ".join(args))
    print()


def main() -> int:
    _print_header()
    today = datetime.now().strftime("%Y-%m-%d")
    end_date = _text(
        "截至日期 YYYY-MM-DD（含当天）",
        today,
        lambda raw: _date_is_valid(raw.strip()) or "日期格式必须是 YYYY-MM-DD",
    )
    lookback_days = _int(
        "往前回溯几天（6 = 最近 7 天，含截至日期）",
        6,
        minimum=0,
        maximum=60,
    )
    mode = _select("请选择运行模式", RUN_MODES, default="full")

    provider_option: ProviderOption | None = None
    model: str | None = None
    base_url: str | None = None

    if mode == "full":
        provider_option = _select(
            "请选择大模型供应商",
            [(option.label, option) for option in PROVIDERS],
            default=PROVIDERS[0],
        )
        model = _select_model(provider_option)
        base_url = provider_option.base_url

    args = [
        sys.executable,
        str(REPORT_SCRIPT),
        "--date",
        end_date,
        "--lookback-days",
        str(lookback_days),
    ]
    if mode == "fast":
        args.append("--no-market-scoring")

    if mode == "full" and provider_option and model:
        args.extend(
            [
                "--llm-market-analysis",
                "--llm-provider",
                provider_option.provider,
                "--llm-model",
                model,
            ]
        )
        if base_url:
            args.extend(["--llm-base-url", base_url])

    mode_label = dict((value, label) for label, value in RUN_MODES)[mode]
    _show_summary(
        args,
        end_date=end_date,
        lookback_days=lookback_days,
        mode=mode_label,
        provider=provider_option.provider if provider_option else None,
        model=model,
    )

    if not _confirm("确认开始生成日报？", default=True):
        print("已取消。")
        return 1

    return subprocess.call(args, cwd=REPO_ROOT)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\n已取消。")
        raise SystemExit(130)
