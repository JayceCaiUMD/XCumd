import pandas as pd
import numpy as np

#       10.2数据聚合 Data Aggregation
# 聚合可以指对groupby对象进行计算的过程 .sum .count .std .mean etc.

df1 = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})

print(df1)

def peak_to_peak(arr):
    dff= arr.max() - arr.min()
    return dff
df1_dff=df1.groupby('key1').aggregate(peak_to_peak) #用aggregate或agg 传入自定义函数作为聚合方法
print(df1_dff,'=dff')                                      #但是自定义函数会比10.1优化过的函数慢很多


#   对多个列使用不同的聚合函数
tips = pd.read_csv('examples/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
grouped = tips.groupby(['day','smoker'])


#同列多个函数
grouped['tip_pct'].agg(['mean','std',peak_to_peak]) #用agg或aggregate 传入多个函数，包括系统自带的函数
multfun= grouped['tip_pct'].agg([('平均数','mean'),('标准差','std')]) #优化一下，用自定义的列名而不是函数名
print(multfun)

#多个列多个函数
functions = ['count', 'mean', 'max']   #注意：自带的函数都是要带''的
result = grouped['tip_pct', 'total_bill'].agg(functions) #多个列传入多个函数
print(result) #输出的是层次化column    等同于分别聚合再concat再指定keys

#多个列分别不同函数
result2= grouped.agg({'tip':[np.max,'mean'],'size':'sum'}) #使用字典的映射关系（列名到字典）
print(result2)

#使用as_index = False 拆分层次化索引， 作用类似reset_index
print(tips.groupby(['day', 'smoker'], as_index=False)['total_bill'].mean())