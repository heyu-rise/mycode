import pandas as pd

# 行列调整
df = pd.DataFrame({"A": [5, 3, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]})

# 列的选择,多个列要用列表
# print(df[['A', 'C']])

# 某几列
# print(df.iloc[:, [0, 2]]) # :表示所有行，获得第1和第3列
#
print(df.loc[0:2])

print(df.loc[[0, 2]])

df['C'] = df['C'].replace(4, 40)
print(df)

import numpy as np

df.replace(np.NaN, 0)

# 多对一替换
df.replace([4, 5, 8], 1000)

# 多对多替换
df.replace({4: 400, 5: 500, 8: 800})

# 排序
# 按照指定列降序排列
df2 = df.sort_values(by=['A'], ascending=False)

print(df2)
# 多列排序
df2 = df.sort_values(by=['A', 'C'], ascending=[True, False])

print(df2)

# 删除列
df2 = df.drop('A', axis=1)
print(df2)
# 删除行
df2 = df.drop(3, axis=0)
print(df2)

# 删除特定行
df2 = df[df['A'] < 4]
print(df2)

print(df.T)

print(df.stack())

print(df.stack().reset_index())