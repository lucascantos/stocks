import pandas as pd

df = pd.DataFrame()
x = pd.Series([i for i in range(10)])
y = pd.Series([2,1,0])

w = 5
p = 5

m = w /(p+1)

k = x.rolling(p).mean()
y = x.ewm(alpha=m).mean()
z = x.ewm(span=p).mean()
print(y==k)
