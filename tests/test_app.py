from fastapi.testclient import TestClient

from main.app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_read_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200