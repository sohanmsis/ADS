class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def getHeight(root):
    if root is None:
        return 0
    else:
        lheight = getHeight(root.left)
        rheight = getHeight(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert(root, key)

print("Height of the BST is", getHeight(root))
