import pandas as pd
import numpy as np

#           8.2合并数据集 dataset merging
# merge方法会丢弃两个对象中的index
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})

print(df1)
print(df2)
dfm1 = pd.merge(df1, df2, on='key')  # 多对一的合并,重叠列的 交集 会被当做'key'
print(dfm1,'=dfm1')

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
dfm2 = pd.merge(df3, df4, left_on='lkey', right_on='rkey',how='inner')  # 如果列名不同的话可以分别进行指定，合并的列默认是交集
print(dfm2, '=dfm2')
dfm3 = pd.merge(df3, df4, left_on='lkey', right_on='rkey', how='outer')  # how='outer'则是 并集
print(dfm3,'=dfm3')

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})

right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
dfm4 = pd.merge(left, right, on='key1', how='outer', suffixes=('_l', '_r'))  # 多对多的merge会产生所有的组合
print(dfm4)  # 用suffixes给重名的列做标记

# 层次化索引的合并

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                               'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})

righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                              'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
dfm5 = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')  # 指明用作合并键的多个列
print(dfm5.sort_values(by=['key1', 'key2']),'dfm5')

#       轴向连接
arr = np.arange(12).reshape((3, 4))
print(np.concatenate([arr, arr], axis=1))

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'a'])

data1 = pd.concat([s1, s2, s3])  # 默认在axis=0上工作,沿着行轴将数据堆起来
data2 = pd.concat([s1, s2, s3], axis=1, sort=True)  # axis=1则会生成DataFrame
print(data2)

result = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'])  # 用key创建一个层次化索引，就可以将concat的对象区分开
print(result)

data3 = pd.concat({'level1': df1, 'level2': df2}, axis=1,join='outer')  # DataFrame的index会进行合并（默认并集）
print(data3,'=data3')  #同样也可不用dict，用keys区分开来

df5 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df6 = pd.DataFrame(np.random.rand(2, 3)*100, columns=['b', 'd', 'a'])
data4 = pd.concat([df5, df6], ignore_index=True,join='inner')  # 合并后的DataFrame的index无意义，则放弃连接轴上的index
print(data4)
# 与merge方法不同，concat使得数据在某一条轴上堆叠，用 join规定 另一条轴 数据合并方式，默认是outer
# 对merge来说，选某一列作为key，key的合并方式由 how决定，默认是inner


#  合并重叠数据
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b','a'])
b[-1] = np.nan
print(a.combine_first(b)) #a,b 应该同等长度
#其意义是合并ab，a中有则选择a，a是空则选择b
print(np.where(a.isnull(),b,a)) #与用where实现的功能类似
