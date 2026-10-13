from abc import ABC, abstractmethod
from typing import Any
from core.utils import LoggerMixin

class DeliveryObserver(ABC):
    @abstractmethod
    def update(self, event: str, data: Any):
        pass


class DeliverySubject:
    def __init__(self):
        self._observers = []

    @property
    def observers(self):
        return list(self._observers)

    def attach(self, new: DeliveryObserver):
        """Adds a subscriptor"""
        if new not in self.observers:
            self._observers.append(new)

    def detach(self, old: DeliveryObserver):
        """Deletes a subscriptor"""
        self._observers.remove(old)

    def notify(self, event: str, data: Any):
        """Notifies all subscriptors"""
        for i in self._observers:
            i.update(event, data)


class CustomerSMSListener(DeliveryObserver):
    """A listener that prints the observer update in the terminal"""
    def update(self, event: str, data: Any):
        print(f"{event}: {data}")

class LogisticsAuditListener(DeliveryObserver, LoggerMixin):
    """A listener that logs the observer update in app_log.txt"""
    def update(self, event: str, data: str):
        self.log_event(f"{event}: {data}")
    
