from fastapi.testclient import TestClient

from ukhaan_api.app import app

client = TestClient(app)


def test_get_ukhaan_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_nepali_returns_200():
    response = client.get("/nepali")
    assert response.status_code == 200


def test_roman_returns_200():
    response = client.get("/roman")
    assert response.status_code == 200


def test_example_returns_200():
    response = client.get("/example")
    assert response.status_code == 200


def test_random_ukhaan_returns_200():
    response = client.get("/random/ukhaan")
    assert response.status_code == 200


def test_random_nepali_returns_200():
    response = client.get("/random/nepali")
    assert response.status_code == 200


def test_random_roman_returns_200():
    response = client.get("/random/roman")
    assert response.status_code == 200


def test_random_example_returns_200():
    response = client.get("/random/example")
    assert response.status_code == 200
