import unittest
from solution import crawler
import os 


class TestSolution(unittest.TestCase):
    
    def test_func(self):
        res = crawler('task1.html')
        self.assertEqual(res.Get_all_Data(),1)

    def test_DatafileExits(self):
        self.assertTrue(os.path.exists('data.json'))

if __name__ == '__main__':
    unittest.main()