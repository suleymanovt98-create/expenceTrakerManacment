import csv
from expenses import getAllExpeses

def totalExpenses():
    expenses = getAllExpeses()

    total = 0

    for e in expenses:
        total += e ["amount"]

    return total

def exportToCSV():
    expenses = getAllExpeses()

    filePath = "data/expenses.csv"                        

    fileNames = ["id", "title", "amount", "category", "date"]

    with open (filePath, 'w', newline="", encoding= 'utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fileNames)  
        writer.writeheader()
        writer.writerows(expenses)

    return filePath