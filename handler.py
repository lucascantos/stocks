'''
Statistics Algoriths
Machine learning
'''
from time import sleep
import numpy as np
import pandas as pd
import xlsxwriter
import math
import requests
from icecream import ic as print
from src.services.iex import IEX

# ic(stocks)

iex = IEX()
portifolio_size = 100000 # How much you want to invest

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

def load_data(update=False):
    if update:
        df = load_from_api()
        df.to_csv('src/data/stocks_info.csv')
        return df
    else:           
        try:
            df = pd.read_csv('src/data/stocks_info.csv')
        except FileNotFoundError:
            df = load_from_api()
            df.to_csv('src/data/stocks_info.csv')
        return df

df = load_data()
print(df)
position_size = portifolio_size / len(df)
for i in range(len(df)):
    df.loc[i, 'N° Shares to Buy'] = math.floor(position_size/df.loc[i, 'Stock Price'])

print(df)
print(position_size)