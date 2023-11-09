import collections
class Stack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x):
        # While q1 is not empty, enqueue q1.front to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Enqueue the new element to q1
        self.q1.append(x)

        # Swap names of two queues to restore stack properties
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        # If both queues are empty, it means that the stack is empty
        if not self.q1:
            raise Exception('Stack is empty')

        # Dequeue from q1 and return the element
        return self.q1.popleft()

    def top(self):
        # If the stack is empty, raise an exception
        if not self.q1:
            raise Exception('Stack is empty')

        # The front of q1 is the top of the stack
        return self.q1[0]

    def empty(self):
        # The stack is empty if both queues are empty
        return not self.q1
    
    