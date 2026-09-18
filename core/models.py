from dataclasses import dataclass

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