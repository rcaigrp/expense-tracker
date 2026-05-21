import unittest
import sys
sys.path.insert(0, '/workspace/projects')
from expense_tracker import parse_expenses

class TestExpenseTracker(unittest.TestCase):
    def test_criterion_1_module_exists(self):
        import expense_tracker
        self.assertIsNotNone(expense_tracker)

    def test_criterion_2_parse_expenses(self):
        expenses = [
            {'amount': 10.0, 'category': 'food', 'date': '2024-01-01'},
            {'amount': 20.0, 'category': 'transport', 'date': '2024-01-02'}
        ]
        result = parse_expenses(expenses)
        self.assertEqual(result['total'], 30.0)
        self.assertEqual(result['by_category']['food'], 10.0)
        self.assertEqual(result['by_category']['transport'], 20.0)
        self.assertEqual(result['by_date']['2024-01-01'], 10.0)
        self.assertEqual(result['by_date']['2024-01-02'], 20.0)

if __name__ == '__main__':
    unittest.main()