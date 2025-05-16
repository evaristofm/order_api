from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"[EMAIL] {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"[SMS] {message}")
