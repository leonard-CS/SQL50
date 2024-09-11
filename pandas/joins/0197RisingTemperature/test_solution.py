import unittest
import pandas as pd
from solution_v2 import rising_temperature

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
        weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})
        result = rising_temperature(weather).reset_index(drop=True)
        
        data = [[2], [4]]
        expected = pd.DataFrame(data, columns=['id']).astype({'id':'Int64'}).reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected)

    def test_case_2(self):
        data = [[1, '2000-12-14', 3], [2, '2000-12-16', 5]]
        weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})
        result = rising_temperature(weather).reset_index(drop=True)

        data = []
        expected = pd.DataFrame(data, columns=['id']).astype({'id':'Int64'}).reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
