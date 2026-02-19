"""
SQLite database for Amelia Studio — users and configuration.

DB is stored in /data/output/studio.db (persisted via Docker volume).
"""

import sqlite3
import hashlib
import secrets
import time
from pathlib import Path
from contextlib import contextmanager

from backend.config import settings

DB_PATH = settings.output_dir / "studio.db"


@contextmanager
def get_db():
    """Get a database connection with row_factory."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    """Create tables if they don't exist."""
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'admin',
                created_at REAL NOT NULL
            );

            CREATE TABLE IF NOT EXISTS sessions (
                token TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                created_at REAL NOT NULL,
                expires_at REAL NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS config (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                updated_at REAL NOT NULL,
                updated_by INTEGER,
                FOREIGN KEY (updated_by) REFERENCES users(id)
            );
        """)


def hash_password(password: str, salt: str = None) -> tuple[str, str]:
    """Hash a password with a salt. Returns (hash, salt)."""
    if salt is None:
        salt = secrets.token_hex(16)
    pw_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return pw_hash, salt


# ── User operations ──

def create_user(username: str, password: str, role: str = "admin") -> dict | None:
    """Create a new user. Returns the user dict or None if username taken."""
    pw_hash, salt = hash_password(password)
    try:
        with get_db() as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash, salt, role, created_at) VALUES (?, ?, ?, ?, ?)",
                (username.lower().strip(), pw_hash, salt, role, time.time()),
            )
            return get_user_by_name(username)
    except sqlite3.IntegrityError:
        return None


def verify_user(username: str, password: str) -> dict | None:
    """Verify credentials. Returns user dict or None."""
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username.lower().strip(),),
        ).fetchone()
        if not row:
            return None
        pw_hash, _ = hash_password(password, row["salt"])
        if pw_hash == row["password_hash"]:
            return dict(row)
        return None


def get_user_by_name(username: str) -> dict | None:
    """Get user by username."""
    with get_db() as conn:
        row = conn.execute(
            "SELECT id, username, role, created_at FROM users WHERE username = ?",
            (username.lower().strip(),),
        ).fetchone()
        return dict(row) if row else None


def get_user_by_id(user_id: int) -> dict | None:
    """Get user by ID."""
    with get_db() as conn:
        row = conn.execute(
            "SELECT id, username, role, created_at FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()
        return dict(row) if row else None


def list_users() -> list[dict]:
    """List all users (without password info)."""
    with get_db() as conn:
        rows = conn.execute(
            "SELECT id, username, role, created_at FROM users ORDER BY id",
        ).fetchall()
        return [dict(r) for r in rows]


def user_count() -> int:
    """Return the total number of users."""
    with get_db() as conn:
        return conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]


# ── Session operations ──

SESSION_TTL = 60 * 60 * 24 * 7  # 7 days


def create_session(user_id: int) -> str:
    """Create a session token for a user."""
    token = secrets.token_urlsafe(32)
    now = time.time()
    with get_db() as conn:
        # Clean up expired sessions
        conn.execute("DELETE FROM sessions WHERE expires_at < ?", (now,))
        conn.execute(
            "INSERT INTO sessions (token, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
            (token, user_id, now, now + SESSION_TTL),
        )
    return token


def validate_session(token: str) -> dict | None:
    """Validate a session token. Returns user dict or None."""
    if not token:
        return None
    with get_db() as conn:
        row = conn.execute(
            "SELECT user_id FROM sessions WHERE token = ? AND expires_at > ?",
            (token, time.time()),
        ).fetchone()
        if row:
            return get_user_by_id(row["user_id"])
    return None


def delete_session(token: str):
    """Delete a session (logout)."""
    with get_db() as conn:
        conn.execute("DELETE FROM sessions WHERE token = ?", (token,))


# ── Config operations ──

def get_config(key: str, default: str = "") -> str:
    """Get a config value."""
    with get_db() as conn:
        row = conn.execute("SELECT value FROM config WHERE key = ?", (key,)).fetchone()
        return row["value"] if row else default


def set_config(key: str, value: str, user_id: int = None):
    """Set a config value."""
    with get_db() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO config (key, value, updated_at, updated_by) VALUES (?, ?, ?, ?)",
            (key, value, time.time(), user_id),
        )


def get_all_config() -> dict[str, str]:
    """Get all config as a dict."""
    with get_db() as conn:
        rows = conn.execute("SELECT key, value FROM config").fetchall()
        return {r["key"]: r["value"] for r in rows}
