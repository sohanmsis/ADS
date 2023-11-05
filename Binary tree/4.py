class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_terminal_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return count_terminal_nodes(root.left) + count_terminal_nodes(root.right)


# Creating the binary search tree shown in the diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("The number of terminal nodes is", count_terminal_nodes(root))
