import numpy as np

# 生成了一个随机数组成的数组，又叫numpy数组，也叫ndarray对象
# numpy创建的数组中的元素类型全都是一样的，用dtype方法查看类型，用astype方法改变类型、
data = np.random.randn(2, 4)
print(data, data.dtype, data.shape)

dataint = data.astype(np.int64)  # astype改变数据类型后并不会返回到原numpy中，所以要储存到其他numpy中
print(dataint, dataint.dtype, dataint.shape)

# 用array函数创建一个ndarray对象，接受 序列型 的对象,嵌套的序列会变成多维数组
data1 = [(1, 2, 4, 5, 3, 6), (1, 5, 61, 43, 4, 1)]
arr1 = np.array(data1)
print(arr1)

# 一些快速生成numpy的方法
arr2 = np.identity(5)  # 单位矩阵
print(arr2)
arr3 = np.arange(3)  # range()类似
print(arr3)

# 字符串的组合也可以存储在numpy中，如果是纯数字的话可以转换成数组
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings)
numeric_floats = numeric_strings.astype('f')  # dtype可以用np.float64也可以用 '类型代码'（需要加引号）
print(numeric_floats)

# numpy可以直接进行数组计算
print(arr1, arr1.sum())

# numpy的索引与切片,操作方法上与列表相似
arr4 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(arr4, end='   ')
# 索引: [(a,)b,c]  (a+1层,）n+1行,m+1列
print('索引[2,0]=', arr4[2, 0])
# fancy indexing: 用全是整数的numpy或list按顺序多次索引并复制
print(arr4[[2, 0, 1]])  # 按照312行的顺序进行索引
# 切片：[(n:m),n:m,n:m]   （n+1层：m+1层,）n+1行：m行，n+1列：m列 注意包头不包尾
arr4_slice = arr4[:2, 1]  # 到第2行，第2列
print('slice=', arr4_slice)
# 切片或索引出来的numpy如果内容被改变，会被boardcast到原numpy中，fancy indexing除外
arr4_slice[:] = 1  # 将切片[:2,1]全部赋值1
print(arr4, '(boardcasted)')

# bool索引，numpy对象在运算后返回一个新的bool型numpy
# 用bool型numpy进行索引时，True的会被抛出来
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
datafornames = np.random.randn(7, 2)  # 随机生成7行5列正态分布的数
print(datafornames)
print(datafornames[names == 'Bob'])

# 数组转置（矩阵转置）.transpose()/.T
arr5 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(arr5.transpose(1, 0))  # 括号里是维度的顺序,二维下0是行，1是列
print(np.dot(arr5.T, arr5))  # np.dot()矩阵相乘

#     对numpy中元素的通用函数ufunc，只有shape相同时才可以使用
# 对每个元素的单独计算
arr6 = np.arange(1, 10).reshape(3, 3)
# 一元ufunc
print(np.sqrt(arr6))
print(arr6 ** 2)
arr7 = np.arange(-1, -10, step=-1).reshape(3, 3)
# 二元ufunc
print(np.multiply(arr6, arr7))  # 对应函数相乘
print(np.maximum(arr7, arr6))  # 相比取最大

# True在numpy中会被强制转换为1（true）和0（false）
# 灵活运用sum可以对bool型数组中的true 计数
compare67 = np.greater_equal(arr6, arr7)
print(compare67)
print(np.sum(compare67))

print((arr6 ** 0.5 > 1).sum())

# any检查是否存在一个以上true，  all是否全是true
# 也可用与非bool型数组，所有非0元素都被当成True
print(compare67.any())
print(np.all(compare67))
