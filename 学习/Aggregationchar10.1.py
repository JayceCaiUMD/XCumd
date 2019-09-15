import pandas as pd
import numpy as np

#             Data Aggregati 数据聚合与分组运算
#           10.1 GroupBy 机制
#          分组运算：split-apply-combine
#           分组方式有很多

df1 = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})
print(df1, '=df1')

grouped = df1['data1'].groupby(by=[df1['key1'], df1['key2']])  # 访问Series对象data1，并根据key1,2调用groupby
mean1 = grouped.mean()  # grouped是GroupBy对象，只有中间数据，调用mean方法计算mean
print(mean1, '=mean1')  # 输出了一个Series，name是data1，index是分组依据'key1''key2'的唯一值

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
mean2 = df1.groupby(by=[states, years])  # 分组键: 1.任何长度适当的 数组（ndarray对象)
# 可以不添加到DataFrame中，直接用作分组键
size1 = df1.groupby(['key1']).size()    # 2.列名     size用来统计频率
print(size1, '=size1')  # 结果中非数值的数据列会被排除

#           对GroupBy对象进行迭代,产生多个二元tuple：(分组1,数据块1),(分组2，数据块2)
for keys, data in df1.groupby(['key1', 'key2']):
    print(keys)  # 对多重键：二元tuple的第一个元素分组名也是tuple
    print(data)

print('------make a dict---------')  # 将GroupBy分组后做成dict
pieces = dict(list(df1.groupby('key1')))
print(pieces['a'])

for dtype, data in df1.groupby(by=df1.dtypes, axis=1):  # axis=1,对列进行分组, 以类型分组
    print(dtype)
    print(data)

mean3 = df1.groupby(['key1', 'key2'])['data1'].mean()  # 对某列数据进行分组操作的 简单写法
print(mean3,'=mean3')  # 如果索引传入单个列，则返回Series；传入多个索引(列表)，则返回DataFrame

# 利用字典或者Series 进行分组
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2, 1:3] = np.nan
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}  # 分组键: 3. 包含映射关系的dict

by_dict = people.groupby([mapping], axis=1).mean()
print(by_dict)
map_series = pd.Series(mapping)  # 4. Series (利用index与value的索引关系)
by_series = people.groupby(map_series, axis=1).count()
print(by_series)

# 通过函数进行分组
by_func = people.groupby(len)  # 5. 直接传入函数
len_counts = by_func.count()  # 以index的长度进行分组
print(len_counts)

key_list = ['one', 'one', 'one', 'two', 'two']
by_mix = people.groupby([len, key_list]).min()
