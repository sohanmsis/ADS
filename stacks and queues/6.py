class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

# Usage
S = Stack()
T = Stack()

# Push elements onto S
S.push("a")
S.push("b")
S.push("c")

# Transfer elements from S to T
transfer(S, T)

# Pop elements from T and print them
while not T.is_empty():
    print(T.pop())