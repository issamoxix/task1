import unittest
from solution import crawler
import os 
import json

class TestSolution(unittest.TestCase):
    
    def test_func(self):
        res = crawler('task1.html')
        self.assertEqual(res.Get_all_Data(),1)

    def test_DatafileExits(self):
        self.assertTrue(os.path.exists('data.json'))

    def test_jsonDataFile(self):
        file = open('data.json','r')
        data = json.load(file)
        self.assertNotEqual(len(data),0)

if __name__ == '__main__':
    unittest.main()