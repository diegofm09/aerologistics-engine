import exceptions as e
from pathlib import Path
from datetime import datetime
from typing import Any


main_p = Path(__file__).resolve().parent.parent
data_p = main_p/"data"
app_log_p = data_p/"app_log.txt"



def inspect_component(obj: Any) -> None:
    """Prints the object dunder atributes"""
    name = getattr(obj, "__name__", None) or obj.__class__.__name__
    doc = getattr(obj, "__doc__", None)
    module = getattr(obj, "__module__", None)
    qualname = getattr(obj, "__qualname__", None) or obj.__class__.__qualname__
    dicti = getattr(obj, "__dict__", None)
    slots = getattr(obj, "__slots__", None)
    print(f"{obj}:\n -Name: {name}\n -Docstring: {doc}\n -Module: {module}\n -Qual Name: {qualname}\n -Dict: {dicti}\n -Slots: {slots}")


class LoggerMixin:
    """Mixin used to make all child classes inherit the log_event method"""

    def log_event(self, message: str) -> None:
        """Logs an event and writes it down onto the app log"""

        current_time = datetime.now()

        current_time = current_time.strftime("%Y/%m/%d %H:%M:%S")

        with open(app_log_p, "a") as file1:
            file1.write(f"[{current_time}] {message}\n")

