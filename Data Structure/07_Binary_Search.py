#       二分查找
#       折半查找
# 只能作用于     有序顺序表

def Binary_Search(alist, item):
    """二分查找,递归"""
    # 将新的子列表切片进行递归
    n = len(alist)
    if n > 0:
        mid = n // 2  # 偶数时中间值为右端
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return Binary_Search(alist[:mid], item)
        else:
            return Binary_Search(alist[mid + 1:], item)
    else:
        return False  # 第一个if全执行完了还没找到，则没有这个目标


def Binary_Search_2(alist, item):
    """二分查找，非递归"""
    # 一直使用索引在原列表上定位，比较，查找
    # 使用 （首索引+尾索引）//2的方式查找中间值，偶数时中间值为左端
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:  # 当等于时只剩下一个元素，还未进行判断
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else: #item > alist[mid]
            first = mid + 1
    return False

"""时间复杂度:
最优：O(1)
最坏：O(logn)  2*2*2*2*2 = n
"""

if __name__ == '__main__':
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(Binary_Search(li, 17))
    print(Binary_Search(li, 100))
    print(Binary_Search_2(li, 31))
    print(Binary_Search_2(li, 100))
