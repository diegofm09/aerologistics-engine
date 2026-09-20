from dataclasses import dataclass
from abc import ABC, abstractmethod
import exceptions

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
            raise exceptions.InvalidPackageError
        self.__weight_kg = new_weight

    @destination_zip.setter
    def destination_zip(self, new_zip: str) -> None:
        self.__destination_zip = new_zip

    @length.setter
    def length(self, new: float) -> None:
        if new > 0:
            self.__length = new
        else:
            raise exceptions.InvalidPackageError

    @width.setter
    def width(self, new: float) -> None:
        if new > 0:
            self.__width = new
        else:
            raise exceptions.InvalidPackageError

    @height.setter
    def height(self, new: float) -> None:
        if new > 0:
            self.__height = new
        else:
            raise exceptions.InvalidPackageError

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
        return f" ---------------\nPackage ID: {self.__package_id}\n -Weight: {self.__weight_kg}kg\n -Destination Zip: {self.__destination_zip}\n -Status: {"Delivered" if self.__delivered else "Undelivered"} \n---------------"

    def __eq__(self, other) -> bool:
        return self.__package_id == other.package_id

    def __lt__(self, other) -> bool:
        return self.__weight_kg < other.weight_kg

    def __gt__(self, other) -> bool:
        return self.__weight_kg > other.weight_kg

    def __add__(self, other) -> float:
        return self.__weight_kg + other.weight_kg


class StandardPackage(BasePackage):
    def __init__(self, package_id, weight_kg, destination_zip, length, width, height):
        pass

    

    