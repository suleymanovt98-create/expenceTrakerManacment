import uuid
from datetime import date
from storage import *
from validation import *
from exception import expensesNotFound

def addExpense(title, amount, category):
    expenses = loadExpenses()


    expense = {

        
        "id": str(uuid.uuid4())[:8],
        "title":validateTitle(title),
        'amount':validateAmoun(amount),
        "category":validateCatecory(category),
        "date":date.today().isoformat()


    }

    expenses.append(expense)
    saveExpenses(expenses)

    return expense

def getAllExpeses():
    return loadExpenses()

def SearchExpenses(expenseID):
    expeses = loadExpenses()
    for e in expeses:
        if e ["id"] == expenseID:
            return e

    expensesNotFound()


def updateExpense(expenseID, title, amount, category):
    expenses = loadExpenses()
    for e in expenses:
            if e ["id"] == expenseID:
                e ["title"] = validateTitle(title)
                e ["amount"] = validateAmoun(amount)
                e ["category"] = validateCatecory(category)

                saveExpenses(expenses)


    expensesNotFound()



def deleteExpense(expenseID):
     expenses = loadExpenses()

     for e in expenses:
      
      if e ["id"] == expenseID:
          expenses.remove(e)

          saveExpenses()

          return True


     expensesNotFound()

