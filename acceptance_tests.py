import pytest


def test_criterion_1_module_import():
    import expense_tracker


def test_criterion_2_add_expense():
    from expense_tracker import add_expense
    result = add_expense('food', 10.50)
    assert isinstance(result, dict)
    assert 'amount' in result


def test_criterion_3_get_expenses():
    from expense_tracker import get_expenses
    expenses = get_expenses()
    assert isinstance(expenses, list)


def test_criterion_4_calculate_total():
    from expense_tracker import calculate_total
    total = calculate_total()
    assert isinstance(total, (int, float))
