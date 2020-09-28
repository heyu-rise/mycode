import pandas as pd

df = pd.DataFrame({"A": [5, 3, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]})
df['E'] = df['A'] + df['C']
print(df)
df['G'] = df['A'] + 5
print(df)
df['H'] = df['A'] > df['C']
print(df)
count = df.count()

print('------------------')
print(type(count))
print(count['A'])
print('------------------')
