from datetime import date, timedelta

def get_level(xp):
    return xp // 100 + 1
def get_streak(habit):
    streak = 0
    current_day = date.today()

    while True:
        day_str = str(current_day)

        if habit["days"].get(day_str):
            streak += 1
            current_day -= timedelta(days=1)
        else:
            break

    return streak


def show_stats(habits):
    print("\nСТАТИСТИКА")
    total_xp = 0

    for habit in habits:
        done = sum(1 for v in habit["days"].values() if v)
        total = len(habit["days"])

        percent = (done / total * 100) if total else 0

        streak = get_streak(habit)

        total_xp += habit["xp"]
        level = get_level(habit["xp"])

        print(f"Уровень: {level}")

        print(f"\n{habit['name']}")
        print(f"XP: {habit['xp']}")
        print(f"Streak: {streak}")
        print(f"Успешность: {percent:.1f}%")

    print(f"\nОбщий XP: {total_xp}")