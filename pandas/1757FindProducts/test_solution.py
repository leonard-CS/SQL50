import unittest
import pandas as pd
from solution_v1 import find_products

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('data.csv')
    
    def test_case_1(self):
        result = find_products(self.df)
        data = {'product_id': [1, 3]}
        expected = pd.DataFrame(data)
        assert(result, expected)

if __name__ == "__main__":
    unittest.main()
