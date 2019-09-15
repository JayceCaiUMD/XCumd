import pandas as pd
import numpy as np
import re

#           10.4 pivot & cross-tabulation

#   pivot table
tips = pd.read_csv('examples/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

pv1 = tips.pivot_table(index=['day', 'smoker'])  # 用.pivot_table 实现类似groupby的效果
print(pv1)

print('-------------------')

pv2 = tips.pivot_table(['tip_pct', 'size'],  # 想要聚合的数据
                       index=['time', 'day'], columns='smoker',  # 行索引和列索引
                       margins=True, margins_name='Count', aggfunc='count',  # 给每块数据添加一个小计，默认平均数
                       fill_value=0.)  # 可自定列名，套用的函数， fill_value替换缺失值
print(pv2)

#   crosstab
#  用于计算分组频率的特殊透视表

data1 = """0       1         USA  Right-handed
1       2       Japan   Left-handed
2       3         USA  Right-handed
3       4       Japan  Right-handed
4       5       Japan   Left-handed
5       6       Japan  Right-handed
6       7         USA  Right-handed
7       8         USA   Left-handed
8       9       Japan  Right-handed
9      10         USA  Right-handed"""


# data regulation
def dfdata(data):
    pattern = r'[0-9]\s+[a-z]+\s+[a-z-?.a-z]+'
    cleanstr = re.compile(pattern, flags=re.IGNORECASE)
    fresult = cleanstr.findall(data)
    dataset = []
    for string in fresult:
        cleaned = re.split(r'\s+', string)
        dataset.append(cleaned)
    print(dataset)
    return pd.DataFrame(dataset, columns=['Sample', 'Nationality', 'Handedness'])


df1 = dfdata(data1)
print(df1)
# crosstab 专门用于频数统计
ct1 = pd.crosstab(df1['Nationality'], df1['Handedness'], margins=True, margins_name='Total')
print(ct1)
