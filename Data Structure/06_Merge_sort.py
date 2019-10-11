#       归并排序
#   不断二等分，直至子集只有一个元素
#   两两大小排序
#   2v2 设立左右游标依次对比，对比后移动游标
#   4v4 同样设立游标

def Merge_sort(alist):
    """归并算法"""
    n = len(alist)
    # 拆分过程
    mid = n // 2  # 最中间的值的 下标
    if n <= 1:  # 大于1就一直执行
        return alist  # 左半边一直执行到只有一个元素并返回单元素列表，再右边
    else:
        # 采用归并排序后形成的新的 有序 列表
        left_li = Merge_sort(alist[:mid])  # 递归左侧全部数 左闭右开
        right_li = Merge_sort(alist[mid:])  # 递归右边全部数
        # 将有序子序列合并成新整体

        l_pointer, r_pointer = 0, 0
        result = []  # 新列表用来存放新值
        while l_pointer < len(left_li) and r_pointer < len(right_li):
            # 当游标值==子列表长度时，退出循环
            if left_li[l_pointer] < right_li[r_pointer]:
                result.append(left_li[l_pointer])
                l_pointer += 1
            else:
                result.append(right_li[r_pointer])
                r_pointer += 1
        result += left_li[l_pointer:]  # 当某一边执行完时，将剩余的值（应该是有序的）全部加到result中
        result += right_li[r_pointer:]
        return result

"""时间复杂度:
拆分（二分）O(1)
两两合并O(n)
两两合并执行了2*2*2...*2 =n    即logn次
最优：O(nlogn)
最坏：O(nlogn)
稳定性: 稳定
但是产生了一个新的列表占据了空间，所以空间复杂度比其他排序更大
"""
if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sortedlist = Merge_sort(li)
    print(sortedlist)
