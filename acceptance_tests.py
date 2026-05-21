import pytest
from expense_tracker import ExpenseTracker, add_expense, get_expenses, calculate_total


def test_module_import():
    # Criterion 1: Module exists and can be imported
    assert True


def test_add_expense():
    # Criterion 2: add_expense adds an expense and returns dict
    tracker = ExpenseTracker()
    exp = tracker.add_expense(50.0, "food")
    assert exp["amount"] == 50.0
    assert exp["category"] == "food"
    assert exp["id"] == 1


def test_get_expenses():
    # Criterion 3: get_expenses returns list of expenses
    tracker = ExpenseTracker()
    tracker.add_expense(10, "cat")
    assert len(tracker.get_expenses()) == 1


def test_calculate_total():
    # Criterion 4: calculate_total returns sum of amounts
    tracker = ExpenseTracker()
    tracker.add_expense(10, "a")
    tracker.add_expense(20, "b")
    assert tracker.calculate_total() == 30
