from http import HTTPStatus

from fastapi.testclient import TestClient

from order_api.main import app
from order_api.models.schemas.item import ItemRequest
from order_api.models.schemas.order import OrderRequest
from order_api.services.order_service import OrderService

client = TestClient(app)

BASE_URL = "/api/v1/order"
TOTAL = 100.0
MAX_DESCONTO_PERCENTUAL = 90.0


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get(f"{BASE_URL}/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá, Mundo!"}


# teste service
def test_process_order_with_pytest_mock(mocker):
    # Arrange
    mock_notifier = mocker.Mock()
    mock_storage = mocker.Mock()
    mock_discount_strategy = mocker.Mock()

    mock_discount_strategy.apply_discount.return_value = 90.0

    service = OrderService(
        notifier=mock_notifier,
        discount_strategy=mock_discount_strategy,
        storage=mock_storage,
    )

    order_data = OrderRequest(
        items=[
            ItemRequest(name="Notebook", price=60.0, quantity=1),
            ItemRequest(name="Mouse", price=40.0, quantity=1),
        ]
    )

    response = service.process_order(order_data)

    assert response.total == TOTAL
    assert response.discounted_total == MAX_DESCONTO_PERCENTUAL
    assert "Order processed" in response.message
    assert "$90.00" in response.message


def test_create_order():
    client = TestClient(app)

    response = client.post(
        f"{BASE_URL}",
        json={"items": [{"name": "Note", "price": 10, "quantity": 1}]}
    )
    assert response.status_code == HTTPStatus.CREATED
