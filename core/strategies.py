from abc import ABC, abstractmethod


class Shipping(ABC):
    """Abstract class for shipping strategy"""
    @abstractmethod
    def cost(self, km, kg) -> float:
        """Gets the cost of the shipping"""
        pass


class GroundShipping(Shipping):
    def cost(self, km, kg):
        if km<=0 or kg <=0:
            raise 
        return 10.0 + 1.4*km + 0.01*kg

class AirShipping(Shipping):
    def cost(self, km, kg):
        return 100 + 1.5*kg + 0.02*km

class DroneEcoShipping(Shipping):
    def cost(self, km, kg):
        return 2 + 0.15*km + 2*kg

class ShippingStrategy:
    def __init__(self, strategy):
        self.strategy = strategy

    def get_shipping_cost(self, km, kg):
        return self.strategy.cost(km, kg)
    