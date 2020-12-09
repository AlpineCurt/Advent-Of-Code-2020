import unittest
import Day7

class TestDay7(unittest.TestCase):
    
    def setUp(self):
        
        self.testRules = Day7.BagRules('Day7_test_inputs.txt')
        
    def test_createRules(self):
        
        self.assertIn('light red', self.testRules.ruleDict)
        self.assertIn('muted yellow', self.testRules.ruleDict)
        self.assertIn('dotted black', self.testRules.ruleDict)
        
        self.assertIn('shiny gold', self.testRules.ruleDict['bright white'])
        self.assertIn('shiny gold', self.testRules.ruleDict['muted yellow'])
        self.assertIn('faded blue', self.testRules.ruleDict['dark olive'])
    
    def test_searchBag(self):
        
        self.assertTrue(self.testRules.searchBag('light red', 'shiny gold'))
        self.assertTrue(self.testRules.searchBag('dark orange', 'shiny gold'))
        self.assertTrue(self.testRules.searchBag('muted yellow', 'shiny gold'))
        self.assertTrue(self.testRules.searchBag('bright white', 'shiny gold'))
        
        self.assertEqual(self.testRules.searchBag('faded blue', 'shiny gold'), None)
        self.assertEqual(self.testRules.searchBag('dark olive', 'light red'), None)
    
    def test_countBags(self):
        
        self.assertEqual(self.testRules.countBags('shiny gold'), 4)