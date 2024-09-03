import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return result_df[['product_id']]

if __name__ == "__main__":
    data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
    products = pd.DataFrame(
        data,
        columns=['product_id', 'low_fats', 'recyclable']
    ).astype({
        'product_id':'int64',
        'low_fats':'category',
        'recyclable':'category'
    })
    products.to_csv('data.csv', index=False)
    print(find_products(products))
