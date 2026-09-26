from dataclasses import dataclass
from abc import ABC, abstractmethod
import exceptions
from typing import Any

@dataclass(frozen=True)
class Waybill:
    """A Waybill class with inmutable atributes"""
    waybill_id: str
    sender: str
    destination: str
    issued_date: str
    final_cost: float

    def __post_init__(self):
        object.__setattr__(self, "waybill_id", self.waybill_id.strip())
        object.__setattr__(self, "sender", self.sender.strip())
        object.__setattr__(self, "destination", self.destination.strip())
        object.__setattr__(self, "issued_date", self.issued_date.strip())

        if self.final_cost <= 0:
            raise ValueError("The final cost must be higher than 0")

        if self.sender == "":
            raise ValueError("The Waybill must have a sender")


class GPSPoint:
    """Creates a GPS Point"""
    __slots__ = ("latitude", "longitude", "timestamp", "speed")
    def __init__(self, latitude: float, longitude: float, timestamp: str, speed: float) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.speed = speed


class BasePackage(ABC):
    """An abstract class that works as a base for all the package types"""
    def __init__(self, package_id: str, weight_kg: float, destination_zip: str, length: float, width: float, height: float) -> None:
        self.__package_id: str = package_id
        self.weight_kg = weight_kg
        self.__destination_zip: str = destination_zip
        self.length = length
        self.width = width
        self.height = height
        self.__delivered: bool = False

    @property
    def length(self) -> float:
        return self.__length

    @property
    def width(self) -> float:
        return self.__width

    @property
    def height(self) -> float:
        return self.__height

    @property
    def package_id(self) -> str:
        return self.__package_id

    @property
    def weight_kg(self) -> float:
        return self.__weight_kg

    @property
    def destination_zip(self) -> str:
        return self.__destination_zip

    @property
    def delivered(self) -> bool:
        return self.__delivered

    @weight_kg.setter
    def weight_kg(self, new_weight: float) -> None:
        if new_weight <= 0:
            raise exceptions.InvalidPackageError("The weight and dimensions must be higher than 0")
        self.__weight_kg = new_weight

    @destination_zip.setter
    def destination_zip(self, new_zip: str) -> None:
        self.__destination_zip = new_zip

    @length.setter
    def length(self, new: float) -> None:
        if new > 0:
            self.__length = new
        else:
            raise exceptions.InvalidPackageError("The weight and dimensions must be higher than 0")

    @width.setter
    def width(self, new: float) -> None:
        if new > 0:
            self.__width = new
        else:
            raise exceptions.InvalidPackageError("The weight and dimensions must be higher than 0")

    @height.setter
    def height(self, new: float) -> None:
        if new > 0:
            self.__height = new
        else:
            raise exceptions.InvalidPackageError("The weight and dimensions must be higher than 0")

    @destination_zip.deleter
    def destination_zip(self) -> None:
        self.__destination_zip = None

    @abstractmethod
    def calculate_volume(self) -> float:
        """Calculates the package volume"""
        pass

    @abstractmethod
    def get_package_type(self) -> str:
        """Gets the package type"""
        pass

    def __str__(self) -> str:
        return f" ---------------\nPackage ID: {self.__package_id}\n -Weight: {self.__weight_kg}kg\n -Destination Zip: {self.__destination_zip}\n -Status: {'Delivered' if self.__delivered else 'Undelivered'}\n -Dimensions: {self.length}*{self.width}*{self.height}cm \n---------------"

    def __eq__(self, other) -> bool:
        return self.__package_id == other.package_id

    def __lt__(self, other) -> bool:
        return self.__weight_kg < other.weight_kg

    def __gt__(self, other) -> bool:
        return self.__weight_kg > other.weight_kg

    def __add__(self, other) -> float:
        if isinstance(other, (float, int)):
            return self.__weight_kg + other
        elif isinstance(other, BasePackage):
            return self.__weight_kg + other.weight_kg
        return NotImplemented


class StandardPackage(BasePackage):
    """The standard package class"""
    def calculate_volume(self) -> float:
        return self.width * self.length * self.height

    def get_package_type(self) -> str:
        return "Standard Package"

    def __repr__(self):
        return f"StandardPackage(package_id={self.package_id}, weight_kg={self.weight_kg}, destination_zip={self.destination_zip}, length={self.length}, width={self.width}, height={self.height}, delivered={self.delivered})"


class ExpressPackage(BasePackage):
    """The express package class"""

    def __init__(self, package_id: str, weight_kg: float, destination_zip: str, length: float, width: float, height: float, urgency_level: int) -> None:
        super().__init__(package_id, weight_kg, destination_zip, length, width, height)
        self.urgency_level = urgency_level

    @property
    def urgency_level(self) -> int:
        return self.__urgency_level

    @urgency_level.setter
    def urgency_level(self, new: int) -> None:
        if new >= 1 and new <= 5:
            self.__urgency_level = new
        else:
            raise exceptions.InvalidUrgencyLevel("The urgency level must be an integrer between 1 and 5")

    def calculate_volume(self) -> float:
        level = 1.0 + self.urgency_level * 0.05
        return (self.width * self.length * self.height)*level

    def get_package_type(self) -> str:
        return "Express Package"

    def __repr__(self):
        return f"ExpressPackage(package_id={self.package_id}, weight_kg={self.weight_kg}, destination_zip={self.destination_zip}, length={self.length}, width={self.width}, height={self.height}, delivered={self.delivered}, urgency_level={self.urgency_level})"

    
class RefrigeratedPackage(BasePackage):
    """The Refrigerated Package Class"""
    def __init__(self, package_id: str, weight_kg: float, destination_zip: str, length: float, width: float, height: float, target_temp_celsius: float) -> None:
        super().__init__(package_id, weight_kg, destination_zip, length, width, height)
        self.target_temp_celsius = target_temp_celsius

    @property
    def target_temp_celsius(self) -> float:
        return self.__target_temp_celsius

    @target_temp_celsius.setter
    def target_temp_celsius(self, new: float) -> None:
        if new<-50.0 or new>5.0:
            raise exceptions.InvalidTemperatureTarget("The temperature target must be between -50.0 and 5.0")
        else:
            self.__target_temp_celsius = new

    def calculate_volume(self) -> float:
        if -50.0 <= self.target_temp_celsius <-30.0:
            temp_level = 1.5
        elif -30.0 <= self.target_temp_celsius <-10.0:
            temp_level = 1.35
        elif -10.0 <= self.target_temp_celsius <0.0:
            temp_level = 1.2
        elif 0 <= self.target_temp_celsius <= 5.00:
            temp_level = 1.1
        return (self.height*self.width*self.length)*temp_level

    def get_package_type(self) -> str:
        return "Refrigerated Package"

    def __repr__(self):
        return f"RefrigeratedPackage(package_id={self.package_id}, weight_kg={self.weight_kg}, destination_zip={self.destination_zip}, length={self.length}, width={self.width}, height={self.height}, delivered={self.delivered}, target_temp_celsius={self.target_temp_celsius})"


class DeliveryVehicle:
    """Delivery Vehicle class"""
    def __init__(self, truck_id: str, max_weight_capacity: float, shipping_strategy: Any) -> None:
        self.__truck_id = truck_id
        self.max_weight_capacity = max_weight_capacity
        self.shipping_strategy = shipping_strategy
        self.__used_weight = 0
        self.__packages = []

    @property
    def truck_id(self) -> str:
        return self.__truck_id

    @property
    def max_weight_capacity(self) -> float:
        return self.__max_weight_capacity

    @property
    def shipping_strategy(self) -> str:
        return self.__shipping_strategy

    @property
    def packages(self) -> list:
        return list(self.__packages)

    @property
    def used_weight(self) -> float:
        return self.__used_weight

    @max_weight_capacity.setter
    def max_weight_capacity(self, new: float) -> None:
        if 0.5 > new or 50000 < new:
            raise exceptions.VehicleWeightError("The vehicle's weight capacity must be between 0.5 and 50000")
        self.__max_weight_capacity = new

    @shipping_strategy.setter
    def shipping_strategy(self, new: str) -> None:
        self.__shipping_strategy = new

    def add_package(self, package):
        """Adds a package to packages"""
        if (self.used_weight + package.weight_kg) <= self.max_weight_capacity:
            self.__packages.append(package)
            self.__used_weight += package.weight_kg
        else:
            raise exceptions.OverweightLimitError("The vehicle's weight limit has been exceeded")

    def delete_package(self, id):
        """Deletes a package from packages"""
        sol = 0
        for i in self.packages:
            if i.package_id == id:
                self.__packages.remove(i)
                self.__used_weight -= i.weight_kg
                sol = 1
                break
        print("Deleted" if sol == 1 else "Not found")

    def get_shipping_cost(self, km: float) -> float:
        return self.shipping_strategy.cost(km, self.used_weight)
            

    def __len__(self) -> int:
        return len(self.packages)

    def __contains__(self, item) -> bool:
        if isinstance(item, str):
            return any(package.package_id == item for package in self.packages)
        if isinstance(item, BasePackage):
            return item in self.packages
        return False