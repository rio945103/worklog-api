from fastapi import FastAPI
from database import init_db, insert_worklog, get_all_worklogs

app = FastAPI()

# 起動時にDBを初期化
init_db()

# ログ一覧を取得
@app.get("/worklogs")
def read_worklogs():
    return get_all_worklogs()

# ログを新規作成
@app.post("/worklogs")
def create_worklog(title: str, duration: int):
    insert_worklog(title, duration)
    return {"message": "保存しました", "title": title, "duration": duration}