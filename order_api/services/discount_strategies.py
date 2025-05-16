from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, valor: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, valor: float) -> float:
        return valor


class BlackFridayDiscount(DiscountStrategy):
    def apply_discount(self, valor: float) -> float:
        return valor * 0.7
