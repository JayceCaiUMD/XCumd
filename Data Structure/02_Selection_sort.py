def selection_sort(alist):
    #选出最小的，放在第一位
    #在循环中记录最小数的下标，遍历完之后进行交换
    n = len(alist)
    for j in range(n-1): #j是需要换到的最小位置
        min_index = j
        for i in range(j+1,n): #i对无序的部分进行遍历
            if alist[min_index] > alist[i]:
                min_index = i
        alist[min_index], alist[j] = alist[j],alist[min_index]

"""时间复杂度:
最优/最坏：O(n^2)
稳定性: 不稳定（将最大的放最后的升序排法）/其他情况稳定
"""



if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(li)
    print(li)