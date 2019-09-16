import pandas as pd
import numpy as np
from datetime import datetime

#           11.5 period
#           时期及其算数运算
#  时期period表示的是时间区间，数日，数月，数年等

p = pd.Period(2018, freq='A-DEC')  # 可以用整数或者字符串   A-DCE指Dec.的最后一天
print(p)  # 这里的Period对象是2018一整年

pm = pd.period_range('2018-1-1', '2018-03-01', freq='M')
print(pm)  # Period类保存了一组的Period，可以在pandas中用作轴索引
print(pd.Series(np.random.randn(3), index=pm))  # 这里的索引是一组period，与Timestamp不同

p1 = p.asfreq('M', how='start')  # 转换成别的频率 从年这一period的start开始
print(p1)  # 将一年时间转换成了开始的一个月 即一月

rng = pd.period_range('2006', '2009', freq='A-DEC')  # 以12月的最后一天结束的一年
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(ts.asfreq('M', how='start'))  # 低频率转换为高频率

# quarters

fp = pd.Period('2012Q4', freq='Q-JAN')  # 以1月底为结束月的财年的季度
print(fp.asfreq('D', how='end'))  # 1月结束的财年，2012Q4是 2011.11-2012.1

fp4pm = (fp.asfreq('B', 'end') - 1).asfreq('T', 's') + 16 * 60  # 将该季度转化成工作日末尾的第二天
print(fp4pm)  # 再转成分，加上16*60分钟，即是16点的时间戳

# 将Timestamp转换为period
print('----------------')
rng1 = pd.date_range('2018-1-1', periods=3, freq='M')
ts2 = pd.Series(np.random.randn(3), index=rng1)
print(ts2)

pts = ts2.to_period(freq='Q')  # period是非重叠的时间段，对给定的时间戳只能属于一个时期
print(pts)  # 也可指定freq，可同时出现重复period

# 通过数组创建PeriodIndex
data = pd.read_csv('examples/macrodata.csv')

index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='q')
print(index)  # 一般会自动识别，也可加入freq如果有特殊要求
data.index = index
data.drop(['year','quarter'],axis=1,inplace=True)
print(data.head())
