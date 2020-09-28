import pandas as pd
import numpy as np
import re

# 从列表创建Series
series = pd.Series(['a', 'b', 'c'])
print(series)

# 通过字典创建带索引的Series
s1 = pd.Series({'a': 11, 'b': 22, 'c': 33})
# 通过关键字创建带索引的Series
s2 = pd.Series([11, 22, 33], index=['a', 'b', 'c'])
print(s1)
print(s2)

s3 = s1.values.tolist()
print(s3)

emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
pattern = '[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
print(mask)
print(emails[mask])