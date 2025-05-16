from typing import List

from pydantic import BaseModel

from order_api.models.schemas.item import ItemRequest


class OrderRequest(BaseModel):
    items: List[ItemRequest]


class OrderResponse(BaseModel):
    total: float
    discounted_total: float
    message: str
