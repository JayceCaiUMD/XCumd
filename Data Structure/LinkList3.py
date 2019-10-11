#               数据结构
#           线性表
#           单向循环链表
#           尾部接到头

class SingleNode(object):
    """结点"""

    def __init__(self, elem):
        # elem用于保存数据区域
        self.elem = elem
        # next代表指向区域，暂时还不知道
        self.next = None


class SingleLinkList(object):
    """单向循环链表"""

    # 把节点串联起来，并支持一些对链表的操作
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node  # 让尾部和头部链接

    def is_empty(self):
        # 链表是否为空 (直接返回)
        return self.__head == None

    def length(self):
        # 链表长度（需要实现遍历节点）
        # 需要一个游标cur（指针）用来移动遍历节点
        # cur的内容是当前的节点，所以具有node的属性
        if self.is_empty():
            return 0
        cur = self.__head
        # count 记录数量
        count = 1  # 需要改变计数方法
        # 开始游标的移动（一个循环的过程）
        while cur.next != self.__head:
            count += 1
            cur = cur.next  # 将cur移动
        return count

    def travel(self):
        # 遍历整个链表
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环时，尾结点还未打印
        print(cur.elem)

    def add(self, item):  # O(n)
        # 链表头部添加元素，头插法，传入的是数据，不是node，我们通过封装将其转化成node
        node = SingleNode(item)
        if self.is_empty():  # 如果是空的
            self.__head = node
            node.next = node
        else:
            # 对单向循环链表，需要一个遍历的过程找到尾结点链接
            cur = self.__head
            while cur.next != self.__head:  # 找到尾结点
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node
        # 特殊情况，空链表

    def append(self, item):  # O(n)
        # 链表尾部添加元素，尾插法 同理
        node = SingleNode(item)
        if self.is_empty():  # 空链表时指向None，none没有next属性，所以要先判断
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head  # 连接循环

    def insert(self, pos, item):  # O(n)
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
        # 对循环链表，不涉及到头尾所以没关系
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
        if self.is_empty():
            return
        # 如果只有一个结点，恰好是想要remove的，pre没有next

        # 需要想删除的前一个node，重新定位他的next
        cur = self.__head  # 移动pre，让cur保持一个node的距离
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if pre == None:  # 头节点,需要遍历找到尾部并链接到头部
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:  # 中间结点，则都可以处理
                    pre.next = cur.next
                return  # 找到后跳出函数
            else:
                pre = cur  # 先移动pre
                cur = cur.next  # 再移动cur

        # 尾部结点不在循环内处理，所以要单独处理
        if cur.elem == item:
            if cur == self.__head:  # 只有一个结点
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):  # O(n)
        # 查找节点是否存在,返回Boolean
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False
        # 循环链表会漏掉最后一个结点，需要单独判断
        # 特殊情况空链表，直接返回False


if __name__ == '__main__':
    sll = SingleLinkList()
    # 创建一个单链表对象，指向None
    print(sll.is_empty())
    print(sll.length())
    print('--LinkList--')
    sll.append(1)
    sll.travel()
    sll.add(8)
    sll.travel()
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
