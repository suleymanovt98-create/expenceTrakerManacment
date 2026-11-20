from exception import *


CATEGORIES = [
    "food",                  
    "shopping",
    "education",
    "health",
    "entertainment",         
    "other"
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
        invalidExpense("Amount must be greater than 0")   

    return amount


def validateCatecory(catogory):
    catogory = catogory.strip().lower()

    if catogory not in CATEGORIES:
        invalidExpense("invalid category")             

    return catogory