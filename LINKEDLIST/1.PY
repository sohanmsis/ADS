class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
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

    def delete_at_head(self):
        if not self.head:
            return
        self.head = self.head.next

    def delete_at_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def add_after_given_data(self, data, new_data):
        current = self.head
        while current:
            if current.data == data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_after_given_data(self, data):
        current = self.head
        while current:
            if current.data == data and current.next:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()