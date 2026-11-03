import sqlite3
import json
from datetime import datetime
from typing import List, Optional
from contextlib import contextmanager


DB_PATH = "reports.db"


@contextmanager
def get_db():
    """Context manager for database connections."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    """Initialize the database and create the reports table if it doesn't exist."""
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id TEXT PRIMARY KEY,
                topic_fa TEXT NOT NULL,
                topic_en TEXT NOT NULL,
                analysis_en TEXT NOT NULL,
                final_report TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        conn.commit()
    print(f"✓ Database initialized at {DB_PATH}")


def save_report(
    report_id: str,
    topic_fa: str,
    topic_en: str,
    analysis_en: dict,
    final_report: dict,
) -> dict:
    """Save a new report or update an existing one."""
    now = datetime.utcnow().isoformat()
    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO reports (id, topic_fa, topic_en, analysis_en, final_report, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                topic_fa = excluded.topic_fa,
                topic_en = excluded.topic_en,
                analysis_en = excluded.analysis_en,
                final_report = excluded.final_report,
                updated_at = excluded.updated_at
            """,
            (
                report_id,
                topic_fa,
                topic_en,
                json.dumps(analysis_en, ensure_ascii=False),
                json.dumps(final_report, ensure_ascii=False),
                now,
                now,
            ),
        )
        conn.commit()
    return get_report(report_id)


def get_all_reports() -> List[dict]:
    """Get all reports, newest first."""
    with get_db() as conn:
        cursor = conn.execute(
            "SELECT id, topic_fa, created_at, updated_at FROM reports ORDER BY created_at DESC"
        )
        return [dict(row) for row in cursor.fetchall()]


def get_report(report_id: str) -> Optional[dict]:
    """Get a single report by ID."""
    with get_db() as conn:
        cursor = conn.execute("SELECT * FROM reports WHERE id = ?", (report_id,))
        row = cursor.fetchone()
        if not row:
            return None
        data = dict(row)
        data["analysis_en"] = json.loads(data["analysis_en"])
        data["final_report"] = json.loads(data["final_report"])
        return data


def delete_report(report_id: str) -> bool:
    """Delete a report by ID. Returns True if deleted, False if not found."""
    with get_db() as conn:
        cursor = conn.execute("DELETE FROM reports WHERE id = ?", (report_id,))
        conn.commit()
        return cursor.rowcount > 0


def update_report_title(report_id: str, new_title: str) -> Optional[dict]:
    """Update the project title in the final report."""
    report = get_report(report_id)
    if not report:
        return None
    report["final_report"]["project_title"] = new_title
    now = datetime.utcnow().isoformat()
    with get_db() as conn:
        conn.execute(
            "UPDATE reports SET final_report = ?, updated_at = ? WHERE id = ?",
            (json.dumps(report["final_report"], ensure_ascii=False), now, report_id),
        )
        conn.commit()
    return get_report(report_id)