#            队列
#     可以用顺序表和链表实现
#   从一端添加，从另一端取出
#           FIFO

class Queue(object):
    def __init__(self):
        """队列"""
        #用顺序表list保存queue的数据
        self.__list = []

    def enqueue(self,item):
        #添加一个元素
        self.__list.append(item)

    def dequeue(self):
        #从另一端删除一个元素
        self.__list.pop(0)

    def is_empty(self):
        return not self.__list

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue('aaa')
    s.enqueue('2')
    s.enqueue(3)
    print(s.dequeue())
    print(s.dequeue())


