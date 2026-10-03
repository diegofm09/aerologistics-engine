from typing import Generator, Callable
from models import DeliveryVehicle, BasePackage, Any

def packages_extractor(vehicle_list: list[DeliveryVehicle], filter_type: str = None) -> Generator[BasePackage, None, None]:
    """A generator that yields every package in a vehicle list, it can be filtered"""
    for vehicle in vehicle_list:
        for package in vehicle.packages:
            if filter_type is None or package.get_package_type() == filter_type:
                yield package


def create_weight_checker(max_limit: float) -> Callable[[BasePackage], bool]:
    def check_weight(package: BasePackage):
        return package.weight_kg > max_limit
    return check_weight


def calculate_fleet_weight(vehicle_list: list[DeliveryVehicle]) -> dict[str: Any]:
    """Returns a dict with the total weight of packages between all the vehicles, the heavier and the lighter packages"""
    packages = list(packages_extractor(vehicle_list))
    total_weight = sum(packages, 0.0)
    max_weight = max(packages) if packages else None
    min_weight = min(packages) if packages else None
    return {"total_weight": total_weight, "max_weight": max_weight.weight_kg, "min_weight": min_weight.weight_kg}

def filter_packages_weight(vehicle_list: list[DeliveryVehicle], min: float = 0.0, max:float = float("inf")) -> list[tuple[str]]:
    """Returns all the packages heavier than min, of a list of vehicles in a legible str with its vehicle id"""
    packages = []
    for vehicle in vehicle_list:
        for package in vehicle.packages:
            packages.append((vehicle.vehicle_id, package))
    filtered_packages = list(filter(lambda x: min < x[1].weight_kg < max, packages))
    str_packages = list(map(lambda x: (f"Package {x[1].package_id}: {x[1].weight_kg}kg", x[0]), filtered_packages))
    return str_packages

def get_urgent_packages_destination(package_list: list[BasePackage]) -> list[str]:
    return [package.destination_zip for package in package_list if package.get_package_type() == "Express Package"]

def get_all_zipcodes(package_list: list[BasePackage]) -> list[str]:
    return {package.destination_zip for package in package_list}



