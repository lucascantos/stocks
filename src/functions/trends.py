from scipy.stats import ttest_ind

def moving_average(df):
    '''
    For a given stock, gives the best Simple Moving Average period
    '''

    
    train_size = 0.6
    for n_days in range(2, 50):      
        results = []      
        subdf = df.copy()
        subdf['forwardClose'] = subdf['close'].shift(-n_days)
        subdf['forwardReturn'] = (subdf['forwardClose'] - subdf['close'])/subdf['close']
        for sma_length in range(20,500):    
            subdf['SMA'] = subdf['close'].rolling(sma_length).mean()
            subdf['input'] = [int(x) for x in subdf['close'] > subdf['SMA']]
            
            subdf = subdf.dropna()
            training = subdf.head(int(train_size * subdf.shape[0]))
            test = subdf.tail(int((1 - train_size) * subdf.shape[0]))
            
            tr_returns = training[training['input'] == 1]['forwardReturn']
            test_returns = test[test['input'] == 1]['forwardReturn']
            mean_forward_return_training = tr_returns.mean()
            mean_forward_return_test = test_returns.mean()
            pvalue = ttest_ind(tr_returns,test_returns,equal_var=False)[1]
            
            result = {
                'sma_length':sma_length,
                'training_forward_return': mean_forward_return_training,
                'test_forward_return': mean_forward_return_test,
                'p-value': round(pvalue*100,2)
            }
            #P-value: >5% = Good, <5% = Overfitting. Market not stable?
            results.append(result)
        results.sort(key = lambda x : -x['training_forward_return'])
        yield n_days, results[0]
