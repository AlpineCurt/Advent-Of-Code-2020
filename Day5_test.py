import unittest
import Day5

class TestDay5(unittest.TestCase):
    
    def setUp(self):
        
        self.boardingPass1 = 'BFFFBBFRRR'
        self.boardingPass2 = 'FFFBBBFRRR'
        self.boardingPass3 = 'BBFFBBFRLL'
        self.boardingPass4 = 'FBFBBFFRLR'
    
    def test_findSeatRowCol(self):
        
        self.assertEqual(Day5.findSeatRowCol(self.boardingPass1), (70, 7))
        self.assertEqual(Day5.findSeatRowCol(self.boardingPass2), (14, 7))
        self.assertEqual(Day5.findSeatRowCol(self.boardingPass3), (102, 4))
        self.assertEqual(Day5.findSeatRowCol(self.boardingPass4), (44, 5))
    
    def test_calcSeatID(self):
        pass1 = Day5.findSeatRowCol(self.boardingPass1)
        self.assertEqual(Day5.calcSeatID(pass1), 567)
        pass2 = Day5.findSeatRowCol(self.boardingPass2)
        self.assertEqual(Day5.calcSeatID(pass2), 119)
        pass3 = Day5.findSeatRowCol(self.boardingPass3)
        self.assertEqual(Day5.calcSeatID(pass3), 820)
        pass4 = Day5.findSeatRowCol(self.boardingPass4)
        self.assertEqual(Day5.calcSeatID(pass4), 357)        