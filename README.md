# 💰 Expense Tracker

A simple command-line application for tracking personal expenses, written in Python. Add, edit, delete and search your expenses, see your total spending, and export everything to a CSV file.

## ✨ Features

- ➕ **Add** a new expense with a title, amount and category
- 📋 **View** all saved expenses
- ✏️ **Edit** an existing expense
- 🗑️ **Delete** an expense by its ID
- 🔍 **Search** an expense by its ID
- 📊 **Total** spending across all expenses
- 🏷️ **Categories** list to choose from
- 📁 **Export** all expenses to a CSV file
- ✅ **Input validation** (empty titles, invalid amounts, unknown categories)

## 📂 Project Structure

```
expense-tracker/
├── main.py          # Entry point: menu and user interaction
├── expenses.py      # Core logic: add, update, delete, search expenses
├── validation.py    # Input validation and the list of categories
├── reports.py       # Total calculation and CSV export
├── storage.py       # Loading and saving expense data
├── exception.py     # Custom error handling
└── data/            # Stored data and exported CSV files
```

## 🛠️ Requirements

- Python 3.8 or higher
- No external libraries needed (only the Python standard library)

## 🚀 Getting Started

1. **Clone or download** the project:
```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
```

2. **Make sure the `data/` folder exists** (it is used for storage and CSV export):
```bash
   mkdir data
```

3. **Run the program:**
```bash
   python main.py
```

## 📖 Usage

When you start the program, the main menu appears:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          💰 EXPENSE TRACKER 💰
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. ➕ Add Expense
2. 📋 Show All Expenses
3. ✏️ Edit Expense
4. 🗑️ Delete Expense
5. 🔍 Search Expense
6. 📊 Show Total Expense
7. 🏷️ Show Categories
8. 📁 Export to CSV

0. 🚪 Exit
```

Type the number of the option you want and press **Enter**.

### Example: Adding an expense

```
Choose: 1
Title: Lunch
Amount: 12.50
Categories: ['food', 'shopping', 'education', 'health', 'entertainment', 'other']
Category: food
Added! {'id': 'a1b2c3d4', 'title': 'Lunch', 'amount': 12.5, 'category': 'food', 'date': '2026-11-20'}
```

### Expense format

Each expense is stored with the following fields:

| Field      | Description                                   |
|------------|-----------------------------------------------|
| `id`       | Unique 8-character ID generated automatically |
| `title`    | Short description of the expense              |
| `amount`   | Positive number (stored as a float)           |
| `category` | One of the available categories               |
| `date`     | Date the expense was added (`YYYY-MM-DD`)     |

### Available categories

`food`, `shopping`, `education`, `health`, `entertainment`, `other`

You can add or change categories in the `CATEGORIES` list inside `validation.py`. Keep them in lowercase.

## ✅ Validation Rules

- **Title** cannot be empty.
- **Amount** must be a number greater than 0.
- **Category** must be one of the available categories.

If the input is invalid, an error message is shown and the program continues running.

## 📁 CSV Export

Choosing option **8** saves all expenses to `data/expenses.csv` with these columns:

```
id,title,amount,category,date
```

You can open the file in Excel, Google Sheets or any other spreadsheet program.

## 🔮 Future Improvements

- Filter expenses by category or date
- Monthly and category-based reports
- Keep the old value when editing (leave a field blank)
- Search by title instead of ID only
- Simple graphical interface

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Created by **Your Name**: [GitHub](https://github.com/your-username)
