#       栈/堆栈
#   保存线性数据的容器
#       LIFO
# 描述的是数据读取的方式
# 只能一端进一端出


#栈的顺序表实现

class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []
        #使用了list作为顺序表

    def push(self,item):
        #压栈/入栈
        #以列表的尾端作为栈顶
        self.__list.append(item) #O(1)
        #若是以头部作为栈顶，使用list的insert方法，为O(n)

    def pop(self):
        #弹出栈顶元素
        return self.__list.pop()

    def peek(self):
        #返回栈顶元素
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []
        # return not self.__list
    def size(self):
        return  len(self.__list)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push('aaa')
    s.push('2')
    s.push(3)
    print(s.pop())
    print(s.pop())




