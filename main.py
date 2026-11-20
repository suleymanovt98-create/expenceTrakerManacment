from expenses import *
from validation import CATEGORIES
from reports import *


def showMenu():
    print('~' * 40)
    print("          💰 EXPENSE TRACKER 💰")
    print('~' * 40)
    print()
    print("1. ➕ Add Expense")
    print("2. 📋 Show All Expenses")
    print("3. ✏️ Edit Expense")
    print("4. 🗑️ Delete Expense")
    print("5. 🔍 Search Expense")
    print("6. 📊 Show Total Expense")
    print("7. 🏷️ Show Categories")
    print("8. 📁 Export to CSV")
    print()
    print("0. 🚪 Exit")
    print()
    print('~' * 40)


while True:
    showMenu()
    choice = input("Choose")

    if choice == "1":
        title = input("Title")
        amount = input("Amount")
        print("Categories", CATEGORIES)
        category = input("Category")
        try:
            e = addExpense(title, amount, category)
            print("Added", e)
        except Exception as error:
            print("Error:", error)

    elif choice == "2":
        expenses = getAllExpeses()
        if len(expenses) == 0:
            print("No expenses")
        else:
            for e in expenses:
                print(e["id"], e["title"], e["amount"], e["category"], e["date"])

    elif choice == "3":
        id = input("Expense ID")
        title = input("New title")
        amount = input("New amount")
        print("Categories", CATEGORIES)
        category = input("New category")
        try:
            updateExpense(id, title, amount, category)
            print("Updated!")
        except Exception as err:
            print("Error", err)

    elif choice == "4":
        id = input("Expense ID:")
        try:
            deleteExpense(id)
            print("Deleted!")
        except Exception as err:
            print("Error:", err)

    elif choice == "5":
        id = input("Expense ID:")
        try:
            e = SearchExpenses(id)
            print(e["id"], e["title"], e["amount"], e["category"], e["date"])
        except Exception as err:
            print("Error:", err)

    elif choice == "6":
        print("Total:", totalExpenses())

    elif choice == "7":
        for c in CATEGORIES:
            print("-", c)

    elif choice == "8":
        try:
            path = exportToCSV()
            print("Exported to", path)
        except Exception as err:
            print("Error:", err)

    elif choice == "0":
        print("sagolun")
        break

    else:
        print("sehv secim")

    print()