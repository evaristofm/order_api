from fastapi import APIRouter, Depends, status

from order_api.models.schemas import OrderRequest, OrderResponse
from order_api.services.order_service import OrderService, get_order_service

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def index():
    return {'message': 'Olá, Mundo!'}


@router.post(
    '/', response_model=OrderResponse, status_code=status.HTTP_201_CREATED
)
async def create_order(
    order_data: OrderRequest,
    service: OrderService = Depends(get_order_service),
):
    return service.process_order(order_data)
