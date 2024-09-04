import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].apply(len) > 15][['tweet_id']]

if __name__ == '__main__':
    data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
    tweets = pd.DataFrame(
        data, columns=['tweet_id', 'content']
    ).astype({
        'tweet_id':'Int64',
        'content':'object',
    })

    tweets.to_csv('data.csv', index=False)
    result = invalid_tweets(tweets)
    print(result)
