import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_search_contact():
    response = client.get("/phonebook/contacts?prefix=Ale")
    assert response.status_code == 200
    assert response.json() == ["824759", "862720"]


@pytest.mark.parametrize(
    "payload, expected_response",
    [
        ({"name": "Alena", "phone": "1111"}, False),
        ({"name": "Alexandr", "phone": "1111"}, True),
    ],
)
def test_add_contact(payload, expected_response):
    response = client.post("/phonebook/contacts", json=payload)
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.parametrize(
    "payload, expected_status_code",
    [
        ({"name": "", "phone": "1111"}, 422),
        ({"name": "Alexandr", "phone": ""}, 422),
    ],
)
def test_add_contact_validation(payload, expected_status_code):
    response = client.post("/phonebook/contacts", json=payload)
    assert response.status_code == expected_status_code
