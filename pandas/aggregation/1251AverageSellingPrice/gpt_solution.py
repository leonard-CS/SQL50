import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(units_sold, prices, on='product_id', how='left')
    merged = merged[(merged['purchase_date'] >= merged['start_date']) & (merged['purchase_date'] <= merged['end_date'])]
    merged['revenue'] = merged['units'] * merged['price']
    agg = merged.groupby(by='product_id').agg(
        total_units=pd.NamedAgg(column='units', aggfunc='sum'),
        total_revenue=pd.NamedAgg(column='revenue', aggfunc='sum')
    ).reset_index()
    agg['average_price'] = (agg['total_revenue'] / agg['total_units']).round(2)
    return agg[['product_id', 'average_price']]

if __name__ == '__main__':
    data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
    prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
    data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
    units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})

    result = average_selling_price(prices, units_sold)
    print(result)
