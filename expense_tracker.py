import json
from pathlib import Path

FILE_NAME = "expenses.json"


def load_expenses():
    file = Path(FILE_NAME)

    if file.exists():
        try:
            with open(file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY): ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()
    amount = float(input("Enter amount: "))

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- Expense Records -----")

    for number, expense in enumerate(expenses, start=1):
        print(f"\nExpense {number}")
        print(f"Date        : {expense['date']}")
        print(f"Category    : {expense['category']}")
        print(f"Description : {expense['description']}")
        print(f"Amount      : ₹{expense['amount']:.2f}")


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ₹{total:.2f}")


def search_by_category(expenses):
    category = input("Enter category to search: ").strip().lower()
    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"{expense['date']} | "
                f"{expense['description']} | "
                f"₹{expense['amount']:.2f}"
            )
            found = True

    if not found:
        print("No expenses found in this category.")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))
        if 1 <= number <= len(expenses):
            expenses.pop(number - 1)
            save_expenses(expenses)
            print("Expense deleted successfully.")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Search by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            search_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
