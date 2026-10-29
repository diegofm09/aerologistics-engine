# 🚚 Aerologistics Engine

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)

A robust command-line interface (CLI) application designed to manage and optimize shipping fleets and package logistics. Made with Python using Modular Object-Oriented Architecture

---

## 🛠 Tech Stacks and Concepts

- **Language:** Python 3.10+
- **Core Concepts:** Object Oriented Programming, Design Patterns, Modular Architecture, Type Hints, Error Handling...
- **Dependencies:** None (Uses Python Standard Library only)

---

## 🛠 CLI Overview
  1) Vehicle Fleet Management (Vehicles, strategies, costs)

  2) Package Management (Standard, express, refrigerated)

  3) Configuration

  4) Analysis & Reports Panel (Weights, filters, zipcodes)

  5) Waybill Management & Exportation

  6) Events & Audit System (Observer logs & app_log.txt)

---

## 🚀 Features

- **Object Oriented Programming:** Used to create classes and methods for a clean architecture using encapsulation, abstract classes, dunder methods and attributes...
- **Advanced Python Optimizations:** Implementation of `@dataclass` (with `frozen=True` and `__post_init__`), memory optimization via `__slots__`, and custom execution-auditing decorators.
- **Design Patterns:**
    - **Strategy pattern** for shipping costs (Ground, Air, Drone)
    - **Factory pattern** for package instantiation (PackageFactory)
    - **Observer pattern** for event logging and notifications.
- **Data Persistence:** Automatically saves and loads the fleet to the fleet.json file and logs them into app_log.txt
- **Advanced Menu:** Comprehensive analytics dashboard with advanced filtering and data aggregation capabilities
- **Dynamic Configuration:** Adjust system parameters on the fly via JSON (fleet capacity limits, fuel price base, and currency selection).
- **Clean Code:** Uses Type Hints and docstrings for easier readability
- **Robust Error Handling with Custom Exceptions:** Prevents crashes from invalid inputs, missing files, or empty data lists, using a custom exceptions class

---

## 📂 Project Structure

```text
aerologistics-engine/
├── main.py
├── config.json
├── core/
│   ├── __init__.py
│   ├── analytics.py
│   ├── exceptions.py
│   ├── factories.py
│   ├── observers.py
│   ├── persistence.py
│   ├── strategies.py
│   ├── utils.py
│   └── models.py
└── data/
    ├── app_log.txt
    ├── waybill_export.txt
    └── fleet.json
```

---

## 💻 How to Run

1. **Clone the repository (or download the files):**

   ```bash
   git clone https://github.com/diegofm09/aerologistics-engine.git

   ```

2. **Run main.py:**
   ```bash
   python main.py
   ```
