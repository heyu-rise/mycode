import pandas as pd

df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
print(df1)

df2 = pd.DataFrame([
                     ['a', 'b'],
                     ['c', 'd']
                    ])
print(df2)

# 自定义列索引
df2.columns = ['one', 'two']
# 自定义行索引
df2.index = ['first', 'second']

# print(df2)
#
# print(df2.columns)
# print(df2.index)
#
# print(df2['first'])
print(df2.iloc[:, [0, 1]]) # :表示所有行，获得第1和第2列

print(df2.loc['first'])

print(df2.loc[['first', 'second']])
