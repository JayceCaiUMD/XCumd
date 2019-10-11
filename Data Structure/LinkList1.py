#               数据结构
#           线性表
#           顺序表和链表

# node ：
class SingleNode(object):
    """结点"""

    def __init__(self, elem):
        # elem用于保存数据区域
        self.elem = elem
        # next代表指向区域，暂时还不知道
        self.next = None


class SingleLinkList(object):
    """单向链表"""

    # 把节点串联起来，并支持一些对链表的操作
    def __init__(self, node=None):
        self.__head = node
        # 创建链表时加入的节点为头部节点，也可以创建空链表
        # 需要有一个属性指向列表的头部节点，就能实现别的操作
        # 构造链表时生成的私有属性_

    def is_empty(self):
        # 链表是否为空 (直接返回)
        return self.__head == None

    def length(self):
        # 链表长度（需要实现遍历节点）
        # 需要一个游标cur（指针）用来移动遍历节点
        # cur的内容是当前的节点，所以具有node的属性
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

    def add(self, item):  #O(1)
        # 链表头部添加元素，头插法，传入的是数据，不是node，我们通过封装将其转化成node
        node = SingleNode(item)
        # 直接给_head赋值会丢掉后面的节点
        # 所以先将新节点的next链接好，再链接到head
        node.next = self.__head
        self.__head = node
        # 考虑特殊情况空链表，发现没问题

    def append(self, item): #O(n)
        # 链表尾部添加元素，尾插法 同理
        node = SingleNode(item)
        if self.is_empty():  # 空链表时指向None，none没有next属性，所以要先判断
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):    #O(n)
        # 指定位置添加元素
        # :param pos 从0开始
        node = SingleNode(item)
        if pos <= 0:  # 如果pos<=0，则认为在头部插入
            self.add(item)
        elif pos > (self.length() - 1):  # 如果pos>最后一个节点的下标即length-1，则认为在尾部插入
            self.append(item)

        # 实现：将插入位置的后一个node链接到插入node.next
        #      插入位置的前一个node需要改变它的next，链接到node
        # 所以定义一个pre游标, 代表插入的前一个node
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):  # pos-1即为前一个node的位置，count=pos-1时就应该退出循环
                count += 1
                pre = pre.next
                # 循环退出后，pre指向pos-1的node
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        # 删除节点
        # 需要一个游标指向想删除的node
        # 需要想删除的前一个node，重新定位他的next
        cur = self.__head  # 移动pre，让cur保持一个node的距离
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断是否是头节点
                if pre == None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break #找到后跳出循环，否则一直满足条件，一直在重新定位
            else:
                pre = cur  # 先移动pre
                cur = cur.next  # 再移动cur
    #       特殊情况空链表，成立
    #       删除的是第一个node，让head等于cur.next
    #       删除的是最后一个node，指向了none，成立

    def search(self, item):     #O(n)
        # 查找节点是否存在,返回Boolean
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False  # 如果到none都没有触发True，则返回False
        # 特殊情况空链表，直接返回False


if __name__ == '__main__':
    node1 = SingleNode(100)

    sll = SingleLinkList()
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