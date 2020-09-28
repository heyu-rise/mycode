import pandas as pd
import numpy as np
import matplotlib as plt
import os

pwd = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(pwd, 'book_utf8.csv')
df = pd.read_csv(path)
# print(df)

# print(df['还行'])

# print(df[1:3])

df.columns = ['star', 'vote', 'shorts']

# print(df.loc[1:3])
# print(df.loc[1:3, ['star']])

print(df['star'] == '力荐')
print(df[df['star'] == '力荐'])




