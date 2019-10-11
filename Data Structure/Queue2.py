#双端队列

#相当于两个栈底部拼到一起

class Dequeue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        #头部添加一个元素
        self.__list.insert(0,item)

    def add_rear(self,item):
        #从尾端添加元素
        self.__list.append(item)

    def pop_front(self):
        #从尾端删除元素
        self.__list.pop()

    def pop_rear(self):
        self.__list.pop(0)

    def is_empty(self):
        return not self.__list

    def size(self):
        return len(self.__list)
