class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if self.elements:
            return self.elements.pop(0)
        else:
            return "No elements in the Queue!"

    def rotate(self):
        reversed_elements = self.elements[::-1]
        self.elements.clear()
        for element in reversed_elements:
            self.enqueue(element)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Original Queue:")
print(queue.elements)

queue.rotate()

print("\nRotated Queue:")
print(queue.elements)