class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def enqueue(self, item):
        self.queue.append(item)
        while self.max_queue and self.max_queue[-1] < item:
            self.max_queue.pop()
        self.max_queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "No elements in the Queue!"
        if self.queue[0] == self.max_queue[0]:
            self.max_queue.pop(0)
        return self.queue.pop(0)

    def findMax(self):
        if not self.max_queue:
            return "No elements in the Queue!"
        return self.max_queue[0]

    def size(self):
        return len(self.queue)