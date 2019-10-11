# 插入算法

def Insertion_Sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        # j = [1,2,3,..,n-1]，总共需要排n-1个数
        # i 是内层循环的起始下标
        i = j  # 默认第一个为有序，从下标1的第二个元素开始插入
        while i > 0:  # ！！需要一直比较直到移到第一个
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1  # 下标往前移
            else:
                break  # 只要发现正序了就会退出，
                # 因为再前移都是已经排好序的，就不用将while循环执行完


"""时间复杂度:
最优/最坏：O(n)(完全正序时)/O(n^2)
稳定性: 稳定
"""

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Insertion_Sort(li)
    print(li)
