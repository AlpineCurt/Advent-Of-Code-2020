import unittest
import Day6

class TestDay6(unittest.TestCase):
    
    def setUp(self):
        
        self.day6_input_text = Day6.openFormatInput('Day6_test_inputs.txt')
        #self.day6_yes_answer_list = Day6.uniqueChars(self.day6_input_text)
        self.day6_input_text_part2 = Day6.openFormatInput_Part2('Day6_test_inputs.txt')
    
    def test_openFormatInput(self):
        
        self.assertEqual(self.day6_input_text[0], 'abc')
        self.assertEqual(self.day6_input_text[1], 'abc')
        self.assertEqual(self.day6_input_text[2], 'abac')
        self.assertEqual(self.day6_input_text[3], 'aaaa')
        self.assertEqual(self.day6_input_text[4], 'b')
    
    def test_uniqueChars(self):
        
        self.assertEqual(Day6.uniqueChars(self.day6_input_text[0]), 3)
        self.assertEqual(Day6.uniqueChars(self.day6_input_text[1]), 3)
        self.assertEqual(Day6.uniqueChars(self.day6_input_text[2]), 3)
        self.assertEqual(Day6.uniqueChars(self.day6_input_text[3]), 1)
        self.assertEqual(Day6.uniqueChars(self.day6_input_text[4]), 1)
        
    def test_totalYeses(self):
        
        self.assertEqual(Day6.totalYeses(self.day6_input_text), 11)
        
    def test_openFormatInput_Part2(self):
        
        self.assertEqual(self.day6_input_text_part2[0], ['abc'])
        self.assertEqual(self.day6_input_text_part2[1], ['a', 'b', 'c'])
        self.assertEqual(self.day6_input_text_part2[2], ['ab', 'ac'])
        self.assertEqual(self.day6_input_text_part2[3], ['a', 'a', 'a', 'a'])
        self.assertEqual(self.day6_input_text_part2[4], ['b'])
    
    def test_find_same_chars(self):
        
        self.assertEqual(Day6.find_same_chars(self.day6_input_text_part2[0]), 3)
        self.assertEqual(Day6.find_same_chars(self.day6_input_text_part2[1]), 0)
        self.assertEqual(Day6.find_same_chars(self.day6_input_text_part2[2]), 1)
        self.assertEqual(Day6.find_same_chars(self.day6_input_text_part2[3]), 1)
        self.assertEqual(Day6.find_same_chars(self.day6_input_text_part2[4]), 1)