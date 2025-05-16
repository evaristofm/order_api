from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    quantity: int


class ItemRequest(Item):
    pass
