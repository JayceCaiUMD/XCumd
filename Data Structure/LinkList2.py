#               数据结构
#           线性表
#           双向链表
#           前驱结点和后继结点
#           有两个链接域prev与next，链接到前驱结点与后继结点


class SingleNode(object):
    """结点"""

    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        # 与单链表相同
        cur = self.__head
        # count 记录数量
        count = 0
        # 开始游标的移动（一个循环的过程）
        while cur != None:
            count += 1
            cur = cur.next  # 将cur移动
        return count

    def travel(self):
        # 遍历整个链表
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print(" ")

    def add(self, item):
        node = SingleNode(item)
        # 新node的next指向下一个node，下一个node的prev指向新node
        if self.__head:
            node.next = self.__head
            self.__head = node
            node.next.prev = node
        else:
            self.__head = node

    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur  # 将新node的prev链接到最后一个node

    def insert(self, pos, item):
        # 指定位置添加元素
        # :param pos 从0开始
        node = SingleNode(item)
        if pos <= 0:  # 如果pos<=0，则认为在头部插入
            self.add(item)
        elif pos > (self.length() - 1):  # 如果pos>最后一个节点的下标即length-1，则认为在尾部插入
            self.append(item)

        else:
            # 不需要pre游标
            # cur代表pos下标的node
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
                # 循环退出时cur指向pos位置
            node.next = cur
            node.prev = cur.prev
            # 改变插入位置前后node的相互指向
            cur.prev.next = node
            cur.prev = node
            # 或 cur.prev = node
            #   node.prev.next = node

    def search(self, item):
        # 查找节点是否存在,返回Boolean
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False  # 如果到none都没有触发True，则返回False
        # 特殊情况空链表，直接返回False

    def remove(self, item):
        cur = self.__head
        # 需要改变item所在node的前后node的prev与next指向
        while cur != None:
            if cur.elem == item:
                # 判断是否是头节点
                if cur.prev == None:
                    self.__head = cur.next
                    # 此时如果只有一个结点，即既是头又是尾，cur.next是none
                    if cur.next:  # 如果cur.next存在
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 判断是否是尾结点，不是尾结点才会运行
                    if cur.next:
                        cur.next.prev = cur.prev
                break  # 找到之后退出循环
            else:
                cur = cur.next


if __name__ == "__main__":
    sll = DoubleLinkList()
    # 创建一个单链表对象，指向None
    print(sll.is_empty())
    print(sll.length())
    print('--LinkList--')
    sll.append(1)
    sll.add(8)
    # 8,1
    sll.append(2)
    sll.append(3)
    sll.append(4)
    # 8,1,2,3,4
    sll.insert(3, 't')
    sll.insert(6, 'e')  # 6>length-1
    sll.insert(-1, 0)
    sll.travel()
    sll.search(111)
    sll.remove('t')
    sll.travel()
