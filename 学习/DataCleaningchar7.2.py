import numpy as np
import pandas as pd

#   7.2 数据转换   （过滤，清理，转换）
df1 = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
print(df1, '=df1')
print(df1.duplicated())  # 返回bool型Series，标识各行是否是重复行(每列上的值都重复）

df1['v1'] = range(7)
print(df1.drop_duplicates(['k1'], keep='last'))  # 只根据某一列来过滤重复值；选择保留最后一个重复值

# 用函数或映射进行数据转换
df2 = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                             'Pastrami', 'corned beef', 'Bacon',
                             'pastrami', 'honey ham', 'nova lox'],
                    'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]}, index=range(1, 10))
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'}  # 想要添加的food到animal的映射

lowercased = df2['food'].str.lower()  # python讲究大小写，所以原df里大小写不一的food先进行转化
df2['animal'] = lowercased.map(meat_to_animal)  # 1.用Series的map方法，接受一个函数或 映射关系dict

# 2.用匿名函数lambda快速完成所有工作
df2['animal'] = df2['food'].map(lambda x: meat_to_animal[x.lower()])
print(df2, '=df2')  # map总是用于元素级转换,且对每个元素进行操作

# 用replace实现替换功能，可以只对某一元素进行操作
s1 = pd.Series([1., -999., 2., -999., -1000., 3.])
s1.replace(-999., np.nan)  # 替换某个数成为他值
s1.replace([-999., -1000], [np.nan, 0], inplace=True)  # 传入列表组或dict实现多对多替换
print(s1, '=s1')

# 重命名轴索引
df3 = pd.DataFrame(np.arange(12).reshape((3, 4)),
                   index=['Ohio', 'Colorado', 'New York'],
                   columns=['one', 'two', 'three', 'four'])

# 轴索引和值一样可以通过函数或映射进行转换
transform = lambda x: x.upper()
df3.columns = df3.columns.map(transform)
print(df3)

# 默认rename也是不会对原对象操作的，只是生成副本
df3.rename(index=str.title, columns=str.lower, inplace=True)
print(df3)

df3.rename(index={'OHIO': 'INDIANA'},  # 结合字典可以实现部分更新
           columns={'three': 'peekaboo'})

#       离散化和面元划分
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]  # 希望划分成这几个 面元（bin)
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
cut1 = pd.cut(ages, bins=bins, right=False, labels=group_names)  # 返回一个特殊的Categorical对象, right表示区间的开闭，labels表示bin的名称
print(cut1)  # 结果展示了pandas.cut划分的面元。你可以将其看做一组表示面元名称的字符串。
# 它的底层含有一个表示不同分类名称的类型数组，以及一个codes属性中的年龄数据的标签
print(pd.value_counts(cut1), '=counts')

data1 = np.random.rand(20)
cut2 = pd.cut(data1, 4, precision=2)  # 若不规定界限，则按数字计算n个等长bin,precision是小数位数
print(cut2)

cut3 = pd.qcut(data1, q=4)  # 用分位数的方法切割，所以每个bin中的数据多少是一样的
print(pd.value_counts(cut3))

# 处理异常值outlier
data2 = pd.DataFrame(np.random.randn(100, 4))
print(data2.describe())

coln = data2[2]
outl1 = coln[np.abs(coln) > 2.5]
print(outl1, '=outl1')  # 筛选第3列绝对值大于2.5的值

outl2 = data2[(np.abs(data2) > 2.5).any(axis=1)]  # any是指定轴上有一个为真即为真（与all不同） 返回的是boolean型 Series
print(outl2, '=outl2')  # 用 bool型Series进行索引时，size必须匹配

data2[(np.abs(data2) > 3).any(1)] = np.sign(data2) * 3  # 将超出（-3，3）范围的outlier根据sign判断正负变为-3或3
print(data2.describe())

#       排列和随机采样
df4 = pd.DataFrame(np.arange(20).reshape(5, 4))
sampler = np.random.permutation(5)  # 生成一个整数ndarray对象
print(df4.take(sampler, axis=0))  # 按sampler对象依此索引选取行
print(df4.sample(2, axis=1, replace=True))  # 随机取样2列(replace=True重复取样)

# 将分类变量（categorical varible) 变为哑变量或叫指标矩阵    可用于构造虚拟变量矩阵
df5 = pd.DataFrame({'age': ['old', 'young', 'middle', 'middle', 'old', 'young'],
                    'data1': range(6)})
agedummies = pd.get_dummies(df5['age'], prefix='ages')  # 根据某列的分类形成虚拟变量矩阵,prefix是便于区分的前缀
print(agedummies)

# 结合get_dummies和离散化函数cut
values = np.random.rand(10)
cut4 = pd.get_dummies(pd.cut(values, 5, precision=2), prefix='group')  # 分位数分类的矩阵
print(cut4)
