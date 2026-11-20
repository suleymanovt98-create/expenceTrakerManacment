def expensesNotFound():
    raise LookupError("Expense not found!")
 
def invalidExpense(message):
    raise ValueError(message)
 