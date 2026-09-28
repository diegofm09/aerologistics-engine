from abc import ABC, abstractmethod
from typing import Any
from utils import LoggerMixin

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
    def update(self, event: str, data: Any):
        print(f"{event}: {data}")

class LogisticsAuditListener(DeliveryObserver, LoggerMixin):
    def update(self, event: str, data: str):
        self.log_event(f"{event}: {data}")
    
