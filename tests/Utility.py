import json
from pathlib import Path

def load_login_data():
    data_path = Path(__file__).parent.parent / "data" / "login_data.json"
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def get_test_id(scenario):
    return scenario.get("test_id", "unnamed_test")

def load_inventory_data():
    data_path = Path(__file__).parent.parent / "data" / "inventory_data.json"
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def get_sort_test_id(scenario):
    return scenario.get("test_id", "unnamed_sort_test")

def load_checkout_data():
    data_path = Path(__file__).parent.parent / "data" / "checkout_data.json"
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    return data