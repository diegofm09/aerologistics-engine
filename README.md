# 🚚 Aerologistics Engine

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)

A script that helps you to manage your shipping fleet. Made with Python using Modular Object-Oriented Architecture

---

## 🛠 Tech Stacks and Concepts

- **Language:** Python 3.10+
- **Core Concepts:** Object Oriented Programming, Design Patterns, Modular Architecture, Type Hints, Error Handling...
- **Dependencies:** None (Uses Python Standard Library only)

---

## 🚀 Features

- **Object Oriented Programming:** Used to create classes and methods for a clean architecture using encapsulation, abstract classes, dunder methods and attributes...
- **Design Patterns:** It implements the factory, observer and strategy patterns
- **Data Persistence:** Automatically saves and load the fleet to the fleet.json file and logs them into app_log.txt
- **Advanced Menu:** Lots of options to analyze your fleet and packages
- **Clean Code:** Uses Type Hints and docstrings for easier readness
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
