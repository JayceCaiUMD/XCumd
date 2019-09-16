import pandas as pd
import numpy as np
from datetime import datetime

#           11.6 resampling   重采样
#         指将时间序列从一个频率转化到另一个频率
#       高到低是降采样downsampling，低到高是升采样upsampling

rng = pd.date_range('2019-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)

# resample可以实现类似groupby功能，先分类，再聚合
# 使用resample之后返回的对象要经过 聚合 才能显示

res1 = ts.resample(rule='M').mean()
print(res1)

# downsampling
rng2 = pd.date_range('2000-01-01', periods=12, freq='T')  # freq是mintues
ts2 = pd.Series(np.arange(12), index=rng2)
print(ts2.head())
res2 = ts2.resample('5min', closed='right').count()  # 按所属的时间段进行分类，左开右闭区间，进行计数
print(res2)  # 显示的时间是开始的时间戳

# 在金融行业中用到的OHLC重采样 计算open，high，low，close
res3 = ts2.resample('5min', closed='left').ohlc()
print(res3)

# upsampling
# 升采样则不需要聚合了
frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2000', periods=2,
                                         freq='W-WED'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(frame)
print(frame.resample('D').asfreq())  # 不进行操作，只转换格式
print(frame.asfreq('W-THU'))

#通过period进行重采样
frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range('2000-1-1', '2001-12-1',
                                           freq='M'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
annual_frame = frame.resample('y').mean()
print(annual_frame)
print(annual_frame.resample('Q-DEC',convention='end').ffill())

"""asfreq 与 resample 的区别 
resample适用性更广，能实现聚合操作
索引可以分为时间戳索引Timestamp
          和时间段组PeriodIndex 两种
对PeriodIndex: asfreq 不会丢失数据，不会多出na值
              resample  升采样出现na(如果数据不够)，降采样产生重复值，需要聚合   
对TimeStamp:   asfreq  升频率出现na值 降频率要规定start或end
              resample 升采样出现na值 降采样也需要规定
"""
# frame = pd.DataFrame(np.random.randn(24, 4),
#                      index=pd.date_range('2000-1', periods=24,
#                                            freq='M'),
#                      columns=['Colorado', 'Texas', 'New York', 'Ohio'])
# annual_frame = frame.resample('d').asfreq()
# print(annual_frame)