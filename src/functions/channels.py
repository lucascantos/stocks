# https://www.investopedia.com/terms/d/donchianchannels.asp#:~:text=The%20Difference%20Between%20Donchian%20Channels,for%20N%20periods%20X%202.
'''
?: How much above/below 0 is worth buy/sell? Season? days<threshold? 
?: Measure which company this is worth it. Worth it on season? 
?: are there other params more accurate?
'''

from src.functions.trends import moving_average
import pandas as pd

def bollinger(df, period, std=2, column='close'):
    data = {
        'upper': moving_average(df, 20) + (std*df[column].rolling(period).std()),
        'lower': moving_average(df, 20) - (std*df[column].rolling(period).std()),
        'middle':  moving_average(df, 20)
    }
    return pd.DataFrame(data)

def donchian(df, period, column='close'):   
    '''
    buy/sell trigger: close - middle. > OR < 0
    ''' 
    data = {
        'upper': df[column].rolling(period).max(),
        'lower': df[column].rolling(period).min(),
    }
    data['middle'] = (data['upper']+data['lower'])/2
    return pd.DataFrame(data)

def macd(df):
    '''
    buy/sell trigger: Signal-MACD. >0=B, <0=S
    Crossing MACD and Signal can tell to buy/sell stock
    https://www.investopedia.com/terms/m/macd.asp
    '''
    data = {
    'short_ema': moving_average(df, 12, 2),
    'long_ema': moving_average(df, 20, 2)
    }
    data.update({'macd': data['short_ema'] - data['long_ema']})
    data.update({'signal': moving_average(data['macd'], 9, 2, None)})
    return pd.DataFrame(data)    