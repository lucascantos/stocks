
import pandas as pd
from src.services.iex import IEX
from icecream import ic as print
iex = IEX()
class Stocks():
    def __init__(self, symbols_file='sp_500_stocks'):
        self.stocks = pd.read_csv(f'src/data/{symbols_file}csv')
    
    def make_batch(self):
        for symbol in range(0, len(self.stocks['Ticker']), 100):
            yield self.stocks['Ticker'][symbol:symbol+100] 

def make_batch(data):
    for symbol in range(0, len(data), 100):
        yield data[symbol:symbol+100] 

def batch_stocks():
    stocks = pd.read_csv('src/data/sp_500_stocks.csv')

    columns = ['ticker', 'price', 'cap', 'sharesBuy']
    df = pd.DataFrame(columns=columns)

    for batch in make_batch(stocks['Ticker']):
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

def batch_stats():
    stocks = pd.read_csv('src/data/sp_500_stocks.csv')
    df = pd.DataFrame()
    for batch in make_batch(stocks['Ticker']):
        batch_string = ','.join(batch)
        data = iex.batch(batch_string, 'price,stats')
        for ticker, stock in data.items():
            stock['stats'].update({
                'price': stock['price'],
                'ticker': ticker
            })
            df = df.append(pd.Series(stock['stats']), ignore_index=True)
    return df

def load(file, update=False):
    function_mapping = {
        'stocks_info': batch_stocks,
        'stats_info': batch_stats
    }
    func = function_mapping.get(file)

    if update:
        df = func()
        save(df, file)
        return df

    else:           
        try:
            df = pd.read_csv(f'src/data/{file}.csv')
        except FileNotFoundError:
            df = func()
            save(df, file)
        return df

def save(df, filename):
    df.to_csv(f'src/data/{filename}.csv')