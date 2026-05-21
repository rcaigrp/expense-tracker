class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount: float, category: str) -> dict:
        expense = {
            "id": len(self.expenses) + 1,
            "amount": amount,
            "category": category
        }
        self.expenses.append(expense)
        return expense

    def get_expenses(self) -> list:
        return self.expenses.copy()

    def calculate_total(self) -> float:
        return sum(e["amount"] for e in self.expenses)


# Module-level convenience
_tracker = ExpenseTracker()

def add_expense(amount, category):
    return _tracker.add_expense(amount, category)

def get_expenses():
    return _tracker.get_expenses()

def calculate_total():
    return _tracker.calculate_total()
