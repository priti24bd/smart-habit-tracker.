import json
from utils import suggest_habit, save_habit, load_habits

def main():
    print("Welcome to Smart Habit Tracker!")
    habits = load_habits()

    while True:
        print("\nMenu:")
        print("1. View Habits")
        print("2. Add Habit")
        print("3. Get Habit Suggestion")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if habits:
                print("Your habits:")
                for h in habits:
                    print(f"- {h}")
            else:
                print("No habits added yet.")
        elif choice == "2":
            habit = input("Enter the habit you want to add: ")
            save_habit(habit, habits)
            print(f"Habit '{habit}' added!")
        elif choice == "3":
            suggestion = suggest_habit()
            print(f"Suggestion for you: {suggestion}")
        elif choice == "4":
            print("Exiting. Stay productive!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
