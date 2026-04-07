# worklog-api

作業ログを管理するREST API

## 技術スタック

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / docker-compose

## 機能

- 作業ログの登録（POST /worklogs）
- 作業ログの一覧取得（GET /worklogs）

## 起動方法

```bash
docker-compose up --build
```

起動後、以下にアクセス：

- API: http://localhost:8000
- ドキュメント: http://localhost:8000/docs

## 開発環境でのローカル起動

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```