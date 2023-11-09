class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def common_elements(list1, list2):
    common_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data == current2.data:
            common_list.add_at_tail(current1.data)
        current1 = current1.next
        current2 = current2.next

    return common_list

# Testing
list1 = LinkedList()
list1.add_at_tail(1)
list1.add_at_tail(2)
list1.add_at_tail(3)
list1.add_at_tail(4)
list1.add_at_tail(5)

list2 = LinkedList()
list2.add_at_tail(3)
list2.add_at_tail(4)
list2.add_at_tail(5)
list2.add_at_tail(6)
list2.add_at_tail(7)

common_list = common_elements(list1, list2)
common_list.print_list()