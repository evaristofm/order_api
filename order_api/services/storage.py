from typing import List

from order_api.models.order import Order


class OrderStorage:
    def __init__(self):
        self.orders: List[Order] = []

    def save(self, order: Order):
        self.orders.append(order)

    def list_orders(self):
        return self.orders
