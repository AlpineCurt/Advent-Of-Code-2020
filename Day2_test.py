import unittest
import Day2

class TestDay2Part1(unittest.TestCase):
    
    def setUp(self):
        
        with open('day2_inputs.txt', 'r') as f:
            day2_list = f.readlines()
        
        day2_inputs = list(map(str.strip, day2_list))
        
    def test_day2_part1(self):
        
        self.assertTrue(Day2.day2_part1('1-3 a: abcde'))
        self.assertFalse(Day2.day2_part1('1-3 b: cdefg'))
        self.assertTrue(Day2.day2_part1('2-9 c: ccccccccc'))
    
    def test_day2_part2(self):
        
        self.assertTrue(Day2.day2_part2('1-3 a: abcde'))
        self.assertFalse(Day2.day2_part2('1-3 b: cdefg'))
        self.assertFalse(Day2.day2_part2('2-9 c: ccccccccc'))