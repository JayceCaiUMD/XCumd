import pandas as pd
import numpy as np

"""时间序列数据的意义meaning of time series data
timestamp 时间戳，特定的时刻
period 固定时期，一段时间
interval 时间间隔， 用起始和结束时间戳表示
"""
from datetime import datetime

#       11.1 date and time
now = datetime.now()
print(now)  # 年，月，日，时，分，秒.毫秒
print(now.year, now.month)  # datetime对象储存了具体的时间

delta = datetime(2012, 2, 15) - datetime(2006, 1, 2, 15, 30)
print(delta)  # timedelta 表示两个datetime之间的时间差 日，秒，毫秒

# string和datetime的转换
stamp = datetime(2011, 1, 3)
print(str(stamp))
print(stamp.strftime('%Y,%m,%d'))  # 以要求格式转换为字符串   %Y 4位数的年， %y 2位数的年

value = '2019-01-22'
date1 = datetime.strptime(value, '%Y-%m-%d')
print(date1)

from dateutil.parser import parse

date2 = parse('12/24/2001', dayfirst=False)  # 智能地将常见的格式装换成datetime
print(date2)
