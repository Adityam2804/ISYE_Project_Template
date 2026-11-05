from pathlib import Path
import sqlite3

HERE = Path(__file__).resolve().parent
DB_PATH = HERE / "practice.db"
SQL_PATH = HERE / "setup.sql"

if DB_PATH.exists():
    DB_PATH.unlink()

con = sqlite3.connect(DB_PATH)
try:
    con.executescript(SQL_PATH.read_text(encoding="utf-8"))
    con.commit()
finally:
    con.close()

print(f"Day 19 practice database created: {DB_PATH}")
