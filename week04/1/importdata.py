import pandas as pd

# pip install xlrd
# 导入excel文件
excel1 = pd.read_excel('1.xlsx')
print(excel1)
# 指定导入哪个Sheet
# pd.read_excel(r'1.xlsx', sheet_name=0)
#
# # 支持其他常见类型
# pd.read_csv(r'c:\file.csv', sep=' ', nrows=10, encoding='utf-8')
#
# pd.read_table(r'file.txt', sep=' ')
print(excel1.head(1))