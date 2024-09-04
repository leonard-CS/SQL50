import unittest
import pandas as pd
from solution_v1 import find_customer_referee

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('data.csv')
    
    def test_case_1(self):
        print(self.df)
        result = find_customer_referee(self.df)
        data = {'name': ['Will', "Jane", "Bill", "Zack"]}
        expected = pd.DataFrame(data)
        assert(result, expected)

if __name__ == "__main__":
    unittest.main()
