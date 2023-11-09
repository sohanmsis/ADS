class Stack:
    def __init__(self, capacity):
        self.top = -1
        self.stack = [None]*capacity

    def push(self, data):
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = data
            return True
        return False

    def pop(self):
        if self.top >= 0:
            popped_data = self.stack[self.top]
            self.top -= 1
            return popped_data
        return None

    def peek(self):
        if self.top >= 0:
            return self.stack[self.top]
        return None

    def is_full(self):
        return self.top == len(self.stack) - 1

    def is_empty(self):
        return self.top == -1

# Driver code
if __name__ == "__main__":
    stack = Stack(3)

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Is Full: ", stack.is_full())
    print("Is Empty: ", stack.is_empty())
    print("Top: ", stack.peek())

    stack.pop()
    print("Is Full: ", stack.is_full())
    print("Is Empty: ", stack.is_empty())
    print("Top: ", stack.peek())