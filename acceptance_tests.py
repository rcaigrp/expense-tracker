import pytest
from expense_tracker import add_expense, get_expenses, calculate_total, expenses

@pytest.fixture(autouse=True)
def clear_expenses_fixture():
    expenses.clear()

def test_criterion_1_module_import():
    assert add_expense is not None
    assert get_expenses is not None
    assert calculate_total is not None

def test_criterion_2_add_expense():
    result = add_expense(50.0, "food", "lunch")
    assert isinstance(result, dict)
    assert result["amount"] == 50.0
    assert result["category"] == "food"

def test_criterion_3_get_expenses():
    result = get_expenses()
    assert isinstance(result, list)

def test_criterion_4_calculate_total():
    add_expense(100.0, "rent")
    total = calculate_total()
    assert total == 100.0
