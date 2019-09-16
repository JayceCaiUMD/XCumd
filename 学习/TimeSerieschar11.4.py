import pandas as pd
import numpy as np
from datetime import datetime

#       11.4  time zone 时区处理

# UTC 协调世界时
# 时区就是UTC的偏移量

import pytz

print(pytz.common_timezones[-5:])

# 默认情况下，pandas中的时间序列使单纯的时区 naive
ts = pd.Series(np.random.randn(10), index=pd.date_range('3/2/2019 12:00', periods=10))
print(ts.index.tz)  # 默认的时区是none

ts_utc = ts.tz_localize('UTC')  # 从naive转换成UTC时区
ts_ny = ts_utc.tz_convert('America/New_York')  # 从非naive转换成别的时区

# 将独立的Timestamp对象从naive本地化为时区意识型 time zone-aware
stamp = pd.Timestamp('2011-03-12 04:00')
stamp_utc = stamp.tz_localize('utc')  # 先本地化
stamp_ny = stamp_utc.tz_convert('Asia/Shanghai')

stamp_moscow = pd.Timestamp('2018-3-2 05:40', tz='Europe/Moscow')
print(stamp_moscow.value)  # Timestamp对象在内部保留了UTC时间戳值，是UNIX纪元算起的纳秒数

ts1 = ts[5:].tz_localize('Europe/London')
ts2 = ts1[:2].tz_convert('Asia/Shanghai')
print(ts1)
print(ts2)
