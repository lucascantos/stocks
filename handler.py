'''
Statistics Algoriths
Machine learning
'''
from time import sleep
# import numpy as np
# import pandas as pd
# import xlsxwriter
import math
import requests
from icecream import ic as print
from src.functions import stocks_data
from scipy import stats

# ic(stocks)

portifolio_size = 100000 # How much you want to invest

df = stocks_data.load()

print(df)
position_size = portifolio_size / len(df)
for i in range(len(df)):
    df.loc[i, 'N° Shares to Buy'] = math.floor(position_size/df.loc[i, 'Stock Price'])

print(df)
print(position_size)