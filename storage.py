import json

FILE = "habits.json"


def load_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_data(habits):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(habits, f, indent=4, ensure_ascii=False)