import collections
import math

class FlexiQueue:
    def __init__(self, max_size=math.inf):
        self.queue = collections.deque()
        self.max_size = max_size

    def enqueue(self, item):
        if len(self.queue) < self.max_size:
            self.queue.append(item)
        else:
            raise Exception('Queue is full')

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            raise Exception('Queue is empty')

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.max_size