from fastapi.testclient import TestClient 

from tutorial10 import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ("message": "Hello World")