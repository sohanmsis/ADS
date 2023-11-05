class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=" ")

    def levelorder_traversal(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            print(queue[0].data, end=" ")
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
