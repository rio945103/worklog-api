from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# GETのテスト
def test_read_worklogs():
    response = client.get("/worklogs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# POSTのテスト
def test_create_worklog():
    response = client.post("/worklogs", json={"title": "テスト作業", "duration": 30})
    assert response.status_code == 200
    assert response.json()["message"] == "保存しました"

# 型が違う場合のテスト
def test_create_worklog_invalid():
    response = client.post("/worklogs", json={"title": "テスト", "duration": "abc"})
    assert response.status_code == 422