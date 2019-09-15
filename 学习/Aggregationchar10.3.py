import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

#       10.3 Apply
#     apply是对分组的整个对象 分别使用函数再进行组合，可以返回二维结果
#     agg则是每次只输入了一列进行运算聚合
tips = pd.read_csv('examples/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
grouped = tips.groupby(['day', 'smoker'])


def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]


print(tips.groupby('smoker').apply(top, n=3))  # 内层索引来自原DataFrame，直接在apply函数中传入目标函数的其他参数

result = tips.groupby('smoker', group_keys=False).apply(top, n=3)  # 放弃分组键组成的外层索引
print(result)

# 分位数quantile 和 桶bucket 分析
frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})
equal4 = pd.cut(frame.data1, 4)  # 将frame四等分装入bucket中
print(equal4[:3])  # 返回的是category对象


def get_states(group):
    return {'min': group.min(), 'max': group.max()}


group1 = frame.data2.groupby(equal4)  # 将category对象传递给groupby作为分组键
print(group1.apply(get_states))  # 再进行聚合运算

quartile4 = pd.qcut(frame.data1, 4, labels=False)  # 四分位数，每个bucket里数据量都相同
group2 = frame.groupby(quartile4)['data1']  # 用label=False 显示分位标记编号 取代分组名
print(group2.apply(get_states))

#   examples for .apply
# ex1: 利用分组 给每组的缺失值NA填充不同值
states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
data = pd.Series(np.random.randn(8), index=states)

group_key = ['East'] * 4 + ['West'] * 4  # 得到了一个串联起来的list，利用它进行分组

data[['Vermont', 'Nevada', 'Idaho']] = np.nan
fillwithmean = lambda x: x.fillna(x.mean())
fill_mean = data.groupby(group_key).apply(fillwithmean)
print(fill_mean)

data[['Vermont', 'Nevada', 'Idaho']] = np.nan
fillvalue = dict((['East', 0.5], ['West', -1]))
fillwithvalue = lambda x: x.fillna(fillvalue[x.name])  # 每组有一个name属性，用于对应替换的值
fill_value = data.groupby(group_key).apply(fillwithvalue)
print(fill_value)

# ex2: resample
# Hearts, Spades, Clubs, Diamonds
suits = ['H', 'S', 'C', 'D']  # 四种花色
card_val = (list(range(1, 11)) + [10] * 3) * 4  # 值的序列
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in suits:
    cards.extend((str(num) + suit) for num in base_names)

deck = pd.Series(card_val, index=cards)  # 包含了52张纸牌的Series 和对应的分数


def draw(deck, n=5):
    return deck.sample(n)  # 随机抽5张的函数


# 想要每种花色中随机抽取两张
get_suit = lambda x: x[-1]
sample = deck.groupby(get_suit).apply(draw, n=2)
print(sample)

# ex3: grouped weighted mean 分组加权平均数和相关系数
df = pd.DataFrame({'category': ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b'],
                   'data': np.random.randn(8),
                   'weights': np.random.rand(8)})

group3 = df.groupby('category')
get_wavg = lambda x:np.average(x['data'],weights=x['weights'])
wavg = group3.apply(get_wavg)
print(wavg) #a组b组分别的加权平均

#          计算 各股票日收益率与SPX的相关系数组成的DataFrame
close_px = pd.read_csv('examples/stock_px_2.csv',   #包含一些股票和标普500植数(SPX)
                       parse_dates=True,index_col=0)
print(close_px.info())

spx_corr = lambda x:x.corrwith(x['SPX']) #算列与列相关系数的函数
rets= close_px.pct_change()  #计算变化率

get_year = lambda x:x.year
corr_year = rets.groupby(get_year).apply(spx_corr) #按年分组并计算相关系数

print(corr_year)

#ex4: 组级别的线性回归
import statsmodels.api as sm #计量经济学库
def regress(data,yvar,xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.0
    result = sm.OLS(Y,X).fit()
    return result.params        #对各个数据块执行OLS回归

# reg_year = rets.groupby(get_year).apply(regress,'AAPL',['SPX'])

