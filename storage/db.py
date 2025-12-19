import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "afterrun.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    return conn
