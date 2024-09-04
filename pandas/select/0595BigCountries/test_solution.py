import unittest
import pandas as pd
from solution_v1 import big_countries

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('data.csv')

    def test_case_1(self):
        result = big_countries(self.df).reset_index(drop=True)
        expected = pd.read_csv('pandas/select/0595BigCountries/test.csv')
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
