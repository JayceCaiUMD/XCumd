# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time
import timeit
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a+b+c ==1000 and a**2+b**2 == c**2:
#                 print('a,b,c',a,b,c)
# end_time = time.time()
# print(end_time-start_time)
# print('finished')

T = 1000 * 1000 * 1000 * 2
# T = N * N * N * 2
# T(n) = n^3 * 2
# T(n) = k*g(n) + c  -> T 是 g 的渐近函数，大体可以表示
# O(g(n)) 即为T(n) 即为大O时间复杂度

"""算法的特性，
1. 输入：具有0或多个输出
2. 输出：有1或多个输出
3. 有穷性：在有限的步骤后会结束，在可接受的时间范围内
4. 确定性：每个步骤有确定的意义
5，可行性：计算机可以执行
"""
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            print('a,b,c', a, b, c)
end_time = time.time()
print(end_time - start_time)
print('finished')
#T(n) = n * n * (1+max(1,0)) = O(n^2)

#           效率的衡量：时间复杂度与大O表示法
# 每台机器执行的总时间不同
# 但是执行的基本运算数量大体相同
# 时间复杂度 T：运行的效率，快慢 （经过了多少基本运算）
# 我们衡量的是最坏的可能情况

# 1.基本操作，只有常数项，O(n)
# 2.顺序结构，加法计算
# 3.循环结构，乘法计算
# 4.分支结构，取最大值
# 5.只关注最高次项
# 6.一般都关注最坏时间复杂度

# O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)

# 对list来讲，对尾部的操作速度快于头部
