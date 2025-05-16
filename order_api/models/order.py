from .item import Item


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def total(self):
        return sum(item.sub_total() for item in self.items)
