def moving_average(df):
    train_size = 0.6
    for sma_length in range(20,500):    
        df['SMA'] = df['Close'].rolling(sma_length).mean()
        df['input'] = [int(x) for x in df['Close'] > df['SMA']]
        
        df = df.dropna()
        training = df.head(int(train_size * df.shape[0]))
        test = df.tail(int((1 - train_size) * df.shape[0]))
        
        tr_returns = training[training['input'] == 1]['Forward Return']
        test_returns = test[test['input'] == 1]['Forward Return']
        mean_forward_return_training = tr_returns.mean()
        mean_forward_return_test = test_returns.mean()
        pvalue = ttest_ind(tr_returns,test_returns,equal_var=False)[1]
        
        result.append({
            'sma_length':sma_length,
            'training_forward_return': mean_forward_return_training,
            'test_forward_return': mean_forward_return_test,
            'p-value':pvalue
        })