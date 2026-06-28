"""Sync Knowledge Planet topics through zsxq-cli into the local inbox.

The script intentionally keeps the official zsxq-cli as the authentication and
API boundary. It writes a daily markdown stream that the existing
import_knowledge_planet.py importer can index.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = REPO_ROOT / "data" / "knowledge_planet"


@dataclass(frozen=True)
class ZsxqGroup:
    group_id: str
    name: str = ""


@dataclass
class AttachmentSyncResult:
    image_lines: list[str]
    file_lines: list[str]
    images_downloaded: int = 0
    images_ocr_ok: int = 0
    image_failures: int = 0
    files_downloaded: int = 0
    file_failures: int = 0


def _candidate_zsxq_cli_paths() -> list[Path]:
    paths: list[Path] = []
    appdata = os.getenv("APPDATA")
    if appdata:
        paths.append(Path(appdata) / "npm" / "zsxq-cli.cmd")
        paths.append(Path(appdata) / "npm" / "zsxq-cli")
    paths.append(Path("zsxq-cli"))
    return paths


def _find_zsxq_cli() -> str:
    for path in _candidate_zsxq_cli_paths():
        if path.name == "zsxq-cli" and path.parent == Path("."):
            return "zsxq-cli"
        if path.exists():
            return str(path)
    return "zsxq-cli"


def _command_env() -> dict[str, str]:
    env = os.environ.copy()
    additions: list[str] = []
    node_dir = Path(r"C:\Program Files\nodejs")
    appdata = os.getenv("APPDATA")
    if node_dir.exists():
        additions.append(str(node_dir))
    if appdata and (Path(appdata) / "npm").exists():
        additions.append(str(Path(appdata) / "npm"))
    if additions:
        env["PATH"] = ";".join(additions + [env.get("PATH", "")])
    return env


def _run_zsxq_json(args: list[str]) -> dict[str, Any]:
    command = [_find_zsxq_cli(), *args]
    completed = subprocess.run(
        command,
        cwd=str(REPO_ROOT),
        env=_command_env(),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        message = (completed.stderr or completed.stdout).strip()
        raise RuntimeError(message or f"zsxq-cli failed with exit code {completed.returncode}")
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"zsxq-cli did not return JSON: {completed.stdout[:500]}") from exc


def _get_file_download_url(file_id: str) -> str:
    if not file_id:
        return ""
    data = _run_zsxq_json(["api", "raw", "--method", "GET", "--path", f"/v2/files/{file_id}/download_url"])
    return str(data.get("download_url") or data.get("url") or "")


def _date_from_topic(topic: dict[str, Any]) -> str:
    raw = str(topic.get("create_time") or topic.get("createTime") or "")
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", raw)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return ""


def _plain_text(value: Any) -> str:
    text = str(value or "")
    text = re.sub(r"\r\n?", "\n", text)
    return text.strip()


def _sanitize_filename(value: str, fallback: str = "attachment") -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "_", str(value or "").strip())
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")
    return (cleaned or fallback)[:120]


def _unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    for idx in range(2, 10000):
        candidate = path.with_name(f"{stem}_{idx}{suffix}")
        if not candidate.exists():
            return candidate
    digest = hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:8]
    return path.with_name(f"{stem}_{digest}{suffix}")


def _suffix_from_url(url: str, fallback: str) -> str:
    parsed = urllib.parse.urlparse(url)
    suffix = Path(parsed.path).suffix.lower()
    if suffix and len(suffix) <= 8:
        return suffix
    return fallback


def _download_url(url: str, target: Path, timeout: int = 60) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 TradingAgents KnowledgePlanetSync/1.0",
            "Accept": "*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read()
    target.write_bytes(data)


def _run_windows_ocr(path: Path, language: str = "zh-Hans-CN") -> str:
    script = REPO_ROOT / "scripts" / "ocr_image_windows.ps1"
    if not script.exists():
        return ""
    completed = subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script),
            "-Path",
            str(path),
            "-Language",
            language,
        ],
        cwd=str(REPO_ROOT),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError((completed.stderr or completed.stdout).strip())
    text = completed.stdout.strip()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _topic_owner(topic: dict[str, Any]) -> str:
    owner = topic.get("owner") if isinstance(topic.get("owner"), dict) else {}
    return str(owner.get("name") or owner.get("alias") or "").strip()


def _topic_group(topic: dict[str, Any], fallback: ZsxqGroup) -> ZsxqGroup:
    group = topic.get("group") if isinstance(topic.get("group"), dict) else {}
    return ZsxqGroup(
        group_id=str(group.get("group_id") or fallback.group_id),
        name=str(group.get("name") or fallback.name),
    )


def _urls_from_images(topic: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    images = topic.get("images")
    if not isinstance(images, list):
        return urls
    for image in images:
        if not isinstance(image, dict):
            continue
        original = image.get("original") if isinstance(image.get("original"), dict) else {}
        large = image.get("large") if isinstance(image.get("large"), dict) else {}
        url = original.get("url") or large.get("url")
        if url:
            urls.append(str(url))
    return urls


def _file_url(file_obj: dict[str, Any]) -> str:
    for key in ("url", "download_url", "downloadUrl"):
        value = file_obj.get(key)
        if value:
            return str(value)
    for nested_key in ("file", "download", "original"):
        nested = file_obj.get(nested_key)
        if isinstance(nested, dict):
            for key in ("url", "download_url", "downloadUrl"):
                value = nested.get(key)
                if value:
                    return str(value)
    return ""


def _file_name(file_obj: dict[str, Any]) -> str:
    for key in ("name", "title", "file_name", "filename"):
        value = file_obj.get(key)
        if value:
            return str(value)
    return "attachment"


def _topic_attachment_stem(topic: dict[str, Any], idx: int) -> str:
    topic_id = str(topic.get("topic_id") or "topic")
    return f"{topic_id}_{idx:02d}"


def _sync_images(
    topic: dict[str, Any],
    *,
    root: Path,
    target_date: str,
    download: bool,
    ocr: bool,
    ocr_language: str,
    max_downloads: int | None,
) -> tuple[list[str], int, int, int]:
    lines: list[str] = []
    downloaded = 0
    ocr_ok = 0
    failures = 0
    image_urls = _urls_from_images(topic)
    if not image_urls:
        return lines, downloaded, ocr_ok, failures
    lines.append("Images:")
    image_dir = root / "attachments" / "images" / target_date
    ocr_dir = root / "attachments" / "ocr" / target_date
    for idx, url in enumerate(image_urls, start=1):
        local_text = ""
        ocr_text = ""
        can_download = download and (max_downloads is None or downloaded < max_downloads)
        if can_download:
            suffix = _suffix_from_url(url, ".jpg")
            target = _unique_path(image_dir / f"{_topic_attachment_stem(topic, idx)}{suffix}")
            try:
                _download_url(url, target)
                downloaded += 1
                local_text = f" local={target.relative_to(REPO_ROOT)}"
                if ocr:
                    try:
                        ocr_text = _run_windows_ocr(target, ocr_language)
                        if ocr_text:
                            ocr_ok += 1
                            ocr_dir.mkdir(parents=True, exist_ok=True)
                            ocr_path = ocr_dir / f"{target.stem}.txt"
                            ocr_path.write_text(ocr_text + "\n", encoding="utf-8")
                    except Exception as exc:
                        failures += 1
                        ocr_text = f"OCR unavailable: {exc}"
            except Exception as exc:
                failures += 1
                local_text = f" download_failed={str(exc).replace(chr(10), ' ')[:180]}"
        lines.append(f"- {url}{local_text}")
        if ocr_text:
            lines.extend(["", "Image OCR:", ocr_text, ""])
    return lines, downloaded, ocr_ok, failures


def _sync_files(
    topic: dict[str, Any],
    *,
    root: Path,
    target_date: str,
    download: bool,
    max_downloads: int | None,
) -> tuple[list[str], int, int]:
    lines: list[str] = []
    downloaded = 0
    failures = 0
    files = topic.get("files")
    if not isinstance(files, list):
        return lines, downloaded, failures
    if files:
        lines.append("Files:")
    for idx, file_obj in enumerate(files, start=1):
        if not isinstance(file_obj, dict):
            continue
        name = _file_name(file_obj)
        url = _file_url(file_obj)
        file_id = file_obj.get("file_id") or file_obj.get("id")
        if not url and file_id:
            try:
                url = _get_file_download_url(str(file_id))
            except Exception as exc:
                failures += 1
                url = ""
                local_text = f" download_url_failed={str(exc).replace(chr(10), ' ')[:180]}"
            else:
                local_text = ""
        else:
            local_text = ""
        can_download = download and bool(url) and (max_downloads is None or downloaded < max_downloads)
        if can_download:
            suffix = Path(_sanitize_filename(name)).suffix.lower() or _suffix_from_url(url, "")
            safe_name = _sanitize_filename(name, f"{_topic_attachment_stem(topic, idx)}{suffix or '.bin'}")
            if not Path(safe_name).suffix and suffix:
                safe_name = f"{safe_name}{suffix}"
            if safe_name.lower().endswith(".pdf") or ".pdf" in safe_name.lower():
                target_dir = root / "reports" / "inbox"
            else:
                target_dir = root / "attachments" / "files" / target_date
            target = _unique_path(target_dir / safe_name)
            try:
                _download_url(url, target)
                downloaded += 1
                local_text = f" local={target.relative_to(REPO_ROOT)}"
            except Exception as exc:
                failures += 1
                local_text = f" download_failed={str(exc).replace(chr(10), ' ')[:180]}"
        suffix_text = f" url={url}" if url else ""
        file_id_text = f" file_id={file_id}" if file_id else ""
        lines.append(f"- {name}{file_id_text}{suffix_text}{local_text}")
    return lines, downloaded, failures


def sync_topic_attachments(
    topic: dict[str, Any],
    *,
    root: Path,
    target_date: str,
    download_images: bool,
    ocr_images: bool,
    ocr_language: str,
    download_files: bool,
    max_image_downloads: int | None = None,
    max_file_downloads: int | None = None,
) -> AttachmentSyncResult:
    image_lines, images_downloaded, images_ocr_ok, image_failures = _sync_images(
        topic,
        root=root,
        target_date=target_date,
        download=download_images,
        ocr=ocr_images,
        ocr_language=ocr_language,
        max_downloads=max_image_downloads,
    )
    file_lines, files_downloaded, file_failures = _sync_files(
        topic,
        root=root,
        target_date=target_date,
        download=download_files,
        max_downloads=max_file_downloads,
    )
    return AttachmentSyncResult(
        image_lines=image_lines,
        file_lines=file_lines,
        images_downloaded=images_downloaded,
        images_ocr_ok=images_ocr_ok,
        image_failures=image_failures,
        files_downloaded=files_downloaded,
        file_failures=file_failures,
    )


def _format_topic_block(
    topic: dict[str, Any],
    fallback_group: ZsxqGroup,
    *,
    attachment_result: AttachmentSyncResult | None = None,
) -> str:
    group = _topic_group(topic, fallback_group)
    topic_id = str(topic.get("topic_id") or "")
    title = _plain_text(topic.get("title") or topic.get("content") or "Knowledge Planet Topic")
    content = _plain_text(topic.get("content"))
    author = _topic_owner(topic)
    create_time = str(topic.get("create_time") or "")
    annotation = _plain_text(topic.get("annotation"))
    lines = [
        f"# {title}",
        "",
        f"source: zsxq",
        f"group_id: {group.group_id}",
        f"group_name: {group.name}",
        f"topic_id: {topic_id}",
        f"author: {author}",
        f"published_at: {create_time}",
    ]
    if annotation:
        lines.append(f"annotation: {annotation}")
    lines.extend(["", content or title])

    if attachment_result and attachment_result.image_lines:
        lines.append("")
        lines.extend(attachment_result.image_lines)
    elif _urls_from_images(topic):
        lines.extend(["", "Images:"])
        lines.extend(f"- {url}" for url in _urls_from_images(topic))

    if attachment_result and attachment_result.file_lines:
        lines.append("")
        lines.extend(attachment_result.file_lines)

    return "\n".join(lines).strip()


class PaginationLimitReached(RuntimeError):
    """Raised when the requested date range was not fully reached."""


def fetch_topics_for_window(
    group: ZsxqGroup,
    start_date: str,
    end_date: str,
    *,
    limit_per_page: int,
    max_pages: int,
) -> list[dict[str, Any]]:
    topics: list[dict[str, Any]] = []
    end_time = ""
    oldest_date = ""
    has_more = False
    pages_scanned = 0
    for _page in range(max_pages):
        pages_scanned += 1
        args = [
            "group",
            "+topics",
            "--group-id",
            group.group_id,
            "--limit",
            str(limit_per_page),
            "--json",
        ]
        if end_time:
            args.extend(["--end-time", end_time])
        data = _run_zsxq_json(args)
        page_topics = data.get("topics_brief")
        if not isinstance(page_topics, list):
            page_topics = data.get("topics") if isinstance(data.get("topics"), list) else []
        if not page_topics:
            break

        for topic in page_topics:
            if not isinstance(topic, dict):
                continue
            topic_date = _date_from_topic(topic)
            if start_date <= topic_date <= end_date:
                topics.append(topic)

        oldest_date = _date_from_topic(page_topics[-1]) if isinstance(page_topics[-1], dict) else ""
        if oldest_date and oldest_date < start_date:
            break
        has_more = bool(data.get("has_more"))
        if not has_more:
            break
        end_time = str(data.get("next_end_time") or "")
        if not end_time:
            break
    else:
        if has_more and (not oldest_date or oldest_date >= start_date):
            raise PaginationLimitReached(
                "pagination limit reached before the requested window was fully covered: "
                f"pages={pages_scanned}, oldest_date={oldest_date or 'unknown'}, "
                f"requested={start_date}..{end_date}; increase --max-pages"
            )
    return topics


def fetch_topics_for_date(
    group: ZsxqGroup,
    target_date: str,
    *,
    limit_per_page: int,
    max_pages: int,
) -> list[dict[str, Any]]:
    return fetch_topics_for_window(
        group,
        target_date,
        target_date,
        limit_per_page=limit_per_page,
        max_pages=max_pages,
    )


def write_daily_markdown(
    groups: list[ZsxqGroup],
    topics_by_group: dict[str, list[dict[str, Any]]],
    target_date: str,
    output: Path,
    *,
    root: Path,
    download_images: bool,
    ocr_images: bool,
    ocr_language: str,
    download_files: bool,
    max_image_downloads: int | None,
    max_file_downloads: int | None,
) -> tuple[int, AttachmentSyncResult]:
    blocks: list[str] = [f"# {target_date} Knowledge Planet zsxq sync"]
    count = 0
    totals = AttachmentSyncResult(image_lines=[], file_lines=[])
    group_map = {group.group_id: group for group in groups}
    for group in groups:
        topics = topics_by_group.get(group.group_id, [])
        for topic in topics:
            topic_date = _date_from_topic(topic) or target_date[:10]
            image_remaining = (
                None
                if max_image_downloads is None
                else max(0, max_image_downloads - totals.images_downloaded)
            )
            file_remaining = (
                None
                if max_file_downloads is None
                else max(0, max_file_downloads - totals.files_downloaded)
            )
            attachment_result = sync_topic_attachments(
                topic,
                root=root,
                target_date=topic_date,
                download_images=download_images,
                ocr_images=ocr_images,
                ocr_language=ocr_language,
                download_files=download_files,
                max_image_downloads=image_remaining,
                max_file_downloads=file_remaining,
            )
            totals.images_downloaded += attachment_result.images_downloaded
            totals.images_ocr_ok += attachment_result.images_ocr_ok
            totals.image_failures += attachment_result.image_failures
            totals.files_downloaded += attachment_result.files_downloaded
            totals.file_failures += attachment_result.file_failures
            blocks.append("---")
            blocks.append(
                _format_topic_block(
                    topic,
                    group_map.get(group.group_id, group),
                    attachment_result=attachment_result,
                )
            )
            count += 1
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n\n".join(blocks).strip() + "\n", encoding="utf-8")
    return count, totals


def parse_group(value: str) -> ZsxqGroup:
    if ":" in value:
        group_id, name = value.split(":", 1)
        return ZsxqGroup(group_id=group_id.strip(), name=name.strip())
    return ZsxqGroup(group_id=value.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync zsxq topics into data/knowledge_planet/inbox.")
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"), help="Window end date, YYYY-MM-DD.")
    parser.add_argument(
        "--start-date",
        default=None,
        help="Optional window start date. Defaults to --date for a single-day sync.",
    )
    parser.add_argument(
        "--group-id",
        action="append",
        default=[],
        help="Group id to sync. Use id:name to keep a display name. Can be repeated.",
    )
    parser.add_argument("--limit-per-page", type=int, default=30, help="Topics per API page, max 30.")
    parser.add_argument("--max-pages", type=int, default=600, help="Maximum pages to scan per group.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Knowledge Planet data root.")
    parser.add_argument("--output", type=Path, default=None, help="Optional output markdown path.")
    parser.add_argument("--no-download-images", action="store_true", help="Do not download topic images.")
    parser.add_argument("--no-ocr-images", action="store_true", help="Do not run Windows OCR on downloaded images.")
    parser.add_argument("--ocr-language", default="zh-Hans-CN", help="Windows OCR language tag.")
    parser.add_argument("--no-download-files", action="store_true", help="Do not download topic file attachments.")
    parser.add_argument("--max-image-downloads", type=int, default=100, help="Maximum images to download in this run.")
    parser.add_argument("--max-file-downloads", type=int, default=50, help="Maximum file attachments to download in this run.")
    args = parser.parse_args()

    groups = [parse_group(value) for value in args.group_id if value.strip()]
    if not groups:
        raise SystemExit("Please pass at least one --group-id. Example: --group-id 28888112822211:前沿信息收录")

    start_date = str(args.start_date or args.date)
    end_date = str(args.date)
    if start_date > end_date:
        raise SystemExit("--start-date must be earlier than or equal to --date")
    output_name = (
        f"{end_date}_zsxq_sync.md"
        if start_date == end_date
        else f"{start_date}_to_{end_date}_zsxq_sync.md"
    )
    output = args.output or args.root / "inbox" / output_name
    topics_by_group: dict[str, list[dict[str, Any]]] = {}
    failures: list[str] = []
    for group in groups:
        try:
            topics = fetch_topics_for_window(
                group,
                start_date,
                end_date,
                limit_per_page=max(1, min(30, args.limit_per_page)),
                max_pages=max(1, args.max_pages),
            )
            topics_by_group[group.group_id] = topics
            print(
                f"{group.group_id} {group.name or ''}: {len(topics)} topic(s) "
                f"for {start_date}..{end_date}"
            )
        except Exception as exc:
            failures.append(f"{group.group_id} {group.name or ''}: {exc}")
            print(f"{group.group_id} {group.name or ''}: failed - {exc}")

    if failures and not topics_by_group:
        print("Sync failed before any complete group result was available; no stream file was written.")
        return 1

    count, attachment_totals = write_daily_markdown(
        groups,
        topics_by_group,
        end_date if start_date == end_date else f"{start_date}..{end_date}",
        output,
        root=args.root,
        download_images=not args.no_download_images,
        ocr_images=not args.no_ocr_images,
        ocr_language=args.ocr_language,
        download_files=not args.no_download_files,
        max_image_downloads=max(0, args.max_image_downloads),
        max_file_downloads=max(0, args.max_file_downloads),
    )
    print(f"wrote {count} topic(s) to {output}")
    print(
        "attachments: "
        f"images_downloaded={attachment_totals.images_downloaded}, "
        f"images_ocr_ok={attachment_totals.images_ocr_ok}, "
        f"image_failures={attachment_totals.image_failures}, "
        f"files_downloaded={attachment_totals.files_downloaded}, "
        f"file_failures={attachment_totals.file_failures}"
    )
    if failures:
        print("Some groups failed:")
        for failure in failures:
            print(f"- {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
