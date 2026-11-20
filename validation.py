from exception import *


categories = [

  "Food",
   "Shopping",
    "Education",
    "Health",
    "Entertaliment",
    "Other"




]

def validateTitle(title):
    title = title.strip()

    if not title:
        invalidExpense("title cannot be empty")

    return title

def validateAmoun(amount):
    try:
        amount = float(amount)

    except ValueError:
        invalidExpense("Amount must be a number")

    if amount <= 0:
        invalidExpense("Amount must be grater than 0 ")


    return amount


