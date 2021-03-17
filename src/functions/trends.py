from scipy.stats import ttest_ind

def moving_average(df):
    n_days = 2
    df['forwardClose'] = df['close'].shift(-n_days)
    df['forwardReturn'] = (df['forwardClose'] - df['close'])/df['close']


    train_size = 0.6
    results = []

    for sma_length in range(20,500):    
        df['SMA'] = df['close'].rolling(sma_length).mean()
        df['input'] = [int(x) for x in df['close'] > df['SMA']]
        
        df = df.dropna()
        training = df.head(int(train_size * df.shape[0]))
        test = df.tail(int((1 - train_size) * df.shape[0]))
        
        tr_returns = training[training['input'] == 1]['forwardReturn']
        test_returns = test[test['input'] == 1]['forwardReturn']
        mean_forward_return_training = tr_returns.mean()
        mean_forward_return_test = test_returns.mean()
        pvalue = ttest_ind(tr_returns,test_returns,equal_var=False)[1]
        
        result = {
            'sma_length':sma_length,
            'training_forward_return': mean_forward_return_training,
            'test_forward_return': mean_forward_return_test,
            'p-value': pvalue 
        }
        #P-value: >5% = Good, <5% = Overfitting. Market not stable?
        results.append(result)
    results.sort(key = lambda x : -x['training_forward_return'])
    yield from results
