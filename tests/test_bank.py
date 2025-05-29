from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_banks():
    response = client.get("/banks/")
    assert response.status_code == 200