import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta
import json

FILE = "habits.json"


# =========================
# DATA
# =========================

def load_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

            for h in data:
                h.setdefault("days", {})
                h.setdefault("xp", 0)
                h.setdefault("category", "general")

            return data
    except:
        return []


def save_data():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(habits, f, indent=4, ensure_ascii=False)


habits = load_data()


# =========================
# CORE FEATURES
# =========================

def get_streak(habit):
    streak = 0
    current = date.today()

    while True:
        d = str(current)

        if habit["days"].get(d):
            streak += 1
            current -= timedelta(days=1)
        else:
            break

    return streak


def get_level(xp):
    return xp // 100 + 1


def progress(habit):
    done = sum(1 for v in habit["days"].values() if v)
    total = len(habit["days"])
    return (done / total * 100) if total else 0


# =========================
# ACTIONS
# =========================

def refresh():
    listbox.delete(0, tk.END)

    today = str(date.today())

    for h in habits:
        bar = "█" * int(progress(h) / 10)
        streak = get_streak(h)

        listbox.insert(
            tk.END,
            f"{h['name']} | XP:{h['xp']} | Lvl:{get_level(h['xp'])} | 🔥{streak} | {bar}"
        )


def add():
    name = entry.get().strip()
    category = category_var.get()

    if not name:
        return

    habits.append({
        "name": name,
        "category": category,
        "days": {},
        "xp": 0
    })

    entry.delete(0, tk.END)
    save_data()
    refresh()


def done():
    sel = listbox.curselection()
    if not sel:
        return

    h = habits[sel[0]]
    today = str(date.today())

    if h["days"].get(today):
        messagebox.showinfo("Info", "Already done today")
        return

    h["days"][today] = True
    h["xp"] += 10

    save_data()
    refresh()


def delete():
    sel = listbox.curselection()
    if not sel:
        return

    habits.pop(sel[0])

    save_data()
    refresh()


def show_stats():
    total_xp = sum(h["xp"] for h in habits)
    total_habits = len(habits)

    messagebox.showinfo(
        "Stats",
        f"Habits: {total_habits}\nXP: {total_xp}\nAvg XP: {total_xp // total_habits if total_habits else 0}"
    )


# =========================
# UI DESIGN (IMPROVED)
# =========================

root = tk.Tk()
root.title("Habit Tracker PRO v5")
root.geometry("600x750")
root.configure(bg="#0f172a")


title = tk.Label(
    root,
    text="🔥 HABIT TRACKER PRO",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=10)


# INPUT
entry = tk.Entry(root, font=("Arial", 14), bg="#1e293b", fg="white")
entry.pack(pady=5, ipadx=10, ipady=5)


# CATEGORY
category_var = tk.StringVar(value="general")

cat_frame = tk.Frame(root, bg="#0f172a")
cat_frame.pack()

tk.Label(cat_frame, text="Category:", bg="#0f172a", fg="white").pack(side=tk.LEFT)

tk.OptionMenu(cat_frame, category_var, "sport", "study", "health", "work").pack(side=tk.LEFT)


# BUTTONS
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=10)


def btn(text, color, cmd):
    return tk.Button(btn_frame, text=text, command=cmd,
                     bg=color, fg="white", width=12)


btn("Add", "#3b82f6", add).grid(row=0, column=0, padx=5)
btn("Done", "#22c55e", done).grid(row=0, column=1, padx=5)
btn("Delete", "#ef4444", delete).grid(row=0, column=2, padx=5)
btn("Stats", "#a855f7", show_stats).grid(row=0, column=3, padx=5)


# LIST
listbox = tk.Listbox(
    root,
    width=70,
    height=25,
    bg="#111827",
    fg="white",
    selectbackground="#3b82f6"
)
listbox.pack(pady=20)


refresh()

root.mainloop()