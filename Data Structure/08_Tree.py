# Tree
#树的实现

class Node(object):
    """结点"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        # 广度遍历用队列的思想实现
        # 每从左端拿出一个结点，对其左右进行分析并放进待分析的队列右端
        # 直至出现空位
        queue = []
        queue.append(self.root)
        while queue: #列表中有None元素也算True会执行，在运行.lchild时会出错
            #当列表为空，每个列表元素（结点）都被判断完成时退出
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        queue = [self.root]
        if self.root is None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder_travel(self,node):
        """先序遍历，（根先，根 左 右）"""
        #每次把子树当作新树遍历，用到递归
        #而为了确定子树，使用根
        #将根结点传入函数
        if node is None:
            #处理到叶子结点时应该退出
            return
        print(node.elem,end=' ')
        self.preorder_travel(node.lchild)
        self.preorder_travel(node.rchild)

    def inorder_travel(self,node):
        """中序遍历，（根中，左 根 右）"""
        #每次把子树当作新树遍历，用到递归
        #而为了确定子树，使用根
        #将根结点传入函数
        if node is None:
            #处理到叶子结点时应该退出
            return
        self.inorder_travel(node.lchild)
        print(node.elem,end=' ')
        self.inorder_travel(node.rchild)

    def postorder_travel(self,node):
        """后序遍历，（根先，左 右 根）"""
        #每次把子树当作新树遍历，用到递归
        #而为了确定子树，使用根
        #将根结点传入函数
        if node is None:
            #处理到叶子结点时应该退出
            return
        self.postorder_travel(node.lchild)
        self.postorder_travel(node.rchild)
        print(node.elem,end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.breadth_travel()
    print(' ')
    tree.preorder_travel(tree.root)
    print(' ')
    tree.inorder_travel(tree.root)
    print(' ')
    tree.postorder_travel(tree.root)