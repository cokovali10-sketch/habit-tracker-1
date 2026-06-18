from datetime import date

from storage import load_data
from habit_manager import (
    add_habit,
    mark_done,
    delete_habit
)
from statistics import (
    show_stats,
    get_streak
)

habits = load_data()


def show_habits():
    today = str(date.today())

    print("\nПРИВЫЧКИ")

    if not habits:
        print("Пока нет привычек")
        return

    for i, habit in enumerate(habits, 1):
        status = "✔" if habit["days"].get(today) else "✖"

        print(
            f"{i}. "
            f"{habit['name']} "
            f"[{habit['category']}] "
            f"{status} "
            f"XP:{habit['xp']} "
            f"🔥{get_streak(habit)}"
        )


while True:
    print("\n====== HABIT TRACKER ======")
    print("1 - добавить")
    print("2 - список")
    print("3 - отметить")
    print("4 - статистика")
    print("5 - удалить")
    print("0 - выход")

    choice = input(">>> ")

    if choice == "1":
        name = input("Название: ")
        category = input("Категория: ")

        add_habit(habits, name, category)

    elif choice == "2":
        show_habits()

    elif choice == "3":
        num = int(input("Номер привычки: "))
        mark_done(habits, num - 1)

    elif choice == "4":
        show_stats(habits)

    elif choice == "5":
        num = int(input("Номер привычки: "))
        delete_habit(habits, num - 1)

    elif choice == "0":
        break

    else:
        print("Неизвестная команда")