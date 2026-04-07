from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
from datetime import datetime

# データベースの接続先
engine = create_engine("postgresql://postgres:YOKO23ryo@localhost:5432/worklog_db")

# モデルの基底クラス
class Base(DeclarativeBase):
    pass

# 作業ログのモデル（テーブルの定義）
class WorkLog(Base):
    __tablename__ = "worklogs_v2"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    created_at = Column(String, default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# テーブルを作成
def init_db():
    Base.metadata.create_all(engine)

# ログを保存
def insert_worklog(title: str, duration: int):
    with Session(engine) as session:
        log = WorkLog(title=title, duration=duration)
        session.add(log)
        session.commit()

# ログを全件取得
def get_all_worklogs():
    with Session(engine) as session:
        logs = session.query(WorkLog).order_by(WorkLog.id.desc()).all()
        return [
            {"id": l.id, "title": l.title, "duration": l.duration, "created_at": l.created_at}
            for l in logs
        ]