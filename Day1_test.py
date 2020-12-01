'''Test case for Day1'''

import unittest
import Day1

class TestExpenseReport(unittest.TestCase):
    
    def test_expense_report(self):
        
        report = [1721, 979, 366, 299, 675, 1546]
        
        self.assertEqual(Day1.expense_report(report), 514579)
        self.assertEqual(Day1.expense_report_part2(report), 241861950)