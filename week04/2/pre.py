import pandas as pd
import numpy as np

x = pd.Series([1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])
print(x.hasnans)
x2 = x.fillna(value=x.mean())
print(x)
print(x2)

df3 = pd.DataFrame({"A": [5, 3, None, 4],
                    "B": [None, 2, 4, 3],
                    "C": [4, 3, 8, 5],
                    "D": [5, 4, 2, None]})

df3.isnull().sum()  # 查看缺失值汇总
df3.ffill()  # 用上一行填充
df3.ffill(axis=1)  # 用前一列填充
print(df3)