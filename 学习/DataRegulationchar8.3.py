import pandas as pd
import numpy as np

#       8.3重塑(reshape)和轴向旋转(pivot)

df1 = pd.DataFrame(np.arange(6).reshape((2, 3)),
                   index=pd.Index(['Ohio', 'Colorado'], name='state'),
                   columns=pd.Index(['one', 'two', 'three'],
                                    name='number'))
result = df1.stack()  # 将DataFrame的列变为分层索引
print(result, '=result')
print(result.unstack())  # .unstack则是反效果，默认是最里层，传入level参数改变层级

df2 = pd.DataFrame({'left': result, 'right': result + 5},
                   columns=pd.Index(['left', 'right'], name='side'))
print(df2, '=df2')
print(df2.unstack('number'))  # 作为旋转轴的级别会成为结果中的最低级别


#       将长格式（long）旋转为宽格式(stacked): pivot
data = pd.read_csv('examples/macrodata.csv')

periods = pd.PeriodIndex(year=data.year, quarter=data.quarter,
                         name='date')  # 将多列分散的日期时间组合成 TimeSeries并作为index
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D')
print(data.head())  # 宽格式， 每行代表一次观察，item下的种类都堆叠起来
ldata = data.stack().reset_index().rename(columns={0: 'value'})   #stack将DataFrame变成层次化Series
print(ldata.head())  # 长格式， 一次观察被分为多个种类的堆叠

pivoted = ldata.pivot('date', 'item', 'value')  # 用pivot快速转换长格式为宽格式  .pivot(行索引，列索引，数据)
print(pivoted.head())

ldata['value2'] = np.random.randn(len(ldata))  # 假设有两个数据列
pivoted1 = ldata.pivot('date', 'item')  # 需要指定 数据集参数， 否则两个都代入会得到层次化的列
print(pivoted1['value'].head())  # 可以指定外层列查看（某个数据集）


#      将宽格式(stacked)旋转为长格式(long): melt
data2 = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
print(data2.head())
melted = data2.melt('key')   #.melt() 需要指定的是 用作分类依据的列，比如商品类型，剩下的是数据
print(melted)     #即变成了长格式
reshaped = melted.pivot('key','variable','value')
print(reshaped.reset_index())

print(data.head(3))
zz= data.reset_index().melt('date').sort_values(by='date').reset_index(drop=True)
print(zz.head()) #其实到melt这步即可 完成了长格式的转换