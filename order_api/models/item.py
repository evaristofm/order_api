class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sub_total(self):
        return self.price * self.quantity
