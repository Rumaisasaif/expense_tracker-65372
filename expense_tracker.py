import datetime

expenses = []

def add_expense():
    print("\n---- Add New Expense ----")
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')  # Validate date format
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    category = input("Enter category (e.g., Food, Travel, Bills, Other): ")
    amount = input("Enter amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    print("\n---- All Expenses ----")
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']} | Description: {exp['description']}")
    print()

def total_by_category():
    print("\n---- Total Expenses by Category ----")
    category = input("Enter category: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"Total expenses for {category}: ${total:.2f}\n")

def delete_expense():
    print("\n---- Delete Expense ----")
    view_expenses()
    try:
        idx = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            print(f"Deleted expense: {removed['description']} (${removed['amount']})\n")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def main_menu():
    while True:
        print("========== Expense Tracker ==========")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Total Expenses by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main_menu()
