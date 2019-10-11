#           Shell sort
#           希尔排序
# 用gap进行分割子序列，分别插入排序，再减小gap

def Shell_Sort(alist):
    """希尔排序"""

    # 假设使用gap
    n = len(alist)
    gap = n // 2
    while gap > 0:  # 当gap为1时退出循环,因为1//2 = 0
        # 插入算法，引入了gap替代1的间隔
        for j in range(gap, n):  # 控制所有子序列的所有元素
            i = j
            while i > 0:  # 控制子序列中的多次插入排序
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
        # 缩短gap

"""时间复杂度:
最优：根据gap序列决定
最坏：O(n^2)
稳定性: 不稳定
"""

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Shell_Sort(li)
    print(li)

def shell(alist):
    n = len(alist)
    gap = n//2
    while gap > 0:
        for j in range(gap,n):
            i = j
            while i > 0: #此处如果是大于gap，则只是由于离gap最近的那个值，下一个gap的不适用
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap = gap//2