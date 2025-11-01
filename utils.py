import json
import random

def load_habits():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_habit(habit, habits):
    habits.append(habit)
    with open("habits.json", "w") as f:
        json.dump(habits, f, indent=4)

def suggest_habit():
    suggestions = [
        "Drink 8 glasses of water",
        "Read 20 pages of a book",
        "Meditate for 10 minutes",
        "Exercise for 30 minutes",
        "Write your daily goals",
        "Take a short walk",
        "Learn a new word in English"
    ]
    return random.choice(suggestions)
