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
# from icecream import ic as print
from src.functions import stocks_data
from scipy import stats



# My info
portifolio_size = 100000 # How much you want to invest

df = stocks_data.load('stats_info', False)
df.sort_values(by='year1ChangePercent', ascending=False, inplace=True)
df.reset_index(inplace=True, drop=True)
df.set_index('ticker', inplace=True)
position_size = portifolio_size / len(df)
print (df)
df['maxShares'] = df['price'].apply(lambda x: math.floor(position_size/x) if x else -1)