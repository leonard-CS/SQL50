import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    result = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())]
    return result[['name']]

if __name__ == "__main__":
    data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
    customer = pd.DataFrame(
        data,
        columns=['id', 'name', 'referee_id']
    ).astype({
        'id':'Int64', 
        'name':'object', 
        'referee_id':'Int64'
    })
    customer.to_csv('data.csv', index=False)
    result = find_customer_referee(customer)
    print(result)
