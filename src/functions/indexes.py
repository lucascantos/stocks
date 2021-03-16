
import pandas as pdf
from scipy import stats
import math
def momentum(df):
    # MOMENTUM CALCULATION
    '''
    Decididor do quão bom é uma empresa baseado no ganho em todos os periodos.
    High Quality = Slow and upward momentum
    Low Quality = Spikes
    '''

    percent_values = [
        'year1Return', 
        'month6Return', 
        'month3Return', 
        'month1Return'
        ]

    for v in percent_values:
        df[f'{v}%'] = df[v].apply(lambda x: stats.percentileofscore(df[v], x)) # Ranking System of value
    df['hqm'] = df[[f'{v}%' for v in percent_values]].mean(axis=1) # High Quality Momentum
    df.sort_values(by='hqm', ascending=False, inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df