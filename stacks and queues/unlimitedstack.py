class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = None(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count