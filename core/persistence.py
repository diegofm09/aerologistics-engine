from pathlib import Path
import json
from core.models import DeliveryVehicle
from typing import Any
from core.factories import PackageFactory
from core.strategies import GroundShipping, AirShipping, DroneEcoShipping
from core.models import Waybill

class FleetRepository:
    """Repository class managing data persistence, file storage initialization, and JSON serialization/deserialization for the fleet system."""
    main_p = Path(__file__).resolve().parent.parent
    data_p = main_p/"data"
    core_p = main_p/"core"
    fleet_p = data_p/"fleet.json"
    app_log_p = data_p/"app_log.txt"
    waybill_export_p = data_p/"waybill_export.txt"
    config_p = main_p/"config.json"
    default_config = {"max_fleet_capacity": 50, "fuel_price_base": 1.50, "currency": "EUR", "system_version": "1.0.0"}

    def __init__(self) -> None:
        """Initializes the repository by ensuring the data directory and base files exist. If fleet.json is missing or empty, it initializes it with an empty list."""
        self.data_p.mkdir(parents=True, exist_ok=True)

        if not self.app_log_p.is_file():
            self.app_log_p.touch()

        if not self.waybill_export_p.is_file():
            self.waybill_export_p.touch()

        if not self.fleet_p.is_file() or self.fleet_p.stat().st_size == 0:
            with open(self.fleet_p, "w", encoding="utf-8") as file1:
                json.dump([], file1, indent=2)
        
        try:
            if self.config_p.is_file() and self.config_p.stat().st_size == 0:
                self.config_p.unlink()
            with open(self.config_p, "w", encoding="utf-8") as file2:
                json.dump(self.default_config, file2, indent=2)
        except Exception:
            pass

    def save_fleet(self, vehicle_list: list[DeliveryVehicle]) -> None:
        """Saves the vehicle list in the fleet.json file"""
        final_vehicle_list = []
        for i in vehicle_list:
            v = {"vehicle_id": i.vehicle_id, "max_weight_capacity": i.max_weight_capacity, "shipping_strategy": (i.shipping_strategy.__class__.__name__), "used_weight": i.used_weight, "packages": []}
            for x in i.packages:
                p = {"package_id": x.package_id, "weight_kg": x.weight_kg, "destination_zip": x.destination_zip, "length": x.length, "width": x.width, "height": x.height, "delivered": x.delivered}
                p_type = x.get_package_type()
                if p_type == "Standard Package":
                    p["type"] = "standard"
                    v["packages"].append(p)
                elif p_type == "Express Package":
                    p["urgency_level"] = x.urgency_level
                    p["type"] = "express"
                    v["packages"].append(p)
                elif p_type == "Refrigerated Package":
                    p["target_temp_celsius"] = x.target_temp_celsius
                    p["type"] = "refrigerated"
                    v["packages"].append(p)
            final_vehicle_list.append(v)

        with open(self.fleet_p, "w", encoding="utf-8") as file3:
            json.dump(final_vehicle_list, file3, indent = 2)

    def load_fleet(self) -> list[DeliveryVehicle]:
        """Loads the vehicle  list of the fleet.json file"""
        with open(self.fleet_p, "r", encoding="utf-8") as file4:
            raw_fleet_list = json.load(file4)
            vehicles_list = []
            for v in raw_fleet_list:
                packages_list = []
                for p in v["packages"]:
                    p_type = p["type"]
                    p.pop("type")
                    package = PackageFactory.create_package(p_type, **p)
                    packages_list.append(package)

                if v["shipping_strategy"] == "GroundShipping":
                    v["shipping_strategy"] = GroundShipping()
                elif v["shipping_strategy"] == "AirShipping":
                    v["shipping_strategy"] = AirShipping()
                elif v["shipping_strategy"] == "DroneEcoShipping":
                    v["shipping_strategy"] = DroneEcoShipping()

                vehicle = DeliveryVehicle(v["vehicle_id"], v["max_weight_capacity"], v["shipping_strategy"])
                for i in packages_list:
                    vehicle.add_package(i)
                vehicles_list.append(vehicle)
        return vehicles_list

    def export_waybill(self, waybill: Waybill) -> None:
        """Exports a waybill object to waybill_export.txt"""
        with open(self.waybill_export_p, "a", encoding="utf-8") as file5:
            file5.write(f" ------------------------\n Waybill {waybill.waybill_id}\n From {waybill.sender} to {waybill.destination}\n Issued date: {waybill.issued_date}\n Final price: {waybill.final_cost}$\n ------------------------\n")

