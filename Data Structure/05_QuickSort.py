#       快速排序

# 左右游标同时向中心移动，夹出元素的正确位置，
# 再对左右分别进行重复操作

def Quicksort(alist, start, end):
    """快速排序"""
    if start >= end: #子集范围缩小到只有一个元素时停止
        return
    mid_value = alist[start]  # 从序列第一个值开始排
    low = start  # low作为左游标，从第一个值开始移动
    high = end  # high作为右游标，从最后一个值开始移动

    while low < high:
        # 让high和low交替移动
        while low < high and alist[high] >= mid_value:  # 游标重合时，停止移动, 否则high移动至小于目标值
            high -= 1
        alist[low] = alist[high]  # 将high游标的值给low,轮到low移动了
        # 当某刻low与high重合时，赋值语句虽然执行但是没意义

        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]  # 退出循环时，将low游标的值给high，又轮到high移动了

    alist[low] = mid_value
    # high = low

    # 分割列表,都用索引表示
    Quicksort(alist, start, low - 1)  # 前半段
    Quicksort(alist, low + 1, end)  # 后半段
    # 引入参数，在每次快排结束时，将前后无序的列表段用索引表示，就可以实现递归
    # 如果用赋值或切片，则原列表不会被改变，而是生成了新列表


def quick_sort(alist,first,last):
    """fisrt 为0，last为最后一个数的索引即len(alist)-1"""
    if first >= last:
        return
    low = first
    high = last
    mid_value = alist[low]
    while low < high:
        while low < high and mid_value <= alist[high]:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value
    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)

"""时间复杂度:
最优：相当于每次分成2份，直到每份都只有1一个元素，即n份
    2*2*2*2*...*2 = n 该复杂度为次数
    每次拆分时的复杂度为n，所以：
    O(nlogn)
最坏：O(n^2)
稳定性: 不稳定
"""
if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Quicksort(li, 0, len(li) - 1)
    print(li)



    l1 = [1,6,2,8,4,2,7,3]
    quick_sort(l1,0,len(l1)-1)
    print(l1)