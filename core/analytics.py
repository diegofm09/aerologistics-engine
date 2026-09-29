from typing import Generator
from models import DeliveryVehicle, BasePackage

def packages_extractor(vehicle_list: list[DeliveryVehicle], filter_type: str = None) -> Generator[BasePackage, None, None]:
    """A generator that yields every package in a vehicle list, it can be filtered"""
    for vehicle in vehicle_list:
        for package in vehicle.packages:
            if filter_type is None or package.get_package_type() == filter_type:
                yield package
                

            