import unittest
import pandas as pd
# from gpt_solution import average_selling_price
from leetcode_solution import average_selling_price

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
        prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
        data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
        units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})
        result = average_selling_price(prices, units_sold).reset_index(drop=True)
        result['average_price'] = result['average_price'].astype('Float64')

        data = [[1, 6.96], [2, 16.96]]
        expected = pd.DataFrame(data, columns=['product_id', 'average_price']).astype({'product_id':'Int64', 'average_price':'Float64'})

        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_3(self):
        data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30], [3, '2019-02-21', '2019-03-31', 30]]
        prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
        data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
        units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})
        result = average_selling_price(prices, units_sold).reset_index(drop=True)
        result['average_price'] = result['average_price'].astype('Float64')

        data = [[1, 6.96], [2, 16.96], [3, 0]]
        expected = pd.DataFrame(data, columns=['product_id', 'average_price']).astype({'product_id':'Int64', 'average_price':'Float64'})

        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
