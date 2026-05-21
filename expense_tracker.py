expenses = []

def add_expense(amount, category, description=""):
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    return expense

def get_expenses():
    return expenses.copy()

def calculate_total():
    return sum(exp["amount"] for exp in expenses)