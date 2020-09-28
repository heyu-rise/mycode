import pandas as pd
import numpy as np

# 聚合
sales = [{'account': 'Jones LLC', 'type': 'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co', 'type': 'b', 'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc', 'type': 'a', 'Jan': 50, 'Feb': 90, 'Mar': 95}]

df2 = pd.DataFrame(sales)
print(df2)
groups = df2.groupby('type')

for a, b in groups:
    print(a)
    print(b)

group = df2.groupby('type').aggregate({'type': 'count', 'Feb': 'sum'})
print(group)

group = ['x', 'y', 'z']
data = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "salary": np.random.randint(5, 50, 10),
    "age": np.random.randint(15, 50, 10)
})

print(data)
mean = data.groupby('group').aggregate('mean')
print(mean)
mean = data.groupby('group').mean()
print(mean)
mean = data.groupby('group').transform('mean')
print(mean)