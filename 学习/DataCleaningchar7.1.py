import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re

# 7.1 缺失数据处理 dealing with NaN

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
#NaN表示确实数据，称为哨兵值

string_data[0]=None #使用None和np.nan都可以
print(string_data.isnull())

s1 = pd.Series([1, None, 3.5, None, 7])
print(s1.dropna()) #去掉空数据返回非空数据和索引的Series

from numpy import nan as NA
df1 = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])

print(df1,'=df1')
print(df1.dropna(axis=1)) #对DataFrame会丢弃任何含有缺失值的行，还可改变为列axis=1
print(df1.dropna(how='all')) #只丢弃全部是na的行

df2 = pd.DataFrame(np.random.randn(7, 3))
df2.iloc[4:, 1] = NA
df2.iloc[2:, 2] = NA

print(df2.dropna(thresh=2)) #保留含有两个及以上非NA数据的行，thresh=n
#用fillna方法将值赋给NA,也可传入字典使替换项传给特定列
print(df2.fillna({1:'f1',2:'f2'},inplace=False)) #用inplace使操作映射到原对象 True/False
print(df2.fillna(method='ffill',limit=2)) #与reindex的method类似，默认使用ffill的全部向下填充方式

