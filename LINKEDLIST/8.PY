class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data

# Test the function
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Middle element of linked list is: ", find_middle(head))