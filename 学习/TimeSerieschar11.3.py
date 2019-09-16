import pandas as pd
import numpy as np
from datetime import datetime

#       11.3 range frequency movement of date
"""
pandas中的原生时间序列一般为不规则的，无固定频率
当需要以固定频率进行分析时，用一些工具进行重采样，频率推断等"""

index = pd.date_range('2018-1-1', '2018-1-3')
print(index)  # 默认频率是每天 'D'

bmidx = pd.date_range(start='2018-1-1', periods=6, freq='BM')
print(bmidx, '=BM')  # period是数量，freq可以又各种形式，BM是 business end of month ,每月的最后一天
wom1 = pd.date_range(start='2019-1-1', periods=6, freq='WOM-2SUN')  # WOM,week of month,每月第2个周日
print(wom1, '=WOM')
pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True)  # 用normalize来将时间规范到midnight，去掉时分秒

from pandas.tseries.offsets import Hour, Minute, Day,MonthEnd

# freq对应的是 日期偏移量date offset 对象， 也就是两次之间的时间间隔
one_halfday = Day(1) + Hour(12)  # 自定义一个dateoffset对象
print(pd.date_range('2019-1-1', freq=one_halfday, periods=4), '=one and half day')
# 将dateoffset对象直接作用于datetime或Timestamp对象上
print(datetime(2019, 3, 31) + one_halfday, '=offset to datetime')

# 数据或时间戳的平移
ts = pd.Series(np.random.randn(4),
               index=pd.date_range('1/1/2018', periods=4, freq='M'))
print(ts.shift(2))  # 沿时间轴将数据平移，保持索引不变,会产生缺失数据
print(ts.shift(-2, freq='M'))  # 传入freq使时间戳平移，就不会丢失数据

ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))

#对锚点偏移量， 即将时间偏移到某个点而不是经过一段时间
#可以使用其rollback，rollfoward 方法
rfoward = MonthEnd()
print(rfoward.rollforward(datetime.now())) #偏移至当前月底

