from fastapi import FastAPI
from pydantic import BaseModel
from database import init_db, insert_worklog, get_all_worklogs

app = FastAPI()
init_db()

# リクエストの型定義
class WorkLogRequest(BaseModel):
    title: str
    duration: int

@app.get("/worklogs")
def read_worklogs():
    return get_all_worklogs()

@app.post("/worklogs")
def create_worklog(request: WorkLogRequest):
    insert_worklog(request.title, request.duration)
    return {"message": "保存しました", "title": request.title, "duration": request.duration}