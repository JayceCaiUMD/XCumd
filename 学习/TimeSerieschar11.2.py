import pandas as pd
import numpy as np
from datetime import datetime

#       11.2 Time Series basic
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)
print(ts.index)  # index中的datetime对象是放在DatetimeIndex 对象中的
stamp = ts.index[0]
print(stamp)  # DatetimeIndex中的各个标量值是pandas的Timestamp对象

print(ts[stamp])  # 将Timestamp作为索引

long_ts = pd.Series(np.random.randn(1000),
                    index=pd.date_range('1/1/2010', periods=1000))  # 设置1000天的数据

print(long_ts['2011-2-11':'2011-2-14'])  # 直接传入年，月等数据，会被自动解释  (修改该切片会被broadcast

print(long_ts.truncate(after='2010-2-1', before='2010-1-28'))  # 注意before和after

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
                          '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)  # 带有重复索引的timeseries

c_ts = dup_ts.groupby(level=0).mean()
print(c_ts) #以某种方法聚合重复数据


