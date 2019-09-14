import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#  9.2 tips visualization
#用pandas绘图
tips = pd.read_csv('examples/tips.csv')
fig, axes = plt.subplots(2, 2)
fig.subplots_adjust(wspace=0, hspace=0)
party_counts = pd.crosstab(tips['day'], tips['size'])  # crosstable 用于统计频率
party_counts = party_counts.iloc[:, 1:5]  # 选出size 2到5的
print(party_counts)
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
print(party_pcts)
party_pcts.plot.bar(ax=axes[0, 0], stacked=True)  # 生成堆叠柱状图


#tips支出百分比图 (用seaborn绘图 )
tips['tip_percent'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
sns.barplot(ax=axes[1, 0], x='tip_percent', y='day', hue='time', data=tips)  # hue是分类
sns.set(style='whitegrid')  # 可是设置图形背景和网格线颜色等

#直方图和密度图
tips['tip_percent'].plot.hist(ax=axes[0,1],bins=40) #直方图，频率统计
tips['tip_percent'].plot.density(ax=axes[1,1]) # 可能会产生目标值的概率分布

#如果还有更多（三个以上）的分类维度，x，y，hue之外，还能用catplot的col,row创建分面网格图
sns.catplot(x='day',y='tip_percent',
            col='smoker',row='time',   #row和col指整个网格图的row和col
            kind='bar',data=tips)
plt.show()
