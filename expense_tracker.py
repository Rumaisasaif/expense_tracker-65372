import datetime

expenses = []

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    try:
        return float(amount_str)
    except ValueError:
        return None

def add_expense():
    print("\n---- Add New Expense ----")
    
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("❌ Invalid date format. Please use YYYY-MM-DD.\n")
        return
    
    category = input("Enter category (e.g., Food, Travel, Bills, Other): ").strip()
    if not category:
        print("❌ Category cannot be empty.\n")
        return
    
    amount_str = input("Enter amount: ")
    amount = validate_amount(amount_str)
    if amount is None or amount <= 0:
        print("❌ Invalid amount. Please enter a positive number.\n")
        return

    description = input("Enter description: ").strip()
    
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("✅ Expense added successfully!\n")

def view_expenses():
    print("\n---- All Expenses ----")
    if not expenses:
        print("ℹ️ No expenses recorded yet.\n")
        return
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']:.2f} | Description: {exp['description']}")
    print()

def total_by_category():
    print("\n---- Total Expenses by Category ----")
    category = input("Enter category: ").strip()
    if not category:
        print("❌ Category cannot be empty.\n")
        return
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"💰 Total expenses for '{category}': ${total:.2f}\n")

def delete_expense():
    print("\n---- Delete Expense ----")
    if not expenses:
        print("ℹ️ No expenses to delete.\n")
        return

    view_expenses()
    try:
        idx = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= idx < len(expenses):
            removed = expenses[idx]
            confirm = input(f"Are you sure you want to delete '{removed['description']}' (${removed['amount']:.2f})? (y/n): ")
            if confirm.lower() == 'y':
                expenses.pop(idx)
                print("🗑️ Expense deleted successfully.\n")
            else:
                print("❌ Deletion cancelled.\n")
        else:
            print("❌ Invalid expense number.\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")

def main_menu():
    while True:
        print("\n========== Expense Tracker ==========")
        print("1. ➕ Add New Expense")
        print("2. 📄 View All Expenses")
        print("3. 📊 Total Expenses by Category")
        print("4. 🗑️ Delete an Expense")
        print("5. 🚪 Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
