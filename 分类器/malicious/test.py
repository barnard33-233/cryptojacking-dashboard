import pandas as pd

# 读取名为 'WebOS_binary.csv' 的文件并创建数据帧 'df1'
df1 = pd.read_csv('WebOS_binary.csv')

# 使用布尔 Series 进行行筛选
index_names = df1[((df1['HW_dst'] != '18:56:80:17:d0:ef') & (df1['Hw_src'] != '18:56:80:17:d0:ef'))].index
df1.drop(index_names, inplace=True)

# 输出满足条件的行数和筛选后的数据帧
print("Number of filtered rows: {}".format(len(index_names)))
print(df1)

# 输出有效数据值的数量
print("df1 -->> {}".format(len(df1.dropna())))
