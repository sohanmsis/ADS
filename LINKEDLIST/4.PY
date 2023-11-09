class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

linked_list = LinkedList()
linked_list.push(20)
linked_list.push(4)
linked_list.push(15)
linked_list.push(85)

print("Original List:")
linked_list.print_list()

linked_list.reverse()

print("Reversed List:")
linked_list.print_list()