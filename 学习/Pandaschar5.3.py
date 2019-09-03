import pandas as pd
import numpy as np

#       5.3 汇总和计算描述性统计
f1 = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(f1, '=f1')
print(f1.sum())  # 列求和（axis=0）
print(f1.sum(axis=1, skipna=False))  # 行求和 （axis=1，NA默认被自动过滤）
print(f1.cumprod(axis=1))  # 单行中每列累计求和

print(f1.idxmin())  # 每列中达到最小/最大值的index
print(f1.describe())  # 描述性统计（数值型的和非数值型的结果不同）
# 其他方法包括 count（非NA值数量）,mean,meadian,mad,var,std,skew,kurt,diff(一阶差分）


s1 = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
print(s1.unique())  #得到唯一值数组（类似集合）
print(s1.value_counts()) #计算各值出现频率

mask=s1.isin(set('bc'))#判断是否在迭代器中,返回bool值
print(s1[mask]) #用返回的bool Series 筛选True的值
#还有match 方法

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                      'Qu2': [2, 3, 1, 2, 3],
                      'Qu3': [1, 5, 2, 4, 4]})

result= data.apply(pd.value_counts).fillna(0)
print(result) #apply默认axis=0，将函数应用到每一列上，然后将NA填充为0
#得出的结果是每一列上每个index的计数
