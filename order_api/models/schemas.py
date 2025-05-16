from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    quantity: int


class ItemRequest(Item):
    pass


class OrderRequest(BaseModel):
    items: List[ItemRequest]


class OrderResponse(BaseModel):
    total: float
    discounted_total: float
    message: str
