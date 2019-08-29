'''函数也是对象，可以是迭代器中的元素，可以是其他函数中的参数'''

states = ['  Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south   carolina##', 'West virginia?']
#使用re模块清理数据

import re
def clean_str(strings):
    result=[]
    for value in strings:
        value=value.strip() #去除字符串首位的字符，默认为空格，可以加字符串参数
        value=re.sub('[#!?%&]','', value) #re.sub(替换掉的旧内容用[]表示可以加逗号，新内容，对象）
        value = value.title() #首字母大写
        result.append(value) #每个清洗的结果添加到list result中，注意写到循环中去
    return result  #写到循环外面，函数的最后
print('方法1',clean_str(states))



states = ['  Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south   carolina##', 'West virginia?']
#对字符串做的所有处理做成列表,然后调用这个函数列表进行数据处理

def remove_punction(value):
    value=re.sub('[#!?%&]','',value)
    return value

clean_ops =[str.strip,remove_punction,str.title] #将一系列函数做成了列表

def clean_str2(strings,ops):
    result=[]
    for value in strings:
        for function in ops:
            value=function(value)
        result.append(value)
    return result
print('方法2',clean_str2(states,clean_ops))

print(tuple(map(remove_punction,states)))
#map用于将一个函数对指定序列做映射
#map()的返回值是iterators迭代器，所以需要加函数转换为list或dict或tuple
