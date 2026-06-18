from datetime import date
from storage import save_data


def add_habit(habits, name, category):
    habits.append({
        "name": name,
        "category": category,
        "days": {},
        "xp": 0
    })

    save_data(habits)


def mark_done(habits, index):
    today = str(date.today())

    if index < 0 or index >= len(habits):
        print("Неверный номер")
        return

    habit = habits[index]

    if habit["days"].get(today):
        print("Уже выполнено сегодня")
        return

    habit["days"][today] = True
    habit["xp"] += 10

    save_data(habits)

    print("Выполнено! +10 XP")


def delete_habit(habits, index):
    if index < 0 or index >= len(habits):
        print("Неверный номер")
        return

    removed = habits.pop(index)

    save_data(habits)

    print(f"Удалено: {removed['name']}")