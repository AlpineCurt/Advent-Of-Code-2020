import unittest
import Day4

class TestDay4(unittest.TestCase):
    
    def setUp(self):
        
        with open('day4_inputs.txt', 'r') as f:
            day4_text = f.read()        
        
        self.passports = Day4.text_to_dicts(day4_text)
        
        self.person1 = {'ecl':'gry', 'pid':'860033327', 'eyr':'2020', 'hcl':'#fffffd', 'byr':'1937', 'iyr':'2017', 'cid':'147', 'hgt':'183cm'}
        self.person2 = {'iyr':'2013', 'ecl':'amb', 'cid':'350', 'eyr':'2023', 'pid':'028048884', 'hcl':'#cfa07d', 'byr':'1929'}
        self.person3 = {'hcl':'#ae17e1',  'iyr':'2013',  'eyr':'2024',  'ecl':'brn',  'pid':'760753108', 'byr':'1931',  'hgt':'179cm'}
        self.person4 = {'hcl':'#cfa07d', 'eyr':'2025', 'pid':'166559648', 'iyr':'2011', 'ecl':'brn', 'hgt':'59in'}
    
    def test_valid_passport(self):
        
        self.assertIn('ecl', self.person1)
        self.assertNotIn('hgt', self.person2)
        self.assertNotIn('cid', self.person3)
        self.assertNotIn('cid', self.person4)
        self.assertNotIn('byr', self.person4)
        
        self.assertTrue(Day4.valid_passport(self.person1))
        self.assertFalse(Day4.valid_passport(self.person2))
        self.assertTrue(Day4.valid_passport(self.person3))
        self.assertFalse(Day4.valid_passport(self.person4))