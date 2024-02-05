from urllib.parse import quote
from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


def test_get_sum():
    response = client.get(f"/api/calc?expression={quote('42+3')}")
    assert response.status_code == 200
    assert response.json()["result"] == "45"


def test_get_diff():
    response = client.get(f"/api/calc?expression={quote('5-8')}")
    assert response.status_code == 200
    assert response.json()["result"] == "-3"


def test_get_mult():
    response = client.get(f"/api/calc?expression={quote('2*8')}")
    assert response.status_code == 200
    assert response.json()["result"] == "16"


def test_get_div():
    response = client.get(f"/api/calc?expression={quote('15/2')}")
    assert response.status_code == 200
    assert response.json()["result"] == "7.5"
