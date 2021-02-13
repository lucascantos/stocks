
import pandas as pd
from src.services.iex import IEX

iex = IEX()
def load_from_api():
    stocks = pd.read_csv('src/data/sp_500_stocks.csv')
    columns = ['Ticker', 'Stock Price', 'Market Cap', 'N° Shares to Buy']
    df = pd.DataFrame(columns=columns)
    for symbol in range(0, len(stocks['Ticker']), 100):
        batch = stocks['Ticker'][symbol:symbol+100] 
        batch_string = ','.join(batch)
        data = iex.batch(batch_string)
        for ticker, stock in data.items():
            df = df.append(pd.Series([
                ticker,
                stock['quote']['latestPrice'],
                stock['quote']['marketCap'],
                None
                ],  index=columns), ignore_index=True)
    return df

def load(update=False):
    if update:
        df = load_from_api()
        save(df)
        return df
    else:           
        try:
            df = pd.read_csv('src/data/stocks_info.csv')
        except FileNotFoundError:
            df = load_from_api()
            save(df)
        return df

def save(df, filename='stocks_info.csv'):
    df.to_csv(f'src/data/{filename}')