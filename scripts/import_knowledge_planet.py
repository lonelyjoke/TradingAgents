"""Import local Knowledge Planet notes and research-report PDFs.

This is intentionally local-first:

- Short posts go into data/knowledge_planet/inbox as .md or .txt files.
- PDF reports go into data/knowledge_planet/reports/inbox.
- The importer deduplicates, stores metadata in SQLite, and archives originals.

The first version uses deterministic rules only. LLM enrichment can be added on
top of this database later without changing the daily workflow.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = REPO_ROOT / "data" / "knowledge_planet"
STREAM_SKIP_FILES = {"README.md", "post_template.md", "daily_stream_template.md"}

BROKER_PATTERNS = [
    (r"Goldman|GS|\u9ad8\u76db", "Goldman Sachs", "GS"),
    (r"CICC|\u4e2d\u91d1", "CICC", "CICC"),
    (r"CITIC|\u4e2d\u4fe1", "CITIC Securities", "CITICS"),
    (r"\u4e1c\u5434", "Soochow Securities", "Soochow"),
    (r"\u4e2d\u4fe1\u5efa\u6295", "CSC Financial", "CSC"),
    (r"\u56fd\u6cf0\u541b\u5b89", "Guotai Junan", "GTJA"),
    (r"\u534e\u6cf0", "Huatai Securities", "Huatai"),
    (r"JPM|J\.P\. Morgan|\u6469\u6839", "J.P. Morgan", "JPM"),
    (r"Morgan Stanley|\u5927\u6469", "Morgan Stanley", "MS"),
]

INDUSTRY_KEYWORDS = {
    "AI": ["AI", "\u4eba\u5de5\u667a\u80fd", "\u7b97\u529b", "\u5149\u6a21\u5757"],
    "brokerage": ["\u5238\u5546", "\u975e\u94f6", "\u8bc1\u5238"],
    "lithium": ["\u78b3\u9178\u9502", "\u9502\u7535", "\u9502\u77ff", "\u9502\u8f89\u77f3"],
    "textile": ["\u7eba\u7ec7", "\u7eba\u7ec7\u8bbe\u5907"],
    "auto": ["\u6c7d\u8f66", "\u65b0\u80fd\u6e90\u8f66", "EV"],
    "nuclear": ["nuclear", "uranium", "\u6838\u7535", "\u94c0"],
    "macro": ["A\u80a1", "\u5b8f\u89c2", "\u7b56\u7565", "\u6d41\u52a8\u6027"],
}


@dataclass
class ImportStats:
    stream_files: int = 0
    stream_items: int = 0
    stream_duplicates: int = 0
    report_files: int = 0
    report_duplicates: int = 0
    failures: int = 0


def utcnow_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text_fallback(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def json_list(values: Iterable[str]) -> str:
    cleaned = []
    for value in values:
        value = str(value).strip()
        if value and value not in cleaned:
            cleaned.append(value)
    return json.dumps(cleaned, ensure_ascii=False)


def init_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS kp_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_hash TEXT NOT NULL UNIQUE,
            source_platform TEXT NOT NULL,
            source_file TEXT NOT NULL,
            source_type TEXT NOT NULL,
            credibility TEXT NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            summary TEXT NOT NULL,
            published_at TEXT,
            imported_at TEXT NOT NULL,
            author TEXT,
            tickers_json TEXT NOT NULL,
            company_names_json TEXT NOT NULL,
            industries_json TEXT NOT NULL,
            themes_json TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS kp_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_hash TEXT NOT NULL UNIQUE,
            source_platform TEXT NOT NULL,
            original_filename TEXT NOT NULL,
            stored_path TEXT NOT NULL,
            extracted_text_path TEXT,
            metadata_path TEXT,
            suggested_filename TEXT,
            extraction_status TEXT NOT NULL,
            title TEXT NOT NULL,
            broker TEXT,
            broker_short TEXT,
            published_at TEXT,
            imported_at TEXT NOT NULL,
            tickers_json TEXT NOT NULL,
            company_names_json TEXT NOT NULL,
            industries_json TEXT NOT NULL,
            themes_json TEXT NOT NULL,
            summary TEXT NOT NULL
        )
        """
    )
    try:
        conn.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS kp_items_fts
            USING fts5(title, text, summary, content='kp_items', content_rowid='id')
            """
        )
        conn.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS kp_reports_fts
            USING fts5(title, summary, content='kp_reports', content_rowid='id')
            """
        )
        conn.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS kp_report_text_fts
            USING fts5(report_id UNINDEXED, title, text)
            """
        )
    except sqlite3.OperationalError:
        # Some Python builds omit FTS5. The normal tables are still usable.
        pass
    conn.commit()
    return conn


def split_stream_items(text: str) -> list[str]:
    blocks = re.split(r"(?m)^\s*(?:---+|\*\*\*+)\s*$", text)
    items = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        if lines[0].startswith("#") and len(lines) <= 3:
            continue
        items.append(block)
    return items


def extract_datetime(text: str) -> str | None:
    match = re.search(
        r"(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})(?:\s+(\d{1,2}):(\d{2}))?",
        text,
    )
    if not match:
        return None
    year, month, day, hour, minute = match.groups()
    if hour is None:
        return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d} {int(hour):02d}:{int(minute):02d}"


def extract_date_from_name_or_mtime(path: Path) -> str:
    date = extract_datetime(path.name)
    if date:
        return date[:10]
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")


def infer_author(block: str) -> str | None:
    lines = [line.strip("# ").strip() for line in block.splitlines() if line.strip()]
    for line in lines[:4]:
        if extract_datetime(line):
            continue
        if ":" in line and len(line) > 20:
            continue
        if len(line) <= 30:
            return line
    return None


def field_value(block: str, field: str) -> str | None:
    match = re.search(rf"(?im)^\s*{re.escape(field)}\s*:\s*(.+?)\s*$", block)
    return match.group(1).strip() if match else None


def infer_title(block: str) -> str:
    explicit = field_value(block, "title")
    if explicit:
        return explicit[:160]
    lines = [line.strip("# ").strip() for line in block.splitlines() if line.strip()]
    for line in lines:
        if extract_datetime(line):
            continue
        if re.match(r"(?i)^(author|published_at|source_type|credibility|text)\s*:", line):
            continue
        if len(line) <= 6:
            continue
        return line[:160]
    return "Untitled Knowledge Planet item"


def infer_source_type(text: str) -> str:
    lowered = text.lower()
    if any(word in text for word in ["PDF", ".pdf", "\u7814\u62a5"]):
        return "report_list_post"
    if any(word in text for word in ["\u4f20\u95fb", "\u636e\u8bf4", "\u542c\u8bf4", "\u7f51\u4f20"]):
        return "unverified_rumor"
    if any(word in text for word in ["\u6bb5\u5b50", "\u8c03\u4f83", "\u7b11"]):
        return "market_joke"
    if any(
        word in text
        for word in [
            "\u6e20\u9053",
            "\u7ec8\u7aef",
            "\u7ecf\u9500\u5546",
            "\u5ba2\u6237",
            "\u4f9b\u5e94\u5546",
            "\u8ba2\u5355",
            "\u9a8c\u8bc1",
            "\u9001\u6837",
        ]
    ):
        return "channel_check"
    if any(
        word in text
        for word in [
            "\u5468\u5ea6\u66f4\u65b0",
            "\u6570\u636e\u5e93",
            "\u5e93\u5b58",
            "\u4ef7\u683c",
            "\u6392\u4ea7",
            "\u51fa\u8d27",
            "\u5f00\u5de5\u7387",
            "\u7a3c\u52a8\u7387",
            "smm",
            "ppi",
        ]
    ):
        return "industry_weekly_data"
    if any(
        word in text
        for word in [
            "\u8c03\u7814",
            "\u4f1a\u8bae\u7eaa\u8981",
            "\u4ea4\u6d41",
            "\u4e13\u5bb6",
            "\u4ea7\u4e1a\u94fe",
            "\u53cd\u9988",
        ]
    ):
        return "company_research_feedback"
    if any(
        word in text
        for word in [
            "\u76ee\u6807\u5e02\u503c",
            "\u5f3acall",
            "\u5927call",
            "\u91cd\u70b9\u63a8\u8350",
            "\u7ffb\u500d",
            "\u73b0\u4ef7",
        ]
    ):
        return "sell_side_push"
    if any(word in text for word in ["\u5468\u5ea6\u66f4\u65b0", "\u6570\u636e\u5e93", "\u5e93\u5b58", "\u4ef7\u683c", "ppi"]):
        return "industry_data_snippet"
    if any(word in text for word in ["\u7b56\u7565", "\u70b9\u8bc4", "\u770b\u597d", "\u5206\u5316", "a\u80a1"]) or "market" in lowered:
        return "strategy_view"
    return "raw_note"


def credibility_for_source_type(source_type: str) -> str:
    return {
        "industry_weekly_data": "broker_survey_or_industry_data",
        "industry_data_snippet": "broker_survey_or_industry_data",
        "company_research_feedback": "research_feedback_hard_to_publicly_verify",
        "channel_check": "high_private_channel_hard_to_verify",
        "sell_side_push": "sell_side_view_with_optimism_bias",
        "strategy_view": "sell_side_view",
        "report_list_post": "attachment_index",
        "unverified_rumor": "unverified_rumor",
        "market_joke": "sentiment_only",
        "raw_note": "unclassified_needs_review",
    }.get(source_type, "unclassified_needs_review")


def extract_tickers(text: str) -> list[str]:
    tickers = []
    patterns = [
        r"\b\d{6}\.(?:SH|SZ|BJ)\b",
        r"\b(?:SH|SZ|BJ)\d{6}\b",
        r"\(([A-Z]{1,5})\)",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            value = match.group(1) if match.groups() else match.group(0)
            if value not in tickers:
                tickers.append(value)
    return tickers


def infer_broker(text: str) -> tuple[str | None, str | None]:
    for pattern, broker, short in BROKER_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return broker, short
    return None, None


def infer_industries(text: str) -> list[str]:
    industries = []
    for industry, keywords in INDUSTRY_KEYWORDS.items():
        if any(keyword.lower() in text.lower() for keyword in keywords):
            industries.append(industry)
    return industries


def infer_themes(text: str) -> list[str]:
    candidates = [
        ("\u53bb\u5e93", "destocking"),
        ("\u5e93\u5b58", "inventory"),
        ("\u4ef7\u683c", "price"),
        ("\u4f30\u503c", "valuation"),
        ("\u6d41\u52a8\u6027", "liquidity"),
        ("\u4eba\u5de5\u667a\u80fd", "AI"),
        ("AI", "AI"),
        ("\u51fa\u53e3", "export"),
        ("\u4e1a\u7ee9", "earnings"),
        ("\u6307\u5f15", "guidance"),
    ]
    themes = []
    for keyword, theme in candidates:
        if keyword.lower() in text.lower() and theme not in themes:
            themes.append(theme)
    return themes


def simple_summary(text: str, max_len: int = 220) -> str:
    collapsed = re.sub(r"\s+", " ", text).strip()
    if len(collapsed) <= max_len:
        return collapsed
    return collapsed[: max_len - 3] + "..."


def archive_path(base: Path, date_text: str, filename: str) -> Path:
    date = date_text[:10] if date_text else datetime.now().strftime("%Y-%m-%d")
    year, month, day = date.split("-")
    target_dir = base / year / month / day
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / filename
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    counter = 2
    while True:
        candidate = target_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def insert_item(conn: sqlite3.Connection, item: dict) -> bool:
    try:
        cursor = conn.execute(
            """
            INSERT INTO kp_items (
                content_hash, source_platform, source_file, source_type, credibility,
                title, text, summary, published_at, imported_at, author,
                tickers_json, company_names_json, industries_json, themes_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item["content_hash"],
                "knowledge_planet",
                item["source_file"],
                item["source_type"],
                item["credibility"],
                item["title"],
                item["text"],
                item["summary"],
                item.get("published_at"),
                item["imported_at"],
                item.get("author"),
                item["tickers_json"],
                item["company_names_json"],
                item["industries_json"],
                item["themes_json"],
            ),
        )
    except sqlite3.IntegrityError:
        return False
    rowid = cursor.lastrowid
    try:
        conn.execute(
            "INSERT INTO kp_items_fts(rowid, title, text, summary) VALUES (?, ?, ?, ?)",
            (rowid, item["title"], item["text"], item["summary"]),
        )
    except sqlite3.OperationalError:
        pass
    return True


def process_stream_files(root: Path, conn: sqlite3.Connection, dry_run: bool) -> ImportStats:
    stats = ImportStats()
    inbox = root / "inbox"
    processed = root / "processed"
    failed = root / "failed"
    for path in sorted([*inbox.glob("*.md"), *inbox.glob("*.txt")]):
        if path.name in STREAM_SKIP_FILES or path.name.startswith("."):
            continue
        stats.stream_files += 1
        try:
            text = read_text_fallback(path)
            blocks = split_stream_items(text)
            file_date = extract_date_from_name_or_mtime(path)
            for block in blocks:
                published_at = field_value(block, "published_at") or extract_datetime(block) or file_date
                title = infer_title(block)
                source_type = field_value(block, "source_type") or infer_source_type(block)
                item = {
                    "content_hash": sha256_text(block),
                    "source_file": str(path),
                    "source_type": source_type,
                    "credibility": field_value(block, "credibility") or credibility_for_source_type(source_type),
                    "title": title,
                    "text": block,
                    "summary": simple_summary(block),
                    "published_at": published_at,
                    "imported_at": utcnow_iso(),
                    "author": field_value(block, "author") or infer_author(block),
                    "tickers_json": json_list(extract_tickers(block)),
                    "company_names_json": json_list([]),
                    "industries_json": json_list(infer_industries(block)),
                    "themes_json": json_list(infer_themes(block)),
                }
                if dry_run:
                    inserted = True
                else:
                    inserted = insert_item(conn, item)
                if inserted:
                    stats.stream_items += 1
                else:
                    stats.stream_duplicates += 1
            if not dry_run:
                target = archive_path(processed, file_date, path.name)
                shutil.move(str(path), str(target))
        except Exception:
            stats.failures += 1
            if not dry_run:
                target = archive_path(failed, datetime.now().strftime("%Y-%m-%d"), path.name)
                shutil.move(str(path), str(target))
    if not dry_run:
        conn.commit()
    return stats


def extract_pdf_text(path: Path) -> tuple[str, str]:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return "", "pypdf_unavailable"

    try:
        reader = PdfReader(str(path))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return "\n\n".join(pages).strip(), "ok"
    except Exception as exc:
        return "", f"extract_failed: {exc}"


def sanitize_filename_part(value: str, max_len: int = 80) -> str:
    value = re.sub(r"[^\w.-]+", "-", value, flags=re.UNICODE).strip("-._")
    value = re.sub(r"-{2,}", "-", value)
    return (value or "report")[:max_len]


def suggested_pdf_name(path: Path, date_text: str, broker_short: str | None, title: str) -> str:
    date_compact = date_text[:10].replace("-", "") if date_text else "undated"
    broker = broker_short or "unknown"
    title_part = sanitize_filename_part(title or path.stem)
    return f"{date_compact}_{broker}_{title_part}.pdf"


def insert_report(conn: sqlite3.Connection, report: dict) -> bool:
    try:
        cursor = conn.execute(
            """
            INSERT INTO kp_reports (
                file_hash, source_platform, original_filename, stored_path,
                extracted_text_path, metadata_path, suggested_filename,
                extraction_status, title, broker, broker_short, published_at,
                imported_at, tickers_json, company_names_json, industries_json,
                themes_json, summary
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                report["file_hash"],
                "knowledge_planet",
                report["original_filename"],
                report["stored_path"],
                report.get("extracted_text_path"),
                report.get("metadata_path"),
                report.get("suggested_filename"),
                report["extraction_status"],
                report["title"],
                report.get("broker"),
                report.get("broker_short"),
                report.get("published_at"),
                report["imported_at"],
                report["tickers_json"],
                report["company_names_json"],
                report["industries_json"],
                report["themes_json"],
                report["summary"],
            ),
        )
    except sqlite3.IntegrityError:
        return False
    rowid = cursor.lastrowid
    try:
        conn.execute(
            "INSERT INTO kp_reports_fts(rowid, title, summary) VALUES (?, ?, ?)",
            (rowid, report["title"], report["summary"]),
        )
    except sqlite3.OperationalError:
        pass
    return True


def upsert_report_text_fts(
    conn: sqlite3.Connection,
    report_id: int,
    title: str,
    text: str,
) -> None:
    try:
        conn.execute("DELETE FROM kp_report_text_fts WHERE report_id = ?", (str(report_id),))
        conn.execute(
            "INSERT INTO kp_report_text_fts(report_id, title, text) VALUES (?, ?, ?)",
            (str(report_id), title, text),
        )
    except sqlite3.OperationalError:
        pass


def process_report_files(
    root: Path,
    conn: sqlite3.Connection,
    dry_run: bool,
    apply_suggested_pdf_names: bool,
) -> ImportStats:
    stats = ImportStats()
    inbox = root / "reports" / "inbox"
    processed = root / "reports" / "processed"
    extracted_dir = root / "reports" / "extracted"
    failed = root / "reports" / "failed"
    extracted_dir.mkdir(parents=True, exist_ok=True)

    for path in sorted(inbox.glob("*.pdf")):
        stats.report_files += 1
        try:
            file_bytes = path.read_bytes()
            file_hash = sha256_bytes(file_bytes)
            probe_text, extraction_status = extract_pdf_text(path)
            combined = f"{path.stem}\n{probe_text[:3000]}"
            published_at = extract_date_from_name_or_mtime(path)
            broker, broker_short = infer_broker(combined)
            title = path.stem
            suggested_name = suggested_pdf_name(path, published_at, broker_short, title)
            archive_name = suggested_name if apply_suggested_pdf_names else path.name
            stored_target = archive_path(processed, published_at, archive_name)

            extracted_text_path = extracted_dir / f"{path.stem}.txt"
            metadata_path = extracted_dir / f"{path.stem}.json"
            summary = simple_summary(probe_text or path.stem)
            metadata = {
                "source_platform": "knowledge_planet",
                "source_type": "sell_side_report_pdf",
                "original_filename": path.name,
                "stored_path": str(stored_target),
                "suggested_filename": suggested_name,
                "extraction_status": extraction_status,
                "title": title,
                "broker": broker,
                "broker_short": broker_short,
                "published_at": published_at,
                "imported_at": utcnow_iso(),
                "tickers": extract_tickers(combined),
                "company_names": [],
                "industries": infer_industries(combined),
                "themes": infer_themes(combined),
                "summary": summary,
                "copyright_note": "internal_research_only",
            }
            report = {
                "file_hash": file_hash,
                "original_filename": path.name,
                "stored_path": str(stored_target),
                "extracted_text_path": str(extracted_text_path),
                "metadata_path": str(metadata_path),
                "suggested_filename": suggested_name,
                "extraction_status": extraction_status,
                "title": title,
                "broker": broker,
                "broker_short": broker_short,
                "published_at": published_at,
                "imported_at": metadata["imported_at"],
                "tickers_json": json_list(metadata["tickers"]),
                "company_names_json": json_list([]),
                "industries_json": json_list(metadata["industries"]),
                "themes_json": json_list(metadata["themes"]),
                "summary": summary,
            }
            inserted = True if dry_run else insert_report(conn, report)
            if inserted:
                if not dry_run:
                    row_id = conn.execute(
                        "SELECT id FROM kp_reports WHERE file_hash = ?",
                        (file_hash,),
                    ).fetchone()[0]
                    extracted_text_path.write_text(probe_text, encoding="utf-8")
                    metadata_path.write_text(
                        json.dumps(metadata, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
                    upsert_report_text_fts(conn, row_id, title, probe_text)
                    shutil.move(str(path), str(stored_target))
            else:
                stats.report_duplicates += 1
                if not dry_run:
                    target = archive_path(processed, published_at, path.name)
                    shutil.move(str(path), str(target))
        except Exception:
            stats.failures += 1
            if not dry_run:
                target = archive_path(failed, datetime.now().strftime("%Y-%m-%d"), path.name)
                shutil.move(str(path), str(target))
    if not dry_run:
        conn.commit()
    return stats


def backfill_report_text(root: Path, conn: sqlite3.Connection, dry_run: bool) -> int:
    """Extract text for reports that were imported before PDF extraction worked."""
    extracted_dir = root / "reports" / "extracted"
    extracted_dir.mkdir(parents=True, exist_ok=True)
    rows = conn.execute(
        """
        SELECT id, stored_path, original_filename, title
        FROM kp_reports
        WHERE extraction_status != 'ok'
           OR id NOT IN (
                SELECT CAST(report_id AS INTEGER)
                FROM kp_report_text_fts
           )
        """
    ).fetchall()
    updated = 0
    for row_id, stored_path, original_filename, title in rows:
        pdf_path = Path(stored_path)
        if not pdf_path.exists():
            continue
        text, status = extract_pdf_text(pdf_path)
        if status != "ok":
            continue
        base_name = Path(original_filename).stem or Path(title).stem or f"report_{row_id}"
        extracted_text_path = extracted_dir / f"{base_name}.txt"
        metadata_path = extracted_dir / f"{base_name}.json"
        summary = simple_summary(text or title)
        metadata = {
            "source_platform": "knowledge_planet",
            "source_type": "sell_side_report_pdf",
            "original_filename": original_filename,
            "stored_path": str(pdf_path),
            "extraction_status": status,
            "title": title,
            "summary": summary,
            "backfilled_at": utcnow_iso(),
        }
        if not dry_run:
            extracted_text_path.write_text(text, encoding="utf-8")
            metadata_path.write_text(
                json.dumps(metadata, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            conn.execute(
                """
                UPDATE kp_reports
                SET extraction_status = ?, extracted_text_path = ?, metadata_path = ?, summary = ?
                WHERE id = ?
                """,
                (status, str(extracted_text_path), str(metadata_path), summary, row_id),
            )
            upsert_report_text_fts(conn, row_id, title, text)
        updated += 1
    if not dry_run:
        conn.commit()
    return updated


def merge_stats(*stats_list: ImportStats) -> ImportStats:
    merged = ImportStats()
    for stats in stats_list:
        merged.stream_files += stats.stream_files
        merged.stream_items += stats.stream_items
        merged.stream_duplicates += stats.stream_duplicates
        merged.report_files += stats.report_files
        merged.report_duplicates += stats.report_duplicates
        merged.failures += stats.failures
    return merged


def main() -> int:
    parser = argparse.ArgumentParser(description="Import local Knowledge Planet files.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--db", type=Path, default=None)
    parser.add_argument("--stream", action="store_true", help="Import md/txt post streams only.")
    parser.add_argument("--reports", action="store_true", help="Import PDF reports only.")
    parser.add_argument("--dry-run", action="store_true", help="Parse files without writing DB or moving files.")
    parser.add_argument(
        "--apply-suggested-pdf-names",
        action="store_true",
        help="Archive PDFs with normalized suggested filenames.",
    )
    parser.add_argument(
        "--backfill-report-text",
        action="store_true",
        help="Extract text for already imported PDF reports whose extraction failed earlier.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    db_path = (args.db or (root / "index.sqlite")).resolve()
    run_stream = args.stream or not args.reports
    run_reports = args.reports or not args.stream

    conn = init_db(db_path)
    stats_parts = []
    if run_stream:
        stats_parts.append(process_stream_files(root, conn, args.dry_run))
    if run_reports:
        stats_parts.append(
            process_report_files(root, conn, args.dry_run, args.apply_suggested_pdf_names)
        )
    backfilled = 0
    if args.backfill_report_text:
        backfilled = backfill_report_text(root, conn, args.dry_run)
    stats = merge_stats(*stats_parts)
    conn.close()

    print("Knowledge Planet import complete")
    print(f"root: {root}")
    print(f"db: {db_path}")
    print(f"stream files: {stats.stream_files}")
    print(f"stream items inserted: {stats.stream_items}")
    print(f"stream duplicates: {stats.stream_duplicates}")
    print(f"report files: {stats.report_files}")
    print(f"report duplicates: {stats.report_duplicates}")
    print(f"report text backfilled: {backfilled}")
    print(f"failures: {stats.failures}")
    if args.dry_run:
        print("dry run: no files moved and no rows inserted")
    return 0 if stats.failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
