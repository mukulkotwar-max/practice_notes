from urllib import response
from fastapi.testclient import TestClient
from fasttest1 import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    #status code check
    assert response.status_code == 200
    #response data check
    assert response.json() == {"message":"hello world"}

def test_add():
    response = client.get("/add?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"result":8}