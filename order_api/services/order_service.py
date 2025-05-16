from order_api.models.item import Item
from order_api.models.order import Order
from order_api.models.schemas.order import OrderRequest, OrderResponse
from order_api.services.discount_strategies import (
    BlackFridayDiscount,
    DiscountStrategy,
)
from order_api.services.notifiers import EmailNotifier
from order_api.services.storage import OrderStorage

from .notifiers import Notifier


class OrderService:
    def __init__(
        self,
        notifier: Notifier,
        discount_strategy: DiscountStrategy,
        storage: OrderStorage,
    ):
        self.notifier = notifier
        self.discount_strategy = discount_strategy
        self.storage = storage

    def process_order(self, order_data: OrderRequest):
        order = Order()
        for item_data in order_data.items:
            item = Item(item_data.name, item_data.price, item_data.quantity)
            order.add_item(item)

        total = order.total()
        discounted_total = self.discount_strategy.apply_discount(total)

        self.storage.save(order)
        message = f"""Order processed.\n
                    Total after discount: ${discounted_total:.2f}"""
        self.notifier.send(message)

        return OrderResponse(
            total=total, discounted_total=discounted_total, message=message
        )


_order_storage = OrderStorage()


def get_order_service():
    return OrderService(
        notifier=EmailNotifier(),
        discount_strategy=BlackFridayDiscount(),
        storage=_order_storage,
    )
