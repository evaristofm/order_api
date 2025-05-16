from http import HTTPStatus

from fastapi.testclient import TestClient

from order_api.main import app

client = TestClient(app)

BASE_URL = "/api/v1/order"


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get(f"{BASE_URL}/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá, Mundo!"}
