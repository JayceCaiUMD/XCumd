all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
# list in list，大的list（all_data）包括两个小的list（names）小的list包含的都是元素（name）
result = []
for names in all_data:
    for name in names:
        if name.count("a") >= 1:
            result.extend([name.upper()])
print(result)

# 嵌套推导式写法
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
result = [name.upper() for names in all_data for name in names if name.count("a") >= 1]
print(result)

#计算素数
prime100 = [a for a in range(2, 20) if 0 not in [a % test for test in range(2, a)]]
print(prime100)

prime20 = []
for a in range(2, 20):
    for test in range(2, a):
        if a % test == 0:
            break
    else: #for...else 结构：如果for循环正常结束，else中语句执行。如果是break的，则不执行
        prime20.append(a)
print(prime20)

