import exceptions as e
from pathlib import Path
from datetime import datetime, timedelta
import time
from typing import Any, Callable, Generator
from functools import wraps
import random


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


def get_date_str() -> str:
    """Gets the current date and time and returns it as a string"""
    current_time = datetime.now()
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return current_time


class LoggerMixin:
    """Mixin used to make all child classes inherit the log_event method"""
    def log_event(self, message: str) -> None:
        """Logs an event and writes it down onto the app log"""

        times = get_date_str()

        with open(app_log_p, "a") as file1:
            file1.write(f"[{times}] {message}\n")


def audit_execution(function: Callable[..., Any]) -> Callable[..., Any]:
    """Writes the function used and the ms it took on app log"""
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        current_date = get_date_str()
        initial_time = time.perf_counter()

        try:
            result = function(*args, **kwargs)

            final_time = time.perf_counter() - initial_time

            with open(app_log_p, "a") as file2:
                file2.write(f"[{current_date}] SUCCESS: Function {function.__name__} executed in {round(final_time*1000, 3)}ms\n")

            return result
                

        except Exception as e:
            with open(app_log_p, "a") as file2:
                file2.write(f"[{current_date}] ERROR: {e}\n")
            raise e
             
    return wrapper


def fuel_price_simulator(seed_value: int | None = None) -> Generator[float, None, None]:
    """Generates a random variation of the oil price between -3.5 and 3.5"""
    if seed_value is not None:
        random.seed(seed_value)
    while True:
        variation = round(random.uniform(-3.5, 3.5), 2)
        yield variation

def calculate_delivery_windows() -> dict[str, str]:
    """Returns what day it is going to be in 3, 7 and 15 days"""
    actual_date = datetime.now()
    thr_days = (timedelta(days = 3) + actual_date).strftime("%Y-%m-%d")
    sev_days = (timedelta(days = 7) + actual_date).strftime("%Y-%m-%d")
    fift_days = (timedelta(days = 15) + actual_date).strftime("%Y-%m-%d")
    return {"express": thr_days, "standard": sev_days, "cheap": fift_days}

