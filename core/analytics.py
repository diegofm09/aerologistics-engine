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
    return {"total_weight": total_weight, "max_weight": max_weight, "min_weight": min_weight}
