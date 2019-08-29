import pandas as pd

# 5.2 pandas 基本功能

# 因为index对象不可直接改变，所以需要用方法操作
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

print(obj.reindex(['a', 'b', 'c', 'd', 'e']))  # 重新排序 插入缺失值

obj2 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj2 = obj2.reindex(range(6), method='ffill')
print(obj2)
