import unittest
import Day3

class TestDay3(unittest.TestCase):
    
    def setUp(self):
        
        with open('Day3_test_inputs.txt', 'r') as f:
            day3_test_list = f.readlines()
        day3_test_inputs = list(map(str.strip, day3_test_list))
        
        with open('day3_inputs.txt', 'r') as f:
            day3_list = f.readlines()
        day3_inputs = list(map(str.strip, day3_list))
        
        self.day3_test_tree_repeating = Day3.tree_repeat(day3_test_inputs)
    
    def test_tree_repeat(self):
        
        self.assertEqual(Day3.tree_hit_count(self.day3_test_tree_repeating, 3, 1), 7)
        self.assertEqual(Day3.tree_hit_count(self.day3_test_tree_repeating, 1, 1), 2)
        self.assertEqual(Day3.tree_hit_count(self.day3_test_tree_repeating, 5, 1), 3)
        self.assertEqual(Day3.tree_hit_count(self.day3_test_tree_repeating, 7, 1), 4)
        self.assertEqual(Day3.tree_hit_count(self.day3_test_tree_repeating, 1, 2), 2)
        
        self.assertEqual(Day3.tree_hit_count(self.day3_test_tree_repeating, 3, 1) *
                         Day3.tree_hit_count(self.day3_test_tree_repeating, 1, 1) *
                         Day3.tree_hit_count(self.day3_test_tree_repeating, 5, 1) *
                         Day3.tree_hit_count(self.day3_test_tree_repeating, 7, 1) *
                         Day3.tree_hit_count(self.day3_test_tree_repeating, 1, 2), 336)