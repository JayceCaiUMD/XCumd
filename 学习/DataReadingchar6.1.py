import pandas as pd
import numpy as np

#       6.1 读写文本格式数据

df1 = pd.read_csv('c:/python/examples/ex1.csv')
print(df1)

df2_1 = pd.read_csv('examples/ex2.csv', header=None)  # 可以不加列名让系统从0开始分配,header=加数字表示表头行数
df2_2 = pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])  # 也可自定义names
print(df2_2)

df2_3 = pd.read_csv('examples/ex2.csv', names=list(('a', 'b', 'c', 'd', 'message')), index_col='message')
print(df2_3)  # 将某列作为索引 若不想自动识别第一列为index则加 index_col=False

# 对多层索引，在设index_col时传入标签列表即可
parsed = pd.read_csv('examples/csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)

df3 = pd.read_csv('examples/ex3.txt', sep='\s+')  # 有些文件不用常规分隔符，这里定义空格为分隔符，正则表达式\s+
print(df3)

df4 = pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])  # 即跳过1，3，4行不读取
print(df4)

df5_1 = pd.read_csv('examples/ex5.csv')  # read_csv 可以识别NULL与NA与空值 为缺失值NaN
print(df5_1, '=df5.1')
df5_2 = pd.read_csv('examples/ex5.csv', na_values=['world'])  # 自定参数让pandas识别为缺失值
print(df5_2)  # world字符被识别为NaN

pd.options.display.max_rows = 8  # 最多显示行数8

df6_1 = pd.read_csv('examples/ex6.csv')
print(df6_1)
df6_2 = pd.read_csv('examples/ex6.csv', nrows=4)  # 只读取若干行
print(df6_2, '=df6.2')

# 可以设置缺失值的表现形式（默认是空字符串）,还可设置是否显示index与header
df5_1.to_csv('examples/out1.csv', na_rep='NULL', index=False, header=False)
# 还可重新自定列，并且不一定要标记全部
df5_1.to_csv('examples/out2.csv', index=False, columns=['a', 'b', 'c'])

import csv

df7_1 = open('examples/ex7.csv')
reader = csv.reader(df7_1)  # 将任何已打开的文件传递给csv.reader
for line in reader:
    print(line)  # 发现对reader对象迭代是每列形成了一个tuple

# 处理一个畸形行文件
with open('examples/ex7.csv') as df7_2:  # withas见withas_test
    lines = list(csv.reader(df7_2))  # 生成多个列表(行)组成的列表

header, values = lines[0], lines[1:]  # 规定lines中第一个列表为header其余为values
print(values)
x, y, z = zip(*values)
data_dict = {h: v for h, v in zip(header, zip(*values))}  # 转置行为列，value与header用zip打包生成dict
print(data_dict)
f1 = pd.DataFrame(data_dict, index=['one', 'two'])
print(f1)


from bs4 import BeautifulSoup
#读取html文件
tables = pd.read_html('examples/fdic_failed_bank_list.html')
# read_html 会搜索<table>标签内的表格数据，生成DataFrame，与一个描述表格的list

failures = tables[0]  # 选取了DataFrame并储存
print(failures.head())

#读取excel文件
xlsx = pd.ExcelFile('examples/ex1.xlsx') #创建ExcelFile类的实例
xl1 = pd.read_excel(xlsx, 'Sheet1') #导入数据到实例
print(xl1)

xl2= pd.read_excel('examples/ex1.xlsx') #直接将文件名传递到read_excel

#写入excel
writer = pd.ExcelWriter('examples/ex2.xlsx') #创建ExcelWriter的实例
df2_2.to_excel(writer,'Sheet01') #将已有的pandas对象写入到实例writer并设定Sheet名字
writer.save()

df2_1.to_excel('example/ex2_1.xlsx') #对象直接传递到文件

