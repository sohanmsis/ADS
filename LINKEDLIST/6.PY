class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def is_palindrome(head):
    if head is None or head.next is None:
        return True

    prev = None
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next

        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    while slow is not None:
        if slow.data != head.data:
            return False
        slow = slow.next
        head = head.next

    return True

head = None
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)

if is_palindrome(head):
    print("Given linked list is palindrome")
else:
    print("Given linked list is not palindrome")