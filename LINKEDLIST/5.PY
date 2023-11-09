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

def split(llist):
    if llist.head is None:
        return None

    slow = llist.head
    fast = llist.head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    temp = slow.next
    slow.next = None
    return temp

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(7)
llist.push(8)
llist.push(9)
llist.push(10)

print("Original Linked List:")
llist.print_list()

second_half = split(llist)

print("First half of Linked List:")
llist.print_list()

print("Second half of Linked List:")
temp = LinkedList()
temp.head = second_half
temp.print_list()