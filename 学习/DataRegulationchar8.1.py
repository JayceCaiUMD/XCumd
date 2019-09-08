import pandas as pd
import numpy as np

#           8.1 层次化索引Hierarchical indexing

s1 = pd.Series(np.random.randn(9),
               index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(s1, '=s1')

print(s1['b':'d'])
print(s1.loc['b', 1])  # 对内层进行索引

data = s1.unstack()  # 以DataFrame方式呈现

f1 = pd.DataFrame(np.arange(12).reshape((4, 3)),  # DataFrame的每条轴都能有分层索引
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])

f1.index.names = ['key1', 'key2']
f1.columns.names = ['state', 'color']
print(f1)  # 注意区分

# 重排与分级排序
print(f1.swaplevel('key1', 'key2'))  # 交换层级 但是数据不会发生变化
print(f1.sort_index(level=0, axis=1))  # 给某一条轴的某一层级排序

print(f1.sum(axis=0, level=1), '=sum')  # 注意level=0也并不是将所有的value相加

f2 = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})

f2_setindx = f2.set_index(['c','d'],drop=False)  #用set_index 将某几列变成多层索引
print(f2_setindx)  #可以用drop=False 将原列保留下来

f2.reset_index()    #用法与set_index正相反

