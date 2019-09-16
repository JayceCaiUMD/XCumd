import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#       11.7 moving window function 移动窗口函数
close_px_all = pd.read_csv('examples/stock_px_2.csv',
                           parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()  # 重采样为工作日频率
print(close_px.head())

fig1, axe = plt.subplots(2, 1)
close_px.AAPL.plot(ax=axe[0])
close_px.AAPL.rolling(window=250).mean().plot(ax=axe[0])  # rolling 就是移动窗口，250行（即250天） 用mean聚合求出250天移动平均
# 观测值在窗口的最右边（最下边），所以前250个会出现缺值
# 用center=True改变观测值位置至中性
r1 = close_px.AAPL.rolling(window=250, min_periods=10).mean()  # min_periods 窗口内至少需要n个值来计算，可以减少开头的缺值
print(r1)
expending_mean = close_px.AAPL.expanding().mean().plot(ax=axe[1])  # 从头开始拓展窗口长度，而不是移动

# 用ewm运算符，  使用时间间隔span定义衰减因子decay factor，
# 使得近期的观察数据有更大的权重，使观察更准确
aapl_px = close_px.AAPL['2006':'2007']
fig2, axe2 = plt.subplots(1, 1)
ma30 = aapl_px.rolling(window=30, min_periods=10).mean().plot(ax=axe2, style='k--',
                                                              label='Simple MA', legend='best')
ewma30 = aapl_px.ewm(span=30).mean().plot(ax=axe2, style='k-', label='EW MA', legend='best')

fig3, axe3 = plt.subplots(2, 1)
spx_px = close_px_all['SPX']
spx_return = spx_px.pct_change()
returns = close_px.pct_change()
# 计算每支股票收益率的50日移动平均与标普500（spx）的相关系数
returns.rolling(250, min_periods=10).corr(spx_return).plot(ax=axe3[0])

# 用seaborn画出了apple与标普500（spx） 50日移动平均的散点回归图
trans_data = pd.merge(spx_return, returns['AAPL'],
                      left_index=True, right_index=True, how='inner')
print(trans_data)
sns.regplot(x='AAPL', y='SPX', data=trans_data, ax=axe3[1], marker='.',
            line_kws={'linewidth': 1, 'color': 'k'})
fig3.show()
