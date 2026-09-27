from abc import ABC, abstractmethod

class DeliveryObserver(ABC):
    @abstractmethod
    def update(self, event: str):
        pass

class DeliverySubject:
    pass