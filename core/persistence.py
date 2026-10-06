from pathlib import Path
import json

class FleetRepository:
    """Repository class managing data persistence, file storage initialization,and JSON serialization/deserialization for the fleet system."""
    main_p = Path(__file__).resolve().parent.parent
    data_p = main_p/"data"
    core_p = main_p/"core"
    fleet_p = data_p/"fleet.json"
    app_log_p = data_p/"app_log.txt"
    waybill_export_p = data_p/"waybill_export.txt"

    def __init__(self) -> None:
        """Initializes the repository by ensuring the data directory and base files exist.If fleet.json is missing or empty, it initializes it with an empty list."""
        self.data_p.mkdir(parents=True, exist_ok=True)

        if not self.app_log_p.is_file():
            self.app_log_p.touch()

        if not self.waybill_export_p.is_file():
            self.waybill_export_p.touch()

        if not self.fleet_p.is_file() or self.fleet_p.stat().st_size == 0:
            with open(self.fleet_p, "w") as file1:
                json.dump([], file1, indent=2)

reporitory = FleetRepository()