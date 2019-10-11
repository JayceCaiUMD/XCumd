# 用顺序表list来实现
# 用链表也可以但是更复杂
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n - 1):
        # 控制排序次数n-1
        for i in range(n - 1 - j):  # 从第1个到第n-1个，下标从0到n-2
            # 操作数据的下标会更简单实现查找，比较，调换的操作
            # 控制从头对比到尾
            # 用j减少循环的次数
            count = 0
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:  # 如果已经有序了，直接退出整个循环,就可以少走外层循环
            return


"""时间复杂度:
最优：未发现可以交换的元素O(n)
最坏：O(n^2)
稳定性: 稳定"""
if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)


