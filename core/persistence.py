from pathlib import Path
import json
from models import DeliveryVehicle
from typing import Any

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
        vehicle_list = [{"vehicle_id": i.vehicle_id, "max_weight_capacity": i.max_weight_capacity, "shipping_strategy": i.shipping_strategy, "used_weight": i.used_weight, "packages": i.packages} for i in vehicle_list]
        with open(self.fleet_p, "w", encoding="utf-8") as file3:
            json.dump(vehicle_list, file3, indent = 2)

    def load_fleet(self) -> list[dict[str, Any]]:
        """Loads the vehicle  list of the fleet.json file"""
        with open(self.fleet_p, "r", encoding="utf-8") as file4:
            return json.load(file4)

reporitory = FleetRepository()
