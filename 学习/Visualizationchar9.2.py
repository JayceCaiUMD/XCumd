import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#           9.2用pandas和seaborn绘图
# 用到plt.show()将图显示出来
s1 = pd.Series(np.random.randn(10).cumsum(), index=np.arange(100, step=10))
s1.plot(alpha=0.6, grid=True,  # 用pandas对Serie生成线型图
        rot=30, use_index=True)  # 用rot旋转标签，alpha是透明度，grid是网格

df1 = pd.DataFrame(np.random.randn(10, 4).cumsum(axis=0),
                   columns=['A', 'B', 'C', 'D'],
                   index=np.arange(100, step=10))
df1.plot(subplots=False,  # 将每条线分到subplot中
         title='line plot',  # DataFrame.plot会在subplot中为 每列 画一条线并自动创建图例
         sort_columns=True)  # 按字母表顺序绘制，默认为DataFrame列的顺序

fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.randint(1, 4, 8), index=list('ABCDEFGH'))
data.plot.bar(ax=axes[0], color='b', alpha=0.6)
data.value_counts().plot.barh(ax=axes[1], color='orange', alpha=0.5)  # values_counts和柱状图结合统计频率

df2 = pd.DataFrame(np.random.rand(3, 4),
                   index=['one', 'two', 'three'],
                   columns=pd.Index(['A', 'B', 'C', 'D'], name='Catalogs'))
print(df2)
df2.plot.bar()  # 每行为一组，包含所有列的值，不同行并排显示, 列名是图例的标题

fig2, axes2 = plt.subplots(1, 1)
comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
values = pd.Series(np.concatenate([comp1, comp2]))
sns.distplot(values, ax=axes2, bins=150, color='k')  # 同时画出直方图和连续密度估计

fig3, axes3 = plt.subplots(1, 1)
macro = pd.read_csv('examples/macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]  # data是DataFrame对象
trans_data = np.log(data).diff(1).dropna()  # 用numpy对每个值取对数，一阶差分，去掉有缺失值的行
sns.regplot(x='m1', y='unemp', data=trans_data, ax=axes3)  # 散点加线性回归图
axes3.set_title('Changes in log m1 versus log unemp')
