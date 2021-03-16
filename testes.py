import pandas as pd

df = pd.DataFrame()

data_row = {
    'value': 0,
    'number': 'b'
}
row = pd.Series(data_row)
print(row)
df = df.append(row, ignore_index=True)
print(df)
