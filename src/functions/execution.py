'''
Once decided which asset, if the asset is worth it and how much to buy/sell,
Theses strategies decide the best way to implement the action
'''
import pandas as pd
from src.functions.trends import moving_average
def twap(df):
    '''
    time weighted average price
    effect, reduce impact on market

    avg(open,close,low,high)
    avg_28days = avg(avg_day[1...28])

    if order_price > avg28:
        return overvalued
    else:
        return undervalued

    Ou seja...dividir meu order de 10**100
    em pedaços onde o pedaçoe seja proximo ao avg28
    '''

    data = {
        'daily_twap': df[['close', 'open', 'low', 'high']].mean(axis=1)
    }
    data.update({'twap': moving_average(data['daily_twap'],28,None)})
    return pd.DataFrame(data)

def vwap(df):
    pass