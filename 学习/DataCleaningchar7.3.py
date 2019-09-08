import numpy as np
import pandas as pd

#           7.3 字符串操作(对字符串使用的方法)

val = 'a  ,b,    c,b'
pieces = [x.strip() for x in val.split(',')]  # 将每个字符串切分开并去除前后空格
print(pieces)

d1 = '::'.join(pieces)  # 用::将目标list或tuple中的对象串起来,返回字符串
print(d1, 'join')

print(val.index('b'), 'index')  # 返回某子串在字符串中的位置，若无则报错ValueError
print(val.find('b'), 'find')  # 返回发现的第一个字串的位置（最后一个用rfind），若无则返回-1
print(val.count('a'), 'count')  # 返回字符串出现次数
print(val.replace(' ', ''), 'replace')  # 字串的替换，也可用于删除

# 正则表达式 regex
import re

text = "foo    bar\t baz  \tqux"  # \t是一个tab

print(re.split('\s+', text), '\s+')  # \s+ 代表一个或多个空白符

regex = re.compile('\s+')
regex.split(text)  # 先用compile 将目标字符串编译一个可重用的regex对象,再使用

text1 = """Dave: dave@google.com
Steve: steve@gmail.com
Rob: rob@gmail.com
Ryan: ryan@yahoo.com
"""

pattern = r'[A-Z0-9._]+@[A-Z0-9.-]+\.[A-Z]{2,4}'  # A pattern compiled with regex
regex1 = re.compile(pattern, flags=re.IGNORECASE)  # re.IGNORECASE  Ignore the case
print(regex1.findall(text1),'=findall')  # findall Return all matchs
print(regex1.search(text1))  # search 返回第一个匹配项 (以特殊的匹配项对象形式返回)
print(regex1.match(text1))  # match 从字符串首开始匹配，不同就失败 (以特殊的匹配项对象形式返回)

print(regex1.sub('Email', text1))  # 用'Email' 替换匹配到的pattern

pattern2 = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'  # 加上括号后匹配项对象可以用.group 通过元组方式输出
regex2 = re.compile(pattern2, flags=re.IGNORECASE)
result = regex2.search('xiuyuan.cai@umd.edu.com')
print(result.groups())  # 用括号（）隔开的各段用tuple输出

# pandas的矢量化字符串函数
text3 = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
         'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = pd.Series(text3)

pattern3 = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

result1 = data.str.findall(pattern3, flags=re.IGNORECASE)  # 用str将对象矢量化并跳过na值进行字符串操作
print(result1)
