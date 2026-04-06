import sqlite3

def get_connection():
    conn = sqlite3.connect("worklog.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS worklogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            duration INTEGER NOT NULL,
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.commit()
    conn.close()

# ログを1件保存する
def insert_worklog(title: str, duration: int):
    conn = get_connection()
    conn.execute(
        "INSERT INTO worklogs (title, duration) VALUES (?, ?)",
        (title, duration)
    )
    conn.commit()
    conn.close()

# ログを全件取得する
def get_all_worklogs():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM worklogs ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]

if __name__ == "__main__":
    init_db()

    # テストデータを入れてみる
    insert_worklog("FastAPI学習", 60)
    insert_worklog("SQLite入門", 45)

    logs = get_all_worklogs()
    for log in logs:
        print(log)