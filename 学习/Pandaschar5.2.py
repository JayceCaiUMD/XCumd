import pandas as pd
import numpy as np

# 5.2 pandas 基本功能

# 对轴，轴标签进行操作时axis=0指行，1指列
# 注意涉及到对values的操作时，axis=0则指每行上的数，看起来像是对整列进行了操作

# 因为index对象不可直接改变，所以需要用方法操作
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

obj1 = obj.reindex(['a', 'b', 'c', 'd', 'e'])  # 重新按序列排列index 插入缺失值
print(obj1, '=obj1')

print(obj1.drop(['b', 'c']), 'obj1_dropped')  # drop方法返回删除特定值之后的新Series or DataFrame
obj1.drop('a', inplace=True)  # 使用inplace=True使得drop操作直接传递给原对象
print(obj1, 'obj1_dropped2')

obj2 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj2 = obj2.reindex(range(6), method='ffill')
print(obj2, '=obj3')

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print(frame, '=frame')
frame2 = frame.reindex(index=['a', 'b', 'c', 'd'], columns=['Texas', 'Huston'])
frame3 = frame.reindex(['Texas', 'DC', 'Maryland'], axis=1)  # 与ndarray一样，0是行维度，1是列维度
print(frame2, '=frame2')
print(frame3, '=frame3')

obj3 = pd.Series(np.arange(-1, 4), index=['one', 'two', 'three', 'four', 'five'])
print(obj3, '=obj3')
print(obj3['two':'four'])  # 直接用标签索引，两头都包含，顺序不正确则返回空Series
print(obj3[2:4])  # 与ndarray对象类似，[]索引包含头不含尾
# 使用整数索引obj3[1]时容易产生歧义，因为无法分辨[1]是指 对应行 还是 行的标签名字1
# 所以尽量使用loc[]与iloc[]

data1 = pd.DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
print(data1['one'])  # 用列标签对DataFrame进行索引

data2 = data1 < 5  # 直接用标量运算得到bool型DataFrame
print(data2)

# 使用 loc[] 轴标签索引 和 iloc[]整数索引 (中括号)
print(data1.loc[['Ohio', 'Utah'], 'two':'four'])
print(data1.iloc[:2, [1, 2]])  # 含头含尾

#           算数运算和自动对齐
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)  # 标签会进行对齐，输出的Series的index是一个union，同样的标签进行运算，不同的标签插入NaN
# DataFrame 类似，行标签和列标签都会对齐

# 还能使用fill_value对Na值进行填充，再进行算数函数的运算
print(s1.add(s2, fill_value=0))

# DataFrame与Series之间的运算会将Series的index匹配到DataFrame的columns，然后每行进行broadcast
# 与其他运算一样，未重叠的部分就会变成Na
frame4 = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                      columns=list('bde'),
                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
s5 = pd.Series(range(4), index=list('bdef'))
print(frame4.add(s5))  # f列s5有值，frame4没有值 未重叠区域变成NaN

s6 = frame4.iloc[:, 2]  # 若对列进行运算，匹配DataFrame的行，则使用算术运算方法，传入轴号
print(frame4.sub(s6, axis=0))  # 0代表frame4的行索引，也可是axis='index'

# Numpy的ufuncs 元素级数组方法可以操作Pandas对象中的每一个元素
print(np.sqrt(frame4))

# 用DataFrame的apply 方法可以将函数运动到 各个行或各个列组成的数组上
f = lambda y: y.max() - y.min()
print(frame4.apply(f, axis=0), '=ff4')  # 默认将f函数运用到每列
# 注意：输入轴号改变行列 index or 0 是对列操作, columns or 1 是对行操作

frame5 = pd.DataFrame(np.arange(8, 0, step=-1).reshape((2, 4)),
                      index=['three', 'one'],
                      columns=['d', 'a', 'b', 'c'])
frame5 = frame5.sort_index(axis=1, ascending=False)
# 用sort_index对Series 或DataFrame的某一索引进行排序,可选升降序（不直接映射到原对象）
print(frame5, '=f5')

# 依据值的排序可以使用sort_values
print(frame5.sort_values(by=['b', 'd']))  # DataFrame中对values排序的依据可能是多个列, 使用by参数

obj3 = pd.Series([7, -5, 7, 4, 2, 0, 4])
frame6 = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
# pandas中的rank方法默认分配平均排名即method='average' （第一个7为第6位，第二个7为第7位，平均都为6.5位）
print(obj3.rank())
print(frame6.rank(axis=1))  # 指定按轴对DataFrame进行排序 axis=1即每列中的数 横向排序

# 有各种打破平级关系的method
print(frame6.rank(axis=0, method='first'))  # method='first'不会出现平均值,按出现先后
print(obj3.rank(method='max'))  # 按最大/最小排名 如一个7为第6，一个为第7 则7/6
print(obj3.rank(method='dense'))  # 总是间隔为1， 同样的元素同组同序

frame7 = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'c'])
print('UniqueIndex7=', frame7.columns.is_unique)
# 若index或columns有重复的标签，索引结果则会改变
# Series中索引重复标签生成Series而不是标量值
# DataFrame中索引重复标签生成DataFrame而不是Series
print(frame7.loc['a'])
