import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-10, 10)
# print(points)

xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

# np.where
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
print([xarr, yarr, cond])

result = [x if c else z for x, c, z in zip(xarr, cond, yarr)]
# zip()各个参数中的元素相互组成tuple再整合成一个list，即[(1.1，2.1，True)，
print(result)

# 用where方法使得三元条件表达式 x if y else z 变得简单 np.where(y,x,z)
print(np.where(cond, xarr, yarr))
# 还可以快速对数组中的数进行条件筛选
ran1 = np.arange(-4, 5).reshape(3, 3)
ran1_pos = np.where(ran1 > 0, 1, ran1)  # 大于0的变成1，小于等于0的不变
print(ran1_pos)

# np中数学统计函数可以对整个数组或单个轴向进行计算，可以做方法method也可做numpy顶级函数
print(ran1, '=ran1')
print(np.sum(ran1, 0), '=sumran1')  # axis代表轴（可以不加关键词索引，）与维度不同，行是1，列是0
print(ran1.mean(axis=1))

print(ran1.cumsum(0))  # cumsum，计算第n维度上加和的 中间值
print(np.cumprod(ran1, 0), '=cumprod')  # cumprod, 计算第n维度上  乘积 的 中间值

ran2 = np.arange(-4, 4).reshape(2, 2, 2)
print(ran2, '=ran2')
print(np.sum(ran2), '=sumran2')
print(ran2.cumsum(0))

# 与python内置函数一样，用sort方法给数组进行排序
# 用sort方法的话会直接修改数组，用np.sort的顶级函数则不会
sort1 = np.arange(9, 0, -1).reshape(3, 3)
print(sort1)

sort1.sort()
print(sort1)

# 利用排序找分位数
ranarr = np.random.randn(30)

quantile1to10_ranarr = (np.sort(ranarr))[int(len(ranarr) * 0.1)]  # 用[]查找特定位置的数
print(quantile1to10_ranarr)

# np.unique寻找数组中的唯一值并返回已排序的结果
# 相当于先取集合，后排序
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
unnames = np.unique(names)
print(unnames)
# 还有一些集合运算
names2 = np.array(['Ruby', 'Mike', 'Tom', 'Joe'])
print(np.union1d(names2, np.unique(names)))  # 并集
print(np.in1d(names2, names))  # x的元素是否在y中， 返回bool值

#               有关线性代数的运算
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])

xy = np.dot(x, y)  # 与 x.dot(y)相同，矩阵乘法，在numpy中可以用@
print(x @ y)
trace = np.trace(x)  # 算对角线的和
diag1 = np.diag(x)

# 伪随机数的生成-通过random模块
sample1 = np.random.normal(loc=2, scale=2, size=(3, 3))  # 正态分布的随机数样本,默认为标准正态分布即loc=0，scale=1
sample2 = np.random.binomial(n=10, p=0.2, size=10)  # 二项分布
sample3 = np.random.chisquare(df=10, size=10)  # 卡方分布
sample4 = np.random.uniform(1, 10, size=3)  # 生成[x,y)中均匀分布的样本值
sample5 = np.random.rand(5)  # 生成()个均匀分布的样本值
sample6 = np.random.randint(1, 50, size=5)  # 生成范围内随机整数

# 随机漫步的生成
position = 0
walk = [position]
steps = 20
for i in range(steps):
    draws = np.random.randint(0, 2)
    step = np.where(draws > 0, 1, -1)
    position += step
    walk.append(position)
print(walk)
plt.plot(walk)
plt.show()
