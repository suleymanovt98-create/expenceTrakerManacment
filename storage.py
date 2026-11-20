import json

DATA_FILE ="data/ expenses.json"


def loadExpenses():
    try:
        with open (DATA_FILE, 'r', encoding='UTF-8') as file:
            expeses = json.load(file)

        return expeses

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        raise ValueError('Json file is corrupted')


def saveExpenses(expenses):
    with open (DATA_FILE, 'w', encoding='UTF-8') as file:
        json.dump(expenses, file, indent=4, ensure_ascii= False)
