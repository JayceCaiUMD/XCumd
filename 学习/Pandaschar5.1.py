import pandas as pd
import numpy as np

#   5.1 pandas 数据结构
#   Series   有规定顺序的序列  注意大写
obj = pd.Series([4, 6, 5, -1])  # 生成带index索引的序列，索引从0开始
print(obj.values, obj.index)  # 查看值与索引
obj2 = pd.Series([2, 1, 6, 9], index=['a', 'b', 'c', 'd'])  # 也可自定索引
obj2[['a', 'b']] = 7  # ['a','b']是索引列表 赋值时可以不加[] 而选取一组值时需要加
print(obj2[['a', 'b']])

# 字典dict可以直接转换为Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

# 字典导入序列时也可重新排序key作为index，设定原先不存在的key会生成空值
obj4 = pd.Series(sdata, index=['Texas', 'Utah', 'Ohio', 'Huston'])
print(obj4)

# 检测是否有缺失数据并返回bool值Series
pd.isnull(obj4)
obj4.notnull()
a = (obj > 3)  # 直接进行对比也可返回bool值Series
print(a)

# Series对象与其index都有name属性，可进行赋值
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4, '=obj4')

#               构建DataFrame的各种方法
# 导入 等长 列表或Numpy数组组成的字典，构建DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# 创建一个DateFrame，可以设置index，给已有key排序作为columns
frame = pd.DataFrame(data, index=range(1, 7), columns=['state', 'pop', 'year', 'debt', 'abc'])
print(frame.head(3))  # 用.head方法选取前n行，默认是5
print(frame.year, frame['pop'])  # 获取某一列

frame.debt = range(2, 8)  # 给某一列赋值,必须长度匹配
val1 = pd.Series([-1.2, 1.6, 5], index=[1, 3, 5])
frame['abc'] = val1  # 用Series给列赋值会将index进行匹配留下空值
frame['eastern'] = frame.state == 'Ohio'  # 给不存在的列赋值则创建一个新列（不能用frame.eastern方法实现）
print(frame, '=f1')
del frame['abc']

# 将嵌套字典传给DataFrame，外层字典key作为columns，内层字典key作为index,内层字典value为value
# 数值的索引会被自动合并，排序
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame2 = pd.DataFrame(pop)
print(frame2, '=f2')

# 将二维ndarray传给DataFrame,矩阵直接变成其中的值
arr1 = np.arange(2, 6).reshape(2, 2)
frame3 = pd.DataFrame(arr1, index=['r1', 'r2'], columns=['c1', 'c2'])
print(frame3, '=f3')

# Series构成的list
s1 = pd.Series([1, 3, 5], index=['a', 'b', 'c'], name='s.1')
s2 = pd.Series([3, 1, 6], index=['a', 'b', 'd'], name='s.2')
frame4 = pd.DataFrame([s1, s2])  # 方向是横的,name作为index
frame5 = pd.DataFrame({'r1': s1, 'r2': s2})  # series组成的dict，key作为columns（与嵌套字典类似）
print(frame4, '=f4')
print(frame5, '=f5')
# Summary: 可输入给DataFrame的数据类型
# 二维ndarray
# turple,list,ndarray对象组成的dict
# Series组成的dict
# Series构成的list或dict
# dict或Series组成的dict

print(frame.values)  # 以二维ndarry的形式返回values

print(frame.columns, frame.index)  # DataFrame与Series的轴标签和元数据等自动构成index对象，不可改变
print('state' in frame.columns)  # 可执行类似set中的指令但是可以存在重复元素

print(frame.columns.is_unique)
# index 对象有一些方法包括 append difference(差集) intersection(交集) union (并集)
