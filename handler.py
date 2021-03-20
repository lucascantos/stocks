'''
Statistics Algoriths
Machine learning
'''
# from time import sleep
# import numpy as np
# import pandas as pd
# import xlsxwriter
# import requests
import matplotlib.pyplot as plt
# from icecream import ic as print
import math
from src.functions import stocks_data

from src.functions import trends
from src.functions import channels



# My info
portifolio_size = 100000 # How much you want to invest

# df = stocks_data.load('stats_info')
# df.sort_values(by='year1ChangePercent', ascending=False, inplace=True)
# df.reset_index(inplace=True, drop=True)
# df.set_index('ticker', inplace=True)
# position_size = portifolio_size / len(df)
# print(df)
# df['maxShares'] = df['price'].apply(lambda x: math.floor(position_size/x) if x else -1)


df = stocks_data.load('chart_info', False, **{'symbol': 'SPY', 'range': '10y'})
df.set_index('date', inplace=True)
position_size = portifolio_size / len(df)
df['maxShares'] = df['close'].apply(lambda x: math.floor(position_size/x) if x else -1)
print(df.columns)



# # MACD
# result = channels.macd(df)
# df[['short_ema', 'long_ema', 'macd', 'signal']] = result

# df = df[-100:]
# print(result)

# fig, axs = plt.subplots(2)
# fig.suptitle('Vertically stacked subplots')
# axs[0].plot(df['close'])
# axs[1].plot(df[['macd', 'signal']])
# plt.show()

## BOLLINGER BAND
# result = channels.bollinger(df, 30)
# df[['donMax', 'donMin', 'donAvg']] = result
# result = df.copy()
# print(result)

# fig, ax = plt.subplots()
# result = result[-365:]
# ax.plot(result[['close', 'donMax', 'donMin', 'donAvg']])
# plt.show()



## SIMPLE MOVING AVERAGE
# subdf = df[df['ticker']=='ZTS']
# print(subdf.head())
# results = trends.moving_average(df)

# f_result = next(results)
# df['SMA'] = df['close'].rolling(f_result['sma_length']).mean()

# fig, ax = plt.subplots()
# ax.plot(df['close'])
# ax.plot(df['SMA'])
# plt.show()