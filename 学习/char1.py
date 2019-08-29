i = 10
j = 1


# 异常的调试

class Myerror(Exception):
    # """self-defined error"""
    # 创建一个exception错误大类下的自定义错误Myerror小类
    pass


try:
    print((i + j))
except NameError as reason:
    i = j = 0
    print(reason)
    print('调试后结果为' + str(i + j))
except TypeError as reason:
    print(reason)
    print('调试后结果为' + str(i) + j)
else:  # 如果都没有错会运行else
    print('myerror raised')
    # (op)raise Myerror
finally:
    print('end')

import maintest as mt

mt.mtest1()
print(mt.__name__)  # 在调用其他模块时，被调用模块的__name__属性为模块名

# 打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end=' ')  # 每执行一次print都会换行，即默认\n结尾，把\n用end参数调成空格
        # 使其不换行还有空格
    print('')  # 一整行print完成之后需要换行，就随便print一个空字符，就可以换行
