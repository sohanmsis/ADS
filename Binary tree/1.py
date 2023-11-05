class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)
            else:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)
        return root

    def print_tree(self, root, traversal_type):
        if traversal_type == "preorder":
            self.preorder_print(root, "")
        elif traversal_type == "inorder":
            self.inorder_print(root, "")
        elif traversal_type == "postorder":
            self.postorder_print(root, "")

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.data) + " -> "
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.data) + " -> "
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.data) + " -> "
        return traversal

