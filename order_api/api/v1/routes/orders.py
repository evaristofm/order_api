from fastapi import APIRouter, Depends, status

from order_api.models.schemas.message import Message
from order_api.models.schemas.order import OrderRequest, OrderResponse
from order_api.services.order_service import OrderService, get_order_service

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=Message)
async def index():
    return {"message": "Olá, Mundo!"}


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OrderResponse
)
async def create_order(
    order_data: OrderRequest,
    service: OrderService = Depends(get_order_service),
):
    return service.process_order(order_data)
