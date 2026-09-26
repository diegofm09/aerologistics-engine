from abc import ABC, abstractmethod
from exceptions import InvalidShipping


class ShippingStrategy(ABC):
    """Abstract class for shipping strategy"""
    @abstractmethod
    def cost(self, km, kg) -> float:
        """Gets the cost of the shipping"""
        pass


class GroundShipping(ShippingStrategy):
    def cost(self, km: float, kg: float):
        if km<=0 or kg <=0:
            raise InvalidShipping("The kg and km of the shipping must be higher than 0")
        return 10.0 + 1.4*km + 0.01*kg

class AirShipping(ShippingStrategy):
    def cost(self, km: float, kg: float):
        if km<=0 or kg <=0:
            raise InvalidShipping("The kg and km of the shipping must be higher than 0")
        return 100 + 1.5*kg + 0.02*km

class DroneEcoShipping(ShippingStrategy):
    def cost(self, km: float, kg: float):
        if km<=0 or km> 15 or kg <=0 or kg>3:
            raise InvalidShipping("The kg of the drone must be between 0 and 3 and the km between 0 and 15")
        return 2 + 0.15*km + 2*kg


    