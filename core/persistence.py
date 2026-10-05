from pathlib import Path
import json

class FleetRepository:
    main_p = Path(__file__).parent.parent
    data_p = main_p/"data"
    core_p = main_p/"core"
    fleet_p = data_p/"fleet.json"
    app_log_p = data_p/"app_log.txt"
    waybill_export_p = data_p/"waybill_export.txt"


